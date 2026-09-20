---
title: Stakeholder Analysis — ContextForge
status: as-built
owner: TBD
updated: 2026-09-20
---

# Stakeholder Analysis — ContextForge

> Code contains no stakeholders. It contains roles, contributors and consumers, which are three
> different things, none of them a stakeholder.

## Roles the code defines

| Role | Scope | Source |
| --- | --- | --- |
| `platform_admin` | global, all permissions | [D: CLAUDE.md:197] |
| `team_admin` | team | [D: CLAUDE.md:197] |
| `developer` | team | [D: CLAUDE.md:197] |
| `viewer` | team | [D: CLAUDE.md:197] |

## Consumers the code serves

MCP clients, admin operators, API consumers, the Rust runtime, upstream MCP servers, A2A agents,
LLM providers and identity providers — listed with their interfaces in
`../../../ContextForge-Specs/architect/architect.md` § System context.

## Contributors

44 contributors over 3213 commits. One contributor accounts for roughly 46% of file ownership.

I: this is a fact about history, not about ownership today — basis: the figure comes from commit
attribution, and published precision for history-derived attribution is around 29%
[D: CLAUDE.md:17].

## Open questions

- OPEN: who decides what ships? No governance document names a maintainer group or a decision
  process, beyond a code of conduct and a contributing guide
  [D: CONTRIBUTING.md:1].
- OPEN: who are the adopters, and what do they need that is not built?
- OPEN: is there a security contact and disclosure process in practice, beyond the policy file
  [D: SECURITY.md:1]?
- OPEN: which contributors maintain which subsystem today?
