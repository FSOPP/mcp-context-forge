---
title: Resource & Cost Estimate — ContextForge
status: as-built
owner: TBD
updated: 2026-09-20
---

# Resource & Cost Estimate — ContextForge

> Reversed, which means almost entirely unanswerable. Cost and staffing are decisions recorded
> outside a repository. What the tree shows is contribution history and the services a deployment
> must run — neither of which is an estimate.

## Team shape

What the history shows, which ranks and does not prove:

- 44 contributors across 3213 commits.
- One contributor holds roughly 46% of file ownership.
- 925 files have a single contributor in their history.

I: this describes contribution, not team structure — basis: the figures come from commit
attribution, and published precision for history-derived attribution is around 29%
[D: CLAUDE.md:17].

OPEN: how many people work on this, in what roles, and how is that expected to change?

## Infrastructure and services

A deployment must run, at minimum:

| Service | Required | Source |
| --- | --- | --- |
| The gateway process | yes | [D: mcpgateway/main.py:2110] |
| A database — SQLite or PostgreSQL | yes | [D: mcpgateway/config.py:1630] |
| Redis | for caching and federation state | [D: mcpgateway/cache/session_registry.py:503] |
| The Rust runtime | optional, a separate binary | [D: crates/mcp_runtime/Cargo.toml:1] |
| An observability back-end | optional; four are wired | [D: docker-compose.siem-opensearch.yml:1] |
| An nginx edge | optional | [D: infra/nginx/Dockerfile:1] |

The one sizing number the code carries is the connection pool, and it is a default rather than a
target [D: mcpgateway/config.py:3661]. A traced request opens four to six connections, so the
pool is sized against traced concurrency rather than request concurrency
[D: mcpgateway/services/observability_service.py:228].

OPEN: what does one deployment cost to run? Nothing in the repository expresses a unit of load,
let alone a price for it.

## Estimate confidence

There is no estimate here to be confident about. The sizes in
`product-backlog.md` are derived from surveyed surface — route decorators and tables — which
measures what was built, not what it took.

## Open questions

- OPEN: what is the target deployment scale — tenants, federated gateways, requests per second?
- OPEN: what is the budget, and what does it constrain?
- OPEN: which services are mandatory in the supported topology? Five deployment targets exist and
  none is marked canonical.
