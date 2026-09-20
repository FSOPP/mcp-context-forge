---
title: API Contract v1.0.10 F-001 — MCP Registry and Federation
id: F-001
status: as-built
owner: TBD
updated: 2026-09-20
---

# API Contract v1.0.10 F-001 — MCP Registry and Federation

> Reversed from code, not written before it. `[D: path:line]` marks a derived fact you can
> reopen; `I:` marks a stated leap; `OPEN:` marks what the code cannot answer.

## Surface summary

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

## Endpoints

90 route decorators, grouped by path. Every row is in `schema/openapi_v1.0.10_F-001.json`, which lists each path and method individually with its source.

| Path group | Routes | Methods | Permissions seen | Example source |
| --- | --- | --- | --- | --- |
| `/catalog` | 2 | GET, POST | `gateways.create`, `servers.create`, `servers.read` | [D: mcpgateway/routers/catalog.py:27] |
| `/export` | 1 | GET | `admin.export` | [D: mcpgateway/main.py:12711] |
| `/export/selective` | 1 | POST | `admin.export` | [D: mcpgateway/main.py:12803] |
| `/gateways` | 11 | DELETE, GET, POST, PUT | `gateways.create`, `gateways.delete`, `gateways.read`, +1 more | [D: mcpgateway/main.py:7391] |
| `/import` | 1 | POST | `admin.import` | [D: mcpgateway/main.py:12872] |
| `/import/cleanup` | 1 | POST | `admin.import` | [D: mcpgateway/main.py:12992] |
| `/import/status` | 2 | GET | `admin.import` | [D: mcpgateway/main.py:12974] |
| `/mcp-servers/test` | 1 | POST | `gateways.read` | [D: mcpgateway/routers/mcp_servers_router.py:67] |
| `/mcp-servers/test-handshake` | 1 | POST | `gateways.read` | [D: mcpgateway/routers/mcp_servers_router.py:107] |
| `/prompts` | 10 | DELETE, GET, POST, PUT | `prompts.create`, `prompts.delete`, `prompts.read`, +1 more | [D: mcpgateway/main.py:6883] |
| `/resources` | 10 | DELETE, GET, POST, PUT | `resources.create`, `resources.delete`, `resources.read`, +1 more | [D: mcpgateway/main.py:6316] |
| `/resources/subscribe` | 1 | POST | `resources.read` | [D: mcpgateway/main.py:6777] |
| `/resources/templates` | 1 | GET | `resources.read` | [D: mcpgateway/main.py:6200] |
| `/resources/test` | 1 | GET | `resources.read` | [D: mcpgateway/main.py:6498] |
| `/roots` | 7 | DELETE, GET, POST, PUT | `admin.system_config` | [D: mcpgateway/main.py:7837] |
| `/roots/changes` | 1 | GET | `admin.system_config` | [D: mcpgateway/main.py:7926] |
| `/roots/export` | 1 | GET | `admin.system_config` | [D: mcpgateway/main.py:7861] |
| `/search` | 1 | GET | — | [D: mcpgateway/routers/search.py:37] |
| `/servers` | 17 | DELETE, GET, POST, PUT | `servers.create`, `servers.delete`, `servers.read`, +2 more (**1 with none**) | [D: mcpgateway/main.py:4139] |
| `/tags` | 3 | GET | `tags.read` | [D: mcpgateway/main.py:12605] |
| `/tools` | 9 | DELETE, GET, POST, PUT | `tools.create`, `tools.delete`, `tools.read`, +1 more | [D: mcpgateway/main.py:5686] |
| `/tools/generate-schemas-from-openapi` | 1 | POST | `tools.create` | [D: mcpgateway/routers/openapi_schema_router.py:43] |
| `/tools/plugin_bindings` | 5 | DELETE, GET, POST | `tools.manage_plugins`, `tools.read` | [D: mcpgateway/routers/tool_plugin_bindings.py:220] |
| `/tools/preview` | 1 | POST | `tools.preview` | [D: mcpgateway/main.py:5898] |

## Events

No channel literal was found in this feature's files. That is a stated empty answer, not an omission — `schema/asyncapi_v1.0.10_F-001.json` is correspondingly empty.

## Error model

Service-layer exception hierarchies map to HTTP responses. Gateway operations raise
`GatewayError` subclasses — `GatewayConnectionError`, `GatewayCredentialError`,
`GatewayDuplicateConflictError` — and tool operations raise `ToolError` subclasses including
`ToolInvocationError`, `ToolLockConflictError` and `ToolNameConflictError`
[D: mcpgateway/services/gateway_service.py:671].

OPEN: which HTTP status each exception class produces. The mapping was not read handler by handler,
and no repository-wide error table states it.

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

- `schema/openapi_v1.0.10_F-001.json` — every path and method above, each with its `x-source` citation and the mounts it answers on. Request and response schemas are empty by design: nothing in the repository states them.
- `schema/asyncapi_v1.0.10_F-001.json` — channel names only.
- Entity shapes are `$ref`s into `schema/schemas.json`. No shape is redefined here.

## Traceability

Stories in `../PRDs/prd_v1.0.10_F-001-*.md` cite the endpoints above as evidence the behaviour
exists. They do not establish that it was wanted; see that document's own open questions.

## Open questions

- OPEN: What is the intended lifecycle of a discovered tool whose upstream gateway is deleted? The schema keeps the rows; no code path in the survey deletes them.
- OPEN: Why do `/gateways` and `/mcp-servers` both exist? The rename is visible; the plan and the removal date are not.
- OPEN: What is the expected upper bound on federated gateways per deployment? No limit is configured anywhere.
