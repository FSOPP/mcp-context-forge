---
title: API Contract v1.0.10 F-003 — Identity, Teams and Access Control
id: F-003
status: as-built
owner: TBD
updated: 2026-09-20
---

# API Contract v1.0.10 F-003 — Identity, Teams and Access Control

> Reversed from code, not written before it. `[D: path:line]` marks a derived fact you can
> reopen; `I:` marks a stated leap; `OPEN:` marks what the code cannot answer.

## Surface summary

This feature answers two separate questions, and the codebase is emphatic that they
stay separate: token scoping decides what a caller can **see**, RBAC decides what a caller can
**do** [D: mcpgateway/middleware/rbac.py:921].

Layer 1 has two policy points and they are not interchangeable. `normalize_token_teams` reads API
and legacy tokens, where the JWT `teams` claim is the sole authority
[D: mcpgateway/auth_context.py:246]; `resolve_session_teams` reads session tokens, where the
database is the authority and the claim can only narrow [D: mcpgateway/auth.py:644]. A missing
`teams` key resolves to public-only, so the default fails closed.

The two live in different modules. `AGENTS.md` places both in `mcpgateway/auth.py`
[D: CLAUDE.md:170]; only `resolve_session_teams` is there.

Layer 2 is `require_permission` on the handler. 422 of 587 route decorators carry an explicit
permission [D: mcpgateway/middleware/rbac.py:921].

Identity is not one column. `email_users` has an `id` primary key, but every foreign key in the
schema targets `email_users.email` instead [D: mcpgateway/db.py:1516].

## Endpoints

81 route decorators, grouped by path. Every row is in `schema/openapi_v1.0.10_F-003.json`, which lists each path and method individually with its source.

| Path group | Routes | Methods | Permissions seen | Example source |
| --- | --- | --- | --- | --- |
| `/auth/csrf-token` | 1 | GET | — | [D: mcpgateway/routers/auth.py:134] |
| `/auth/email` | 15 | DELETE, GET, PATCH, POST | `admin.user_management` | [D: mcpgateway/routers/email_auth.py:658] |
| `/auth/login` | 1 | POST | — | [D: mcpgateway/routers/auth.py:177] |
| `/auth/logout` | 1 | POST | — | [D: mcpgateway/routers/auth.py:263] |
| `/auth/refresh` | 1 | POST | — | [D: mcpgateway/routers/auth.py:538] |
| `/auth/sso` | 10 | DELETE, GET, POST, PUT | `admin.sso_providers:create`, `admin.sso_providers:delete`, `admin.sso_providers:read`, +2 more | [D: mcpgateway/routers/sso.py:560] |
| `/auth/validate` | 1 | GET | — | [D: mcpgateway/routers/auth.py:505] |
| `/oauth/authorize` | 1 | GET | — | [D: mcpgateway/routers/oauth_router.py:586] |
| `/oauth/callback` | 1 | GET | — | [D: mcpgateway/routers/oauth_router.py:778] |
| `/oauth/fetch-tools` | 1 | POST | `gateways.update` | [D: mcpgateway/routers/oauth_router.py:1690] |
| `/oauth/registered-clients` | 3 | DELETE, GET | — | [D: mcpgateway/routers/oauth_router.py:1775] |
| `/oauth/status` | 2 | GET | — | [D: mcpgateway/routers/oauth_router.py:1509] |
| `/rbac/my` | 2 | GET | — | [D: mcpgateway/routers/rbac.py:600] |
| `/rbac/permissions` | 3 | GET, POST | `admin.security_audit` | [D: mcpgateway/routers/rbac.py:540] |
| `/rbac/roles` | 5 | DELETE, GET, POST, PUT | `admin.user_management` | [D: mcpgateway/routers/rbac.py:131] |
| `/rbac/users` | 3 | DELETE, GET, POST | `admin.user_management` | [D: mcpgateway/routers/rbac.py:356] |
| `/teams` | 16 | DELETE, GET, POST, PUT | `teams.create`, `teams.delete`, `teams.join`, +3 more | [D: mcpgateway/routers/teams.py:195] |
| `/teams/discover` | 1 | GET | `teams.read` | [D: mcpgateway/routers/teams.py:322] |
| `/teams/invitations` | 2 | DELETE, POST | `teams.join`, `teams.manage_members` | [D: mcpgateway/routers/teams.py:958] |
| `/tokens` | 6 | DELETE, GET, POST, PUT | `tokens.create`, `tokens.read`, `tokens.revoke`, +1 more | [D: mcpgateway/routers/tokens.py:328] |
| `/tokens/admin` | 2 | DELETE, GET | — | [D: mcpgateway/routers/tokens.py:627] |
| `/tokens/teams` | 2 | GET, POST | `tokens.create`, `tokens.read` | [D: mcpgateway/routers/tokens.py:920] |
| `/vault/authorize` | 1 | GET | — | [D: mcpgateway/routers/vault_router.py:86] |

## Events

| Channel | Kind | Role | Source |
| --- | --- | --- | --- |
| topic `token-exchange` | message transport | declared, unused direction | [D: mcpgateway/routers/oauth_router.py:58] |

OPEN: payload shape, delivery guarantee and ordering key for each channel. The survey found the topic names; nothing in the repository declares a schema for them.

## Error model

Authorisation failures are HTTP 401 and 403. CSRF failure is 403 with detail
`CSRF token validation failed` [D: mcpgateway/admin.py:1886]. A token whose team claim resolves to
no team yields public-only visibility rather than an error, so a caller sees an empty list instead
of a denial [D: mcpgateway/auth.py:1].

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

- `schema/openapi_v1.0.10_F-003.json` — every path and method above, each with its `x-source` citation and the mounts it answers on. Request and response schemas are empty by design: nothing in the repository states them.
- `schema/asyncapi_v1.0.10_F-003.json` — channel names only.
- Entity shapes are `$ref`s into `schema/schemas.json`. No shape is redefined here.

## Traceability

Stories in `../PRDs/prd_v1.0.10_F-003-*.md` cite the endpoints above as evidence the behaviour
exists. They do not establish that it was wanted; see that document's own open questions.

## Open questions

- OPEN: Why is `email_users.email` the foreign-key target rather than `email_users.id`? Changing a user's email address now rewrites every referencing row, and nothing states whether that is intended or simply inherited.
- OPEN: What is the intended session lifetime, and is it different for SSO-provisioned identities?
- OPEN: Which of the 104 routes with no RBAC decorator are deliberately public, and which are oversights? The trust gate explains `/_internal/**`; it does not explain the rest.
