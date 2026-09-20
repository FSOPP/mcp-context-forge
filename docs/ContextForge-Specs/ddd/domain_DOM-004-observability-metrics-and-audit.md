---
title: Domain — Observability, Metrics and Audit
id: DOM-004
kind: domain
feature: F-004
status: as-built
owner: TBD
updated: 2026-09-20
---

# Domain — Observability, Metrics and Audit

> Reconstructed from code. Rules below were promoted from constraint comments written by the
> people who knew them; each cites both the statement and the site enforcing it. Motive is not
> recoverable and is asked, not written.

## Ubiquitous language

| Term | Means | Do not use for |
| --- | --- | --- |
| Trace | one request's span tree | — |
| Rollup | the hourly aggregate of per-invocation metrics | — |
| Audit trail | the record of who changed what | structured log, which records what happened |

## Actors

| Actor | Role |
| --- | --- |
| Operator | reads traces, metrics and logs |
| Auditor | reads the audit trail |
| The gateway itself | writes every row here |

## Business rules

**DOM-004-R1.** Set trace_id in context variable for access throughout async call stack. Tokens are reset in the finally block below so stale trace/span context never bleeds into later requests that reuse the same task/context.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/middleware/observability_middleware.py:182].

**DOM-004-R2.** Always reset ContextVars so trace/span context never leaks into whatever request or task reuses this context next.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/middleware/observability_middleware.py:302].

**DOM-004-R3.** Get the configured auth header (default Authorization) and parse the Bearer scheme case-insensitively. Reading from the configured header keeps token scoping aligned with the auth dependency so scope restrictions cannot be bypassed by setting AUTH_HEADER_NAME.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/middleware/token_scoping.py:490].

**DOM-004-R4.** Each source over-fetches at most `limit`, so the merged top-`limit` is exact; the id tiebreak (also in each source's ORDER BY) keeps timestamp ties deterministic.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/routers/log_search.py:1095].

**DOM-004-R5.** Unified feed entry derived from AuditTrail or SecurityEvent rows. The server owns presentation: title, description, and status are rendered here and MUST NOT be re-derived by clients (contract: #5129 / #5944).

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/routers/log_search.py:304].

**DOM-004-R6.** Discard the holder task and log any exception that escaped. asyncio's "Task exception was never retrieved" warning at GC time is unreliable; this captures the failure into the standard logger immediately.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/notification_service.py:696].

**DOM-004-R7.** No holder for this id — common case (downstream responded after the holder TTL'd, or the id never had a holder because the request was dispatched the legacy SDK way).

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/notification_service.py:866].

**DOM-004-R8.** Return whether public ``/mcp`` should be served directly by Rust. Returns: ``True`` only when the Rust runtime is enabled and Rust can safely own steady-state public MCP session traffic.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/version.py:508].

**DOM-004-R9.** Return whether Rust should own the effective public MCP session stack. Returns: ``True`` only when the public MCP transport and session semantics should stay on the Rust-backed path.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/version.py:518].

## Process flow

The process is the API surface: 34 route decorators, listed in `../data/api-contract_v1.0.10_F-004.md`, and the call sequence is in `../architect/feature_v1.0.10_F-004_architect.md` § Sequence. It is written there once rather than paraphrased here.

## Invariants

Database-level invariants for this feature are the `required` and key declarations in `../data/schema/schemas.json`, derived from the column definitions. `../data/data-erd_v1.0.10_F-004.md` lists them per table.

OPEN: which invariants are enforced only in application code and would survive a direct database write? The column constraints are visible; the guard clauses were not inventoried.

## Implementation status

States and what `done` costs: `../status-model.md`. Every row starts at `todo`; a rule reaches
`done` only when a test names the rule ID and that test passed here.

| Rule | Status | Evidence |
| --- | --- | --- |
| DOM-004-R1 | wip — implemented, no test names this rule ID | — |
| DOM-004-R2 | wip — implemented, no test names this rule ID | — |
| DOM-004-R3 | wip — implemented, no test names this rule ID | — |
| DOM-004-R4 | wip — implemented, no test names this rule ID | — |
| DOM-004-R5 | wip — implemented, no test names this rule ID | — |
| DOM-004-R6 | wip — implemented, no test names this rule ID | — |
| DOM-004-R7 | wip — implemented, no test names this rule ID | — |
| DOM-004-R8 | wip — implemented, no test names this rule ID | — |
| DOM-004-R9 | wip — implemented, no test names this rule ID | — |

## Open questions

- OPEN: What is the retention policy for traces, spans and per-invocation metrics? The tables grow without bound and no code in the survey deletes from them except `delete_old_traces`, whose schedule is not set here.
- OPEN: Is the loss of an audit record acceptable? `log_action` swallows its own exceptions, so a failure is silent by construction.
- OPEN: What is this deployment's actual concurrency, against the 4-6 independent sessions each traced request opens?
- OPEN: which of the rules above the business would still hold if the code stopped enforcing them?
  A rule recovered from an enforcement site cannot distinguish policy from implementation detail.
