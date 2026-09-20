---
title: Test Plan v1.0.10 F-002 — MCP Protocol Serving and Transports
id: F-002
status: as-built
owner: TBD
updated: 2026-09-20
---

# Test Plan v1.0.10 F-002 — MCP Protocol Serving and Transports

> **This document is inverted.** A test plan normally says what will be tested; this one records
> what *is* tested, reversed from the suite. Its useful half is the coverage holes at the end.

## Scope

35 test files map to F-002, carrying 834 surveyed
test cases.

A `-TC` row below is one test **file**, not one case. The survey found 24,797 cases across the
repository; one row each would produce a document nobody opens, and the file is the unit the suite
itself is organised in. Each row cites the file's first case so the row can be reopened.

## Test cases

| ID | File | Cases | Status | Source |
| --- | --- | --- | --- | --- |
| F-002-TC1 | `scripts/test_mcp_token_scoping.py` | 2 | wip — unverified, `make test` collects only tests/ and never ran `scripts/test_mcp_token_scoping.py` — run that tree's own suite | [D: scripts/test_mcp_token_scoping.py:103] |
| F-002-TC2 | `tests/compliance/mcp_2025_11_25/transport_core/test_streamable_http_protocol_header.py` | 2 | wip — unverified, `make test` collects only tests/ and never ran `tests/compliance/mcp_2025_11_25/transport_core/test_streamable_http_protocol_header.py` — run that tree's own suite | [D: tests/compliance/mcp_2025_11_25/transport_core/test_streamable_http_protocol_header.py:17] |
| F-002-TC3 | `tests/live_gateway/e2e_rust/test_mcp_access_matrix.py` | 5 | wip — unverified, `make test` collects only tests/ and never ran `tests/live_gateway/e2e_rust/test_mcp_access_matrix.py` — run that tree's own suite | [D: tests/live_gateway/e2e_rust/test_mcp_access_matrix.py:407] |
| F-002-TC4 | `tests/live_gateway/e2e_rust/test_mcp_session_isolation.py` | 10 | wip — unverified, `make test` collects only tests/ and never ran `tests/live_gateway/e2e_rust/test_mcp_session_isolation.py` — run that tree's own suite | [D: tests/live_gateway/e2e_rust/test_mcp_session_isolation.py:459] |
| F-002-TC5 | `tests/live_gateway/mcp/test_mcp_plugin_parity.py` | 5 | wip — unverified, `make test` collects only tests/ and never ran `tests/live_gateway/mcp/test_mcp_plugin_parity.py` — run that tree's own suite | [D: tests/live_gateway/mcp/test_mcp_plugin_parity.py:336] |
| F-002-TC6 | `tests/playwright/security/test_mcp_transport_auth_matrix.py` | 4 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/security/test_mcp_transport_auth_matrix.py` — run that tree's own suite | [D: tests/playwright/security/test_mcp_transport_auth_matrix.py:70] |
| F-002-TC7 | `tests/playwright/test_mcp_registry_page.py` | 23 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/test_mcp_registry_page.py` — run that tree's own suite | [D: tests/playwright/test_mcp_registry_page.py:22] |
| F-002-TC8 | `tests/security/test_rpc_api.py` | 1 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/security/test_rpc_api.py:31] |
| F-002-TC9 | `tests/security/test_rpc_endpoint_validation.py` | 5 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/security/test_rpc_endpoint_validation.py:55] |
| F-002-TC10 | `tests/security/test_rpc_input_validation.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/security/test_rpc_input_validation.py:124] |
| F-002-TC11 | `tests/security/test_validation.py` | 26 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/security/test_validation.py:27] |
| F-002-TC12 | `tests/unit/loadtest/test_locustfile_mcp_protocol.py` | 31 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/loadtest/test_locustfile_mcp_protocol.py:53] |
| F-002-TC13 | `tests/unit/mcpgateway/middleware/test_protocol_version.py` | 4 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/middleware/test_protocol_version.py:45] |
| F-002-TC14 | `tests/unit/mcpgateway/routers/test_cancellation_router.py` | 15 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_cancellation_router.py:43] |
| F-002-TC15 | `tests/unit/mcpgateway/routers/test_reverse_proxy.py` | 76 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_reverse_proxy.py:72] |
| F-002-TC16 | `tests/unit/mcpgateway/services/test_a2a_protocol.py` | 114 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_a2a_protocol.py:38] |
| F-002-TC17 | `tests/unit/mcpgateway/services/test_cancellation_service.py` | 23 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_cancellation_service.py:22] |
| F-002-TC18 | `tests/unit/mcpgateway/services/test_mcp_apps.py` | 37 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_mcp_apps.py:40] |
| F-002-TC19 | `tests/unit/mcpgateway/services/test_mcp_chat_history_extra.py` | 3 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_mcp_chat_history_extra.py:26] |
| F-002-TC20 | `tests/unit/mcpgateway/services/test_mcp_client_chat_service.py` | 56 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_mcp_client_chat_service.py:33] |
| F-002-TC21 | `tests/unit/mcpgateway/services/test_mcp_client_chat_service_extended.py` | 101 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_mcp_client_chat_service_extended.py:24] |
| F-002-TC22 | `tests/unit/mcpgateway/test_internal_mcp_auth_context_validation.py` | 9 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_internal_mcp_auth_context_validation.py:25] |
| F-002-TC23 | `tests/unit/mcpgateway/test_mcp_apps_protocol.py` | 2 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_mcp_apps_protocol.py:17] |
| F-002-TC24 | `tests/unit/mcpgateway/test_mcp_apps_security.py` | 47 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_mcp_apps_security.py:56] |
| F-002-TC25 | `tests/unit/mcpgateway/test_mcp_method_registry.py` | 13 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_mcp_method_registry.py:39] |
| F-002-TC26 | `tests/unit/mcpgateway/test_reverse_proxy.py` | 81 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_reverse_proxy.py:51] |
| F-002-TC27 | `tests/unit/mcpgateway/test_rpc_backward_compatibility.py` | 4 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_rpc_backward_compatibility.py:36] |
| F-002-TC28 | `tests/unit/mcpgateway/test_rpc_permission_team_fallback.py` | 9 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_rpc_permission_team_fallback.py:49] |
| F-002-TC29 | `tests/unit/mcpgateway/test_rpc_tool_invocation.py` | 18 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_rpc_tool_invocation.py:57] |
| F-002-TC30 | `tests/unit/mcpgateway/transports/test_mcp_ingress_mount.py` | 9 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/transports/test_mcp_ingress_mount.py:35] |
| F-002-TC31 | `tests/unit/mcpgateway/transports/test_rust_mcp_public_proxy.py` | 19 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/transports/test_rust_mcp_public_proxy.py:167] |
| F-002-TC32 | `tests/unit/mcpgateway/transports/test_rust_mcp_runtime_proxy.py` | 20 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/transports/test_rust_mcp_runtime_proxy.py:39] |
| F-002-TC33 | `tests/unit/mcpgateway/transports/test_sse_transport.py` | 39 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/transports/test_sse_transport.py:31] |
| F-002-TC34 | `tests/unit/mcpgateway/transports/test_streamable_rpc_permission_fallback.py` | 5 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/transports/test_streamable_rpc_permission_fallback.py:40] |
| F-002-TC35 | `tests/unit/scripts/test_mcp_token_scoping.py` | 2 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/scripts/test_mcp_token_scoping.py:58] |

## Coverage holes

Path groups in this feature that no test **name** mentions:

- `/reverse-proxy/sessions`
- `/reverse-proxy/sessions/{session_id}`
- `/reverse-proxy/sessions/{session_id}/request`
- `/reverse-proxy/sse/{session_id}`
- `/reverse-proxy/ws`

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
