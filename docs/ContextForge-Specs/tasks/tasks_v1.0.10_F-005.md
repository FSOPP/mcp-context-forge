---
title: Tasks v1.0.10 F-005 — A2A Agent Federation
id: F-005
status: as-built
owner: TBD
updated: 2026-09-20
---

# Tasks v1.0.10 F-005 — A2A Agent Federation

> **Inverted document.** These are not tasks to do; they are an inventory of shipped work, one row
> per unit that exists, each pointing at the artefact. The `done-when` column holds the check that
> *would* prove the row — which is what the status column then has to cash.

## Tasks

| ID | Task | Done when | Status | Artifact |
| --- | --- | --- | --- | --- |
| F-005-T1 | Serve `/a2a` — 7 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:4890] |
| F-005-T2 | Serve `/a2a-agents/plugin-bindings` — 5 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/a2a_agent_plugin_bindings.py:224] |
| F-005-T3 | Serve `/a2a/invoke` — 2 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:5406] |
| F-005-T4 | Serve `/a2a/jsonrpc` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:5459] |
| F-005-T5 | Serve `/a2a/state` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:5157] |
| F-005-T6 | Serve `/a2a/toggle` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:5194] |
| F-005-T7 | Persist `a2a_agents` (41 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:4923] |
| F-005-T8 | Persist `a2a_tasks` (11 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:5117] |
| F-005-T9 | Persist `a2a_agent_auth` (8 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:5190] |
| F-005-T10 | Persist `a2a_push_notification_configs` (9 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:5211] |
| F-005-T11 | Persist `a2a_task_events` (8 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:5233] |
| F-005-T12 | Persist `a2a_agent_metrics` (7 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2697] |
| F-005-T13 | Persist `a2a_agent_metrics_hourly` (15 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2842] |
| F-005-T14 | Persist `server_task_mappings` (8 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:5146] |
| F-005-T15 | Persist `a2a_agent_plugin_bindings` (13 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:7010] |
| F-005-T16 | Persist `server_a2a_association` (2 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2555] |

## Implementation status

States and what `done` costs: `../status-model.md`. A row starts at `todo` and reaches `done` only
when its done-when check ran **here** and the note records the command and result.

## Open questions

- OPEN: what work on this feature is in flight but not yet in the tree? A working tree shows what
  landed, never what is half-finished elsewhere.
- OPEN: which of these rows were one change and which accumulated over many? The grouping is by
  surface, not by the history that produced it.
- OPEN: What is the trust model for a remote gateway in a cross-gateway call? Both sides must trust the same JWT issuer, and nothing states how that is established operationally.
