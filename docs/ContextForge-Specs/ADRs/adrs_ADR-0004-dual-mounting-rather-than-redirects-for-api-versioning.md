---
title: ADR-0004 — Dual mounting rather than redirects for API versioning
id: ADR-0004
status: accepted
owner: TBD
updated: 2026-09-20
---

# ADR-0004 — Dual mounting rather than redirects for API versioning

## Status

Accepted — **reconstructed from code, 2026-09-20**. Rationale not recovered.

This record was written by reading the codebase, not by the people who made the decision. The
Context and Consequences below are facts with citations. The Alternatives section is empty on
purpose.

## Context

Every core router is assembled once and mounted twice: under `/v1` and unversioned
[D: mcpgateway/api/v1/__init__.py:436]. The unversioned mount is excluded from the OpenAPI
document [D: mcpgateway/api/v1/__init__.py:436]. A pure-ASGI middleware stamps `Sunset`,
`Deprecation`, `Link` and `X-Deprecated-Endpoint` on shim responses, implemented outside
`BaseHTTPMiddleware` to avoid buffering SSE and streaming responses
[D: mcpgateway/middleware/deprecation.py:154]. The prefix set driving it is maintained by hand and
kept in sync by a unit test [D: mcpgateway/middleware/deprecation.py:56]. Two routers are mounted a
third time, under newer names [D: mcpgateway/api/v1/__init__.py:58].

## Decision

Both paths serve the same handlers. `/v1` is the documented contract; the unversioned
path is a deprecated shim carrying headers [D: mcpgateway/api/v1/__init__.py:436].

## Alternatives considered

OPEN: not recoverable. The repository retains no record of what was rejected, and inventing a
plausible alternatives table here would foreclose the discussion this record exists to reopen.

## Consequences

No client breaks on the move. Every route exists at two or three live paths, so any
path-based policy — rate limits, WAF rules, access logs, metrics labels — must cover all of them.
The hand-maintained prefix set is a standing sync obligation, which the repository already guards
with a test [D: mcpgateway/middleware/deprecation.py:56].

## Links

- `../architect/architect.md` § Decision index
- `../architect/architect_common.md` § Design patterns

## Open questions

- OPEN: who made this decision, when, and against what constraint?
- OPEN: what would have to change for it to be revisited?
- OPEN: was an alternative tried and abandoned? A discarded branch leaves no trace in a working
  tree.
