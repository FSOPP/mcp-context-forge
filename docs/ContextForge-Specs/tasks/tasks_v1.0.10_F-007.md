---
title: Tasks v1.0.10 F-007 — Plugin Framework and Tool Operations
id: F-007
status: as-built
owner: TBD
updated: 2026-09-20
---

# Tasks v1.0.10 F-007 — Plugin Framework and Tool Operations

> **Inverted document.** These are not tasks to do; they are an inventory of shipped work, one row
> per unit that exists, each pointing at the artefact. The `done-when` column holds the check that
> *would* prove the row — which is what the status column then has to cash.

## Tasks

| ID | Task | Done when | Status | Artifact |
| --- | --- | --- | --- | --- |
| F-007-T1 | Serve `/plugins` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/plugins.py:29] |
| F-007-T2 | Serve `/toolops/enrichment` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/toolops_router.py:144] |
| F-007-T3 | Serve `/toolops/validation` — 2 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/toolops_router.py:108] |
| F-007-T4 | Persist `tool_plugin_bindings` (13 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:6929] |
| F-007-T5 | Persist `toolops_test_cases` (3 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:4064] |

## Implementation status

States and what `done` costs: `../status-model.md`. A row starts at `todo` and reaches `done` only
when its done-when check ran **here** and the note records the command and result.

## Open questions

- OPEN: what work on this feature is in flight but not yet in the tree? A working tree shows what
  landed, never what is half-finished elsewhere.
- OPEN: which of these rows were one change and which accumulated over many? The grouping is by
  surface, not by the history that produced it.
- OPEN: What is the failure policy when a plugin hook raises? Whether the request fails or the plugin is skipped is a decision the framework makes and the documentation does not state.
