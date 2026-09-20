---
title: Feature Architecture v1.0.10 F-010 — Bundled MCP Servers and Templates
id: F-010
status: as-built
owner: TBD
updated: 2026-09-20
---

# Feature Architecture v1.0.10 F-010 — Bundled MCP Servers and Templates

> As-built. `[D: path:line]` is derived and reopenable, `I:` states its leap, `OPEN:` is a question
> the code cannot answer. Shared conventions live in `architect_common.md`; the system view lives
> in `architect.md`.

## Design summary

This feature is the bundled MCP servers and the templates that generate new ones —
six Python servers under `mcp-servers/python/` and cookiecutter scaffolds for Go and Python.

They are separate products that happen to share the repository. Each carries its own manifest and
version [D: mcp-servers/python/data_analysis_server/pyproject.toml:3], and the gateway does not
import them; it federates them over MCP like any third-party peer.

Only `mcp_eval_server` exposes an HTTP surface of its own [D:
mcp-servers/python/mcp_eval_server/mcp_eval_server/rest_server.py:68].

Implementation lives in:

- `mcp-servers/`

## API contracts

0 route decorators belong to this feature. The readable
contract is `../data/api-contract_v1.0.10_F-010.md`; the machine-readable one is
`../data/schema/openapi_v1.0.10_F-010.json` and `../data/schema/asyncapi_v1.0.10_F-010.json`.

Request and response shapes are not stated in either. The repository ships no OpenAPI document,
and the handlers were not read field by field, so inventing those shapes here would be the one
thing this hub must not do.

## Data model

| table | fields | source |
| --- | --- | --- |
| — | — | this feature owns no table |

`../data/schema/erd_v1.0.10_F-010.puml` is deliberately empty and says so on its face.

## Sequence

Each bundled server runs as its own process and speaks MCP. The gateway reaches
them the way it reaches any third-party peer, through F-001's registration
[D: mcpgateway/services/gateway_service.py:671].

`mcp_eval_server` additionally runs a FastAPI application of its own
[D: mcp-servers/python/mcp_eval_server/mcp_eval_server/rest_server.py:68].

OPEN: whether the bundled servers are started by the deployment or left to the operator.

## Failure modes

OPEN: each bundled server has its own error handling, none of which was read.

## Observability

Execution metrics for this feature's primitives are written to the per-invocation
and hourly tables when `METRICS_ENABLED` style recording is on [D: mcpgateway/config.py:2394].
Traces and spans come from `ObservabilityMiddleware`, which covers every path not on the skip list
[D: mcpgateway/middleware/path_filter.py:33]. Audit rows are written through `log_action` on its
own session [D: mcpgateway/services/audit_trail_service.py:73].

OPEN: which of this feature's operations are expected to be alertable, and on what threshold. No
alert rule or SLO appears in the repository.

## Traceability

- Stories: `../PRDs/prd_v1.0.10_F-010-*.md`
- Tasks: `../tasks/tasks_v1.0.10_F-010.md`
- Tests: `../tests/test_v1.0.10_F-010.md`
- Contract: `../data/api-contract_v1.0.10_F-010.md`

## Open questions

- OPEN: Are the bundled servers products, reference implementations, or test fixtures? All three readings fit the tree.
- OPEN: Which gateway versions is each bundled server tested against?
