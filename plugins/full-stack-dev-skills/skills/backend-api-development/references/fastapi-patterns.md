# FastAPI patterns (reference)

## Contents
- Session-cookie auth (server-rendered / htmx)
- JWT auth (SPA / API clients)
- One-shape error handling
- Pagination helper
- Endpoint design checklist

## Session-cookie auth (server-rendered / htmx)
```python
# Starlette's SessionMiddleware: signed cookie, no server-side store needed to start
app.add_middleware(SessionMiddleware, secret_key=settings.secret_key,
                   https_only=True, same_site="lax")

from pwdlib import PasswordHash
hasher = PasswordHash.recommended()   # Argon2id; build once at import, not per request.
                                      # Do NOT name it `pwd` — that shadows the stdlib module.

def require_user(request: Request, db: Session = Depends(get_db)) -> User:
    if uid := request.session.get("uid"):
        if user := db.get(User, uid):
            return user
    raise HTTPException(401)

@router.post("/login")
def login(data: LoginIn, request: Request, db: Session = Depends(get_db)):
    user = db.scalar(select(User).where(User.email == data.email))
    if not user or not hasher.verify(data.password, user.password_hash):
        raise HTTPException(401, "Invalid credentials")   # same message both cases
    request.session["uid"] = user.id
    return {"ok": True}
```
CSRF: SameSite=Lax covers most cases; add a CSRF token for state-changing cross-site forms.

## JWT auth (SPA / API clients)
```python
def make_token(uid: int) -> str:
    return jwt.encode({"sub": str(uid), "exp": now() + timedelta(minutes=15)},
                      settings.secret_key, algorithm="HS256")

def current_user(creds: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
                 db: Session = Depends(get_db)) -> User:
    try:
        payload = jwt.decode(creds.credentials, settings.secret_key, algorithms=["HS256"])
    except jwt.PyJWTError:
        raise HTTPException(401) from None
    user = db.get(User, int(payload["sub"]))
    if user is None:
        raise HTTPException(401)
    return user
```
Refresh: long-lived refresh token in an HttpOnly cookie or a DB table (revocable), exchanged
for short access tokens at `/refresh`. Password hashing: Argon2id via `pwdlib`
(`PasswordHash.recommended()`) — never custom, never passlib (unmaintained since 2020).

## One-shape error handling
```python
class DomainError(Exception):
    status = 400

@app.exception_handler(DomainError)
def domain_error(_, exc: DomainError):
    return JSONResponse({"detail": str(exc)}, status_code=exc.status)

@app.exception_handler(Exception)          # last resort: log detail, hide it
def unhandled(_, exc: Exception):
    log.exception("unhandled", exc_info=exc)   # exc_info=exc is load bearing — see below
    return JSONResponse({"detail": "Internal error"}, status_code=500)
```
Pass `exc_info=exc` explicitly: an exception handler is not running inside an `except` block, so
a bare `log.exception("unhandled")` records `NoneType: None` where the traceback should be — the
one thing the generic 500 handler exists to capture. Verified on FastAPI 0.141.

This keeps the `{"detail": ...}` **key** that FastAPI already uses for validation failures, raised
`HTTPException`s, and unrouted URLs — but be precise about what that does and does not buy you.
Only the key is consistent; the value type is not. Measured on FastAPI:

| Source | `detail` type | Value |
|---|---|---|
| 422 validation | **list** | `[{"type": "int_parsing", "loc": ["body","n"], "msg": …}, …]` |
| raised `HTTPException` | str | `"conflict"` |
| unrouted URL (404) | str | `"Not Found"` |

That matters because this plugin's own client (`frontend-recipes.md`) does
`detail = JSON.parse(body).detail ?? detail` and then `throw new ApiError(r.status, detail)`. On a
422 the thrown `detail` is an array. What the user actually sees is **`[object Object]`** — or,
in React, an "Objects are not valid as a React child" throw that takes the view down — not the
pydantic repr you would see in Python; JavaScript never produces that form. Either normalise in
the client (`Array.isArray(detail) ? detail.map(e => e.msg).join("; ") : detail`, which
`frontend-recipes.md`'s client now does) or override `RequestValidationError` so the server emits
one shape. If you prefer a coded envelope
(`full-stack-dev-skills:elite-python-engineer` shows `{"error": {"code", "message"}}`), those
three built-in paths keep emitting `{"detail": ...}` until you override
`RequestValidationError` and Starlette's `HTTPException` as well; that reference has both
handlers written out.

Status map: 400 bad request semantics · 401 who are you · 403 not yours · 404 absent
(also for "exists but you may not know that") · 409 conflict/duplicate · 422 shape invalid
(automatic).

## Pagination helper
```python
def paginate(db: Session, stmt, limit: int = 50, offset: int = 0, cap: int = 200) -> dict:
    limit = min(limit, cap)
    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    items = db.scalars(stmt.limit(limit).offset(offset)).all()
    return {"items": items, "total": total, "limit": limit, "offset": offset}
```
Cursor pagination (keyset: `WHERE id > :last ORDER BY id LIMIT n`) when rows shift under
offset paging or tables get large.

## Endpoint design checklist
- [ ] Request + response Pydantic models; `response_model` set (output filtered)
- [ ] Route thin: parse → one service call → return
- [ ] Auth dependency at router level unless truly public
- [ ] Errors raised, not returned; correct status codes
- [ ] List endpoints paginated with a cap
- [ ] Names: plural nouns (`/invoices/{id}`), verbs only for true actions (`/invoices/{id}/send`)
- [ ] Shows correctly in `/docs` — the contract is accurate
