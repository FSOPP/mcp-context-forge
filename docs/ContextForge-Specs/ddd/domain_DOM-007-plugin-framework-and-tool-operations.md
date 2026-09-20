---
title: Domain — Plugin Framework and Tool Operations
id: DOM-007
kind: domain
feature: F-007
status: as-built
owner: TBD
updated: 2026-09-20
---

# Domain — Plugin Framework and Tool Operations

> Reconstructed from code. Rules below were promoted from constraint comments written by the
> people who knew them; each cites both the statement and the site enforcing it. Motive is not
> recoverable and is asked, not written.

## Ubiquitous language

| Term | Means | Do not use for |
| --- | --- | --- |
| Hook | a point in request handling a plugin may observe | — |
| Binding | the row attaching a plugin to one tool or agent | activation, which is global |

## Actors

| Actor | Role |
| --- | --- |
| Platform administrator | binds a plugin to a tool or agent |
| Plugin | observes or alters a hook |

## Business rules

**DOM-007-R1.** Key names only (CPEX never includes values). _sanitize_config_key() validates each key against _CONFIG_KEY_RE: commas, CR/LF, control chars, non-ASCII, and secret-shaped text are rejected (key dropped entirely, not truncated) to prevent CSV ambiguity and log/telemetry injection. The joined string is

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/plugins/control_telemetry.py:634].

## Process flow

The process is the API surface: 4 route decorators, listed in `../data/api-contract_v1.0.10_F-007.md`, and the call sequence is in `../architect/feature_v1.0.10_F-007_architect.md` § Sequence. It is written there once rather than paraphrased here.

## Invariants

Database-level invariants for this feature are the `required` and key declarations in `../data/schema/schemas.json`, derived from the column definitions. `../data/data-erd_v1.0.10_F-007.md` lists them per table.

OPEN: which invariants are enforced only in application code and would survive a direct database write? The column constraints are visible; the guard clauses were not inventoried.

## Implementation status

States and what `done` costs: `../status-model.md`. Every row starts at `todo`; a rule reaches
`done` only when a test names the rule ID and that test passed here.

| Rule | Status | Evidence |
| --- | --- | --- |
| DOM-007-R1 | wip — implemented, no test names this rule ID | — |

## Open questions

- OPEN: What is the failure policy when a plugin hook raises? Whether the request fails or the plugin is skipped is a decision the framework makes and the documentation does not state.
- OPEN: Why is the framework off by default?
- OPEN: which of the rules above the business would still hold if the code stopped enforcing them?
  A rule recovered from an enforcement site cannot distinguish policy from implementation detail.
