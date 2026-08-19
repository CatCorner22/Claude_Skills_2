---
name: reliability-engineering
description: >-
  Applies reliability-engineering math to systems and processes: splits non-repairable populations
  (Weibull time-to-failure, censoring, fit checks, bootstrap bounds) from repairable systems with
  recurrent failures (power-law NHPP / Crow-AMSAA trend), reads beta to pick burn-in,
  run-to-failure, or scheduled replacement, computes MTBF, MTTR, time- or event-based availability,
  and an error budget, converts an SLO into a downtime budget, works series/parallel arithmetic —
  parallel credit only with demonstrated independent failover — and forecasts from two or three
  failures with Weibayes. Use when a failure log needs quantifying (interface or data-feed
  failures, job aborts, process breaks, equipment), when sizing redundancy against an uptime
  target, or setting a replacement schedule. Triggers: Weibull, bathtub curve, MTBF, MTTR,
  availability math, downtime budget, series parallel reliability, burn-in, failure rate fit, how
  much downtime does our SLO allow.
metadata:
  version: "1.3.0"
---

# Reliability engineering

## When to use
- A failure log exists — interface or data-feed failures, scheduled-job aborts, reconciliation
  breaks, equipment faults — and you want math, not adjectives, out of it.
- Deciding whether the thing you are modelling is a **non-repairable population** (Weibull) or a
  **repairable system with recurrent failures** (power-law NHPP / Crow-AMSAA) — the choice that
  makes every later number mean something, and the one most analyses skip.
- Converting an SLO or uptime commitment into an allowed-downtime budget — time-based, or
  event-based with an error budget — and sizing redundancy to meet it.
- Choosing a maintenance policy: burn-in, run-to-failure with redundancy, or scheduled
  replacement — including deterministic expiries (certificates, passwords, key rotations).
- Forecasting failures from tiny samples (two or three events) with Weibayes.
- Not for: qualitative resilience patterns — timeouts, retries, circuit breakers, bulkheads →
  see `continuous-improvement-skills:lean-six-sigma-for-software` (its stability-and-redundancy
  reference; this skill installs the math underneath it). Hunting unusual patterns in a metric
  stream → see `machine-learning-skills:anomaly-detection`.

## Do it
1. **Collect failure data honestly.** Times to failure on one consistent clock (operating hours
   or calendar time — pick one and say which). Units still running at the cutoff and units
   removed unfailed are **censored/suspended** — they enter the fit as censored, never get
   dropped: dropping survivors biases the estimate toward pessimism, and dropping early
   removals toward optimism. One failure mode per dataset; separate modes before fitting. Data
   quality is the human gate — confirm the timestamps mean what you think (failure start, not
   ticket-open).
2. **Classify the data before choosing a model — this decides everything after it.**
   - **Non-repairable population:** many units, each contributing **one** time-to-first-failure
     plus censored survivors (certificates, disks, one-shot devices). → Weibull, step 3.
   - **Repairable system:** **one** system failing, being repaired, and failing again — a feed, a
     job, a service, a machine. This is **recurrent-event data**, not a set of lifetimes. Fitting
     a Weibull to one repaired system's gaps mixes the hazard shape with the reliability trend and
     produces a β that the step-3 table cannot legally interpret. → power-law NHPP
     (**Crow-AMSAA**), step 4.
   Say which case you are in, in writing, before any number is quoted.
3. **Non-repairable: fit a Weibull, check the fit, bound it, then read β.** (Mechanics and worked
   numbers in `references/reliability-math.md`.) Check the fit before quoting anything — the
   Weibull plot should be straight; curvature means a threshold or mixed modes, and comparing r²
   against a lognormal plot guards against fitting the wrong family. Then **bootstrap the fit** —
   resample from the fitted parameters, refit, and report percentile intervals on β, η, and any
   B-life. A five-point fit typically leaves β spanning several-fold and a B10 spanning a factor
   of three, so no interval means no policy. The decision table:
   - **β < 1 — infant mortality.** Failures front-loaded (bad installs, fresh patches) →
     burn-in / shake-down before trusting the unit; hunt the defect source; do not schedule
     replacements.
   - **β ≈ 1 — random, constant hazard.** Age tells you nothing → run-to-failure plus
     redundancy and fast repair; scheduled replacement buys nothing.
   - **β > 1 — wear-out.** Hazard rises with age → scheduled replacement before the hazard
     knee (a B10-style life sets the interval).
   - **β → ∞ — deterministic expiry.** Certificates, passwords, key rotations fail on a known
     date: pure wear-out → calendar-driven renewal, alarmed well ahead.
   This is the bathtub curve made decidable: β tells you which region you are in and the region
   dictates the policy — for a **unit's own age**, which is why it applies only to case one.
4. **Repairable: model the failure intensity, not a lifetime.** Fit the power-law NHPP
   N(t) = λt^β with β̂ = n ÷ Σ ln(T/tᵢ) and λ̂ = n ÷ T^β̂ over an observation window T, and read it
   on its own scale: **β < 1 the system is improving** (fixes are sticking), **β ≈ 1 stable**
   (constant rate — random regime), **β > 1 degrading between repairs** (repair returns it
   bad-as-old; renew the unit or change repair practice — *not* a burn-in and *not* a wear-out
   claim about units). Run the cheap **Laplace trend test** first: no trend means a renewal
   process survives and Weibull-on-gaps becomes legitimate. β̂ has SE ≈ β̂/√n, so with a handful
   of failures report the interval and expect it to straddle 1.
5. **Compute MTBF, MTTR, availability — with bounds and the right definition.** MTBF = total
   operating time ÷ failures; MTTR = mean detection-to-restored time (include detection and
   diagnosis, not repair alone); Availability = MTBF ÷ (MTBF + MTTR). Attach the exact Poisson
   (chi-square) interval on the failure rate — nine failures give a roughly fourfold MTBF range,
   which decides whether "we missed the target" is a finding or noise. Convert the SLO into a
   downtime budget — 99.9% allows about 43.8 minutes a month (full table in the reference) — and
   compare measured to budget: the gap says whether to attack failure rate (MTBF) or recovery
   (MTTR). For a request-serving service, use the **event-based** definition instead
   (good events ÷ valid events) with an **error budget** = (1 − SLO) × valid events and a burn
   rate, because a service erroring on 3% of calls logs zero minutes of downtime. The two
   definitions don't convert unless traffic is uniform in time — say which one the SLO is written
   against.
   - **None of this applies to something that only acts on demand.** MTTR is clocked from
     when you *noticed*, and a dormant protective function — the interlock, the relief valve,
     the alarm, the failover path, the backup restore, the escalation that fires only when the
     primary misses — fails **hidden**: nothing tells you, because nothing has asked it to
     act. Its governing quantity is the **probability of failure on demand**, approximately
     **λT/2** for a constant hazard λ and a proof-test interval T. The lever is **T** — how
     often you deliberately exercise it — not repair speed and not redundancy, and the β ≈ 1
     row of the decision table ("run to failure, attack MTTR, scheduled replacement buys
     nothing") is exactly backwards for these: it means never find out. Redundancy multiplies
     only across channels that are independently tested; a test that does not invoke the real
     path is not a proof test. See `references/reliability-math.md` §4b.
6. **Do the system arithmetic.** Series (every part needed): R = ∏Rᵢ — chains multiply badly;
   two 99% components in series give 98.01%. **That product assumes independent failures too:**
   it is the no-overlap end of the range (fully overlapping outages would give 99%), so it is
   safe to plan with but is not a reason to skip the shared-cause audit. Parallel (any one
   suffices): R = 1 − ∏(1 − Rᵢ) — **claim it only where independent failover has been
   demonstrated.** An unexercised standby contributes nothing ("untested failover is scenery" —
   here a theorem, not a slogan), and common causes (shared credential, same patch, same
   endpoint) void independence even when the failover works.
7. **Small samples — Weibayes.** With two or three failures, assume β from engineering
   knowledge or the history of like items, and estimate only the scale η from the data. State
   the assumed β in every output, and show what a different defensible β would have given; the
   forecast is conditional on it.
8. **Deliver the decision, not the fit.** Paste the failure log and have the model run and
   interpret the math; the deliverable is the repairable/non-repairable call, a maintenance policy
   per failure mode with an interval on every quoted number, the downtime budget versus measured,
   and redundancy sized to the SLO — with the two judgments no fit can make flagged for a human:
   is the data honest, and are the parallel paths truly independent?

## Why / learn
The bathtub curve is folklore until it is decidable — everyone sketches it, but the sketch
doesn't say whether *your* failures are infant mortality or wear-out, and the two demand
opposite policies (replacing components under β ≈ 1 wastes money on parts whose age was never
the problem; running β > 1 parts to failure schedules your outages at the worst time). β is the
exponent of the hazard function, so one fitted number locates you on the curve — that is why
Weibull's distribution (introduced in the ASME Journal of Applied Mechanics, 1951) became a
citation classic: the shape parameter carries physical meaning, not just fit quality. US Air
Force handbook practice and Pratt & Whitney turbine-engine work, codified in Abernethy's New
Weibull Handbook, pushed it further: with Weibayes, usable replacement decisions from as few as
two or three failures [snippet-only].

**But β only locates you on that curve if the curve is the right picture of your data.** The
bathtub is a statement about *one unit's own age*, estimated across a population of units each
observed until its first failure. One system that fails and gets repaired nine times is a
different object: what varies there is the *rate* at which events arrive, and the model for it is
a recurrent-event one — the power-law NHPP. Both models have a parameter called β and the two
mean different things, which is exactly why the mistake is so easy and so invisible. Fitted to one
repaired system's gaps, the Weibull β absorbs reliability growth or decay along with any hazard
shape, and the resulting number is then read off a table it does not belong to. Asking
"repairable or not?" first is what keeps the rest of the arithmetic honest.

The second habit worth building is refusing point estimates. β̂ = 3.8 on five failures sounds
decisive and is not: bootstrap the fit and the interval routinely spans several-fold, which can
leave the *qualitative* claim (wear-out is real) standing while destroying the *quantitative* one
(replace at 51 days). Those two deserve different confidence and usually get the same, and that
is where reliability math causes harm rather than preventing it.

The system formulas teach the structural lessons. Series multiplication is why long chains
disappoint — a feed whose four steps run at 99.5%, 99.9%, 99.7% and 99.8% is a 98.90% chain, and
no step "feels" like the problem. Both formulas rest on independence, in opposite directions: in series,
correlated outages overlap and the product is the pessimistic end of the range (safe to plan
with); in parallel the product is the whole claim, so the moment both paths share a credential, a
patch cycle, or an endpoint the joint failure probability is the common cause's, not the product's
— which is why demonstrated, exercised failover is the price of admission for parallel credit.
Availability arithmetic converts "how reliable is enough?" from taste into a budget you can spend
and audit, whether you count minutes or events; counting events is the fairer measure wherever
failure is partial rather than total. The barrier to all of this was never the concepts — it was
the statistics: MLE fits, censoring, plotting positions, trend tests were a reliability
engineer's trade. With the math runnable on a pasted log, what remains genuinely human are the
judgments no fit can make: whether the data is honest, and whether the redundant paths share a
common cause.

## Common mistakes
- Fitting a Weibull to one repaired system's inter-arrival times → a category error; that is
  recurrent-event data. Use the power-law NHPP (Crow-AMSAA), and read its β on its own scale.
- Reading an NHPP β through the bathtub table → β > 1 there means the system degrades between
  repairs, not that units wear out. Name which model produced the β you are quoting.
- Quoting β, η, or a B-life as a bare number → bootstrap it. A five-point fit can support
  "wear-out is real" while refusing to support "replace at 50 days."
- Skipping the fit check → a curved Weibull plot means a threshold or two mixed modes, and no β
  read off it means anything. Look at the plot; compare against a lognormal.
- Dropping censored/suspended units → biased fit; enter survivors and removals as censored.
- Mixing failure modes in one dataset → a meaningless in-between β; split by mode, fit each.
- Reading MTBF as a lifetime promise → it is the mean of a distribution; under β ≈ 1 roughly
  63% of units fail before MTBF. It also has wide bounds — nine failures leave a ~4× range.
- Scheduled replacement under β ≈ 1 → pure waste; random failure calls for redundancy and fast
  repair, not calendars.
- Time-based availability on a request-serving service → partial failure logs as zero downtime.
- Applying MTBF/MTTR/availability to a dormant protective function → its failures are hidden, so
  MTTR is meaningless; price it as probability of failure on demand (~λT/2) and manage the
  proof-test interval T.
- Adding a redundant channel to a protective function nobody tests → two things that can be
  silently dead, sharing whatever common cause killed the first.
  Count events (good ÷ valid) and spend an error budget.
- Multiplying a series chain without naming the independence assumption → the product is the
  no-overlap end of the range; still audit shared causes, which are what widen the blast radius.
- Parallel credit for an unexercised standby → treat it as absent until switchover is
  demonstrated; then re-check for common causes.
- MTTR clocked from ticket-open instead of failure-start → availability overstated; include
  detection lag.
- Mixing operating hours and calendar time in one fit → pick one clock and state it.

## Tailor to your environment
Record your real setup in `references/your-environment.md`: which feeds and interfaces you
monitor and where their failure timestamps live, **which of them are repairable systems and which
are populations of replaceable units** (that list is what stops the wrong model being fitted next
time), your uptime commitments and maintenance windows, whether each SLO is written time-based or
event-based, your MTTR convention (when the clock starts and stops), and known common-cause
couplings between "redundant" paths. Real incident details, system names, or account data go in
`your-environment.private.md` (git-ignored). Never commit real client or payment data.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/reliability-engineering.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/reliability-math.md — the repairable/non-repairable split, Weibull formulas with fit
  checks and bootstrap bounds, the β decision table, the power-law NHPP (Crow-AMSAA) with the
  Laplace trend test, MTBF/MTTR/availability with Poisson bounds, the SLO downtime-budget table and
  the event-based error-budget arithmetic, series/parallel arithmetic with its independence bounds,
  Weibayes, and a worked overnight-feed failure log
- references/your-environment.md — your feeds, SLOs, and repair-time conventions (add when supplied)
