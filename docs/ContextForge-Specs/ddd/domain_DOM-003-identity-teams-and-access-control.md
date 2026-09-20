---
title: Domain — Identity, Teams and Access Control
id: DOM-003
kind: domain
feature: F-003
status: as-built
owner: TBD
updated: 2026-09-20
---

# Domain — Identity, Teams and Access Control

> Reconstructed from code. Rules below were promoted from constraint comments written by the
> people who knew them; each cites both the statement and the site enforcing it. Motive is not
> recoverable and is asked, not written.

## Ubiquitous language

| Term | Means | Do not use for |
| --- | --- | --- |
| Token scoping | Layer 1 — what a caller can see | RBAC, which is Layer 2 |
| RBAC | Layer 2 — what a caller can do | token scoping |
| Personal team | the team auto-created for one user | team, which is shared |
| Admin bypass | visibility unrestricted by team, signalled by `token_teams=None` | permission to see another user's private rows, which it never grants |
| Public | platform-public scope | internet-anonymous, which it never means |

## Actors

| Actor | Role |
| --- | --- |
| Platform administrator | grants roles, approves users |
| Team administrator | manages members of one team |
| Member | authenticates and acts inside their teams |
| Identity provider | asserts an external identity |

## Business rules

**DOM-003-R1.** Single-use rotation: revoke the predecessor before minting so the old token cannot be replayed to mint further tokens. fail_if_already_revoked makes the revocation compare-and-set — concurrent refreshes race and exactly one wins. Fail closed when revocation cannot be persisted.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/routers/auth.py:581].

**DOM-003-R2.** Admin bypass (PR #4341 invariant): never reveal another user's private rows. Anonymous bypass sees public + team only; a DB-resolved admin session additionally sees their own private rows. Mirrors _apply_access_control.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/base_service.py:260].

**DOM-003-R3.** Admin bypass: respect PR #4341's invariant that admin bypass NEVER reveals another user's private rows. Anonymous bypass (no email) sees public + team only; DB-resolved admin sessions additionally see their OWN private rows. Matches the pattern in a2a_service._visible_agent_ids.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/base_service.py:106].

**DOM-003-R4.** Fetch a session-attached EmailUser directly from the DB, bypassing cache. Required for mutation paths (authenticate_user, unlock_user_account) where the returned object must be tracked by self.db so that ORM mutations and self.db.commit() are durable. Never use the cached detached object for writes.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/email_auth_service.py:607].

**DOM-003-R5.** Some tests patch create_task with a plain Mock return value. In that case the coroutine is never actually scheduled and must be closed.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/team_management_service.py:453].

**DOM-003-R6.** Add token permissions to team_admin role. The migration is idempotent: permissions that already exist are skipped. Supports both PostgreSQL and SQLite databases.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/alembic/versions/a31c6ffc2239_add_token_permissions_to_team_admin_role.py:75].

**DOM-003-R7.** Preserve raw JWT teams claim separately from the RBAC-resolved value. Used by OAuth token storage path selection (jwt_teams_claim is the authority for which Vault path was used during authorization — admin bypass must not collapse it to None for that purpose).

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/auth.py:1763].

**DOM-003-R8.** Session tokens ignore JWT is_admin claim — DB is the authority. An old/stale session JWT carrying is_admin=true must not influence the boolean admin decision; only DB-resolved token_teams=None can produce admin bypass below.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/auth_context.py:859].

**DOM-003-R9.** Grant bypass only when the fresh DB check positively confirms admin. db_user_is_admin is None (user missing from DB or query error) must fail-closed — a deleted or missing user should not inherit bypass even if the cached token_teams=None signal persists.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/auth_context.py:889].

**DOM-003-R10.** Return whether a persisted user has no local password credential. Missing attributes are treated as programmer errors. Cached/read-only identity objects may omit credential material, and callers must not classify those objects as passwordless.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/auth_user_helpers.py:25].

**DOM-003-R11.** Cross-worker revocation check: when a token is revoked on another worker, the revoking worker writes a Redis revocation marker. Check it BEFORE the L1 in-memory cache so that stale L1 entries cannot bypass revocation.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/cache/auth_cache.py:273].

**DOM-003-R12.** CWE-209: log full detail server-side only; never render internal error strings (which may contain upstream hostnames, token-endpoint URLs, or raw HTTP response bodies) into the browser-facing HTML page.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/routers/oauth_router.py:1222].

## Process flow

The process is the API surface: 81 route decorators, listed in `../data/api-contract_v1.0.10_F-003.md`, and the call sequence is in `../architect/feature_v1.0.10_F-003_architect.md` § Sequence. It is written there once rather than paraphrased here.

## Invariants

Database-level invariants for this feature are the `required` and key declarations in `../data/schema/schemas.json`, derived from the column definitions. `../data/data-erd_v1.0.10_F-003.md` lists them per table.

OPEN: which invariants are enforced only in application code and would survive a direct database write? The column constraints are visible; the guard clauses were not inventoried.

## Implementation status

States and what `done` costs: `../status-model.md`. Every row starts at `todo`; a rule reaches
`done` only when a test names the rule ID and that test passed here.

| Rule | Status | Evidence |
| --- | --- | --- |
| DOM-003-R1 | wip — implemented, no test names this rule ID | — |
| DOM-003-R2 | wip — implemented, no test names this rule ID | — |
| DOM-003-R3 | wip — implemented, no test names this rule ID | — |
| DOM-003-R4 | wip — implemented, no test names this rule ID | — |
| DOM-003-R5 | wip — implemented, no test names this rule ID | — |
| DOM-003-R6 | wip — implemented, no test names this rule ID | — |
| DOM-003-R7 | wip — implemented, no test names this rule ID | — |
| DOM-003-R8 | wip — implemented, no test names this rule ID | — |
| DOM-003-R9 | wip — implemented, no test names this rule ID | — |
| DOM-003-R10 | wip — implemented, no test names this rule ID | — |
| DOM-003-R11 | wip — implemented, no test names this rule ID | — |
| DOM-003-R12 | wip — implemented, no test names this rule ID | — |

## Open questions

- OPEN: Why is `email_users.email` the foreign-key target rather than `email_users.id`? Changing a user's email address now rewrites every referencing row, and nothing states whether that is intended or simply inherited.
- OPEN: What is the intended session lifetime, and is it different for SSO-provisioned identities?
- OPEN: Which of the 104 routes with no RBAC decorator are deliberately public, and which are oversights? The trust gate explains `/_internal/**`; it does not explain the rest.
- OPEN: which of the rules above the business would still hold if the code stopped enforcing them?
  A rule recovered from an enforcement site cannot distinguish policy from implementation detail.
