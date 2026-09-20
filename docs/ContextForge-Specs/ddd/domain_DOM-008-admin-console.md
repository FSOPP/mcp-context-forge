---
title: Domain — Admin Console
id: DOM-008
kind: domain
feature: F-008
status: as-built
owner: TBD
updated: 2026-09-20
---

# Domain — Admin Console

> Reconstructed from code. Rules below were promoted from constraint comments written by the
> people who knew them; each cites both the statement and the site enforcing it. Motive is not
> recoverable and is asked, not written.

## Ubiquitous language

| Term | Means | Do not use for |
| --- | --- | --- |
| Console | the server-rendered admin UI | Admin API, which is its HTTP surface |

## Actors

| Actor | Role |
| --- | --- |
| Console operator | performs every domain action through the UI |

## Business rules

**DOM-008-R1.** Reuse the standard admin auth helper: - sends Bearer auth when a JS-readable token exists - otherwise relies on same-origin cookie auth Never synthesize default credentials client-side.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/admin_ui/a2aAgents.js:837].

**DOM-008-R2.** Drive navigation through Alpine's reactive data directly so that prevPage() / nextPage()'s own hasPrev / hasNext guards are the authority — avoids relying on DOM button disabled state which may not be evaluated yet after an HTMX swap.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/admin_ui/events.js:992].

**DOM-008-R3.** Keep a checked public value enabled in edit forms so FormData includes visibility and we don't silently change saved state. This is intentionally one-way: once switched away from public in restricted team scope, public cannot be re-selected.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/admin_ui/teams.js:1139].

## Process flow

The process is the API surface: 231 route decorators, listed in `../data/api-contract_v1.0.10_F-008.md`, and the call sequence is in `../architect/feature_v1.0.10_F-008_architect.md` § Sequence. It is written there once rather than paraphrased here.

## Invariants

This feature persists nothing, so it declares no data invariant.

OPEN: what must stay true about this feature at runtime? Nothing in the code states it.

## Implementation status

States and what `done` costs: `../status-model.md`. Every row starts at `todo`; a rule reaches
`done` only when a test names the rule ID and that test passed here.

| Rule | Status | Evidence |
| --- | --- | --- |
| DOM-008-R1 | wip — implemented, no test names this rule ID | — |
| DOM-008-R2 | wip — implemented, no test names this rule ID | — |
| DOM-008-R3 | wip — implemented, no test names this rule ID | — |

## Open questions

- OPEN: Is the Admin Console intended to stay at parity with the domain APIs, or is it a superset that will diverge?
- OPEN: Why do 118 routes share `admin.system_config`? That permission is doing the work of a role rather than a permission.
- OPEN: Who is the intended operator — a platform administrator, or a team administrator with narrower scope?
- OPEN: which of the rules above the business would still hold if the code stopped enforcing them?
  A rule recovered from an enforcement site cannot distinguish policy from implementation detail.
