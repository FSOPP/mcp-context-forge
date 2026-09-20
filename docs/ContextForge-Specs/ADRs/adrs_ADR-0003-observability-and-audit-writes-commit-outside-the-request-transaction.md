---
title: ADR-0003 — Observability and audit writes commit outside the request transaction
id: ADR-0003
status: accepted
owner: TBD
updated: 2026-09-20
---

# ADR-0003 — Observability and audit writes commit outside the request transaction

## Status

Accepted — **reconstructed from code, 2026-09-20**. Rationale not recovered.

This record was written by reading the codebase, not by the people who made the decision. The
Context and Consequences below are facts with citations. The Alternatives section is empty on
purpose.

## Context

Observability write methods open their own `SessionLocal()` and commit immediately
[D: mcpgateway/services/observability_service.py:228]. `AuditTrailService.log_action` does the
same and additionally swallows its own exceptions, returning `None` on failure
[D: mcpgateway/services/audit_trail_service.py:73]. Callers are instructed never to pass the
request-scoped session in, because a second commit on an already-committed session breaks rollback
[D: CLAUDE.md:255]. A traced request opens four to six independent sessions
[D: mcpgateway/config.py:3661].

## Decision

Telemetry and audit rows persist independently of the request that produced them. They
are not atomic with it [D: mcpgateway/services/observability_service.py:228].

## Alternatives considered

OPEN: not recoverable. The repository retains no record of what was rejected, and inventing a
plausible alternatives table here would foreclose the discussion this record exists to reopen.

## Consequences

A failed request still leaves a trace, which is the visibility this buys. An audit write
can fail silently. A caller's generic exception handler still rolls back and reports an error to
the API caller even when the underlying row was already committed [D: CLAUDE.md:255]. Connection
pool sizing becomes a first-order deployment concern.

## Links

- `../architect/architect.md` § Decision index
- `../architect/architect_common.md` § Design patterns

## Open questions

- OPEN: who made this decision, when, and against what constraint?
- OPEN: what would have to change for it to be revisited?
- OPEN: was an alternative tried and abandoned? A discarded branch leaves no trace in a working
  tree.
