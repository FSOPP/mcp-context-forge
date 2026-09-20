---
title: Test Plan v1.0.10 F-010 — Bundled MCP Servers and Templates
id: F-010
status: as-built
owner: TBD
updated: 2026-09-20
---

# Test Plan v1.0.10 F-010 — Bundled MCP Servers and Templates

> **This document is inverted.** A test plan normally says what will be tested; this one records
> what *is* tested, reversed from the suite. Its useful half is the coverage holes at the end.

## Scope

8 test files map to F-010, carrying 138 surveyed
test cases.

A `-TC` row below is one test **file**, not one case. The survey found 24,797 cases across the
repository; one row each would produce a document nobody opens, and the file is the unit the suite
itself is organised in. Each row cites the file's first case so the row can be reopened.

## Test cases

| ID | File | Cases | Status | Source |
| --- | --- | --- | --- | --- |
| F-010-TC1 | `mcp-servers/python/data_analysis_server/tests/test_data_loader.py` | 14 | wip — unverified, `make test` collects only tests/ and never ran `mcp-servers/python/data_analysis_server/tests/test_data_loader.py` — run each bundled server's own `make test`, e.g. mcp-servers/python/data_analysis_server | [D: mcp-servers/python/data_analysis_server/tests/test_data_loader.py:26] |
| F-010-TC2 | `mcp-servers/python/graphviz_server/tests/test_server.py` | 10 | wip — unverified, `make test` collects only tests/ and never ran `mcp-servers/python/graphviz_server/tests/test_server.py` — run each bundled server's own `make test`, e.g. mcp-servers/python/data_analysis_server | [D: mcp-servers/python/graphviz_server/tests/test_server.py:17] |
| F-010-TC3 | `mcp-servers/python/mcp-rss-search/tests/test_server.py` | 23 | wip — unverified, `make test` collects only tests/ and never ran `mcp-servers/python/mcp-rss-search/tests/test_server.py` — run each bundled server's own `make test`, e.g. mcp-servers/python/data_analysis_server | [D: mcp-servers/python/mcp-rss-search/tests/test_server.py:101] |
| F-010-TC4 | `mcp-servers/python/mcp_eval_server/test_all_providers.py` | 1 | wip — unverified, `make test` collects only tests/ and never ran `mcp-servers/python/mcp_eval_server/test_all_providers.py` — run each bundled server's own `make test`, e.g. mcp-servers/python/data_analysis_server | [D: mcp-servers/python/mcp_eval_server/test_all_providers.py:77] |
| F-010-TC5 | `mcp-servers/python/mcp_eval_server/tests/test_server.py` | 17 | wip — unverified, `make test` collects only tests/ and never ran `mcp-servers/python/mcp_eval_server/tests/test_server.py` — run each bundled server's own `make test`, e.g. mcp-servers/python/data_analysis_server | [D: mcp-servers/python/mcp_eval_server/tests/test_server.py:25] |
| F-010-TC6 | `mcp-servers/python/url_to_markdown_server/tests/test_server.py` | 23 | wip — unverified, `make test` collects only tests/ and never ran `mcp-servers/python/url_to_markdown_server/tests/test_server.py` — run each bundled server's own `make test`, e.g. mcp-servers/python/data_analysis_server | [D: mcp-servers/python/url_to_markdown_server/tests/test_server.py:23] |
| F-010-TC7 | `mcp-servers/python/url_to_markdown_server/tests/test_ssrf.py` | 48 | wip — unverified, `make test` collects only tests/ and never ran `mcp-servers/python/url_to_markdown_server/tests/test_ssrf.py` — run each bundled server's own `make test`, e.g. mcp-servers/python/data_analysis_server | [D: mcp-servers/python/url_to_markdown_server/tests/test_ssrf.py:53] |
| F-010-TC8 | `mcp-servers/templates/python/{{cookiecutter.project_slug}}/tests/test_server.py` | 2 | wip — unverified, `make test` collects only tests/ and never ran `mcp-servers/templates/python/{{cookiecutter.project_slug}}/tests/test_server.py` — run each bundled server's own `make test`, e.g. mcp-servers/python/data_analysis_server | [D: mcp-servers/templates/python/{{cookiecutter.project_slug}}/tests/test_server.py:6] |

## Coverage holes

Path groups in this feature that no test **name** mentions:

Every path group in this feature is named by at least one test name. That is a weak signal — a mention is not a test of the behaviour — and is stated as such.

OPEN: a name-match is not coverage. Which of these paths are genuinely untested, and which are
tested by a case whose name does not say so? Answering needs a coverage run, not a survey.

## How to run

The repository's own command, from `Makefile`:

```
make test
```

It runs `pytest -n auto --maxfail=0` against an in-memory SQLite database
[D: Makefile:1], collecting only `tests/` and excluding seven paths inside it
[D: pyproject.toml:667].

## Implementation status

States and what `done` costs: `../status-model.md`. Every row is `todo` until the suite has run
here and the result is recorded in the note.

## Open questions

- OPEN: what is the coverage target for this feature, and is it enforced? A coverage
  configuration exists [D: pyproject.toml:809]; a threshold that fails a build does not appear in it.
- OPEN: which of these files are unit tests and which need a live gateway? The suite ignores
  `tests/live_gateway` by default [D: Makefile:1], so a second surface exists and is not run here.
- OPEN: are the deny-path regression tests the repository requires for security changes present
  for every security-sensitive route in this feature? The requirement is stated
  [D: CLAUDE.md:178]; whether it holds was not checked case by case.
