---
title: How to Develop — ContextForge
status: as-built
owner: TBD
updated: 2026-09-20
---

# How to Develop — ContextForge

> Reversed from the repository's own `Makefile` and instructions. Commands not run while writing
> this are marked `I:`.

## Before you start

Read, in this order:

1. `../ContextForge-Specs/architect/architect.md` — the system view.
2. `../ContextForge-Specs/architect/architect_common.md` — conventions as practised.
3. The feature's route file, `../ContextForge-Specs/route/route_v1.0.10_F-nnn.md`, which names
   every document to read before touching that feature.

Set up with the repository's own sequence [D: CLAUDE.md:49]; the full runbook is
`../ContextForge-Specs/runbook/runbook_DEV_RB-001-local-setup.md`.

## Loop

```
make dev                 # autoreload on :8000
make pre-commit          # after writing code
make ruff bandit interrogate pylint verify
```

I: this is the repository's stated per-edit chain — basis: it lists these commands under Code
Quality and separates them from the once-per-PR gate [D: CLAUDE.md:63].

Before a PR, the gate runs once, in order [D: CLAUDE.md:523]:

```
make ruff interrogate pylint
make test
make coverage diff-cover
make docker-nuke docker-prod-rust testing-up RUST_MCP_MODE=
make test-e2e
make detect-secrets-scan
```

## Standards

- Python `>=3.12,<3.14`, type hints, strict mypy [D: pyproject.toml:54].
- Ruff with `D1` and `D417` selected, so docstrings and their parameter coverage are enforced
  [D: pyproject.toml:449]. Line length 200 [D: pyproject.toml:403].
- Comments are a last resort; a comment earns its place only for a durable constraint
  [D: CLAUDE.md:493].
- Commits are signed (`git commit -s`) and follow Conventional Commits [D: CLAUDE.md:515].
- **Never mention AI assistants in a PR or diff** [D: CLAUDE.md:563].

Adding a database column or table needs an Alembic migration whose `down_revision` is the current
head — check `alembic heads` first, never copy from an older migration [D: CLAUDE.md:366].

## Definition of done

A change is done when the pre-merge gate above passes and the feature's status rows in
`../ContextForge-Specs/tasks/` carry the command and its result. `done` asserts a check passed
here; see `../ContextForge-Specs/status-model.md`.

## Open questions

- OPEN: which CI workflows are required checks? That is a repository setting, not a file.
- OPEN: what is the expected review turnaround, and who reviews what?
