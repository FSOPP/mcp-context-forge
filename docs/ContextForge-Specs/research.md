---
title: Research & Reference Material — ContextForge
status: as-built
owner: TBD
updated: 2026-09-20
---

# Research & Reference Material — ContextForge

> Reversed. A research file normally records what was investigated before building. That is a
> record of process, and process is not in a working tree. What follows is what the code
> *depends on*, which is a different and smaller thing.

## Third-party integrations

| Integration | Boundary | Source |
| --- | --- | --- |
| `cpex` plugin framework | settings proxied out, hooks dispatched outside this repository | [D: mcpgateway/config.py:4178] |
| Upstream MCP servers | registered as `gateways` rows, polled for primitives | [D: mcpgateway/services/gateway_service.py:671] |
| A2A agents | agent card fetch plus task dispatch | [D: mcpgateway/db.py:4923] |
| LLM providers | proxied under a runtime-configured prefix | [D: mcpgateway/main.py:13187] |
| SSO / external IdP | identities provisioned into local user records | [D: mcpgateway/routers/sso.py:1] |
| Redis | cache and federation state, optional | [D: mcpgateway/cache/session_registry.py:503] |
| OpenTelemetry | OTLP export behind a flag | [D: mcpgateway/config.py:4037] |
| Vault | secret storage behind a flag | [D: mcpgateway/routers/vault_router.py:1] |

## Standards the code implements

These are citable because the code names them, which is stronger than a reading list:

- RFC 8693 token exchange, for on-behalf-of gateway auth [D: CLAUDE.md:179].
- RFC 9728 OAuth protected resource metadata [D: mcpgateway/routers/well_known.py:117].
- RFC 8615 well-known URIs — the reason the well-known router is mounted at server root rather
  than under `/v1` [D: mcpgateway/api/v1/__init__.py:298].
- RFC 8594 `Sunset`, for the deprecated unversioned shim
  [D: mcpgateway/middleware/deprecation.py:154].
- CWE-532, cited where metadata values are deliberately not logged
  [D: mcpgateway/transports/streamablehttp_transport.py:2904].

## Spikes

OPEN: unrecoverable. A spike that was abandoned leaves nothing behind; a spike that succeeded is
indistinguishable from ordinary code once merged.

The one visible trace of exploration is that four migrations in progress are live at once — API
versioning, resource renaming, the Rust runtime, and the external plugin framework — each with
both states present. They are listed in `../project-management/ContextForge/Envision/product-roadmap.md`.

## Reference material

OPEN: which external documents the team treats as authoritative. The repository cites RFCs and CWE
identifiers inline, and links nothing else.

## Open questions

- OPEN: what alternatives were evaluated for the plugin framework before `cpex`?
- OPEN: what prompted the Rust runtime — a measured bottleneck, or a strategic bet?
- OPEN: which MCP protocol revision is the target, and how is drift against it tracked?
  A compliance suite exists for `mcp_2025_11_25` [D: tests/AGENTS.md:1].
