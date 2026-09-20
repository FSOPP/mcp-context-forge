---
title: Feature Architecture v1.0.10 F-004 — Observability, Metrics and Audit
id: F-004
status: as-built
owner: TBD
updated: 2026-09-20
---

# Feature Architecture v1.0.10 F-004 — Observability, Metrics and Audit

> As-built. `[D: path:line]` is derived and reopenable, `I:` states its leap, `OPEN:` is a question
> the code cannot answer. Shared conventions live in `architect_common.md`; the system view lives
> in `architect.md`.

## Design summary

This feature records what happened: traces and spans, per-entity execution metrics,
structured logs, security events and the audit trail.

Its defining property is that it does not share the request's transaction. Write operations open
their own `SessionLocal()` and commit immediately, so observability survives a failed request
[D: mcpgateway/services/observability_service.py:228]. `AuditTrailService.log_action` does the same
and swallows its own exceptions [D: mcpgateway/services/audit_trail_service.py:73]. Query
operations take the request-scoped session instead [D: mcpgateway/services/observability_service.py:228].

I: the split is drawn on RBAC — basis: the query methods accept a `db: Session` parameter and the
write methods do not, and only the query path filters rows by token scope
[D: mcpgateway/services/observability_service.py:228].

Metrics are stored twice: a per-invocation row and an hourly rollup, one pair per primitive type
[D: mcpgateway/db.py:2592].

I: the hourly tables are a read-path optimisation rather than a retention tier — basis: they carry
the same measures as the per-invocation tables and no code deletes the per-invocation rows when a
rollup is written [D: mcpgateway/db.py:2742].

Implementation lives in:

- `mcpgateway/services/observability_service.py`
- `mcpgateway/services/audit_trail_service.py`
- `mcpgateway/services/metrics.py`
- `mcpgateway/routers/observability.py`
- `mcpgateway/routers/compliance_router.py`
- `mcpgateway/routers/siem.py`
- `mcpgateway/routers/log_search.py`
- `mcpgateway/routers/metrics_maintenance.py`
- `mcpgateway/middleware/`
- `mcpgateway/instrumentation/`
- `mcpgateway/services/notification_service.py`
- `mcpgateway/version.py`

## API contracts

34 route decorators belong to this feature. The readable
contract is `../data/api-contract_v1.0.10_F-004.md`; the machine-readable one is
`../data/schema/openapi_v1.0.10_F-004.json` and `../data/schema/asyncapi_v1.0.10_F-004.json`.

Request and response shapes are not stated in either. The repository ships no OpenAPI document,
and the handlers were not read field by field, so inventing those shapes here would be the one
thing this hub must not do.

## Data model

| table | fields | source |
| --- | --- | --- |
| `observability_traces` | 16 | [D: mcpgateway/db.py:2896] |
| `observability_spans` | 15 | [D: mcpgateway/db.py:2963] |
| `observability_events` | 11 | [D: mcpgateway/db.py:3028] |
| `observability_metrics` | 11 | [D: mcpgateway/db.py:3085] |
| `observability_saved_queries` | 10 | [D: mcpgateway/db.py:3138] |
| `tool_metrics` | 6 | [D: mcpgateway/db.py:2592] |
| `resource_metrics` | 6 | [D: mcpgateway/db.py:2618] |
| `server_metrics` | 6 | [D: mcpgateway/db.py:2644] |
| `prompt_metrics` | 6 | [D: mcpgateway/db.py:2670] |
| `tool_metrics_hourly` | 14 | [D: mcpgateway/db.py:2742] |
| `resource_metrics_hourly` | 14 | [D: mcpgateway/db.py:2767] |
| `prompt_metrics_hourly` | 14 | [D: mcpgateway/db.py:2792] |
| `server_metrics_hourly` | 14 | [D: mcpgateway/db.py:2817] |
| `performance_snapshots` | 6 | [D: mcpgateway/db.py:3189] |
| `performance_aggregates` | 17 | [D: mcpgateway/db.py:3230] |
| `performance_metrics` | 17 | [D: mcpgateway/db.py:6232] |
| `structured_log_entries` | 29 | [D: mcpgateway/db.py:6162] |
| `security_events` | 25 | [D: mcpgateway/db.py:6279] |
| `audit_trails` | 26 | [D: mcpgateway/db.py:6645] |
| `migration_metadata` | 4 | [D: mcpgateway/db.py:1156] |

20 tables, 267 columns. Full field detail is `../data/schema/schemas.json`; the diagram is `../data/schema/erd_v1.0.10_F-004.puml`.

## Sequence

Recording one traced request:

1. `ObservabilityMiddleware` starts a trace. It does not put a session on `request.state`
   [D: mcpgateway/services/observability_service.py:228].
2. Each write — trace start and end, span start and end, metrics, events — opens its own
   `SessionLocal()` and commits immediately [D: mcpgateway/services/observability_service.py:228].
3. The request proceeds. If it fails, the observability rows already written stay written.
4. Query endpoints use the request-scoped session instead, so RBAC and token scoping apply to
   reads [D: mcpgateway/services/observability_service.py:228].

I: a traced request costs four to six connections rather than one — basis: each of the listed write
points opens its own session and none of them shares
[D: mcpgateway/services/observability_service.py:228].

## Failure modes

- Any observability write fails: the request is unaffected, since the session is not
  shared [D: mcpgateway/services/observability_service.py:228].
- An audit write fails: swallowed, returns `None`, nothing is raised
  [D: mcpgateway/services/audit_trail_service.py:73].
- Connection pool exhausted: surfaces as `QueuePool limit exceeded`, made likelier by the several
  independent sessions per traced request [D: mcpgateway/config.py:3661].

I: audit loss is silent by design rather than by accident — basis: the exception is caught inside
`log_action` and converted to a `None` return rather than re-raised
[D: mcpgateway/services/audit_trail_service.py:73].

## Observability

This feature is the observability implementation, so its own instrumentation is the
thing being described above rather than a separate concern.

Health is exposed at `/health` and `/ready`, both excluded from the middleware skip list handling
so they stay cheap [D: mcpgateway/middleware/path_filter.py:33].

OPEN: what monitors these endpoints in production, and what it does when they fail.

## Traceability

- Stories: `../PRDs/prd_v1.0.10_F-004-*.md`
- Tasks: `../tasks/tasks_v1.0.10_F-004.md`
- Tests: `../tests/test_v1.0.10_F-004.md`
- Contract: `../data/api-contract_v1.0.10_F-004.md`

## Open questions

- OPEN: What is the retention policy for traces, spans and per-invocation metrics? The tables grow without bound and no code in the survey deletes from them except `delete_old_traces`, whose schedule is not set here.
- OPEN: Is the loss of an audit record acceptable? `log_action` swallows its own exceptions, so a failure is silent by construction.
- OPEN: What is this deployment's actual concurrency, against the 4-6 independent sessions each traced request opens?
