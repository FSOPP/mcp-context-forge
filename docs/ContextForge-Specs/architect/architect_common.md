---
title: Common Engineering Standards — ContextForge
id: ARCH-COMMON
status: as-built
owner: TBD
updated: 2026-09-20
---

# Common Engineering Standards — ContextForge

> Reversed from the repository as it stands at commit `0b79a082`. `[D: path:line]` marks a fact
> you can reopen; `I:` marks a stated leap; `OPEN:` marks what the code cannot answer. This
> document records conventions **as practised**, which is not the same as conventions as intended.

## Tech stack

| Layer | Choice | Version | Source |
| --- | --- | --- | --- |
| Language | Python | `>=3.12,<3.14` | [D: pyproject.toml:54] |
| Web framework | FastAPI on Starlette ASGI | `>=0.140.0` | [D: pyproject.toml:76] |
| ORM | SQLAlchemy, 2.0 `Mapped[]` declarative form | — | [D: mcpgateway/db.py:3305] |
| Migrations | Alembic | `>=1.19.1` | [D: pyproject.toml:65] |
| Server | gunicorn | `>=26.0.0` | [D: pyproject.toml:79] |
| Plugin framework | `cpex`, external, exact pin | `==0.1.3` | [D: pyproject.toml:74] |
| Sidecar runtime | Rust crate `contextforge_mcp_runtime` | — | [D: crates/mcp_runtime/Cargo.toml:1] |
| Admin UI | JavaScript bundle built with vite | — | [D: package.json:1] |
| Chart | Helm `mcp-stack` | `1.0.10` | [D: charts/mcp-stack/Chart.yaml:25] |

The Python package and the Helm chart both carry `1.0.10` [D: pyproject.toml:54]
[D: charts/mcp-stack/Chart.yaml:25].

OPEN: whether those two versions are required to move together. They match today; nothing in the
repository enforces it.

## Project layout

| Directory | Code files | Role |
| --- | --- | --- |
| `tests/` | 1033 | the suite [D: tests/AGENTS.md:1] |
| `mcpgateway/` | 459 | the gateway application [D: mcpgateway/main.py:2110] |
| `plugins/` | 122 | shipped plugin implementations [D: plugins/config.yaml:1] |
| `mcp-servers/` | 89 | bundled MCP servers and templates [D: mcp-servers/README.md:1] |
| `scripts/` | 34 | build and demo scripts [D: scripts/benchmark_middleware.py:1] |
| `.github/` | 9 | CI automation [D: .github/workflows/alembic-upgrade-validation.yml:1] |
| `crates/` | 7 | the Rust runtime [D: crates/mcp_runtime/Cargo.toml:1] |

Test code outnumbers application code roughly two to one.

Inside `mcpgateway/`, the layering is by kind: `routers/` declares HTTP endpoints, `services/`
holds business logic, `middleware/` holds cross-cutting request processing, `transports/` holds
protocol implementations, and `db.py` holds every ORM model in one file
[D: mcpgateway/db.py:1129].

I: the import rule the code obeys is one-way, routers to services to db — basis: `grpc_validation.py`
states the rule for its own case and says it depends on neither of the two modules that use it,
keeping the tree one-way [D: mcpgateway/utils/grpc_validation.py:1].

Two files carry a disproportionate share of the application: `mcpgateway/main.py` at 583 KiB with
184 route decorators, and `mcpgateway/admin.py` at 908 KiB with 208
[D: mcpgateway/main.py:3587] [D: mcpgateway/admin.py:1889].

OPEN: is the size of `main.py` and `admin.py` deliberate, or accumulated? Both are listed as bug
magnets in the repository's own index, and neither has been split.

## Naming conventions

As practised, and consistent across the tree [D: CLAUDE.md:472]:

- `snake_case` for functions and modules, `PascalCase` for classes, `UPPER_CASE` for constants.
- Table names are plural snake_case; the ORM class is singular PascalCase
  [D: mcpgateway/db.py:3305].
- Routers are named `<domain>_router` and declare their own prefix
  [D: mcpgateway/main.py:3587].
- Settings attributes are snake_case mirrors of the `UPPER_CASE` environment variable
  [D: mcpgateway/config.py:4037].
- A service raises its own error hierarchy: `GatewayError` and `ToolError` subclasses rather than
  generic exceptions [D: mcpgateway/services/gateway_service.py:671].

## Design patterns

**Synchronous SQLAlchemy inside async handlers.** `SessionLocal()` is used from async FastAPI
handlers and ASGI middleware rather than an async driver. The repository records this as a
deliberate design decision, not an oversight [D: CLAUDE.md:429].

**Separate session for best-effort writes.** Observability and audit writes open their own session
and commit immediately, so they survive a failed request and are not atomic with it
[D: mcpgateway/services/observability_service.py:228] [D: mcpgateway/services/audit_trail_service.py:73].

**Dual mounting for API versioning.** Every core router is mounted twice, once under `/v1` and once
unversioned, from one assembly function [D: mcpgateway/api/v1/__init__.py:436].

**Feature flags as mount-time conditions.** Whole routers are included or skipped on a settings
boolean rather than gated per-request [D: mcpgateway/api/v1/__init__.py:275].

**Policy points, not inline checks.** Token team interpretation and token scope evaluation each
have one named function the rest of the code is required to call
[D: mcpgateway/auth_context.py:246] [D: mcpgateway/middleware/rbac.py:55].

## Code quality

| Tool | Setting | Source |
| --- | --- | --- |
| Ruff lint | `select = ["E3","E4","E7","E9","F","D1","D417","PL","G004"]` | [D: pyproject.toml:449] |
| Ruff / Black | `line-length = 200` | [D: pyproject.toml:403] |
| mypy | configured, strict per project instruction | [D: pyproject.toml:634] |
| pytest | configured with markers including `slow` | [D: pyproject.toml:667] |
| coverage | configured | [D: pyproject.toml:809] |
| Secret scanning | `detect-secrets` with a checked-in baseline | [D: .secrets.baseline:1] |

`D1` and `D417` are selected, so a docstring and its parameter coverage are enforced rather than
encouraged [D: pyproject.toml:449].

CI is 29 GitHub Actions workflows [D: .github/workflows/alembic-upgrade-validation.yml:1].

OPEN: which of these workflows gate a merge and which are advisory. Required checks are a
repository setting, not a file in the tree.

## Security baseline

- Two-layer model: token scoping decides visibility, RBAC decides action
  [D: mcpgateway/middleware/rbac.py:55].
- Layer 1 fails closed: a missing `teams` claim resolves to public-only
  [D: mcpgateway/auth_context.py:246].
- 422 of 587 route decorators carry an explicit permission [D: mcpgateway/middleware/rbac.py:921].
- `/admin` is listed in `csrf_exempt_paths`, and CSRF on it is enforced by a router-level
  dependency instead [D: mcpgateway/api/v1/__init__.py:298].
- `/_internal/**` is authorised by a trust predicate rather than RBAC, and requires an encoded auth
  context on every route except `*/authenticate` [D: mcpgateway/auth_context.py:638].
- Outbound targets are validated against SSRF on both the Python and Rust sides
  [D: mcpgateway/utils/grpc_validation.py:1] [D: crates/mcp_runtime/src/backend_url_validator.rs:1].
- Secrets are stored through an `EncryptedText` column type rather than as plain text
  [D: mcpgateway/db.py:290].

112 of the 346 surveyed configuration keys are secret-shaped. No value for any of them appears in
this hub [D: mcpgateway/config.py:4037].

## Review checklist

OPEN: the review checklist is a team practice and is not recoverable from the working tree. The
repository states a pre-merge command sequence [D: CLAUDE.md:523], but what a reviewer is expected
to look for beyond those commands is not written down anywhere in the code.

## Open questions

- OPEN: which of these conventions are intentional and which are accidental? The code is
  consistent; consistency is not evidence of a decision.
- OPEN: what is the intended maximum size of a module before it is split? Two files are far beyond
  the rest and no threshold is stated.
- OPEN: why is `cpex` an external package rather than an in-tree module? The boundary is visible;
  the reason is not.
- OPEN: is the sync-SQLAlchemy decision scheduled for revisit, and against what trigger?
