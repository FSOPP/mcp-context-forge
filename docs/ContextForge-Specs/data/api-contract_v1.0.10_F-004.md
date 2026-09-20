---
title: API Contract v1.0.10 F-004 — Observability, Metrics and Audit
id: F-004
status: as-built
owner: TBD
updated: 2026-09-20
---

# API Contract v1.0.10 F-004 — Observability, Metrics and Audit

> Reversed from code, not written before it. `[D: path:line]` marks a derived fact you can
> reopen; `I:` marks a stated leap; `OPEN:` marks what the code cannot answer.

## Surface summary

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

## Endpoints

| Method | Path | Auth | Source |
| --- | --- | --- | --- |
| GET | `/api/logs/activity` | `audit:read` | [D: mcpgateway/routers/log_search.py:1021] |
| GET | `/api/logs/audit-trails` | `audit:read` | [D: mcpgateway/routers/log_search.py:936] |
| GET | `/api/logs/performance-metrics` | `metrics:read` | [D: mcpgateway/routers/log_search.py:1109] |
| POST | `/api/logs/search` | `logs:read` | [D: mcpgateway/routers/log_search.py:638] |
| GET | `/api/logs/security-events` | `security:read` | [D: mcpgateway/routers/log_search.py:860] |
| GET | `/api/logs/trace/{correlation_id}` | `logs:read` | [D: mcpgateway/routers/log_search.py:747] |
| POST | `/api/metrics/cleanup`, `/v1/api/metrics/cleanup` | **none on the handler** | [D: mcpgateway/routers/metrics_maintenance.py:104] |
| GET | `/api/metrics/config`, `/v1/api/metrics/config` | **none on the handler** | [D: mcpgateway/routers/metrics_maintenance.py:271] |
| POST | `/api/metrics/rollup`, `/v1/api/metrics/rollup` | **none on the handler** | [D: mcpgateway/routers/metrics_maintenance.py:185] |
| GET | `/api/metrics/stats`, `/v1/api/metrics/stats` | **none on the handler** | [D: mcpgateway/routers/metrics_maintenance.py:238] |
| GET | `/compliance/frameworks`, `/v1/compliance/frameworks` | dependency `get_current_user_with_permissions` | [D: mcpgateway/routers/compliance_router.py:124] |
| GET | `/compliance/reports`, `/v1/compliance/reports` | dependency `get_current_user_with_permissions`, `get_db` | [D: mcpgateway/routers/compliance_router.py:187] |
| POST | `/compliance/reports`, `/v1/compliance/reports` | dependency `get_current_user_with_permissions`, `get_db` | [D: mcpgateway/routers/compliance_router.py:143] |
| GET | `/compliance/reports/{report_id}`, `/v1/compliance/reports/{report_id}` | dependency `get_current_user_with_permissions`, `get_db` | [D: mcpgateway/routers/compliance_router.py:228] |
| GET | `/compliance/reports/{report_id}/export`, `/v1/compliance/reports/{report_id}/export` | dependency `get_current_user_with_permissions`, `get_db` | [D: mcpgateway/routers/compliance_router.py:271] |
| GET | `/health` | **none on the handler** | [D: mcpgateway/main.py:12424] |
| GET | `/health/security` | dependency `require_admin_auth` | [D: mcpgateway/main.py:12558] |
| GET | `/healthz` | not extracted | [D: mcpgateway/translate.py:875] |
| POST | `/logging/setLevel` | `admin.system_config` | [D: mcpgateway/main.py:12315] |
| GET | `/metrics`, `/v1/metrics` | `admin.metrics` | [D: mcpgateway/main.py:12343] |
| GET | `/metrics/prometheus` | not extracted | [D: mcpgateway/services/metrics.py:467] |
| POST | `/metrics/reset`, `/v1/metrics/reset` | `admin.metrics` | [D: mcpgateway/main.py:12375] |
| GET | `/observability/analytics/query-performance`, `/v1/observability/analytics/query-performance` | `admin.system_config` | [D: mcpgateway/routers/observability.py:678] |
| GET | `/observability/metrics/percentiles`, `/v1/observability/metrics/percentiles` | `metrics:read` | [D: mcpgateway/routers/observability.py:921] |
| GET | `/observability/metrics/timeseries`, `/v1/observability/metrics/timeseries` | `metrics:read` | [D: mcpgateway/routers/observability.py:883] |
| GET | `/observability/spans`, `/v1/observability/spans` | `admin.system_config` | [D: mcpgateway/routers/observability.py:328] |
| GET | `/observability/stats`, `/v1/observability/stats` | `admin.system_config` | [D: mcpgateway/routers/observability.py:431] |
| GET | `/observability/traces`, `/v1/observability/traces` | `admin.system_config` | [D: mcpgateway/routers/observability.py:77] |
| DELETE | `/observability/traces/cleanup`, `/v1/observability/traces/cleanup` | `admin.system_config` | [D: mcpgateway/routers/observability.py:392] |
| POST | `/observability/traces/export`, `/v1/observability/traces/export` | `admin.system_config` | [D: mcpgateway/routers/observability.py:492] |
| POST | `/observability/traces/query`, `/v1/observability/traces/query` | `admin.system_config` | [D: mcpgateway/routers/observability.py:163] |
| GET | `/observability/traces/{trace_id}`, `/v1/observability/traces/{trace_id}` | `admin.system_config` | [D: mcpgateway/routers/observability.py:278] |
| GET | `/ready` | **none on the handler** | [D: mcpgateway/main.py:12492] |
| GET | `/version` | not extracted | [D: mcpgateway/version.py:1259] |

## Events

No channel literal was found in this feature's files. That is a stated empty answer, not an omission — `schema/asyncapi_v1.0.10_F-004.json` is correspondingly empty.

## Error model

OPEN: this feature's error responses were not read handler by handler. The repository ships no OpenAPI document and no central error table, so the status codes and error body shape are not stated anywhere a reader can check.

## Versioning and compatibility

Two mounts of every core router are live: the canonical `/v1/**` path and an
unversioned legacy shim. `DeprecationHeadersMiddleware` stamps `Sunset`, `Deprecation`, `Link` and
`X-Deprecated-Endpoint` on the shim responses [D: mcpgateway/middleware/deprecation.py:154]. The
shim is excluded from the OpenAPI document, so `/v1` is the documented contract
[D: mcpgateway/api/v1/__init__.py:436].

`_LEGACY_PREFIXES` must be kept in sync with `_assemble_routers` by hand; a unit test fails when
they diverge [D: mcpgateway/middleware/deprecation.py:56].

OPEN: what the Sunset date actually is for this release, and whether any consumer still depends on
the unversioned paths. The date is supplied by the caller that constructs the middleware, not fixed
in the source.

## Spec files

- `schema/openapi_v1.0.10_F-004.json` — every path and method above, each with its `x-source` citation and the mounts it answers on. Request and response schemas are empty by design: nothing in the repository states them.
- `schema/asyncapi_v1.0.10_F-004.json` — channel names only.
- Entity shapes are `$ref`s into `schema/schemas.json`. No shape is redefined here.

## Traceability

Stories in `../PRDs/prd_v1.0.10_F-004-*.md` cite the endpoints above as evidence the behaviour
exists. They do not establish that it was wanted; see that document's own open questions.

## Open questions

- OPEN: What is the retention policy for traces, spans and per-invocation metrics? The tables grow without bound and no code in the survey deletes from them except `delete_old_traces`, whose schedule is not set here.
- OPEN: Is the loss of an audit record acceptable? `log_action` swallows its own exceptions, so a failure is silent by construction.
- OPEN: What is this deployment's actual concurrency, against the 4-6 independent sessions each traced request opens?
