---
name: full-stack-app-architecture
description: >-
  Chooses and structures a full-stack application the lean way — picking the stack (default:
  FastAPI + React/Vite or htmx, SQLite-first), monolith-first project layout, module
  boundaries that follow features not layers, twelve-factor config/env handling, and the
  criteria for when (rarely, late) to split services. Use when starting an app, restructuring
  a project, choosing between monolith and services, or deciding where new code should live.
  Triggers: app architecture, project structure, monolith vs microservices, choose the stack,
  folder layout, where should this code live, new web app setup, scaffold project, module
  boundaries, config management app.
---

# Full-stack application architecture

## When to use
- Starting a new full-stack app: stack choice, repo layout, config strategy.
- Restructuring an existing project, or deciding where a new feature's code belongs.
- Evaluating a split into services (or arguing against one).
- Not for: line-level code style → see `full-stack-dev-skills:lean-code-principles`. Each
  layer's craft → the dedicated backend/database/frontend skills in this plugin.

## Do it
1. **Default the stack; deviate only on a real constraint.** Reference stack: **Python +
   FastAPI** (typed, async, OpenAPI built in), **React + Vite** for app-like UIs or **htmx +
   server templates** when the UI is mostly forms/tables (dramatically less code), **SQLite
   first, Postgres when deployment demands it** (see
   `full-stack-dev-skills:database-and-orm`). A stack you know beats a stack that benchmarks
   well; the lean rule is fewer moving pieces.
2. **Start as a monolith — one deployable, one database.** A modular monolith serves almost
   every app until well past product-market fit. Split a service out only when a boundary has
   *proven* different scaling, different release cadence, or a different team owning it — and
   split along that proven seam, not a guessed one.
3. **Lay out the project by feature, not by layer:**

```
app/
├── main.py            # FastAPI app, router mounting — the only "framework" file
├── config.py          # settings from env (one Pydantic Settings class)
├── db.py              # engine/session setup, one place
├── features/
│   ├── invoices/      # routes.py, models.py, service.py, tests/
│   └── users/
└── frontend/          # Vite app (or templates/ for htmx)
```

   A feature folder holds its routes, models, logic, and tests together — the code that
   changes together lives together, and deleting a feature is deleting a folder.
4. **Keep module boundaries honest.** Features talk to each other through small, explicit
   functions (a `users.get_user(id)` call), never by reaching into each other's tables or
   internals. That discipline is what keeps the "split it out later" option real — a service
   boundary is just a module boundary that grew up.
5. **Handle config the twelve-factor way.** All environment differences (DB URL, secrets,
   feature toggles) come from **environment variables**, read once at startup into a single
   typed settings object (`pydantic-settings`). No `if ENV == "prod"` scattered through code;
   no secrets in git (`.env` is git-ignored — same rule as this repo's own hygiene, see
   `data-tools-skills:data-file-hygiene`).
6. **Decide the rendering split deliberately.** JSON API + React when the frontend is a real
   application (heavy interactivity, offline-ish state); server-rendered + htmx when it's
   CRUD screens (one language, no build pipeline for the UI, far fewer lines). Mixing is
   fine: htmx pages with one React island where interactivity concentrates.
7. **Write the architecture down in one page** — stack, layout, boundaries, config, and the
   split criteria you'll honor later — using `references/architecture-decisions.md` as the
   template (it includes the service-split checklist and the stack decision table).

## Why / learn
Architecture is deciding *what changes together* — and most early architectural failure comes
from optimizing for imagined scale instead of for change. The monolith-first rule is
empirical: successful systems that started as microservices are rare, because service
boundaries drawn before the domain is understood are guesses, and a wrong service boundary
costs network calls, distributed debugging, and deployment orchestration *forever* — while a
wrong module boundary costs a refactor. Feature-folder layout follows the same logic at file
scale: layer-first layout (`routes/`, `models/`, `services/`) scatters every feature across
the tree, so every change touches four directories; feature-first layout makes the common
operation (change one feature) local and the rare operation (change all routes) global —
which matches reality. The twelve-factor config rule is about making the same artifact run
everywhere: the moment behavior depends on scattered environment checks, you have multiple
programs pretending to be one, and staging stops predicting production. And the honest-
boundaries rule is the option premium you pay to keep futures open: modules that communicate
through narrow interfaces can be split, scaled, or rewritten independently later — you're not
building microservices, you're preserving the *right* to.

## Common mistakes
- Choosing the stack by hype benchmark → fewer moving pieces you know beats novel pieces you don't.
- Microservices at day one → guessed boundaries, distributed-system tax with no scale to justify it; modular monolith.
- Layer-first folders → every feature change touches the whole tree; organize by feature.
- Features importing each other's models/tables directly → boundaries rot, split option dies; narrow explicit interfaces.
- Config sprinkled as `os.environ` reads and env checks → one typed settings object, read at startup.
- Secrets in the repo "temporarily" → git history is forever; env vars + git-ignored `.env`.
- Defaulting to a React SPA for CRUD forms → htmx/server-rendered is often 5x less code; choose per UI reality.
- Architecture doc as a wiki novel → one page: stack, layout, boundaries, split criteria.

## Tailor to your environment
Capture your app's decisions in `references/your-environment.md`: chosen stack and why, the
layout, module boundaries and their interfaces, config/secrets handling, and your recorded
split criteria — so future changes (and agents) follow the same shape.

## References
- references/architecture-decisions.md — one-page architecture template, stack decision table, service-split checklist
- references/your-environment.md — your stack, layout, boundaries, criteria (fill in)
