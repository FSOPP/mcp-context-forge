---
title: Fixtures — v1.0.10 F-003 — Identity, Teams and Access Control
id: F-003
status: as-built
owner: TBD
updated: 2026-09-20
---

# Fixtures — v1.0.10 F-003 — Identity, Teams and Access Control

> Minimal valid records, one per entity, generated from the required columns in
> `schema/schemas.json`. They are shape examples, not scenarios.

## Sets

| Entity | Records | Contents |
| --- | --- | --- |
| `email_api_tokens` | 1 rows | 7 required fields |
| `email_auth_events` | 1 rows | 4 required fields |
| `email_team_invitations` | 1 rows | 9 required fields |
| `email_team_join_requests` | 1 rows | 6 required fields |
| `email_team_member_history` | 1 rows | 7 required fields |
| `email_team_members` | 1 rows | 6 required fields |
| `email_teams` | 1 rows | 9 required fields |
| `email_users` | 1 rows | 10 required fields |
| `oauth_states` | 1 rows | 6 required fields |
| `oauth_tokens` | 1 rows | 8 required fields |
| `password_history` | 1 rows | 4 required fields |
| `password_reset_tokens` | 1 rows | 5 required fields |
| `pending_user_approvals` | 1 rows | 7 required fields |
| `permission_audit_log` | 1 rows | 4 required fields |
| `registered_oauth_clients` | 1 rows | 9 required fields |
| `roles` | 1 rows | 9 required fields |
| `sso_auth_sessions` | 1 rows | 6 required fields |
| `sso_providers` | 1 rows | 17 required fields |
| `token_revocations` | 1 rows | 3 required fields |
| `token_usage_logs` | 1 rows | 5 required fields |
| `user_roles` | 1 rows | 7 required fields |

Every string field carries the literal `OPEN` rather than a plausible-looking value. A fixture
that reads like real data is the easiest way for an invented field to survive review.

No value here comes from an environment file. The survey recorded 112 secret-shaped configuration
keys and read none of their values [D: mcpgateway/config.py:4037].

## Scenarios

OPEN: what scenario is each set for? These were generated from the schema, not lifted from the
suite. The repository's own fixtures live in `tests/` and `conftest.py`
[D: conftest.py:1] and are richer; mapping them onto these entities was not done.

## Open questions

- OPEN: which of these entities needs a realistic fixture for a meaningful test, and what would
  make it realistic?
- OPEN: are there entity combinations that must appear together to be valid? Foreign keys say what
  may reference what; they do not say what must exist.
