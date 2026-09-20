---
title: API Contract v1.0.10 F-010 — Bundled MCP Servers and Templates
id: F-010
status: as-built
owner: TBD
updated: 2026-09-20
---

# API Contract v1.0.10 F-010 — Bundled MCP Servers and Templates

> Reversed from code, not written before it. `[D: path:line]` marks a derived fact you can
> reopen; `I:` marks a stated leap; `OPEN:` marks what the code cannot answer.

## Surface summary

This feature is the bundled MCP servers and the templates that generate new ones —
six Python servers under `mcp-servers/python/` and cookiecutter scaffolds for Go and Python.

They are separate products that happen to share the repository. Each carries its own manifest and
version [D: mcp-servers/python/data_analysis_server/pyproject.toml:3], and the gateway does not
import them; it federates them over MCP like any third-party peer.

Only `mcp_eval_server` exposes an HTTP surface of its own [D:
mcp-servers/python/mcp_eval_server/mcp_eval_server/rest_server.py:68].

## Endpoints

F-010 exposes no HTTP endpoint of its own. Its surface is a separate process with its own contract; see the Surface summary above.

## Events

No channel literal was found in this feature's files. That is a stated empty answer, not an omission — `schema/asyncapi_v1.0.10_F-010.json` is correspondingly empty.

## Error model

OPEN: this feature's error responses were not read handler by handler. The repository ships no OpenAPI document and no central error table, so the status codes and error body shape are not stated anywhere a reader can check.

## Versioning and compatibility

Each bundled server carries its own version, independent of the gateway's
[D: mcp-servers/python/data_analysis_server/pyproject.toml:3].

OPEN: which gateway versions each bundled server is tested against.

## Spec files

- `schema/openapi_v1.0.10_F-010.json` — every path and method above, each with its `x-source` citation and the mounts it answers on. Request and response schemas are empty by design: nothing in the repository states them.
- `schema/asyncapi_v1.0.10_F-010.json` — channel names only.
- Entity shapes are `$ref`s into `schema/schemas.json`. No shape is redefined here.

## Traceability

Stories in `../PRDs/prd_v1.0.10_F-010-*.md` cite the endpoints above as evidence the behaviour
exists. They do not establish that it was wanted; see that document's own open questions.

## Open questions

- OPEN: Are the bundled servers products, reference implementations, or test fixtures? All three readings fit the tree.
- OPEN: Which gateway versions is each bundled server tested against?
