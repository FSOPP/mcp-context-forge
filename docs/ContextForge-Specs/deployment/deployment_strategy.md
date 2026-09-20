---
title: Deployment Strategy — ContextForge
id: DEPLOY
status: as-built
owner: TBD
updated: 2026-09-20
---

# Deployment Strategy — ContextForge

> Reversed from manifests, compose files, the Helm chart and the `Makefile`. **Nothing here was
> executed.** Every command is `I:` — it is the command the repository declares, not one watched
> to succeed. Where a section needs a decision rather than a file, it is `OPEN:`.

## Targets

| Target | Artefact | Source |
| --- | --- | --- |
| Kubernetes / OpenShift | Helm chart `mcp-stack` `1.0.10` | [D: charts/mcp-stack/Chart.yaml:25] |
| Docker Compose | nine compose files | [D: docker-compose.yml:1] |
| Ansible | playbooks including an OpenShift path | [D: ansible/README.md:1] |
| Bare process | gunicorn, `make serve` | [D: Makefile:458] |
| Edge | nginx container | [D: infra/nginx/Dockerfile:1] |

The nine compose files are variants rather than stages: TLS, embedded, SSO, lite override, and
four observability back-ends (Phoenix ×2, Langfuse, OpenSearch SIEM)
[D: docker-compose.siem-opensearch.yml:1].

OPEN: which target is the supported one? Five exist and nothing in the repository marks one
canonical. A reader choosing today would be guessing.

## Configuration

The deployment contract is the environment. The survey recorded 346 configuration keys read by
`mcpgateway/config.py` [D: mcpgateway/config.py:4037], of which 112 are secret-shaped.

**No value for any key appears in this hub.** `.env.example` is a convention, not a guarantee, and
the survey read its keys without reading its values
[D: .env.example:1].

Precedence the repository states, strongest first: `mcpgateway/config.py` and runtime code, then
`Makefile` targets, then `.env.example` as a dev override, then docs and comments
[D: CLAUDE.md:556].

Feature flags are evaluated once at router assembly, so changing one needs a restart rather than a
reload [D: mcpgateway/api/v1/__init__.py:275].

## Database

Default SQLite, supported alternative PostgreSQL [D: mcpgateway/config.py:1630]. Alembic owns
schema change, and the repository requires a single head plus idempotent upgrades that check
before modifying [D: CLAUDE.md:389].

Pool sizing is a first-order concern rather than a tuning detail: a traced request opens four to
six independent sessions [D: mcpgateway/config.py:3661].

OPEN: what pool size does this deployment need? The repository gives guidance in prose and no
target load to size against.

## Pipeline

29 GitHub Actions workflows [D: .github/workflows/alembic-upgrade-validation.yml:1], including
migration validation, production compose smoke tests, conformance, dependency review,
multi-platform image builds and image scanning [D: .github/workflows/conformance.yml:1].

I: the pre-merge gate is the stated command sequence, not the workflow set — basis: the repository
names an ordered list of commands a PR must pass [D: CLAUDE.md:523] and never says which workflow
enforces which command.

OPEN: which workflows are required checks? That is a repository setting, not a file in the tree.

## Rollout

OPEN: rollout strategy. No canary, blue-green or progressive delivery configuration appears in the
chart or the compose files.

OPEN: rollback. `helm rollback` exists as a tool; whether a schema change can be rolled back with
it depends on each migration's `downgrade`, and the repository states the hermetic-downgrade rule
for migrations that read settings [D: CLAUDE.md:389] without stating a rollback procedure.

## Open questions

- OPEN: what are the production sizing targets — requests per second, concurrent sessions,
  federated gateway count? None is stated anywhere.
- OPEN: is the Rust runtime part of a supported deployment, and if so how is it versioned against
  the gateway? [D: crates/mcp_runtime/Cargo.toml:1]
- OPEN: what is the disaster-recovery position? No backup or restore procedure appears in the
  repository.
- OPEN: which observability back-end is the intended one? Four are wired and none is marked
  default.
