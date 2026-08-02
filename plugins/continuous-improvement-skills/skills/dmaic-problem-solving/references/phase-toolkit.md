# DMAIC phase toolkit (reference)

Per-phase deliverables, the tools each uses, and the tollgate question that gates advancement. Framed
for finance/accounting/treasury projects.

## Contents
- Define
- Measure
- Analyze
- Improve
- Control
- Tollgate discipline

## Define
- **Deliverables:** project charter (problem statement, goal/target, scope, business case, team,
  timeline); SIPOC; voice-of-customer captured; CTQs with measurable specs.
- **Tools:** SIPOC, VOC interviews, CTQ tree (translate a customer need → measurable characteristic →
  spec/limit), stakeholder map.
- **Finance example:** "Cut duplicate-payment defects from 1.2% to <0.3% of runs by Q4." CTQ = each
  payment is unique and authorized; spec = zero duplicates per run.
- **Tollgate:** Is the problem quantified, the goal measurable, and the scope bounded? Charter signed?

## Measure
- **Deliverables:** operational definition of the metric; data-collection plan; measurement-system
  sanity check; **baseline**.
- **Tools:** operational definitions (so two people count identically), data-collection plan (what,
  who, how, sample size), a Gage/attribute agreement check or at minimum a consistency review, run
  chart of the baseline.
- **Watch:** ambiguous definitions ("late" — by whose clock?) and untrustworthy source data poison
  everything downstream.
- **Tollgate:** Can we trust the data, and do we have a baseline to improve against?

## Analyze
- **Deliverables:** a **verified** root cause.
- **Tools:** fishbone/6M and 5 Whys to generate hypotheses (see
  `continuous-improvement-skills:root-cause-analysis`); Pareto to prioritize; then *test* with data —
  stratify and compare groups, scatter/correlation, hypothesis tests where warranted (see
  `data-analytics-bi-skills:statistical-inference`). Distinguish common-cause from special-cause
  variation.
- **Watch:** correlation is not cause; confirm the driver changes the effect.
- **Tollgate:** Is the cause confirmed by data, not opinion?

## Improve
- **Deliverables:** a piloted solution shown to move the metric.
- **Tools:** solution brainstorming against the verified cause, impact/effort (or PICK) selection,
  error-proofing (poka-yoke), a small-scale **pilot** measured against baseline; FMEA to check for new
  risks introduced.
- **Tollgate:** Did the pilot move the metric versus baseline, beyond normal variation?

## Control
- **Deliverables:** control plan; new standard work; monitoring; owner handoff; confirmed sustained
  result.
- **Tools:** standard work / SOP (see `continuous-improvement-skills:standard-work`), control chart /
  SPC or KPI with limits, a response plan for out-of-limit signals, and a formal handoff to the
  process owner.
- **Tollgate:** Is the gain standardized, monitored, owned, and holding over time?

## Tollgate discipline
Do not advance a phase until its deliverable is real. The tollgates front-load rigor: each checkpoint
confirms the prior phase produced something trustworthy, which is cheaper than discovering it was hollow
two phases later. A DMAIC project can and should be paused or killed at a tollgate.
