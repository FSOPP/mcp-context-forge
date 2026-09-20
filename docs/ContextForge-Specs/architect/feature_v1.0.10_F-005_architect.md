---
title: Feature Architecture v1.0.10 F-005 — A2A Agent Federation
id: F-005
status: as-built
owner: TBD
updated: 2026-09-20
---

# Feature Architecture v1.0.10 F-005 — A2A Agent Federation

> As-built. `[D: path:line]` is derived and reopenable, `I:` states its leap, `OPEN:` is a question
> the code cannot answer. Shared conventions live in `architect_common.md`; the system view lives
> in `architect.md`.

## Design summary

This feature federates A2A agents the way F-001 federates MCP servers: an agent is
registered, its card is fetched, and its tasks are tracked through their lifecycle.

The surface is doubled the same way F-002's is — a public `/a2a` router and a matching
`/_internal/a2a/**` set for the Rust runtime, gated by the same trust predicate and additionally
disabled outright when A2A is off [D: mcpgateway/auth_context.py:654].

Cross-gateway routing is fail-closed. An empty `UAID_ALLOWED_DOMAINS` blocks every cross-gateway
call unless `UAID_ALLOW_ALL_DOMAINS` is set [D: mcpgateway/config.py:907].

Implementation lives in:

- `mcpgateway/services/a2a_service.py`
- `mcpgateway/routers/a2a_agent_plugin_bindings.py`
- `a2a-agents/`
- `mcpgateway/utils/uaid.py`

## API contracts

17 route decorators belong to this feature. The readable
contract is `../data/api-contract_v1.0.10_F-005.md`; the machine-readable one is
`../data/schema/openapi_v1.0.10_F-005.json` and `../data/schema/asyncapi_v1.0.10_F-005.json`.

Request and response shapes are not stated in either. The repository ships no OpenAPI document,
and the handlers were not read field by field, so inventing those shapes here would be the one
thing this hub must not do.

## Data model

| table | fields | source |
| --- | --- | --- |
| `a2a_agents` | 41 | [D: mcpgateway/db.py:4923] |
| `a2a_tasks` | 11 | [D: mcpgateway/db.py:5117] |
| `a2a_agent_auth` | 8 | [D: mcpgateway/db.py:5190] |
| `a2a_push_notification_configs` | 9 | [D: mcpgateway/db.py:5211] |
| `a2a_task_events` | 8 | [D: mcpgateway/db.py:5233] |
| `a2a_agent_metrics` | 7 | [D: mcpgateway/db.py:2697] |
| `a2a_agent_metrics_hourly` | 15 | [D: mcpgateway/db.py:2842] |
| `server_task_mappings` | 8 | [D: mcpgateway/db.py:5146] |
| `a2a_agent_plugin_bindings` | 13 | [D: mcpgateway/db.py:7010] |
| `server_a2a_association` | 2 | [D: mcpgateway/db.py:2555] |

10 tables, 122 columns. Full field detail is `../data/schema/schemas.json`; the diagram is `../data/schema/erd_v1.0.10_F-005.puml`.

## Sequence

Invoking an A2A agent follows F-001's shape — register, fetch the card, dispatch —
with a task lifecycle on top: `a2a_tasks` rows carry state and `a2a_task_events` records
transitions [D: mcpgateway/db.py:5117].

Cross-gateway routing adds an allowlist check before the outbound call, and forwards the caller's
bearer token so the remote gateway can run its own RBAC [D: mcpgateway/config.py:907].

OPEN: the task state machine. The states are columns; the legal transitions were not read.

## Failure modes

- Cross-gateway domain not in the allowlist: blocked, and an empty allowlist blocks
  everything [D: mcpgateway/config.py:907].
- Remote gateway returns 401 or 403: raised as `A2AAgentError` with troubleshooting text
  [D: mcpgateway/db.py:4923].
- A2A disabled: `/_internal/a2a/**` stops being trusted at the gate
  [D: mcpgateway/auth_context.py:654].

## Observability

Execution metrics for this feature's primitives are written to the per-invocation
and hourly tables when `METRICS_ENABLED` style recording is on [D: mcpgateway/config.py:2394].
Traces and spans come from `ObservabilityMiddleware`, which covers every path not on the skip list
[D: mcpgateway/middleware/path_filter.py:33]. Audit rows are written through `log_action` on its
own session [D: mcpgateway/services/audit_trail_service.py:73].

OPEN: which of this feature's operations are expected to be alertable, and on what threshold. No
alert rule or SLO appears in the repository.

## Traceability

- Stories: `../PRDs/prd_v1.0.10_F-005-*.md`
- Tasks: `../tasks/tasks_v1.0.10_F-005.md`
- Tests: `../tests/test_v1.0.10_F-005.md`
- Contract: `../data/api-contract_v1.0.10_F-005.md`

## Open questions

- OPEN: What is the trust model for a remote gateway in a cross-gateway call? Both sides must trust the same JWT issuer, and nothing states how that is established operationally.
- OPEN: What happens to an in-flight A2A task when its agent is deregistered?
