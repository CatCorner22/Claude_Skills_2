# Evals — machine-learning-skills:ml-project-framing

## 1. Positive trigger (should load the skill)
> "Finance wants us to 'use ML to predict which vendor payments will be late.' Before I build anything,
> how should I frame this as a proper prediction problem — what's the target, and how do I know it's
> even feasible?"

Expected: skill loads; names the decision and its cost; defines a precise target with an observation
window; fixes the unit of prediction (one invoice/payment) and the prediction time; lists only features
known at that time; picks a decision-tied metric and a baseline to beat; runs feasibility/leakage checks;
produces a one-page framing spec and hands metric details to `model-evaluation`.

## 2. Near-miss (should NOT load this skill)
> "My random forest is overfitting — train accuracy is 0.99 but validation is 0.71. How do I fix it?"

Expected: this is validation/overfitting diagnosis on an already-framed, already-built model. The
`machine-learning-skills:model-evaluation` (and `supervised-modeling`) skills should handle it. If this
framing skill loads, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** states the decision first, defines target + type + window, fixes grain and prediction
  time, lists prediction-time features, chooses a metric tied to error costs, sets a baseline, and checks
  feasibility/leakage — ideally as a one-page spec.
- **Teaches:** explains *why* most ML failures are framing failures (wrong target, metric disconnected
  from the decision) and why fixing the prediction time is what makes leakage visible — not just a checklist.
- **Safe:** is willing to conclude "this isn't an ML problem" or "ship the baseline" when the decision,
  labels, or signal don't justify a model; never skips the baseline.
