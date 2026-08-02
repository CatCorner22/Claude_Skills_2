# Evals — metacognition-skills:dynamic-analysis-engine

## 1. Positive trigger (should load the skill)
> "Our bank fees jumped 40% this quarter and I don't know why. Here's the fee export —
> dig into what's driving it. Could be volume, could be pricing, could be a new service."

Expected: skill loads; characterizes the data; logs the three candidate hypotheses (volume,
price, mix/new service) plus rivals; tests each with executed code (volume × unit price
decomposition); prunes and deepens adaptively; reports the driver with calibrated confidence
and limitations. May pull in `banking-skills:bank-fee-analysis` for domain specifics.

## 2. Near-miss (should NOT load this skill)
> "I just got this new dataset — give me a quick profile: columns, types, missing values."

Expected: a first-pass profile → `data-analytics-bi-skills:exploratory-data-analysis`.
If this skill loads for a plain profiling request, tighten the description.

## 3. Quality rubric
A good response:
- **Does the task:** explicit hypothesis log with rivals, executable tests, adaptive depth,
  and a synthesis with confidence + limitations + alternatives.
- **Teaches:** explains why hypotheses are written before testing and why depth follows
  information value.
- **Safe:** runs code rather than mental arithmetic; never presents a single unqualified
  number as the answer; states what evidence would change the conclusion.
