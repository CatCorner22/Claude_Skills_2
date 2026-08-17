---
name: reliability-engineering
description: >-
  Applies reliability-engineering math to systems and processes: fits a Weibull distribution to
  failure times (censored units handled honestly), reads the shape parameter beta to choose
  burn-in vs run-to-failure vs scheduled replacement, computes MTBF, MTTR, and availability,
  converts an SLO target into an allowed-downtime budget, works series/parallel system
  arithmetic — parallel credit only with demonstrated independent failover — and forecasts from
  two or three failures with Weibayes. Use when a failure log needs quantifying (interface or
  data-feed failures, job aborts, process breaks, equipment), when sizing redundancy against an
  uptime target, or when setting a replacement or renewal schedule. Triggers: Weibull, bathtub
  curve, MTBF, MTTR, availability math, downtime budget, series parallel reliability, burn-in,
  failure rate fit, how much downtime does our SLO allow.
metadata:
  version: "1.1.0"
---

# Reliability engineering

## When to use
- A failure log exists — Oracle interface or BAI2 feed failures, scheduled-job aborts, recon
  breaks, equipment faults — and you want math, not adjectives, out of it.
- Converting an SLO or uptime commitment into an allowed-downtime budget, and sizing redundancy
  to meet it.
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
2. **Fit a Weibull and read the shape parameter β.** (Fitting mechanics and worked numbers in
   `references/reliability-math.md`.) The decision table:
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
   dictates the policy.
3. **Compute MTBF, MTTR, availability.** MTBF = total operating time ÷ failures. MTTR = mean
   detection-to-restored time (include detection and diagnosis, not repair alone).
   Availability = MTBF ÷ (MTBF + MTTR). Convert the SLO into a downtime budget — 99.9% allows
   about 43.8 minutes a month (full table in the reference) — and compare measured downtime to
   the budget: the gap tells you whether to attack failure rate (MTBF) or recovery (MTTR).
4. **Do the system arithmetic.** Series (every part needed): R = ∏Rᵢ — chains multiply badly;
   two 99% components in series give 98.01%. Parallel (any one suffices):
   R = 1 − ∏(1 − Rᵢ) — **but claim it only where independent failover has been demonstrated.**
   An unexercised standby contributes nothing ("untested failover is scenery" — here a theorem,
   not a slogan), and common causes (shared credential, same patch, same endpoint) void
   independence even when the failover works.
5. **Small samples — Weibayes.** With two or three failures, assume β from engineering
   knowledge or the history of like items, and estimate only the scale η from the data. State
   the assumed β in every output; the forecast is conditional on it.
6. **Deliver the decision, not the fit.** Paste the failure log and have the model run and
   interpret the math; the deliverable is a maintenance policy per failure mode, the downtime
   budget versus measured, and redundancy sized to the SLO — with the two judgments no fit can
   make flagged for a human: is the data honest, and are the parallel paths truly independent?

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
two or three failures [snippet-only]. The system formulas teach the two structural lessons.
Series multiplication is why long chains disappoint — a bank feed that traverses four
99%-class steps is a ~98.9% chain, and no step "feels" like the problem. The parallel formula
flatters, because it assumes independence: the moment both paths share a credential, a patch
cycle, or an endpoint, the joint failure probability is set by the common cause, not the
product — which is why demonstrated, exercised failover is the price of admission for parallel
credit. Availability arithmetic converts "how reliable is enough?" from taste into a budget you
can spend and audit. The barrier to all of this was never the concepts — it was the statistics:
MLE fits, censoring, plotting positions were a reliability engineer's trade. With the math
runnable on a pasted log, what remains genuinely human are the judgments no fit can make:
whether the data is honest, and whether the redundant paths share a common cause.

## Common mistakes
- Dropping censored/suspended units → biased fit; enter survivors and removals as censored.
- Mixing failure modes in one dataset → a meaningless in-between β; split by mode, fit each.
- Reading MTBF as a lifetime promise → it is the mean of a distribution; under β ≈ 1 roughly
  63% of units fail before MTBF.
- Scheduled replacement under β ≈ 1 → pure waste; random failure calls for redundancy and fast
  repair, not calendars.
- Parallel credit for an unexercised standby → treat it as absent until switchover is
  demonstrated; then re-check for common causes.
- MTTR clocked from ticket-open instead of failure-start → availability overstated; include
  detection lag.
- Mixing operating hours and calendar time in one fit → pick one clock and state it.

## Tailor to your environment
Record your real setup in `references/your-environment.md`: which feeds and interfaces you
monitor and where their failure timestamps live (e.g. the bank-statement feed, interface run
logs), your uptime commitments and maintenance windows, your MTTR convention (when the clock
starts and stops), and known common-cause couplings between "redundant" paths. Real incident
details, system names, or account data go in `your-environment.private.md` (git-ignored).
Never commit real bank or payment data.

## References
- references/reliability-math.md — formulas, the β decision table, the SLO downtime-budget table, and worked examples (a BAI2-feed MTBF case, series/parallel arithmetic, a Weibull fit, Weibayes)
- references/your-environment.md — your feeds, SLOs, and repair-time conventions (add when supplied)
