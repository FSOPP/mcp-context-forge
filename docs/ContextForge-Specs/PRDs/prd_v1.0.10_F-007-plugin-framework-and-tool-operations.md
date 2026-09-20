---
title: PRD v1.0.10 F-007 — Plugin Framework and Tool Operations
id: F-007
status: as-built
owner: TBD
updated: 2026-09-20
---

# PRD v1.0.10 F-007 — Plugin Framework and Tool Operations

> **Read the warning first.** A PRD states intent, and intent is not in a repository. Every story
> below was inferred backwards from endpoints and test names; not one of them is evidence that the
> feature was wanted, only that it exists. Business value, priority, metrics and personas are
> `OPEN:` throughout, and that is the honest answer rather than a gap to fill in later.
>
> This document deliberately holds no path and no schema. Those live in
> `../data/api-contract_v1.0.10_F-007.md` and `../data/schema/schemas.json`.

## Problem statement

OPEN: what problem does Plugin Framework and Tool Operations solve, for whom, and what did they do before it existed? Not
recoverable from code.

## Business value

OPEN: unrecoverable. No metric, target or business case appears anywhere in the repository for
this feature.

## Target users

OPEN: the actors are listed in `../ddd/domain_*-plugin-framework-and-tool-operations.md`, derived from auth roles and
endpoint consumers. Which of them this feature was built *for* is not stated.

## User stories

**F-007-US1.** As a consumer of Plugin Framework and Tool Operations, I can read plugins.

I: inferred from 1 route decorators carrying GET on `/plugins` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/plugins.py:29].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/plugins` are listed in `../tests/test_v1.0.10_F-007.md` and are the nearest available evidence that the behaviour is intended.

**F-007-US2.** As a consumer of Plugin Framework and Tool Operations, I can manage enrichment.

I: inferred from 1 route decorators carrying POST on `/toolops/enrichment` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/toolops_router.py:144].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/toolops/enrichment` are listed in `../tests/test_v1.0.10_F-007.md` and are the nearest available evidence that the behaviour is intended.

**F-007-US3.** As a consumer of Plugin Framework and Tool Operations, I can manage validation.

I: inferred from 2 route decorators carrying POST on `/toolops/validation` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/toolops_router.py:108].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/toolops/validation` are listed in `../tests/test_v1.0.10_F-007.md` and are the nearest available evidence that the behaviour is intended.

## Non-functional requirements

OPEN: no SLO, latency target, throughput target or availability target appears in the repository
for this feature.

Where a number **is** configured, it is a real find and is recorded in
`../architect/feature_v1.0.10_F-007_architect.md` rather than guessed at here.

## Out of scope

OPEN: unrecoverable. Code records what was built and keeps no record of what was declined.

## Implementation status

States and what `done` costs: `../status-model.md`. A story is never more done than the test cases
that cover it.

| Story | Status | Evidence |
| --- | --- | --- |
| F-007-US1 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-007-US2 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-007-US3 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |

## Open questions

- OPEN: What is the failure policy when a plugin hook raises? Whether the request fails or the plugin is skipped is a decision the framework makes and the documentation does not state.
- OPEN: Why is the framework off by default?
