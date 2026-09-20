---
title: Fixtures — v1.0.10 F-004 — Observability, Metrics and Audit
id: F-004
status: as-built
owner: TBD
updated: 2026-09-20
---

# Fixtures — v1.0.10 F-004 — Observability, Metrics and Audit

> Minimal valid records, one per entity, generated from the required columns in
> `schema/schemas.json`. They are shape examples, not scenarios.

## Sets

| Entity | Records | Contents |
| --- | --- | --- |
| `audit_trails` | 1 rows | 7 required fields |
| `migration_metadata` | 1 rows | 2 required fields |
| `observability_events` | 1 rows | 5 required fields |
| `observability_metrics` | 1 rows | 6 required fields |
| `observability_saved_queries` | 1 rows | 8 required fields |
| `observability_spans` | 1 rows | 7 required fields |
| `observability_traces` | 1 rows | 5 required fields |
| `performance_aggregates` | 1 rows | 16 required fields |
| `performance_metrics` | 1 rows | 16 required fields |
| `performance_snapshots` | 1 rows | 5 required fields |
| `prompt_metrics` | 1 rows | 5 required fields |
| `prompt_metrics_hourly` | 1 rows | 7 required fields |
| `resource_metrics` | 1 rows | 5 required fields |
| `resource_metrics_hourly` | 1 rows | 7 required fields |
| `security_events` | 1 rows | 13 required fields |
| `server_metrics` | 1 rows | 5 required fields |
| `server_metrics_hourly` | 1 rows | 7 required fields |
| `structured_log_entries` | 1 rows | 10 required fields |
| `tool_metrics` | 1 rows | 5 required fields |
| `tool_metrics_hourly` | 1 rows | 7 required fields |

Every string field carries the literal `OPEN` rather than a plausible-looking value. A fixture
that reads like real data is the easiest way for an invented field to survive review.

No value here comes from an environment file. The survey recorded 112 secret-shaped configuration
keys and read none of their values [D: mcpgateway/config.py:4037].

## Scenarios

OPEN: what scenario is each set for? These were generated from the schema, not lifted from the
suite. The repository's own fixtures live in `tests/` and `conftest.py`
[D: conftest.py:1] and are richer; mapping them onto these entities was not done.

## Open questions

- OPEN: which of these entities needs a realistic fixture for a meaningful test, and what would
  make it realistic?
- OPEN: are there entity combinations that must appear together to be valid? Foreign keys say what
  may reference what; they do not say what must exist.
