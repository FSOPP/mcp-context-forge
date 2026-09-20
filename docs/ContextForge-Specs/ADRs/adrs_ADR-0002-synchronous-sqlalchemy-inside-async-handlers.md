---
title: ADR-0002 — Synchronous SQLAlchemy inside async handlers
id: ADR-0002
status: accepted
owner: TBD
updated: 2026-09-20
---

# ADR-0002 — Synchronous SQLAlchemy inside async handlers

## Status

Accepted — **reconstructed from code, 2026-09-20**. Rationale not recovered.

This record was written by reading the codebase, not by the people who made the decision. The
Context and Consequences below are facts with citations. The Alternatives section is empty on
purpose.

## Context

`SessionLocal()` is used from async FastAPI handlers and from ASGI middleware rather than
an async database driver [D: mcpgateway/services/observability_service.py:228]. The repository
states this is a deliberate decision and instructs reviewers not to flag it or convert individual
call sites [D: CLAUDE.md:429]. It also states the decision may be revisited alongside a migration
to async drivers [D: CLAUDE.md:429].

## Decision

Synchronous sessions remain in async handlers. Individual call sites are not converted.
Any change is a coordinated migration, not a local fix [D: CLAUDE.md:429].

## Alternatives considered

OPEN: not recoverable. The repository retains no record of what was rejected, and inventing a
plausible alternatives table here would foreclose the discussion this record exists to reopen.

## Consequences

The blocking call occupies an event-loop worker for its duration, which makes pool
sizing a correctness concern rather than a tuning one [D: mcpgateway/config.py:3661]. Reviewers
must know the decision exists, because the pattern reads as a bug on sight.

## Links

- `../architect/architect.md` § Decision index
- `../architect/architect_common.md` § Design patterns

## Open questions

- OPEN: who made this decision, when, and against what constraint?
- OPEN: what would have to change for it to be revisited?
- OPEN: was an alternative tried and abandoned? A discarded branch leaves no trace in a working
  tree.
