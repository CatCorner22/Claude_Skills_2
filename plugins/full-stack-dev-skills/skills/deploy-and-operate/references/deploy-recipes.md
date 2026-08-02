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
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12", cache: pip }
      - run: pip install -r requirements.txt -r requirements-dev.txt
      - run: ruff check . && ruff format --check .
      - run: alembic upgrade head          # migrations apply cleanly to a scratch DB
        env: { DB_URL: "sqlite:///./ci.db" }
      - run: pytest -q
        env: { DB_URL: "sqlite:///./ci.db" }
  deploy:
    needs: checks
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: docker build -t $REGISTRY/app:${{ github.sha }} .
      - run: docker push $REGISTRY/app:${{ github.sha }}
      - run: ./deploy.sh ${{ github.sha }}   # platform-specific: run migrations, then point at the SHA
        env: { DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }} }
```
Fail-fast order (lint before tests before build); the image is built once and the SHA is
the release name.

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
    start = time.perf_counter()
    response = await call_next(request)
    log.info("request", extra={"rid": rid, "method": request.method,
             "path": request.url.path, "status": response.status_code,
             "ms": round((time.perf_counter() - start) * 1000)})
    response.headers["x-request-id"] = rid
    return response
```
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
