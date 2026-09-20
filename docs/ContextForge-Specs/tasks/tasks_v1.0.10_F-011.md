---
title: Tasks v1.0.10 F-011 — Rust MCP Runtime
id: F-011
status: as-built
owner: TBD
updated: 2026-09-20
---

# Tasks v1.0.10 F-011 — Rust MCP Runtime

> **Inverted document.** These are not tasks to do; they are an inventory of shipped work, one row
> per unit that exists, each pointing at the artefact. The `done-when` column holds the check that
> *would* prove the row — which is what the status column then has to cash.

## Tasks

| ID | Task | Done when | Status | Artifact |
| --- | --- | --- | --- | --- |
| F-011-T1 | Serve `/_internal/event-store` — 2 route decorators | the suite covering these paths passes here | wip — unverified, not covered by `make test` — `cd crates/mcp_runtime && cargo test` | [D: crates/mcp_runtime/src/lib.rs:1353] |
| F-011-T2 | Serve `/health` — 2 route decorators | the suite covering these paths passes here | wip — unverified, not covered by `make test` — `cd crates/mcp_runtime && cargo test` | [D: crates/mcp_runtime/src/lib.rs:1350] |
| F-011-T3 | Serve `/healthz` — 2 route decorators | the suite covering these paths passes here | wip — unverified, not covered by `make test` — `cd crates/mcp_runtime && cargo test` | [D: crates/mcp_runtime/src/lib.rs:1351] |
| F-011-T4 | Serve `/mcp` — 4 route decorators | the suite covering these paths passes here | wip — unverified, not covered by `make test` — `cd crates/mcp_runtime && cargo test` | [D: crates/mcp_runtime/src/lib.rs:1359] |
| F-011-T5 | Serve `/rpc` — 4 route decorators | the suite covering these paths passes here | wip — unverified, not covered by `make test` — `cd crates/mcp_runtime && cargo test` | [D: crates/mcp_runtime/src/lib.rs:1357] |
| F-011-T6 | Serve `/servers/mcp` — 4 route decorators | the suite covering these paths passes here | wip — unverified, not covered by `make test` — `cd crates/mcp_runtime && cargo test` | [D: crates/mcp_runtime/src/lib.rs:1367] |

## Implementation status

States and what `done` costs: `../status-model.md`. A row starts at `todo` and reaches `done` only
when its done-when check ran **here** and the note records the command and result.

## Open questions

- OPEN: what work on this feature is in flight but not yet in the tree? A working tree shows what
  landed, never what is half-finished elsewhere.
- OPEN: which of these rows were one change and which accumulated over many? The grouping is by
  surface, not by the history that produced it.
- OPEN: When should an operator run the Rust runtime instead of the Python path? Both serve MCP and nothing states the trade-off.
