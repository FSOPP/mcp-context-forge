---
title: PRD v1.0.10 F-011 — Rust MCP Runtime
id: F-011
status: as-built
owner: TBD
updated: 2026-09-20
---

# PRD v1.0.10 F-011 — Rust MCP Runtime

> **Read the warning first.** A PRD states intent, and intent is not in a repository. Every story
> below was inferred backwards from endpoints and test names; not one of them is evidence that the
> feature was wanted, only that it exists. Business value, priority, metrics and personas are
> `OPEN:` throughout, and that is the honest answer rather than a gap to fill in later.
>
> This document deliberately holds no path and no schema. Those live in
> `../data/api-contract_v1.0.10_F-011.md` and `../data/schema/schemas.json`.

## Problem statement

OPEN: what problem does Rust MCP Runtime solve, for whom, and what did they do before it existed? Not
recoverable from code.

## Business value

OPEN: unrecoverable. No metric, target or business case appears anywhere in the repository for
this feature.

## Target users

OPEN: the actors are listed in `../ddd/domain_*-rust-mcp-runtime.md`, derived from auth roles and
endpoint consumers. Which of them this feature was built *for* is not stated.

## User stories

**F-011-US1.** As a consumer of Rust MCP Runtime, I can manage event store.

I: inferred from 2 route decorators carrying POST on `/_internal/event-store` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: crates/mcp_runtime/src/lib.rs:1353].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/_internal/event-store` are listed in `../tests/test_v1.0.10_F-011.md` and are the nearest available evidence that the behaviour is intended.

**F-011-US2.** As a consumer of Rust MCP Runtime, I can read health.

I: inferred from 2 route decorators carrying GET on `/health` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: crates/mcp_runtime/src/lib.rs:1350].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/health` are listed in `../tests/test_v1.0.10_F-011.md` and are the nearest available evidence that the behaviour is intended.

**F-011-US3.** As a consumer of Rust MCP Runtime, I can read healthz.

I: inferred from 2 route decorators carrying GET on `/healthz` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: crates/mcp_runtime/src/lib.rs:1351].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/healthz` are listed in `../tests/test_v1.0.10_F-011.md` and are the nearest available evidence that the behaviour is intended.

**F-011-US4.** As a consumer of Rust MCP Runtime, I can read mcp.

I: inferred from 4 route decorators carrying GET on `/mcp` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: crates/mcp_runtime/src/lib.rs:1359].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/mcp` are listed in `../tests/test_v1.0.10_F-011.md` and are the nearest available evidence that the behaviour is intended.

**F-011-US5.** As a consumer of Rust MCP Runtime, I can manage rpc.

I: inferred from 4 route decorators carrying POST on `/rpc` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: crates/mcp_runtime/src/lib.rs:1357].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/rpc` are listed in `../tests/test_v1.0.10_F-011.md` and are the nearest available evidence that the behaviour is intended.

**F-011-US6.** As a consumer of Rust MCP Runtime, I can read mcp.

I: inferred from 4 route decorators carrying GET on `/servers/mcp` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: crates/mcp_runtime/src/lib.rs:1367].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/servers/mcp` are listed in `../tests/test_v1.0.10_F-011.md` and are the nearest available evidence that the behaviour is intended.

## Non-functional requirements

OPEN: no SLO, latency target, throughput target or availability target appears in the repository
for this feature.

Where a number **is** configured, it is a real find and is recorded in
`../architect/feature_v1.0.10_F-011_architect.md` rather than guessed at here.

## Out of scope

OPEN: unrecoverable. Code records what was built and keeps no record of what was declined.

## Implementation status

States and what `done` costs: `../status-model.md`. A story is never more done than the test cases
that cover it.

| Story | Status | Evidence |
| --- | --- | --- |
| F-011-US1 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-011-US2 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-011-US3 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-011-US4 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-011-US5 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-011-US6 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |

## Open questions

- OPEN: When should an operator run the Rust runtime instead of the Python path? Both serve MCP and nothing states the trade-off.
- OPEN: What is the compatibility contract across the `/_internal/**` boundary?
