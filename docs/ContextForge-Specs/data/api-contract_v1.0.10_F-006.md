---
title: API Contract v1.0.10 F-006 — LLM Gateway and Chat
id: F-006
status: as-built
owner: TBD
updated: 2026-09-20
---

# API Contract v1.0.10 F-006 — LLM Gateway and Chat

> Reversed from code, not written before it. `[D: path:line]` marks a derived fact you can
> reopen; `I:` marks a stated leap; `OPEN:` marks what the code cannot answer.

## Surface summary

This feature is a provider-agnostic LLM surface: a registry of providers and models,
a chat endpoint, and a pass-through proxy.

The proxy is mounted differently from everything else in the hub. Its prefix is read from
configuration at startup rather than declared on the router, so it is attached to the application
directly instead of through `_assemble_routers`
[D: mcpgateway/main.py:13187].

I: provider credentials are not held in `llm_providers` in plaintext — basis: the column is
declared with the `EncryptedText` type used elsewhere for secrets [D: mcpgateway/db.py:6504].

## Endpoints

| Method | Path | Auth | Source |
| --- | --- | --- | --- |
| POST | `/chat/completions` | `llm.invoke` | [D: mcpgateway/routers/llm_proxy_router.py:43] |
| GET | `/llm/gateway/models`, `/v1/llm/gateway/models` | dependency `get_current_user`, `get_db` | [D: mcpgateway/routers/llm_config_router.py:596] |
| GET | `/llm/models`, `/v1/llm/models` | `admin.system_config` | [D: mcpgateway/routers/llm_config_router.py:385] |
| POST | `/llm/models`, `/v1/llm/models` | `admin.system_config` | [D: mcpgateway/routers/llm_config_router.py:346] |
| DELETE | `/llm/models/{model_id}`, `/v1/llm/models/{model_id}` | `admin.system_config` | [D: mcpgateway/routers/llm_config_router.py:520] |
| GET | `/llm/models/{model_id}`, `/v1/llm/models/{model_id}` | `admin.system_config` | [D: mcpgateway/routers/llm_config_router.py:440] |
| PATCH | `/llm/models/{model_id}`, `/v1/llm/models/{model_id}` | `admin.system_config` | [D: mcpgateway/routers/llm_config_router.py:479] |
| POST | `/llm/models/{model_id}/state`, `/v1/llm/models/{model_id}/state` | `admin.system_config` | [D: mcpgateway/routers/llm_config_router.py:550] |
| GET | `/llm/providers`, `/v1/llm/providers` | `admin.system_config` | [D: mcpgateway/routers/llm_config_router.py:110] |
| POST | `/llm/providers`, `/v1/llm/providers` | `admin.system_config` | [D: mcpgateway/routers/llm_config_router.py:61] |
| DELETE | `/llm/providers/{provider_id}`, `/v1/llm/providers/{provider_id}` | `admin.system_config` | [D: mcpgateway/routers/llm_config_router.py:239] |
| GET | `/llm/providers/{provider_id}`, `/v1/llm/providers/{provider_id}` | `admin.system_config` | [D: mcpgateway/routers/llm_config_router.py:156] |
| PATCH | `/llm/providers/{provider_id}`, `/v1/llm/providers/{provider_id}` | `admin.system_config` | [D: mcpgateway/routers/llm_config_router.py:192] |
| POST | `/llm/providers/{provider_id}/health`, `/v1/llm/providers/{provider_id}/health` | `admin.system_config` | [D: mcpgateway/routers/llm_config_router.py:307] |
| POST | `/llm/providers/{provider_id}/state`, `/v1/llm/providers/{provider_id}/state` | `admin.system_config` | [D: mcpgateway/routers/llm_config_router.py:269] |
| POST | `/llmchat/chat`, `/v1/llmchat/chat` | `llm.invoke` | [D: mcpgateway/routers/llmchat_router.py:1287] |
| GET | `/llmchat/config/{user_id}`, `/v1/llmchat/config/{user_id}` | `llm.read` | [D: mcpgateway/routers/llmchat_router.py:1575] |
| POST | `/llmchat/connect`, `/v1/llmchat/connect` | `llm.invoke` | [D: mcpgateway/routers/llmchat_router.py:1011] |
| POST | `/llmchat/disconnect`, `/v1/llmchat/disconnect` | `llm.invoke` | [D: mcpgateway/routers/llmchat_router.py:1412] |
| GET | `/llmchat/gateway/models`, `/v1/llmchat/gateway/models` | `llm.read` | [D: mcpgateway/routers/llmchat_router.py:1636] |
| GET | `/llmchat/status/{user_id}`, `/v1/llmchat/status/{user_id}` | `llm.read` | [D: mcpgateway/routers/llmchat_router.py:1524] |
| GET | `/models` | `llm.read` | [D: mcpgateway/routers/llm_proxy_router.py:133] |

## Events

No channel literal was found in this feature's files. That is a stated empty answer, not an omission — `schema/asyncapi_v1.0.10_F-006.json` is correspondingly empty.

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

- `schema/openapi_v1.0.10_F-006.json` — every path and method above, each with its `x-source` citation and the mounts it answers on. Request and response schemas are empty by design: nothing in the repository states them.
- `schema/asyncapi_v1.0.10_F-006.json` — channel names only.
- Entity shapes are `$ref`s into `schema/schemas.json`. No shape is redefined here.

## Traceability

Stories in `../PRDs/prd_v1.0.10_F-006-*.md` cite the endpoints above as evidence the behaviour
exists. They do not establish that it was wanted; see that document's own open questions.

## Open questions

- OPEN: Which providers are supported in practice, and which are merely representable in `llm_providers`?
- OPEN: What is the cost or rate ceiling on the proxy? No limit is configured.
