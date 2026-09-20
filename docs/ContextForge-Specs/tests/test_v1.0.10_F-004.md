---
title: Test Plan v1.0.10 F-004 — Observability, Metrics and Audit
id: F-004
status: as-built
owner: TBD
updated: 2026-09-20
---

# Test Plan v1.0.10 F-004 — Observability, Metrics and Audit

> **This document is inverted.** A test plan normally says what will be tested; this one records
> what *is* tested, reversed from the suite. Its useful half is the coverage holes at the end.

## Scope

52 test files map to F-004, carrying 1067 surveyed
test cases.

A `-TC` row below is one test **file**, not one case. The survey found 24,797 cases across the
repository; one row each would produce a document nobody opens, and the file is the unit the suite
itself is organised in. Each row cites the file's first case so the row can be reopened.

## Test cases

| ID | File | Cases | Status | Source |
| --- | --- | --- | --- | --- |
| F-004-TC1 | `scripts/test_rest_api_endpoints.py` | 4 | wip — unverified, `make test` collects only tests/ and never ran `scripts/test_rest_api_endpoints.py` — run that tree's own suite | [D: scripts/test_rest_api_endpoints.py:69] |
| F-004-TC2 | `tests/e2e/test_admin_apis.py` | 41 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/e2e/test_admin_apis.py:256] |
| F-004-TC3 | `tests/e2e/test_main_apis.py` | 113 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/e2e/test_main_apis.py:357] |
| F-004-TC4 | `tests/fuzz/test_api_schema_fuzz.py` | 7 | wip — unverified, `make test` collects only tests/ and never ran `tests/fuzz/test_api_schema_fuzz.py` — run that tree's own suite | [D: tests/fuzz/test_api_schema_fuzz.py:21] |
| F-004-TC5 | `tests/integration/test_api_versioning.py` | 23 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_api_versioning.py:50] |
| F-004-TC6 | `tests/integration/test_api_versioning_security.py` | 9 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_api_versioning_security.py:108] |
| F-004-TC7 | `tests/integration/test_metrics_cleanup_pg.py` | 4 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_metrics_cleanup_pg.py:127] |
| F-004-TC8 | `tests/integration/test_middleware_session_sharing.py` | 6 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_middleware_session_sharing.py:29] |
| F-004-TC9 | `tests/playwright/operations/test_observability.py` | 8 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/operations/test_observability.py` — run that tree's own suite | [D: tests/playwright/operations/test_observability.py:37] |
| F-004-TC10 | `tests/playwright/security/test_api_abuse_hardening.py` | 5 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/security/test_api_abuse_hardening.py` — run that tree's own suite | [D: tests/playwright/security/test_api_abuse_hardening.py:95] |
| F-004-TC11 | `tests/playwright/test_api_endpoints.py` | 5 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/test_api_endpoints.py` — run that tree's own suite | [D: tests/playwright/test_api_endpoints.py:20] |
| F-004-TC12 | `tests/playwright/test_api_integration.py` | 3 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/test_api_integration.py` — run that tree's own suite | [D: tests/playwright/test_api_integration.py:91] |
| F-004-TC13 | `tests/playwright/test_version_page.py` | 16 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/test_version_page.py` — run that tree's own suite | [D: tests/playwright/test_version_page.py:25] |
| F-004-TC14 | `tests/unit/mcpgateway/cache/test_metrics_cache.py` | 2 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/cache/test_metrics_cache.py:19] |
| F-004-TC15 | `tests/unit/mcpgateway/db/test_metrics_read_permission_migration.py` | 4 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/db/test_metrics_read_permission_migration.py:52] |
| F-004-TC16 | `tests/unit/mcpgateway/db/test_observability_migrations.py` | 9 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/db/test_observability_migrations.py:51] |
| F-004-TC17 | `tests/unit/mcpgateway/middleware/test_db_query_logging.py` | 20 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/middleware/test_db_query_logging.py:35] |
| F-004-TC18 | `tests/unit/mcpgateway/middleware/test_observability_middleware.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/middleware/test_observability_middleware.py:40] |
| F-004-TC19 | `tests/unit/mcpgateway/middleware/test_observability_middleware_transactions.py` | 11 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/middleware/test_observability_middleware_transactions.py:46] |
| F-004-TC20 | `tests/unit/mcpgateway/middleware/test_request_logging_middleware.py` | 66 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/middleware/test_request_logging_middleware.py:86] |
| F-004-TC21 | `tests/unit/mcpgateway/plugins/test_observability_adapter.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/plugins/test_observability_adapter.py:25] |
| F-004-TC22 | `tests/unit/mcpgateway/routers/test_compliance_router.py` | 17 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_compliance_router.py:73] |
| F-004-TC23 | `tests/unit/mcpgateway/routers/test_metrics_maintenance.py` | 10 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_metrics_maintenance.py:21] |
| F-004-TC24 | `tests/unit/mcpgateway/routers/test_observability_metrics.py` | 12 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_observability_metrics.py:164] |
| F-004-TC25 | `tests/unit/mcpgateway/routers/test_observability_sql.py` | 22 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_observability_sql.py:45] |
| F-004-TC26 | `tests/unit/mcpgateway/routers/test_siem.py` | 20 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_siem.py:21] |
| F-004-TC27 | `tests/unit/mcpgateway/services/test_compliance_service.py` | 26 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_compliance_service.py:145] |
| F-004-TC28 | `tests/unit/mcpgateway/services/test_logging_service.py` | 29 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_logging_service.py:54] |
| F-004-TC29 | `tests/unit/mcpgateway/services/test_logging_service_comprehensive.py` | 35 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_logging_service_comprehensive.py:46] |
| F-004-TC30 | `tests/unit/mcpgateway/services/test_metrics.py` | 11 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_metrics.py:48] |
| F-004-TC31 | `tests/unit/mcpgateway/services/test_metrics_api_coverage.py` | 7 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_metrics_api_coverage.py:32] |
| F-004-TC32 | `tests/unit/mcpgateway/services/test_metrics_buffer_service.py` | 61 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_metrics_buffer_service.py:25] |
| F-004-TC33 | `tests/unit/mcpgateway/services/test_metrics_cleanup_service.py` | 28 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_metrics_cleanup_service.py:39] |
| F-004-TC34 | `tests/unit/mcpgateway/services/test_metrics_exception_coverage.py` | 5 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_metrics_exception_coverage.py:84] |
| F-004-TC35 | `tests/unit/mcpgateway/services/test_metrics_query_service.py` | 45 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_metrics_query_service.py:27] |
| F-004-TC36 | `tests/unit/mcpgateway/services/test_metrics_rollup_service.py` | 42 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_metrics_rollup_service.py:35] |
| F-004-TC37 | `tests/unit/mcpgateway/services/test_observability_attribute_removal.py` | 5 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_observability_attribute_removal.py:17] |
| F-004-TC38 | `tests/unit/mcpgateway/services/test_observability_service.py` | 92 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_observability_service.py:58] |
| F-004-TC39 | `tests/unit/mcpgateway/services/test_tool_pre_invoke_logging.py` | 9 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_tool_pre_invoke_logging.py:24] |
| F-004-TC40 | `tests/unit/mcpgateway/test_admin_metrics_helpers.py` | 7 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_admin_metrics_helpers.py:24] |
| F-004-TC41 | `tests/unit/mcpgateway/test_admin_observability_sql.py` | 20 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_admin_observability_sql.py:38] |
| F-004-TC42 | `tests/unit/mcpgateway/test_api_v1.py` | 51 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_api_v1.py:108] |
| F-004-TC43 | `tests/unit/mcpgateway/test_api_versioning_parity.py` | 8 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_api_versioning_parity.py:44] |
| F-004-TC44 | `tests/unit/mcpgateway/test_metrics.py` | 16 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_metrics.py:62] |
| F-004-TC45 | `tests/unit/mcpgateway/test_metrics_aggregation_fix.py` | 6 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_metrics_aggregation_fix.py:22] |
| F-004-TC46 | `tests/unit/mcpgateway/test_metrics_coverage.py` | 18 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_metrics_coverage.py:38] |
| F-004-TC47 | `tests/unit/mcpgateway/test_observability.py` | 37 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_observability.py:71] |
| F-004-TC48 | `tests/unit/mcpgateway/test_observability_baggage_exceptions.py` | 3 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_observability_baggage_exceptions.py:22] |
| F-004-TC49 | `tests/unit/mcpgateway/test_observability_coverage.py` | 8 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_observability_coverage.py:19] |
| F-004-TC50 | `tests/unit/mcpgateway/test_ui_version.py` | 2 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_ui_version.py:42] |
| F-004-TC51 | `tests/unit/mcpgateway/test_version.py` | 28 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_version.py:112] |
| F-004-TC52 | `tests/unit/mcpgateway/utils/test_metrics_common.py` | 3 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/utils/test_metrics_common.py:16] |

## Coverage holes

Path groups in this feature that no test **name** mentions:

Every path group in this feature is named by at least one test name. That is a weak signal — a mention is not a test of the behaviour — and is stated as such.

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
