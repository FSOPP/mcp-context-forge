---
title: Data — v1.0.10 F-003 — Identity, Teams and Access Control
id: F-003
status: as-built
owner: TBD
updated: 2026-09-20
---

# Data — v1.0.10 F-003 — Identity, Teams and Access Control

> Reversed from the ORM models in `mcpgateway/db.py`, which is a consolidated snapshot of the
> shape the database has. The migration directory records how it got there and is the change
> story, not the shape.

## Entities

| Table | Columns | Required | Primary key | Foreign keys | Source |
| --- | --- | --- | --- | --- | --- |
| `email_users` | 17 | 10 | `id` PK | — | [D: mcpgateway/db.py:1516] |
| `email_teams` | 11 | 9 | `id` PK | `created_by`→`email_users.email` | [D: mcpgateway/db.py:1976] |
| `email_team_members` | 8 | 6 | `id` PK | `team_id`→`email_teams.id`, `user_email`→`email_users.email`, `invited_by`→`email_users.email` | [D: mcpgateway/db.py:2119] |
| `email_team_member_history` | 8 | 7 | `id` PK | `team_member_id`→`email_team_members.id`, `team_id`→`email_teams.id`, `user_email`→`email_users.email`, +1 | [D: mcpgateway/db.py:2187] |
| `email_team_invitations` | 9 | 9 | `id` PK | `team_id`→`email_teams.id`, `invited_by`→`email_users.email` | [D: mcpgateway/db.py:2255] |
| `email_team_join_requests` | 10 | 6 | `id` PK | `team_id`→`email_teams.id`, `user_email`→`email_users.email`, `reviewed_by`→`email_users.email` | [D: mcpgateway/db.py:2358] |
| `email_auth_events` | 9 | 4 | `id` PK | — | [D: mcpgateway/db.py:1768] |
| `roles` | 11 | 9 | `id` PK | `inherits_from`→`roles.id`, `created_by`→`email_users.email` | [D: mcpgateway/db.py:1170] |
| `user_roles` | 10 | 7 | `id` PK | `user_email`→`email_users.email`, `role_id`→`roles.id`, `granted_by`→`email_users.email` | [D: mcpgateway/db.py:1223] |
| `permission_audit_log` | 11 | 4 | `id` PK | — | [D: mcpgateway/db.py:1296] |
| `email_api_tokens` | 17 | 7 | `id` PK | `user_email`→`email_users.email`, `team_id`→`email_teams.id`, `server_id`→`servers.id` | [D: mcpgateway/db.py:5486] |
| `token_usage_logs` | 12 | 5 | `id` PK | — | [D: mcpgateway/db.py:5630] |
| `token_revocations` | 6 | 3 | `jti` PK | `revoked_by`→`email_users.email` | [D: mcpgateway/db.py:5687] |
| `oauth_tokens` | 13 | 8 | `id` PK | `gateway_id`→`gateways.id`, `app_user_email`→`email_users.email` | [D: mcpgateway/db.py:5354] |
| `oauth_states` | 10 | 6 | `id` PK | `gateway_id`→`gateways.id` | [D: mcpgateway/db.py:5387] |
| `registered_oauth_clients` | 15 | 9 | `id` PK | `gateway_id`→`gateways.id` | [D: mcpgateway/db.py:5414] |
| `sso_providers` | 21 | 17 | `id` PK | — | [D: mcpgateway/db.py:5752] |
| `sso_auth_sessions` | 9 | 6 | `id` PK | `provider_id`→`sso_providers.id`, `user_email`→`email_users.email` | [D: mcpgateway/db.py:5821] |
| `password_reset_tokens` | 8 | 5 | `id` PK | `user_email`→`email_users.email` | [D: mcpgateway/db.py:1881] |
| `password_history` | 4 | 4 | `id` PK | `user_email`→`email_users.email` | [D: mcpgateway/db.py:1932] |
| `pending_user_approvals` | 12 | 7 | `id` PK | `approved_by`→`email_users.email` | [D: mcpgateway/db.py:2453] |

The diagram is `schema/erd_v1.0.10_F-003.puml`. Field-level detail is `schema/schemas.json`, which this table must not restate — one definition per shape, and this is the summary view of it.

## Migrations

`mcpgateway/alembic/versions/` holds the change history for these tables
[D: mcpgateway/alembic/versions/356a2d4eed6f_uuid_change_for_prompt_and_resources.py:1]. The
repository requires one head and an idempotent upgrade that checks before it modifies
[D: CLAUDE.md:389].

I: the models are the authority over the migrations for *shape* — basis: the repository states
that a fresh database is created from `db.py` directly and migrations skip tables they do not
find [D: CLAUDE.md:389].

## Access pattern

OPEN: which of this feature's tables are read on the hot path and which only by the console. The
queries were not inventoried, and the two have very different indexing consequences.

## Open questions

- OPEN: retention and archival for these tables. No TTL is declared on any of them.
- OPEN: backward-compatibility window for a shape change here — what a client may still be
  sending when a column is dropped.
- OPEN: are the migrations reversible? A `downgrade` that loses data is indistinguishable from one
  that does not, without reading each.
