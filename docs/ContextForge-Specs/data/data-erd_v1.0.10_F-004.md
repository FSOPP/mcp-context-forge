---
title: Data — v1.0.10 F-004 — Observability, Metrics and Audit
id: F-004
status: as-built
owner: TBD
updated: 2026-09-20
---

# Data — v1.0.10 F-004 — Observability, Metrics and Audit

> Reversed from the ORM models in `mcpgateway/db.py`, which is a consolidated snapshot of the
> shape the database has. The migration directory records how it got there and is the change
> story, not the shape.

## Entities

| Table | Columns | Required | Primary key | Foreign keys | Source |
| --- | --- | --- | --- | --- | --- |
| `observability_traces` | 16 | 5 | `trace_id` PK | — | [D: mcpgateway/db.py:2896] |
| `observability_spans` | 15 | 7 | `span_id` PK | `trace_id`→`observability_traces.trace_id`, `parent_span_id`→`observability_spans.span_id` | [D: mcpgateway/db.py:2963] |
| `observability_events` | 11 | 5 | `id` PK | `span_id`→`observability_spans.span_id` | [D: mcpgateway/db.py:3028] |
| `observability_metrics` | 11 | 6 | `id` PK | `trace_id`→`observability_traces.trace_id` | [D: mcpgateway/db.py:3085] |
| `observability_saved_queries` | 10 | 8 | `id` PK | — | [D: mcpgateway/db.py:3138] |
| `tool_metrics` | 6 | 5 | `id` PK | `tool_id`→`tools.id` | [D: mcpgateway/db.py:2592] |
| `resource_metrics` | 6 | 5 | `id` PK | `resource_id`→`resources.id` | [D: mcpgateway/db.py:2618] |
| `server_metrics` | 6 | 5 | `id` PK | `server_id`→`servers.id` | [D: mcpgateway/db.py:2644] |
| `prompt_metrics` | 6 | 5 | `id` PK | `prompt_id`→`prompts.id` | [D: mcpgateway/db.py:2670] |
| `tool_metrics_hourly` | 14 | 7 | `id` PK | `tool_id`→`tools.id` | [D: mcpgateway/db.py:2742] |
| `resource_metrics_hourly` | 14 | 7 | `id` PK | `resource_id`→`resources.id` | [D: mcpgateway/db.py:2767] |
| `prompt_metrics_hourly` | 14 | 7 | `id` PK | `prompt_id`→`prompts.id` | [D: mcpgateway/db.py:2792] |
| `server_metrics_hourly` | 14 | 7 | `id` PK | `server_id`→`servers.id` | [D: mcpgateway/db.py:2817] |
| `performance_snapshots` | 6 | 5 | `id` PK | — | [D: mcpgateway/db.py:3189] |
| `performance_aggregates` | 17 | 16 | `id` PK | — | [D: mcpgateway/db.py:3230] |
| `performance_metrics` | 17 | 16 | `id` PK | — | [D: mcpgateway/db.py:6232] |
| `structured_log_entries` | 29 | 10 | `id` PK | — | [D: mcpgateway/db.py:6162] |
| `security_events` | 25 | 13 | `id` PK | `log_entry_id`→`structured_log_entries.id` | [D: mcpgateway/db.py:6279] |
| `audit_trails` | 26 | 7 | `id` PK | — | [D: mcpgateway/db.py:6645] |
| `migration_metadata` | 4 | 2 | `revision` PK, `key` PK | — | [D: mcpgateway/db.py:1156] |

The diagram is `schema/erd_v1.0.10_F-004.puml`. Field-level detail is `schema/schemas.json`, which this table must not restate — one definition per shape, and this is the summary view of it.

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
