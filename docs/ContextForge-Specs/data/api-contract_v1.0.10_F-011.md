---
title: API Contract v1.0.10 F-011 — Rust MCP Runtime
id: F-011
status: as-built
owner: TBD
updated: 2026-09-20
---

# API Contract v1.0.10 F-011 — Rust MCP Runtime

> Reversed from code, not written before it. `[D: path:line]` marks a derived fact you can
> reopen; `I:` marks a stated leap; `OPEN:` marks what the code cannot answer.

## Surface summary

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

## Endpoints

| Method | Path | Auth | Source |
| --- | --- | --- | --- |
| POST | `/_internal/event-store/replay` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1353] |
| POST | `/_internal/event-store/store` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1352] |
| GET | `/health` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1350] |
| GET | `/health` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1400] |
| GET | `/healthz` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1351] |
| GET | `/healthz` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1401] |
| GET | `/mcp` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1359] |
| GET | `/mcp` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1404] |
| GET | `/mcp/` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1363] |
| GET | `/mcp/` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1408] |
| POST | `/rpc` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1357] |
| POST | `/rpc` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1402] |
| POST | `/rpc/` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1358] |
| POST | `/rpc/` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1403] |
| GET | `/servers/{server_id}/mcp` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1367] |
| GET | `/servers/{server_id}/mcp` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1412] |
| GET | `/servers/{server_id}/mcp/` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1373] |
| GET | `/servers/{server_id}/mcp/` | not extracted | [D: crates/mcp_runtime/src/lib.rs:1418] |

## Events

No channel literal was found in this feature's files. That is a stated empty answer, not an omission — `schema/asyncapi_v1.0.10_F-011.json` is correspondingly empty.

## Error model

OPEN: this feature's error responses were not read handler by handler. The repository ships no OpenAPI document and no central error table, so the status codes and error body shape are not stated anywhere a reader can check.

## Versioning and compatibility

The crate is versioned separately from the Python package
[D: crates/mcp_runtime/Cargo.toml:1]. Its route table is declared in one builder
[D: crates/mcp_runtime/src/lib.rs:1350] with no version prefix of its own.

OPEN: the compatibility contract between a runtime binary and a gateway version. The
`/_internal/**` surface is the coupling point and nothing declares a version on it.

## Spec files

- `schema/openapi_v1.0.10_F-011.json` — every path and method above, each with its `x-source` citation and the mounts it answers on. Request and response schemas are empty by design: nothing in the repository states them.
- `schema/asyncapi_v1.0.10_F-011.json` — channel names only.
- Entity shapes are `$ref`s into `schema/schemas.json`. No shape is redefined here.

## Traceability

Stories in `../PRDs/prd_v1.0.10_F-011-*.md` cite the endpoints above as evidence the behaviour
exists. They do not establish that it was wanted; see that document's own open questions.

## Open questions

- OPEN: When should an operator run the Rust runtime instead of the Python path? Both serve MCP and nothing states the trade-off.
- OPEN: What is the compatibility contract across the `/_internal/**` boundary?
