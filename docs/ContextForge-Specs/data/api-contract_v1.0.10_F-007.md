---
title: API Contract v1.0.10 F-007 — Plugin Framework and Tool Operations
id: F-007
status: as-built
owner: TBD
updated: 2026-09-20
---

# API Contract v1.0.10 F-007 — Plugin Framework and Tool Operations

> Reversed from code, not written before it. `[D: path:line]` marks a derived fact you can
> reopen; `I:` marks a stated leap; `OPEN:` marks what the code cannot answer.

## Surface summary

This feature is the in-process plugin framework: discovery, lifecycle, hook
dispatch, and the bindings that attach a plugin to a specific tool or A2A agent.

The framework itself is not in this repository. `settings.plugins` proxies to
`cpex.framework.settings` [D: mcpgateway/config.py:4178], and `cpex` is pinned to an exact version
[D: pyproject.toml:74] with a resolver cut-off date alongside it [D: pyproject.toml:20].
`PLUGINS_ENABLED` and `PLUGINS_CONFIG_FILE` are therefore read by that package, not by
`mcpgateway/config.py`.

Plugins are configured by file, not by API: the HTTP surface here is the catalogue and the binding
tables, not a management API [D: mcpgateway/routers/plugins.py:26].

I: the plugin contract is treated as unstable — basis: the dependency carries both an exact
version pin [D: pyproject.toml:74] and a resolver cut-off date [D: pyproject.toml:20], where a
range would do for a stable one.

OPEN: what `cpex` guarantees across a version bump. This repository holds no copy of that
contract.

## Endpoints

| Method | Path | Auth | Source |
| --- | --- | --- | --- |
| GET | `/plugins`, `/v1/plugins` | `plugins.read` | [D: mcpgateway/routers/plugins.py:29] |
| POST | `/toolops/enrichment/enrich_tool`, `/v1/toolops/enrichment/enrich_tool` | `admin.system_config` | [D: mcpgateway/routers/toolops_router.py:144] |
| POST | `/toolops/validation/execute_tool_nl_testcases`, `/v1/toolops/validation/execute_tool_nl_testcases` | `admin.system_config` | [D: mcpgateway/routers/toolops_router.py:108] |
| POST | `/toolops/validation/generate_testcases`, `/v1/toolops/validation/generate_testcases` | `admin.system_config` | [D: mcpgateway/routers/toolops_router.py:66] |

## Events

No channel literal was found in this feature's files. That is a stated empty answer, not an omission — `schema/asyncapi_v1.0.10_F-007.json` is correspondingly empty.

## Error model

OPEN: this feature's error responses were not read handler by handler. The repository ships no OpenAPI document and no central error table, so the status codes and error body shape are not stated anywhere a reader can check.

## Versioning and compatibility

Two mounts of every core router are live: the canonical `/v1/**` path and an
unversioned legacy shim. `DeprecationHeadersMiddleware` stamps `Sunset`, `Deprecation`, `Link` and
`X-Deprecated-Endpoint` on the shim responses [D: mcpgateway/middleware/deprecation.py:154]. The
shim is excluded from the OpenAPI document, so `/v1` is the documented contract
[D: mcpgateway/api/v1/__init__.py:436].

`_LEGACY_PREFIXES` must be kept in sync with `_assemble_routers` by hand; a unit test fails when
they diverge [D: mcpgateway/middleware/deprecation.py:56].

OPEN: what the Sunset date actually is for this release, and whether any consumer still depends on
the unversioned paths. The date is supplied by the caller that constructs the middleware, not fixed
in the source.

## Spec files

- `schema/openapi_v1.0.10_F-007.json` — every path and method above, each with its `x-source` citation and the mounts it answers on. Request and response schemas are empty by design: nothing in the repository states them.
- `schema/asyncapi_v1.0.10_F-007.json` — channel names only.
- Entity shapes are `$ref`s into `schema/schemas.json`. No shape is redefined here.

## Traceability

Stories in `../PRDs/prd_v1.0.10_F-007-*.md` cite the endpoints above as evidence the behaviour
exists. They do not establish that it was wanted; see that document's own open questions.

## Open questions

- OPEN: What is the failure policy when a plugin hook raises? Whether the request fails or the plugin is skipped is a decision the framework makes and the documentation does not state.
- OPEN: Why is the framework off by default?
