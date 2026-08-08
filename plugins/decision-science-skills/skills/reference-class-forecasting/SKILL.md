---
name: reference-class-forecasting
description: >-
  Applies the outside view (Kahneman/Tversky's planning fallacy; Flyvbjerg's reference-class
  method) to discipline any material estimate: identify a reference class of comparable past
  cases, establish its outcome distribution, anchor on that base rate, adjust only with explicit
  written justification — or apply a required uplift at a chosen certainty level (P80-style) —
  then log the prediction and score it against actuals. Counters optimism bias and strategic
  misrepresentation, and guards against tampering (reworking the rule after every miss). Turns
  an existing variance history, such as per-driver MAPE and signed bias, into next-cycle
  base-rate anchors; it feeds estimation loops, never builds the models. Use when an estimate
  rests only on its own story or a plan looks optimistic. Triggers: outside view, reference
  class, base-rate anchor, base rate, optimism bias, planning fallacy, how long do projects
  like this actually take, uplift the estimate.
---

# Reference-class forecasting (the outside view)

Kahneman and Tversky distinguished the **inside view** — estimating from the specifics of the case
in front of you — from the **outside view** — asking how cases *like this one* actually turned
out. The inside view produces the planning fallacy; the outside view corrects it. Bent Flyvbjerg
operationalized the correction as reference-class forecasting (formalized in a 2006 PMI paper),
and UK government appraisal guidance adopted it as mandatory optimism-bias uplifts (HM Treasury
Green Book; Department for Transport uplift tables) [snippet-only].

## When to use
- A material estimate that so far rests only on its own story: project cost or duration, a
  feature-delivery date, a next-cycle number for a cash driver.
- Turning a variance history you already keep into next-cycle anchors. The canonical mount:
  `cash-management-skills:cash-forecasting` already measures per-driver MAPE and signed bias (its
  `references/forecast-model-and-accuracy.md` defines both) — that history IS a ready-made
  reference class. This skill closes a loop the library already runs: per-driver base-rate anchors
  and uplifts for tuition receipts, payroll, grant drawdowns.
- Software/project estimation from a delivery history (e.g., a feature-delivery reference class
  for an app build).
- Sanity-checking someone else's optimistic plan or business case.
- Not for: building the estimate's underlying model itself — direct-method cash projections belong
  to `cash-management-skills:cash-forecasting`, and statistical/ML series models to
  `machine-learning-skills:time-series-forecasting`. This skill FEEDS those loops with base rates
  and uplifts; it never replaces them.

## Do it
Full class-selection heuristics, uplift math, and a worked cash-driver example are in
`references/outside-view-method.md`; calibration and the tampering guard are in
`references/calibration-and-tampering.md`.

1. **Identify the reference class** — comparable past cases, broad enough for statistics, narrow
   enough to stay comparable. The assistant proposes 2–3 candidate classes with their trade-offs
   (this is the hard judgment step); the **human ratifies the choice** — everything downstream
   inherits it. Freeze the class before looking at outcomes.
2. **Establish the class's outcome distribution.** Express each past case as a comparable outcome
   measure — cost overrun %, actual/estimate ratio, schedule slip %, signed error — and compute
   empirical percentiles (P10/P50/P80/P90), not just the mean. The assistant computes this
   directly from the user's own variance history when one exists.
3. **Anchor on the base rate.** Position the current case in that distribution. The naive answer
   is the class P50 applied to the raw estimate — write that number down *before* any adjustment.
4. **Adjust only with explicit written justification.** Either (a) a short inside-vs-outside memo
   stating why this case sits above or below the class, which the assistant drafts and the human
   signs; or (b) skip case-by-case adjustment and apply a **required uplift at a chosen certainty
   level** — e.g., a P80 uplift in the style of the Department for Transport tables: the uplift
   that 80% of past cases would not have exceeded. Pick the certainty level in the direction the
   risk hurts (uplift disbursements and costs; haircut receipts).
5. **Log the prediction and score it later** (decision-journal practice): the number, the
   confidence level or range, the class used, the reasoning, and a review date. When actuals land,
   score it — Brier-style for probabilities, error percentile for point estimates — and feed the
   outcome back into the class.
6. **Guard against tampering before touching any rule.** Adjusting the estimate rule after every
   single-period miss is Deming funnel Rule 2 and roughly doubles variance [snippet-only]. First
   test whether the miss is common-cause (inside the class's normal spread) — if so, leave the
   rule alone; only a special-cause signal (outside the spread, or a run of same-signed misses)
   justifies a diagnosed, one-time rule change.

**Division of labor (the human gate).** The assistant proposes candidate reference classes,
computes the distribution and percentile placement from the user's own history, and drafts the
reconciliation memo. The human ratifies the class choice and owns the final number — the class is
a judgment call that determines the whole answer, so it is never the assistant's to make alone.

## Why / learn
The planning fallacy is not carelessness — it is how the inside view works. Building an estimate
from the case's specifics means chaining best-case steps into a coherent story, and stories
under-represent the ways things go sideways because those ways are, individually, unlikely and,
collectively, near-certain. The outside view sidesteps the story entirely: distributions of past
outcomes already contain every derailment that actually happened, including the kinds nobody
anticipated. That is why the base-rate anchor comes *before* case specifics, and why step 3 writes
the unadjusted number down — once the anchor exists, adjustments must argue against it in writing.

Flyvbjerg's second finding is that not all optimism is cognitive: estimates compete for approval,
so there is **strategic misrepresentation** — the incentive to present the winning number rather
than the likely one. The outside view is the countermeasure for both at once, because a base rate
computed from what actually happened cannot be argued down by a better story [snippet-only]. The
same logic makes written adjustment discipline load-bearing: adjustment is the door bias walks
back through, so it is either justified on paper or replaced by a fixed uplift at a stated
certainty level.

Logging and scoring close the loop. Calibration improves only against a record — granular
probabilities, small frequent updates, and scoring are the practices that separate strong
forecasters from the rest (Tetlock's superforecasting research) [snippet-only]. And the tampering
guard protects the record from you: reacting to noise adds noise, so a miss must first be
classified common-cause vs. special-cause before it is allowed to change anything.

## Common mistakes
- "No past case is like ours" → nothing is unique enough to escape a base rate; widen the class
  until it has statistics, then put the differences in the adjustment memo.
- Choosing the class after seeing which class gives the nicest answer → freeze the class first;
  changing it afterward is anchoring in reverse.
- Anchoring on the mean of a skewed distribution → overruns are fat-tailed; use percentiles at a
  stated certainty level.
- Free-hand adjustments to the anchor → every adjustment written and signed, or none (fixed uplift).
- Uplifting in the comfortable direction → uplift costs/disbursements, haircut receipts; pick the
  percentile on the side where the miss hurts.
- Re-tuning the rule after every miss → funnel Rule 2 doubles variance; test common-cause first.
- Logging predictions but never scoring them → set the review date when logging; an unscored
  journal is a diary.
- Using this skill to build the projection itself → the model belongs to
  `cash-management-skills:cash-forecasting` or `machine-learning-skills:time-series-forecasting`;
  this skill supplies their anchors and uplifts.

## Tailor to your environment
Record your setup in `references/your-environment.md`: where each variance history lives, the
drivers or project types you estimate repeatedly, your house certainty level (e.g., P80 for
disbursements, P20 for receipts), where the decision journal is kept, and your review cadence.
Keep committed content structural — real figures, counterparty names, or client data belong in
`your-environment.private.md` (git-ignored), never in a committed file.

## References
- references/outside-view-method.md — class-selection heuristics, distribution and uplift math,
  and a worked cash-driver example from a MAPE/bias history
- references/calibration-and-tampering.md — Tetlock calibration practices, the decision-journal
  template, and Deming's funnel rules as the tampering guard
- references/your-environment.md — your variance histories, drivers, certainty conventions, and journal
