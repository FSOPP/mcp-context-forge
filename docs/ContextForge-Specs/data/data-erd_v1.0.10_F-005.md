---
title: Data — v1.0.10 F-005 — A2A Agent Federation
id: F-005
status: as-built
owner: TBD
updated: 2026-09-20
---

# Data — v1.0.10 F-005 — A2A Agent Federation

> Reversed from the ORM models in `mcpgateway/db.py`, which is a consolidated snapshot of the
> shape the database has. The migration directory records how it got there and is the change
> story, not the shape.

## Entities

| Table | Columns | Required | Primary key | Foreign keys | Source |
| --- | --- | --- | --- | --- | --- |
| `a2a_agents` | 41 | 15 | `id` PK | `team_id`→`email_teams.id`, `tool_id`→`tools.id` | [D: mcpgateway/db.py:4923] |
| `a2a_tasks` | 11 | 6 | `id` PK | `a2a_agent_id`→`a2a_agents.id` | [D: mcpgateway/db.py:5117] |
| `a2a_agent_auth` | 8 | 4 | `id` PK | `a2a_agent_id`→`a2a_agents.id` | [D: mcpgateway/db.py:5190] |
| `a2a_push_notification_configs` | 9 | 7 | `id` PK | `a2a_agent_id`→`a2a_agents.id` | [D: mcpgateway/db.py:5211] |
| `a2a_task_events` | 8 | 6 | `id` PK | `a2a_agent_id`→`a2a_agents.id` | [D: mcpgateway/db.py:5233] |
| `a2a_agent_metrics` | 7 | 6 | `id` PK | `a2a_agent_id`→`a2a_agents.id` | [D: mcpgateway/db.py:2697] |
| `a2a_agent_metrics_hourly` | 15 | 8 | `id` PK | `a2a_agent_id`→`a2a_agents.id` | [D: mcpgateway/db.py:2842] |
| `server_task_mappings` | 8 | 8 | `id` PK | `server_id`→`servers.id`, `agent_id`→`a2a_agents.id` | [D: mcpgateway/db.py:5146] |
| `a2a_agent_plugin_bindings` | 13 | 11 | `id` PK | `team_id`→`email_teams.id` | [D: mcpgateway/db.py:7010] |
| `server_a2a_association` | 2 | 2 | `server_id` PK, `a2a_agent_id` PK | `server_id`→`servers.id`, `a2a_agent_id`→`a2a_agents.id` | [D: mcpgateway/db.py:2555] |

The diagram is `schema/erd_v1.0.10_F-005.puml`. Field-level detail is `schema/schemas.json`, which this table must not restate — one definition per shape, and this is the summary view of it.

## Migrations

`mcpgateway/alembic/versions/` holds the change history for these tables
[D: mcpgateway/alembic/versions/356a2d4eed6f_uuid_change_for_prompt_and_resources.py:1]. The
repository requires one head and an idempotent upgrade that checks before it modifies
[D: CLAUDE.md:389].

I: the models are the authority over the migrations for *shape* — basis: the repository states
that a fresh database is created from `db.py` directly and migrations skip tables they do not
find [D: CLAUDE.md:389].

## Access pattern

OPEN: which of this feature's tables are read on the hot path and which only by the console. The
queries were not inventoried, and the two have very different indexing consequences.

## Open questions

- OPEN: retention and archival for these tables. No TTL is declared on any of them.
- OPEN: backward-compatibility window for a shape change here — what a client may still be
  sending when a column is dropped.
- OPEN: are the migrations reversible? A `downgrade` that loses data is indistinguishable from one
  that does not, without reading each.
