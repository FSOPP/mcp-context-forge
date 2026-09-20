---
title: Feature Architecture v1.0.10 F-009 — Plugin Catalog
id: F-009
status: as-built
owner: TBD
updated: 2026-09-20
---

# Feature Architecture v1.0.10 F-009 — Plugin Catalog

> As-built. `[D: path:line]` is derived and reopenable, `I:` states its leap, `OPEN:` is a question
> the code cannot answer. Shared conventions live in `architect_common.md`; the system view lives
> in `architect.md`.

## Design summary

This feature is the shipped plugin catalogue: 41 plugin directories, 38 carrying a
`plugin-manifest.yaml`, listed for activation in `plugins/config.yaml` [D: plugins/config.yaml:1].

These are content for F-007's framework, not a service. They expose no HTTP surface of their own
and own no table; a plugin is a hook implementation plus a manifest.

I: the three directories without a manifest are not loadable as plugins — basis: 38 of 41
directories carry one, and the loader resolves plugins by manifest [D: plugins/config.yaml:1].

Implementation lives in:

- `plugins/`

## API contracts

0 route decorators belong to this feature. The readable
contract is `../data/api-contract_v1.0.10_F-009.md`; the machine-readable one is
`../data/schema/openapi_v1.0.10_F-009.json` and `../data/schema/asyncapi_v1.0.10_F-009.json`.

Request and response shapes are not stated in either. The repository ships no OpenAPI document,
and the handlers were not read field by field, so inventing those shapes here would be the one
thing this hub must not do.

## Data model

| table | fields | source |
| --- | --- | --- |
| — | — | this feature owns no table |

`../data/schema/erd_v1.0.10_F-009.puml` is deliberately empty and says so on its face.

## Sequence

A plugin is a directory with a manifest and a hook implementation
[D: plugins/config.yaml:1]. It has no request path of its own; it runs inside F-007's dispatch.

OPEN: the loading order and what happens when two plugins bind to the same hook on the same tool.

## Failure modes

OPEN: a failing plugin's effect on the request is F-007's policy, which lives in `cpex` [D: mcpgateway/config.py:4178].

## Observability

Execution metrics for this feature's primitives are written to the per-invocation
and hourly tables when `METRICS_ENABLED` style recording is on [D: mcpgateway/config.py:2394].
Traces and spans come from `ObservabilityMiddleware`, which covers every path not on the skip list
[D: mcpgateway/middleware/path_filter.py:33]. Audit rows are written through `log_action` on its
own session [D: mcpgateway/services/audit_trail_service.py:73].

OPEN: which of this feature's operations are expected to be alertable, and on what threshold. No
alert rule or SLO appears in the repository.

## Traceability

- Stories: `../PRDs/prd_v1.0.10_F-009-*.md`
- Tasks: `../tasks/tasks_v1.0.10_F-009.md`
- Tests: `../tests/test_v1.0.10_F-009.md`
- Contract: `../data/api-contract_v1.0.10_F-009.md`

## Open questions

- OPEN: Which of the 41 plugins are supported, and which are examples? The directory layout does not distinguish them.
- OPEN: What is the review bar for adding a plugin to this catalogue?
