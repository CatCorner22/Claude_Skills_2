# Your causal-inference environment (fill in)

Wire in your current role here — the skill stays generic until this file names your real
questions. If anything is sensitive (client names, case specifics, real figures), keep it in
`your-environment.private.md` instead — that suffix is git-ignored. Commit only sanitized,
structural examples.

## Causal questions your role actually faces
- <"Did the intake-form change cut resolution time?" / "Did the fee change move churn?" /
  "Did the new routing cause the backlog drop?">

## Natural experiments your organization generates for free
- **Cutoffs / thresholds (RD candidates):** <score lines, dollar thresholds, date cutoffs,
  eligibility rules>
- **Staggered / one-unit-first rollouts (DiD candidates):** <office-by-office launches,
  pilot regions, phased policy dates>
- **Assignment quirks (IV candidates):** <rotation-based case assignment, timing accidents,
  eligibility nudges>

## Known confounders and colliders in your data
- **Usual suspects (adjust when on a backdoor):** <seasonality, mix shift, team, tenure>
- **Selection filters that are colliders in disguise:** <"escalated only," "closed-won only",
  "audited only" — datasets defined by an outcome>

## Burden of proof
- Who must be convinced, and at what standard: <a manager deciding a rollout | opposing
  counsel | a regulator | a peer-review bar>
- What claim strength each audience accepts: <"consistent with" vs "demonstrates">

## Where the association arithmetic runs
- Your testing conventions and tools live with `data-analytics-bi-skills:statistical-inference`
  — keep the two environment files consistent.
