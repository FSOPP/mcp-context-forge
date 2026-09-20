---
title: Product Backlog — ContextForge
status: as-built
owner: TBD
updated: 2026-09-20
---

# Product Backlog — ContextForge

> **Inverted.** A backlog lists what is not built yet. This one lists what is, because the rows
> came from reversing the code. Size is derived from the surveyed surface. Value and priority are
> `OPEN:` — they are statements about intent and no amount of reading recovers them.

## Items

| ID | Feature | Route sites | Tables | Size | Value | Priority | State |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | MCP Registry and Federation | 90 | 12 | L | OPEN | OPEN | shipped |
| F-002 | MCP Protocol Serving and Transports | 107 | 3 | L | OPEN | OPEN | shipped |
| F-003 | Identity, Teams and Access Control | 81 | 21 | L | OPEN | OPEN | shipped |
| F-004 | Observability, Metrics and Audit | 34 | 20 | L | OPEN | OPEN | shipped |
| F-005 | A2A Agent Federation | 17 | 10 | M | OPEN | OPEN | shipped |
| F-006 | LLM Gateway and Chat | 22 | 2 | M | OPEN | OPEN | shipped |
| F-007 | Plugin Framework and Tool Operations | 4 | 2 | S | OPEN | OPEN | shipped |
| F-008 | Admin Console | 231 | 0 | L | OPEN | OPEN | shipped |
| F-009 | Plugin Catalog | 0 | 0 | S | OPEN | OPEN | shipped |
| F-010 | Bundled MCP Servers and Templates | 0 | 0 | S | OPEN | OPEN | shipped |
| F-011 | Rust MCP Runtime | 18 | 0 | M | OPEN | OPEN | shipped |
| F-012 | Deployment and Operations | 0 | 0 | S | OPEN | OPEN | shipped |

604 route decorators and 70 tables across twelve features. Size is `L` above
80 sites or 15 tables, `M` above 15 sites or 3 tables, `S` otherwise — a mechanical rule stated so
it can be disagreed with.

## What is missing from this backlog

Everything not yet built. A reversed backlog has no forward half, and pretending otherwise would
be the clearest possible invention.

OPEN: what is on the real backlog right now?

## Sizing basis

I: surveyed surface is a proxy for size — basis: route decorators and tables are countable and
correlate with the work that produced them, while nothing in the tree records effort
[D: mcpgateway/api/v1/__init__.py:436].

That proxy has a known failure: F-008 Admin Console scores 231 sites and owns no table,
because it is a second surface over other features' logic. Its size is inflated by this rule.

## Open questions

- OPEN: what is the priority order among these twelve? Nothing in the repository ranks them.
- OPEN: which features are complete and which are partial? The code runs; "complete" is a
  judgement against a requirement that is not written down.
- OPEN: which of these would the team build again?
