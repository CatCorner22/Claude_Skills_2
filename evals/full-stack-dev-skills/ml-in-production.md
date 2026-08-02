# Evals — full-stack-dev-skills:ml-in-production

## 1. Positive trigger (should load the skill)
> "Our churn model works great in the notebook — put it into the app. Product wants scores
> on the customer page, and I'm worried it'll rot silently once it's live."

Expected: skill loads; asks whether scores are needed per-request or can be batch
(customer-page display → batch table, most likely); packages the whole pipeline as a
versioned artifact; shares feature code between training and serving; validated endpoint or
batch job with prediction logging from day one; drift monitoring and written
retrain/rollback triggers; shadow/canary for the next version.

## 2. Near-miss (should NOT load this skill)
> "Which model should I train for churn — logistic regression or gradient boosting — and
> how do I evaluate it?"

Expected: modeling/evaluation — `machine-learning-skills:supervised-modeling` +
`model-evaluation`. If this skill loads, sharpen the deployment framing.

## 3. Quality rubric
A good response:
- **Does the task:** serving pattern chosen by latency need, versioned artifact, validated
  inputs, version in responses, logging + drift + triggers set up.
- **Teaches:** models as dependencies-on-the-past that degrade untouched, training/serving
  skew as the failure evaluation can't catch, batch-first economics, product-metric
  promotion.
- **Safe:** no bare-estimator persistence, no per-request model loading, no promotion on
  validation metrics alone, sensitive inputs hashed in logs.
