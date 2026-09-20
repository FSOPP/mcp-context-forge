---
title: PRD v1.0.10 F-008 — Admin Console
id: F-008
status: as-built
owner: TBD
updated: 2026-09-20
---

# PRD v1.0.10 F-008 — Admin Console

> **Read the warning first.** A PRD states intent, and intent is not in a repository. Every story
> below was inferred backwards from endpoints and test names; not one of them is evidence that the
> feature was wanted, only that it exists. Business value, priority, metrics and personas are
> `OPEN:` throughout, and that is the honest answer rather than a gap to fill in later.
>
> This document deliberately holds no path and no schema. Those live in
> `../data/api-contract_v1.0.10_F-008.md` and `../data/schema/schemas.json`.

## Problem statement

OPEN: what problem does Admin Console solve, for whom, and what did they do before it existed? Not
recoverable from code.

## Business value

OPEN: unrecoverable. No metric, target or business case appears anywhere in the repository for
this feature.

## Target users

OPEN: the actors are listed in `../ddd/domain_*-admin-console.md`, derived from auth roles and
endpoint consumers. Which of them this feature was built *for* is not stated.

## User stories

**F-008-US1.** As a consumer of Admin Console, I can read admin.

I: inferred from 1 route decorators carrying GET on `/admin` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:3748].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US2.** As a consumer of Admin Console, I can manage a2a.

I: inferred from 13 route decorators carrying GET, POST on `/admin/a2a` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:16239].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/a2a` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US3.** As a consumer of Admin Console, I can manage cache.

I: inferred from 2 route decorators carrying GET, POST on `/admin/cache` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:2594].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/cache` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US4.** As a consumer of Admin Console, I can manage change password required.

I: inferred from 2 route decorators carrying GET, POST on `/admin/change-password-required` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:5128].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/change-password-required` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US5.** As a consumer of Admin Console, I can manage config.

I: inferred from 5 route decorators carrying GET, POST, PUT on `/admin/config` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:2424].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/config` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US6.** As a consumer of Admin Console, I can read events.

I: inferred from 1 route decorators carrying GET on `/admin/events` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:14818].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/events` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US7.** As a consumer of Admin Console, I can manage export.

I: inferred from 2 route decorators carrying GET, POST on `/admin/export` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:15859].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/export` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US8.** As a consumer of Admin Console, I can manage forgot password.

I: inferred from 2 route decorators carrying GET, POST on `/admin/forgot-password` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:4696].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/forgot-password` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US9.** As a consumer of Admin Console, I can manage gateways.

I: inferred from 14 route decorators carrying DELETE, GET, POST, PUT on `/admin/gateways` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:3637].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/gateways` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US10.** As a consumer of Admin Console, I can manage grpc.

I: inferred from 8 route decorators carrying GET, POST, PUT on `/admin/grpc` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:16941].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/grpc` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US11.** As a consumer of Admin Console, I can manage import.

I: inferred from 4 route decorators carrying GET, POST on `/admin/import` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:16079].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/import` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US12.** As a consumer of Admin Console, I can manage llm.

I: inferred from 13 route decorators carrying DELETE, GET, POST on `/admin/llm` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/llm_admin_router.py:428].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/llm` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US13.** As a consumer of Admin Console, I can manage login.

I: inferred from 2 route decorators carrying GET, POST on `/admin/login` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:4407].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/login` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US14.** As a consumer of Admin Console, I can manage logout.

I: inferred from 2 route decorators carrying GET, POST on `/admin/logout` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:5102].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/logout` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US15.** As a consumer of Admin Console, I can read logs.

I: inferred from 4 route decorators carrying GET on `/admin/logs` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:15307].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/logs` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US16.** As a consumer of Admin Console, I can read maintenance.

I: inferred from 1 route decorators carrying GET on `/admin/maintenance` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:18547].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/maintenance` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US17.** As a consumer of Admin Console, I can manage mcp registry.

I: inferred from 5 route decorators carrying GET, POST on `/admin/mcp-registry` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:18256].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/mcp-registry` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US18.** As a consumer of Admin Console, I can manage metrics.

I: inferred from 3 route decorators carrying GET, POST on `/admin/metrics` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:14632].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/metrics` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US19.** As a consumer of Admin Console, I can manage observability.

I: inferred from 30 route decorators carrying DELETE, GET, POST, PUT on `/admin/observability` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:19812].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/observability` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US20.** As a consumer of Admin Console, I can read overview.

I: inferred from 1 route decorators carrying GET on `/admin/overview` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:2259].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/overview` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US21.** As a consumer of Admin Console, I can read performance.

I: inferred from 6 route decorators carrying GET on `/admin/performance` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:20756].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/performance` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US22.** As a consumer of Admin Console, I can manage plugins.

I: inferred from 6 route decorators carrying GET, PUT on `/admin/plugins` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:17714].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/plugins` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US23.** As a consumer of Admin Console, I can manage prompts.

I: inferred from 9 route decorators carrying GET, POST on `/admin/prompts` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:3579].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/prompts` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US24.** As a consumer of Admin Console, I can manage reset password.

I: inferred from 2 route decorators carrying GET, POST on `/admin/reset-password` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:4758].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/reset-password` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US25.** As a consumer of Admin Console, I can manage resources.

I: inferred from 10 route decorators carrying GET, POST on `/admin/resources` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:3524].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/resources` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US26.** As a consumer of Admin Console, I can manage roots.

I: inferred from 6 route decorators carrying GET, POST on `/admin/roots` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:14429].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/roots` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US27.** As a consumer of Admin Console, I can manage runtime.

I: inferred from 4 route decorators carrying GET, PATCH on `/admin/runtime` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/runtime_admin_router.py:435].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/runtime` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US28.** As a consumer of Admin Console, I can read search.

I: inferred from 1 route decorators carrying GET on `/admin/search` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:11900].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/search` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US29.** As a consumer of Admin Console, I can read sections.

I: inferred from 4 route decorators carrying GET on `/admin/sections` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:17412].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/sections` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US30.** As a consumer of Admin Console, I can manage servers.

I: inferred from 9 route decorators carrying GET, POST on `/admin/servers` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:2812].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/servers` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US31.** As a consumer of Admin Console, I can manage siem.

I: inferred from 5 route decorators carrying GET, POST, PUT on `/admin/siem` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/siem.py:68].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/siem` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US32.** As a consumer of Admin Console, I can read support bundle.

I: inferred from 1 route decorators carrying GET on `/admin/support-bundle` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:18466].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/support-bundle` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US33.** As a consumer of Admin Console, I can read system.

I: inferred from 1 route decorators carrying GET on `/admin/system` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:18394].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/system` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US34.** As a consumer of Admin Console, I can read tags.

I: inferred from 1 route decorators carrying GET on `/admin/tags` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:15031].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/tags` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US35.** As a consumer of Admin Console, I can manage teams.

I: inferred from 21 route decorators carrying DELETE, GET, POST on `/admin/teams` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:5957].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/teams` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US36.** As a consumer of Admin Console, I can manage tokens.

I: inferred from 3 route decorators carrying DELETE, GET on `/admin/tokens` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:10932].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/tokens` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US37.** As a consumer of Admin Console, I can read tool ops.

I: inferred from 1 route decorators carrying GET on `/admin/tool-ops` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:9099].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/tool-ops` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US38.** As a consumer of Admin Console, I can manage tools.

I: inferred from 14 route decorators carrying GET, POST on `/admin/tools` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:8790].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/tools` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US39.** As a consumer of Admin Console, I can manage users.

I: inferred from 11 route decorators carrying DELETE, GET, POST on `/admin/users` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/admin.py:7743].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/users` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

**F-008-US40.** As a consumer of Admin Console, I can read well known.

I: inferred from 1 route decorators carrying GET on `/admin/well-known` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/well_known.py:338].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/admin/well-known` are listed in `../tests/test_v1.0.10_F-008.md` and are the nearest available evidence that the behaviour is intended.

## Non-functional requirements

OPEN: no SLO, latency target, throughput target or availability target appears in the repository
for this feature.

Where a number **is** configured, it is a real find and is recorded in
`../architect/feature_v1.0.10_F-008_architect.md` rather than guessed at here.

## Out of scope

OPEN: unrecoverable. Code records what was built and keeps no record of what was declined.

## Implementation status

States and what `done` costs: `../status-model.md`. A story is never more done than the test cases
that cover it.

| Story | Status | Evidence |
| --- | --- | --- |
| F-008-US1 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US2 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US3 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US4 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US5 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US6 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US7 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US8 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US9 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US10 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US11 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US12 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US13 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US14 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US15 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US16 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US17 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US18 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US19 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US20 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US21 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US22 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US23 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US24 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US25 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US26 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US27 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US28 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US29 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US30 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US31 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US32 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US33 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US34 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US35 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US36 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US37 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US38 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US39 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-008-US40 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |

## Open questions

- OPEN: Is the Admin Console intended to stay at parity with the domain APIs, or is it a superset that will diverge?
- OPEN: Why do 118 routes share `admin.system_config`? That permission is doing the work of a role rather than a permission.
- OPEN: Who is the intended operator — a platform administrator, or a team administrator with narrower scope?
