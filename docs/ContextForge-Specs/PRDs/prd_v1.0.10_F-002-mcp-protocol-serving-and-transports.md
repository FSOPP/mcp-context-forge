---
title: PRD v1.0.10 F-002 — MCP Protocol Serving and Transports
id: F-002
status: as-built
owner: TBD
updated: 2026-09-20
---

# PRD v1.0.10 F-002 — MCP Protocol Serving and Transports

> **Read the warning first.** A PRD states intent, and intent is not in a repository. Every story
> below was inferred backwards from endpoints and test names; not one of them is evidence that the
> feature was wanted, only that it exists. Business value, priority, metrics and personas are
> `OPEN:` throughout, and that is the honest answer rather than a gap to fill in later.
>
> This document deliberately holds no path and no schema. Those live in
> `../data/api-contract_v1.0.10_F-002.md` and `../data/schema/schemas.json`.

## Problem statement

OPEN: what problem does MCP Protocol Serving and Transports solve, for whom, and what did they do before it existed? Not
recoverable from code.

## Business value

OPEN: unrecoverable. No metric, target or business case appears anywhere in the repository for
this feature.

## Target users

OPEN: the actors are listed in `../ddd/domain_*-mcp-protocol-serving-and-transports.md`, derived from auth roles and
endpoint consumers. Which of them this feature was built *for* is not stated.

## User stories

**F-002-US1.** As a consumer of MCP Protocol Serving and Transports, I can manage a2a.

I: inferred from 30 route decorators carrying POST on `/_internal/a2a` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:9973].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/_internal/a2a` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US2.** As a consumer of MCP Protocol Serving and Transports, I can manage mcp.

I: inferred from 57 route decorators carrying DELETE, POST on `/_internal/mcp` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:8122].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/_internal/mcp` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US3.** As a consumer of MCP Protocol Serving and Transports, I can manage sessions.

I: inferred from 2 route decorators carrying POST on `/appbridge/sessions` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:10663].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/appbridge/sessions` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US4.** As a consumer of MCP Protocol Serving and Transports, I can manage cancel.

I: inferred from 1 route decorators carrying POST on `/cancellation/cancel` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/cancellation_router.py:68].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/cancellation/cancel` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US5.** As a consumer of MCP Protocol Serving and Transports, I can read status.

I: inferred from 1 route decorators carrying GET on `/cancellation/status` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/cancellation_router.py:110].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/cancellation/status` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US6.** As a consumer of MCP Protocol Serving and Transports, I can manage mcp.

I: inferred from 1 route decorators carrying POST on `/mcp` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/translate.py:2025].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/mcp` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US7.** As a consumer of MCP Protocol Serving and Transports, I can manage message.

I: inferred from 1 route decorators carrying POST on `/message` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12268].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/message` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US8.** As a consumer of MCP Protocol Serving and Transports, I can manage completion.

I: inferred from 1 route decorators carrying POST on `/protocol/completion` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4087].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/protocol/completion` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US9.** As a consumer of MCP Protocol Serving and Transports, I can manage initialize.

I: inferred from 1 route decorators carrying POST on `/protocol/initialize` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:3992].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/protocol/initialize` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US10.** As a consumer of MCP Protocol Serving and Transports, I can manage notifications.

I: inferred from 1 route decorators carrying POST on `/protocol/notifications` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4052].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/protocol/notifications` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US11.** As a consumer of MCP Protocol Serving and Transports, I can manage ping.

I: inferred from 1 route decorators carrying POST on `/protocol/ping` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4024].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/protocol/ping` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US12.** As a consumer of MCP Protocol Serving and Transports, I can manage sampling.

I: inferred from 1 route decorators carrying POST on `/protocol/sampling` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4112].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/protocol/sampling` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US13.** As a consumer of MCP Protocol Serving and Transports, I can manage sessions.

I: inferred from 3 route decorators carrying DELETE, GET, POST on `/reverse-proxy/sessions` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/reverse_proxy.py:328].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/reverse-proxy/sessions` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US14.** As a consumer of MCP Protocol Serving and Transports, I can read sse.

I: inferred from 1 route decorators carrying GET on `/reverse-proxy/sse` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/reverse_proxy.py:502].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/reverse-proxy/sse` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US15.** As a consumer of MCP Protocol Serving and Transports, I can read ws.

I: inferred from 1 route decorators carrying WEBSOCKET on `/reverse-proxy/ws` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/reverse_proxy.py:239].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/reverse-proxy/ws` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US16.** As a consumer of MCP Protocol Serving and Transports, I can manage rpc.

I: inferred from 2 route decorators carrying POST on `/rpc` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:8106].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/rpc` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US17.** As a consumer of MCP Protocol Serving and Transports, I can read sse.

I: inferred from 1 route decorators carrying GET on `/sse` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12161].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/sse` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

**F-002-US18.** As a consumer of MCP Protocol Serving and Transports, I can read ws.

I: inferred from 1 route decorators carrying WEBSOCKET on `/ws` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12079].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/ws` are listed in `../tests/test_v1.0.10_F-002.md` and are the nearest available evidence that the behaviour is intended.

## Non-functional requirements

OPEN: no SLO, latency target, throughput target or availability target appears in the repository
for this feature.

Where a number **is** configured, it is a real find and is recorded in
`../architect/feature_v1.0.10_F-002_architect.md` rather than guessed at here.

## Out of scope

OPEN: unrecoverable. Code records what was built and keeps no record of what was declined.

## Implementation status

States and what `done` costs: `../status-model.md`. A story is never more done than the test cases
that cover it.

| Story | Status | Evidence |
| --- | --- | --- |
| F-002-US1 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US2 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US3 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US4 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US5 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US6 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US7 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US8 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US9 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US10 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US11 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US12 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US13 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US14 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US15 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US16 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US17 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-002-US18 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |

## Open questions

- OPEN: What is the complete live operation list? It is the 27 literal JSON-RPC methods plus every row in `tools` — a runtime value this repository cannot state.
- OPEN: Which MCP protocol revision is targeted, and what happens when a client negotiates a different one?
- OPEN: What is the target p95 for `tools/call`? No SLO appears in the repository.
