---
title: Domain — Bundled MCP Servers and Templates
id: DOM-010
kind: domain
feature: F-010
status: as-built
owner: TBD
updated: 2026-09-20
---

# Domain — Bundled MCP Servers and Templates

> Reconstructed from code. Rules below were promoted from constraint comments written by the
> people who knew them; each cites both the statement and the site enforcing it. Motive is not
> recoverable and is asked, not written.

## Ubiquitous language

| Term | Means | Do not use for |
| --- | --- | --- |
| Bundled server | an MCP server shipped in this repository | gateway, which federates it |
| Template | a cookiecutter scaffold for a new server | — |

## Actors

| Actor | Role |
| --- | --- |
| Operator | runs a bundled server |
| Template user | scaffolds a new server |

## Business rules

**DOM-010-R1.** Raised when a URL fails SSRF validation. ``str(e)`` is always the generic caller-facing message "URL is not allowed" - the specific check that tripped is intentionally never included, so callers cannot leak internal network topology through error text.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcp-servers/python/url_to_markdown_server/src/url_to_markdown_server/ssrf.py:80].

**DOM-010-R2.** A Unicode (IDN) hostname must be IDNA-encoded to punycode before use. Pre-fix, httpx auto-punycoded the hostname when making the actual request; post-fix, validate_url() hands the hostname straight to a Host header, so a raw Unicode hostname must be normalized here or httpx's header encoder raises a

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcp-servers/python/url_to_markdown_server/tests/test_ssrf.py:631].

**DOM-010-R3.** Generic, fixed caller-facing message. Never interpolate the URL or the specific check that tripped into this string - that would help an attacker map internal network topology through error text.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcp-servers/python/url_to_markdown_server/src/url_to_markdown_server/ssrf.py:38].

**DOM-010-R4.** Rejected by the SSRF validator specifically (ssrf.py) - always the fixed, generic message, never anything more specific.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcp-servers/python/url_to_markdown_server/tests/e2e_verify_ssrf_fix.py:222].

**DOM-010-R5.** The exception message must never leak which check tripped.

I: promoted to a domain rule — basis: the constraint is stated in a comment at the site that enforces it [D: mcp-servers/python/url_to_markdown_server/tests/test_ssrf.py:515].

## Process flow

This feature has no request flow of its own; see `../architect/feature_v1.0.10_F-010_architect.md` § Sequence.

## Invariants

This feature persists nothing, so it declares no data invariant.

OPEN: what must stay true about this feature at runtime? Nothing in the code states it.

## Implementation status

States and what `done` costs: `../status-model.md`. Every row starts at `todo`; a rule reaches
`done` only when a test names the rule ID and that test passed here.

| Rule | Status | Evidence |
| --- | --- | --- |
| DOM-010-R1 | wip — implemented, no test names this rule ID | — |
| DOM-010-R2 | wip — implemented, no test names this rule ID | — |
| DOM-010-R3 | wip — implemented, no test names this rule ID | — |
| DOM-010-R4 | wip — implemented, no test names this rule ID | — |
| DOM-010-R5 | wip — implemented, no test names this rule ID | — |

## Open questions

- OPEN: Are the bundled servers products, reference implementations, or test fixtures? All three readings fit the tree.
- OPEN: Which gateway versions is each bundled server tested against?
- OPEN: which of the rules above the business would still hold if the code stopped enforcing them?
  A rule recovered from an enforcement site cannot distinguish policy from implementation detail.
