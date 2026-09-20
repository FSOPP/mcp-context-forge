---
title: ADR-0006 — Identity is joined on email rather than on the user primary key
id: ADR-0006
status: accepted
owner: TBD
updated: 2026-09-20
---

# ADR-0006 — Identity is joined on email rather than on the user primary key

## Status

Accepted — **reconstructed from code, 2026-09-20**. Rationale not recovered.

This record was written by reading the codebase, not by the people who made the decision. The
Context and Consequences below are facts with citations. The Alternatives section is empty on
purpose.

## Context

`email_users` declares an `id` primary key [D: mcpgateway/db.py:1516]. Twenty-one tables
in the identity group declare their foreign keys against `email_users.email` instead
[D: mcpgateway/db.py:1223]. Several of those use `ondelete="CASCADE"`
[D: mcpgateway/db.py:1884].

## Decision

`email_users.email` is the join key across the identity model
[D: mcpgateway/db.py:1223].

## Alternatives considered

OPEN: not recoverable. The repository retains no record of what was rejected, and inventing a
plausible alternatives table here would foreclose the discussion this record exists to reopen.

## Consequences

Changing a user's email address rewrites every referencing row. The email column must
carry a unique constraint for the foreign keys to be valid, which makes email a second primary
key in practice. An audit trail keyed on email stays readable without a join, which is the one
visible benefit [D: mcpgateway/db.py:1223].

## Links

- `../architect/architect.md` § Decision index
- `../architect/architect_common.md` § Design patterns

## Open questions

- OPEN: who made this decision, when, and against what constraint?
- OPEN: what would have to change for it to be revisited?
- OPEN: was an alternative tried and abandoned? A discarded branch leaves no trace in a working
  tree.
