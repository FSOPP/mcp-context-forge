---
title: Test Plan v1.0.10 F-003 — Identity, Teams and Access Control
id: F-003
status: as-built
owner: TBD
updated: 2026-09-20
---

# Test Plan v1.0.10 F-003 — Identity, Teams and Access Control

> **This document is inverted.** A test plan normally says what will be tested; this one records
> what *is* tested, reversed from the suite. Its useful half is the coverage holes at the end.

## Scope

94 test files map to F-003, carrying 3645 surveyed
test cases.

A `-TC` row below is one test **file**, not one case. The survey found 24,797 cases across the
repository; one row each would produce a document nobody opens, and the file is the unit the suite
itself is organised in. Each row cites the file's first case so the row can be reopened.

## Test cases

| ID | File | Cases | Status | Source |
| --- | --- | --- | --- | --- |
| F-003-TC1 | `scripts/test_email_auth_api.py` | 137 | wip — unverified, `make test` collects only tests/ and never ran `scripts/test_email_auth_api.py` — run that tree's own suite | [D: scripts/test_email_auth_api.py:191] |
| F-003-TC2 | `tests/e2e/test_oauth_protected_resource.py` | 17 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/e2e/test_oauth_protected_resource.py:225] |
| F-003-TC3 | `tests/e2e/test_vault_plugin_a2a_e2e.py` | 3 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/e2e/test_vault_plugin_a2a_e2e.py:154] |
| F-003-TC4 | `tests/integration/test_admin_teams_ui.py` | 3 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_admin_teams_ui.py:39] |
| F-003-TC5 | `tests/integration/test_cross_env_auth.py` | 5 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_cross_env_auth.py:142] |
| F-003-TC6 | `tests/integration/test_external_idp_auth_integration.py` | 4 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_external_idp_auth_integration.py:46] |
| F-003-TC7 | `tests/integration/test_oauth_token_exchange_keycloak.py` | 5 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_oauth_token_exchange_keycloak.py:60] |
| F-003-TC8 | `tests/integration/test_rbac_management_endpoints.py` | 9 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_rbac_management_endpoints.py:183] |
| F-003-TC9 | `tests/integration/test_rbac_ownership_http.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_rbac_ownership_http.py:41] |
| F-003-TC10 | `tests/integration/test_sso_adfs_integration.py` | 15 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_sso_adfs_integration.py:150] |
| F-003-TC11 | `tests/integration/test_tool_auth_headers_api.py` | 7 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_tool_auth_headers_api.py:75] |
| F-003-TC12 | `tests/integration/test_vault_integration.py` | 20 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/integration/test_vault_integration.py:108] |
| F-003-TC13 | `tests/live_gateway/mcp/test_oauth_redirect_validation.py` | 1 | wip — unverified, `make test` collects only tests/ and never ran `tests/live_gateway/mcp/test_oauth_redirect_validation.py` — run that tree's own suite | [D: tests/live_gateway/mcp/test_oauth_redirect_validation.py:39] |
| F-003-TC14 | `tests/live_gateway/mcp/test_oauth_status_live.py` | 8 | wip — unverified, `make test` collects only tests/ and never ran `tests/live_gateway/mcp/test_oauth_status_live.py` — run that tree's own suite | [D: tests/live_gateway/mcp/test_oauth_status_live.py:232] |
| F-003-TC15 | `tests/live_gateway/sso/test_oauth_jwks_e2e.py` | 5 | wip — unverified, `make test` collects only tests/ and never ran `tests/live_gateway/sso/test_oauth_jwks_e2e.py` — run that tree's own suite | [D: tests/live_gateway/sso/test_oauth_jwks_e2e.py:316] |
| F-003-TC16 | `tests/playwright/security/test_rbac_admin.py` | 11 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/security/test_rbac_admin.py` — run that tree's own suite | [D: tests/playwright/security/test_rbac_admin.py:58] |
| F-003-TC17 | `tests/playwright/security/test_sso_management.py` | 5 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/security/test_sso_management.py` — run that tree's own suite | [D: tests/playwright/security/test_sso_management.py:83] |
| F-003-TC18 | `tests/playwright/test_auth.py` | 6 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/test_auth.py` — run that tree's own suite | [D: tests/playwright/test_auth.py:63] |
| F-003-TC19 | `tests/playwright/test_rbac_permissions.py` | 33 | wip — unverified, `make test` collects only tests/ and never ran `tests/playwright/test_rbac_permissions.py` — run that tree's own suite | [D: tests/playwright/test_rbac_permissions.py:350] |
| F-003-TC20 | `tests/security/test_rbac_decorator_coverage.py` | 5 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/security/test_rbac_decorator_coverage.py:102] |
| F-003-TC21 | `tests/unit/mcpgateway/cache/test_auth_cache_l1_l2.py` | 85 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/cache/test_auth_cache_l1_l2.py:51] |
| F-003-TC22 | `tests/unit/mcpgateway/cache/test_auth_cache_user.py` | 11 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/cache/test_auth_cache_user.py:66] |
| F-003-TC23 | `tests/unit/mcpgateway/db/test_a2a_agents_auth_value_migration.py` | 28 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/db/test_a2a_agents_auth_value_migration.py:78] |
| F-003-TC24 | `tests/unit/mcpgateway/db/test_oauth_tokens_constraint_migration.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/db/test_oauth_tokens_constraint_migration.py:110] |
| F-003-TC25 | `tests/unit/mcpgateway/db/test_rbac_permission_backfill_migration.py` | 43 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/db/test_rbac_permission_backfill_migration.py:55] |
| F-003-TC26 | `tests/unit/mcpgateway/db/test_rbac_unique_constraints_migration.py` | 22 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/db/test_rbac_unique_constraints_migration.py:112] |
| F-003-TC27 | `tests/unit/mcpgateway/middleware/test_auth_method_propagation.py` | 2 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/middleware/test_auth_method_propagation.py:39] |
| F-003-TC28 | `tests/unit/mcpgateway/middleware/test_auth_middleware.py` | 40 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/middleware/test_auth_middleware.py:17] |
| F-003-TC29 | `tests/unit/mcpgateway/middleware/test_http_auth_headers.py` | 54 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/middleware/test_http_auth_headers.py:62] |
| F-003-TC30 | `tests/unit/mcpgateway/middleware/test_http_auth_integration.py` | 25 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/middleware/test_http_auth_integration.py:38] |
| F-003-TC31 | `tests/unit/mcpgateway/middleware/test_rbac.py` | 153 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/middleware/test_rbac.py:67] |
| F-003-TC32 | `tests/unit/mcpgateway/middleware/test_rbac_admin_bypass.py` | 9 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/middleware/test_rbac_admin_bypass.py:93] |
| F-003-TC33 | `tests/unit/mcpgateway/middleware/test_rbac_endpoint_coverage.py` | 9 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/middleware/test_rbac_endpoint_coverage.py:107] |
| F-003-TC34 | `tests/unit/mcpgateway/plugins/plugins/vault/test_vault_plugin.py` | 37 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/plugins/plugins/vault/test_vault_plugin.py:67] |
| F-003-TC35 | `tests/unit/mcpgateway/plugins/plugins/vault/test_vault_plugin_smoke.py` | 3 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/plugins/plugins/vault/test_vault_plugin_smoke.py:42] |
| F-003-TC36 | `tests/unit/mcpgateway/routers/test_auth.py` | 46 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_auth.py:26] |
| F-003-TC37 | `tests/unit/mcpgateway/routers/test_email_auth_helpers.py` | 8 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_email_auth_helpers.py:41] |
| F-003-TC38 | `tests/unit/mcpgateway/routers/test_email_auth_router.py` | 83 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_email_auth_router.py:66] |
| F-003-TC39 | `tests/unit/mcpgateway/routers/test_oauth_router.py` | 205 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_oauth_router.py:68] |
| F-003-TC40 | `tests/unit/mcpgateway/routers/test_rbac_router.py` | 35 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_rbac_router.py:60] |
| F-003-TC41 | `tests/unit/mcpgateway/routers/test_sso_router.py` | 52 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_sso_router.py:25] |
| F-003-TC42 | `tests/unit/mcpgateway/routers/test_teams.py` | 79 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_teams.py:223] |
| F-003-TC43 | `tests/unit/mcpgateway/routers/test_teams_coverage.py` | 54 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_teams_coverage.py:145] |
| F-003-TC44 | `tests/unit/mcpgateway/routers/test_teams_v2.py` | 21 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_teams_v2.py:131] |
| F-003-TC45 | `tests/unit/mcpgateway/routers/test_tokens.py` | 88 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_tokens.py:114] |
| F-003-TC46 | `tests/unit/mcpgateway/routers/test_tokens_admin_delegation.py` | 15 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_tokens_admin_delegation.py:120] |
| F-003-TC47 | `tests/unit/mcpgateway/routers/test_vault_router.py` | 17 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/routers/test_vault_router.py:90] |
| F-003-TC48 | `tests/unit/mcpgateway/services/test_a2a_authorization_access.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_a2a_authorization_access.py:56] |
| F-003-TC49 | `tests/unit/mcpgateway/services/test_a2a_query_param_auth.py` | 13 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_a2a_query_param_auth.py:128] |
| F-003-TC50 | `tests/unit/mcpgateway/services/test_authorization_access.py` | 71 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_authorization_access.py:140] |
| F-003-TC51 | `tests/unit/mcpgateway/services/test_email_auth_basic.py` | 191 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_email_auth_basic.py:68] |
| F-003-TC52 | `tests/unit/mcpgateway/services/test_email_auth_get_user_cache.py` | 18 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_email_auth_get_user_cache.py:81] |
| F-003-TC53 | `tests/unit/mcpgateway/services/test_email_auth_service.py` | 19 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_email_auth_service.py:58] |
| F-003-TC54 | `tests/unit/mcpgateway/services/test_email_auth_service_admin_role_sync.py` | 14 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_email_auth_service_admin_role_sync.py:29] |
| F-003-TC55 | `tests/unit/mcpgateway/services/test_gateway_query_param_auth.py` | 11 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_gateway_query_param_auth.py:107] |
| F-003-TC56 | `tests/unit/mcpgateway/services/test_gateway_service_health_oauth.py` | 16 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_gateway_service_health_oauth.py:95] |
| F-003-TC57 | `tests/unit/mcpgateway/services/test_gateway_service_oauth_comprehensive.py` | 29 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_gateway_service_oauth_comprehensive.py:142] |
| F-003-TC58 | `tests/unit/mcpgateway/services/test_oauth_audience.py` | 20 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_oauth_audience.py:36] |
| F-003-TC59 | `tests/unit/mcpgateway/services/test_oauth_authorization_code_health.py` | 7 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_oauth_authorization_code_health.py:47] |
| F-003-TC60 | `tests/unit/mcpgateway/services/test_oauth_manager.py` | 137 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_oauth_manager.py:37] |
| F-003-TC61 | `tests/unit/mcpgateway/services/test_oauth_manager_pkce.py` | 131 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_oauth_manager_pkce.py:29] |
| F-003-TC62 | `tests/unit/mcpgateway/services/test_oauth_team_resolution.py` | 11 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_oauth_team_resolution.py:27] |
| F-003-TC63 | `tests/unit/mcpgateway/services/test_rbac_cross_team_isolation.py` | 8 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_rbac_cross_team_isolation.py:161] |
| F-003-TC64 | `tests/unit/mcpgateway/services/test_rbac_fail_closed.py` | 10 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_rbac_fail_closed.py:74] |
| F-003-TC65 | `tests/unit/mcpgateway/services/test_rbac_permission_matrix.py` | 15 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_rbac_permission_matrix.py:287] |
| F-003-TC66 | `tests/unit/mcpgateway/services/test_sso_admin_assignment.py` | 16 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_sso_admin_assignment.py:55] |
| F-003-TC67 | `tests/unit/mcpgateway/services/test_sso_approval_workflow.py` | 4 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_sso_approval_workflow.py:41] |
| F-003-TC68 | `tests/unit/mcpgateway/services/test_sso_entra_role_mapping.py` | 40 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_sso_entra_role_mapping.py:64] |
| F-003-TC69 | `tests/unit/mcpgateway/services/test_sso_generic_oidc_role_mapping.py` | 19 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_sso_generic_oidc_role_mapping.py:66] |
| F-003-TC70 | `tests/unit/mcpgateway/services/test_sso_service.py` | 292 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_sso_service.py:98] |
| F-003-TC71 | `tests/unit/mcpgateway/services/test_sso_user_normalization.py` | 73 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_sso_user_normalization.py:88] |
| F-003-TC72 | `tests/unit/mcpgateway/services/test_vault_coverage_boost.py` | 60 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_vault_coverage_boost.py:98] |
| F-003-TC73 | `tests/unit/mcpgateway/services/test_vault_token_backend.py` | 68 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/services/test_vault_token_backend.py:29] |
| F-003-TC74 | `tests/unit/mcpgateway/test_admin_rbac_ui.py` | 13 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_admin_rbac_ui.py:23] |
| F-003-TC75 | `tests/unit/mcpgateway/test_auth.py` | 282 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_auth.py:44] |
| F-003-TC76 | `tests/unit/mcpgateway/test_auth_context.py` | 12 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_auth_context.py:56] |
| F-003-TC77 | `tests/unit/mcpgateway/test_auth_context_email_precedence.py` | 16 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_auth_context_email_precedence.py:27] |
| F-003-TC78 | `tests/unit/mcpgateway/test_auth_context_redis_signing.py` | 12 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_auth_context_redis_signing.py:72] |
| F-003-TC79 | `tests/unit/mcpgateway/test_auth_context_root_admin.py` | 3 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_auth_context_root_admin.py:27] |
| F-003-TC80 | `tests/unit/mcpgateway/test_auth_coverage.py` | 15 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_auth_coverage.py:19] |
| F-003-TC81 | `tests/unit/mcpgateway/test_auth_helpers.py` | 19 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_auth_helpers.py:64] |
| F-003-TC82 | `tests/unit/mcpgateway/test_auth_idle_timeout.py` | 12 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_auth_idle_timeout.py:48] |
| F-003-TC83 | `tests/unit/mcpgateway/test_auth_logout.py` | 8 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_auth_logout.py:67] |
| F-003-TC84 | `tests/unit/mcpgateway/test_auth_ratelimiter_redis.py` | 13 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_auth_ratelimiter_redis.py:30] |
| F-003-TC85 | `tests/unit/mcpgateway/test_configurable_auth_header.py` | 29 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_configurable_auth_header.py:43] |
| F-003-TC86 | `tests/unit/mcpgateway/test_multi_auth_headers.py` | 22 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_multi_auth_headers.py:32] |
| F-003-TC87 | `tests/unit/mcpgateway/test_oauth_manager.py` | 67 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_oauth_manager.py:27] |
| F-003-TC88 | `tests/unit/mcpgateway/test_schemas_auth_validation.py` | 90 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/test_schemas_auth_validation.py:22] |
| F-003-TC89 | `tests/unit/mcpgateway/utils/test_external_idp_auth.py` | 69 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/utils/test_external_idp_auth.py:19] |
| F-003-TC90 | `tests/unit/mcpgateway/utils/test_proxy_auth.py` | 33 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/utils/test_proxy_auth.py:59] |
| F-003-TC91 | `tests/unit/mcpgateway/utils/test_services_auth.py` | 8 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/utils/test_services_auth.py:34] |
| F-003-TC92 | `tests/unit/mcpgateway/utils/test_sso_bootstrap.py` | 32 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/utils/test_sso_bootstrap.py:26] |
| F-003-TC93 | `tests/unit/mcpgateway/utils/test_url_auth.py` | 30 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/mcpgateway/utils/test_url_auth.py:25] |
| F-003-TC94 | `tests/unit/scripts/test_demo_a2a_agent_auth.py` | 2 | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; every case in this file passed | [D: tests/unit/scripts/test_demo_a2a_agent_auth.py:42] |

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
