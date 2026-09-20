---
title: Data — v1.0.10 F-007 — Plugin Framework and Tool Operations
id: F-007
status: as-built
owner: TBD
updated: 2026-09-20
---

# Data — v1.0.10 F-007 — Plugin Framework and Tool Operations

> Reversed from the ORM models in `mcpgateway/db.py`, which is a consolidated snapshot of the
> shape the database has. The migration directory records how it got there and is the change
> story, not the shape.

## Entities

| Table | Columns | Required | Primary key | Foreign keys | Source |
| --- | --- | --- | --- | --- | --- |
| `tool_plugin_bindings` | 13 | 11 | `id` PK | `team_id`→`email_teams.id` | [D: mcpgateway/db.py:6929] |
| `toolops_test_cases` | 3 | 3 | `tool_id` PK | — | [D: mcpgateway/db.py:4064] |

The diagram is `schema/erd_v1.0.10_F-007.puml`. Field-level detail is `schema/schemas.json`, which this table must not restate — one definition per shape, and this is the summary view of it.

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
