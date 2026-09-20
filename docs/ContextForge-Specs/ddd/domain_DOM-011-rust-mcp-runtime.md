---
title: Domain — Rust MCP Runtime
id: DOM-011
kind: domain
feature: F-011
status: as-built
owner: TBD
updated: 2026-09-20
---

# Domain — Rust MCP Runtime

> Reconstructed from code. Rules below were promoted from constraint comments written by the
> people who knew them; each cites both the statement and the site enforcing it. Motive is not
> recoverable and is asked, not written.

## Ubiquitous language

| Term | Means | Do not use for |
| --- | --- | --- |
| Runtime | the Rust daemon | gateway, which is the Python application |

## Actors

| Actor | Role |
| --- | --- |
| Operator | runs the daemon alongside the gateway |

## Business rules

**DOM-011-R1.** Builds the shared application state for the Rust MCP runtime. # Errors Returns an error when the HTTP client, database pool, or Redis client cannot be initialized from the provided configuration.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: crates/mcp_runtime/src/lib.rs:714].

## Process flow

The process is the API surface: 18 route decorators, listed in `../data/api-contract_v1.0.10_F-011.md`, and the call sequence is in `../architect/feature_v1.0.10_F-011_architect.md` § Sequence. It is written there once rather than paraphrased here.

## Invariants

This feature persists nothing, so it declares no data invariant.

OPEN: what must stay true about this feature at runtime? Nothing in the code states it.

## Implementation status

States and what `done` costs: `../status-model.md`. Every row starts at `todo`; a rule reaches
`done` only when a test names the rule ID and that test passed here.

| Rule | Status | Evidence |
| --- | --- | --- |
| DOM-011-R1 | wip — implemented, no test names this rule ID | — |

## Open questions

- OPEN: When should an operator run the Rust runtime instead of the Python path? Both serve MCP and nothing states the trade-off.
- OPEN: What is the compatibility contract across the `/_internal/**` boundary?
- OPEN: which of the rules above the business would still hold if the code stopped enforcing them?
  A rule recovered from an enforcement site cannot distinguish policy from implementation detail.
