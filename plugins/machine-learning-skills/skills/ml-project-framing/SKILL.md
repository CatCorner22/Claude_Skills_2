---
name: ml-project-framing
description: >-
  Turns a business problem into a well-posed machine-learning task before any model is built —
  names the decision and the cost of a wrong call, defines the target (type, window, labeling
  rule), fixes the unit of prediction and the prediction time, lists only features knowable at
  that moment (the on-paper leakage check), picks a metric tied to those costs,
  sets the naive baseline the model must beat, runs feasibility checks, and writes a one-page
  framing spec — and is willing to conclude ML does not fit or the baseline should ship. Use
  when starting an ML or prediction project, scoping a "can we predict X?" request, deciding
  whether ML fits at all, or diagnosing a model that underperforms from a framing flaw. Triggers:
  ML problem, machine learning problem, framing, frame the problem, target variable,
  prediction task, unit of prediction, baseline model, is this an ML problem, does ML fit,
  feasibility, well-posed, can we predict, framing spec, scope an ML project.
metadata:
  version: "1.2.0"
  source: >-
    The framing discipline descends from CRISP-DM's Business Understanding phase (the
    late-1990s NCR/DaimlerChrysler/SPSS/OHRA consortium process model), verified via
    web-search snippets — claims so sourced are marked [snippet-only] in the reference.
---

# ML project framing

## When to use
- Starting a new ML/prediction effort — forecasting demand or cash, flagging anomalies,
  scoring risk, prioritizing a queue of cases — and needing to scope it before touching data.
- Sanity-checking a stakeholder's "can we predict X?" request — deciding whether ML is the right tool at all.
- Reviewing an existing model that underperforms in production to find a framing flaw.
- Not for: choosing metrics and validation once the task is framed → see
  `machine-learning-skills:model-evaluation`. For profiling the data to test feasibility → see
  `data-analytics-bi-skills:exploratory-data-analysis`.
- Not for: architecting a bespoke or fine-tuned language model once framing says a generic one
  will not do — the prompting/RAG/PEFT/full-tune ladder, data budget, and eval harness → see
  `machine-learning-skills:bespoke-llm-architect`.

## Do it
1. **State the decision first, not the model.** Write one sentence: *who* acts, *what* action changes
   based on the prediction, *when* they act, and *what a wrong call costs*. If no action changes, stop —
   there is no ML problem here, only curiosity. The decision is what every later choice is judged against.
2. **Define the target precisely.** Name exactly what you predict, its type (a number → regression; a
   category → classification; an event over a window → time-to-event or a windowed label), the
   observation window, and how it is actually measured/labeled. "Predict a late payment" is not yet a
   target; "will invoice *i* be paid > 30 days past due — on net-30 terms, paid after issue + 60 —
   judged at issue + 75, still-unpaid counted late" is. The type
   routes the eventual build: number/category → `machine-learning-skills:supervised-modeling`; a
   series over time → `machine-learning-skills:time-series-forecasting`; unusual-instance detection
   with scarce labels → `machine-learning-skills:anomaly-detection`. If the label comes from human
   judgment (reviewers grading cases), check the judges agree before trusting the labels —
   `continuous-improvement-skills:measurement-systems-analysis` measures that agreement.
3. **Fix the unit of prediction and the prediction time.** State what one row is (one account-day, one
   invoice, one customer-month, one ticket) and the exact moment the prediction is made. Everything
   downstream — features, leakage, evaluation — is defined relative to this timestamp.
4. **List features available at prediction time.** For each candidate feature ask: *was this value
   knowable at the prediction timestamp?* Anything recorded later, or derived from the outcome, is
   leakage and must be dropped now, on paper, before it poisons results. The surviving list is the
   input contract for `machine-learning-skills:feature-engineering`, which owns the encoding,
   scaling, and fit-on-train-only pipeline once building starts.
5. **Pick an evaluation metric tied to the decision.** Translate the cost of errors into a metric: an
   asymmetric cost (missing fraud ≫ a false alarm) argues for recall/precision at a threshold; an
   over- vs under-forecast asymmetry argues for a pinball/quantile loss. Map the metric back to money
   or workload. Hand the details to `machine-learning-skills:model-evaluation`.
6. **Set the baseline you must beat.** Write down the naive rule: last value, seasonal-naive, the
   current human heuristic, or the majority class. The model's job is to beat *this*, not to score well
   in the abstract. If it can't, ship the baseline. For what improvement is *realistic to promise*,
   take the outside view — `decision-science-skills:reference-class-forecasting` anchors the pitch on
   how efforts like this actually perform rather than on the demo's optimism.
7. **Run feasibility and leakage checks.** Confirm there is enough labeled history, plausible signal in
   the features, a relationship stable enough to persist, and that the target is genuinely available for
   past periods. Use `data-analytics-bi-skills:exploratory-data-analysis` to test signal before committing.
8. **Write a one-page framing spec.** Capture decision, target, grain, prediction time, feature list,
   metric + baseline, data availability, and known risks. This page is the contract the project is
   built against — see `references/framing-spec.md` for the template and worked examples across
   analyst, attorney, operations, and developer settings.

## Why / learn
Most ML projects that fail do not fail on the algorithm — they fail on the frame. The two classic
killers are a **wrong target** (you optimized something that isn't the decision) and a **metric
disconnected from the decision** (you celebrated 0.92 AUC while the business kept losing money because
the cost of the errors you were making was never in the objective). Framing forces those choices into
the open *before* modeling, when they are cheap to fix — the same insight the CRISP-DM process model
institutionalized by putting a Business Understanding phase before any data work [snippet-only]. The
discipline of naming the **prediction time** is what makes leakage visible: leakage is simply using
information that would not exist yet when the prediction is really made, and you can only see it once
you have fixed the moment of prediction. The **baseline** exists because "good" is meaningless in
isolation — a forecast is only worth deploying if it beats the free naive rule, and models
routinely don't. Think of framing as writing the problem down so precisely that the modeling becomes
almost mechanical: a well-posed task is already half-solved, and a badly posed one cannot be rescued
by any amount of tuning.

## Common mistakes
- Jumping to "which algorithm" before naming the decision → you optimize the wrong thing. Decision first.
- A vague target ("predict churn") with no window or measurement rule → an unlearnable, unmeasurable label. Pin the window and how it's judged.
- Not fixing the prediction time → leakage hides in plain sight. Anchor every feature to "known at prediction time?"
- Choosing accuracy/R² by reflex → ignores error costs. Pick the metric from the decision's cost of being wrong.
- No baseline → you can't tell if the model helps. Write down the naive rule and beat it.
- Assuming data exists → the target isn't labeled historically, or a key feature is only known after the fact. Check availability early.
- Trusting human-judged labels without checking agreement → a label two reviewers assign differently is noise, not truth. Measure agreement first.

## Tailor to your environment
Wire in your current role here — the framing method is domain-neutral and attaches to whatever
predictions matter wherever you work next: an analyst's payment risk, an attorney's matter-intake
triage, an ops manager's volume forecast, a developer's incident scoring. Record your real problem
in `references/your-environment.md` (keep anything sensitive — actual figures, identifiers, sample
rows — in `your-environment.private.md`, which is git-ignored; commit only sanitized structure).
Note the decision and its owner, the target and how you label it, your unit of prediction and
prediction cadence, the systems your features come from and when each becomes available, your
cost-of-error asymmetry, and the baseline you compare to. This skill then maps its generic steps
onto your specific problem and hands the framed task to `machine-learning-skills:model-evaluation`.

## References
- references/framing-spec.md — the one-page framing template, worked examples across four
  settings (analyst, attorney, operations, developer), the leakage checklist, the baseline
  catalog, and the "is this even an ML problem?" filter
- references/your-environment.md — your decision, target, grain, features, and baseline (fill in)
