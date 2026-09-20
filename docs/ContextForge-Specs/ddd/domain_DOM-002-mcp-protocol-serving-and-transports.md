---
title: Domain — MCP Protocol Serving and Transports
id: DOM-002
kind: domain
feature: F-002
status: as-built
owner: TBD
updated: 2026-09-20
---

# Domain — MCP Protocol Serving and Transports

> Reconstructed from code. Rules below were promoted from constraint comments written by the
> people who knew them; each cites both the statement and the site enforcing it. Motive is not
> recoverable and is asked, not written.

## Ubiquitous language

| Term | Means | Do not use for |
| --- | --- | --- |
| Session | one client connection with negotiated capabilities | — |
| Method | the JSON-RPC operation name | endpoint, which is the HTTP path |
| Transport | SSE, WebSocket, streamable HTTP or stdio | protocol, which is MCP |

## Actors

| Actor | Role |
| --- | --- |
| MCP client | opens a session and sends JSON-RPC |
| Rust MCP runtime | calls the internal surface on a client's behalf |

## Business rules

**DOM-002-R1.** Direct proxy mode: forward request to remote MCP server SECURITY: CWE-532 protection - Log only meta_data key names, NEVER values Metadata may contain PII, authentication tokens, or sensitive context that MUST NOT be written to logs. This is a critical security control.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/transports/streamablehttp_transport.py:2904].

**DOM-002-R2.** Early-boot / test-bootstrap race. Fail closed with 503 — we cannot enforce the invariant without the singleton, and in any real deployment lifespan initializes the service before the HTTP listener accepts traffic.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/transports/streamablehttp_transport.py:3802].

**DOM-002-R3.** Clear the runtime state singleton. Tests only. Production code must not call this — it intentionally drops any active override and leaks the prior coordinator's pubsub task if one is running.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/runtime_state.py:497].

**DOM-002-R4.** Per-session FIFO, cross-session concurrency: claim the session's in-memory lock synchronously (arrival order), then dispatch on a task so the mailbox never stalls behind an execution. Global concurrency is bounded inside the task, AFTER session ordering.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/session_affinity.py:1019].

**DOM-002-R5.** Start the worker heartbeat background task. Must be called from an async context. Safe to call multiple times; subsequent calls are no-ops if the heartbeat is already running.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/session_affinity.py:263].

**DOM-002-R6.** asyncio.wait_for timeout path: the owner task hangs (TCP accepted but never responds) and we timeout waiting for the ready future. The owner task never hits its `except Exception` handler (it receives CancelledError instead, which is a BaseException and deliberately excluded). So we must categorize,

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/upstream_session_registry.py:620].

**DOM-002-R7.** Strip gateway-internal session affinity headers; they must not be forwarded upstream. Upstream sees its own session id, which it assigns via its initialize response.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/services/upstream_session_registry.py:932].

**DOM-002-R8.** Only evict if the event is actually present. Returning 0 tells the caller the entry was already gone (idempotent).

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/transports/redis_event_store.py:143].

**DOM-002-R9.** Initialize the proxy with the existing Python MCP transport fallback. Args: python_fallback_app: Python MCP transport app used when Rust cannot handle the request.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/transports/rust_mcp_runtime_proxy.py:158].

**DOM-002-R10.** Pre-generate the event id so the Pub/Sub payload can reference it, and so we have a fixed id to evict if the EVAL reply never reaches us (EVAL completed server-side but the reply was lost).

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/transports/server_event_bus.py:362].

**DOM-002-R11.** Enforce account-active check (matches JWT path in _enforce_revocation_and_active_user). A disabled user - including a disabled admin - must not be able to authenticate via trusted-proxy mode and inherit their pre-disable authorizations.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/transports/streamablehttp_transport.py:5058].

**DOM-002-R12.** Order matters: check_hostname must be disabled before verify_mode is set to CERT_NONE, otherwise Python raises "Cannot set verify_mode to CERT_NONE when check_hostname is enabled."

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcpgateway/utils/internal_http.py:118].

## Process flow

The process is the API surface: 107 route decorators, listed in `../data/api-contract_v1.0.10_F-002.md`, and the call sequence is in `../architect/feature_v1.0.10_F-002_architect.md` § Sequence. It is written there once rather than paraphrased here.

## Invariants

Database-level invariants for this feature are the `required` and key declarations in `../data/schema/schemas.json`, derived from the column definitions. `../data/data-erd_v1.0.10_F-002.md` lists them per table.

OPEN: which invariants are enforced only in application code and would survive a direct database write? The column constraints are visible; the guard clauses were not inventoried.

## Implementation status

States and what `done` costs: `../status-model.md`. Every row starts at `todo`; a rule reaches
`done` only when a test names the rule ID and that test passed here.

| Rule | Status | Evidence |
| --- | --- | --- |
| DOM-002-R1 | wip — implemented, no test names this rule ID | — |
| DOM-002-R2 | wip — implemented, no test names this rule ID | — |
| DOM-002-R3 | wip — implemented, no test names this rule ID | — |
| DOM-002-R4 | wip — implemented, no test names this rule ID | — |
| DOM-002-R5 | wip — implemented, no test names this rule ID | — |
| DOM-002-R6 | wip — implemented, no test names this rule ID | — |
| DOM-002-R7 | wip — implemented, no test names this rule ID | — |
| DOM-002-R8 | wip — implemented, no test names this rule ID | — |
| DOM-002-R9 | wip — implemented, no test names this rule ID | — |
| DOM-002-R10 | wip — implemented, no test names this rule ID | — |
| DOM-002-R11 | wip — implemented, no test names this rule ID | — |
| DOM-002-R12 | wip — implemented, no test names this rule ID | — |

## Open questions

- OPEN: What is the complete live operation list? It is the 27 literal JSON-RPC methods plus every row in `tools` — a runtime value this repository cannot state.
- OPEN: Which MCP protocol revision is targeted, and what happens when a client negotiates a different one?
- OPEN: What is the target p95 for `tools/call`? No SLO appears in the repository.
- OPEN: which of the rules above the business would still hold if the code stopped enforcing them?
  A rule recovered from an enforcement site cannot distinguish policy from implementation detail.
