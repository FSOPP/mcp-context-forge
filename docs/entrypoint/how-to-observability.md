---
title: How to Observe — ContextForge
status: as-built
owner: TBD
updated: 2026-09-20
---

# How to Observe — ContextForge

> Reversed from the instrumentation that exists. The design and its trade-off are
> `../ContextForge-Specs/architect/feature_v1.0.10_F-004_architect.md` and ADR-0003.

## Signals

| Signal | Where it lands | Source |
| --- | --- | --- |
| Traces and spans | `observability_traces`, `observability_spans` | [D: mcpgateway/db.py:2896] |
| Execution metrics | per-invocation and hourly tables, one pair per primitive | [D: mcpgateway/db.py:2592] |
| Structured logs | `structured_log_entries` | [D: mcpgateway/db.py:6162] |
| Security events | `security_events` | [D: mcpgateway/db.py:6279] |
| Audit trail | `audit_trails` | [D: mcpgateway/db.py:6645] |
| Prometheus / OTLP | exporters behind `OBSERVABILITY_ENABLED` | [D: mcpgateway/config.py:4037] |

Everything is off by default: `OBSERVABILITY_ENABLED`, `STRUCTURED_LOGGING_DATABASE_ENABLED` and
audit trail logging each default to false [D: CLAUDE.md:296].

## Required instrumentation

**Observability writes do not join the request transaction.** Each write opens its own
`SessionLocal()` and commits immediately [D: mcpgateway/services/observability_service.py:228].
Two consequences you must plan for:

- A traced request opens four to six database connections, not one. Size the pool accordingly
  [D: mcpgateway/config.py:3661]; the symptom of getting it wrong is `QueuePool limit exceeded`.
- An audit write can fail without anyone noticing: `log_action` catches its own exceptions and
  returns `None` [D: mcpgateway/services/audit_trail_service.py:73].

Never pass a request-scoped session into `log_action` [D: CLAUDE.md:256].

## Dashboards and alerts

Four observability back-ends are wired in compose — Phoenix twice, Langfuse, and an OpenSearch
SIEM [D: docker-compose.siem-opensearch.yml:1].

OPEN: which one is intended, and what does a dashboard for this system show? No dashboard
definition and no alert rule appears anywhere in the repository.

## Debug playbook

| Symptom | First place to look | Source |
| --- | --- | --- |
| `QueuePool limit exceeded` | pool size against traced-request concurrency | [D: mcpgateway/config.py:3661] |
| `This transaction is inactive` | a caller passing its own session to `log_action` | [D: CLAUDE.md:256] |
| A trace shows "in progress" | the request failed after the trace started; that is the design | [D: mcpgateway/services/observability_service.py:228] |
| Intermittent `403 CSRF_TOKEN_INVALID` | `CSRF_COOKIE_NAME` or `CSRF_TOKEN_NAME` overridden | [D: mcpgateway/config.py:1801] |
| A path produces no telemetry | the middleware skip list | [D: mcpgateway/middleware/path_filter.py:33] |

## Open questions

- OPEN: what is the retention policy? No table declares one, and only traces have a delete path.
- OPEN: is losing an audit record acceptable? The code makes that loss silent by construction.
- OPEN: do the Rust runtime's traces join the Python side's tree, or form a separate one?
  [D: crates/mcp_runtime/src/observability.rs:1]
