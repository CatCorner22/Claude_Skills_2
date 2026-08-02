# Architecture decision templates (reference)

## Contents
- One-page architecture doc template
- Stack decision table
- Service-split checklist
- Rendering-split decision

## One-page architecture doc template
```markdown
# <App> architecture (as of YYYY-MM)
Stack: <backend / frontend / db / hosting> — chosen because <one line each>
Layout: feature folders under app/features/; frontend in <frontend/ | templates/>
Boundaries: features communicate via <module functions>; no cross-feature table access
Config: env vars → pydantic-settings; secrets via <mechanism>; .env git-ignored
Data: SQLite in dev; <SQLite | Postgres> in prod; migrations via Alembic
Auth: <sessions | JWT> (see backend-api-development)
Split criteria we will honor: different scaling proven by metrics, different release cadence,
or separate team ownership — otherwise it stays in the monolith.
```

## Stack decision table
| Situation | Lean default | Consider instead when |
|---|---|---|
| API backend | FastAPI | Team is deeply invested elsewhere (Express/Rails/Django) |
| UI: app-like, heavy interactivity | React + Vite | Svelte/Vue if team knows them — parity |
| UI: forms, tables, CRUD | htmx + Jinja templates | React if interactivity will provably grow |
| Database | SQLite → Postgres | Postgres day one if multi-writer/hosted from the start |
| Background jobs | In-process (FastAPI BackgroundTasks / APScheduler) | Redis + worker (arq/Celery) when jobs outlive requests or need retries |
| Cache | None, then functools/DB | Redis when measurements demand it |
| Auth | Session cookies (server-rendered) / JWT (SPA + API) | An identity provider when SSO/enterprise appears |

## Service-split checklist (all should be true before splitting)
- [ ] A measured scaling difference (this module needs 10x the compute/memory of the rest)
- [ ] OR a proven release-cadence conflict (deploys of A regularly blocked by B)
- [ ] OR separate team ownership with real coordination cost
- [ ] The boundary already exists as a clean module interface (no shared tables)
- [ ] You can state the new operational cost (deploys, monitoring, versioned API) and accept it
Guessed future scale is not on the list.

## Rendering-split decision
- Mostly reading/writing records, few client-side state needs → server-rendered + htmx
  (one deployable, no JS build, ~5x less UI code).
- Rich client state (editors, dashboards with live interactions, offline) → React SPA + JSON API.
- Hybrid: server-rendered app with a React island mounted only on the complex page.
Revisit when the UI's nature changes — not because a framework released a major version.
