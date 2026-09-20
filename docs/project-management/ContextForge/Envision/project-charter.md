---
title: Project Charter — ContextForge
status: as-built
owner: TBD
updated: 2026-09-20
---

# Project Charter — ContextForge

> **This is the most honest document in the hub, and almost all of it is questions.** A charter
> states why a product exists, who it is for and what success looks like. None of that is in a
> repository. What follows is the small part code can support, and the list of things the
> organisation knows and has never written down.

## Vision statement

The repository describes itself as an open source registry and proxy that federates MCP, A2A and
REST/gRPC APIs with centralized governance, discovery and observability
[D: CLAUDE.md:17].

I: that sentence is a description of capability, not a vision — basis: it names what the software
does and no audience, no problem and no change it intends to produce [D: CLAUDE.md:17].

OPEN: for whom does this exist, what did they do before it, and what changes for them once they
adopt it?

## Business value

OPEN: unrecoverable, entirely. No metric, revenue model, adoption target or cost case appears
anywhere in the repository.

OPEN: is this a product, a platform component, or infrastructure a larger system depends on? The
three imply different success measures and the code distinguishes none of them.

## Target users

Derived from the auth roles the code defines, which is a floor rather than an answer:
`platform_admin`, `team_admin`, `developer`, `viewer` [D: CLAUDE.md:197].

OPEN: which of these is the primary persona? A role is a permission set, not a person with a job
to be done.

OPEN: who operates a deployment — the same organisation that uses it, or a separate platform team?

## In scope / Out of scope

In scope, as evidenced by what exists:

| Area | Evidence |
| --- | --- |
| MCP federation and registry | 90 route decorators, 12 tables |
| Protocol serving across four transports | 107 route decorators |
| Multi-tenant identity and RBAC | 81 route decorators, 21 tables |
| Observability and audit | 34 route decorators, 20 tables |
| A2A agent federation | 17 route decorators, 10 tables |
| LLM proxying | 22 route decorators |
| Plugin framework and catalogue | 4 route decorators, 41 plugins |
| Admin console | 231 route decorators |

OPEN: out of scope. **Code records what was built and keeps no record of what was declined.** This
section cannot be filled by any amount of reading, and leaving it as a question is the point.

## Success metrics

OPEN: no SLO, no adoption target, no performance target and no quality gate threshold appears in
the repository. A coverage configuration exists without a failing threshold
[D: pyproject.toml:809].

## Constraints and assumptions

Derivable constraints:

- Python `>=3.12,<3.14` [D: pyproject.toml:54].
- Apache-2.0 licensed [D: LICENSE:1].
- The plugin framework is an external, exactly-pinned dependency [D: pyproject.toml:74].
- 44 contributors, and 925 files with a bus factor of one.

OPEN: budget, timeline, compliance obligations and team size. None is in the tree.

OPEN: what assumption is this architecture betting on? The dual Python/Rust runtime and the
external plugin framework each look like a bet; neither states what it is betting on.

## Top risks

OPEN: no risk register exists. What the code makes visible, stated as facts rather than as a
register:

| Observation | Evidence |
| --- | --- |
| 925 files have a single contributor in their history | repository index |
| `main.py` and `admin.py` are the two largest files and the two most-fixed | [D: mcpgateway/admin.py:1889] |
| Two runtimes implement overlapping MCP behaviour with no declared version contract | [D: crates/mcp_runtime/src/lib.rs:2132] |
| An audit write can fail silently | [D: mcpgateway/services/audit_trail_service.py:73] |
| No table declares a retention period | [D: mcpgateway/db.py:1129] |

OPEN: which of these the team considers a risk, and which are accepted positions.
