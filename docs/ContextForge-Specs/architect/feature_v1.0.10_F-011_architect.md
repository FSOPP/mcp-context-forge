---
title: Feature Architecture v1.0.10 F-011 — Rust MCP Runtime
id: F-011
status: as-built
owner: TBD
updated: 2026-09-20
---

# Feature Architecture v1.0.10 F-011 — Rust MCP Runtime

> As-built. `[D: path:line]` is derived and reopenable, `I:` states its leap, `OPEN:` is a question
> the code cannot answer. Shared conventions live in `architect_common.md`; the system view lives
> in `architect.md`.

## Design summary

This feature is the Rust sidecar: a daemon that terminates MCP traffic and calls
back into the Python gateway over `/_internal/**`.

It serves 18 routes of its own, declared in two router builders
[D: crates/mcp_runtime/src/lib.rs:1350] [D: crates/mcp_runtime/src/lib.rs:1400]. Most mirror a
Python path — `/rpc`, `/mcp`, `/servers/{server_id}/mcp`, `/health` — since the daemon terminates
the same protocol. Two do not: `/_internal/event-store/store` and `/_internal/event-store/replay`
appear in the first builder only [D: crates/mcp_runtime/src/lib.rs:1352].

I: the two builders are two run modes rather than two services — basis: the second repeats the
first's routes minus the event-store pair, and the Python side carries a setting naming which
runtime owns event-store semantics [D: mcpgateway/config.py:281].

OPEN: which builder runs when? The condition selecting between them was not read.

It is a separate Cargo package with its own build and test commands
[D: crates/mcp_runtime/Cargo.toml:1], roughly 23,000 lines across five source modules. Two of those
modules exist to validate what the daemon is allowed to reach: `backend_url_validator.rs` is an
SSRF boundary [D: crates/mcp_runtime/src/backend_url_validator.rs:1].

I: the daemon holds no database state of its own — basis: it owns no table in `mcpgateway/db.py`
and its shared state is built from a pool and a client handed in at startup
[D: crates/mcp_runtime/src/lib.rs:714].

Implementation lives in:

- `crates/`
- `plugins_rust/`

## API contracts

18 route decorators belong to this feature. The readable
contract is `../data/api-contract_v1.0.10_F-011.md`; the machine-readable one is
`../data/schema/openapi_v1.0.10_F-011.json` and `../data/schema/asyncapi_v1.0.10_F-011.json`.

Request and response shapes are not stated in either. The repository ships no OpenAPI document,
and the handlers were not read field by field, so inventing those shapes here would be the one
thing this hub must not do.

## Data model

| table | fields | source |
| --- | --- | --- |
| — | — | this feature owns no table |

`../data/schema/erd_v1.0.10_F-011.puml` is deliberately empty and says so on its face.

## Sequence

The daemon terminates MCP traffic and calls the Python gateway over `/_internal/**`
[D: crates/mcp_runtime/src/lib.rs:2132]. It also serves two routes the Python side does not have,
for the resumable event store [D: crates/mcp_runtime/src/lib.rs:1352].

Startup builds shared state from an HTTP client, a database pool and a Redis client, and fails if
any of them cannot be initialised [D: crates/mcp_runtime/src/lib.rs:714]. The internal auth secret
is required at that point [D: crates/mcp_runtime/src/lib.rs:721].

OPEN: the sequence of a request that crosses the boundary twice. Only each side's own half was
read.

## Failure modes

- Any of the HTTP client, database pool or Redis client fails to initialise: startup
  returns an error rather than degrading [D: crates/mcp_runtime/src/lib.rs:714].
- Internal auth secret absent: startup fails at that check
  [D: crates/mcp_runtime/src/lib.rs:721].
- Backend URL rejected by the validator: the outbound call does not happen
  [D: crates/mcp_runtime/src/backend_url_validator.rs:1].

## Observability

The crate has its own observability module [D: crates/mcp_runtime/src/observability.rs:1].

OPEN: whether the Rust runtime's traces join the same trace as the Python side's, or form a
separate tree. The propagation was not read.

## Traceability

- Stories: `../PRDs/prd_v1.0.10_F-011-*.md`
- Tasks: `../tasks/tasks_v1.0.10_F-011.md`
- Tests: `../tests/test_v1.0.10_F-011.md`
- Contract: `../data/api-contract_v1.0.10_F-011.md`

## Open questions

- OPEN: When should an operator run the Rust runtime instead of the Python path? Both serve MCP and nothing states the trade-off.
- OPEN: What is the compatibility contract across the `/_internal/**` boundary?
