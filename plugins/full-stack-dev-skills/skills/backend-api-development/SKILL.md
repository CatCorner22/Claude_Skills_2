---
name: backend-api-development
description: >-
  Builds lean FastAPI backends — routing and dependency injection, Pydantic models as the
  single validation/serialization layer, thin routes over feature-module services, auth
  (session cookies vs JWT, chosen by client type), one error shape with correct status
  codes, pagination on every list endpoint, and the auto-generated OpenAPI schema as the
  API contract. Use when creating or extending a REST API, adding authentication, fixing
  validation or error-handling inconsistencies, or designing endpoints. Triggers: FastAPI,
  build an API, REST endpoint, add an endpoint, pydantic validation, API auth, JWT vs
  session, API error handling, HTTP status codes, pagination endpoint, OpenAPI schema,
  dependency injection fastapi, CRUD API.
metadata:
  version: "1.5.0"
---

# Backend API development (FastAPI)

## When to use
- Creating or extending a JSON API: endpoints, validation, auth, errors, pagination.
- Reviewing an API for consistency, security basics, or excess code.
- Not for: consuming someone else's API → see `data-tools-skills:rest-api-data-pulls`.
  Database modeling behind the endpoints → see `full-stack-dev-skills:database-and-orm`.
  Streaming/WebSocket endpoints → see `full-stack-dev-skills:realtime-and-dynamic-features`.
- Not for: whole-project Python rigor around the service — the 2026 toolchain (uv, Ruff,
  strict type checking), packaging/CI layout, and ship-ready hardening of an entire codebase
  → invoke the "Pythagoras" persona in `full-stack-dev-skills:elite-python-engineer`. This
  skill stays at the endpoint and contract level.

## Do it
1. **Let Pydantic models be the whole validation layer.** One request model and one response
   model per endpoint shape; FastAPI validates input, serializes output, and documents both —
   zero hand-written validation code:

```python
class InvoiceIn(BaseModel):
    customer_id: int
    amount: Decimal = Field(gt=0)
    due_date: date

@router.post("/invoices", response_model=InvoiceOut, status_code=201)
def create_invoice(data: InvoiceIn, db: Session = Depends(get_db)):
    return invoices.create(db, data)   # route stays thin; logic lives in the feature module
```

   `response_model` doubles as an output filter — fields not in the model never leak.
2. **Keep routes thin; put logic in the feature module.** A route function should parse
   (automatic), call one service function, and return. Business logic in routes can't be
   reused or tested without HTTP; the feature-folder layout
   (`full-stack-dev-skills:full-stack-app-architecture`) gives it a home.
3. **Use dependency injection for cross-cutting needs** — DB session, current user, settings
   — as `Depends()` functions. One `get_db`, one `get_current_user`; auth on a whole router
   via `dependencies=[Depends(require_user)]` instead of per-route copy-paste.
4. **Choose auth by client type, then use the boring version:**
   - Browser + server-rendered/htmx → **session cookie** (HttpOnly, Secure, SameSite=Lax);
     framework session middleware, no token plumbing.
   - SPA or third-party API clients → **JWT access token** (short-lived, ~15 min) +
     refresh flow, or an opaque token in a table if you want revocation without JWT caveats.
   - Never build password hashing yourself — `pwdlib[argon2]` (Argon2id;
     `PasswordHash.recommended()`). passlib's last release is 1.7.4, October 2020. Never put
     secrets in the JWT payload (it's readable, only *signed*).
5. **Make errors one shape everywhere.** Raise `HTTPException` (or a small domain exception
   mapped by one handler) so every error returns `{"detail": ...}` with the right status:
   422 validation (automatic), 401 unauthenticated, 403 forbidden, 404 absent, 409 conflict.
   `{"detail": ...}` is the default here because it is what FastAPI's own validation, routing,
   and `HTTPException` paths already emit — nothing has to be re-wrapped for the shape to hold.
   A custom envelope (`full-stack-dev-skills:elite-python-engineer` prefers
   `{"error": {"code", "message"}}` for its stable machine-readable code) is equally valid but
   only becomes "one shape" once the validation and `HTTPException` handlers are overridden too;
   pick one per service rather than one per route. Never return 200-with-error-body; never leak
   stack traces (a generic 500 handler logs the detail server-side).
6. **Paginate every list endpoint from day one** — `limit`/`offset` params with a maximum,
   returning `{"items": [...], "total": n}` (cursor pagination only when data shifts under
   pagination — see the consumer-side view in `data-tools-skills:rest-api-data-pulls`).
   Retro-fitting pagination onto clients later is the expensive version.
7. **Treat `/docs` (OpenAPI) as the contract.** The auto-generated schema *is* the API
   documentation — keep models/status codes accurate and frontend or agent consumers can
   generate clients from it. `references/fastapi-patterns.md` has the auth recipes, error
   handler, pagination helper, and the endpoint design checklist.

## Why / learn
The lean insight of FastAPI is that **types are the API**: one Pydantic model simultaneously
validates input, serializes output, filters leaks, and writes the documentation — four jobs
that older stacks did with four hand-maintained artifacts that drifted apart. Every pattern
in this skill extends that collapse-the-duplicates move: DI collapses per-route boilerplate
into one declared dependency; a single error shape collapses N client-side error parsers
into one; the OpenAPI contract collapses "the docs" and "the code" into the same file. The
auth guidance is about threat models, not fashion: cookies exist for browsers (automatic
sending is convenient *and* the CSRF risk — hence SameSite), JWTs exist for clients that
can hold a token (no CSRF, but revocation is hard because the token is self-contained —
hence short lifetimes). Choosing by client type resolves the debate in one line. And thin
routes matter because HTTP is your app's *edge*, not its body — logic that lives at the edge
can only be exercised through the edge, which makes tests slow and reuse impossible; logic
in plain functions is cheap to test and free to call from a CLI, a job, or tomorrow's second
endpoint.

## Common mistakes
- Hand validation inside routes (`if not data.get(...)`) → that's Pydantic's job; model it.
- Fat routes with business logic → thin route → service function; test the function, not HTTP.
- One shared dict/`**kwargs` for request bodies → typed models or you've disabled the framework.
- JWT for a same-site server-rendered app → session cookie is simpler and safer there.
- Long-lived JWTs to avoid a refresh flow → you've made logout/revocation impossible; short + refresh.
- 200 responses carrying `{"error": ...}` → clients must special-case; use status codes.
- Unpaginated lists "for now" → the 50k-row response arrives in production; limit/offset from day one.
- Stack traces or ORM errors in API responses → generic 500 + server-side log.
- Writing separate API docs → keep the OpenAPI schema honest; it's already the docs.

## Tailor to your environment
Record your API conventions in `references/your-environment.md`: auth choice per client,
error shape, pagination defaults/max, versioning policy if any, and naming conventions —
so every new endpoint (human- or agent-written) matches the house shape.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/backend-api-development.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/fastapi-patterns.md — auth recipes (sessions + JWT), error handler, pagination helper, endpoint checklist
- references/your-environment.md — your auth, conventions, limits (fill in)
