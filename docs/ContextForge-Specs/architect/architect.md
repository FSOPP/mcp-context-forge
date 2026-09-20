---
title: Master Architecture — ContextForge
id: ARCH-MASTER
status: as-built
owner: TBD
updated: 2026-09-20
---

# Master Architecture — ContextForge

> Reversed from the repository at commit `0b79a082`. What follows is a structural and behavioural
> view recovered from code. Deployment topology beyond what the manifests show, quality-attribute
> intent, and anything about people or process are **not** recoverable this way and are marked
> `OPEN:` rather than described.

## System context

ContextForge sits between MCP clients and a fleet of upstream capability providers. It registers
those providers, discovers what each one offers, and re-exposes a governed, composed view of them
on one endpoint.

| Actor | Direction | Interface | Source |
| --- | --- | --- | --- |
| MCP client | inbound | JSON-RPC over SSE, WebSocket, streamable HTTP, stdio | [D: mcpgateway/main.py:11542] |
| Admin operator | inbound | server-rendered console at `/admin` | [D: mcpgateway/admin.py:1889] |
| API consumer | inbound | REST under `/v1` | [D: mcpgateway/api/v1/__init__.py:436] |
| Upstream MCP server | outbound | MCP, registered as a `gateways` row | [D: mcpgateway/services/gateway_service.py:671] |
| A2A agent | outbound | agent card fetch and task dispatch | [D: mcpgateway/db.py:4923] |
| LLM provider | outbound | proxied chat and completion | [D: mcpgateway/main.py:13187] |
| Rust MCP runtime | both | HTTP over `/_internal/**` | [D: crates/mcp_runtime/src/lib.rs:2132] |
| Identity provider | inbound | SSO, and external IdP tokens | [D: mcpgateway/routers/sso.py:1] |

I: the product is a control plane rather than a data plane for tool output — basis: tool results
pass through `invoke_tool` and are returned to the caller, while the persisted tables hold
registrations, metrics and audit rows rather than payloads [D: mcpgateway/main.py:11947].

## Component view

| Component | Responsibility | Feature | Source |
| --- | --- | --- | --- |
| `routers/` | HTTP endpoint declaration, 30 modules | all | [D: mcpgateway/routers/well_known.py:117] |
| `services/` | business logic, 74 modules | all | [D: mcpgateway/services/gateway_service.py:671] |
| `middleware/` | auth context, RBAC, token scoping, deprecation, observability, CSRF, rate limiting; 24 modules | F-003, F-004 | [D: mcpgateway/middleware/rbac.py:55] |
| `transports/` | SSE, WebSocket, streamable HTTP, stdio; 11 modules | F-002 | [D: mcpgateway/transports/base.py:1] |
| `handlers/` | lifecycle signals and sampling | F-002 | [D: mcpgateway/handlers/sampling.py:1] |
| `db.py` | every ORM model, 70 tables in one module | all | [D: mcpgateway/db.py:1129] |
| `config.py` | 346 settings keys | all | [D: mcpgateway/config.py:4037] |
| `admin.py` + `admin_ui/` | the console and its bundle | F-008 | [D: mcpgateway/admin.py:1889] |
| `api/v1/__init__.py` | router assembly and dual mounting | all | [D: mcpgateway/api/v1/__init__.py:436] |
| `crates/mcp_runtime` | Rust sidecar, MCP termination | F-011 | [D: crates/mcp_runtime/Cargo.toml:1] |
| `plugins/` + `cpex` | hook framework and 41 implementations | F-007, F-009 | [D: mcpgateway/config.py:4178] |

Dependency direction is one-way: routers call services, services call `db.py`, and `db.py` calls
nothing in the application [D: mcpgateway/utils/grpc_validation.py:1].

The repository's own index reports seven strongly-connected component groups, including one inside
`mcpgateway` and one between `mcpgateway` and `tests`.

OPEN: are the circular dependency groups known and accepted, or unnoticed? They are visible in the
import graph and nothing in the tree records a decision about them.

## Data architecture

One relational store holds all 70 tables [D: mcpgateway/db.py:1129]. SQLite is the default and
PostgreSQL the supported alternative [D: mcpgateway/config.py:1630]. Redis is optional, used for
caching and for federation state [D: mcpgateway/cache/session_registry.py:503].

Entity groups, by owning feature:

| Group | Tables | Feature |
| --- | --- | --- |
| Registry — gateways, tools, resources, prompts, servers, associations | 12 | F-001 |
| Sessions and messages | 3 | F-002 |
| Identity, teams, roles, tokens, OAuth, SSO | 21 | F-003 |
| Traces, spans, metrics, rollups, logs, audit | 20 | F-004 |
| A2A agents, tasks, events, push configs | 10 | F-005 |
| LLM providers and models | 2 | F-006 |
| Plugin bindings and toolops cases | 2 | F-007 |

The full field-level model is `../data/schema/schemas.json`; the diagram is
`../data/schema/erd_master.puml`, which draws 70 entities and 77 declared foreign-key relations.

Two structural facts are worth stating because they shape every query:

- Identity joins on `email_users.email`, not on `email_users.id`, even though the table has an `id`
  primary key [D: mcpgateway/db.py:1516].
- Metrics are written twice, once per invocation and once per hour, one pair per primitive type
  [D: mcpgateway/db.py:2592] [D: mcpgateway/db.py:2742].

OPEN: what is the system of record for a federated tool's definition — this database, or the
upstream gateway it was discovered from? Both hold a copy and the reconciliation rule is not stated.

OPEN: retention. No table declares a TTL and only traces have a delete path.

## API surface

593 route decorators in `mcpgateway/`, each mounted at two or three paths
[D: mcpgateway/api/v1/__init__.py:436].

**The route table is not the whole API.** `/rpc` and `/mcp` dispatch on a JSON-RPC `method` field
through a 27-branch chain, and the terminal branch treats an unmatched method name as a registered
tool name [D: mcpgateway/main.py:11947]. The live operation list is therefore the `tools` table at
runtime, which no static reading of this repository can produce.

Three parallel surfaces exist over the same capabilities:

| Surface | Audience | Auth mechanism | Source |
| --- | --- | --- | --- |
| `/v1/**` | API consumers | RBAC per handler | [D: mcpgateway/middleware/rbac.py:921] |
| unversioned shim | legacy clients | same handlers, deprecation headers stamped | [D: mcpgateway/middleware/deprecation.py:154] |
| `/_internal/**` | the Rust runtime | trust gate plus encoded auth context | [D: mcpgateway/auth_context.py:638] |
| `/admin/**` | console operators | RBAC plus router-level CSRF | [D: mcpgateway/admin.py:1889] |

The repository ships no OpenAPI document; `/v1` is generated at runtime and the shim is excluded
from it [D: mcpgateway/api/v1/__init__.py:436].

## Cross-cutting concerns

**Authorisation** is two independent layers. Layer 1 decides visibility through one of two policy
functions depending on token type [D: mcpgateway/auth_context.py:246] [D: mcpgateway/auth.py:644].
Layer 2 decides action through `require_permission` on the handler
[D: mcpgateway/middleware/rbac.py:921]. Layer 1 narrowing does not restrict which team roles Layer 2
evaluates.

**Trust boundaries**, as drawn by where the auth middleware sits:

- Public edge: `/health`, `/ready`, `/.well-known/**`, the login routes.
- Authenticated edge: everything under `/v1` and `/admin`.
- Internal: `/_internal/**`, reachable only with a runtime auth context
  [D: mcpgateway/auth_context.py:638].
- Outbound: every upstream URL passes an SSRF validator before it is called
  [D: mcpgateway/utils/grpc_validation.py:1].

OPEN: why the internal boundary is a shared-secret trust gate rather than a mutual-TLS or
service-identity boundary. The mechanism is visible; the threat model it answers is not.

**Observability** does not participate in the request transaction, by construction
[D: mcpgateway/services/observability_service.py:228]. A traced request opens several independent
sessions, which makes connection-pool sizing a first-order concern rather than a tuning detail
[D: mcpgateway/config.py:3661].

**Feature flags** are evaluated once, at router assembly, rather than per request
[D: mcpgateway/api/v1/__init__.py:275]. A flag change needs a restart.

**Deprecation** is middleware that stamps four headers on the unversioned shim, driven by a
hand-maintained prefix set that a unit test keeps in sync with the assembly function
[D: mcpgateway/middleware/deprecation.py:56].

## Decision index

No ADR exists in this repository for any of the decisions above. Four are costly enough that their
reasoning is worth recovering from the people who made them, and each is recorded as a
reconstructed ADR stub in `../ADRs/` with an honest empty Alternatives section:

| Decision | Visible in code | Reasoning |
| --- | --- | --- |
| Synchronous SQLAlchemy in async handlers | [D: CLAUDE.md:429] | stated as deliberate, unexplained |
| Observability writes outside the request transaction | [D: mcpgateway/services/observability_service.py:228] | not recovered |
| Dual mounting rather than a redirect for `/v1` | [D: mcpgateway/api/v1/__init__.py:436] | not recovered |
| A Rust sidecar for MCP termination | [D: crates/mcp_runtime/Cargo.toml:1] | not recovered |

## Feature architecture index

| ID | Feature | Document |
| --- | --- | --- |
| F-001 | MCP Registry and Federation | `feature_v1.0.10_F-001_architect.md` |
| F-002 | MCP Protocol Serving and Transports | `feature_v1.0.10_F-002_architect.md` |
| F-003 | Identity, Teams and Access Control | `feature_v1.0.10_F-003_architect.md` |
| F-004 | Observability, Metrics and Audit | `feature_v1.0.10_F-004_architect.md` |
| F-005 | A2A Agent Federation | `feature_v1.0.10_F-005_architect.md` |
| F-006 | LLM Gateway and Chat | `feature_v1.0.10_F-006_architect.md` |
| F-007 | Plugin Framework and Tool Operations | `feature_v1.0.10_F-007_architect.md` |
| F-008 | Admin Console | `feature_v1.0.10_F-008_architect.md` |
| F-009 | Plugin Catalog | `feature_v1.0.10_F-009_architect.md` |
| F-010 | Bundled MCP Servers and Templates | `feature_v1.0.10_F-010_architect.md` |
| F-011 | Rust MCP Runtime | `feature_v1.0.10_F-011_architect.md` |
| F-012 | Deployment and Operations | `feature_v1.0.10_F-012_architect.md` |

## Open questions

- OPEN: what scale is this architecture built for? No target throughput, tenant count or federated
  gateway count appears anywhere in the repository.
- OPEN: which components are owned by which team? The repository index reports 925 files with a
  bus factor of one, which is a fact about history, not about intent.
- OPEN: is the Rust runtime the intended future of MCP termination, or an optimisation for one
  path? Both implementations are live and nothing states the plan.
- OPEN: why is there one database for all 70 tables rather than a split between the control plane
  and the observability store? The observability tables already run on independent sessions.
