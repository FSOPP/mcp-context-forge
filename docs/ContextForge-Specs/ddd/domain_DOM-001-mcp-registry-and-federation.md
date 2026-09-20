---
title: Domain — MCP Registry and Federation
id: DOM-001
kind: domain
feature: F-001
status: as-built
owner: TBD
updated: 2026-09-20
---

# Domain — MCP Registry and Federation

> Reconstructed from code. Rules below were promoted from constraint comments written by the
> people who knew them; each cites both the statement and the site enforcing it. Motive is not
> recoverable and is asked, not written.

## Ubiquitous language

| Term | Means | Do not use for |
| --- | --- | --- |
| Gateway | a registered upstream MCP server | not the ContextForge process itself, which this domain also calls a gateway |
| Virtual server | a named composition of tools, resources and prompts | `server`, which the API also spells `virtual-server` |
| Tool | one invocable capability discovered from a gateway | — |
| Primitive | a tool, resource or prompt | — |
| Federation | re-exposing another gateway's primitives as this one's | — |

## Actors

| Actor | Role |
| --- | --- |
| Platform administrator | registers and removes upstream gateways |
| Team member | reads and invokes the primitives their team can see |
| Upstream MCP server | is registered; supplies the primitives |

## Business rules

**DOM-001-R1.** A token-exchange gateway's Authorization must always come from a fresh RFC 8693 exchange of the caller's inbound JWT -- never from generic header passthrough, which would forward the caller's raw JWT upstream unexchanged.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/gateway_service.py:7051].

**DOM-001-R2.** Safety net for CancelledError (BaseException) and any path that bypassed the record_* calls above. Idempotent: releases only if the slot is still held.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/cache/registry_cache.py:482].

**DOM-001-R3.** Skip only if it's an auth_code gateway with no data (user may not have completed authorization)

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/gateway_service.py:6843].

**DOM-001-R4.** ProcessPoolExecutor queues a task the instant every worker is busy, and future.result(timeout=...) below cannot tell "still queued" apart from "running past its budget" -- both look like a timeout. Reserving a slot here first means a submission only ever reaches the pool when a worker is actually fr

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/utils/jq_runner.py:375].

**DOM-001-R5.** Release the half-open probe slot unconditionally. Used by the cancellation/finally safety net in ``_redis_operation_with_timeout`` so that an outer task cancellation cannot strand the flag in the set position and permanently disable the circuit breaker.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/cache/registry_cache.py:341].

**DOM-001-R6.** Scope is part of the cache key: cached registration state must never cross caller identities or Layer-1 team scopes. Keep ``None`` distinct from an empty tuple because it represents admin bypass, while the latter is public-only access.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/catalog_service.py:225].

**DOM-001-R7.** Comma-separated input (the shape admin.py's own OAuth form accepts, see admin._assemble_oauth_config_from_fields()) must be split the same way here, otherwise "repo,read:user" is stored as one malformed scope instead of two.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/catalog_service.py:469].

**DOM-001-R8.** Subject token: Authorization bearer first, then the HttpOnly jwt_token cookie (Admin UI sessions cannot attach a bearer header). Both routes sit behind CSRF enforcement at the endpoint/middleware layer.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/gateway_service.py:1069].

**DOM-001-R9.** Validate JWT claims (audience, scopes, issuer) before forwarding token. Mirrors the validation in _resolve_auth_code_refresh_headers so the two call sites cannot drift on claim-validation behaviour.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/gateway_service.py:2393].

**DOM-001-R10.** Always back off here too - an unexpected acquire()/lock error must not spin the loop with no delay (busy-loops the event loop and can starve the worker of CPU needed to serve requests).

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/gateway_service.py:5721].

**DOM-001-R11.** Layer 1 invariant: parent visibility/team/owner must propagate to derived tools so token-scoping changes on the gRPC service take effect immediately.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/grpc_service.py:779].

**DOM-001-R12.** Record server metrics ONLY when the server scoping check passed. This prevents recording metrics with unvalidated server_id values from admin API headers (X-Server-ID) or RPC params.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/prompt_service.py:2184].

## Process flow

The process is the API surface: 90 route decorators, listed in `../data/api-contract_v1.0.10_F-001.md`, and the call sequence is in `../architect/feature_v1.0.10_F-001_architect.md` § Sequence. It is written there once rather than paraphrased here.

## Invariants

Database-level invariants for this feature are the `required` and key declarations in `../data/schema/schemas.json`, derived from the column definitions. `../data/data-erd_v1.0.10_F-001.md` lists them per table.

OPEN: which invariants are enforced only in application code and would survive a direct database write? The column constraints are visible; the guard clauses were not inventoried.

## Implementation status

States and what `done` costs: `../status-model.md`. Every row starts at `todo`; a rule reaches
`done` only when a test names the rule ID and that test passed here.

| Rule | Status | Evidence |
| --- | --- | --- |
| DOM-001-R1 | wip — implemented, no test names this rule ID | — |
| DOM-001-R2 | wip — implemented, no test names this rule ID | — |
| DOM-001-R3 | wip — implemented, no test names this rule ID | — |
| DOM-001-R4 | wip — implemented, no test names this rule ID | — |
| DOM-001-R5 | wip — implemented, no test names this rule ID | — |
| DOM-001-R6 | wip — implemented, no test names this rule ID | — |
| DOM-001-R7 | wip — implemented, no test names this rule ID | — |
| DOM-001-R8 | wip — implemented, no test names this rule ID | — |
| DOM-001-R9 | wip — implemented, no test names this rule ID | — |
| DOM-001-R10 | wip — implemented, no test names this rule ID | — |
| DOM-001-R11 | wip — implemented, no test names this rule ID | — |
| DOM-001-R12 | wip — implemented, no test names this rule ID | — |

## Open questions

- OPEN: What is the intended lifecycle of a discovered tool whose upstream gateway is deleted? The schema keeps the rows; no code path in the survey deletes them.
- OPEN: Why do `/gateways` and `/mcp-servers` both exist? The rename is visible; the plan and the removal date are not.
- OPEN: What is the expected upper bound on federated gateways per deployment? No limit is configured anywhere.
- OPEN: which of the rules above the business would still hold if the code stopped enforcing them?
  A rule recovered from an enforcement site cannot distinguish policy from implementation detail.
