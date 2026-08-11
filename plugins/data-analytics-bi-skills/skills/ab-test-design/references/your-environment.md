# Your A/B test-design environment (fill in)

Wire in your current role here — the skill stays generic until this file names your real
tests. If anything is sensitive (real metric values, client identifiers, live results), keep
it in `your-environment.private.md` instead — that suffix is git-ignored. Commit only
sanitized, structural examples.

## What you actually test
- <pricing-page variants | intake-form versions | outreach/dunning letters | notification
  cadences | queue-routing or process pilots | feature flags>

## Randomization units and interference channels
- **Units available:** <user / account / case / matter / office / time-slice>
- **Known spillover:** <shared queues, one team handling both arms, shared budgets, word of
  mouth> → coarsest unit that contains each

## Baselines for sizing
- **OEC candidates and their historical baselines/variances:** <response rate p=…, cycle time
  mean/sd=…> (real values → private file)
- **House MDE conventions:** <smallest effect worth acting on, per metric>
- **Traffic/volume reality:** <units per week available to a test>

## Guardrail set
- <complaint rate, opt-out rate, error/rework rate, latency, staff overtime> with veto
  thresholds and who owns each

## Authority and cadence
- **Launch/stop authority:** <who pre-commits the stopping rule and who may override — in
  writing>
- **Readout cadence:** <when scorecards are read; SRM check first, every time>
- **A/A policy:** <when new assignment machinery must pass an A/A before its first real test>

## Analysis handoff
- Statistical conventions (α, power, sidedness, multiplicity) live with
  `data-analytics-bi-skills:statistical-inference` — keep the two environment files consistent.
