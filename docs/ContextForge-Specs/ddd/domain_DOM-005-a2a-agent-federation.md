---
title: Domain — A2A Agent Federation
id: DOM-005
kind: domain
feature: F-005
status: as-built
owner: TBD
updated: 2026-09-20
---

# Domain — A2A Agent Federation

> Reconstructed from code. Rules below were promoted from constraint comments written by the
> people who knew them; each cites both the statement and the site enforcing it. Motive is not
> recoverable and is asked, not written.

## Ubiquitous language

| Term | Means | Do not use for |
| --- | --- | --- |
| Agent | a registered A2A peer | tool, which is an MCP primitive |
| Task | one unit of agent work with a lifecycle | invocation, which is synchronous |
| UAID | the cross-gateway agent identifier | — |

## Actors

| Actor | Role |
| --- | --- |
| Platform administrator | registers agents and allowlists domains |
| A2A agent | executes tasks |
| Remote gateway | receives forwarded, RBAC-checked calls |

## Business rules

**DOM-005-R1.** Empty `hash_or_did` (e.g. `uaid:aid:;uid=0;...`) is rejected by the Rust counterpart via `MissingParams`; rejecting here too keeps the cross-runtime contract airtight so a mixed Python↔Rust federation chain never disagrees on whether a UAID is valid.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/utils/uaid.py:282].

**DOM-005-R2.** Encrypt webhook bearer token at rest. Rust push dispatch decrypts via the shared AES-GCM secret; anyone with raw DB access or a backup cannot recover webhook credentials.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/a2a_service.py:3491].

**DOM-005-R3.** Log at ERROR level — not WARNING. Default production LOG_LEVEL is ERROR (see CLAUDE.md), and a malformed hop token silently resets the federation counter to 0. That's a loop-protection bypass, not a lint; it must be visible under the default log level.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/utils/uaid.py:85].

## Process flow

The process is the API surface: 17 route decorators, listed in `../data/api-contract_v1.0.10_F-005.md`, and the call sequence is in `../architect/feature_v1.0.10_F-005_architect.md` § Sequence. It is written there once rather than paraphrased here.

## Invariants

Database-level invariants for this feature are the `required` and key declarations in `../data/schema/schemas.json`, derived from the column definitions. `../data/data-erd_v1.0.10_F-005.md` lists them per table.

OPEN: which invariants are enforced only in application code and would survive a direct database write? The column constraints are visible; the guard clauses were not inventoried.

## Implementation status

States and what `done` costs: `../status-model.md`. Every row starts at `todo`; a rule reaches
`done` only when a test names the rule ID and that test passed here.

| Rule | Status | Evidence |
| --- | --- | --- |
| DOM-005-R1 | wip — implemented, no test names this rule ID | — |
| DOM-005-R2 | wip — implemented, no test names this rule ID | — |
| DOM-005-R3 | wip — implemented, no test names this rule ID | — |

## Open questions

- OPEN: What is the trust model for a remote gateway in a cross-gateway call? Both sides must trust the same JWT issuer, and nothing states how that is established operationally.
- OPEN: What happens to an in-flight A2A task when its agent is deregistered?
- OPEN: which of the rules above the business would still hold if the code stopped enforcing them?
  A rule recovered from an enforcement site cannot distinguish policy from implementation detail.
