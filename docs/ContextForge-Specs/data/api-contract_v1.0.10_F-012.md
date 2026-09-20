---
title: API Contract v1.0.10 F-012 — Deployment and Operations
id: F-012
status: as-built
owner: TBD
updated: 2026-09-20
---

# API Contract v1.0.10 F-012 — Deployment and Operations

> Reversed from code, not written before it. `[D: path:line]` marks a derived fact you can
> reopen; `I:` marks a stated leap; `OPEN:` marks what the code cannot answer.

## Surface summary

This feature is how the product is shipped and run: a Helm chart, nine compose
files, Ansible playbooks, an nginx edge, and 29 GitHub Actions workflows.

It exposes no application surface. Its contract is the environment: 346 configuration keys read by
`mcpgateway/config.py` [D: mcpgateway/config.py:4037], of which 112 are secret-shaped and carry no
value in this documentation.

The survey reported this repository as having no CI configuration. That is a defect in the survey
tool, not a fact about the repository — 29 workflow files exist [D: .github/workflows/alembic-upgrade-validation.yml:1].

## Endpoints

F-012 exposes no HTTP endpoint of its own. Its surface is a set of files on disk; see the Surface summary above.

## Events

No channel literal was found in this feature's files. That is a stated empty answer, not an omission — `schema/asyncapi_v1.0.10_F-012.json` is correspondingly empty.

## Error model

OPEN: this feature's error responses were not read handler by handler. The repository ships no OpenAPI document and no central error table, so the status codes and error body shape are not stated anywhere a reader can check.

## Versioning and compatibility

The chart, the compose files and the Python package all carry version 1.0.10
[D: charts/mcp-stack/Chart.yaml:25].

OPEN: whether those versions are required to move together, or merely happen to match today.

## Spec files

- `schema/openapi_v1.0.10_F-012.json` — every path and method above, each with its `x-source` citation and the mounts it answers on. Request and response schemas are empty by design: nothing in the repository states them.
- `schema/asyncapi_v1.0.10_F-012.json` — channel names only.
- Entity shapes are `$ref`s into `schema/schemas.json`. No shape is redefined here.

## Traceability

Stories in `../PRDs/prd_v1.0.10_F-012-*.md` cite the endpoints above as evidence the behaviour
exists. They do not establish that it was wanted; see that document's own open questions.

## Open questions

- OPEN: Which deployment topology is the supported one? Nine compose files and a Helm chart describe several, and none is marked canonical.
- OPEN: What are the production sizing targets? `DB_POOL_SIZE` guidance exists in prose but no target load is stated.
- OPEN: What is the rollback procedure for a failed migration?
