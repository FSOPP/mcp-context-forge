---
title: PRD v1.0.10 F-006 — LLM Gateway and Chat
id: F-006
status: as-built
owner: TBD
updated: 2026-09-20
---

# PRD v1.0.10 F-006 — LLM Gateway and Chat

> **Read the warning first.** A PRD states intent, and intent is not in a repository. Every story
> below was inferred backwards from endpoints and test names; not one of them is evidence that the
> feature was wanted, only that it exists. Business value, priority, metrics and personas are
> `OPEN:` throughout, and that is the honest answer rather than a gap to fill in later.
>
> This document deliberately holds no path and no schema. Those live in
> `../data/api-contract_v1.0.10_F-006.md` and `../data/schema/schemas.json`.

## Problem statement

OPEN: what problem does LLM Gateway and Chat solve, for whom, and what did they do before it existed? Not
recoverable from code.

## Business value

OPEN: unrecoverable. No metric, target or business case appears anywhere in the repository for
this feature.

## Target users

OPEN: the actors are listed in `../ddd/domain_*-llm-gateway-and-chat.md`, derived from auth roles and
endpoint consumers. Which of them this feature was built *for* is not stated.

## User stories

**F-006-US1.** As a consumer of LLM Gateway and Chat, I can manage completions.

I: inferred from 1 route decorators carrying POST on `/chat/completions` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/llm_proxy_router.py:43].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/chat/completions` are listed in `../tests/test_v1.0.10_F-006.md` and are the nearest available evidence that the behaviour is intended.

**F-006-US2.** As a consumer of LLM Gateway and Chat, I can read gateway.

I: inferred from 1 route decorators carrying GET on `/llm/gateway` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/llm_config_router.py:596].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/llm/gateway` are listed in `../tests/test_v1.0.10_F-006.md` and are the nearest available evidence that the behaviour is intended.

**F-006-US3.** As a consumer of LLM Gateway and Chat, I can manage models.

I: inferred from 6 route decorators carrying DELETE, GET, PATCH, POST on `/llm/models` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/llm_config_router.py:385].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/llm/models` are listed in `../tests/test_v1.0.10_F-006.md` and are the nearest available evidence that the behaviour is intended.

**F-006-US4.** As a consumer of LLM Gateway and Chat, I can manage providers.

I: inferred from 7 route decorators carrying DELETE, GET, PATCH, POST on `/llm/providers` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/llm_config_router.py:110].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/llm/providers` are listed in `../tests/test_v1.0.10_F-006.md` and are the nearest available evidence that the behaviour is intended.

**F-006-US5.** As a consumer of LLM Gateway and Chat, I can manage chat.

I: inferred from 1 route decorators carrying POST on `/llmchat/chat` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/llmchat_router.py:1287].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/llmchat/chat` are listed in `../tests/test_v1.0.10_F-006.md` and are the nearest available evidence that the behaviour is intended.

**F-006-US6.** As a consumer of LLM Gateway and Chat, I can read config.

I: inferred from 1 route decorators carrying GET on `/llmchat/config` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/llmchat_router.py:1575].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/llmchat/config` are listed in `../tests/test_v1.0.10_F-006.md` and are the nearest available evidence that the behaviour is intended.

**F-006-US7.** As a consumer of LLM Gateway and Chat, I can manage connect.

I: inferred from 1 route decorators carrying POST on `/llmchat/connect` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/llmchat_router.py:1011].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/llmchat/connect` are listed in `../tests/test_v1.0.10_F-006.md` and are the nearest available evidence that the behaviour is intended.

**F-006-US8.** As a consumer of LLM Gateway and Chat, I can manage disconnect.

I: inferred from 1 route decorators carrying POST on `/llmchat/disconnect` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/llmchat_router.py:1412].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/llmchat/disconnect` are listed in `../tests/test_v1.0.10_F-006.md` and are the nearest available evidence that the behaviour is intended.

**F-006-US9.** As a consumer of LLM Gateway and Chat, I can read gateway.

I: inferred from 1 route decorators carrying GET on `/llmchat/gateway` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/llmchat_router.py:1636].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/llmchat/gateway` are listed in `../tests/test_v1.0.10_F-006.md` and are the nearest available evidence that the behaviour is intended.

**F-006-US10.** As a consumer of LLM Gateway and Chat, I can read status.

I: inferred from 1 route decorators carrying GET on `/llmchat/status` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/llmchat_router.py:1524].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/llmchat/status` are listed in `../tests/test_v1.0.10_F-006.md` and are the nearest available evidence that the behaviour is intended.

**F-006-US11.** As a consumer of LLM Gateway and Chat, I can read models.

I: inferred from 1 route decorators carrying GET on `/models` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/llm_proxy_router.py:133].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/models` are listed in `../tests/test_v1.0.10_F-006.md` and are the nearest available evidence that the behaviour is intended.

## Non-functional requirements

OPEN: no SLO, latency target, throughput target or availability target appears in the repository
for this feature.

Where a number **is** configured, it is a real find and is recorded in
`../architect/feature_v1.0.10_F-006_architect.md` rather than guessed at here.

## Out of scope

OPEN: unrecoverable. Code records what was built and keeps no record of what was declined.

## Implementation status

States and what `done` costs: `../status-model.md`. A story is never more done than the test cases
that cover it.

| Story | Status | Evidence |
| --- | --- | --- |
| F-006-US1 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-006-US2 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-006-US3 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-006-US4 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-006-US5 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-006-US6 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-006-US7 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-006-US8 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-006-US9 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-006-US10 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-006-US11 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |

## Open questions

- OPEN: Which providers are supported in practice, and which are merely representable in `llm_providers`?
- OPEN: What is the cost or rate ceiling on the proxy? No limit is configured.
