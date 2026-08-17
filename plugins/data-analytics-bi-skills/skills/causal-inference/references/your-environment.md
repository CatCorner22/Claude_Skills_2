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
- **One-unit-first rollouts (clean 2×2 DiD candidates):** <the single pilot office, the one
  region that went first while the rest held> — **count your treated units here.** One treated
  unit means no conventional standard error exists; note whether you have a pool of untreated
  units (synthetic control is possible) or not (report the estimate with its checks and no
  interval). See `causal-identification.md` §5.
- **Staggered / phased rollouts (staggered-adoption DiD candidates):** <office-by-office
  launches over weeks, phased policy dates, cohort-by-cohort migrations> — **not the same design
  as the row above.** A two-way fixed-effects regression is biased here (it uses already-treated
  units as controls and can flip the sign); record which staggered-adoption estimator your team
  has agreed to use, and whether any units stay **never-treated** — those are the ones carrying
  the identification. See `causal-identification.md` §5a.
- **Assignment quirks (IV candidates):** <rotation-based case assignment, timing accidents,
  eligibility nudges> — for each, record the **first-stage strength** you actually measured (F,
  and the share of units the instrument moved) and **who the compliers are in words**, since that
  subpopulation is what any estimate describes.

## Known confounders and colliders in your data
- **Usual suspects (adjust when on a backdoor):** <seasonality, mix shift, team, tenure>
- **Selection filters that are colliders in disguise:** <"escalated only," "closed-won only",
  "audited only" — datasets defined by an outcome>

## Burden of proof
- Who must be convinced, and at what standard: <a manager deciding a rollout | opposing
  counsel | a regulator | a peer-review bar>
- What claim strength each audience accepts: <"consistent with" vs "demonstrates">

## Sensitivity convention
- Which named sensitivity method your audience accepts: <E-value on the point estimate and the
  near-null confidence limit | Rosenbaum bounds (Γ) for matched designs | negative-control
  outcome> — pick one before the analysis, so the answer to "what if something else explains it"
  is a number rather than an argument.

## Where the association arithmetic runs
- Your testing conventions and tools live with `data-analytics-bi-skills:statistical-inference`
  — keep the two environment files consistent. **Not covered there:** clustered standard errors
  and the few-treated-clusters problem. That stays here (`causal-identification.md` §5); record
  the convention your team uses so nobody assumes the other skill handled it.
