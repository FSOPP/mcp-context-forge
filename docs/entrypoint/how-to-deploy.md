---
title: How to Deploy — ContextForge
status: as-built
owner: TBD
updated: 2026-09-20
---

# How to Deploy — ContextForge

> **Nothing here was executed.** Every command is the one the repository declares, marked `I:`
> because it was not watched to succeed. Targets and trade-offs:
> `../ContextForge-Specs/deployment/deployment_strategy.md`.

## Preconditions

- An `.env` derived from `.env.example`, with `AUTH_ENCRYPTION_SECRET` generated
  [D: CLAUDE.md:281]. No value from that file appears in any document here.
- A database. SQLite is the default, PostgreSQL the supported alternative
  [D: mcpgateway/config.py:1630].
- A decision about which target you are on. Five exist — Helm, nine compose files, Ansible, a bare
  gunicorn process, and an nginx edge — and none is marked canonical
  [D: charts/mcp-stack/Chart.yaml:25].

## Procedure

Helm, the Kubernetes path:

```
helm install mcp-stack charts/mcp-stack -f charts/mcp-stack/values.yaml
```

I: declared, not run here — basis: the chart and its values file exist
[D: charts/mcp-stack/values.yaml:1].

Compose, the local and CI path:

```
docker compose up -d
docker compose --profile experimental up -d      # adds the separate web UI
```

I: declared, not run here — basis: the compose file exists [D: docker-compose.yml:1] and the
experimental profile is documented [D: CLAUDE.md:319].

Bare process:

```
make serve          # gunicorn on :4444
make serve-ssl      # the same with TLS, creating certs if absent
```

I: declared, not run here — basis: both targets exist [D: Makefile:458].

Schema changes are applied by Alembic. `alembic heads` **was run here** and printed a single head,
`5e211ec89cad` [D: CLAUDE.md:366].

## Verification

```
curl -fsS http://<host>:4444/health
curl -fsS http://<host>:4444/ready
```

I: these are the health paths the code serves — basis: both are on the middleware skip list as
permanently unversioned, health-check endpoints [D: mcpgateway/middleware/deprecation.py:30].

A feature flag change needs a restart: flags are evaluated once at router assembly, not per
request [D: mcpgateway/api/v1/__init__.py:275].

## Rollback

```
helm rollback mcp-stack
make docker-nuke        # compose path; wide blast radius, read the target first
```

I: declared, not run here — basis: the target exists [D: Makefile:5267].

OPEN: whether a schema change can be rolled back with the application. That depends on each
migration's `downgrade`, and a migration reading settings must snapshot them to be hermetic
[D: CLAUDE.md:389]. No rollback procedure is written down.

## Open questions

- OPEN: which deployment target is supported?
- OPEN: what are the sizing targets? `DB_POOL_SIZE` guidance exists without a load to size against
  [D: mcpgateway/config.py:3661].
- OPEN: what is the backup and restore procedure? None appears in the repository.
