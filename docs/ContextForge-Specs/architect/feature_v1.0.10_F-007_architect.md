---
title: Feature Architecture v1.0.10 F-007 — Plugin Framework and Tool Operations
id: F-007
status: as-built
owner: TBD
updated: 2026-09-20
---

# Feature Architecture v1.0.10 F-007 — Plugin Framework and Tool Operations

> As-built. `[D: path:line]` is derived and reopenable, `I:` states its leap, `OPEN:` is a question
> the code cannot answer. Shared conventions live in `architect_common.md`; the system view lives
> in `architect.md`.

## Design summary

This feature is the in-process plugin framework: discovery, lifecycle, hook
dispatch, and the bindings that attach a plugin to a specific tool or A2A agent.

The framework itself is not in this repository. `settings.plugins` proxies to
`cpex.framework.settings` [D: mcpgateway/config.py:4178], and `cpex` is pinned to an exact version
[D: pyproject.toml:74] with a resolver cut-off date alongside it [D: pyproject.toml:20].
`PLUGINS_ENABLED` and `PLUGINS_CONFIG_FILE` are therefore read by that package, not by
`mcpgateway/config.py`.

Plugins are configured by file, not by API: the HTTP surface here is the catalogue and the binding
tables, not a management API [D: mcpgateway/routers/plugins.py:26].

I: the plugin contract is treated as unstable — basis: the dependency carries both an exact
version pin [D: pyproject.toml:74] and a resolver cut-off date [D: pyproject.toml:20], where a
range would do for a stable one.

OPEN: what `cpex` guarantees across a version bump. This repository holds no copy of that
contract.

Implementation lives in:

- `mcpgateway/plugins/`
- `mcpgateway/routers/plugins.py`
- `mcpgateway/routers/tool_plugin_bindings.py`
- `mcpgateway/routers/toolops_router.py`

## API contracts

4 route decorators belong to this feature. The readable
contract is `../data/api-contract_v1.0.10_F-007.md`; the machine-readable one is
`../data/schema/openapi_v1.0.10_F-007.json` and `../data/schema/asyncapi_v1.0.10_F-007.json`.

Request and response shapes are not stated in either. The repository ships no OpenAPI document,
and the handlers were not read field by field, so inventing those shapes here would be the one
thing this hub must not do.

## Data model

| table | fields | source |
| --- | --- | --- |
| `tool_plugin_bindings` | 13 | [D: mcpgateway/db.py:6929] |
| `toolops_test_cases` | 3 | [D: mcpgateway/db.py:4064] |

2 tables, 16 columns. Full field detail is `../data/schema/schemas.json`; the diagram is `../data/schema/erd_v1.0.10_F-007.puml`.

## Sequence

Hook dispatch happens inside `cpex`, not in this repository
[D: mcpgateway/config.py:4178]. What this repository contributes is the binding tables that say
which plugin applies to which tool or agent [D: mcpgateway/db.py:6929], and four routes that read
them [D: mcpgateway/routers/plugins.py:26].

OPEN: the hook call order and the failure policy. Both are decisions of the external package.

## Failure modes

OPEN: hook failure policy belongs to `cpex` [D: mcpgateway/config.py:4178] and is not in this repository.

## Observability

Execution metrics for this feature's primitives are written to the per-invocation
and hourly tables when `METRICS_ENABLED` style recording is on [D: mcpgateway/config.py:2394].
Traces and spans come from `ObservabilityMiddleware`, which covers every path not on the skip list
[D: mcpgateway/middleware/path_filter.py:33]. Audit rows are written through `log_action` on its
own session [D: mcpgateway/services/audit_trail_service.py:73].

OPEN: which of this feature's operations are expected to be alertable, and on what threshold. No
alert rule or SLO appears in the repository.

## Traceability

- Stories: `../PRDs/prd_v1.0.10_F-007-*.md`
- Tasks: `../tasks/tasks_v1.0.10_F-007.md`
- Tests: `../tests/test_v1.0.10_F-007.md`
- Contract: `../data/api-contract_v1.0.10_F-007.md`

## Open questions

- OPEN: What is the failure policy when a plugin hook raises? Whether the request fails or the plugin is skipped is a decision the framework makes and the documentation does not state.
- OPEN: Why is the framework off by default?
