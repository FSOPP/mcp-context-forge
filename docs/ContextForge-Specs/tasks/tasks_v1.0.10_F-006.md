---
title: Tasks v1.0.10 F-006 — LLM Gateway and Chat
id: F-006
status: as-built
owner: TBD
updated: 2026-09-20
---

# Tasks v1.0.10 F-006 — LLM Gateway and Chat

> **Inverted document.** These are not tasks to do; they are an inventory of shipped work, one row
> per unit that exists, each pointing at the artefact. The `done-when` column holds the check that
> *would* prove the row — which is what the status column then has to cash.

## Tasks

| ID | Task | Done when | Status | Artifact |
| --- | --- | --- | --- | --- |
| F-006-T1 | Serve `/chat/completions` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/llm_proxy_router.py:43] |
| F-006-T2 | Serve `/llm/gateway` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/llm_config_router.py:596] |
| F-006-T3 | Serve `/llm/models` — 6 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/llm_config_router.py:385] |
| F-006-T4 | Serve `/llm/providers` — 7 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/llm_config_router.py:110] |
| F-006-T5 | Serve `/llmchat/chat` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/llmchat_router.py:1287] |
| F-006-T6 | Serve `/llmchat/config` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/llmchat_router.py:1575] |
| F-006-T7 | Serve `/llmchat/connect` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/llmchat_router.py:1011] |
| F-006-T8 | Serve `/llmchat/disconnect` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/llmchat_router.py:1412] |
| F-006-T9 | Serve `/llmchat/gateway` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/llmchat_router.py:1636] |
| F-006-T10 | Serve `/llmchat/status` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/llmchat_router.py:1524] |
| F-006-T11 | Serve `/models` — 1 route decorators | the suite covering these paths passes here | done — make test: 23042 passed, 1 failed, 919 skipped, 0:44:51; the one failure is tests/unit/test_docker_entrypoint.py, outside this feature | [D: mcpgateway/routers/llm_proxy_router.py:133] |
| F-006-T12 | Persist `llm_providers` (20 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:6504] |
| F-006-T13 | Persist `llm_models` (16 columns) | a migration creates it and `alembic heads` shows one head | done — `alembic heads` ran here and printed one head, 5e211ec89cad, exit 0 | [D: mcpgateway/db.py:6587] |

## Implementation status

States and what `done` costs: `../status-model.md`. A row starts at `todo` and reaches `done` only
when its done-when check ran **here** and the note records the command and result.

## Open questions

- OPEN: what work on this feature is in flight but not yet in the tree? A working tree shows what
  landed, never what is half-finished elsewhere.
- OPEN: which of these rows were one change and which accumulated over many? The grouping is by
  surface, not by the history that produced it.
- OPEN: Which providers are supported in practice, and which are merely representable in `llm_providers`?
