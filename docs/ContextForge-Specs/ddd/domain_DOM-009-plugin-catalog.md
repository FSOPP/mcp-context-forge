---
title: Domain — Plugin Catalog
id: DOM-009
kind: domain
feature: F-009
status: as-built
owner: TBD
updated: 2026-09-20
---

# Domain — Plugin Catalog

> Reconstructed from code. Rules below were promoted from constraint comments written by the
> people who knew them; each cites both the statement and the site enforcing it. Motive is not
> recoverable and is asked, not written.

## Ubiquitous language

| Term | Means | Do not use for |
| --- | --- | --- |
| Plugin | a directory with a manifest and a hook implementation | — |

## Actors

| Actor | Role |
| --- | --- |
| Plugin author | adds a directory and a manifest |
| Platform administrator | activates a plugin |

## Business rules

No constraint comment in this feature's files survived the survey's relevance cut, so no rule is promoted here. An empty rule set is a stated answer, not an omission.

OPEN: does this feature have business rules that no comment and no guard clause records?

## Process flow

This feature has no request flow of its own; see `../architect/feature_v1.0.10_F-009_architect.md` § Sequence.

## Invariants

This feature persists nothing, so it declares no data invariant.

OPEN: what must stay true about this feature at runtime? Nothing in the code states it.

## Implementation status

States and what `done` costs: `../status-model.md`. Every row starts at `todo`; a rule reaches
`done` only when a test names the rule ID and that test passed here.

| Rule | Status | Evidence |
| --- | --- | --- |
| — | — | no rules promoted |

## Open questions

- OPEN: Which of the 41 plugins are supported, and which are examples? The directory layout does not distinguish them.
- OPEN: What is the review bar for adding a plugin to this catalogue?
- OPEN: which of the rules above the business would still hold if the code stopped enforcing them?
  A rule recovered from an enforcement site cannot distinguish policy from implementation detail.
