---
title: Domain — LLM Gateway and Chat
id: DOM-006
kind: domain
feature: F-006
status: as-built
owner: TBD
updated: 2026-09-20
---

# Domain — LLM Gateway and Chat

> Reconstructed from code. Rules below were promoted from constraint comments written by the
> people who knew them; each cites both the statement and the site enforcing it. Motive is not
> recoverable and is asked, not written.

## Ubiquitous language

| Term | Means | Do not use for |
| --- | --- | --- |
| Provider | an LLM vendor configuration | model, which is one of its offerings |

## Actors

| Actor | Role |
| --- | --- |
| Platform administrator | registers providers and models |
| Chat consumer | sends completions through the proxy |

## Business rules

**DOM-006-R1.** Re-stamp idle clock per chunk so the reaper never evicts a session that is still actively streaming (§4 of the multi-worker session fix).

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/routers/llmchat_router.py:1246].

## Process flow

The process is the API surface: 22 route decorators, listed in `../data/api-contract_v1.0.10_F-006.md`, and the call sequence is in `../architect/feature_v1.0.10_F-006_architect.md` § Sequence. It is written there once rather than paraphrased here.

## Invariants

Database-level invariants for this feature are the `required` and key declarations in `../data/schema/schemas.json`, derived from the column definitions. `../data/data-erd_v1.0.10_F-006.md` lists them per table.

OPEN: which invariants are enforced only in application code and would survive a direct database write? The column constraints are visible; the guard clauses were not inventoried.

## Implementation status

States and what `done` costs: `../status-model.md`. Every row starts at `todo`; a rule reaches
`done` only when a test names the rule ID and that test passed here.

| Rule | Status | Evidence |
| --- | --- | --- |
| DOM-006-R1 | wip — implemented, no test names this rule ID | — |

## Open questions

- OPEN: Which providers are supported in practice, and which are merely representable in `llm_providers`?
- OPEN: What is the cost or rate ceiling on the proxy? No limit is configured.
- OPEN: which of the rules above the business would still hold if the code stopped enforcing them?
  A rule recovered from an enforcement site cannot distinguish policy from implementation detail.
