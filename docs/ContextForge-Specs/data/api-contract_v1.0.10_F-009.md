---
title: API Contract v1.0.10 F-009 — Plugin Catalog
id: F-009
status: as-built
owner: TBD
updated: 2026-09-20
---

# API Contract v1.0.10 F-009 — Plugin Catalog

> Reversed from code, not written before it. `[D: path:line]` marks a derived fact you can
> reopen; `I:` marks a stated leap; `OPEN:` marks what the code cannot answer.

## Surface summary

This feature is the shipped plugin catalogue: 41 plugin directories, 38 carrying a
`plugin-manifest.yaml`, listed for activation in `plugins/config.yaml` [D: plugins/config.yaml:1].

These are content for F-007's framework, not a service. They expose no HTTP surface of their own
and own no table; a plugin is a hook implementation plus a manifest.

I: the three directories without a manifest are not loadable as plugins — basis: 38 of 41
directories carry one, and the loader resolves plugins by manifest [D: plugins/config.yaml:1].

## Endpoints

F-009 exposes no HTTP endpoint of its own. Its surface is a set of files on disk; see the Surface summary above.

## Events

No channel literal was found in this feature's files. That is a stated empty answer, not an omission — `schema/asyncapi_v1.0.10_F-009.json` is correspondingly empty.

## Error model

OPEN: this feature's error responses were not read handler by handler. The repository ships no OpenAPI document and no central error table, so the status codes and error body shape are not stated anywhere a reader can check.

## Versioning and compatibility

Plugin versioning is per manifest, not per gateway release
[D: plugins/config.yaml:1].

OPEN: whether a plugin manifest declares a compatible gateway version range.

## Spec files

- `schema/openapi_v1.0.10_F-009.json` — every path and method above, each with its `x-source` citation and the mounts it answers on. Request and response schemas are empty by design: nothing in the repository states them.
- `schema/asyncapi_v1.0.10_F-009.json` — channel names only.
- Entity shapes are `$ref`s into `schema/schemas.json`. No shape is redefined here.

## Traceability

Stories in `../PRDs/prd_v1.0.10_F-009-*.md` cite the endpoints above as evidence the behaviour
exists. They do not establish that it was wanted; see that document's own open questions.

## Open questions

- OPEN: Which of the 41 plugins are supported, and which are examples? The directory layout does not distinguish them.
- OPEN: What is the review bar for adding a plugin to this catalogue?
