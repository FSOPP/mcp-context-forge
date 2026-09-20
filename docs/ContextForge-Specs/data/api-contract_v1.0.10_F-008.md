---
title: API Contract v1.0.10 F-008 — Admin Console
id: F-008
status: as-built
owner: TBD
updated: 2026-09-20
---

# API Contract v1.0.10 F-008 — Admin Console

> Reversed from code, not written before it. `[D: path:line]` marks a derived fact you can
> reopen; `I:` marks a stated leap; `OPEN:` marks what the code cannot answer.

## Surface summary

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

## Endpoints

231 route decorators, grouped by path. Every row is in `schema/openapi_v1.0.10_F-008.json`, which lists each path and method individually with its source.

| Path group | Routes | Methods | Permissions seen | Example source |
| --- | --- | --- | --- | --- |
| `/admin` | 1 | GET | `admin.dashboard` | [D: mcpgateway/admin.py:3748] |
| `/admin/a2a` | 13 | GET, POST | `a2a.create`, `a2a.delete`, `a2a.invoke`, +3 more | [D: mcpgateway/admin.py:16239] |
| `/admin/cache` | 2 | GET, POST | `admin.system_config` | [D: mcpgateway/admin.py:2594] |
| `/admin/change-password-required` | 2 | GET, POST | — (**1 with none**) | [D: mcpgateway/admin.py:5128] |
| `/admin/config` | 5 | GET, POST, PUT | `admin.system_config` | [D: mcpgateway/admin.py:2424] |
| `/admin/events` | 1 | GET | `admin.events` | [D: mcpgateway/admin.py:14818] |
| `/admin/export` | 2 | GET, POST | `admin.system_config` | [D: mcpgateway/admin.py:15859] |
| `/admin/forgot-password` | 2 | GET, POST | — (**1 with none**) | [D: mcpgateway/admin.py:4696] |
| `/admin/gateways` | 14 | DELETE, GET, POST, PUT | `gateways.create`, `gateways.delete`, `gateways.read`, +1 more | [D: mcpgateway/admin.py:3637] |
| `/admin/grpc` | 8 | GET, POST, PUT | `admin.grpc` | [D: mcpgateway/admin.py:16941] |
| `/admin/import` | 4 | GET, POST | `admin.system_config` | [D: mcpgateway/admin.py:16079] |
| `/admin/llm` | 13 | DELETE, GET, POST | `admin.system_config` | [D: mcpgateway/routers/llm_admin_router.py:428] |
| `/admin/login` | 2 | GET, POST | — (**1 with none**) | [D: mcpgateway/admin.py:4407] |
| `/admin/logout` | 2 | GET, POST | — (**2 with none**) | [D: mcpgateway/admin.py:5102] |
| `/admin/logs` | 4 | GET | `admin.system_config` | [D: mcpgateway/admin.py:15307] |
| `/admin/maintenance` | 1 | GET | `admin.system_config` | [D: mcpgateway/admin.py:18547] |
| `/admin/mcp-registry` | 5 | GET, POST | `gateways.create`, `servers.create`, `servers.read` | [D: mcpgateway/admin.py:18256] |
| `/admin/metrics` | 3 | GET, POST | `admin.system_config` | [D: mcpgateway/admin.py:14632] |
| `/admin/observability` | 30 | DELETE, GET, POST, PUT | `admin.system_config` | [D: mcpgateway/admin.py:19812] |
| `/admin/overview` | 1 | GET | `admin.overview` | [D: mcpgateway/admin.py:2259] |
| `/admin/performance` | 6 | GET | `admin.system_config` | [D: mcpgateway/admin.py:20756] |
| `/admin/plugins` | 6 | GET, PUT | `admin.plugins` | [D: mcpgateway/admin.py:17714] |
| `/admin/prompts` | 9 | GET, POST | `prompts.create`, `prompts.delete`, `prompts.read`, +1 more | [D: mcpgateway/admin.py:3579] |
| `/admin/reset-password` | 2 | GET, POST | — | [D: mcpgateway/admin.py:4758] |
| `/admin/resources` | 10 | GET, POST | `resources.create`, `resources.delete`, `resources.read`, +1 more | [D: mcpgateway/admin.py:3524] |
| `/admin/roots` | 6 | GET, POST | `admin.system_config` | [D: mcpgateway/admin.py:14429] |
| `/admin/runtime` | 4 | GET, PATCH | `admin.system_config` | [D: mcpgateway/routers/runtime_admin_router.py:435] |
| `/admin/search` | 1 | GET | `admin.dashboard` | [D: mcpgateway/admin.py:11900] |
| `/admin/sections` | 4 | GET | `gateways.read`, `prompts.read`, `resources.read`, +1 more | [D: mcpgateway/admin.py:17412] |
| `/admin/servers` | 9 | GET, POST | `servers.create`, `servers.delete`, `servers.read`, +1 more | [D: mcpgateway/admin.py:2812] |
| `/admin/siem` | 5 | GET, POST, PUT | `admin.security_audit` | [D: mcpgateway/routers/siem.py:68] |
| `/admin/support-bundle` | 1 | GET | `admin.system_config` | [D: mcpgateway/admin.py:18466] |
| `/admin/system` | 1 | GET | `admin.system_config` | [D: mcpgateway/admin.py:18394] |
| `/admin/tags` | 1 | GET | `tags.read` | [D: mcpgateway/admin.py:15031] |
| `/admin/teams` | 21 | DELETE, GET, POST | `teams.create`, `teams.delete`, `teams.join`, +3 more | [D: mcpgateway/admin.py:5957] |
| `/admin/tokens` | 3 | DELETE, GET | `tokens.read`, `tokens.revoke` | [D: mcpgateway/admin.py:10932] |
| `/admin/tool-ops` | 1 | GET | `tools.read` | [D: mcpgateway/admin.py:9099] |
| `/admin/tools` | 14 | GET, POST | `tools.create`, `tools.delete`, `tools.read`, +1 more | [D: mcpgateway/admin.py:8790] |
| `/admin/users` | 11 | DELETE, GET, POST | `admin.user_management`, `teams.manage_members` | [D: mcpgateway/admin.py:7743] |
| `/admin/well-known` | 1 | GET | — | [D: mcpgateway/routers/well_known.py:338] |

## Events

No channel literal was found in this feature's files. That is a stated empty answer, not an omission — `schema/asyncapi_v1.0.10_F-008.json` is correspondingly empty.

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

- `schema/openapi_v1.0.10_F-008.json` — every path and method above, each with its `x-source` citation and the mounts it answers on. Request and response schemas are empty by design: nothing in the repository states them.
- `schema/asyncapi_v1.0.10_F-008.json` — channel names only.
- Entity shapes are `$ref`s into `schema/schemas.json`. No shape is redefined here.

## Traceability

Stories in `../PRDs/prd_v1.0.10_F-008-*.md` cite the endpoints above as evidence the behaviour
exists. They do not establish that it was wanted; see that document's own open questions.

## Open questions

- OPEN: Is the Admin Console intended to stay at parity with the domain APIs, or is it a superset that will diverge?
- OPEN: Why do 118 routes share `admin.system_config`? That permission is doing the work of a role rather than a permission.
- OPEN: Who is the intended operator — a platform administrator, or a team administrator with narrower scope?
