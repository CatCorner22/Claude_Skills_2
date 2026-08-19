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
  container image size, run migrations on deploy, observability basics, containerize.
metadata:
  version: "1.3.0"
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
RUN python -m venv /opt/venv && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# only if you have a Vite frontend
FROM node:22-slim AS ui
WORKDIR /ui
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ .
RUN npm run build

FROM python:3.12-slim
WORKDIR /app
COPY --from=deps /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY app/ app/
# FastAPI serves the built UI — one deployable (drop this line and the `ui` stage if no frontend)
COPY --from=ui /ui/dist app/static/
USER nobody
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

   Slim base, no build tools in the final stage, non-root user, dependencies cached in
   their own layer (rebuilds are seconds when only code changed). Copy a **virtualenv**, not
   `site-packages`: the interpreter's install path embeds the minor version, so
   `COPY --from=deps /usr/local/lib/python3.12/site-packages …` repeats `3.12` in four places
   that must agree. Bump only the final `FROM` to 3.13 and the build still succeeds: the packages
   land in a `python3.12` directory a 3.13 interpreter never looks in, and the first thing anyone
   learns about it is `ModuleNotFoundError` from a container that pulled and started fine.
   `/opt/venv` leaves the two `FROM` tags as the only strings to keep in step, and drops the
   `/usr/local/bin` copy that was quietly mixing two images' console scripts.
   This is the pip/`requirements.txt` shape. On a project built to
   `full-stack-dev-skills:elite-python-engineer`'s toolchain there is no `requirements.txt` —
   swap the deps stage for `COPY pyproject.toml uv.lock ./` plus
   `ENV UV_PROJECT_ENVIRONMENT=/opt/venv` and `uv sync --locked --no-dev` (that variable is what
   puts the environment at `/opt/venv` instead of the project's `.venv`), and the CI
   `pip install` step for `uv sync --locked`. **`uv` is not in the `python:3.12-slim` base
   image** — the deps stage fails with `uv: not found` unless you put it there first, so add
   `COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv` (pin the tag in real use) to
   that stage, and install it in CI too. Everything downstream of the deps stage is unchanged.
2. **Shape CI as lint → test → build → migrate → deploy, failing fast and cheap first.** One
   workflow: ruff/type-check (seconds) → pytest with the real test DB
   (`full-stack-dev-skills:testing-strategy`) → build the image once, tag with the git SHA →
   `alembic upgrade head` against the target database (step 4) → deploy that exact artifact.
   The SHA tag is the whole versioning scheme: what runs in prod is a commit you can check out.
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

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/deploy-and-operate.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/deploy-recipes.md — CI workflow, compose file, logging middleware, go-live checklist
- references/your-environment.md — your platform, registry, secrets, runbook (fill in)
