---
title: Fixtures — v1.0.10 F-009 — Plugin Catalog
id: F-009
status: as-built
owner: TBD
updated: 2026-09-20
---

# Fixtures — v1.0.10 F-009 — Plugin Catalog

> Minimal valid records, one per entity, generated from the required columns in
> `schema/schemas.json`. They are shape examples, not scenarios.

## Sets

| Entity | Records | Contents |
| --- | --- | --- |
| — | — | this feature owns no entity |

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
