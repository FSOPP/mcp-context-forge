---
title: PRD v1.0.10 F-005 — A2A Agent Federation
id: F-005
status: as-built
owner: TBD
updated: 2026-09-20
---

# PRD v1.0.10 F-005 — A2A Agent Federation

> **Read the warning first.** A PRD states intent, and intent is not in a repository. Every story
> below was inferred backwards from endpoints and test names; not one of them is evidence that the
> feature was wanted, only that it exists. Business value, priority, metrics and personas are
> `OPEN:` throughout, and that is the honest answer rather than a gap to fill in later.
>
> This document deliberately holds no path and no schema. Those live in
> `../data/api-contract_v1.0.10_F-005.md` and `../data/schema/schemas.json`.

## Problem statement

OPEN: what problem does A2A Agent Federation solve, for whom, and what did they do before it existed? Not
recoverable from code.

## Business value

OPEN: unrecoverable. No metric, target or business case appears anywhere in the repository for
this feature.

## Target users

OPEN: the actors are listed in `../ddd/domain_*-a2a-agent-federation.md`, derived from auth roles and
endpoint consumers. Which of them this feature was built *for* is not stated.

## User stories

**F-005-US1.** As a consumer of A2A Agent Federation, I can manage a2a.

I: inferred from 7 route decorators carrying DELETE, GET, POST, PUT on `/a2a` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4890].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/a2a` are listed in `../tests/test_v1.0.10_F-005.md` and are the nearest available evidence that the behaviour is intended.

**F-005-US2.** As a consumer of A2A Agent Federation, I can manage plugin bindings.

I: inferred from 5 route decorators carrying DELETE, GET, POST on `/a2a-agents/plugin-bindings` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/a2a_agent_plugin_bindings.py:224].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/a2a-agents/plugin-bindings` are listed in `../tests/test_v1.0.10_F-005.md` and are the nearest available evidence that the behaviour is intended.

**F-005-US3.** As a consumer of A2A Agent Federation, I can manage invoke.

I: inferred from 2 route decorators carrying POST on `/a2a/invoke` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:5406].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/a2a/invoke` are listed in `../tests/test_v1.0.10_F-005.md` and are the nearest available evidence that the behaviour is intended.

**F-005-US4.** As a consumer of A2A Agent Federation, I can manage jsonrpc.

I: inferred from 1 route decorators carrying POST on `/a2a/jsonrpc` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:5459].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/a2a/jsonrpc` are listed in `../tests/test_v1.0.10_F-005.md` and are the nearest available evidence that the behaviour is intended.

**F-005-US5.** As a consumer of A2A Agent Federation, I can manage state.

I: inferred from 1 route decorators carrying POST on `/a2a/state` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:5157].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/a2a/state` are listed in `../tests/test_v1.0.10_F-005.md` and are the nearest available evidence that the behaviour is intended.

**F-005-US6.** As a consumer of A2A Agent Federation, I can manage toggle.

I: inferred from 1 route decorators carrying POST on `/a2a/toggle` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:5194].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/a2a/toggle` are listed in `../tests/test_v1.0.10_F-005.md` and are the nearest available evidence that the behaviour is intended.

## Non-functional requirements

OPEN: no SLO, latency target, throughput target or availability target appears in the repository
for this feature.

Where a number **is** configured, it is a real find and is recorded in
`../architect/feature_v1.0.10_F-005_architect.md` rather than guessed at here.

## Out of scope

OPEN: unrecoverable. Code records what was built and keeps no record of what was declined.

## Implementation status

States and what `done` costs: `../status-model.md`. A story is never more done than the test cases
that cover it.

| Story | Status | Evidence |
| --- | --- | --- |
| F-005-US1 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-005-US2 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-005-US3 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-005-US4 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-005-US5 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-005-US6 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |

## Open questions

- OPEN: What is the trust model for a remote gateway in a cross-gateway call? Both sides must trust the same JWT issuer, and nothing states how that is established operationally.
- OPEN: What happens to an in-flight A2A task when its agent is deregistered?
