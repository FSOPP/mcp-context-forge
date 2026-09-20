---
title: Feature Architecture v1.0.10 F-012 — Deployment and Operations
id: F-012
status: as-built
owner: TBD
updated: 2026-09-20
---

# Feature Architecture v1.0.10 F-012 — Deployment and Operations

> As-built. `[D: path:line]` is derived and reopenable, `I:` states its leap, `OPEN:` is a question
> the code cannot answer. Shared conventions live in `architect_common.md`; the system view lives
> in `architect.md`.

## Design summary

This feature is how the product is shipped and run: a Helm chart, nine compose
files, Ansible playbooks, an nginx edge, and 29 GitHub Actions workflows.

It exposes no application surface. Its contract is the environment: 346 configuration keys read by
`mcpgateway/config.py` [D: mcpgateway/config.py:4037], of which 112 are secret-shaped and carry no
value in this documentation.

The survey reported this repository as having no CI configuration. That is a defect in the survey
tool, not a fact about the repository — 29 workflow files exist [D: .github/workflows/alembic-upgrade-validation.yml:1].

Implementation lives in:

- `charts/`
- `ansible/`
- `infra/`
- `docker-compose`
- `Dockerfile`
- `Containerfile`
- `.github/workflows/`
- `Makefile`

## API contracts

0 route decorators belong to this feature. The readable
contract is `../data/api-contract_v1.0.10_F-012.md`; the machine-readable one is
`../data/schema/openapi_v1.0.10_F-012.json` and `../data/schema/asyncapi_v1.0.10_F-012.json`.

Request and response shapes are not stated in either. The repository ships no OpenAPI document,
and the handlers were not read field by field, so inventing those shapes here would be the one
thing this hub must not do.

## Data model

| table | fields | source |
| --- | --- | --- |
| — | — | this feature owns no table |

`../data/schema/erd_v1.0.10_F-012.puml` is deliberately empty and says so on its face.

## Sequence

OPEN: no runtime sequence. This feature's artefacts are build and deploy steps, and
none of them was executed here. The commands are listed in the runbook with that stated.

## Failure modes

OPEN: deployment failure modes were not exercised. Nothing was deployed here.

## Observability

OPEN: what is monitored in a deployment, and by what. The chart and compose files
declare services; nothing in them declares an alert.

## Traceability

- Stories: `../PRDs/prd_v1.0.10_F-012-*.md`
- Tasks: `../tasks/tasks_v1.0.10_F-012.md`
- Tests: `../tests/test_v1.0.10_F-012.md`
- Contract: `../data/api-contract_v1.0.10_F-012.md`

## Open questions

- OPEN: Which deployment topology is the supported one? Nine compose files and a Helm chart describe several, and none is marked canonical.
- OPEN: What are the production sizing targets? `DB_POOL_SIZE` guidance exists in prose but no target load is stated.
- OPEN: What is the rollback procedure for a failed migration?
