---
title: ADR-0001 — Record Architecture Decisions
id: ADR-0001
status: accepted
owner: TBD
updated: 2026-09-20
---

# ADR-0001 — Record Architecture Decisions

## Status

Accepted — **reconstructed from code, 2026-09-20**. Rationale not recovered.

## Context

This repository contains no architecture decision records
[D: docs/ContextForge-Specs/ADRs/how-to-read.md:1]. It does contain decisions with visible cost,
and in several places it contains the *instruction* not to change one without recording why — the
synchronous-SQLAlchemy rule tells reviewers the pattern is deliberate and must not be converted
call site by call site [D: CLAUDE.md:429], and the audit-session rule tells callers not to pass a
shared session and states that changing it is "a deliberate design change requiring review"
[D: CLAUDE.md:256].

Those instructions live in `AGENTS.md`, a file whose stated purpose is guidance for coding agents
[D: CLAUDE.md:3]. A decision recorded there is reachable by whoever reads that file and by nobody
else, and it sits next to conventions, commands and lint rules, which are not decisions.

The repository also carries numeric claims in that same file that the code has since outgrown: it
states 19 routers where `mcpgateway/routers/` holds 30, and 16 middleware where
`mcpgateway/middleware/` holds 24 [D: CLAUDE.md:28]. Its own guardrail section warns against
exactly those claims [D: CLAUDE.md:559].

## Decision

Architecture decisions are recorded as ADRs in `docs/ContextForge-Specs/ADRs/`, one decision per
file, with Context stated as facts and Alternatives left explicitly empty when the reasoning was
not recovered [D: docs/ContextForge-Specs/ADRs/how-to-read.md:1].

ADR-0002 through ADR-0007 are the first six, each reconstructed from code for a decision whose
cost is visible and whose reasoning is not.

## Alternatives considered

OPEN: not recoverable. This record is itself reconstructed, and the repository retains no
discussion of whether ADRs were considered and rejected before now.

One observable alternative is in use: recording decisions as prose in `AGENTS.md`
[D: CLAUDE.md:429]. Whether that was chosen or simply happened is not stated.

## Consequences

A decision now has a place that is neither a comment nor a contributor's memory. Six decisions
already visible in the code have a record with an honest empty Alternatives section, which starts
the conversation rather than closing it.

The reconstructed records carry no rationale. They are worth less than a record written at the
time, and they say so in their own Status line rather than implying otherwise.

## Links

- `how-to-read.md` — naming and reading order for this directory
- `../architect/architect.md` § Decision index

## Open questions

- OPEN: should the decisions currently stated in `AGENTS.md` be moved here, or cross-referenced
  from here and left in place? Moving them breaks the agent guidance that depends on them.
- OPEN: who approves an ADR, and what makes one `accepted` rather than `proposed`?
- OPEN: which past decisions are worth reconstructing beyond the six recorded here?
