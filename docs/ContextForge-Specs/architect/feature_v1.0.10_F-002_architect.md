---
title: Feature Architecture v1.0.10 F-002 — MCP Protocol Serving and Transports
id: F-002
status: as-built
owner: TBD
updated: 2026-09-20
---

# Feature Architecture v1.0.10 F-002 — MCP Protocol Serving and Transports

> As-built. `[D: path:line]` is derived and reopenable, `I:` states its leap, `OPEN:` is a question
> the code cannot answer. Shared conventions live in `architect_common.md`; the system view lives
> in `architect.md`.

## Design summary

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

Implementation lives in:

- `mcpgateway/transports/`
- `mcpgateway/handlers/`
- `mcpgateway/validation/`
- `mcpgateway/cache/session_registry.py`
- `mcpgateway/routers/reverse_proxy.py`
- `mcpgateway/routers/cancellation_router.py`
- `mcpgateway/translate.py`
- `mcpgateway/services/session_affinity.py`
- `mcpgateway/services/upstream_session_registry.py`
- `mcpgateway/utils/internal_http.py`
- `mcpgateway/runtime_state.py`

## API contracts

107 route decorators belong to this feature. The readable
contract is `../data/api-contract_v1.0.10_F-002.md`; the machine-readable one is
`../data/schema/openapi_v1.0.10_F-002.json` and `../data/schema/asyncapi_v1.0.10_F-002.json`.

Request and response shapes are not stated in either. The repository ships no OpenAPI document,
and the handlers were not read field by field, so inventing those shapes here would be the one
thing this hub must not do.

## Data model

| table | fields | source |
| --- | --- | --- |
| `mcp_sessions` | 4 | [D: mcpgateway/db.py:5327] |
| `mcp_messages` | 5 | [D: mcpgateway/db.py:5340] |
| `mcp_app_sessions` | 8 | [D: mcpgateway/db.py:4036] |

3 tables, 17 columns. Full field detail is `../data/schema/schemas.json`; the diagram is `../data/schema/erd_v1.0.10_F-002.puml`.

## Sequence

Serving one JSON-RPC call:

1. A client posts an envelope to `/rpc` or `/mcp` [D: mcpgateway/main.py:8170].
2. The envelope's `method` is matched against 27 literal branches
   [D: mcpgateway/main.py:11542].
3. On `tools/call`, the named tool is resolved and invoked [D: mcpgateway/main.py:11731].
4. On no match, the method name itself is passed to `invoke_tool`
   [D: mcpgateway/main.py:11947]. This is the dynamic-dispatch branch: any registered tool name is
   a valid method.
5. A `JSONRPCError` is raised for an unknown name, invalid params or an internal fault
   [D: mcpgateway/main.py:11818].

The same operations are reachable one-per-route under `/_internal/**`, which the Rust runtime
calls after passing the trust gate [D: mcpgateway/auth_context.py:638].

## Failure modes

- Unknown method and unknown tool: JSON-RPC `-32601` [D: mcpgateway/main.py:11947].
- Malformed params: `-32602` [D: mcpgateway/main.py:11818].
- Feature disabled: `-32601` carrying the setting name that would enable it
  [D: mcpgateway/main.py:11818].
- Internal fault: `-32603` [D: mcpgateway/main.py:11818].
- Client disconnects mid-stream: handled by dedicated middleware rather than by the handler
  [D: mcpgateway/middleware/client_disconnect.py:74].

## Observability

Execution metrics for this feature's primitives are written to the per-invocation
and hourly tables when `METRICS_ENABLED` style recording is on [D: mcpgateway/config.py:2394].
Traces and spans come from `ObservabilityMiddleware`, which covers every path not on the skip list
[D: mcpgateway/middleware/path_filter.py:33]. Audit rows are written through `log_action` on its
own session [D: mcpgateway/services/audit_trail_service.py:73].

OPEN: which of this feature's operations are expected to be alertable, and on what threshold. No
alert rule or SLO appears in the repository.

## Traceability

- Stories: `../PRDs/prd_v1.0.10_F-002-*.md`
- Tasks: `../tasks/tasks_v1.0.10_F-002.md`
- Tests: `../tests/test_v1.0.10_F-002.md`
- Contract: `../data/api-contract_v1.0.10_F-002.md`

## Open questions

- OPEN: What is the complete live operation list? It is the 27 literal JSON-RPC methods plus every row in `tools` — a runtime value this repository cannot state.
- OPEN: Which MCP protocol revision is targeted, and what happens when a client negotiates a different one?
- OPEN: What is the target p95 for `tools/call`? No SLO appears in the repository.
