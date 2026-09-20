#!/usr/bin/env python3
"""Rule config for v1.0.10 F-011.

Config only — the logic lives in route.py. Add paths to EXTRA as the feature's
document set grows, then re-run this file to regenerate the JSON.

    python rule_v1.0.10_F-011.py
"""
from route import build, emit

VERSION = "v1.0.10"
FEATURE_ID = "F-011"
FEATURE_TITLE = "Rust MCP Runtime"

EXTRA = {
    "domain": ["docs/ContextForge-Specs/ddd/domain_DOM-011-rust-mcp-runtime.md"],
    "adrs": ["docs/ContextForge-Specs/ADRs/adrs_ADR-0001-record-architecture-decisions.md"],
    "runbooks": ["docs/ContextForge-Specs/runbook/runbook_DEV_RB-001-local-setup.md"],
    "tests": ["docs/ContextForge-Specs/tests/test_v1.0.10_F-011.md"],
}

if __name__ == "__main__":
    emit(build(VERSION, FEATURE_ID, FEATURE_TITLE, EXTRA))
