---
title: ADR-0005 — A Rust sidecar terminates MCP traffic
id: ADR-0005
status: accepted
owner: TBD
updated: 2026-09-20
---

# ADR-0005 — A Rust sidecar terminates MCP traffic

## Status

Accepted — **reconstructed from code, 2026-09-20**. Rationale not recovered.

This record was written by reading the codebase, not by the people who made the decision. The
Context and Consequences below are facts with citations. The Alternatives section is empty on
purpose.

## Context

`crates/mcp_runtime` is a separate Cargo package of roughly 23,000 lines
[D: crates/mcp_runtime/Cargo.toml:1]. It calls the Python gateway over `/_internal/**`
[D: crates/mcp_runtime/src/lib.rs:2132] and serves two routes of its own for a resumable event
store that has no Python counterpart [D: crates/mcp_runtime/src/lib.rs:1352]. Authorisation across
the boundary is a trust predicate plus an encoded auth context, not RBAC
[D: mcpgateway/auth_context.py:638]. Startup requires an internal auth secret
[D: crates/mcp_runtime/src/lib.rs:721]. The Python side keeps a setting naming which runtime owns
event-store semantics, marked deprecated [D: mcpgateway/config.py:281].

## Decision

MCP termination may run in the Rust daemon, with the Python gateway reached over an
internal HTTP surface [D: crates/mcp_runtime/src/lib.rs:2132].

## Alternatives considered

OPEN: not recoverable. The repository retains no record of what was rejected, and inventing a
plausible alternatives table here would foreclose the discussion this record exists to reopen.

## Consequences

Two implementations of overlapping behaviour are live at once, in two languages, with
no declared version contract between them. A cross-runtime invariant must be enforced on both
sides, which the code already does in at least one place
[D: mcpgateway/utils/uaid.py:282]. The internal surface becomes a security boundary requiring its
own gate [D: mcpgateway/auth_context.py:638].

## Links

- `../architect/architect.md` § Decision index
- `../architect/architect_common.md` § Design patterns

## Open questions

- OPEN: who made this decision, when, and against what constraint?
- OPEN: what would have to change for it to be revisited?
- OPEN: was an alternative tried and abandoned? A discarded branch leaves no trace in a working
  tree.
