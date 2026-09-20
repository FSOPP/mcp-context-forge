---
title: Tasks v1.0.10 F-009 — Plugin Catalog
id: F-009
status: as-built
owner: TBD
updated: 2026-09-20
---

# Tasks v1.0.10 F-009 — Plugin Catalog

> **Inverted document.** These are not tasks to do; they are an inventory of shipped work, one row
> per unit that exists, each pointing at the artefact. The `done-when` column holds the check that
> *would* prove the row — which is what the status column then has to cash.

## Tasks

| ID | Task | Done when | Status | Artifact |
| --- | --- | --- | --- | --- |
| F-009-T1 | Ship the artefacts under `plugins/` | the feature's own build command succeeds here | wip — unverified, not covered by `make test` — `make test` does not collect plugins/; run that tree's own tests | [D: plugins/AGENTS.md:1] |

## Implementation status

States and what `done` costs: `../status-model.md`. A row starts at `todo` and reaches `done` only
when its done-when check ran **here** and the note records the command and result.

## Open questions

- OPEN: what work on this feature is in flight but not yet in the tree? A working tree shows what
  landed, never what is half-finished elsewhere.
- OPEN: which of these rows were one change and which accumulated over many? The grouping is by
  surface, not by the history that produced it.
- OPEN: Which of the 41 plugins are supported, and which are examples? The directory layout does not distinguish them.
