# Architecture decisions (reference)

The default tree with the reason for every boundary and the test that tells you the boundary is
real; a "where does this code go" question carried end to end with the resulting change manifest;
the split signals that count and the five that only look like they do; twelve-factor config as
code rather than as a slogan; and the failure envelopes of all three rules.

## Contents
- The reference tree, boundary by boundary
- Enforcing the import rule (20 lines of pytest)
- Worked example: where does the overdue-reminder feature go?
- Split signals that count — and the five imposters
- Failure envelope: where monolith-first stops working
- Failure envelope: where feature-first layout stops working
- Twelve-factor config, concretely
- Failure envelope: where twelve-factor stops being enough
- Migrating a layer-first tree without a big bang
- Stack decision table
- Rendering-split decision
- Deliverable contract: the one-page architecture doc

## The reference tree, boundary by boundary

```
app/
├── main.py                  # builds the FastAPI app, mounts every feature router
├── config.py                # the ONLY file that reads the environment
├── db.py                    # engine + session factory. No models.
├── jobs.py                  # the scheduler's registry of job callables
├── platform/                # code that outlives every feature
│   ├── email.py             #   transport: send_text(to, subject, body)
│   ├── errors.py            #   the one error shape + exception handlers
│   └── security.py          #   hashing, token signing
├── features/
│   ├── invoices/
│   │   ├── __init__.py      #   the PUBLIC surface: what other features may call
│   │   ├── routes.py        #   HTTP only — parse, call service, return
│   │   ├── models.py        #   ORM tables owned by this feature
│   │   ├── rules.py         #   pure domain functions: no db, no clock, no I/O
│   │   ├── service.py       #   orchestration: db + rules + platform calls
│   │   ├── jobs.py          #   the body of any scheduled work
│   │   ├── templates/       #   this feature's emails/pages
│   │   └── tests/           #   dies when the feature dies
│   └── customers/
└── static/                  # built frontend assets land here at image build
migrations/                  # one Alembic history for the whole app
frontend/                    # separate toolchain, separate lockfile
tests/                       # ONLY tests that cross features (end-to-end flows)
.env.example                 # committed; .env is not
```

Each boundary earns its place by answering one question, and each has a test that says whether it
is real or decorative:

| Boundary | Why it exists | The test that it is real |
|---|---|---|
| `main.py` ↔ features | Composition points one way: main knows every feature, no feature knows main | Import a feature's `service.py` in a plain script with no app object. If it fails, the framework has leaked into the domain |
| `config.py` | One reader of the environment means one place to see every knob | `grep -rn "os.environ\|os.getenv" app/` returns `config.py` and nothing else |
| `db.py` (no models) | Models import the session base; if `db.py` imported models you get an import cycle the first time a feature is added | `db.py` imports nothing from `app.features` |
| `platform/` | Holds what survives deleting every feature | Ask it of each file: email *transport* survives; the reminder email *template* does not |
| `features/<x>/__init__.py` | The published surface; everything else in the folder is private | The boundary test below passes |
| `rules.py` vs `service.py` | Pure rules are testable without a database, which is where date and money arithmetic actually gets checked | `rules.py` has no import of the session, no `datetime.now()` — the clock arrives as a parameter |
| feature `tests/` vs top-level `tests/` | Deleting a feature must delete its tests | After `rm -rf app/features/x`, the remaining suite still collects |
| `migrations/` at the root | The database is one shared resource, so its history is global even when the code is not. Per-feature migration folders give you multiple Alembic heads and a merge conflict on every branch | `alembic heads` prints one line |
| `frontend/` as a sibling | Different toolchain and lockfile; the built artifact is copied into `app/static/` at image build (`full-stack-dev-skills:deploy-and-operate`) | The backend test suite runs with `node` uninstalled |

Naming convention with a payoff: a feature folder is the domain noun, plural, and matches both the
URL segment (`/invoices`) and the table prefix (`invoices`, `invoice_reminders`). Given a URL from a
bug report or a table name from a slow-query log, you know the folder without searching.

## Enforcing the import rule (20 lines of pytest)

A boundary rule nobody checks is a preference. This is the mechanical version:

```python
# tests/test_boundaries.py
import ast, pathlib

FEATURES = pathlib.Path("app/features")


def test_features_touch_each_other_only_through_their_public_surface():
    violations = []
    for py in FEATURES.rglob("*.py"):
        owner = py.relative_to(FEATURES).parts[0]
        for node in ast.walk(ast.parse(py.read_text())):
            if not isinstance(node, ast.ImportFrom) or not node.module:
                continue
            parts = node.module.split(".")            # app, features, <other>, <leaf>
            if len(parts) < 3 or parts[:2] != ["app", "features"]:
                continue
            if parts[2] != owner and len(parts) > 3:  # deeper than the package = private
                violations.append(f"{py}: imports {node.module}")
    assert not violations, violations
```

The rule is positional, not a list of forbidden filenames: `from app.features.customers import
contact_email` addresses the package — therefore `__init__.py` — and passes; anything deeper fails.
The version most people write first is a denylist of the insides (`{"models", "routes", "rules"}`),
and it quietly permits whatever filename someone adds next — including `service.py`, which is
exactly where the public function's body lives.

Three things this does not catch, and the fix for each:

- **Relative imports.** `from ..customers.models import Customer` has `node.module == "customers.models"`
  and `level == 2`, so it slips past. Ban relative imports repo-wide instead of complicating the
  test — Ruff's `TID252` does it in one config line.
- **Plain `import` statements.** `import app.features.customers.models as m` is an `ast.Import`,
  not an `ast.ImportFrom`, so the walk skips it; `TID252` does not cover it either. One extra
  branch closes it (`elif isinstance(node, ast.Import): modules = [a.name for a in node.names]`),
  and is worth adding only if your codebase actually uses that style.
- **Reaching through the ORM.** `db.query(Invoice).join(Customer)` imports nothing illegal and still
  couples the two schemas. Nothing static will catch it; code review is the control, and the tell in
  review is a query in feature A that names feature B's table.

If you already run `import-linter`, its layered contracts express this better and also catch cycles.
The pytest version exists so that a project with no extra dependency still has the rule enforced —
the point is that *something* fails, not which tool does it.

## Worked example: where does the overdue-reminder feature go?

**The request:** "When an invoice is 30 days past due, email the customer a reminder — once — and
show a Reminders tab on the invoice page."

This is the case that breaks naive layouts, because it touches domain logic, persistence, a
template, an outbound transport, a scheduler, a route, another feature's data, and config. Eight
kinds of code, one feature.

**The decision procedure.** Ask three questions in order, stop at the first that answers:

1. **Deletion test** — if this feature were cancelled tomorrow, would this code be deleted with it?
   Yes → `features/<this feature>/`.
2. **Second-noun test** — does the code need a fact owned by another feature? Then it does not move
   there; you call that feature's public function and keep the code where question 1 put it.
3. **Runtime test** — does this exist because of the framework or the deployment rather than the
   domain? → `app/` root or `app/platform/`.

Applied, piece by piece:

| # | Piece of code | Q | Goes | Because |
|---|---|---|---|---|
| 1 | `is_reminder_due(issued, due, today, last_sent, grace_days)` | 1 | `features/invoices/rules.py` | Pure date arithmetic, dies with the feature, and this is the part that must be tested against a calendar without a database |
| 2 | Query for invoices past due with no reminder | 1 | `features/invoices/service.py` | Touches this feature's own tables only |
| 3 | `InvoiceReminder` table (`invoice_id`, `sent_at`) | 1 | `features/invoices/models.py` | Owned by invoices; the "once" guarantee is its unique index |
| 4 | The reminder email body | 1 | `features/invoices/templates/` | Cancel the feature and the template is meaningless |
| 5 | SMTP client, retries, from-address | 3 | `platform/email.py` | Survives deleting every feature; the next feature that mails reuses it unchanged |
| 6 | The customer's email address | 2 | call `customers.contact_email(db, id)` | Invoices must not join `customers.email` — that join is what makes the customers table unchangeable later |
| 7 | Daily 07:00 schedule entry | 3 + 1 | registration in `app/jobs.py`, body in `features/invoices/jobs.py` | The registry is a framework file that must know everything; the body must be deletable |
| 8 | `reminder_grace_days`, `reminders_enabled`, `smtp_url` | 3 | `config.py` | Varies per deploy, not per customer (see the config-vs-data rule below) |
| 9 | `GET /invoices/{id}/reminders` behind the Reminders tab | 1 | `features/invoices/routes.py` | The tab dies with the feature; the route parses and calls the service, and holds no rule of its own |

Row 6 is the one people get wrong, and it is worth being explicit about the cost. The join version
is one line shorter today. It also means that the day customers grows a `contacts` table with a
billing-contact role, invoices breaks — and nothing in the invoices feature said it depended on the
shape of `customers.email`. The function call makes the dependency a signature that a type checker
and a grep can both see.

**The artifact this produces.** The change manifest for the finished feature:

| File | Lines added |
|---|---|
| `app/features/invoices/rules.py` | 9 |
| `app/features/invoices/models.py` | 7 |
| `app/features/invoices/service.py` | 22 |
| `app/features/invoices/jobs.py` (new) | 6 |
| `app/features/invoices/templates/reminder_email.txt` (new) | 8 |
| `app/features/invoices/routes.py` | 5 |
| `app/features/invoices/tests/test_reminders.py` (new) | 34 |
| `app/platform/email.py` | 11 |
| `app/features/customers/__init__.py` + `service.py` | 4 |
| `app/config.py` | 3 |
| `app/jobs.py` | 1 |
| `migrations/versions/xxxx_invoice_reminders.py` | 18 |

Inside `features/invoices/`: 9 + 7 + 22 + 6 + 8 + 5 + 34 = 91 lines. Outside it: 11 + 4 + 3 + 1 + 18 = 37 lines,
for 91 + 37 = 128 lines across the twelve entries above — and 91 / 128 ≈ 71% of the change sits in
one folder.

**Read the shape, not the total.** The 37 outside lines are the signature of a boundary that held:
one new platform capability, three one-line additions, and a migration. The failure signature looks
different and is easy to recognise — a layer-first version of this same feature puts 30 lines into a
shared `services/notification_service.py` with a branch on document type, so the *next* notification
feature edits that same file, and the two features are now coupled through a file neither of them
owns. When you review a diff, count the lines that landed in files the feature does not own. Trending
up, feature after feature, is the earliest visible sign that the layout is dissolving.

Sanity check on piece 1 while you are there, because it is the only real arithmetic in the feature:
an invoice due on day 0 with `grace_days = 30` is first eligible on day 30, so a run on day 29 must
send nothing and a run on day 30 must send exactly one — and a second run on day 31 must also send
nothing. Three assertions, no database, no SMTP. That test is why `rules.py` is a separate file.

## Split signals that count — and the five imposters

### The four signals

**1. Resource shape divergence, measured.** One deployable means every replica is sized for the
fattest module. If a rendering or inference path peaks at 3.5 GB while every other path holds under
0.4 GB, then five replicas cost 5 × 3.5 = 17.5 GB, where a split fleet of four web replicas plus one
fat worker costs 4 × 0.4 + 3.5 = 5.1 GB — a difference of 17.5 − 5.1 = 12.4 GB bought to serve a path
that is a small share of traffic. Two conditions make this real rather than theoretical: the ratio
has to be large (a 20% difference is noise; roughly 5× or more is where the fleet-wide rounding
dominates) and you have to already be running enough replicas that the multiplier bites. At two
replicas the whole saving is about one machine, which does not pay for a second pipeline. Redo this
with your own numbers — the numbers above are an illustration of the calculation, not a benchmark.

**2. Release cadence conflict, counted from the deploy log.** Count, for one quarter: deploys of A
delayed a day or more by unrelated work in B, and the median hours lost. Say that is 9 events at 6
hours: 9 × 6 = 54 hours in the quarter, so 54 × 4 = 216 hours a year. Now price the split's carrying
cost in the same unit — the five items in the next paragraph — and note the asymmetry that decides
it: the blocked-deploy cost is recoverable by cheaper means (deploy trains, feature flags, faster
tests, trunk-based development), while the split's cost is permanent and compounds. So the rule is
not "216 beats the estimate"; it is "216 survived a quarter of the cheap fixes and still beats the
estimate, twice running." Two consecutive quarters, because one quarter of a bad migration looks
exactly like a cadence conflict.

The five carrying costs, none of which is zero: a second build/deploy pipeline; a second set of
dashboards, alerts and on-call surface; a versioned contract between the two, which now needs
backward-compatible changes; a new failure mode that did not previously exist (partial availability —
A up, B down, and a decision about what A does then); and a local dev setup that requires both
services running. That fifth one is the one teams forget and the one that slows every new joiner.
The cost also grows superlinearly: n services have up to n × (n − 1) ÷ 2 pairwise contracts, so at
n = 5 that is 5 × 4 ÷ 2 = 10 seams to keep compatible.

**3. Ownership that already matches the code.** Separate team ownership is a signal *only when the
code boundary is already where the team boundary is*. If two teams edit the same files today,
splitting the deployable converts a merge conflict into a distributed contract negotiation, which is
strictly worse. Test it before believing it: attribute the last 200 commits in the candidate module
by team. If one team wrote nearly all of them, ownership is real. If it is a mix, you have a
shared module, not a shared service.

**4. A containment requirement.** Blast radius or regulatory isolation is the one signal that
justifies a split on day one, because it is not about scale at all. The tell is that you can state
what must be *impossible*, not merely unlikely: "a bug in user-supplied report rendering must not be
able to read the payments table", "this data may not leave a jurisdiction". Process isolation is a
real control there in a way that a module boundary is not. If you cannot state the forbidden
outcome in one sentence, this is not your signal.

### The five imposters

| Sounds like a split | What it actually indicates | The cheaper fix |
|---|---|---|
| "The codebase is too big to understand" | Missing *module* boundaries, not missing *network* boundaries. Splitting makes the same tangle need two checkouts and a running dependency | Feature folders and the import test above |
| "The test suite takes 22 minutes" | Slow tests — usually per-test schema setup. Splitting shrinks each suite while the sum grows, and adds contract tests you did not have | `full-stack-dev-skills:testing-strategy`: transaction-rollback fixtures, parallelism |
| "Deploys are slow and scary" | A pipeline problem: fat images, migrations run as an app side effect, no rollback path | `full-stack-dev-skills:deploy-and-operate`; splitting multiplies the pipelines you have not fixed |
| "This team wants autonomy" | A process problem whose code boundary may be nowhere near the team boundary | Module ownership in CODEOWNERS plus review rights — most of the autonomy, none of the distributed tax |
| "We might need to scale later" | Nothing measurable. It is a prediction, and the boundary it suggests is a guess made at the moment you know least | Write the criterion down (see the deliverable contract) and revisit with data |

One genuine case hides among the imposters: **a different runtime is genuinely required** — a GPU,
a native library that pins an incompatible interpreter or CUDA version, a component that must be
written in another language for a hard reason. That is a proven boundary, not a guessed one; it is
signal 1 in a harder form, because no amount of module discipline makes one process host two
incompatible runtimes. Split exactly that module and nothing adjacent to it.

## Failure envelope: where monolith-first stops working

What the practitioner actually sees when the modular monolith has stopped being the right shape:

- **Memory-limit restarts traced to one endpoint.** The fleet is being sized for the p99 of a single
  path. Observable as OOM kills whose stack traces all name the same module.
- **A deploy checklist with human coordination on it.** When shipping requires notifying other teams
  and picking a window, the release cadence conflict has become a process, and processes do not
  shrink on their own.
- **A dependency resolution that cannot be solved.** Two modules need mutually incompatible versions
  of the same native dependency. This one is binary: you see a resolver failure, and no refactor
  fixes it.
- **A freeze.** A recurring deploy freeze is the terminal symptom — the organisation has concluded
  that deploying is dangerous and has stopped, which converts every subsequent release into a bigger
  release, which makes it more dangerous.

What you do *not* see, and should stop waiting for: a moment when the codebase "gets too big". Size
alone never produces a symptom you can act on, which is why it is the reason most often given and
the one least worth acting on.

## Failure envelope: where feature-first layout stops working

**The shared kernel eats the app.** Every `platform/` or `shared/` line is a line no feature can
delete, so its size measures how much of the codebase is permanently coupled. Measure it:

```bash
feat=$(find app/features -name '*.py' | xargs cat | wc -l)
plat=$(find app/platform -name '*.py' | xargs cat | wc -l)
echo "platform/features = $plat / $feat"
```

Read the *trend*, not the level. 2,400 ÷ 9,600 = 0.25 one quarter and 3,300 ÷ 10,100 ≈ 0.33 the next
means the shared layer added 3,300 − 2,400 = 900 lines while the domain added 10,100 − 9,600 = 500,
so the undeletable part of the codebase grew 900 ÷ 500 = 1.8 times faster than the part it exists to
serve — the layout is quietly reverting to layer-first with nicer folder names. The usual cause is a "shared" module that started
as one helper and became a place to put anything two features touched. The fix is not a ratio target;
it is to name what each platform module *is* and move anything that fails the survives-deleting-every-
feature test back into the feature that uses it.

A legitimately high ratio exists: an app that is mostly infrastructure with a thin domain — a
gateway, a proxy, a sync daemon — will have thin features by nature. The question the ratio asks is
whether the number matches the kind of app you believe you are building.

**Other places the layout is the wrong tool:**

- **A library or SDK.** Its consumers *are* the layers; the public API surface is the organising
  principle, and feature folders hide it.
- **A pipeline whose stages are the domain.** For ingest → transform → load, the stages are what
  changes together and what gets deleted together. That is layer-first and it is correct.
- **One feature.** Below roughly two or three features the folder level is pure ceremony; start flat
  in `app/` and introduce `features/` at the moment the second domain noun appears.
- **A coordinator that spans features.** A checkout flow that touches carts, payments and inventory
  is not a fourth feature — a "feature" whose only content is importing three others is a use case,
  and it belongs in the feature that owns the *outcome* (the order), calling the others' public
  surfaces. Creating `features/checkout/` produces a hub every feature depends on, which is the
  shared-kernel failure in a different costume.

## Twelve-factor config, concretely

```python
# app/config.py — the only file in the tree that reads the environment
from functools import lru_cache
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="APP_", extra="forbid"
    )

    database_url: str                          # no default -> required
    secret_key: SecretStr                      # no default, and never printed
    smtp_url: SecretStr

    reminder_grace_days: int = Field(default=30, ge=1, le=365)
    reminders_enabled: bool = False            # off is the safe default
    log_level: str = "INFO"


@lru_cache
def get_settings() -> Settings:
    return Settings()                          # constructed once, at import of the app
```

Five decisions in twenty lines, each of which is the point:

1. **No default on a secret.** A default for `secret_key` means the app boots in production with the
   development key and tells you nothing. Absent default → the process refuses to start.
2. **`SecretStr`.** Its `repr` and `str` mask the value as `**********`, so a settings object
   dumped into a log line or an exception page does not leak it. Getting the value takes
   `.get_secret_value()`, which makes every read of a secret greppable.
3. **Validation on the value, not just the type.** `ge=1, le=365` turns `APP_REMINDER_GRACE_DAYS=0`
   into a boot failure rather than a Monday morning where every invoice is overdue.
4. **`extra="forbid"`.** A key in `.env` that matches no field becomes an error instead of a silent
   no-op — `DATBASE_URL=...` fails at boot rather than leaving the default quietly in place. Caveat
   worth knowing: if several tools share one `.env`, this bites; give each its own prefix or file.
5. **`lru_cache`, not a module-level global.** One instance per process, constructible with an
   override in tests, and injectable as `Depends(get_settings)` (`full-stack-dev-skills:backend-api-development`).

**Three checks that prove the config is actually twelve-factor**, run them in CI:

```bash
# 1. One reader of the environment. Anything else here is a config leak.
grep -rn "os.environ\|os.getenv" app/ | grep -v "^app/config.py"

# 2. Fail fast and completely: an empty environment must fail in under a second,
#    listing EVERY missing variable, not just the first one.
env -i python -c "from app.config import Settings; Settings()"

# 3. The environments differ in values only. The NAME sets must be identical.
diff <(sort staging.env.names) <(sort prod.env.names)
```

Check 2 is the one that catches the common half-migration: a `Settings` class that exists while some
module still reads `os.environ` lazily on first use, so the app boots clean and dies an hour later
on the first request that touches that path. Pydantic reports all missing fields at once precisely
so that a fresh deploy tells you everything wrong in one attempt.

Check 3 is what makes staging predictive. The moment prod has a variable staging does not, staging
stopped testing prod.

**Config or data? The deploy test.** Config is what varies between *deploys of the same code*.
Anything that varies per customer, tenant, or user is data and belongs in the database. The tell is
the question "does changing this require a deploy?" — if a non-engineer needs to change it, or it
differs between two customers on the same deployment, an environment variable is the wrong home and
will be discovered as such the first time someone asks for a per-customer value.

| Kind of value | Home | Why |
|---|---|---|
| Database URL, secrets, external endpoints | Environment → `Settings` | Differs per deploy, never per request |
| Limits and toggles that differ between staging and prod | Environment → `Settings` | Same code, different deploy |
| Per-tenant grace periods, plan limits, branding | Database, keyed by tenant | Differs *within* one deploy |
| A value identical everywhere forever (a rounding rule) | A constant in the module that uses it | Making it configurable invents a variation nobody asked for |
| A flag someone must flip without shipping | Database (or a flag service), not env | An env flag flip is a restart; if that is unacceptable, it is data |

Short-lived deploy-scoped feature flags as environment booleans are fine and often the right call —
they are config because they change on the deploy boundary and get deleted after the rollout. A flag
that outlives two releases has become configuration of behaviour, and belongs with the other data.

## Failure envelope: where twelve-factor stops being enough

- **Secret rotation without a restart.** Settings are read once at boot, so rotating a credential
  means a rolling restart. That is usually fine and worth the simplicity. When it is not, you need a
  secret manager with a refresh path and a code path that re-reads — accept that you have left the
  simple model, and keep the exception to the one credential that needs it.
- **Too many variables.** Past a couple of dozen, per-environment drift becomes real and check 3
  starts failing for boring reasons. The answer is fewer variables, not better tooling: collapse
  host/port/user/password/database into one DSN, and delete the toggles for experiments that ended.
- **Config that must agree across services.** Two deployables that must hold the same value have a
  new class of bug — skewed config — that a monolith cannot have. Worth noting when you are pricing
  a split; it is one of the costs that never appears in the proposal.
- **Very large values.** Certificates, key material, or a policy document as an environment variable
  runs into per-variable size limits and unreadable diffs. Mount them as files and put the *path* in
  the environment.

## Migrating a layer-first tree without a big bang

Four steps, none of which requires a freeze:

1. Create `app/features/` and move **one** feature — the one with the fewest inbound imports, which
   you find with a grep for its module names. Leave shims at the old paths that re-export from the
   new ones, so nothing else has to change in the same commit.
2. Delete the shims for that feature when `grep -rn "old.path" app/` is clean. Do not start the
   second feature until the first has no shims; two half-moved features are harder to reason about
   than one unmoved one.
3. Add the boundary test in warn mode with an **allowlist file** of the violations that exist today,
   one per line. New violations fail immediately; old ones are visible and counted.
4. Make CI assert that the allowlist's line count never grows. This is the whole trick — an
   allowlist with no ratchet grows, and an allowlist that only shrinks converts a refactor into a
   monotone process that survives changing priorities.

Do not move the database schema at the same time. Code moves are reversible in a commit; schema
moves are not (`full-stack-dev-skills:database-and-orm`).

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

The column that matters is the third one, and the discipline is to write the *trigger* rather than
the option: "Redis when measurements demand it" is only useful if the doc names the measurement.
Replace each right-hand cell with the condition you would actually be able to observe.

## Rendering-split decision

- Mostly reading/writing records, few client-side state needs → server-rendered + htmx
  (one deployable, no JS build, far less UI code).
- Rich client state (editors, dashboards with live interactions, offline) → React SPA + JSON API.
- Hybrid: server-rendered app with a React island mounted only on the complex page.

Revisit when the UI's nature changes — not because a framework released a major version. The signal
that you chose wrong in the htmx direction is client state that has to be reconstructed from the DOM
on every interaction; the signal you chose wrong in the SPA direction is a frontend that is mostly
forms posting to endpoints that mostly do inserts, with a build pipeline and a duplicated validation
layer paid for nothing.

## Deliverable contract: the one-page architecture doc

The one-page constraint is load-bearing. A longer document is not read, and an unread architecture
doc is worse than none, because it gets cited as authority by people who have not opened it.

```markdown
# <App> architecture (revised YYYY-MM, owner: <role>)
Stack: <backend / frontend / db / hosting> — one line each, naming the constraint it satisfies
Layout: feature folders under app/features/; platform code in app/platform/; frontend in <...>
Boundaries: features call each other's public surface only; enforced by tests/test_boundaries.py
Config: env -> pydantic-settings (app/config.py); secrets via <mechanism>; .env git-ignored
Data vs config: per-tenant values live in <table>; env holds deploy-scoped values only
Data: SQLite in dev; <SQLite | Postgres> in prod; one Alembic history
Auth: <sessions | JWT>
Split criteria we will honor: <criterion> measured by <metric> from <source>, threshold <value>
Known debt: <violation> -> <plan or explicit acceptance, with who accepted it>
```

Item by item, "done" means:

| Item | Done when |
|---|---|
| Stack | Every choice has a reason naming a constraint, and at least one names the alternative rejected and why |
| Layout | A new engineer can place a named piece of code without asking. Test it by handing them the reminder question above |
| Boundaries | There is a test that fails on a violation. A boundary rule with no test is a preference |
| Config | Every variable is listed with type, secret-or-not, and default; `.env.example` matches the `Settings` fields exactly |
| Data vs config | The doc says where per-tenant behaviour lives, so the first request for it does not become an env var |
| Split criteria | Each names a *measurement*, a threshold, and where the number comes from. "When we need to scale" is not a criterion |
| Known debt | Each entry names the rule it violates and either a plan or an explicit, attributed acceptance |
| Revision | The doc names its owner and what triggers a revision: a stack change, a split, or a new cross-cutting concern |

**What does not belong in it:** endpoint lists, schema dumps, dependency inventories, anything a
tool generates. They go stale within weeks, and their staleness is what teaches readers to distrust
the parts of the document that were still true.
