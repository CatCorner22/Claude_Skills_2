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
metadata:
  version: "1.1.0"
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
   split along that proven seam, not a guessed one. Four signals actually count (measured resource
   divergence, a counted cadence conflict, ownership that already matches the code, a stateable
   containment requirement); five common ones only look like they do — "too big to understand",
   slow tests, scary deploys, a team wanting autonomy, and "we might need to scale". Each imposter
   has a cheaper fix; the reference names it.
3. **Lay out the project by feature, not by layer:**

```
app/
├── main.py            # FastAPI app, router mounting — the only "framework" file
├── config.py          # settings from env (one Pydantic Settings class)
├── db.py              # engine/session setup, one place — no models
├── platform/          # code that outlives every feature (email transport, error shape)
├── features/
│   ├── invoices/      # __init__.py (public surface), routes, models, rules, service, tests/
│   └── users/
└── frontend/          # Vite app (or templates/ for htmx)
migrations/            # one Alembic history — the DB is shared even when the code isn't
tests/                 # only tests that cross features
```

   A feature folder holds its routes, models, logic, and tests together — the code that
   changes together lives together, and deleting a feature is deleting a folder. Two boundaries
   inside it earn their keep: `platform/` holds what would still make sense if every feature were
   deleted, and `rules.py` holds pure domain functions (no DB, no clock) so the arithmetic is
   testable without a database. The reference gives the full tree with the test for each boundary.
4. **Keep module boundaries honest.** Features talk to each other through small, explicit
   functions (a `users.get_user(id)` call), never by reaching into each other's tables or
   internals. State it as one rule — *a feature may import another feature's public surface and
   nothing else* — and enforce it with a test, because a boundary rule nobody checks is a
   preference; the reference carries a 20-line pytest that walks the imports. That discipline is
   what keeps the "split it out later" option real — a service boundary is just a module boundary
   that grew up.
5. **Handle config the twelve-factor way.** All environment differences (DB URL, secrets,
   feature toggles) come from **environment variables**, read once at startup into a single
   typed settings object (`pydantic-settings`). No `if ENV == "prod"` scattered through code;
   no secrets in git (`.env` is git-ignored — same rule as this repo's own hygiene, see
   `data-tools-skills:data-file-hygiene`). Two rules make it real rather than nominal: secrets get
   **no default**, so an empty environment fails at boot instead of running on the dev key; and
   config is only what varies *between deploys of the same code* — anything that varies per
   customer or tenant is data and belongs in the database. `grep -rn "os.environ" app/` should
   return nothing outside `config.py` — and once `pydantic-settings` is doing the reading, usually
   nothing at all.
6. **Decide the rendering split deliberately.** JSON API + React when the frontend is a real
   application (heavy interactivity, offline-ish state); server-rendered + htmx when it's
   CRUD screens (one language, no build pipeline for the UI, far fewer lines). Mixing is
   fine: htmx pages with one React island where interactivity concentrates.
7. **Write the architecture down in one page** — stack, layout, boundaries, config, and the
   split criteria you'll honor later — using `references/architecture-decisions.md` as the
   template. One page is a constraint, not a target: a longer doc is not read, and an unread
   architecture doc is worse than none because it gets cited as authority. Each split criterion
   must name a measurement, a threshold, and where the number comes from; "when we need to scale"
   is not a criterion. The reference's deliverable contract gives the "done when" test per item.

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
- Defaulting to a React SPA for CRUD forms → htmx/server-rendered is usually far less code; choose per UI reality.
- Architecture doc as a wiki novel → one page: stack, layout, boundaries, split criteria.
- A `shared/` folder that only ever grows → it is layer-first returning under a new name; every line in it is a line no feature can delete. Watch the platform-to-features ratio's direction.
- Env var for something that differs per customer → that is data; it belongs in a table, and you'll find out when someone asks for a second customer's value.
- Splitting because tests or deploys are slow → those are test and pipeline problems; a split multiplies both while adding contract tests you didn't have.
- A boundary rule stated in the doc but not tested → it decays silently; the first violation is found in review, the tenth is not.

## Tailor to your environment
Capture your app's decisions in `references/your-environment.md`: chosen stack and why, the
layout, module boundaries and their interfaces, config/secrets handling, and your recorded
split criteria — so future changes (and agents) follow the same shape.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/full-stack-app-architecture.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/architecture-decisions.md — the reference tree with the test for each boundary; the
  import-rule pytest; a "where does this code go" feature carried end to end with its change
  manifest; the four split signals and the five imposters; failure envelopes for monolith-first,
  feature-first, and twelve-factor; config as code; the layer-first migration ratchet; the stack
  decision table; the deliverable contract for the one-page doc
- references/your-environment.md — your stack, layout, boundaries, criteria (fill in)
