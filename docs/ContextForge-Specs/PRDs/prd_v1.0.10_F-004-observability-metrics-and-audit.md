---
title: PRD v1.0.10 F-004 — Observability, Metrics and Audit
id: F-004
status: as-built
owner: TBD
updated: 2026-09-20
---

# PRD v1.0.10 F-004 — Observability, Metrics and Audit

> **Read the warning first.** A PRD states intent, and intent is not in a repository. Every story
> below was inferred backwards from endpoints and test names; not one of them is evidence that the
> feature was wanted, only that it exists. Business value, priority, metrics and personas are
> `OPEN:` throughout, and that is the honest answer rather than a gap to fill in later.
>
> This document deliberately holds no path and no schema. Those live in
> `../data/api-contract_v1.0.10_F-004.md` and `../data/schema/schemas.json`.

## Problem statement

OPEN: what problem does Observability, Metrics and Audit solve, for whom, and what did they do before it existed? Not
recoverable from code.

## Business value

OPEN: unrecoverable. No metric, target or business case appears anywhere in the repository for
this feature.

## Target users

OPEN: the actors are listed in `../ddd/domain_*-observability-metrics-and-audit.md`, derived from auth roles and
endpoint consumers. Which of them this feature was built *for* is not stated.

## User stories

**F-004-US1.** As a consumer of Observability, Metrics and Audit, I can manage logs.

I: inferred from 6 route decorators carrying GET, POST on `/api/logs` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/log_search.py:1021].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/api/logs` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US2.** As a consumer of Observability, Metrics and Audit, I can manage metrics.

I: inferred from 4 route decorators carrying GET, POST on `/api/metrics` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/metrics_maintenance.py:104].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/api/metrics` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US3.** As a consumer of Observability, Metrics and Audit, I can read frameworks.

I: inferred from 1 route decorators carrying GET on `/compliance/frameworks` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/compliance_router.py:124].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/compliance/frameworks` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US4.** As a consumer of Observability, Metrics and Audit, I can manage reports.

I: inferred from 4 route decorators carrying GET, POST on `/compliance/reports` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/compliance_router.py:187].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/compliance/reports` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US5.** As a consumer of Observability, Metrics and Audit, I can read health.

I: inferred from 1 route decorators carrying GET on `/health` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12424].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/health` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US6.** As a consumer of Observability, Metrics and Audit, I can read security.

I: inferred from 1 route decorators carrying GET on `/health/security` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12558].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/health/security` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US7.** As a consumer of Observability, Metrics and Audit, I can read healthz.

I: inferred from 1 route decorators carrying GET on `/healthz` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/translate.py:875].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/healthz` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US8.** As a consumer of Observability, Metrics and Audit, I can manage setLevel.

I: inferred from 1 route decorators carrying POST on `/logging/setLevel` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12315].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/logging/setLevel` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US9.** As a consumer of Observability, Metrics and Audit, I can read metrics.

I: inferred from 1 route decorators carrying GET on `/metrics` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12343].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/metrics` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US10.** As a consumer of Observability, Metrics and Audit, I can read prometheus.

I: inferred from 1 route decorators carrying GET on `/metrics/prometheus` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/services/metrics.py:467].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/metrics/prometheus` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US11.** As a consumer of Observability, Metrics and Audit, I can manage reset.

I: inferred from 1 route decorators carrying POST on `/metrics/reset` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12375].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/metrics/reset` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US12.** As a consumer of Observability, Metrics and Audit, I can read analytics.

I: inferred from 1 route decorators carrying GET on `/observability/analytics` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/observability.py:678].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/observability/analytics` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US13.** As a consumer of Observability, Metrics and Audit, I can read metrics.

I: inferred from 2 route decorators carrying GET on `/observability/metrics` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/observability.py:921].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/observability/metrics` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US14.** As a consumer of Observability, Metrics and Audit, I can read spans.

I: inferred from 1 route decorators carrying GET on `/observability/spans` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/observability.py:328].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/observability/spans` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US15.** As a consumer of Observability, Metrics and Audit, I can read stats.

I: inferred from 1 route decorators carrying GET on `/observability/stats` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/observability.py:431].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/observability/stats` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US16.** As a consumer of Observability, Metrics and Audit, I can manage traces.

I: inferred from 5 route decorators carrying DELETE, GET, POST on `/observability/traces` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/routers/observability.py:77].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/observability/traces` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US17.** As a consumer of Observability, Metrics and Audit, I can read ready.

I: inferred from 1 route decorators carrying GET on `/ready` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/main.py:12492].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/ready` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

**F-004-US18.** As a consumer of Observability, Metrics and Audit, I can read version.

I: inferred from 1 route decorators carrying GET on `/version` — basis: an endpoint is evidence the behaviour exists, not that it was wanted [D: mcpgateway/version.py:1259].

Acceptance criteria: OPEN — no criterion is stated anywhere. The tests covering `/version` are listed in `../tests/test_v1.0.10_F-004.md` and are the nearest available evidence that the behaviour is intended.

## Non-functional requirements

OPEN: no SLO, latency target, throughput target or availability target appears in the repository
for this feature.

Where a number **is** configured, it is a real find and is recorded in
`../architect/feature_v1.0.10_F-004_architect.md` rather than guessed at here.

## Out of scope

OPEN: unrecoverable. Code records what was built and keeps no record of what was declined.

## Implementation status

States and what `done` costs: `../status-model.md`. A story is never more done than the test cases
that cover it.

| Story | Status | Evidence |
| --- | --- | --- |
| F-004-US1 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US2 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US3 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US4 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US5 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US6 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US7 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US8 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US9 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US10 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US11 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US12 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US13 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US14 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US15 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US16 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US17 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |
| F-004-US18 | wip — unverified, no test case names this story; needs per-test coverage attribution | — |

## Open questions

- OPEN: What is the retention policy for traces, spans and per-invocation metrics? The tables grow without bound and no code in the survey deletes from them except `delete_old_traces`, whose schedule is not set here.
- OPEN: Is the loss of an audit record acceptable? `log_action` swallows its own exceptions, so a failure is silent by construction.
- OPEN: What is this deployment's actual concurrency, against the 4-6 independent sessions each traced request opens?
