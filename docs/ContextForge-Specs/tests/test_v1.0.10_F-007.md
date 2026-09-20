---
title: Test Plan v1.0.10 F-007 — Plugin Framework and Tool Operations
id: F-007
status: as-built
owner: TBD
updated: 2026-09-20
---

# Test Plan v1.0.10 F-007 — Plugin Framework and Tool Operations

> **This document is inverted.** A test plan normally says what will be tested; this one records
> what *is* tested, reversed from the suite. Its useful half is the coverage holes at the end.

## Scope

28 test files map to F-007, carrying 614 surveyed
test cases.

A `-TC` row below is one test **file**, not one case. The survey found 24,797 cases across the
repository; one row each would produce a document nobody opens, and the file is the unit the suite
itself is organised in. Each row cites the file's first case so the row can be reopened.

## Test cases

| ID | File | Cases | Status | Source |
| --- | --- | --- | --- | --- |
| F-007-TC1 | `plugins/external/cedar/tests/test_cedarpolicyplugin.py` | 12 | wip — unverified, `make test` collects only tests/ and never ran `plugins/external/cedar/tests/test_cedarpolicyplugin.py` — run that tree's own suite | [D: plugins/external/cedar/tests/test_cedarpolicyplugin.py:22] |
| F-007-TC2 | `plugins/external/llmguard/tests/test_cache.py` | 17 | wip — unverified, `make test` collects only tests/ and never ran `plugins/external/llmguard/tests/test_cache.py` — run that tree's own suite | [D: plugins/external/llmguard/tests/test_cache.py:35] |
| F-007-TC3 | `plugins/external/llmguard/tests/test_llmguardplugin.py` | 45 | wip — unverified, `make test` collects only tests/ and never ran `plugins/external/llmguard/tests/test_llmguardplugin.py` — run that tree's own suite | [D: plugins/external/llmguard/tests/test_llmguardplugin.py:24] |
| F-007-TC4 | `plugins/external/llmguard/tests/test_policy.py` | 71 | wip — unverified, `make test` collects only tests/ and never ran `plugins/external/llmguard/tests/test_policy.py` — run that tree's own suite | [D: plugins/external/llmguard/tests/test_policy.py:30] |
| F-007-TC5 | `plugins/external/opa/tests/test_all.py` | 6 | wip — unverified, `make test` collects only tests/ and never ran `plugins/external/opa/tests/test_all.py` — run that tree's own suite | [D: plugins/external/opa/tests/test_all.py:41] |
| F-007-TC6 | `plugins/external/opa/tests/test_errors.py` | 6 | wip — unverified, `make test` collects only tests/ and never ran `plugins/external/opa/tests/test_errors.py` — run that tree's own suite | [D: plugins/external/opa/tests/test_errors.py:29] |
| F-007-TC7 | `plugins/external/opa/tests/test_opapluginfilter.py` | 7 | wip — unverified, `make test` collects only tests/ and never ran `plugins/external/opa/tests/test_opapluginfilter.py` — run that tree's own suite | [D: plugins/external/opa/tests/test_opapluginfilter.py:39] |
| F-007-TC8 | `tests/integration/plugins/test_output_length_guard_integration.py` | 28 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/plugins/test_output_length_guard_integration.py:30] |
| F-007-TC9 | `tests/integration/plugins/test_plugin_metrics_consumer_integration.py` | 11 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/plugins/test_plugin_metrics_consumer_integration.py:36] |
| F-007-TC10 | `tests/integration/plugins/test_span_attribute_customizer_integration.py` | 7 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/plugins/test_span_attribute_customizer_integration.py:98] |
| F-007-TC11 | `tests/integration/test_plugins_config_yaml_validation.py` | 1 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_plugins_config_yaml_validation.py:34] |
| F-007-TC12 | `tests/playwright/test_plugins_page.py` | 6 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/test_plugins_page.py` — run that tree's own suite | [D: tests/playwright/test_plugins_page.py:38] |
| F-007-TC13 | `tests/unit/mcpgateway/db/test_plugins_read_permission_migration.py` | 2 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/db/test_plugins_read_permission_migration.py:54] |
| F-007-TC14 | `tests/unit/mcpgateway/plugins/agent/test_agent_plugins.py` | 8 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/plugins/agent/test_agent_plugins.py:23] |
| F-007-TC15 | `tests/unit/mcpgateway/plugins/plugins/test_init_hooks_plugins.py` | 4 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/plugins/plugins/test_init_hooks_plugins.py:150] |
| F-007-TC16 | `tests/unit/mcpgateway/plugins/test_plugins_utils.py` | 38 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/plugins/test_plugins_utils.py:44] |
| F-007-TC17 | `tests/unit/mcpgateway/routers/test_plugins.py` | 6 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_plugins.py:60] |
| F-007-TC18 | `tests/unit/mcpgateway/services/test_resource_service_plugins.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_resource_service_plugins.py:127] |
| F-007-TC19 | `tests/unit/mcpgateway/test_toolops_altk_service.py` | 13 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_toolops_altk_service.py:36] |
| F-007-TC20 | `tests/unit/mcpgateway/test_toolops_utils.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_toolops_utils.py:20] |
| F-007-TC21 | `tests/unit/plugins/test_circuit_breaker.py` | 32 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/plugins/test_circuit_breaker.py:84] |
| F-007-TC22 | `tests/unit/plugins/test_encoded_exfil_detector.py` | 80 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/plugins/test_encoded_exfil_detector.py:43] |
| F-007-TC23 | `tests/unit/plugins/test_jwt_claims_extraction.py` | 7 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/plugins/test_jwt_claims_extraction.py:72] |
| F-007-TC24 | `tests/unit/plugins/test_secrets_detection.py` | 8 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/plugins/test_secrets_detection.py:29] |
| F-007-TC25 | `tests/unit/plugins/test_unified_pdp.py` | 46 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/plugins/test_unified_pdp.py:88] |
| F-007-TC26 | `tests/unit/plugins/test_unified_pdp_plugin.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/plugins/test_unified_pdp_plugin.py:80] |
| F-007-TC27 | `tests/unit/plugins/toon_encoder/test_toon.py` | 90 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/plugins/toon_encoder/test_toon.py:31] |
| F-007-TC28 | `tests/unit/plugins/toon_encoder/test_toon_encoder.py` | 21 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/plugins/toon_encoder/test_toon_encoder.py:48] |

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
