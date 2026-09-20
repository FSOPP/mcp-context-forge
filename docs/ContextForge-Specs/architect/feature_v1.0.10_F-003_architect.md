---
title: Feature Architecture v1.0.10 F-003 — Identity, Teams and Access Control
id: F-003
status: as-built
owner: TBD
updated: 2026-09-20
---

# Feature Architecture v1.0.10 F-003 — Identity, Teams and Access Control

> As-built. `[D: path:line]` is derived and reopenable, `I:` states its leap, `OPEN:` is a question
> the code cannot answer. Shared conventions live in `architect_common.md`; the system view lives
> in `architect.md`.

## Design summary

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

Implementation lives in:

- `mcpgateway/auth.py`
- `mcpgateway/auth_context.py`
- `mcpgateway/middleware/rbac.py`
- `mcpgateway/routers/auth.py`
- `mcpgateway/routers/email_auth.py`
- `mcpgateway/routers/teams.py`
- `mcpgateway/routers/tokens.py`
- `mcpgateway/routers/rbac.py`
- `mcpgateway/routers/sso.py`
- `mcpgateway/routers/oauth_router.py`
- `mcpgateway/routers/vault_router.py`
- `mcpgateway/services/permission_service.py`
- `mcpgateway/services/team_service.py`
- `mcpgateway/services/token_catalog_service.py`
- `mcpgateway/auth_user_helpers.py`
- `mcpgateway/cache/auth_cache.py`
- `mcpgateway/services/email_auth_service.py`
- `mcpgateway/services/sso_service.py`
- `mcpgateway/services/team_management_service.py`
- `mcpgateway/utils/admin_check.py`
- `mcpgateway/utils/token_exchange_audit.py`
- `mcpgateway/services/base_service.py`
- `mcpgateway/alembic/versions/a31c6ffc2239_add_token_permissions_to_team_admin_role.py`

## API contracts

81 route decorators belong to this feature. The readable
contract is `../data/api-contract_v1.0.10_F-003.md`; the machine-readable one is
`../data/schema/openapi_v1.0.10_F-003.json` and `../data/schema/asyncapi_v1.0.10_F-003.json`.

Request and response shapes are not stated in either. The repository ships no OpenAPI document,
and the handlers were not read field by field, so inventing those shapes here would be the one
thing this hub must not do.

## Data model

| table | fields | source |
| --- | --- | --- |
| `email_users` | 17 | [D: mcpgateway/db.py:1516] |
| `email_teams` | 11 | [D: mcpgateway/db.py:1976] |
| `email_team_members` | 8 | [D: mcpgateway/db.py:2119] |
| `email_team_member_history` | 8 | [D: mcpgateway/db.py:2187] |
| `email_team_invitations` | 9 | [D: mcpgateway/db.py:2255] |
| `email_team_join_requests` | 10 | [D: mcpgateway/db.py:2358] |
| `email_auth_events` | 9 | [D: mcpgateway/db.py:1768] |
| `roles` | 11 | [D: mcpgateway/db.py:1170] |
| `user_roles` | 10 | [D: mcpgateway/db.py:1223] |
| `permission_audit_log` | 11 | [D: mcpgateway/db.py:1296] |
| `email_api_tokens` | 17 | [D: mcpgateway/db.py:5486] |
| `token_usage_logs` | 12 | [D: mcpgateway/db.py:5630] |
| `token_revocations` | 6 | [D: mcpgateway/db.py:5687] |
| `oauth_tokens` | 13 | [D: mcpgateway/db.py:5354] |
| `oauth_states` | 10 | [D: mcpgateway/db.py:5387] |
| `registered_oauth_clients` | 15 | [D: mcpgateway/db.py:5414] |
| `sso_providers` | 21 | [D: mcpgateway/db.py:5752] |
| `sso_auth_sessions` | 9 | [D: mcpgateway/db.py:5821] |
| `password_reset_tokens` | 8 | [D: mcpgateway/db.py:1881] |
| `password_history` | 4 | [D: mcpgateway/db.py:1932] |
| `pending_user_approvals` | 12 | [D: mcpgateway/db.py:2453] |

21 tables, 231 columns. Full field detail is `../data/schema/schemas.json`; the diagram is `../data/schema/erd_v1.0.10_F-003.puml`.

## Sequence

Authorising one request:

1. `AuthContextMiddleware` resolves the principal and memoizes the derived triple on
   `request.state` [D: mcpgateway/auth_context.py:246].
2. Layer 1 runs. For an API or legacy token, `normalize_token_teams` reads the JWT `teams` claim as
   the sole authority [D: mcpgateway/auth_context.py:246]. For a session token,
   `resolve_session_teams` takes the database as authority and lets the claim narrow only
   [D: mcpgateway/auth.py:644].
3. `TokenScopingMiddleware` evaluates the token's scopes through `token_scope_grants`, where an
   empty scope list means inherit from RBAC rather than deny
   [D: mcpgateway/middleware/rbac.py:55].
4. Layer 2 runs on the handler: `require_permission` checks the action
   [D: mcpgateway/middleware/rbac.py:921].
5. The handler passes the Layer-1 scope into the service call, so the query filters rows the
   caller may not see [D: mcpgateway/auth_context.py:246].

Admin bypass is signalled by `token_teams=None` while the email is kept, so an administrator still
owner-matches their own private rows [D: mcpgateway/auth_context.py:246].

## Failure modes

- Token with no resolvable team: returns an empty result set rather than an error
  [D: mcpgateway/auth_context.py:246]. A caller cannot distinguish "nothing exists" from "nothing
  visible to you".
- CSRF mismatch: 403 with detail `CSRF token validation failed` [D: mcpgateway/admin.py:1886].
- Revoked team in a session token's claim: intersection is empty, access falls to public-only
  [D: mcpgateway/auth.py:644].

## Observability

Execution metrics for this feature's primitives are written to the per-invocation
and hourly tables when `METRICS_ENABLED` style recording is on [D: mcpgateway/config.py:2394].
Traces and spans come from `ObservabilityMiddleware`, which covers every path not on the skip list
[D: mcpgateway/middleware/path_filter.py:33]. Audit rows are written through `log_action` on its
own session [D: mcpgateway/services/audit_trail_service.py:73].

OPEN: which of this feature's operations are expected to be alertable, and on what threshold. No
alert rule or SLO appears in the repository.

## Traceability

- Stories: `../PRDs/prd_v1.0.10_F-003-*.md`
- Tasks: `../tasks/tasks_v1.0.10_F-003.md`
- Tests: `../tests/test_v1.0.10_F-003.md`
- Contract: `../data/api-contract_v1.0.10_F-003.md`

## Open questions

- OPEN: Why is `email_users.email` the foreign-key target rather than `email_users.id`? Changing a user's email address now rewrites every referencing row, and nothing states whether that is intended or simply inherited.
- OPEN: What is the intended session lifetime, and is it different for SSO-provisioned identities?
- OPEN: Which of the 104 routes with no RBAC decorator are deliberately public, and which are oversights? The trust gate explains `/_internal/**`; it does not explain the rest.
