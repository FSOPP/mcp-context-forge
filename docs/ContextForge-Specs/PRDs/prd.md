---
title: Master PRD — ContextForge
status: as-built
owner: TBD
updated: 2026-09-20
---

# Master PRD — ContextForge

> Reversed. Every requirement statement below is a question, because a requirement is intent and
> intent is not in a repository. The feature index is real; the rest is the list of things nobody
> wrote down.

## Product summary

An open source registry and proxy that federates MCP, A2A and REST/gRPC APIs with centralized
governance, discovery and observability [D: CLAUDE.md:17].

## Features

| ID | PRD | Route sites | Tables |
| --- | --- | --- | --- |
| F-001 | [MCP Registry and Federation](../PRDs/prd_v1.0.10_F-001-mcp-registry-and-federation.md) | 90 | 12 |
| F-002 | [MCP Protocol Serving and Transports](../PRDs/prd_v1.0.10_F-002-mcp-protocol-serving-and-transports.md) | 107 | 3 |
| F-003 | [Identity, Teams and Access Control](../PRDs/prd_v1.0.10_F-003-identity-teams-and-access-control.md) | 81 | 21 |
| F-004 | [Observability, Metrics and Audit](../PRDs/prd_v1.0.10_F-004-observability-metrics-and-audit.md) | 34 | 20 |
| F-005 | [A2A Agent Federation](../PRDs/prd_v1.0.10_F-005-a2a-agent-federation.md) | 17 | 10 |
| F-006 | [LLM Gateway and Chat](../PRDs/prd_v1.0.10_F-006-llm-gateway-and-chat.md) | 22 | 2 |
| F-007 | [Plugin Framework and Tool Operations](../PRDs/prd_v1.0.10_F-007-plugin-framework-and-tool-operations.md) | 4 | 2 |
| F-008 | [Admin Console](../PRDs/prd_v1.0.10_F-008-admin-console.md) | 231 | 0 |
| F-009 | [Plugin Catalog](../PRDs/prd_v1.0.10_F-009-plugin-catalog.md) | 0 | 0 |
| F-010 | [Bundled MCP Servers and Templates](../PRDs/prd_v1.0.10_F-010-bundled-mcp-servers-and-templates.md) | 0 | 0 |
| F-011 | [Rust MCP Runtime](../PRDs/prd_v1.0.10_F-011-rust-mcp-runtime.md) | 18 | 0 |
| F-012 | [Deployment and Operations](../PRDs/prd_v1.0.10_F-012-deployment-and-operations.md) | 0 | 0 |

## MVP definition

OPEN: unrecoverable. The product ships at `1.0.10` [D: pyproject.toml:54]; which subset was the
MVP, and whether that subset was met, is not in the tree.

## Non-functional requirements

One `OPEN:` per concern, except where a number is actually configured — in which case it is a
derived fact and a genuinely useful find:

| Concern | Status |
| --- | --- |
| Latency | OPEN — no target stated |
| Throughput | OPEN — no target stated |
| Availability | OPEN — no target stated |
| Connection pool | `DB_POOL_SIZE` and `DB_MAX_OVERFLOW` are configured [D: mcpgateway/config.py:3661] |
| Tool invocation timeout | `TOOL_TIMEOUT` is configured [D: mcpgateway/config.py:4037] |
| Resource cache | `RESOURCE_CACHE_SIZE` and `RESOURCE_CACHE_TTL` are configured [D: mcpgateway/config.py:4037] |
| Health check interval | `HEALTH_CHECK_INTERVAL` is configured [D: mcpgateway/config.py:4037] |
| Rate limiting | middleware exists [D: mcpgateway/middleware/rate_limit_middleware.py:40] |
| Security | invariants are stated in the repository's own instructions [D: CLAUDE.md:163] |

I: the configured numbers are defaults rather than requirements — basis: each is a settings default
a deployment overrides, and nothing states a target the default is meant to meet
[D: mcpgateway/config.py:4037].

## Open questions

- OPEN: what does "done" mean for this product?
- OPEN: which of the twelve features is load-bearing for adoption?
- OPEN: what would make a user choose this over a direct MCP connection?
