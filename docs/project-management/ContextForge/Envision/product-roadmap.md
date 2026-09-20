---
title: Product Roadmap — ContextForge
status: as-built
owner: TBD
updated: 2026-09-20
---

# Product Roadmap — ContextForge

> A roadmap is entirely about the future. This document can hold only two things honestly: the
> directions the code is visibly already moving in, and the questions that a real roadmap would
> answer.

## Directions visible in the code

These are migrations in progress, evidenced by two states existing at once. None of them is a
plan; each is a position the code is currently in the middle of.

| Direction | Evidence of both states |
| --- | --- |
| Unversioned API → `/v1` | both mounts live, shim stamped with `Sunset` [D: mcpgateway/middleware/deprecation.py:154] |
| `/gateways` → `/mcp-servers`, `/servers` → `/virtual-servers` | both names mounted to the same routers [D: mcpgateway/api/v1/__init__.py:58] |
| Python MCP termination → Rust runtime | both implementations live, with a deprecated setting naming which owns event-store semantics [D: mcpgateway/config.py:281] |
| In-tree plugins → external `cpex` framework | settings proxied out, bindings kept in [D: mcpgateway/config.py:4178] |

I: each row is a migration rather than a permanent duality — basis: in every case one side carries
a deprecation marker, a newer name, or a proxy to the other [D: mcpgateway/middleware/deprecation.py:154].

## Open questions

- OPEN: what is the target end state for each of the four directions above, and when?
- OPEN: which one is furthest along, and what is blocking the others?
- OPEN: is the Rust runtime intended to replace the Python MCP path or to sit beside it
  permanently?
- OPEN: what is on the roadmap that has no code yet? By definition this document cannot see it.
