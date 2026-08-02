---
name: ml-project-framing
description: >-
  Turns a business problem into a well-posed machine-learning task: names the decision, defines the
  target and the unit of prediction, lists only features available at prediction time, picks an
  evaluation metric tied to the decision, sets a baseline to beat, and runs leakage and feasibility
  checks before any model is built. Use when starting an ML project, scoping a prediction, or
  sanity-checking whether ML even fits the problem. Triggers: ML problem, machine learning problem,
  framing, frame the problem, target variable, prediction task, unit of prediction, baseline model,
  is this an ML problem, does ML fit, feasibility, well-posed.
---

# ML project framing

## When to use
- Starting a new ML/prediction effort (forecasting cash, flagging anomalies, scoring risk) and needing to scope it before touching data.
- Sanity-checking a stakeholder's "can we predict X?" request — deciding whether ML is the right tool at all.
- Reviewing an existing model that underperforms in production to find a framing flaw.
- Not for: choosing metrics and validation once the task is framed → see `machine-learning-skills:model-evaluation`. For profiling the data to test feasibility → see `data-analytics-bi-skills:exploratory-data-analysis`.

## Do it
1. **State the decision first, not the model.** Write one sentence: *who* acts, *what* action changes
   based on the prediction, *when* they act, and *what a wrong call costs*. If no action changes, stop —
   there is no ML problem here, only curiosity. The decision is what every later choice is judged against.
2. **Define the target precisely.** Name exactly what you predict, its type (a number → regression; a
   category → classification; an event over a window → time-to-event or a windowed label), the
   observation window, and how it is actually measured/labeled. "Predict a late payment" is not yet a
   target; "will invoice *i* be paid > 30 days past due, judged 45 days after issue" is.
3. **Fix the unit of prediction and the prediction time.** State what one row is (one account-day, one
   invoice, one customer-month) and the exact moment the prediction is made. Everything downstream —
   features, leakage, evaluation — is defined relative to this timestamp.
4. **List features available at prediction time.** For each candidate feature ask: *was this value
   knowable at the prediction timestamp?* Anything recorded later, or derived from the outcome, is
   leakage and must be dropped now, on paper, before it poisons results.
5. **Pick an evaluation metric tied to the decision.** Translate the cost of errors into a metric: an
   asymmetric cost (missing fraud ≫ a false alarm) argues for recall/precision at a threshold; an
   over- vs under-forecast asymmetry argues for a pinball/quantile loss. Map the metric back to dollars.
   Hand the details to `machine-learning-skills:model-evaluation`.
6. **Set the baseline you must beat.** Write down the naive rule: last value, seasonal-naive, the
   current human heuristic, or the majority class. The model's job is to beat *this*, not to score well
   in the abstract. If it can't, ship the baseline.
7. **Run feasibility and leakage checks.** Confirm there is enough labeled history, plausible signal in
   the features, a relationship stable enough to persist, and that the target is genuinely available for
   past periods. Use `data-analytics-bi-skills:exploratory-data-analysis` to test signal before committing.
8. **Write a one-page framing spec.** Capture decision, target, grain, prediction time, feature list,
   metric + baseline, data availability, and known risks. This page is the contract the project is
   built against — see `references/framing-spec.md` for the template.

## Why / learn
Most ML projects that fail do not fail on the algorithm — they fail on the frame. The two classic
killers are a **wrong target** (you optimized something that isn't the decision) and a **metric
disconnected from the decision** (you celebrated 0.92 AUC while the business kept losing money because
the cost of the errors you were making was never in the objective). Framing forces those choices into
the open *before* modeling, when they are cheap to fix. The discipline of naming the **prediction
time** is what makes leakage visible: leakage is simply using information that would not exist yet when
the prediction is really made, and you can only see it once you have fixed the moment of prediction. The
**baseline** exists because "good" is meaningless in isolation — a forecast is only worth deploying if
it beats the free naive rule, and a shocking share of models don't. Think of framing as writing the
problem down so precisely that the modeling becomes almost mechanical: a well-posed task is already
half-solved, and a badly posed one cannot be rescued by any amount of tuning.

## Common mistakes
- Jumping to "which algorithm" before naming the decision → you optimize the wrong thing. Decision first.
- A vague target ("predict churn") with no window or measurement rule → an unlearnable, unmeasurable label. Pin the window and how it's judged.
- Not fixing the prediction time → leakage hides in plain sight. Anchor every feature to "known at prediction time?"
- Choosing accuracy/R² by reflex → ignores error costs. Pick the metric from the decision's cost of being wrong.
- No baseline → you can't tell if the model helps. Write down the naive rule and beat it.
- Assuming data exists → the target isn't labeled historically, or a key feature is only known after the fact. Check availability early.

## Tailor to your environment
Record your real problem in `references/your-environment.md` (keep anything sensitive — actual figures,
account identifiers, sample rows — in `your-environment.private.md`, which is git-ignored; commit only
sanitized structure). Note the decision and its owner, the target and how you label it, your unit of
prediction and prediction cadence, the systems your features come from and when each becomes available,
your cost-of-error asymmetry, and the baseline you compare to. This skill then maps its generic steps
onto your specific problem, and hands the framed task to `machine-learning-skills:model-evaluation`.

## References
- references/framing-spec.md — the one-page framing template, with worked treasury examples and a leakage checklist
- references/your-environment.md — your decision, target, grain, features, and baseline (add when supplied)
