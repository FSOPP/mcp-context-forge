---
title: Runbook (DEV) — Local Setup
id: RB-001
type: DEV
status: as-built
owner: TBD
updated: 2026-09-20
---

# Runbook (DEV) — Local Setup

> Every command below is taken from the repository's own `Makefile` and `README`. **None of them
> was run while writing this document**, except `make test`, which is called out where it appears.
> An unrun command is marked `I:` — it is declared, not demonstrated.

## Preconditions

| Requirement | Value | Source |
| --- | --- | --- |
| Python | `>=3.12,<3.14` | [D: pyproject.toml:54] |
| Package manager | `uv` | [D: Makefile:284] |
| Node | required for the Admin UI bundle | [D: package.json:1] |
| Rust toolchain | only for `crates/mcp_runtime` | [D: crates/mcp_runtime/Cargo.toml:1] |
| Docker | only for the compose and production targets | [D: docker-compose.yml:1] |

A generated encryption secret is required before the gateway will start
[D: CLAUDE.md:281].

## Steps

1. Copy the environment template.

   ```
   cp .env.example .env
   ```

   I: this is the documented first step — basis: the repository states it as the setup entry point
   [D: CLAUDE.md:49]. Do not copy any value out of that file into a document.

2. Install with development dependencies. This also builds the Admin UI bundle.

   ```
   make install-dev
   ```

   I: declared, not run here — basis: the target exists and depends on `venv`
   [D: Makefile:325].

3. Check the environment against the template.

   ```
   make check-env
   ```

   I: declared, not run here — basis: the target exists [D: Makefile:377].

4. Generate the encryption secret.

   ```
   make init-secrets-patch-env
   ```

   I: declared, not run here — basis: the repository names this command as the way to produce
   `AUTH_ENCRYPTION_SECRET` [D: CLAUDE.md:281], and the target exists [D: Makefile:389].

5. Run the development server on port 8000 with autoreload.

   ```
   make dev
   ```

   I: declared, not run here — basis: the target exists [D: Makefile:480].

## Verification

```
make test
```

**This one was run.** It executes `pytest -n auto --maxfail=0` against an in-memory SQLite
database with reduced Argon2 parameters [D: Makefile:1]. The result of that run is recorded in
each feature's `../tests/test_v1.0.10_F-*.md` status rows and in `../tasks/tasks_v1.0.10_F-*.md`.

The suite ignores `tests/fuzz`, `tests/manual`, `test.py` and `tests/live_gateway`
[D: Makefile:1]. A live-gateway run is a separate surface:

```
make docker-nuke docker-prod-rust testing-up RUST_MCP_MODE=
make test-e2e
```

I: declared, not run here — basis: the repository names this sequence as the pre-merge gate
[D: CLAUDE.md:523] and the targets exist [D: Makefile:931].

## Rollback / cleanup

```
make docker-nuke
```

I: declared, not run here — basis: the target exists [D: Makefile:5267].

OPEN: what does `docker-nuke` remove beyond this project's containers? The name suggests a wide
blast radius and the target was not read line by line.

## Common failures

| Symptom | Likely cause | Source |
| --- | --- | --- |
| `Multiple heads are present` | a migration's `down_revision` does not point at the current head | [D: CLAUDE.md:389] |
| `Target database is not up to date` | `alembic upgrade head` has not run | [D: CLAUDE.md:389] |
| `QueuePool limit exceeded` | pool too small for the independent sessions per traced request | [D: mcpgateway/config.py:3661] |
| `This transaction is inactive` | a caller passed its own session into `log_action` | [D: CLAUDE.md:255] |
| intermittent `403 CSRF_TOKEN_INVALID` | `CSRF_COOKIE_NAME` or `CSRF_TOKEN_NAME` overridden | [D: mcpgateway/config.py:1801] |

That last row is a genuine find: the setting is overridable, and overriding it desynchronises the
middleware from every other consumer, which the code warns about at startup rather than refusing
[D: mcpgateway/config.py:1801].

## Open questions

- OPEN: how long does a cold `make install-dev` take on a clean machine? Not measured here.
- OPEN: which steps need network access, and what does the setup do behind a proxy?
- OPEN: is a local Redis required for any development path, or is it optional throughout?
