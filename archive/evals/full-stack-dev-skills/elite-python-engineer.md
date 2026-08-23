# Evals — full-stack-dev-skills:elite-python-engineer

## 1. Positive trigger (should load the skill)
> "Build a production-ready webhook ingestion service in Python — set the project up from
> scratch, typed and tested, with proper logging we can audit later. Use modern tooling."

Expected: skill loads; Pythagoras persona; restates requirements + assumptions; complete
`pyproject.toml` (uv, Ruff py314/line-100/preview, strict ty/Pyright, pytest config) with
`src/` layout and `py.typed`; full implementation with 100% type annotations, domain
exception hierarchy + one JSON error shape, structlog JSON config with bound request
context; pytest + hypothesis tests mirroring `src/`; README/`uv run` usage; pre-commit +
CI snippet; next-steps section. No partial code.

## 2. Near-miss (should NOT load this skill)
> "Write me a quick Python script that reads this CSV of bank transactions and totals them
> by month — just something I can run once for the analysis."

Expected: analyst-grade one-off → `coding-agent-skills:python-for-analysts`. If this skill
loads and delivers a full src/-layout project with CI for a throwaway script, sharpen the
production-vs-analysis boundary in both descriptions.

## 3. Quality rubric
A good response:
- **Does the task:** complete, runnable code plus its toolchain (pyproject.toml, configs,
  tests, docs) in one delivery; `uv` commands shown; checklist satisfied.
- **Teaches:** why uv/Ruff/ty replace the legacy pile (speed → sustainable strictness),
  why domain exceptions + one error shape make failure a designed output, why bound
  structlog context turns audits into filters, async-vs-free-threading by workload.
- **Safe/modern:** no pip/poetry/black/mypy suggestions, no bare `except:`, no `print()`
  logging, no `Any` without justification, no secrets or PII in logs or configs.
