---
title: API Contract v1.0.10 F-002 — MCP Protocol Serving and Transports
id: F-002
status: as-built
owner: TBD
updated: 2026-09-20
---

# API Contract v1.0.10 F-002 — MCP Protocol Serving and Transports

> Reversed from code, not written before it. `[D: path:line]` marks a derived fact you can
> reopen; `I:` marks a stated leap; `OPEN:` marks what the code cannot answer.

## Surface summary

This feature serves the MCP protocol itself: session setup, the JSON-RPC message
loop, and the transports that carry it — SSE, WebSocket, streamable HTTP and stdio.

**The route table is not the operation list.** `/rpc` and `/mcp` accept a JSON-RPC envelope and
dispatch on its `method` field through an if/elif chain [D: mcpgateway/main.py:11542]. Twenty-seven
method names are matched literally, and the terminal `else` branch passes the method name to
`tool_service.invoke_tool` [D: mcpgateway/main.py:11947]. Any registered tool name is therefore a
callable operation, and the live operation list is the `tools` table, not this repository.

`/_internal/**` is a second surface for the same operations, one HTTP route per JSON-RPC method
[D: mcpgateway/main.py:8205]. It carries no RBAC decorator. Authorisation is a trust gate instead:
`is_trusted_internal_mcp_request` admits the request only under the internal path prefixes, and
requires an encoded auth context on every route except `*/authenticate`
[D: mcpgateway/auth_context.py:638].

I: `/_internal/**` exists for the Rust runtime rather than for clients — basis: the crate issues
these exact paths [D: crates/mcp_runtime/src/lib.rs:2132], and the gate keys on a runtime-issued auth
context rather than on a user token [D: mcpgateway/auth_context.py:638].

The prefix is not served by one process. `/_internal/event-store/store` and
`/_internal/event-store/replay` are routes on the Rust daemon
[D: crates/mcp_runtime/src/lib.rs:1352] and have no Python handler, while the `/_internal/mcp/**`
routes are Python handlers the daemon calls [D: mcpgateway/main.py:8205]. Traffic runs both ways
across the same prefix.

## Endpoints

107 route decorators, grouped by path. Every row is in `schema/openapi_v1.0.10_F-002.json`, which lists each path and method individually with its source.

| Path group | Routes | Methods | Permissions seen | Example source |
| --- | --- | --- | --- | --- |
| `/_internal/a2a` | 30 | POST | — | [D: mcpgateway/main.py:9973] |
| `/_internal/mcp` | 57 | DELETE, POST | — | [D: mcpgateway/main.py:8122] |
| `/appbridge/sessions` | 2 | POST | `resources.read`, `tools.execute` | [D: mcpgateway/main.py:10663] |
| `/cancellation/cancel` | 1 | POST | `admin.system_config` | [D: mcpgateway/routers/cancellation_router.py:68] |
| `/cancellation/status` | 1 | GET | `admin.system_config` | [D: mcpgateway/routers/cancellation_router.py:110] |
| `/mcp` | 1 | POST | — | [D: mcpgateway/translate.py:2025] |
| `/message` | 1 | POST | `tools.execute` | [D: mcpgateway/main.py:12268] |
| `/protocol/completion` | 1 | POST | — | [D: mcpgateway/main.py:4087] |
| `/protocol/initialize` | 1 | POST | — | [D: mcpgateway/main.py:3992] |
| `/protocol/notifications` | 1 | POST | — | [D: mcpgateway/main.py:4052] |
| `/protocol/ping` | 1 | POST | — | [D: mcpgateway/main.py:4024] |
| `/protocol/sampling` | 1 | POST | — | [D: mcpgateway/main.py:4112] |
| `/reverse-proxy/sessions` | 3 | DELETE, GET, POST | — | [D: mcpgateway/routers/reverse_proxy.py:328] |
| `/reverse-proxy/sse` | 1 | GET | — | [D: mcpgateway/routers/reverse_proxy.py:502] |
| `/reverse-proxy/ws` | 1 | WEBSOCKET | — | [D: mcpgateway/routers/reverse_proxy.py:239] |
| `/rpc` | 2 | POST | — | [D: mcpgateway/main.py:8106] |
| `/sse` | 1 | GET | `servers.use` | [D: mcpgateway/main.py:12161] |
| `/ws` | 1 | WEBSOCKET | — (**1 with none**) | [D: mcpgateway/main.py:12079] |

## Events

| Channel | Kind | Role | Source |
| --- | --- | --- | --- |
| topic `hello` | pubsub transport | consume+produce direction | [D: mcpgateway/translate.py:197] |
| topic `mcp_session_events` | pubsub transport | consume direction | [D: mcpgateway/cache/session_registry.py:503] |
| topic `mcp_session_events` | redis transport | produce direction | [D: mcpgateway/cache/session_registry.py:654] |
| topic `second` | pubsub transport | consume+produce direction | [D: mcpgateway/translate.py:248] |
| topic `test` | pubsub transport | consume+produce direction | [D: mcpgateway/translate.py:234] |

OPEN: payload shape, delivery guarantee and ordering key for each channel. The survey found the topic names; nothing in the repository declares a schema for them.

## Error model

JSON-RPC error objects, not HTTP status codes, on the `/rpc` and `/mcp` surface.
`-32601 Method not found` is raised when a method name matches no branch and no registered tool
[D: mcpgateway/main.py:11947]. `-32602` marks invalid params and `-32603` an internal error
[D: mcpgateway/main.py:11812]. Feature-disabled conditions reuse `-32601` with a `config` key
naming the setting that would enable it [D: mcpgateway/main.py:11818].

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

- `schema/openapi_v1.0.10_F-002.json` — every path and method above, each with its `x-source` citation and the mounts it answers on. Request and response schemas are empty by design: nothing in the repository states them.
- `schema/asyncapi_v1.0.10_F-002.json` — channel names only.
- Entity shapes are `$ref`s into `schema/schemas.json`. No shape is redefined here.

## Traceability

Stories in `../PRDs/prd_v1.0.10_F-002-*.md` cite the endpoints above as evidence the behaviour
exists. They do not establish that it was wanted; see that document's own open questions.

## Open questions

- OPEN: What is the complete live operation list? It is the 27 literal JSON-RPC methods plus every row in `tools` — a runtime value this repository cannot state.
- OPEN: Which MCP protocol revision is targeted, and what happens when a client negotiates a different one?
- OPEN: What is the target p95 for `tools/call`? No SLO appears in the repository.
