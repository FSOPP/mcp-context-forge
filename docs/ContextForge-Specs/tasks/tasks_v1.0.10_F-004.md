---
title: Tasks v1.0.10 F-004 — Observability, Metrics and Audit
id: F-004
status: as-built
owner: TBD
updated: 2026-09-20
---

# Tasks v1.0.10 F-004 — Observability, Metrics and Audit

> **Inverted document.** These are not tasks to do; they are an inventory of shipped work, one row
> per unit that exists, each pointing at the artefact. The `done-when` column holds the check that
> *would* prove the row — which is what the status column then has to cash.

## Tasks

| ID | Task | Done when | Status | Artifact |
| --- | --- | --- | --- | --- |
| F-004-T1 | Serve `/api/logs` — 6 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/log_search.py:1021] |
| F-004-T2 | Serve `/api/metrics` — 4 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/metrics_maintenance.py:104] |
| F-004-T3 | Serve `/compliance/frameworks` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/compliance_router.py:124] |
| F-004-T4 | Serve `/compliance/reports` — 4 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/compliance_router.py:187] |
| F-004-T5 | Serve `/health` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:12424] |
| F-004-T6 | Serve `/health/security` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:12558] |
| F-004-T7 | Serve `/healthz` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/translate.py:875] |
| F-004-T8 | Serve `/logging/setLevel` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:12315] |
| F-004-T9 | Serve `/metrics` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:12343] |
| F-004-T10 | Serve `/metrics/prometheus` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/services/metrics.py:467] |
| F-004-T11 | Serve `/metrics/reset` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:12375] |
| F-004-T12 | Serve `/observability/analytics` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/observability.py:678] |
| F-004-T13 | Serve `/observability/metrics` — 2 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/observability.py:921] |
| F-004-T14 | Serve `/observability/spans` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/observability.py:328] |
| F-004-T15 | Serve `/observability/stats` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/observability.py:431] |
| F-004-T16 | Serve `/observability/traces` — 5 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/observability.py:77] |
| F-004-T17 | Serve `/ready` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:12492] |
| F-004-T18 | Serve `/version` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/version.py:1259] |
| F-004-T19 | Persist `observability_traces` (16 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2896] |
| F-004-T20 | Persist `observability_spans` (15 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2963] |
| F-004-T21 | Persist `observability_events` (11 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:3028] |
| F-004-T22 | Persist `observability_metrics` (11 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:3085] |
| F-004-T23 | Persist `observability_saved_queries` (10 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:3138] |
| F-004-T24 | Persist `tool_metrics` (6 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2592] |
| F-004-T25 | Persist `resource_metrics` (6 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2618] |
| F-004-T26 | Persist `server_metrics` (6 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2644] |
| F-004-T27 | Persist `prompt_metrics` (6 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2670] |
| F-004-T28 | Persist `tool_metrics_hourly` (14 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2742] |
| F-004-T29 | Persist `resource_metrics_hourly` (14 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2767] |
| F-004-T30 | Persist `prompt_metrics_hourly` (14 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2792] |
| F-004-T31 | Persist `server_metrics_hourly` (14 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2817] |
| F-004-T32 | Persist `performance_snapshots` (6 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:3189] |
| F-004-T33 | Persist `performance_aggregates` (17 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:3230] |
| F-004-T34 | Persist `performance_metrics` (17 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:6232] |
| F-004-T35 | Persist `structured_log_entries` (29 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:6162] |
| F-004-T36 | Persist `security_events` (25 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:6279] |
| F-004-T37 | Persist `audit_trails` (26 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:6645] |
| F-004-T38 | Persist `migration_metadata` (4 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:1156] |

## Implementation status

States and what `done` costs: `../status-model.md`. A row starts at `todo` and reaches `done` only
when its done-when check ran **here** and the note records the command and result.

## Open questions

- OPEN: what work on this feature is in flight but not yet in the tree? A working tree shows what
  landed, never what is half-finished elsewhere.
- OPEN: which of these rows were one change and which accumulated over many? The grouping is by
  surface, not by the history that produced it.
- OPEN: What is the retention policy for traces, spans and per-invocation metrics? The tables grow without bound and no code in the survey deletes from them except `delete_old_traces`, whose schedule is not set here.
