---
title: Test Plan v1.0.10 F-005 — A2A Agent Federation
id: F-005
status: as-built
owner: TBD
updated: 2026-09-20
---

# Test Plan v1.0.10 F-005 — A2A Agent Federation

> **This document is inverted.** A test plan normally says what will be tested; this one records
> what *is* tested, reversed from the suite. Its useful half is the coverage holes at the end.

## Scope

20 test files map to F-005, carrying 707 surveyed
test cases.

A `-TC` row below is one test **file**, not one case. The survey found 24,797 cases across the
repository; one row each would produce a document nobody opens, and the file is the unit the suite
itself is organised in. Each row cites the file's first case so the row can be reopened.

## Test cases

| ID | File | Cases | Status | Source |
| --- | --- | --- | --- | --- |
| F-005-TC1 | `tests/integration/test_a2a_sdk_integration.py` | 26 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_a2a_sdk_integration.py:332] |
| F-005-TC2 | `tests/unit/mcpgateway/admin/test_admin_a2a_plugin_bindings.py` | 17 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/admin/test_admin_a2a_plugin_bindings.py:112] |
| F-005-TC3 | `tests/unit/mcpgateway/cache/test_a2a_stats_cache.py` | 1 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/cache/test_a2a_stats_cache.py:19] |
| F-005-TC4 | `tests/unit/mcpgateway/routers/test_a2a_agent_plugin_bindings.py` | 17 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_a2a_agent_plugin_bindings.py:118] |
| F-005-TC5 | `tests/unit/mcpgateway/services/test_a2a_agent_invoke_hooks.py` | 18 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_a2a_agent_invoke_hooks.py:122] |
| F-005-TC6 | `tests/unit/mcpgateway/services/test_a2a_agent_plugin_binding_service.py` | 31 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_a2a_agent_plugin_binding_service.py:91] |
| F-005-TC7 | `tests/unit/mcpgateway/services/test_a2a_domain_validation_coverage.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_a2a_domain_validation_coverage.py:23] |
| F-005-TC8 | `tests/unit/mcpgateway/services/test_a2a_ipv6_edge_cases.py` | 6 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_a2a_ipv6_edge_cases.py:31] |
| F-005-TC9 | `tests/unit/mcpgateway/services/test_a2a_server_service.py` | 31 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_a2a_server_service.py:87] |
| F-005-TC10 | `tests/unit/mcpgateway/services/test_a2a_service.py` | 253 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_a2a_service.py:169] |
| F-005-TC11 | `tests/unit/mcpgateway/services/test_a2a_service_uaid_security.py` | 34 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_a2a_service_uaid_security.py:46] |
| F-005-TC12 | `tests/unit/mcpgateway/services/test_a2a_uaid_allowlist.py` | 6 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_a2a_uaid_allowlist.py:20] |
| F-005-TC13 | `tests/unit/mcpgateway/test_a2a_agent.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_a2a_agent.py:136] |
| F-005-TC14 | `tests/unit/mcpgateway/test_a2a_domain_schemas.py` | 10 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_a2a_domain_schemas.py:26] |
| F-005-TC15 | `tests/unit/mcpgateway/test_a2a_jsonrpc_passthrough.py` | 66 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_a2a_jsonrpc_passthrough.py:99] |
| F-005-TC16 | `tests/unit/mcpgateway/test_a2a_passthrough_headers.py` | 53 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_a2a_passthrough_headers.py:90] |
| F-005-TC17 | `tests/unit/mcpgateway/test_a2a_plugin_header_security.py` | 16 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_a2a_plugin_header_security.py:42] |
| F-005-TC18 | `tests/unit/mcpgateway/test_a2a_uaid_coverage.py` | 9 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_a2a_uaid_coverage.py:46] |
| F-005-TC19 | `tests/unit/mcpgateway/test_internal_a2a_endpoints.py` | 66 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_internal_a2a_endpoints.py:98] |
| F-005-TC20 | `tests/unit/scripts/test_demo_a2a_agent.py` | 19 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/scripts/test_demo_a2a_agent.py:41] |

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
