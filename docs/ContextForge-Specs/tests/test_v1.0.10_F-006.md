---
title: Test Plan v1.0.10 F-006 — LLM Gateway and Chat
id: F-006
status: as-built
owner: TBD
updated: 2026-09-20
---

# Test Plan v1.0.10 F-006 — LLM Gateway and Chat

> **This document is inverted.** A test plan normally says what will be tested; this one records
> what *is* tested, reversed from the suite. Its useful half is the coverage holes at the end.

## Scope

10 test files map to F-006, carrying 431 surveyed
test cases.

A `-TC` row below is one test **file**, not one case. The survey found 24,797 cases across the
repository; one row each would produce a document nobody opens, and the file is the unit the suite
itself is organised in. Each row cites the file's first case so the row can be reopened.

## Test cases

| ID | File | Cases | Status | Source |
| --- | --- | --- | --- | --- |
| F-006-TC1 | `tests/integration/test_llmchat_endpoints.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_llmchat_endpoints.py:103] |
| F-006-TC2 | `tests/playwright/operations/test_llm_config.py` | 8 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/operations/test_llm_config.py` — run that tree's own suite | [D: tests/playwright/operations/test_llm_config.py:42] |
| F-006-TC3 | `tests/unit/mcpgateway/routers/test_llm_admin_router.py` | 38 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_llm_admin_router.py:78] |
| F-006-TC4 | `tests/unit/mcpgateway/routers/test_llm_config_router.py` | 34 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_llm_config_router.py:106] |
| F-006-TC5 | `tests/unit/mcpgateway/routers/test_llm_proxy_router.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_llm_proxy_router.py:27] |
| F-006-TC6 | `tests/unit/mcpgateway/routers/test_llmchat_router.py` | 118 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_llmchat_router.py:78] |
| F-006-TC7 | `tests/unit/mcpgateway/services/test_llm_provider_service.py` | 52 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_llm_provider_service.py:64] |
| F-006-TC8 | `tests/unit/mcpgateway/services/test_llm_proxy_service.py` | 67 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_llm_proxy_service.py:70] |
| F-006-TC9 | `tests/unit/mcpgateway/test_llm_schemas.py` | 60 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_llm_schemas.py:50] |
| F-006-TC10 | `tests/unit/mcpgateway/test_models.py` | 26 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_models.py:54] |

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
