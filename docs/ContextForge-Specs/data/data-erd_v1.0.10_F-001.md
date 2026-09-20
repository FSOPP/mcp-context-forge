---
title: Data — v1.0.10 F-001 — MCP Registry and Federation
id: F-001
status: as-built
owner: TBD
updated: 2026-09-20
---

# Data — v1.0.10 F-001 — MCP Registry and Federation

> Reversed from the ORM models in `mcpgateway/db.py`, which is a consolidated snapshot of the
> shape the database has. The migration directory records how it got there and is the change
> story, not the shape.

## Entities

| Table | Columns | Required | Primary key | Foreign keys | Source |
| --- | --- | --- | --- | --- | --- |
| `gateways` | 51 | 16 | `id` PK | `team_id`→`email_teams.id` | [D: mcpgateway/db.py:4710] |
| `tools` | 51 | 18 | `id` PK | `gateway_id`→`gateways.id`, `grpc_service_id`→`grpc_services.id`, `team_id`→`email_teams.id` | [D: mcpgateway/db.py:3305] |
| `resources` | 30 | 9 | `id` PK | `gateway_id`→`gateways.id`, `team_id`→`email_teams.id` | [D: mcpgateway/db.py:3690] |
| `prompts` | 29 | 13 | `id` PK | `gateway_id`→`gateways.id`, `team_id`→`email_teams.id` | [D: mcpgateway/db.py:4089] |
| `servers` | 24 | 9 | `id` PK | `team_id`→`email_teams.id` | [D: mcpgateway/db.py:4424] |
| `resource_subscriptions` | 5 | 4 | `id` PK | `resource_id`→`resources.id` | [D: mcpgateway/db.py:4022] |
| `grpc_services` | 33 | 17 | `id` PK | `team_id`→`email_teams.id` | [D: mcpgateway/db.py:5260] |
| `server_tool_association` | 2 | 2 | `server_id` PK, `tool_id` PK | `server_id`→`servers.id`, `tool_id`→`tools.id` | [D: mcpgateway/db.py:2531] |
| `server_resource_association` | 2 | 2 | `server_id` PK, `resource_id` PK | `server_id`→`servers.id`, `resource_id`→`resources.id` | [D: mcpgateway/db.py:2539] |
| `server_prompt_association` | 2 | 2 | `server_id` PK, `prompt_id` PK | `server_id`→`servers.id`, `prompt_id`→`prompts.id` | [D: mcpgateway/db.py:2547] |
| `server_interfaces` | 10 | 7 | `id` PK | `server_id`→`servers.id` | [D: mcpgateway/db.py:5167] |
| `global_config` | 2 | 1 | `id` PK | — | [D: mcpgateway/db.py:2571] |

The diagram is `schema/erd_v1.0.10_F-001.puml`. Field-level detail is `schema/schemas.json`, which this table must not restate — one definition per shape, and this is the summary view of it.

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
