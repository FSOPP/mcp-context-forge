---
title: Feature Architecture v1.0.10 F-006 — LLM Gateway and Chat
id: F-006
status: as-built
owner: TBD
updated: 2026-09-20
---

# Feature Architecture v1.0.10 F-006 — LLM Gateway and Chat

> As-built. `[D: path:line]` is derived and reopenable, `I:` states its leap, `OPEN:` is a question
> the code cannot answer. Shared conventions live in `architect_common.md`; the system view lives
> in `architect.md`.

## Design summary

This feature is a provider-agnostic LLM surface: a registry of providers and models,
a chat endpoint, and a pass-through proxy.

The proxy is mounted differently from everything else in the hub. Its prefix is read from
configuration at startup rather than declared on the router, so it is attached to the application
directly instead of through `_assemble_routers`
[D: mcpgateway/main.py:13187].

I: provider credentials are not held in `llm_providers` in plaintext — basis: the column is
declared with the `EncryptedText` type used elsewhere for secrets [D: mcpgateway/db.py:6504].

Implementation lives in:

- `mcpgateway/routers/llm_config_router.py`
- `mcpgateway/routers/llm_admin_router.py`
- `mcpgateway/routers/llm_proxy_router.py`
- `mcpgateway/routers/llmchat_router.py`
- `mcpgateway/toolops/`

## API contracts

22 route decorators belong to this feature. The readable
contract is `../data/api-contract_v1.0.10_F-006.md`; the machine-readable one is
`../data/schema/openapi_v1.0.10_F-006.json` and `../data/schema/asyncapi_v1.0.10_F-006.json`.

Request and response shapes are not stated in either. The repository ships no OpenAPI document,
and the handlers were not read field by field, so inventing those shapes here would be the one
thing this hub must not do.

## Data model

| table | fields | source |
| --- | --- | --- |
| `llm_providers` | 20 | [D: mcpgateway/db.py:6504] |
| `llm_models` | 16 | [D: mcpgateway/db.py:6587] |

2 tables, 36 columns. Full field detail is `../data/schema/schemas.json`; the diagram is `../data/schema/erd_v1.0.10_F-006.puml`.

## Sequence

OPEN: the proxy request path was not read call by call. What is derived: the proxy
router is attached to the application directly rather than through the shared assembly, and its
prefix comes from `settings.llm_api_prefix` at startup [D: mcpgateway/main.py:13187]. Provider and
model records are ordinary rows [D: mcpgateway/db.py:6504].

## Failure modes

OPEN: the proxy's error branches were not read. No error table is stated here rather than an invented one.

## Observability

Execution metrics for this feature's primitives are written to the per-invocation
and hourly tables when `METRICS_ENABLED` style recording is on [D: mcpgateway/config.py:2394].
Traces and spans come from `ObservabilityMiddleware`, which covers every path not on the skip list
[D: mcpgateway/middleware/path_filter.py:33]. Audit rows are written through `log_action` on its
own session [D: mcpgateway/services/audit_trail_service.py:73].

OPEN: which of this feature's operations are expected to be alertable, and on what threshold. No
alert rule or SLO appears in the repository.

## Traceability

- Stories: `../PRDs/prd_v1.0.10_F-006-*.md`
- Tasks: `../tasks/tasks_v1.0.10_F-006.md`
- Tests: `../tests/test_v1.0.10_F-006.md`
- Contract: `../data/api-contract_v1.0.10_F-006.md`

## Open questions

- OPEN: Which providers are supported in practice, and which are merely representable in `llm_providers`?
- OPEN: What is the cost or rate ceiling on the proxy? No limit is configured.
