# Full-stack engineering standards (standard work for the codebase)

The "advanced but well-accepted" bar: practices with a decade of industry consensus behind
them, applied as **standard work** — the documented best-known method, followed until a
measured improvement replaces it. Depth per layer lives in `full-stack-dev-skills` (linked
throughout); this file is the standard itself.

Contents: §1 Principles · §2 Backend · §3 Frontend · §4 Data layer · §5 API contracts ·
§6 Pipeline & operations · §7 Observability · §8 Security baseline · §9 Definition of Done

## §1 Principles

- **Boring on purpose.** Choose the technology a competent stranger can maintain: proven
  frameworks, one obvious way per concern, no resume-driven architecture. Advanced ≠ exotic;
  advanced = disciplined use of well-accepted tools.
- **Lean code.** Stdlib → framework → well-maintained library → own code, YAGNI, small public
  surface, earn every abstraction (→ `full-stack-dev-skills:lean-code-principles`).
- **Types are poka-yoke.** Strict typing at every boundary — illegal states unrepresentable
  beats illegal states documented.
- **Jidoka pipeline.** Every quality rule that matters is a *blocking automated check*; humans
  review for design, not for what a linter can catch.
- **Single golden path.** New service/page/module starts from the template with logging, auth,
  tests, and CI wired. Deviation is allowed with a written reason (ADR) — that's kaizen input,
  not rebellion.

## §2 Backend

- Python 3.12+ · **FastAPI** (async, DI, automatic OpenAPI) · **Pydantic v2** models at every
  boundary — request, response, settings (`BaseSettings`), and external payloads. No naked
  dicts across layers (→ `full-stack-dev-skills:backend-api-development`,
  `full-stack-dev-skills:elite-python-engineer`).
- Toolchain: **uv** (envs/locking, `pyproject.toml`, `src/` layout), **Ruff** (lint+format),
  strict type checking (Pyright strict; Astral's ty once it exits beta), **pytest**
  (+ `pytest-asyncio`, coverage on critical paths, **Hypothesis** for the algorithmic core —
  see `adversarial-testing.md`).
- Layering, hexagonal-lite: routes → services (domain logic, framework-free) → repositories
  (persistence). Domain logic testable without HTTP or DB. Don't ceremony this into DDD
  cosplay for a CRUD app — layers earn their keep at the seams that change.
- Errors: typed exception hierarchy at the domain layer; one exception handler translating to
  RFC 9457 problem-details responses; never leak stack traces or SQL to clients.
- 12-factor: config from environment; stateless processes; logs to stdout as structured JSON.

## §3 Frontend

- **TypeScript strict mode** — `any` is a code-review finding. React (or the house framework)
  with server state in **TanStack Query** (caching, retries, invalidation) and UI state kept
  local; global stores only for genuinely global concerns
  (→ `full-stack-dev-skills:frontend-modern-ui`).
- Components: accessible primitives (Radix/shadcn-style headless + your design tokens) rather
  than hand-rolled dropdowns/dialogs/comboboxes — accessibility comes largely free and tested
  (see `accessible-ui-design-system.md`).
- Forms: schema-validated (zod or equivalent) with the *same* validation contract the API
  enforces — one source of truth, mirrored, never divergent.
- Every async view designs its four states up front: loading (skeleton), error (with retry),
  empty (with next action), success. The unhappy paths are the product too.
- Performance budget in CI: route-level code splitting, image discipline, Core Web Vitals
  budget enforced by the pipeline, not by hope.

## §4 Data layer

- Relational default: **PostgreSQL**. Schema as versioned migrations (Alembic or house tool);
  never hand-edit a live schema; every migration has a rollback path and is rehearsed against
  a production-shaped copy (→ `full-stack-dev-skills:database-and-orm`).
- Constraints are poka-yoke: NOT NULL, UNIQUE, FK, CHECK at the database — the app validates
  for UX; the database *enforces* for truth.
- SQLAlchemy 2.0 style (async where the stack is async); repository layer owns queries; no ORM
  calls scattered through route handlers.
- Reference-bearing identifiers (invoice numbers, account numbers, chart numbers) are TEXT,
  never numeric floats — leading zeros are data (a lesson this library enforces everywhere).
- Money is integer minor units or NUMERIC — never binary floats.

## §5 API contracts

- Contract-first: the OpenAPI schema is the agreement; generate the client types from it
  (openapi-typescript or equivalent) so a contract change that breaks the frontend fails the
  *build*, not the demo.
- Versioning policy declared up front (URL or header); additive changes preferred; breaking
  changes get a deprecation window and a migration note.
- Idempotency for any mutation a client might retry (idempotency keys on POSTs that create
  money-adjacent things); pagination, filtering, and error shape consistent across endpoints.

## §6 Pipeline & operations

- Trunk-based development, small PRs, short-lived branches
  (→ `coding-agent-skills:git-and-code-review`).
- CI stages, each a jidoka gate: format/lint → types → unit → integration (real DB in a
  container) → build → security scans (SAST, dependency audit, secret scan) → deploy to
  staging → smoke.
- Feature flags decouple deploy from release; canary or blue-green for anything user-facing;
  rollback is one command and is *rehearsed* (→ `full-stack-dev-skills:deploy-and-operate`,
  `references/stability-and-redundancy.md`).
- Reproducible builds: lockfiles committed, containers pinned, "works on my machine" retired.

## §7 Observability (genchi genbutsu at runtime)

- Structured JSON logs with correlation/trace IDs end to end.
- **OpenTelemetry** traces across frontend → API → DB; RED metrics (rate, errors, duration)
  per endpoint; a handful of business metrics (payments posted, forms completed).
- Error tracking (Sentry-class) with release tagging so a regression names its deploy.
- Alerts page on *user-impacting symptoms* (SLO burn), not on every internal hiccup — alert
  fatigue is Chicken Little syndrome in ops clothing.

## §8 Security baseline

- AuthN via the platform (OIDC/OAuth2); never hand-rolled password storage; short-lived
  tokens; AuthZ enforced server-side per resource (IDOR is the classic miss).
- Input validated at the boundary (schemas), output encoded (XSS), parameterized queries only
  (SQLi), CSRF protection where cookies auth, security headers (CSP, HSTS).
- Secrets in a manager, never in code or logs; dependency and secret scanning in CI
  (see `adversarial-testing.md` §5 for the hostile version of all of this).

## §9 Definition of Done (the standard-work checklist)

- [ ] Typed end to end; lint/format/type gates green
- [ ] Tests: unit for logic, integration for the seam touched, property-based where input
      space is wild; coverage of the critical path, not vanity totals
- [ ] Four UI states designed and accessible (see `accessible-ui-design-system.md` checklist)
- [ ] Contract updated + client types regenerated (if API changed)
- [ ] Migration rehearsed + rollback path (if schema changed)
- [ ] Observability: logs/traces/metrics for the new path; alert if it's an SLO surface
- [ ] Flagged, canaried, or otherwise reversible release plan
- [ ] Docs: ADR for a decision, runbook entry for an operable thing, changelog for users
