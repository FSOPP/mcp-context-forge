---
title: Feature Architecture v1.0.10 F-001 — MCP Registry and Federation
id: F-001
status: as-built
owner: TBD
updated: 2026-09-20
---

# Feature Architecture v1.0.10 F-001 — MCP Registry and Federation

> As-built. `[D: path:line]` is derived and reopenable, `I:` states its leap, `OPEN:` is a question
> the code cannot answer. Shared conventions live in `architect_common.md`; the system view lives
> in `architect.md`.

## Design summary

This feature is the registry: the catalogue of upstream MCP servers the gateway
federates, and the tools, resources, prompts and roots it discovers from them. A virtual server
composes a subset of those primitives into one endpoint a client can point at.

The surface is CRUD plus discovery. Registration writes a `gateways` row and the gateway then
polls that peer for its primitives [D: mcpgateway/services/gateway_service.py:671]. Tools,
resources and prompts arrive by that discovery, not by direct authoring, and carry both an
`original_name` and a gateway-scoped name [D: mcpgateway/db.py:3305].

Two naming schemes are live at once. `_assemble_routers` mounts the gateway router at `/gateways`
and the server router at `/servers` [D: mcpgateway/api/v1/__init__.py:48], and `build_v1_router`
mounts the same two routers a second time at `/v1/mcp-servers` and `/v1/virtual-servers`
[D: mcpgateway/api/v1/__init__.py:58]. Both names reach the same handlers.

I: the second pair is a rename in progress rather than a distinct API — basis: both mounts pass
the identical router object, so no handler can distinguish them, and the newer names read as the
domain terms the rest of the codebase uses [D: mcpgateway/api/v1/__init__.py:58].

Implementation lives in:

- `mcpgateway/services/gateway_service.py`
- `mcpgateway/services/tool_service.py`
- `mcpgateway/services/resource_service.py`
- `mcpgateway/services/prompt_service.py`
- `mcpgateway/services/server_service.py`
- `mcpgateway/services/root_service.py`
- `mcpgateway/services/export_service.py`
- `mcpgateway/services/import_service.py`
- `mcpgateway/services/tag_service.py`
- `mcpgateway/routers/catalog.py`
- `mcpgateway/routers/search.py`
- `mcpgateway/routers/mcp_servers_router.py`
- `mcpgateway/cache/registry_cache.py`
- `mcpgateway/services/catalog_service.py`
- `mcpgateway/services/grpc_service.py`
- `mcpgateway/translate_grpc.py`
- `mcpgateway/utils/jq_runner.py`
- `mcpgateway/services/import_service.py`

## API contracts

90 route decorators belong to this feature. The readable
contract is `../data/api-contract_v1.0.10_F-001.md`; the machine-readable one is
`../data/schema/openapi_v1.0.10_F-001.json` and `../data/schema/asyncapi_v1.0.10_F-001.json`.

Request and response shapes are not stated in either. The repository ships no OpenAPI document,
and the handlers were not read field by field, so inventing those shapes here would be the one
thing this hub must not do.

## Data model

| table | fields | source |
| --- | --- | --- |
| `gateways` | 51 | [D: mcpgateway/db.py:4710] |
| `tools` | 51 | [D: mcpgateway/db.py:3305] |
| `resources` | 30 | [D: mcpgateway/db.py:3690] |
| `prompts` | 29 | [D: mcpgateway/db.py:4089] |
| `servers` | 24 | [D: mcpgateway/db.py:4424] |
| `resource_subscriptions` | 5 | [D: mcpgateway/db.py:4022] |
| `grpc_services` | 33 | [D: mcpgateway/db.py:5260] |
| `server_tool_association` | 2 | [D: mcpgateway/db.py:2531] |
| `server_resource_association` | 2 | [D: mcpgateway/db.py:2539] |
| `server_prompt_association` | 2 | [D: mcpgateway/db.py:2547] |
| `server_interfaces` | 10 | [D: mcpgateway/db.py:5167] |
| `global_config` | 2 | [D: mcpgateway/db.py:2571] |

12 tables, 241 columns. Full field detail is `../data/schema/schemas.json`; the diagram is `../data/schema/erd_v1.0.10_F-001.puml`.

## Sequence

Registering an upstream gateway, as the handler runs it:

1. The request reaches a `gateway_router` handler, dual-mounted at `/v1/gateways`,
   `/v1/mcp-servers` and `/gateways` [D: mcpgateway/api/v1/__init__.py:48].
2. RBAC evaluates `gateways.create` before the body is used [D: mcpgateway/middleware/rbac.py:921].
3. The target URL is validated against the SSRF rules before any outbound call
   [D: mcpgateway/utils/grpc_validation.py:1].
4. `GatewayService` connects to the peer and reads its capability list
   [D: mcpgateway/services/gateway_service.py:671].
5. Discovered primitives are written as `tools`, `resources` and `prompts` rows, each keeping the
   upstream `original_name` alongside the gateway-scoped name [D: mcpgateway/db.py:3305].
6. The main write commits, and only then does `log_action` open its own session for the audit row
   [D: mcpgateway/services/audit_trail_service.py:73].

OPEN: what happens on a partial discovery — some primitives readable, others not. The failure
branches were not read to that depth.

## Failure modes

- Upstream unreachable at registration: `GatewayConnectionError`
  [D: mcpgateway/services/gateway_service.py:671].
- Credentials rejected by the peer: `GatewayCredentialError` [D: mcpgateway/services/gateway_service.py:671].
- A gateway already registered under the same identity: `GatewayDuplicateConflictError`
  [D: mcpgateway/services/gateway_service.py:671].
- A tool name already taken: `ToolNameConflictError` [D: mcpgateway/services/tool_service.py:1].
- Audit write fails after the main commit: swallowed inside `log_action`, which returns `None`
  [D: mcpgateway/services/audit_trail_service.py:73]. The caller's generic handler still rolls back
  and returns an error, although the row is already committed [D: CLAUDE.md:255].

That last one is worth reading twice: the API reports a failure for a write that succeeded.

## Observability

Execution metrics for this feature's primitives are written to the per-invocation
and hourly tables when `METRICS_ENABLED` style recording is on [D: mcpgateway/config.py:2394].
Traces and spans come from `ObservabilityMiddleware`, which covers every path not on the skip list
[D: mcpgateway/middleware/path_filter.py:33]. Audit rows are written through `log_action` on its
own session [D: mcpgateway/services/audit_trail_service.py:73].

OPEN: which of this feature's operations are expected to be alertable, and on what threshold. No
alert rule or SLO appears in the repository.

## Traceability

- Stories: `../PRDs/prd_v1.0.10_F-001-*.md`
- Tasks: `../tasks/tasks_v1.0.10_F-001.md`
- Tests: `../tests/test_v1.0.10_F-001.md`
- Contract: `../data/api-contract_v1.0.10_F-001.md`

## Open questions

- OPEN: What is the intended lifecycle of a discovered tool whose upstream gateway is deleted? The schema keeps the rows; no code path in the survey deletes them.
- OPEN: Why do `/gateways` and `/mcp-servers` both exist? The rename is visible; the plan and the removal date are not.
- OPEN: What is the expected upper bound on federated gateways per deployment? No limit is configured anywhere.
