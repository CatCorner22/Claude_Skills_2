---
name: deploy-and-operate
description: >-
  Ships and runs full-stack apps the lean way — small multi-stage Docker images, a CI
  pipeline shaped lint → test → build → migrate → deploy, twelve-factor environment and
  secrets discipline, health endpoints, structured logging with request IDs, and the minimal
  observability that answers "is it up and what broke" — plus rollback as a first-class
  path. Use when containerizing an app, setting up CI/CD, wiring environments and secrets,
  adding health checks or logging, or designing the deploy/rollback flow. Triggers:
  dockerfile, deploy the app, CI/CD pipeline, github actions deploy, environment variables
  prod, secrets management app, health check endpoint, structured logging, rollback deploy,
  container image size, run migrations on deploy, observability basics.
---

# Deploy and operate

## When to use
- Containerizing an app, standing up CI/CD, or wiring environments, secrets, health checks,
  logging, and rollback for a full-stack service.
- Reviewing a deploy setup that is slow, flaky, or opaque when things break.
- Not for: which cloud/platform to buy — this skill's patterns are platform-agnostic
  (containers + env vars run anywhere). App architecture and config *design* →
  `full-stack-dev-skills:full-stack-app-architecture`. Long-lived connection infra concerns →
  `full-stack-dev-skills:realtime-and-dynamic-features`.

## Do it
1. **Build one small image with a multi-stage Dockerfile:**

```dockerfile
FROM python:3.12-slim AS deps
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM node:22-slim AS ui                # only if you have a Vite frontend
WORKDIR /ui
COPY frontend/package*.json .
RUN npm ci
COPY frontend/ .
RUN npm run build

FROM python:3.12-slim
WORKDIR /app
COPY --from=deps /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=deps /usr/local/bin /usr/local/bin
COPY app/ app/
COPY --from=ui /ui/dist app/static/   # FastAPI serves the built UI — one deployable
USER nobody
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

   Slim base, no build tools in the final stage, non-root user, dependencies cached in
   their own layer (rebuilds are seconds when only code changed).
2. **Shape CI as lint → test → build → deploy, failing fast and cheap first.** One workflow:
   ruff/type-check (seconds) → pytest with the real test DB (`full-stack-dev-skills:testing-strategy`)
   → build the image once, tag with the git SHA → deploy that exact artifact. The SHA tag is
   the whole versioning scheme: what runs in prod is a commit you can check out.
3. **Keep environments twelve-factor: same image, different env.** All differences arrive as
   environment variables into the one settings object
   (`full-stack-dev-skills:full-stack-app-architecture`); secrets come from the platform's
   secret store or CI secrets — never baked into images, never in git (the same rule as
   `data-tools-skills:data-file-hygiene`). If you can't run the prod image locally with a
   different env file, environments have drifted.
4. **Run migrations as a deploy step, not an app side effect:** `alembic upgrade head`
   before the new code serves traffic (a CI step or release phase). Combined with
   deploy-safe migration patterns (`full-stack-dev-skills:database-and-orm`), old and new
   code both tolerate the schema during the switchover.
5. **Expose health honestly:** `/healthz` (process up — for restarts) and `/readyz` (DB
   reachable, migrations current — for routing traffic). The platform restarts on the
   first and gates traffic on the second; deep dependency checks belong in `/readyz` only,
   so a flaky dependency doesn't crash-loop the process.
6. **Log structured lines to stdout with a request ID.** JSON (or key=value) per event,
   one request-ID middleware so every log line of a request correlates; log at the
   boundaries (request in/out, job start/end, external calls) with duration and status.
   The platform collects stdout — no log files, no rotation code.
7. **Make rollback boring and rehearsed:** deploy = point at image SHA, rollback = point at
   the previous SHA (plus `alembic downgrade` only if the migration wasn't additive —
   prefer additive so rollback is code-only). Keep the last-known-good SHA one command
   away. `references/deploy-recipes.md` has the CI workflow, compose file, logging
   middleware, and the go-live checklist.

## Why / learn
Deployment is a *reproducibility* problem wearing an infrastructure costume: every classic
failure — works-on-my-machine, staging-passed-prod-broke, can't-roll-back — is some
difference between what you tested and what you ran. The container answers "same code, same
runtime"; env-only configuration answers "same artifact, different environment"; the
SHA-tagged image answers "which exact thing is running"; and migrations-as-deploy-step
answer "code and schema move in lockstep." Once those four invariants hold, deploys stop
being events and become pointer updates — which is also why rollback becomes trivial: it's
the same pointer update, backwards. The health-check split exists because "alive" and
"ready" are different questions with different consumers (the restarter vs the router), and
conflating them turns a database blip into a restart storm. Structured logs with request
IDs are the minimum observability that pays: when something breaks, the question is always
"what happened to *this* request/job," and grep-able correlated events answer it without a
tracing platform. All of it is lean-code applied to operations — the fewest moving parts
that make "is it up, what broke, put it back" answerable in minutes.

## Common mistakes
- Fat single-stage images with build tools inside → slow pulls, big attack surface; multi-stage, slim, non-root.
- `latest` tags in prod → "what is running?" becomes archaeology; deploy git-SHA tags.
- Config baked into images or `if prod:` in code → one image, env-only differences.
- Secrets in git or Dockerfiles "temporarily" → history is forever; platform secret store + CI secrets.
- Migrations run by the app at import time → racing replicas and half-migrated crashes; explicit deploy step.
- One health endpoint doing deep checks → dependency blips cause restart storms; split healthz/readyz.
- Log files inside containers → lost on restart; structured stdout, platform collects.
- No request ID → every incident is log soup; one middleware line buys correlation.
- Rollback as an emergency improvisation → rehearse it; additive migrations keep it code-only.

## Tailor to your environment
Record your ops shape in `references/your-environment.md`: platform and deploy mechanism,
image registry and tagging, secret store, environment list, migration step location, health
endpoints wired to what, and the rollback runbook. **Never commit real secrets, hostnames
you consider sensitive, or tokens.**

## References
- references/deploy-recipes.md — CI workflow, compose file, logging middleware, go-live checklist
- references/your-environment.md — your platform, registry, secrets, runbook (fill in)
