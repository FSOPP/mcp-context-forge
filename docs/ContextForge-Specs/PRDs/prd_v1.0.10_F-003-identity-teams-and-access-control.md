---
title: PRD v1.0.10 F-003 — Identity, Teams and Access Control
id: F-003
status: as-built
owner: TBD
updated: 2026-09-20
---

# PRD v1.0.10 F-003 — Identity, Teams and Access Control

> **Read the warning first.** A PRD states intent, and intent is not in a repository. Every story
> below was inferred backwards from endpoints and test names; not one of them is evidence that the
> feature was wanted, only that it exists. Business value, priority, metrics and personas are
> `OPEN:` throughout, and that is the honest answer rather than a gap to fill in later.
>
> This document deliberately holds no path and no schema. Those live in
> `../data/api-contract_v1.0.10_F-003.md` and `../data/schema/schemas.json`.

## Problem statement

OPEN: what problem does Identity, Teams and Access Control solve, for whom, and what did they do before it existed? Not
recoverable from code.

## Business value

OPEN: unrecoverable. No metric, target or business case appears anywhere in the repository for
this feature.

## Target users

OPEN: the actors are listed in `../ddd/domain_*-identity-teams-and-access-control.md`, derived from auth roles and
endpoint consumers. Which of them this feature was built *for* is not stated.

## User stories

**F-003-US1.** As a consumer of Identity, Teams and Access Control, I can read csrf token.

I: inferred from 1 route decorators carrying GET on `/auth/csrf-token` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/auth.py:134].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/auth/csrf-token` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US2.** As a consumer of Identity, Teams and Access Control, I can manage email.

I: inferred from 15 route decorators carrying DELETE, GET, PATCH, POST on `/auth/email` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/email_auth.py:658].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/auth/email` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US3.** As a consumer of Identity, Teams and Access Control, I can manage login.

I: inferred from 1 route decorators carrying POST on `/auth/login` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/auth.py:177].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/auth/login` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US4.** As a consumer of Identity, Teams and Access Control, I can manage logout.

I: inferred from 1 route decorators carrying POST on `/auth/logout` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/auth.py:263].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/auth/logout` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US5.** As a consumer of Identity, Teams and Access Control, I can manage refresh.

I: inferred from 1 route decorators carrying POST on `/auth/refresh` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/auth.py:538].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/auth/refresh` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US6.** As a consumer of Identity, Teams and Access Control, I can manage sso.

I: inferred from 10 route decorators carrying DELETE, GET, POST, PUT on `/auth/sso` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/sso.py:560].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/auth/sso` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US7.** As a consumer of Identity, Teams and Access Control, I can read validate.

I: inferred from 1 route decorators carrying GET on `/auth/validate` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/auth.py:505].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/auth/validate` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US8.** As a consumer of Identity, Teams and Access Control, I can read authorize.

I: inferred from 1 route decorators carrying GET on `/oauth/authorize` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/oauth_router.py:586].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/oauth/authorize` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US9.** As a consumer of Identity, Teams and Access Control, I can read callback.

I: inferred from 1 route decorators carrying GET on `/oauth/callback` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/oauth_router.py:778].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/oauth/callback` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US10.** As a consumer of Identity, Teams and Access Control, I can manage fetch tools.

I: inferred from 1 route decorators carrying POST on `/oauth/fetch-tools` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/oauth_router.py:1690].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/oauth/fetch-tools` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US11.** As a consumer of Identity, Teams and Access Control, I can manage registered clients.

I: inferred from 3 route decorators carrying DELETE, GET on `/oauth/registered-clients` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/oauth_router.py:1775].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/oauth/registered-clients` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US12.** As a consumer of Identity, Teams and Access Control, I can read status.

I: inferred from 2 route decorators carrying GET on `/oauth/status` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/oauth_router.py:1509].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/oauth/status` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US13.** As a consumer of Identity, Teams and Access Control, I can read my.

I: inferred from 2 route decorators carrying GET on `/rbac/my` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/rbac.py:600].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/rbac/my` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US14.** As a consumer of Identity, Teams and Access Control, I can manage permissions.

I: inferred from 3 route decorators carrying GET, POST on `/rbac/permissions` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/rbac.py:540].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/rbac/permissions` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US15.** As a consumer of Identity, Teams and Access Control, I can manage roles.

I: inferred from 5 route decorators carrying DELETE, GET, POST, PUT on `/rbac/roles` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/rbac.py:131].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/rbac/roles` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US16.** As a consumer of Identity, Teams and Access Control, I can manage users.

I: inferred from 3 route decorators carrying DELETE, GET, POST on `/rbac/users` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/rbac.py:356].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/rbac/users` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US17.** As a consumer of Identity, Teams and Access Control, I can manage teams.

I: inferred from 5 route decorators carrying DELETE, GET, POST, PUT on `/teams` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/teams.py:195].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/teams` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US18.** As a consumer of Identity, Teams and Access Control, I can read discover.

I: inferred from 1 route decorators carrying GET on `/teams/discover` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/teams.py:322].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/teams/discover` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US19.** As a consumer of Identity, Teams and Access Control, I can manage invitations.

I: inferred from 4 route decorators carrying DELETE, GET, POST on `/teams/invitations` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/teams.py:958].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/teams/invitations` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US20.** As a consumer of Identity, Teams and Access Control, I can manage join.

I: inferred from 1 route decorators carrying POST on `/teams/join` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/teams.py:1005].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/teams/join` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US21.** As a consumer of Identity, Teams and Access Control, I can manage join requests.

I: inferred from 3 route decorators carrying DELETE, GET, POST on `/teams/join-requests` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/teams.py:1129].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/teams/join-requests` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US22.** As a consumer of Identity, Teams and Access Control, I can manage leave.

I: inferred from 1 route decorators carrying DELETE on `/teams/leave` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/teams.py:1074].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/teams/leave` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US23.** As a consumer of Identity, Teams and Access Control, I can manage members.

I: inferred from 4 route decorators carrying DELETE, GET, POST, PUT on `/teams/members` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/teams.py:564].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/teams/members` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US24.** As a consumer of Identity, Teams and Access Control, I can manage tokens.

I: inferred from 5 route decorators carrying DELETE, GET, POST, PUT on `/tokens` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/tokens.py:328].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/tokens` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US25.** As a consumer of Identity, Teams and Access Control, I can manage admin.

I: inferred from 2 route decorators carrying DELETE, GET on `/tokens/admin` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/tokens.py:627].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/tokens/admin` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US26.** As a consumer of Identity, Teams and Access Control, I can manage teams.

I: inferred from 2 route decorators carrying GET, POST on `/tokens/teams` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/tokens.py:920].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/tokens/teams` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US27.** As a consumer of Identity, Teams and Access Control, I can read usage.

I: inferred from 1 route decorators carrying GET on `/tokens/usage` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/tokens.py:588].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/tokens/usage` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

**F-003-US28.** As a consumer of Identity, Teams and Access Control, I can read authorize.

I: inferred from 1 route decorators carrying GET on `/vault/authorize` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/vault_router.py:86].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/vault/authorize` are listed in `../tests/test_v1.0.10_F-003.md` and are the nearest available evidence that the behaviour is intended.

## Non-functional requirements

OPEN: no SLO, latency target, throughput target or availability target appears in the repository
for this feature.

Where a number **is** configured, it is a real find and is recorded in
`../architect/feature_v1.0.10_F-003_architect.md` rather than guessed at here.

## Out of scope

OPEN: unrecoverable. Code records what was built and keeps no record of what was declined.

## Implementation status

States and what `done` costs: `../status-model.md`. A story is never more done than the test cases
that cover it.

| Story | Status | Evidence |
| --- | --- | --- |
| F-003-US1 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US2 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US3 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US4 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US5 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US6 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US7 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US8 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US9 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US10 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US11 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US12 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US13 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US14 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US15 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US16 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US17 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US18 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US19 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US20 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US21 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US22 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US23 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US24 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US25 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US26 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US27 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-003-US28 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |

## Open questions

- OPEN: Why is `email_users.email` the foreign-key target rather than `email_users.id`? Changing a user's email address now rewrites every referencing row, and nothing states whether that is intended or simply inherited.
- OPEN: What is the intended session lifetime, and is it different for SSO-provisioned identities?
- OPEN: Which of the 104 routes with no RBAC decorator are deliberately public, and which are oversights? The trust gate explains `/_internal/**`; it does not explain the rest.
