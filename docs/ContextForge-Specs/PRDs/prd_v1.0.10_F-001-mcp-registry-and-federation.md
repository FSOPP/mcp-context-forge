---
title: PRD v1.0.10 F-001 — MCP Registry and Federation
id: F-001
status: as-built
owner: TBD
updated: 2026-09-20
---

# PRD v1.0.10 F-001 — MCP Registry and Federation

> **Read the warning first.** A PRD states intent, and intent is not in a repository. Every story
> below was inferred backwards from endpoints and test names; not one of them is evidence that the
> feature was wanted, only that it exists. Business value, priority, metrics and personas are
> `OPEN:` throughout, and that is the honest answer rather than a gap to fill in later.
>
> This document deliberately holds no path and no schema. Those live in
> `../data/api-contract_v1.0.10_F-001.md` and `../data/schema/schemas.json`.

## Problem statement

OPEN: what problem does MCP Registry and Federation solve, for whom, and what did they do before it existed? Not
recoverable from code.

## Business value

OPEN: unrecoverable. No metric, target or business case appears anywhere in the repository for
this feature.

## Target users

OPEN: the actors are listed in `../ddd/domain_*-mcp-registry-and-federation.md`, derived from auth roles and
endpoint consumers. Which of them this feature was built *for* is not stated.

## User stories

**F-001-US1.** As a consumer of MCP Registry and Federation, I can read catalog.

I: inferred from 1 route decorators carrying GET on `/catalog` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/catalog.py:27].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/catalog` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US2.** As a consumer of MCP Registry and Federation, I can manage register.

I: inferred from 1 route decorators carrying POST on `/catalog/register` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/catalog.py:86].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/catalog/register` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US3.** As a consumer of MCP Registry and Federation, I can read export.

I: inferred from 1 route decorators carrying GET on `/export` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12711].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/export` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US4.** As a consumer of MCP Registry and Federation, I can manage selective.

I: inferred from 1 route decorators carrying POST on `/export/selective` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12803].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/export/selective` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US5.** As a consumer of MCP Registry and Federation, I can manage gateways.

I: inferred from 7 route decorators carrying DELETE, GET, POST, PUT on `/gateways` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:7391].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/gateways` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US6.** As a consumer of MCP Registry and Federation, I can read impact preview.

I: inferred from 1 route decorators carrying GET on `/gateways/impact-preview` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:7599].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/gateways/impact-preview` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US7.** As a consumer of MCP Registry and Federation, I can manage state.

I: inferred from 1 route decorators carrying POST on `/gateways/state` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:7320].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/gateways/state` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US8.** As a consumer of MCP Registry and Federation, I can manage toggle.

I: inferred from 1 route decorators carrying POST on `/gateways/toggle` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:7365].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/gateways/toggle` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US9.** As a consumer of MCP Registry and Federation, I can manage tools.

I: inferred from 1 route decorators carrying POST on `/gateways/tools` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:7764].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/gateways/tools` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US10.** As a consumer of MCP Registry and Federation, I can manage import.

I: inferred from 1 route decorators carrying POST on `/import` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12872].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/import` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US11.** As a consumer of MCP Registry and Federation, I can manage cleanup.

I: inferred from 1 route decorators carrying POST on `/import/cleanup` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12992].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/import/cleanup` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US12.** As a consumer of MCP Registry and Federation, I can read status.

I: inferred from 2 route decorators carrying GET on `/import/status` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12974].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/import/status` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US13.** As a consumer of MCP Registry and Federation, I can manage test.

I: inferred from 1 route decorators carrying POST on `/mcp-servers/test` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/mcp_servers_router.py:67].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/mcp-servers/test` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US14.** As a consumer of MCP Registry and Federation, I can manage test handshake.

I: inferred from 1 route decorators carrying POST on `/mcp-servers/test-handshake` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/mcp_servers_router.py:107].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/mcp-servers/test-handshake` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US15.** As a consumer of MCP Registry and Federation, I can manage prompts.

I: inferred from 8 route decorators carrying DELETE, GET, POST, PUT on `/prompts` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:6883].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/prompts` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US16.** As a consumer of MCP Registry and Federation, I can manage state.

I: inferred from 1 route decorators carrying POST on `/prompts/state` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:6815].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/prompts/state` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US17.** As a consumer of MCP Registry and Federation, I can manage toggle.

I: inferred from 1 route decorators carrying POST on `/prompts/toggle` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:6857].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/prompts/toggle` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US18.** As a consumer of MCP Registry and Federation, I can manage resources.

I: inferred from 7 route decorators carrying DELETE, GET, POST, PUT on `/resources` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:6316].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/resources` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US19.** As a consumer of MCP Registry and Federation, I can read info.

I: inferred from 1 route decorators carrying GET on `/resources/info` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:6622].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/resources/info` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US20.** As a consumer of MCP Registry and Federation, I can manage state.

I: inferred from 1 route decorators carrying POST on `/resources/state` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:6248].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/resources/state` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US21.** As a consumer of MCP Registry and Federation, I can manage subscribe.

I: inferred from 1 route decorators carrying POST on `/resources/subscribe` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:6777].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/resources/subscribe` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US22.** As a consumer of MCP Registry and Federation, I can read templates.

I: inferred from 1 route decorators carrying GET on `/resources/templates` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:6200].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/resources/templates` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US23.** As a consumer of MCP Registry and Federation, I can read test.

I: inferred from 1 route decorators carrying GET on `/resources/test` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:6498].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/resources/test` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US24.** As a consumer of MCP Registry and Federation, I can manage toggle.

I: inferred from 1 route decorators carrying POST on `/resources/toggle` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:6290].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/resources/toggle` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US25.** As a consumer of MCP Registry and Federation, I can manage roots.

I: inferred from 7 route decorators carrying DELETE, GET, POST, PUT on `/roots` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:7837].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/roots` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US26.** As a consumer of MCP Registry and Federation, I can read changes.

I: inferred from 1 route decorators carrying GET on `/roots/changes` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:7926].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/roots/changes` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US27.** As a consumer of MCP Registry and Federation, I can read export.

I: inferred from 1 route decorators carrying GET on `/roots/export` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:7861].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/roots/export` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US28.** As a consumer of MCP Registry and Federation, I can read search.

I: inferred from 1 route decorators carrying GET on `/search` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/search.py:37].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/search` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US29.** As a consumer of MCP Registry and Federation, I can manage servers.

I: inferred from 7 route decorators carrying DELETE, GET, POST, PUT on `/servers` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4139].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/servers` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US30.** As a consumer of MCP Registry and Federation, I can read .well known.

I: inferred from 2 route decorators carrying GET on `/servers/.well-known` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/server_well_known.py:37].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/servers/.well-known` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US31.** As a consumer of MCP Registry and Federation, I can manage message.

I: inferred from 1 route decorators carrying POST on `/servers/message` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4697].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/servers/message` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US32.** As a consumer of MCP Registry and Federation, I can read prompts.

I: inferred from 1 route decorators carrying GET on `/servers/prompts` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4853].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/servers/prompts` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US33.** As a consumer of MCP Registry and Federation, I can read resources.

I: inferred from 1 route decorators carrying GET on `/servers/resources` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4817].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/servers/resources` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US34.** As a consumer of MCP Registry and Federation, I can read sse.

I: inferred from 1 route decorators carrying GET on `/servers/sse` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4578].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/servers/sse` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US35.** As a consumer of MCP Registry and Federation, I can manage state.

I: inferred from 1 route decorators carrying POST on `/servers/state` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4400].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/servers/state` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US36.** As a consumer of MCP Registry and Federation, I can manage test handshake.

I: inferred from 1 route decorators carrying POST on `/servers/test-handshake` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4463].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/servers/test-handshake` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US37.** As a consumer of MCP Registry and Federation, I can manage toggle.

I: inferred from 1 route decorators carrying POST on `/servers/toggle` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4437].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/servers/toggle` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US38.** As a consumer of MCP Registry and Federation, I can read tools.

I: inferred from 1 route decorators carrying GET on `/servers/tools` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:4771].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/servers/tools` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US39.** As a consumer of MCP Registry and Federation, I can read tags.

I: inferred from 2 route decorators carrying GET on `/tags` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12605].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/tags` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US40.** As a consumer of MCP Registry and Federation, I can read entities.

I: inferred from 1 route decorators carrying GET on `/tags/entities` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12656].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/tags/entities` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US41.** As a consumer of MCP Registry and Federation, I can manage tools.

I: inferred from 7 route decorators carrying DELETE, GET, POST, PUT on `/tools` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:5686].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/tools` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US42.** As a consumer of MCP Registry and Federation, I can manage generate schemas from openapi.

I: inferred from 1 route decorators carrying POST on `/tools/generate-schemas-from-openapi` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/openapi_schema_router.py:43].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/tools/generate-schemas-from-openapi` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US43.** As a consumer of MCP Registry and Federation, I can manage plugin_bindings.

I: inferred from 5 route decorators carrying DELETE, GET, POST on `/tools/plugin_bindings` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/tool_plugin_bindings.py:220].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/tools/plugin_bindings` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US44.** As a consumer of MCP Registry and Federation, I can manage preview.

I: inferred from 1 route decorators carrying POST on `/tools/preview` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:5898].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/tools/preview` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US45.** As a consumer of MCP Registry and Federation, I can manage state.

I: inferred from 1 route decorators carrying POST on `/tools/state` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:6128].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/tools/state` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

**F-001-US46.** As a consumer of MCP Registry and Federation, I can manage toggle.

I: inferred from 1 route decorators carrying POST on `/tools/toggle` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:6170].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/tools/toggle` are listed in `../tests/test_v1.0.10_F-001.md` and are the nearest available evidence that the behaviour is intended.

## Non-functional requirements

OPEN: no SLO, latency target, throughput target or availability target appears in the repository
for this feature.

Where a number **is** configured, it is a real find and is recorded in
`../architect/feature_v1.0.10_F-001_architect.md` rather than guessed at here.

## Out of scope

OPEN: unrecoverable. Code records what was built and keeps no record of what was declined.

## Implementation status

States and what `done` costs: `../status-model.md`. A story is never more done than the test cases
that cover it.

| Story | Status | Evidence |
| --- | --- | --- |
| F-001-US1 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US2 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US3 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US4 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US5 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US6 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US7 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US8 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US9 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US10 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US11 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US12 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US13 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US14 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US15 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US16 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US17 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US18 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US19 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US20 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US21 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US22 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US23 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US24 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US25 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US26 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US27 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US28 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US29 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US30 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US31 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US32 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US33 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US34 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US35 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US36 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US37 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US38 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US39 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US40 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US41 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US42 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US43 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US44 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US45 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-001-US46 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |

## Open questions

- OPEN: What is the intended lifecycle of a discovered tool whose upstream gateway is deleted? The schema keeps the rows; no code path in the survey deletes them.
- OPEN: Why do `/gateways` and `/mcp-servers` both exist? The rename is visible; the plan and the removal date are not.
- OPEN: What is the expected upper bound on federated gateways per deployment? No limit is configured anywhere.
