---
title: Test Plan v1.0.10 F-008 — Admin Console
id: F-008
status: as-built
owner: TBD
updated: 2026-09-20
---

# Test Plan v1.0.10 F-008 — Admin Console

> **This document is inverted.** A test plan normally says what will be tested; this one records
> what *is* tested, reversed from the suite. Its useful half is the coverage holes at the end.

## Scope

18 test files map to F-008, carrying 307 surveyed
test cases.

A `-TC` row below is one test **file**, not one case. The survey found 24,797 cases across the
repository; one row each would produce a document nobody opens, and the file is the unit the suite
itself is organised in. Each row cites the file's first case so the row can be reopened.

## Test cases

| ID | File | Cases | Status | Source |
| --- | --- | --- | --- | --- |
| F-008-TC1 | `tests/integration/test_admin_bypass_owner_visibility.py` | 12 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_admin_bypass_owner_visibility.py:326] |
| F-008-TC2 | `tests/integration/test_session_admin_bypass.py` | 1 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_session_admin_bypass.py:232] |
| F-008-TC3 | `tests/playwright/regression/test_admin_crud_regression.py` | 10 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/regression/test_admin_crud_regression.py` — run that tree's own suite | [D: tests/playwright/regression/test_admin_crud_regression.py:121] |
| F-008-TC4 | `tests/playwright/test_admin_menu_visibility.py` | 6 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/test_admin_menu_visibility.py` — run that tree's own suite | [D: tests/playwright/test_admin_menu_visibility.py:396] |
| F-008-TC5 | `tests/playwright/test_admin_ui.py` | 6 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/test_admin_ui.py` — run that tree's own suite | [D: tests/playwright/test_admin_ui.py:25] |
| F-008-TC6 | `tests/playwright/test_admin_url_context.py` | 27 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/test_admin_url_context.py` — run that tree's own suite | [D: tests/playwright/test_admin_url_context.py:269] |
| F-008-TC7 | `tests/unit/mcpgateway/cache/test_admin_stats_cache.py` | 17 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/cache/test_admin_stats_cache.py:21] |
| F-008-TC8 | `tests/unit/mcpgateway/middleware/test_admin_csrf_binding.py` | 30 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/middleware/test_admin_csrf_binding.py:85] |
| F-008-TC9 | `tests/unit/mcpgateway/routers/test_runtime_admin_router.py` | 18 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_runtime_admin_router.py:158] |
| F-008-TC10 | `tests/unit/mcpgateway/services/test_team_id_admin_filter.py` | 2 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_team_id_admin_filter.py:44] |
| F-008-TC11 | `tests/unit/mcpgateway/services/test_team_id_admin_filter_rows.py` | 1 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_team_id_admin_filter_rows.py:186] |
| F-008-TC12 | `tests/unit/mcpgateway/test_admin_error_handlers.py` | 9 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_admin_error_handlers.py:86] |
| F-008-TC13 | `tests/unit/mcpgateway/test_admin_logout_token_revocation.py` | 7 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_admin_logout_token_revocation.py:86] |
| F-008-TC14 | `tests/unit/mcpgateway/test_admin_menu_visibility.py` | 18 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_admin_menu_visibility.py:19] |
| F-008-TC15 | `tests/unit/mcpgateway/test_admin_module.py` | 83 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_admin_module.py:152] |
| F-008-TC16 | `tests/unit/mcpgateway/test_admin_openapi.py` | 12 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_admin_openapi.py:53] |
| F-008-TC17 | `tests/unit/mcpgateway/test_admin_permission_helpers.py` | 25 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_admin_permission_helpers.py:38] |
| F-008-TC18 | `tests/unit/mcpgateway/test_admin_plugin_runtime.py` | 23 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_admin_plugin_runtime.py:182] |

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
