---
title: Master Data Model — ContextForge
id: DATA-MASTER
status: as-built
owner: TBD
updated: 2026-09-20
---

# Master Data Model — ContextForge

> One row per surveyed entity, with the feature that owns it and the definition site. Shapes are
> defined once in `schema/schemas.json` and drawn once in `schema/erd_master.puml`; this file is
> the registry, not a third copy.

## Registry

| Table | Owner | Columns | Defined at |
| --- | --- | --- | --- |
| `a2a_agent_auth` | F-005 | 8 columns | [D: mcpgateway/db.py:5190] |
| `a2a_agent_metrics` | F-005 | 7 columns | [D: mcpgateway/db.py:2697] |
| `a2a_agent_metrics_hourly` | F-005 | 15 columns | [D: mcpgateway/db.py:2842] |
| `a2a_agent_plugin_bindings` | F-005 | 13 columns | [D: mcpgateway/db.py:7010] |
| `a2a_agents` | F-005 | 41 columns | [D: mcpgateway/db.py:4923] |
| `a2a_push_notification_configs` | F-005 | 9 columns | [D: mcpgateway/db.py:5211] |
| `a2a_task_events` | F-005 | 8 columns | [D: mcpgateway/db.py:5233] |
| `a2a_tasks` | F-005 | 11 columns | [D: mcpgateway/db.py:5117] |
| `audit_trails` | F-004 | 26 columns | [D: mcpgateway/db.py:6645] |
| `email_api_tokens` | F-003 | 17 columns | [D: mcpgateway/db.py:5486] |
| `email_auth_events` | F-003 | 9 columns | [D: mcpgateway/db.py:1768] |
| `email_team_invitations` | F-003 | 9 columns | [D: mcpgateway/db.py:2255] |
| `email_team_join_requests` | F-003 | 10 columns | [D: mcpgateway/db.py:2358] |
| `email_team_member_history` | F-003 | 8 columns | [D: mcpgateway/db.py:2187] |
| `email_team_members` | F-003 | 8 columns | [D: mcpgateway/db.py:2119] |
| `email_teams` | F-003 | 11 columns | [D: mcpgateway/db.py:1976] |
| `email_users` | F-003 | 17 columns | [D: mcpgateway/db.py:1516] |
| `gateways` | F-001 | 51 columns | [D: mcpgateway/db.py:4710] |
| `global_config` | F-001 | 2 columns | [D: mcpgateway/db.py:2571] |
| `grpc_services` | F-001 | 33 columns | [D: mcpgateway/db.py:5260] |
| `llm_models` | F-006 | 16 columns | [D: mcpgateway/db.py:6587] |
| `llm_providers` | F-006 | 20 columns | [D: mcpgateway/db.py:6504] |
| `mcp_app_sessions` | F-002 | 8 columns | [D: mcpgateway/db.py:4036] |
| `mcp_messages` | F-002 | 5 columns | [D: mcpgateway/db.py:5340] |
| `mcp_sessions` | F-002 | 4 columns | [D: mcpgateway/db.py:5327] |
| `migration_metadata` | F-004 | 4 columns | [D: mcpgateway/db.py:1156] |
| `oauth_states` | F-003 | 10 columns | [D: mcpgateway/db.py:5387] |
| `oauth_tokens` | F-003 | 13 columns | [D: mcpgateway/db.py:5354] |
| `observability_events` | F-004 | 11 columns | [D: mcpgateway/db.py:3028] |
| `observability_metrics` | F-004 | 11 columns | [D: mcpgateway/db.py:3085] |
| `observability_saved_queries` | F-004 | 10 columns | [D: mcpgateway/db.py:3138] |
| `observability_spans` | F-004 | 15 columns | [D: mcpgateway/db.py:2963] |
| `observability_traces` | F-004 | 16 columns | [D: mcpgateway/db.py:2896] |
| `password_history` | F-003 | 4 columns | [D: mcpgateway/db.py:1932] |
| `password_reset_tokens` | F-003 | 8 columns | [D: mcpgateway/db.py:1881] |
| `pending_user_approvals` | F-003 | 12 columns | [D: mcpgateway/db.py:2453] |
| `performance_aggregates` | F-004 | 17 columns | [D: mcpgateway/db.py:3230] |
| `performance_metrics` | F-004 | 17 columns | [D: mcpgateway/db.py:6232] |
| `performance_snapshots` | F-004 | 6 columns | [D: mcpgateway/db.py:3189] |
| `permission_audit_log` | F-003 | 11 columns | [D: mcpgateway/db.py:1296] |
| `prompt_metrics` | F-004 | 6 columns | [D: mcpgateway/db.py:2670] |
| `prompt_metrics_hourly` | F-004 | 14 columns | [D: mcpgateway/db.py:2792] |
| `prompts` | F-001 | 29 columns | [D: mcpgateway/db.py:4089] |
| `registered_oauth_clients` | F-003 | 15 columns | [D: mcpgateway/db.py:5414] |
| `resource_metrics` | F-004 | 6 columns | [D: mcpgateway/db.py:2618] |
| `resource_metrics_hourly` | F-004 | 14 columns | [D: mcpgateway/db.py:2767] |
| `resource_subscriptions` | F-001 | 5 columns | [D: mcpgateway/db.py:4022] |
| `resources` | F-001 | 30 columns | [D: mcpgateway/db.py:3690] |
| `roles` | F-003 | 11 columns | [D: mcpgateway/db.py:1170] |
| `security_events` | F-004 | 25 columns | [D: mcpgateway/db.py:6279] |
| `server_a2a_association` | F-005 | 2 columns | [D: mcpgateway/db.py:2555] |
| `server_interfaces` | F-001 | 10 columns | [D: mcpgateway/db.py:5167] |
| `server_metrics` | F-004 | 6 columns | [D: mcpgateway/db.py:2644] |
| `server_metrics_hourly` | F-004 | 14 columns | [D: mcpgateway/db.py:2817] |
| `server_prompt_association` | F-001 | 2 columns | [D: mcpgateway/db.py:2547] |
| `server_resource_association` | F-001 | 2 columns | [D: mcpgateway/db.py:2539] |
| `server_task_mappings` | F-005 | 8 columns | [D: mcpgateway/db.py:5146] |
| `server_tool_association` | F-001 | 2 columns | [D: mcpgateway/db.py:2531] |
| `servers` | F-001 | 24 columns | [D: mcpgateway/db.py:4424] |
| `sso_auth_sessions` | F-003 | 9 columns | [D: mcpgateway/db.py:5821] |
| `sso_providers` | F-003 | 21 columns | [D: mcpgateway/db.py:5752] |
| `structured_log_entries` | F-004 | 29 columns | [D: mcpgateway/db.py:6162] |
| `token_revocations` | F-003 | 6 columns | [D: mcpgateway/db.py:5687] |
| `token_usage_logs` | F-003 | 12 columns | [D: mcpgateway/db.py:5630] |
| `tool_metrics` | F-004 | 6 columns | [D: mcpgateway/db.py:2592] |
| `tool_metrics_hourly` | F-004 | 14 columns | [D: mcpgateway/db.py:2742] |
| `tool_plugin_bindings` | F-007 | 13 columns | [D: mcpgateway/db.py:6929] |
| `toolops_test_cases` | F-007 | 3 columns | [D: mcpgateway/db.py:4064] |
| `tools` | F-001 | 51 columns | [D: mcpgateway/db.py:3305] |
| `user_roles` | F-003 | 10 columns | [D: mcpgateway/db.py:1223] |

Every table in `mcpgateway/db.py` is owned by exactly one feature.

## Relations

`schema/erd_master.puml` draws 77 relations, every one of them a declared `ForeignKey` target.

I: relations that exist only through application code are missing from that count — basis: the
diagram is built from `ForeignKey` declarations alone, and a join written in a query leaves no
trace in the model [D: mcpgateway/db.py:1129].

## System of record

OPEN: for federated primitives — tools, resources, prompts discovered from an upstream gateway —
which copy wins on conflict, this database or the upstream? Both hold one and the reconciliation
rule is not stated in the code.

## Retention

OPEN: no table declares a retention period. `delete_old_traces` exists for observability traces;
nothing schedules it in this repository, and no other table has an equivalent.

## Open questions

- OPEN: which feature introduced each entity? The migration history could rank this, and history
  ranks rather than proves — published precision for history-derived attribution is around 29%,
  so it is not written here as fact.
- OPEN: why is identity joined on `email_users.email` rather than on its `id` primary key? The
  choice is consistent across 21 tables, which makes it a decision rather than an accident.
