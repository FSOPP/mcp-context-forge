---
title: Testing Strategy — ContextForge
status: as-built
owner: TBD
updated: 2026-09-20
---

# Testing Strategy — ContextForge

> Reversed from the suite. This describes how the repository tests itself today, not how it
> intends to.

## Shape

1175 test files carrying 24,797 surveyed test cases, against 459 application files in
`mcpgateway/`. Test code outnumbers application code roughly two to one.

Layers present in the tree: `tests/unit`, `tests/integration`, `tests/e2e`, `tests/security`,
`tests/performance`, `tests/playwright`, `tests/loadtest`, `tests/compliance`, `tests/acceptance`,
`tests/async`, `tests/fuzz`, `tests/manual`, `tests/live_gateway`
[D: tests/AGENTS.md:1].

## Commands

| Command | Runs | Source |
| --- | --- | --- |
| `make test` | `pytest -n auto --maxfail=0`, in-memory SQLite | [D: Makefile:1] |
| `make test-e2e` | MCP protocol and RBAC against a live gateway | [D: Makefile:931] |
| `npm test` | `vitest run` for the Admin UI bundle | [D: package.json:1] |
| `cargo test` | the Rust runtime | [D: crates/mcp_runtime/Cargo.toml:1] |

**`make test` collects far less than the tree contains.** `testpaths = ["tests"]` limits
collection to that directory [D: pyproject.toml:667], so nothing under `mcp-servers/`, `plugins/`,
`crates/` or `scripts/` is collected at all. Within `tests/`, seven more paths are excluded —
`playwright`, `migration`, `performance` and `compliance` from `addopts`
[D: pyproject.toml:667], and `fuzz`, `manual` and `live_gateway` from the Makefile target
[D: Makefile:1].

That is the single most important thing to know about this suite, and it is why many status rows
in `test_v1.0.10_F-*.md` read `wip` despite a green headline number.

## Stated requirements

The repository requires deny-path regression tests for security-sensitive changes —
unauthenticated, wrong team, insufficient permission, feature disabled
[D: CLAUDE.md:178] — and a full black-box test against a running gateway for any PR whose behaviour
can be exercised through one [D: CLAUDE.md:519].

## Coverage

A coverage configuration exists [D: pyproject.toml:809]. No failing threshold appears in it.

OPEN: what is the coverage target, and does anything enforce it?

## Open questions

- OPEN: which layer is the intended primary one? Unit tests dominate by count; the compliance and
  e2e suites carry the contract.
- OPEN: why are four suites excluded from `make test`, and what runs them?
- OPEN: 523 test files could not be mapped to a feature by path. Are they cross-cutting by design,
  or is the mapping just crude?
- OPEN: is there a flaky-test policy? Nothing in the tree records one.
