---
name: dmaic-problem-solving
description: >-
  Runs a Six Sigma DMAIC cycle — Define, Measure, Analyze, Improve, Control — to structure a
  data-driven improvement project that measures and confirms cause before changing anything:
  a signed project charter with voice of the customer translated into CTQs, an operationally
  defined metric checked for trustworthiness before a baseline is drawn, a root cause verified
  against data rather than opinion, a solution piloted against that baseline, and a control
  plan that keeps the gain from reverting — with a tollgate review between phases. Use when
  structuring an improvement project, reducing defects or variation with rigor, proving a fix
  actually moved the metric, or translating voice of the customer into CTQs and a charter.
  Triggers: DMAIC, six sigma, define measure analyze improve control, process improvement
  project, reduce defects, reduce variation, CTQ, project charter, tollgate, control plan,
  voice of the customer, prove the fix worked.
metadata:
  version: "1.1.0"
---

# DMAIC problem solving

## When to use
- Structuring a substantial improvement project where you must *prove* the change worked, not just try
  something (reducing a defect rate, cycle time, or process variation).
- Translating voice-of-the-customer into measurable **CTQs** and a project charter.
- Any problem important enough to justify a baseline, a verified cause, and a control plan.
- Not for: a quick one-off cause hunt with no measurement system → see
  `continuous-improvement-skills:root-cause-analysis`. To document the improved method afterward as the
  new standard → see `continuous-improvement-skills:standard-work`. Improving a *software delivery*
  process (releases, defects, pipelines) or building software to engineering standards → see
  `continuous-improvement-skills:lean-six-sigma-for-software`.

## Do it
Work the five phases in order, with a **tollgate** review between each — don't advance until the prior
phase's deliverable is real. See `references/phase-toolkit.md` for each phase's checklist. The
assistant drafts every phase artifact — charter, data-collection plan, analysis, control plan — and
runs the arithmetic; the human owns the data's provenance, tollgate sign-off, and the rollout decision.
1. **Define.** Write a project charter: problem statement (quantified, blame-free), goal/target,
   scope, business case, team, timeline. Scope the process with **SIPOC**. Capture **voice of the
   customer** and translate it into **CTQs** (Critical-to-Quality characteristics) with measurable
   specs. Output: an approved charter everyone signs.
2. **Measure.** Define the metric operationally (so two people count it the same way), build a data-
   collection plan, and run a quick **measurement-system sanity check** — is the data trustworthy,
   consistent, and unambiguous? Then collect a **baseline** of current performance. Output: a
   trustworthy baseline you can later compare against.
3. **Analyze.** Find and *verify* the root cause. Use fishbone/5 Whys (see
   `continuous-improvement-skills:root-cause-analysis`) to generate hypotheses, then **test them
   against data** rather than opinion — compare groups, look for correlation, run a significance test
   where warranted (see `data-analytics-bi-skills:statistical-inference`). Output: a cause confirmed
   by data, not asserted.
4. **Improve.** Generate candidate solutions that address the verified cause, select on impact vs.
   effort/risk, and **pilot** on a small scale before full rollout. Measure the pilot against the
   baseline. Output: a solution shown to move the metric on real data.
5. **Control.** Lock the gain in: write the new **standard work**, set up ongoing monitoring (a control
   chart / SPC or a simple KPI with limits), define the response plan when it drifts, and hand off
   ownership to the process owner. Confirm the improvement holds over time. Output: a control plan and
   a documented, owned, sustained result.

## Why / learn
What separates DMAIC from guess-and-check is a single rule enforced by its sequence: **you measure and
confirm the cause before you change anything.** Most failed "improvements" skip straight from a problem
to a favorite solution — they change the process, the number wobbles, and no one can say whether it was
the change, noise, or the season. DMAIC blocks that. Measure comes before Analyze so you have a
*trustworthy baseline* — and the measurement-system check exists because a change measured with a bad
ruler is unknowable; if your data can't be trusted, nothing downstream can. Analyze comes before Improve
so the cause is *verified with data*, not asserted — you fix what actually drives the defect, not what
feels responsible. Improve pilots before rollout so you learn cheaply and reversibly. And **Control is
the phase everyone skips and the reason gains evaporate**: without new standard work and ongoing
monitoring, the process quietly reverts to how it was, and six months later the problem is back. The
tollgates are deliberate friction — each is a checkpoint that the prior phase produced something real, so
the rigor is front-loaded where it prevents wasted work. The payoff isn't just this fix; it's a process
whose variation you now understand and can keep in control.

## Common mistakes
- Jumping to a solution in Define → you skip the baseline and the cause. Hold the sequence.
- Skipping the measurement-system check → you improve against an untrustworthy ruler; the result is noise.
- Asserting the cause in Analyze instead of testing it → you fix the wrong thing. Confirm with data.
- Full rollout with no pilot → an expensive, hard-to-reverse mistake. Pilot small first.
- Declaring victory at Improve and skipping Control → the gain silently reverts. Standardize and monitor.
- Confusing a one-off shift with a real change → check against the baseline and normal variation.
- A charter with a fuzzy goal → you can't tell if you succeeded. Make the target measurable.

## Tailor to your environment
Record your real project setup in `references/your-environment.md` (use `your-environment.private.md`,
git-ignored, if it names real customers, systems, or numbers). Capture your CTQ definitions and specs,
where you pull baseline data, your measurement-system and significance conventions, your pilot and
control-chart practice, and who owns tollgate sign-offs. Never commit real customer or transaction data —
keep it sanitized to structure.

## References
- references/phase-toolkit.md — per-phase deliverables, tollgate questions, and the tools each phase uses
- references/your-environment.md — your CTQs, data sources, and sign-offs (add when supplied)
