---
title: Tasks v1.0.10 F-001 — MCP Registry and Federation
id: F-001
status: as-built
owner: TBD
updated: 2026-09-20
---

# Tasks v1.0.10 F-001 — MCP Registry and Federation

> **Inverted document.** These are not tasks to do; they are an inventory of shipped work, one row
> per unit that exists, each pointing at the artefact. The `done-when` column holds the check that
> *would* prove the row — which is what the status column then has to cash.

## Tasks

| ID | Task | Done when | Status | Artifact |
| --- | --- | --- | --- | --- |
| F-001-T1 | Serve `/catalog` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/catalog.py:27] |
| F-001-T2 | Serve `/catalog/register` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/catalog.py:86] |
| F-001-T3 | Serve `/export` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:12711] |
| F-001-T4 | Serve `/export/selective` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:12803] |
| F-001-T5 | Serve `/gateways` — 7 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:7391] |
| F-001-T6 | Serve `/gateways/impact-preview` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:7599] |
| F-001-T7 | Serve `/gateways/state` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:7320] |
| F-001-T8 | Serve `/gateways/toggle` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:7365] |
| F-001-T9 | Serve `/gateways/tools` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:7764] |
| F-001-T10 | Serve `/import` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:12872] |
| F-001-T11 | Serve `/import/cleanup` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:12992] |
| F-001-T12 | Serve `/import/status` — 2 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:12974] |
| F-001-T13 | Serve `/mcp-servers/test` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/mcp_servers_router.py:67] |
| F-001-T14 | Serve `/mcp-servers/test-handshake` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/mcp_servers_router.py:107] |
| F-001-T15 | Serve `/prompts` — 8 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:6883] |
| F-001-T16 | Serve `/prompts/state` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:6815] |
| F-001-T17 | Serve `/prompts/toggle` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:6857] |
| F-001-T18 | Serve `/resources` — 7 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:6316] |
| F-001-T19 | Serve `/resources/info` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:6622] |
| F-001-T20 | Serve `/resources/state` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:6248] |
| F-001-T21 | Serve `/resources/subscribe` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:6777] |
| F-001-T22 | Serve `/resources/templates` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:6200] |
| F-001-T23 | Serve `/resources/test` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:6498] |
| F-001-T24 | Serve `/resources/toggle` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:6290] |
| F-001-T25 | Serve `/roots` — 7 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:7837] |
| F-001-T26 | Serve `/roots/changes` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:7926] |
| F-001-T27 | Serve `/roots/export` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:7861] |
| F-001-T28 | Serve `/search` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/search.py:37] |
| F-001-T29 | Serve `/servers` — 7 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:4139] |
| F-001-T30 | Serve `/servers/.well-known` — 2 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/server_well_known.py:37] |
| F-001-T31 | Serve `/servers/message` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:4697] |
| F-001-T32 | Serve `/servers/prompts` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:4853] |
| F-001-T33 | Serve `/servers/resources` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:4817] |
| F-001-T34 | Serve `/servers/sse` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:4578] |
| F-001-T35 | Serve `/servers/state` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:4400] |
| F-001-T36 | Serve `/servers/test-handshake` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:4463] |
| F-001-T37 | Serve `/servers/toggle` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:4437] |
| F-001-T38 | Serve `/servers/tools` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:4771] |
| F-001-T39 | Serve `/tags` — 2 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:12605] |
| F-001-T40 | Serve `/tags/entities` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:12656] |
| F-001-T41 | Serve `/tools` — 7 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:5686] |
| F-001-T42 | Serve `/tools/generate-schemas-from-openapi` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/openapi_schema_router.py:43] |
| F-001-T43 | Serve `/tools/plugin_bindings` — 5 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/tool_plugin_bindings.py:220] |
| F-001-T44 | Serve `/tools/preview` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:5898] |
| F-001-T45 | Serve `/tools/state` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:6128] |
| F-001-T46 | Serve `/tools/toggle` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/main.py:6170] |
| F-001-T47 | Persist `gateways` (51 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:4710] |
| F-001-T48 | Persist `tools` (51 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:3305] |
| F-001-T49 | Persist `resources` (30 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:3690] |
| F-001-T50 | Persist `prompts` (29 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:4089] |
| F-001-T51 | Persist `servers` (24 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:4424] |
| F-001-T52 | Persist `resource_subscriptions` (5 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:4022] |
| F-001-T53 | Persist `grpc_services` (33 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:5260] |
| F-001-T54 | Persist `server_tool_association` (2 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2531] |
| F-001-T55 | Persist `server_resource_association` (2 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2539] |
| F-001-T56 | Persist `server_prompt_association` (2 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2547] |
| F-001-T57 | Persist `server_interfaces` (10 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:5167] |
| F-001-T58 | Persist `global_config` (2 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:2571] |

## Implementation status

States and what `done` costs: `../status-model.md`. A row starts at `todo` and reaches `done` only
when its done-when check ran **here** and the note records the command and result.

## Open questions

- OPEN: what work on this feature is in flight but not yet in the tree? A working tree shows what
  landed, never what is half-finished elsewhere.
- OPEN: which of these rows were one change and which accumulated over many? The grouping is by
  surface, not by the history that produced it.
- OPEN: What is the intended lifecycle of a discovered tool whose upstream gateway is deleted? The schema keeps the rows; no code path in the survey deletes them.
