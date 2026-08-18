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
  `continuous-improvement-skills:lean-six-sigma-for-software`. Nor for problems outside DMAIC's
  operating envelope — a defect that occurs a handful of times a year (no baseline is possible),
  a process so unstable it has no single level to improve against (remove the special causes
  first), a one-off with no repeating cycle, or a process whose fix is already known and obvious.
  `references/phase-toolkit.md` closes with the full "when DMAIC is the wrong machine" list and
  where each case routes.

## Do it
Work the five phases in order, with a **tollgate** review between each — don't advance until the prior
phase's deliverable is real. `references/phase-toolkit.md` carries each phase's deliverable contract
and its tollgate questions written as *the answer that means stop*; `references/worked-project.md`
carries one project through all five phases with numbers that recompute. The
assistant drafts every phase artifact — charter, data-collection plan, analysis, control plan — and
runs the arithmetic; the human owns the data's provenance, tollgate sign-off, and the rollout decision.
1. **Define.** Write a project charter: problem statement (quantified, blame-free), goal/target,
   scope, business case, team, timeline. Scope the process with **SIPOC**. Capture **voice of the
   customer** and translate it into **CTQs** (Critical-to-Quality characteristics) with measurable
   specs. Output: an approved charter everyone signs.
2. **Measure.** Define the metric operationally (so two people count it the same way), build a data-
   collection plan, and run a quick **measurement-system sanity check** — is the data trustworthy,
   consistent, and unambiguous? Then collect a **baseline** of current performance. Output: a
   trustworthy baseline you can later compare against. Two decisions belong here and nowhere else:
   **freeze the operational definition at this tollgate** — after it, any change forces restating
   every prior number under both versions — and collect **20–25 subgroups** before treating control
   limits as established, since limits from fewer carry enough sampling error to signal on their own
   noise. Then check the goal against the baseline's limits: a target sitting inside normal variation
   can be "met" by a lucky week.
3. **Analyze.** Find and *verify* the root cause. Use fishbone/5 Whys (see
   `continuous-improvement-skills:root-cause-analysis`) to generate hypotheses, then **test them
   against data** rather than opinion — compare groups, look for correlation, run a significance test
   where warranted (see `data-analytics-bi-skills:statistical-inference`). Output: a cause confirmed
   by data, not asserted — and asserted is what you have until the cause made a prediction that
   could have failed. Stratify with **denominators beside the counts** (counts show where the volume
   is, rates show where the mechanism is), and don't stop at a location: "area B" is where to look
   next, not why. Compute what fraction of the charter gap the cause explains before advancing.
4. **Improve.** Generate candidate solutions that address the verified cause, select on impact vs.
   effort/risk, and **pilot** on a small scale before full rollout. Measure the pilot against the
   baseline. Keep it reversible, run it long enough that the novelty of being watched wears off, and
   watch the **denominator**: a fix that removes a category of work also removes it from the
   population you are measuring, so move the metric up to one the change cannot redefine. Output: a
   solution shown to move the metric on real data, with its projected effect on the top-line number
   stated before rollout.
5. **Control.** Lock the gain in: write the new **standard work**, set up ongoing monitoring (a control
   chart / SPC or a simple KPI with limits), define the response plan when it drifts, and hand off
   ownership to a **named individual and a deputy** — not a team, not a dashboard. Confirm the
   improvement holds: the 3σ limit rule catches large shifts instantly and moderate ones almost never,
   so arm run rules too (eight points on one side of the centerline, ~1 false alarm in 128 points, is
   usually what proves a real shift). Chart selection, limit formulas, the conditions under which a
   chart can tell you nothing, and the eleven-field control-plan contract are in
   `references/control-charts-and-control-plans.md`. Output: a control plan, a documented owned
   sustained result, and a closure statement saying plainly whether the goal was met, partially met,
   or missed.

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
the rigor is front-loaded where it prevents wasted work. One idea carries the Control phase and does
not appear anywhere in the phase names: **the distinction between variation the process always had
and variation something new introduced.** Without it every number invites a reaction, and reacting to
ordinary variation makes a stable process *worse* — Deming's tampering, where the correction is
uncorrelated with the deviation and adds its own. With it, most periods correctly require nothing,
which is exactly what makes the few that require something visible. That is why the control chart is
the *inference instrument* of a DMAIC project rather than its dashboard: it is the thing that lets you
say the gain held, instead of hoping it did. The payoff isn't just this fix; it's a process
whose variation you now understand and can keep in control.

## Common mistakes
- Jumping to a solution in Define → you skip the baseline and the cause. Hold the sequence.
- Skipping the measurement-system check → you improve against an untrustworthy ruler; the result is noise.
- Asserting the cause in Analyze instead of testing it → you fix the wrong thing. Confirm with data.
- Full rollout with no pilot → an expensive, hard-to-reverse mistake. Pilot small first.
- Declaring victory at Improve and skipping Control → the gain silently reverts. Standardize and monitor.
- Confusing a one-off shift with a real change → check against the baseline and normal variation.
- A charter with a fuzzy goal → you can't tell if you succeeded. Make the target measurable.
- A gain that appeared the day the definition or the extraction changed → that is definition drift, not
  improvement. Freeze the definition at the Measure tollgate and restate both versions if it moves.
- Chartering off one unusually bad month → regression to the mean improves it for you and takes the
  credit. Baseline across enough periods that the trigger is one point among many.
- Reacting to every point that looks bad → tampering adds variation to a stable process. Act on
  signals, not on values.
- A control plan owned by a team, a role, or a dashboard → nobody actually looks. Name a person, a
  deputy, and a review date.
- Renegotiating the goal at closure so the project "succeeded" → it devalues every future project's
  numbers. Report met, partially met, or missed, with the arithmetic.

## Tailor to your environment
Record your real project setup in `references/your-environment.md` (use `your-environment.private.md`,
git-ignored, if it names real customers, systems, or numbers). Capture your CTQ definitions and specs,
where you pull baseline data, your measurement-system and significance conventions, your pilot and
control-chart practice, and who owns tollgate sign-offs. Never commit real customer or transaction data —
keep it sanitized to structure.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/dmaic-problem-solving.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/phase-toolkit.md — per-phase deliverable contracts, tollgate questions with the answer
  that means stop, how DMAIC projects actually fail, and when DMAIC is the wrong machine
- references/worked-project.md — one improvement project carried end to end with real numbers:
  baseline and its stability, the definition change that moved the metric, the verified cause, the
  piloted fix, the control chart that proved it held, and the charter goal it missed
- references/control-charts-and-control-plans.md — common vs special cause, choosing the chart, limit
  formulas, when a chart can tell you nothing, run rules and their false-alarm cost, and the
  eleven-field control-plan contract
- references/your-environment.md — your CTQs, data sources, and sign-offs (add when supplied)
