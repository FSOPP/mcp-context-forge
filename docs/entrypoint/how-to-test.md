---
title: How to Test — ContextForge
status: as-built
owner: TBD
updated: 2026-09-20
---

# How to Test — ContextForge

> Reversed from the suite as it stands. The full picture is
> `../ContextForge-Specs/tests/testing_strategy.md`.

## Running tests

```
make test          # pytest -n auto --maxfail=0, in-memory SQLite
make test-e2e      # MCP protocol and RBAC against a live gateway
npm test           # vitest, the Admin UI bundle
cargo test         # the Rust runtime, from crates/mcp_runtime
```

`make test` **ran here**: 23042 passed, 1 failed, 919 skipped, 2 xfailed, in 44:51
[D: Makefile:1].

It collects only `tests/` — `testpaths = ["tests"]` [D: pyproject.toml:667] — so nothing under
`mcp-servers/`, `plugins/`, `crates/` or `scripts/` runs at all. Inside `tests/`, seven more paths
are excluded between `addopts` [D: pyproject.toml:667] and the Makefile target [D: Makefile:1]:
`playwright`, `migration`, `performance`, `compliance`, `fuzz`, `manual`, `live_gateway`.

Check what a green run actually covered before reading it as coverage.

## Adding a test

Conventions live in `tests/AGENTS.md` [D: tests/AGENTS.md:1]. Two requirements the repository
states rather than suggests:

- A security-sensitive change needs deny-path regression tests: unauthenticated, wrong team,
  insufficient permission, feature disabled [D: CLAUDE.md:178].
- A PR whose behaviour can be exercised through a live gateway needs a full black-box test against
  a running one [D: CLAUDE.md:519].

I: a test name is treated as documentation here — basis: the coverage-hole sections in
`../ContextForge-Specs/tests/` were built by matching path groups against test names, and that
matching worked for most features [D: tests/AGENTS.md:1].

## Interpreting failures

The one failure in the run above is environmental rather than a product defect: the test invokes
`bash -lc`, which loads a login profile, then asserts the subprocess printed nothing to stdout
[D: tests/unit/test_docker_entrypoint.py:223]. On a machine whose profile prints anything — an
ssh-agent line, a version notice — it fails.

Other symptoms and their usual cause are tabulated in
`../ContextForge-Specs/runbook/runbook_DEV_RB-001-local-setup.md` § Common failures.

## Pointer

- Per-feature coverage and holes: `../ContextForge-Specs/tests/test_v1.0.10_F-nnn.md`
- Strategy and layer inventory: `../ContextForge-Specs/tests/testing_strategy.md`
- Status vocabulary: `../ContextForge-Specs/status-model.md`

## Open questions

- OPEN: what runs the four excluded suites, and how often?
- OPEN: what is the coverage threshold, and does anything fail a build on it?
- OPEN: is there a flaky-test policy? Nothing in the tree records one.
