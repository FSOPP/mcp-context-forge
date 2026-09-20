---
title: Test Plan v1.0.10 F-001 — MCP Registry and Federation
id: F-001
status: as-built
owner: TBD
updated: 2026-09-20
---

# Test Plan v1.0.10 F-001 — MCP Registry and Federation

> **This document is inverted.** A test plan normally says what will be tested; this one records
> what *is* tested, reversed from the suite. Its useful half is the coverage holes at the end.

## Scope

38 test files map to F-001, carrying 1251 surveyed
test cases.

A `-TC` row below is one test **file**, not one case. The survey found 24,797 cases across the
repository; one row each would produce a document nobody opens, and the file is the unit the suite
itself is organised in. Each row cites the file's first case so the row can be reopened.

## Test cases

| ID | File | Cases | Status | Source |
| --- | --- | --- | --- | --- |
| F-001-TC1 | `tests/e2e/test_search_e2e.py` | 3 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/e2e/test_search_e2e.py:137] |
| F-001-TC2 | `tests/integration/test_search_endpoint.py` | 16 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_search_endpoint.py:167] |
| F-001-TC3 | `tests/integration/test_team_search_query_sql.py` | 6 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_team_search_query_sql.py:69] |
| F-001-TC4 | `tests/integration/test_tools_pagination.py` | 7 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_tools_pagination.py:37] |
| F-001-TC5 | `tests/live_gateway/mcp/test_catalog_oauth_registration.py` | 3 | wip — unverified, `make test` collects only tests/ and never ran `tests/live_gateway/mcp/test_catalog_oauth_registration.py` — run that tree's own suite | [D: tests/live_gateway/mcp/test_catalog_oauth_registration.py:90] |
| F-001-TC6 | `tests/performance/test_bulk_import_performance.py` | 18 | wip — unverified, `make test` collects only tests/ and never ran `tests/performance/test_bulk_import_performance.py` — run that tree's own suite | [D: tests/performance/test_bulk_import_performance.py:285] |
| F-001-TC7 | `tests/playwright/entities/test_gateways_extended.py` | 79 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/entities/test_gateways_extended.py` — run that tree's own suite | [D: tests/playwright/entities/test_gateways_extended.py:65] |
| F-001-TC8 | `tests/playwright/entities/test_prompts.py` | 2 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/entities/test_prompts.py` — run that tree's own suite | [D: tests/playwright/entities/test_prompts.py:31] |
| F-001-TC9 | `tests/playwright/entities/test_prompts_extended.py` | 59 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/entities/test_prompts_extended.py` — run that tree's own suite | [D: tests/playwright/entities/test_prompts_extended.py:41] |
| F-001-TC10 | `tests/playwright/entities/test_resources.py` | 2 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/entities/test_resources.py` — run that tree's own suite | [D: tests/playwright/entities/test_resources.py:17] |
| F-001-TC11 | `tests/playwright/entities/test_resources_extended.py` | 57 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/entities/test_resources_extended.py` — run that tree's own suite | [D: tests/playwright/entities/test_resources_extended.py:42] |
| F-001-TC12 | `tests/playwright/entities/test_servers.py` | 2 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/entities/test_servers.py` — run that tree's own suite | [D: tests/playwright/entities/test_servers.py:17] |
| F-001-TC13 | `tests/playwright/entities/test_servers_extended.py` | 30 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/entities/test_servers_extended.py` — run that tree's own suite | [D: tests/playwright/entities/test_servers_extended.py:44] |
| F-001-TC14 | `tests/playwright/entities/test_tools.py` | 2 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/entities/test_tools.py` — run that tree's own suite | [D: tests/playwright/entities/test_tools.py:25] |
| F-001-TC15 | `tests/playwright/entities/test_tools_extended.py` | 74 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/entities/test_tools_extended.py` — run that tree's own suite | [D: tests/playwright/entities/test_tools_extended.py:49] |
| F-001-TC16 | `tests/playwright/operations/test_export_import.py` | 9 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/operations/test_export_import.py` — run that tree's own suite | [D: tests/playwright/operations/test_export_import.py:32] |
| F-001-TC17 | `tests/playwright/test_gateways.py` | 41 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/test_gateways.py` — run that tree's own suite | [D: tests/playwright/test_gateways.py:28] |
| F-001-TC18 | `tests/unit/mcpgateway/plugins/plugins/regex_filter/test_search_replace.py` | 34 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/plugins/plugins/regex_filter/test_search_replace.py:34] |
| F-001-TC19 | `tests/unit/mcpgateway/plugins/plugins/tools_telemetry_exporter/test_tools_telemetry_exporter.py` | 5 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/plugins/plugins/tools_telemetry_exporter/test_tools_telemetry_exporter.py:52] |
| F-001-TC20 | `tests/unit/mcpgateway/routers/test_catalog.py` | 26 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_catalog.py:56] |
| F-001-TC21 | `tests/unit/mcpgateway/routers/test_log_search.py` | 33 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_log_search.py:36] |
| F-001-TC22 | `tests/unit/mcpgateway/routers/test_log_search_activity.py` | 44 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_log_search_activity.py:171] |
| F-001-TC23 | `tests/unit/mcpgateway/routers/test_log_search_helpers.py` | 4 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_log_search_helpers.py:20] |
| F-001-TC24 | `tests/unit/mcpgateway/routers/test_mcp_servers_router.py` | 74 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_mcp_servers_router.py:119] |
| F-001-TC25 | `tests/unit/mcpgateway/routers/test_search_router.py` | 12 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_search_router.py:69] |
| F-001-TC26 | `tests/unit/mcpgateway/services/test_catalog_service.py` | 81 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_catalog_service.py:35] |
| F-001-TC27 | `tests/unit/mcpgateway/services/test_export_service.py` | 58 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_export_service.py:129] |
| F-001-TC28 | `tests/unit/mcpgateway/services/test_gateway_resources_prompts.py` | 8 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_gateway_resources_prompts.py:24] |
| F-001-TC29 | `tests/unit/mcpgateway/services/test_import_service.py` | 155 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_import_service.py:70] |
| F-001-TC30 | `tests/unit/mcpgateway/services/test_siem_export_service.py` | 6 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_siem_export_service.py:21] |
| F-001-TC31 | `tests/unit/mcpgateway/services/test_token_catalog_service.py` | 150 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_token_catalog_service.py:124] |
| F-001-TC32 | `tests/unit/mcpgateway/test_admin_catalog_htmx.py` | 7 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_admin_catalog_htmx.py:117] |
| F-001-TC33 | `tests/unit/mcpgateway/test_admin_ids_search.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_admin_ids_search.py:46] |
| F-001-TC34 | `tests/unit/mcpgateway/test_admin_import_export.py` | 12 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_admin_import_export.py:43] |
| F-001-TC35 | `tests/unit/mcpgateway/test_cli_export_import_coverage.py` | 36 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_cli_export_import_coverage.py:26] |
| F-001-TC36 | `tests/unit/mcpgateway/test_token_catalog_service_cache.py` | 11 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_token_catalog_service_cache.py:55] |
| F-001-TC37 | `tests/unit/mcpgateway/validation/test_tags.py` | 28 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/validation/test_tags.py:19] |
| F-001-TC38 | `tests/unit/scripts/test_fetch_catalog_icons.py` | 43 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/scripts/test_fetch_catalog_icons.py:48] |

## Coverage holes

Path groups in this feature that no test **name** mentions:

- `/mcp-servers/test`
- `/mcp-servers/test-handshake`

OPEN: a name-match is not coverage. Which of these paths are genuinely untested, and which are
tested by a case whose name does not say so? Answering needs a coverage run, not a survey.

## How to run

The repository's own command, from `Makefile`:

```
make test
```

It runs `pytest -n auto --maxfail=0` against an in-memory SQLite database
[D: Makefile:1], collecting only `tests/` and excluding seven paths inside it
[D: pyproject.toml:667].

## Implementation status

States and what `done` costs: `../status-model.md`. Every row is `todo` until the suite has run
here and the result is recorded in the note.

## Open questions

- OPEN: what is the coverage target for this feature, and is it enforced? A coverage
  configuration exists [D: pyproject.toml:809]; a threshold that fails a build does not appear in it.
- OPEN: which of these files are unit tests and which need a live gateway? The suite ignores
  `tests/live_gateway` by default [D: Makefile:1], so a second surface exists and is not run here.
- OPEN: are the deny-path regression tests the repository requires for security changes present
  for every security-sensitive route in this feature? The requirement is stated
  [D: CLAUDE.md:178]; whether it holds was not checked case by case.
