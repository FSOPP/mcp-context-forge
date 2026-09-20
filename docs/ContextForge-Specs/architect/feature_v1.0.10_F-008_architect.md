---
title: Feature Architecture v1.0.10 F-008 — Admin Console
id: F-008
status: as-built
owner: TBD
updated: 2026-09-20
---

# Feature Architecture v1.0.10 F-008 — Admin Console

> As-built. `[D: path:line]` is derived and reopenable, `I:` states its leap, `OPEN:` is a question
> the code cannot answer. Shared conventions live in `architect_common.md`; the system view lives
> in `architect.md`.

## Design summary

This feature is the Admin Console: a server-rendered UI plus the 217 routes behind
it. Its routes mirror the domain features rather than adding capability — `/admin/tools` and
`/tools` reach the same services.

It is one shipping artefact for three reasons the code states. It is feature-flagged as a unit by
`MCPGATEWAY_ADMIN_API_ENABLED` [D: mcpgateway/api/v1/__init__.py:275]. Every route on it carries a
CSRF dependency declared once on the router [D: mcpgateway/admin.py:1889]. And 118 of its routes
share the single permission `admin.system_config` [D: mcpgateway/admin.py:1889].

The CSRF placement is load-bearing: `/admin` is listed in `csrf_exempt_paths`, so the router-level
dependency is the only CSRF control these routes get on the legacy mount
[D: mcpgateway/api/v1/__init__.py:298].

Implementation lives in:

- `mcpgateway/admin.py`
- `mcpgateway/admin_ui/`
- `mcpgateway/routers/runtime_admin_router.py`

## API contracts

231 route decorators belong to this feature. The readable
contract is `../data/api-contract_v1.0.10_F-008.md`; the machine-readable one is
`../data/schema/openapi_v1.0.10_F-008.json` and `../data/schema/asyncapi_v1.0.10_F-008.json`.

Request and response shapes are not stated in either. The repository ships no OpenAPI document,
and the handlers were not read field by field, so inventing those shapes here would be the one
thing this hub must not do.

## Data model

| table | fields | source |
| --- | --- | --- |
| — | — | this feature owns no table |

`../data/schema/erd_v1.0.10_F-008.puml` is deliberately empty and says so on its face.

## Sequence

Serving one console route:

1. The request arrives under `/admin`, which `CSRFMiddleware` skips
   [D: mcpgateway/api/v1/__init__.py:298].
2. The router-level `enforce_admin_csrf` dependency runs instead, comparing the submitted token
   against the cookie with `secrets.compare_digest` and raising 403 on mismatch
   [D: mcpgateway/admin.py:1886].
3. RBAC runs on the handler [D: mcpgateway/middleware/rbac.py:921].
4. The handler delegates to the same service the matching `/v1` route uses, then renders a
   template or returns JSON [D: mcpgateway/admin.py:1889].

## Failure modes

- CSRF token missing or mismatched: 403 [D: mcpgateway/admin.py:1886].
- Admin API disabled: the whole router is absent, so every path 404s
  [D: mcpgateway/api/v1/__init__.py:275].

## Observability

Execution metrics for this feature's primitives are written to the per-invocation
and hourly tables when `METRICS_ENABLED` style recording is on [D: mcpgateway/config.py:2394].
Traces and spans come from `ObservabilityMiddleware`, which covers every path not on the skip list
[D: mcpgateway/middleware/path_filter.py:33]. Audit rows are written through `log_action` on its
own session [D: mcpgateway/services/audit_trail_service.py:73].

OPEN: which of this feature's operations are expected to be alertable, and on what threshold. No
alert rule or SLO appears in the repository.

## Traceability

- Stories: `../PRDs/prd_v1.0.10_F-008-*.md`
- Tasks: `../tasks/tasks_v1.0.10_F-008.md`
- Tests: `../tests/test_v1.0.10_F-008.md`
- Contract: `../data/api-contract_v1.0.10_F-008.md`

## Open questions

- OPEN: Is the Admin Console intended to stay at parity with the domain APIs, or is it a superset that will diverge?
- OPEN: Why do 118 routes share `admin.system_config`? That permission is doing the work of a role rather than a permission.
- OPEN: Who is the intended operator — a platform administrator, or a team administrator with narrower scope?
