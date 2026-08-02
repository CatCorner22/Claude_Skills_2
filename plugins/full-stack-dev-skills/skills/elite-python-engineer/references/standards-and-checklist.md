# Engineering standards, patterns, and the pre-delivery checklist

Contents:
1. The ten core principles
2. Deterministic error handling (pattern)
3. Audit-ready structured logging (pattern)
4. Pre-delivery checklist
5. Special modes (review, legacy migration, performance, CLI, data/ML)

## 1. The ten core principles

1. **Readability and the Zen of Python** — PEP 20 is the baseline. Code must be obvious,
   explicit, and pleasant to read.
2. **Strict typing everywhere** — 100% annotation coverage including private helpers,
   tests, and scripts; `typing` + `typing_extensions`, deferred annotations (PEP 649).
   `Any` only when genuinely unavoidable, with a comment justifying it.
3. **Modern syntax** — Python 3.14+ features on purpose: t-strings (PEP 750) for safe,
   validated interpolation; pattern matching; `pathlib` exclusively; dataclasses or
   Pydantic over bare classes; free-threading awareness when choosing concurrency.
4. **Deterministic error handling** — domain-specific exception classes; no bare
   `except:`; predictable JSON error payloads with correct HTTP status codes; fail loudly
   and predictably rather than silently; `contextlib`/`contextvars` for structured error
   context.
5. **Audit-ready structured logging** — structlog exclusively; machine-readable JSON in
   production; context (request ID, transaction reference, user ID) bound at operation
   start; never `print()` for system events.
6. **Pure functions, small modules** — functional style where sensible; one
   responsibility per function, class, and module.
7. **Security and performance first** — Pydantic validation on all external input, rate
   limiting, sensitive-data redaction in logs, memory/profile awareness, async only when
   I/O-bound.
8. **Documentation** — Google-style docstrings (NumPy style for scientific code);
   module-level `__doc__` and `__version__` always.
9. **Testing** — unit + integration + property-based (hypothesis); ≥95% coverage;
   `tests/` mirrors `src/`.
10. **CI/CD ready** — every code delivery includes `pyproject.toml`, Ruff config,
    `.pre-commit-config.yaml`, a CI snippet, and `uv.lock` guidance.

## 2. Deterministic error handling (pattern)

```python
"""Domain exceptions: one hierarchy, one API error shape."""

class AppError(Exception):
    """Base for all domain errors; carries a stable machine-readable code."""

    code: str = "app_error"
    status: int = 500

class ConfigurationError(AppError):
    code = "configuration_error"
    status = 500

class PaymentNotFoundError(AppError):
    code = "payment_not_found"
    status = 404
```

FastAPI: map the hierarchy once, so every error is the same shape.

```python
@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    log.warning("request_failed", code=exc.code, path=request.url.path)
    return JSONResponse(
        status_code=exc.status,
        content={"error": {"code": exc.code, "message": str(exc)}},
    )
```

Rules: catch the narrowest exception you can act on; re-raise with context
(`raise DomainError(...) from exc`); never return 200 with an error body; never leak stack
traces to clients (generic 500 handler logs the detail server-side).

## 3. Audit-ready structured logging (pattern)

```python
"""structlog: JSON in production, pretty console in development."""
import logging
import structlog

def configure_logging(*, dev: bool = False) -> None:
    processors: list[structlog.typing.Processor] = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]
    renderer = (
        structlog.dev.ConsoleRenderer() if dev else structlog.processors.JSONRenderer()
    )
    structlog.configure(
        processors=[*processors, renderer],
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        cache_logger_on_first_use=True,
    )
```

Bind context at the start of each operation so every subsequent event carries it:

```python
log = structlog.get_logger()

async def handle_transfer(request_id: str, user_id: str, ref: str) -> None:
    structlog.contextvars.bind_contextvars(
        request_id=request_id, user_id=user_id, transaction_ref=ref
    )
    log.info("transfer_started")
    ...
    log.info("transfer_completed", amount_cents=amount)
```

Redact secrets/PII with a processor before the renderer — tokens, passwords, and account
numbers must never reach the sink. Wire OpenTelemetry trace IDs into the same context.

## 4. Pre-delivery checklist

Verify every delivery before sending:

- [ ] Ruff-compliant (line-length 100, preview rules enabled)
- [ ] 100% type coverage; ty/Pyright strict passes
- [ ] Google docstrings + type hints on everything (module `__doc__`, `__version__`)
- [ ] `uv` commands shown for setup
- [ ] `src/` layout with proper `__init__.py` and `py.typed`
- [ ] Async where I/O-bound, sync/free-threaded where CPU-bound (note the trade-off)
- [ ] structlog JSON configured; context bound to loggers
- [ ] Custom domain exceptions defined and handled deterministically
- [ ] No global state; dependency injection via FastAPI `Depends` or explicit context
- [ ] Pydantic models for all external data
- [ ] hypothesis or edge-case tests included; coverage target ≥95%
- [ ] No partial code, no deprecated tools, no `print()` logging

## 5. Special modes

- **Code review / refactor** — point out every violation of these standards (especially
  missing structured logging and sloppy exception handling), explain why each matters,
  then deliver the fully rewritten version.
- **Legacy migration** — incremental, safe order: (1) `uv init` + import existing
  requirements with `uv add -r requirements.txt`; (2) swap black/isort/flake8 for Ruff and
  auto-fix; (3) turn on ty/Pyright per-module and annotate outward from the core;
  (4) introduce structlog behind the existing logging facade, then flip the renderer to
  JSON; (5) add pre-commit + CI last so the gates lock in the gains.
- **Performance-critical** — measure first; discuss free-threading vs multiprocessing,
  GIL release points in extensions, and Polars vs pandas (lazy evaluation, zero-copy
  Arrow). Prefer algorithmic wins before parallelism.
- **CLI tools** — Typer + Rich; structlog console renderer in dev, JSON in prod;
  `__main__.py` entrypoint and a `[project.scripts]` entry.
- **Data science / ML** — Polars + scikit-learn or JAX/Torch with full typing; keep
  notebooks thin wrappers over typed `src/` functions so the library stays testable.
