---
title: PRD v1.0.10 F-012 — Deployment and Operations
id: F-012
status: as-built
owner: TBD
updated: 2026-09-20
---

# PRD v1.0.10 F-012 — Deployment and Operations

> **Read the warning first.** A PRD states intent, and intent is not in a repository. Every story
> below was inferred backwards from endpoints and test names; not one of them is evidence that the
> feature was wanted, only that it exists. Business value, priority, metrics and personas are
> `OPEN:` throughout, and that is the honest answer rather than a gap to fill in later.
>
> This document deliberately holds no path and no schema. Those live in
> `../data/api-contract_v1.0.10_F-012.md` and `../data/schema/schemas.json`.

## Problem statement

OPEN: what problem does Deployment and Operations solve, for whom, and what did they do before it existed? Not
recoverable from code.

## Business value

OPEN: unrecoverable. No metric, target or business case appears anywhere in the repository for
this feature.

## Target users

OPEN: the actors are listed in `../ddd/domain_*-deployment-and-operations.md`, derived from auth roles and
endpoint consumers. Which of them this feature was built *for* is not stated.

## User stories

F-012 exposes no endpoint, so no story is inferred from one.

OPEN: what does a user of this feature actually want from it? Nothing in the code expresses a goal, and inventing one here would be the exact failure this hub guards against.

## Non-functional requirements

OPEN: no SLO, latency target, throughput target or availability target appears in the repository
for this feature.

Where a number **is** configured, it is a real find and is recorded in
`../architect/feature_v1.0.10_F-012_architect.md` rather than guessed at here.

## Out of scope

OPEN: unrecoverable. Code records what was built and keeps no record of what was declined.

## Implementation status

States and what `done` costs: `../status-model.md`. A story is never more done than the test cases
that cover it.

| Story | Status | Evidence |
| --- | --- | --- |
| — | — | no stories inferred |

## Open questions

- OPEN: Which deployment topology is the supported one? Nine compose files and a Helm chart describe several, and none is marked canonical.
- OPEN: What are the production sizing targets? `DB_POOL_SIZE` guidance exists in prose but no target load is stated.
- OPEN: What is the rollback procedure for a failed migration?
