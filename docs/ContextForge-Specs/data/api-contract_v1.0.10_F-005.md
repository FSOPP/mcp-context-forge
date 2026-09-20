---
title: API Contract v1.0.10 F-005 — A2A Agent Federation
id: F-005
status: as-built
owner: TBD
updated: 2026-09-20
---

# API Contract v1.0.10 F-005 — A2A Agent Federation

> Reversed from code, not written before it. `[D: path:line]` marks a derived fact you can
> reopen; `I:` marks a stated leap; `OPEN:` marks what the code cannot answer.

## Surface summary

This feature federates A2A agents the way F-001 federates MCP servers: an agent is
registered, its card is fetched, and its tasks are tracked through their lifecycle.

The surface is doubled the same way F-002's is — a public `/a2a` router and a matching
`/_internal/a2a/**` set for the Rust runtime, gated by the same trust predicate and additionally
disabled outright when A2A is off [D: mcpgateway/auth_context.py:654].

Cross-gateway routing is fail-closed. An empty `UAID_ALLOWED_DOMAINS` blocks every cross-gateway
call unless `UAID_ALLOW_ALL_DOMAINS` is set [D: mcpgateway/config.py:907].

## Endpoints

| Method | Path | Auth | Source |
| --- | --- | --- | --- |
| GET | `/a2a`, `/v1/a2a` | `a2a.read` | [D: mcpgateway/main.py:4890] |
| POST | `/a2a`, `/v1/a2a` | `a2a.create` | [D: mcpgateway/main.py:5011] |
| DELETE | `/v1/a2a-agents/plugin-bindings` | `tools.manage_plugins` | [D: mcpgateway/routers/a2a_agent_plugin_bindings.py:224] |
| GET | `/v1/a2a-agents/plugin-bindings` | `tools.read` | [D: mcpgateway/routers/a2a_agent_plugin_bindings.py:146] |
| POST | `/v1/a2a-agents/plugin-bindings` | `tools.manage_plugins` | [D: mcpgateway/routers/a2a_agent_plugin_bindings.py:80] |
| DELETE | `/v1/a2a-agents/plugin-bindings/{binding_id}` | `tools.manage_plugins` | [D: mcpgateway/routers/a2a_agent_plugin_bindings.py:267] |
| GET | `/v1/a2a-agents/plugin-bindings/{team_id}` | `tools.read` | [D: mcpgateway/routers/a2a_agent_plugin_bindings.py:184] |
| GET | `/a2a/`, `/v1/a2a/` | `a2a.read` | [D: mcpgateway/main.py:4891] |
| POST | `/a2a/`, `/v1/a2a/` | `a2a.create` | [D: mcpgateway/main.py:5012] |
| POST | `/a2a/invoke`, `/v1/a2a/invoke` | `a2a.invoke` | [D: mcpgateway/main.py:5406] |
| DELETE | `/a2a/{agent_id}`, `/v1/a2a/{agent_id}` | `a2a.delete` | [D: mcpgateway/main.py:5220] |
| GET | `/a2a/{agent_id}`, `/v1/a2a/{agent_id}` | `a2a.read` | [D: mcpgateway/main.py:4970] |
| PUT | `/a2a/{agent_id}`, `/v1/a2a/{agent_id}` | `a2a.update` | [D: mcpgateway/main.py:5098] |
| POST | `/a2a/{agent_id}/state`, `/v1/a2a/{agent_id}/state` | `a2a.update` | [D: mcpgateway/main.py:5157] |
| POST | `/a2a/{agent_id}/toggle`, `/v1/a2a/{agent_id}/toggle` | `a2a.update` | [D: mcpgateway/main.py:5194] |
| POST | `/a2a/{agent_name}/invoke`, `/v1/a2a/{agent_name}/invoke` | `a2a.invoke` | [D: mcpgateway/main.py:5358] |
| POST | `/a2a/{agent_name}/jsonrpc`, `/v1/a2a/{agent_name}/jsonrpc` | `a2a.invoke` | [D: mcpgateway/main.py:5459] |

## Events

No channel literal was found in this feature's files. That is a stated empty answer, not an omission — `schema/asyncapi_v1.0.10_F-005.json` is correspondingly empty.

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

- `schema/openapi_v1.0.10_F-005.json` — every path and method above, each with its `x-source` citation and the mounts it answers on. Request and response schemas are empty by design: nothing in the repository states them.
- `schema/asyncapi_v1.0.10_F-005.json` — channel names only.
- Entity shapes are `$ref`s into `schema/schemas.json`. No shape is redefined here.

## Traceability

Stories in `../PRDs/prd_v1.0.10_F-005-*.md` cite the endpoints above as evidence the behaviour
exists. They do not establish that it was wanted; see that document's own open questions.

## Open questions

- OPEN: What is the trust model for a remote gateway in a cross-gateway call? Both sides must trust the same JWT issuer, and nothing states how that is established operationally.
- OPEN: What happens to an in-flight A2A task when its agent is deregistered?
