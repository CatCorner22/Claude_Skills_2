# Evals — data-analytics-bi-skills:survey-and-sampling-design

## 1. Positive trigger (should load the skill)
> "We want to survey our 1,200 employees about which internal processes waste their time.
> Help me with the survey design — the questionnaire, the sampling plan, and how many
> responses we need for a solid answer."

Expected: loads the skill; states the decision and target population first, names the
frame and its coverage gap; budgets the four total-survey-error sources before drafting
questions; picks a design (stratified by unit here) and says what it does to inference;
computes n in plain terms (worst-case p = 0.5, finite-population correction at N = 1,200,
then divides by the expected response rate for the invitation count); plans the
nonresponse follow-up (Dillman-style contact sequence, early-vs-late and
respondent-vs-frame diagnostics) BEFORE launch; audits questions for double-barreled,
leading, acquiescence, and order effects with a pretest; precommits the analysis plan and
hands the collected-data analysis to `data-analytics-bi-skills:statistical-inference`.

## 2. Near-miss (collected-data analysis guard)
> "We got 412 survey responses back and 61% said the new portal is confusing. What's the
> confidence interval on that, and is the difference between Operations and Sales
> statistically significant?"

Expected: `data-analytics-bi-skills:statistical-inference` owns the analysis of collected
sample data — confidence intervals, hypothesis tests, the sampling distribution. This
skill designs before data exists; if it loads on a pure analyze-my-results ask, the seam
is failing. (Loading both is acceptable only if the user also asks to critique the
original design.)

## 2b. Near-miss (qualitative-interview guard)
> "I need to interview our operations manager to understand how invoices actually get
> approved — she knows the real process but never wrote it down. How should I run that
> stakeholder interview?"

Expected: `collaboration-skills:disarming-elicitation` owns the one-on-one stakeholder
interview — adaptive, qualitative elicitation of tacit knowledge from a willing expert.
This skill fields a standardized instrument across a sample; a single expert conversation
is not a survey. If survey-and-sampling-design loads here, tighten the boundary.

## 3. Quality rubric
- **Does**: decision and population stated before instrument work; frame named with its
  coverage gap; error budget across all four sources; sampling design chosen with its
  inference consequence stated (convenience labeled as unquantifiable); sample size shown
  in plain terms with FPC and invitation math; nonresponse plan (contacts + diagnostics)
  designed pre-launch; every question audited against the wording checklist; pretest
  included; analysis plan precommitted with the statistical-inference handoff named.
- **Teaches**: total survey error as a budget with trade-offs (n only fixes sampling
  error); the Literary Digest told correctly per Squire 1988 — nonresponse, not just frame
  bias, was decisive, and sample size does not cure selection bias; 1948 as BOTH quota
  selection and stopping-too-early; Dillman's mature method as four-error reduction, not
  response-rate worship; why wording effects are measurement error with experimental
  evidence behind them (Schuman & Presser).
- **Stays honest**: no margin of error quoted for a convenience sample; provenance marks
  carried on external claims ([snippet-only] / [background — verify]); the Cochran
  citation and the "big data paradox" coda stay hedged; no invented response-rate or
  cost statistics; quota vs stratified never conflated; the skill never claims the
  downstream analysis it hands to statistical-inference.
