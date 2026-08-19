# Deploy and operate recipes (reference)

## Contents
- CI workflow (GitHub Actions shape)
- docker-compose for dev
- Request-ID + logging middleware
- Go-live checklist

## CI workflow (GitHub Actions shape)
```yaml
name: ci
on: { push: { branches: [main] }, pull_request: {} }
jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with: { python-version: "3.12", cache: pip }
      - run: pip install -r requirements.txt -r requirements-dev.txt
      - run: ruff check . && ruff format --check .
      - run: alembic upgrade head          # migrations apply cleanly to a scratch DB
        env: { APP_DATABASE_URL: "sqlite:///./ci.db" }
      - run: pytest -q
        env: { TEST_DATABASE_URL: "sqlite:///./ci.db" }
  deploy:
    needs: checks
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    permissions: { contents: read, packages: write }   # packages: write is the GHCR push right
    env: { REGISTRY: "${{ vars.REGISTRY }}" }
    steps:
      - uses: actions/checkout@v7
      - uses: docker/login-action@v4        # without this the push fails: denied/unauthorized
        with:
          registry: ghcr.io                 # the host only — no /<org> path segment
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - run: docker build -t $REGISTRY/app:${{ github.sha }} .
      - run: docker push $REGISTRY/app:${{ github.sha }}
      - run: ./deploy.sh ${{ github.sha }}   # platform-specific: migrate, then point at the SHA
        env: { DEPLOY_TOKEN: "${{ secrets.DEPLOY_TOKEN }}" }
```
Set the repository variable `REGISTRY` to your image host (e.g. `ghcr.io/<org>`); `DEPLOY_TOKEN`
is a repository secret. Without the `env:` block `$REGISTRY` expands to nothing and the build
tags `/app:<sha>`, which Docker rejects. Note the quotes around every `${{ … }}` that sits inside
a `{ }` flow mapping: unquoted, the `{{` opens a nested mapping and GitHub rejects the whole file
as invalid YAML.

**The login step is not optional and its absence does not look like an auth problem.** A fresh
runner holds no credentials for any registry, so `docker push` fails with `denied` /
`unauthorized` *after* the build has already run — minutes of green pipeline followed by a
message that reads like a permissions bug in the registry. For GHCR the built-in `GITHUB_TOKEN`
suffices once the job declares `packages: write` (job-level `permissions:` replaces the
repository default wholesale, which is why `contents: read` is listed alongside it — omit it and
`actions/checkout` loses its read right). For Docker Hub, ECR, or a private registry, swap in
that registry's host and a pair of repository secrets.

The two `env:` names are deliberate and must match the code that reads them: `APP_DATABASE_URL`
is the `env_prefix = "APP_"` settings object from
`full-stack-dev-skills:full-stack-app-architecture`, and `TEST_DATABASE_URL` is what the conftest
spine in `full-stack-dev-skills:testing-strategy` reads. A name nothing reads is the worst
outcome here — the step passes while silently exercising the default database, so the
migration check proves nothing.

Fail-fast order: lint (seconds), then the scratch-DB migration check, then tests — all before
anything is built. The image is built once and the SHA is the release name; `./deploy.sh` runs
`alembic upgrade head` against the target database before pointing traffic at the new SHA.

## docker-compose for dev
```yaml
services:
  app:
    build: .
    ports: ["8000:8000"]
    env_file: .env               # git-ignored
    volumes: ["./app:/app/app"]  # live-reload in dev
    command: uvicorn app.main:app --host 0.0.0.0 --reload
  db:                            # only once you've moved past SQLite
    image: postgres:17
    environment: { POSTGRES_PASSWORD: dev }
    volumes: ["pgdata:/var/lib/postgresql/data"]
volumes: { pgdata: {} }
```

## Request-ID + logging middleware
```python
@app.middleware("http")
async def request_context(request: Request, call_next):
    rid = request.headers.get("x-request-id", uuid4().hex[:12])
    request.state.request_id = rid          # handlers and services read it from here
    start = time.perf_counter()
    status = 500                            # what gets logged if call_next raises
    try:
        response = await call_next(request)
        status = response.status_code
    finally:                                # finally, not else — see below
        log.info("request", extra={"rid": rid, "method": request.method,
                 "path": request.url.path, "status": status,
                 "ms": round((time.perf_counter() - start) * 1000)})
    response.headers["x-request-id"] = rid
    return response
```
**The `try/finally` is the whole point of the middleware.** Written as a bare
`response = await call_next(request)` followed by the log line, an unhandled exception skips
both the log call and the header — so the one request class you most need correlated, the 500,
is the one that leaves no trace. Verified on FastAPI 0.141: a route raising `ValueError`
produced a 500 response with **no** log line and **no** `x-request-id` header, while a 200 on the
same app logged normally.

The 500 response itself still cannot carry the header: Starlette's `ServerErrorMiddleware` sits
*outside* your `@app.middleware("http")` stack, so it builds that response where you can no
longer touch it. Correlate through the logged line instead — which is exactly why the log must
run in `finally`, and why the generic 500 handler should log `rid` (read it back off
`request.state.request_id`) next to the traceback.

Configure logging once (JSON formatter to stdout). Log boundaries: requests (above), job
start/end with the job id, and external calls with duration + status. Pass `rid` into
service logs for full correlation.

## Go-live checklist
- [ ] Image: multi-stage, slim, non-root, SHA-tagged; `docker run` works locally with a prod-shaped env file
- [ ] CI green: lint, migrations-apply, tests; deploy only from main
- [ ] Secrets in the platform store; none in git/image history
- [ ] `alembic upgrade head` wired as the pre-traffic deploy step
- [ ] `/healthz` (liveness) and `/readyz` (DB + migration check) wired to the platform
- [ ] Structured logs visible in the platform; request ID present end-to-end
- [ ] Error alerting: 5xx rate and job failures notify someone
- [ ] Rollback rehearsed once: previous SHA redeploys in minutes; last-known-good recorded
- [ ] Backups running if Postgres (the day-one ops cost of leaving SQLite)
- [ ] Stream endpoints (SSE/WS) have proxy buffering/timeout config if used
