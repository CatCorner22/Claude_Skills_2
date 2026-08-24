# The 2026 toolchain — mandatory stack and config templates

Contents:
1. The stack at a glance
2. uv commands
3. pyproject.toml template (single source of truth)
4. Type-checker config (ty / Pyright strict)
5. .pre-commit-config.yaml
6. GitHub Actions CI (uv-based)

Version floors below are refreshed at review time (last: 2026-08). Run
`uv pip list --outdated` — or `uv add <pkg>` and read what it pins — before pasting them into a
real project; a floor that predates the `target-version` in the same file fails on first run.

## 1. The stack at a glance

| Concern | Tool | Notes |
|---|---|---|
| Package / env / build | **uv** (Astral) | Replaces pip, venv, pip-tools, poetry, twine. Lockfile: `uv.lock`. |
| Lint + format + import sort | **Ruff** | Replaces black, isort, flake8. Configured in `pyproject.toml`. |
| Type checking | **Pyright** (strict) or **ty** | Pyright has one strict switch; ty has none — promote rules explicitly. Annotation *coverage* is Ruff's `ANN`, not the checker's. |
| Testing | **pytest** + **hypothesis** | Plus `pytest-cov`, `pytest-asyncio` where async. |
| Validation / settings | **Pydantic v2** | `model_config = ConfigDict(...)`; `pydantic-settings` for config. |
| Web / API | **FastAPI** (Litestar for ultra-high perf) | SQLModel / Tortoise-ORM / Prisma as fits. |
| DataFrames | **Polars** (DuckDB, pyarrow) | pandas only when the ecosystem forces it. |
| Logging / observability | **structlog** + OpenTelemetry | Strict JSON in prod; console renderer in dev. |
| Layout | `src/` layout | `py.typed` marker; `pyproject.toml` is the single source of truth. |
| Python | **3.14+** | Free-threading is officially supported (PEP 779) but ships as a SEPARATE build: `uv python install 3.14t`. The default `3.14` still holds the GIL. t-strings (PEP 750); deferred annotations (PEP 649). |

Never suggest pip, poetry, black, isort, flake8, or mypy unless the user explicitly forces
legacy tooling — and then show the migration path off them.

## 2. uv commands

```bash
uv init my-project --lib          # or --app; creates src/ layout + pyproject.toml
cd my-project
uv add fastapi pydantic structlog polars
uv add --dev pytest pytest-cov pytest-asyncio hypothesis ruff ty pre-commit
uv sync                            # resolve + install from uv.lock (creates it if absent)
uv run pytest                      # run anything inside the managed environment
uv run python -m my_project
uv build                           # sdist + wheel
uvx ruff check .                   # run a tool without installing it into the project
```

Commit `uv.lock`. CI installs with `uv sync --locked` so builds are reproducible.

## 3. pyproject.toml template

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "One-line description."
readme = "README.md"
requires-python = ">=3.14"
license = { text = "MIT" }
dependencies = [
    "fastapi>=0.141",
    "pydantic>=2.13",
    "pydantic-settings>=2.15",
    "structlog>=26.1",
    "polars>=1.43",
]

[dependency-groups]
dev = [
    "pytest>=9.1",
    "pytest-cov>=7.0",
    "pytest-asyncio>=1.4",
    "hypothesis>=6.165",
    "ruff>=0.16",          # earlier releases reject target-version = "py314"
    "ty",
    "pre-commit>=4.6",
]

[build-system]
requires = ["uv_build"]
build-backend = "uv_build"

[tool.ruff]
target-version = "py314"
line-length = 100
preview = true
src = ["src", "tests"]

[tool.ruff.lint]
select = [
    "E", "W",    # pycodestyle
    "F",         # pyflakes
    "I",         # isort
    "N",         # pep8-naming
    "UP",        # pyupgrade
    "B",         # bugbear
    "SIM",       # simplify
    "C4",        # comprehensions
    "PTH",       # pathlib everywhere
    "RUF",       # ruff-specific
    "S",         # bandit (security)
    "T20",       # no print()
    "ANN",       # annotations required
]
# Ruff 0.16 wants rule *names*, not codes, in ignore lists (codes still fine in `select`).
ignore = ["any-type"]  # ANN401: allow Any only where truly unavoidable — justify it

[tool.ruff.lint.per-file-ignores]
"tests/**" = ["assert"]  # S101: assert is the point of tests

[tool.pytest.ini_options]
addopts = "--cov=src --cov-report=term-missing --cov-fail-under=95 -q"
asyncio_mode = "auto"
testpaths = ["tests"]

[tool.coverage.run]
branch = true
source = ["src"]
```

Layout that goes with it:

```
my-project/
├── pyproject.toml
├── uv.lock
├── README.md
├── src/my_project/
│   ├── __init__.py        # __doc__, __version__
│   ├── py.typed
│   ├── exceptions.py      # domain exception hierarchy
│   ├── logging.py         # structlog configuration
│   └── __main__.py        # CLI entrypoint when applicable
└── tests/                 # mirrors src/
    └── test_*.py
```

## 4. Type-checker config

**Pyright is the default when a hard strict gate is claimed** — it has a single switch that
turns on the whole strict rule set, including "this parameter has no annotation":

```toml
[tool.pyright]
typeCheckingMode = "strict"
pythonVersion = "3.14"
enableExperimentalFeatures = true
include = ["src", "tests"]
```

ty is the fast-feedback checker, and it has **no top-level strict mode** —
`[tool.ty] strict = true` is rejected outright (`unknown field 'strict', expected one of
environment, src, rules, terminal, analysis, overrides`). Promote the checks you require, by
name, instead:

```toml
[tool.ty.environment]
python-version = "3.14"

[tool.ty.rules]
possibly-unresolved-reference = "error"
unresolved-attribute = "error"
missing-argument = "error"
unknown-argument = "error"
invalid-return-type = "error"
```

An unknown rule name is reported as `warning[unknown-rule]`, so a typo is visible rather than
silently inert — check the list after a ty upgrade.

Annotation *coverage* is enforced by neither: ty ignores a bare `def f(x): ...`, so the `ANN`
rules in the Ruff config above are what make "annotations on everything — public API, private
helpers, tests, scripts" a gate rather than an aspiration.

## 5. .pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.16.3
    hooks:
      - id: ruff-check    # lint (+ import sort); the bare `ruff` id is a legacy alias
        args: [--fix]
      - id: ruff-format   # format
  - repo: local
    hooks:
      - id: ty
        name: ty (rules promoted in [tool.ty.rules])
        entry: uv run ty check
        language: system
        pass_filenames: false
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-toml
```

Install with `uv run pre-commit install`.

## 6. GitHub Actions CI (uv-based)

```yaml
name: ci
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: astral-sh/setup-uv@v10.0.1   # no moving major tag past v7 — pin the release
        with:
          enable-cache: true
      - run: uv python install 3.14        # add 3.14t as well if you target free-threading
      - run: uv sync --locked
      - run: uv run ruff check .
      - run: uv run ruff format --check .
      - run: uv run ty check
      - run: uv run pytest
```
