---
title: Release Plan — ContextForge
status: as-built
owner: TBD
updated: 2026-09-20
---

# Release Plan — ContextForge

> Reversed. What exists is a version number and a pipeline; a plan is a statement about the
> future and is not in the tree.

## Current release

`1.0.10`, carried identically by the Python package [D: pyproject.toml:54] and the Helm chart
[D: charts/mcp-stack/Chart.yaml:25].

The repository has 3213 commits, 44 contributors and **no tags**.

I: releases are cut somewhere other than this repository's tags — basis: a published version
number exists in two manifests while the tag list is empty [D: pyproject.toml:54].

## Pipeline

29 GitHub Actions workflows, including multi-platform image builds and image scanning
[D: .github/workflows/docker-multiplatform.yml:1].

## Compatibility commitments

The unversioned API shim carries `Sunset`, `Deprecation`, `Link` and `X-Deprecated-Endpoint`
headers [D: mcpgateway/middleware/deprecation.py:154]. The sunset date is supplied by whoever
constructs the middleware rather than fixed in the source
[D: mcpgateway/middleware/deprecation.py:154].

OPEN: what is the actual sunset date for this release, and has it been communicated?

## Open questions

- OPEN: what is the release cadence, and what triggers a release?
- OPEN: what is the support window for `1.0.x`?
- OPEN: are the chart version and the application version required to move together?
- OPEN: how is a release cut, given there are no tags here?
