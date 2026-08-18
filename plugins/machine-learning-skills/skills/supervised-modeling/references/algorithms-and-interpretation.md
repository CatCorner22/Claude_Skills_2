# Algorithms, defaults, and interpretation (reference)

## Contents
- Model-family cheat-sheet
- Sensible starting hyperparameters — and the reasoning behind each number
- Worked example: baseline → ensemble on one dataset, and the decision to stop
- When a linear model genuinely beats a tree ensemble — and how you would know
- Class-imbalance tactics, and the thresholds that pick between them
- Interpretation — what each quantity licenses, and what it is NOT evidence of
- Failure envelopes — where this method stops working, and what you see
- Deliverable contract — the model summary, item by item

## Model-family cheat-sheet
| Family | Strengths | Watch out for | Reach for when |
|---|---|---|---|
| **Linear / logistic regression** | Fast, interpretable, hard to overfit, extrapolates | Assumes additive, monotone effects; needs encoding/scaling | Always — as the baseline; when explanation matters |
| **Regularized linear (ridge/lasso/elastic-net)** | Controls overfit; lasso selects features | Still linear in the features you give it | Many features, collinearity, want sparsity |
| **Random forest** | Robust, low tuning, captures interactions, little preprocessing | Larger models; biased default importances | A strong nonlinear baseline with minimal fuss |
| **Gradient boosting (XGBoost/LightGBM/CatBoost)** | Top tabular accuracy | Overfits without care; more tuning | You need the best accuracy on tabular data |

Trees split the feature space into boxes: they capture interactions for free and need little scaling, but
they **cannot extrapolate** beyond the training range — a forecast of a value larger than anything seen is
impossible. Linear models extrapolate but assume the straight-line (or log-odds-linear) relationship holds.

## Sensible starting hyperparameters — and the reasoning behind each number

Start here, then tune only what the validation curve says is worth tuning. Every number below is a
starting point with a stated mechanism, not a tuned optimum; the point of stating the mechanism is that
you can tell when your data breaks it.

### Linear / logistic
| Setting | Start at | Why this, and what you see when it is wrong |
|---|---|---|
| Feature scaling | Standardize before any penalty | The penalty acts on the coefficient, and a coefficient is an effect *per unit*, so the units decide who gets shrunk. Re-express a column in 100× larger units (dollars → cents) and its coefficient is 100× smaller, so L1 penalizes it 100× *less* and L2 10,000× less — the features punished hardest are the small-scale ones, whatever their signal. Symptom of skipping it: a feature you know matters drops out of the lasso path while a big-numbered irrelevant one survives, and re-expressing one column in different units changes the selected set |
| Penalty | L2 (ridge) | Keeps correlated features together with shared, stable coefficients |
| L1 (lasso) | when you need a sparse set | L1 picks *one* of a correlated pair arbitrarily, and the pick flips between bootstrap resamples |
| Strength grid | log-spaced, ≥ 6 decades (e.g. C from 1e-4 to 1e2, two points per decade) | The optimum moves with sample size and feature scaling, so a narrow grid usually misses it. Hard rule: the CV curve must have an **interior** minimum — if the best value sits at an endpoint, the grid is too small, extend it and refit |

### Random forest
| Setting | Start at | Why this, and what you see when it is wrong |
|---|---|---|
| `n_estimators` | 300–500 | Accuracy rises then flattens; more trees never hurt accuracy, only time. Measure the knee once on OOB score, then stop thinking about it |
| `max_features` | sqrt(p) classification, p/3 regression | Decorrelates the trees, which is where the ensemble's variance reduction comes from. **Raise it when few features are informative**: with p = 26 and only 4 informative, the chance a 5-feature draw misses all four is C(22,5)/C(26,5): 26,334/65,780 = 0.40 — two splits in five see nothing useful |
| `min_samples_leaf` | 1–5 regression, 20–40 noisy classification | The forest averages many noisy trees, so pure leaves are survivable; a floor buys variance reduction cheaply on noisy data. Diagnose by the train-vs-validation gap, not by taste (see the ladder below, rows 2→3) |

### Gradient boosting
| Setting | Start at | Why this, and what you see when it is wrong |
|---|---|---|
| `learning_rate` | 0.05 | Halving it roughly doubles the rounds needed for the same fit; below ~0.01 the extra compute rarely buys measurable accuracy |
| `n_estimators` | large, chosen by **early stopping** (patience ≈ 50 rounds) | Never grid-search rate and rounds together — fix the rate and let early stopping pick the rounds, or you spend the whole budget re-discovering their product |
| `num_leaves` (LightGBM) | 31, with `max_depth` as a cap | LightGBM grows **leaf-wise**, so a depth cap alone does not bound complexity. Keep `num_leaves` ≤ 2^`max_depth` — depth 6 caps at 64 |
| `min_data_in_leaf` | ≈ 10 / (positive rate) | Boosting fits residuals greedily, so a leaf holding one positive emits a huge log-odds step. At a 3% positive rate a 20-row leaf expects 0.6 positives: 20 × 0.03 = 0.6 — its value is decided by whether one positive happened to land in it. A 300-row floor expects 9: 300 × 0.03 = 9 |
| `min_child_weight` (XGBoost) | derive it, don't copy it | This is a sum of **hessians**, not a row count. Under logloss the per-row hessian is p(1−p), where the model already predicts p̂ = 0.03 the per-row hessian is 0.0291, so the default of 1 corresponds to 34 rows: 1/0.0291 = 34 — but where p̂ = 0.5 it is 4 rows: 1/0.25 = 4. The same setting means different things in different regions |
| `subsample` / `colsample_bytree` | 0.8 / 0.8 | Decorrelates successive stages; acts as a regularizer at no accuracy cost. LightGBM gotcha: `bagging_fraction` does nothing until `bagging_freq` > 0 |

**Search budget.** Past three hyperparameters, prefer **random search over ~40–60 trials** to a grid at the
same cost: a grid spends its trials re-sampling dimensions the metric is flat in, and a boosting metric is
flat in most of them. Spend the saved budget on repeated CV instead — knowing your noise band is worth more
than one more trial.

## Worked example: baseline → ensemble on one dataset, and the decision to stop

*This run is a fully worked illustration on a synthetic tabular problem — it is internally consistent so
that you can follow every decision, and it is not a measurement of any real dataset. Your numbers will
differ; the structure of the decisions should not.*

**Setup.** Binary classification: will an account cancel within 60 days of the as-of date. 48,000 account-
months, 3.0% positive. 26 features (18 numeric, 8 categorical). Split by time: train 33,600 / validation
7,200 / test 7,200, so the test set holds 216 positives: 7,200 × 0.03 = 216. Headline metric: **PR-AUC**,
because positives are scarce and the baseline PR-AUC is the positive rate itself, 0.030. Validation scores are the
mean ± standard deviation across 5 stratified folds of the training block.

**Write the stop rule before the first fit.** Keep a rung only when its validation gain over the *best kept*
model exceeds `max(across-fold sd, the smallest gain that would change a decision)`. A gain inside the fold
sd is not evidence. A gain that is real but smaller than the decision threshold is real and useless.

| # | Model | train PR-AUC | val PR-AUC (5-fold) | Δ vs last kept | Verdict |
|---|---|---|---|---|---|
| 0 | Majority class | — | 0.030 | — | Reference floor = prevalence |
| 1 | Logistic, standardized, L2 (C by CV) | 0.181 | 0.171 ± 0.012 | +0.141 | Keep — the model to beat |
| 2 | Random forest, defaults, unlimited depth | 0.982 | 0.184 ± 0.019 | +0.013 | Fix the fit before judging it |
| 3 | Random forest, `min_samples_leaf` 40 | 0.336 | 0.207 ± 0.015 | +0.036 | Keep |
| 4 | LightGBM, lr 0.05, early stop at 640 rounds | 0.402 | 0.246 ± 0.014 | +0.039 | Keep |
| 5 | LightGBM, 60-trial random search | 0.418 | 0.259 ± 0.016 | +0.013 | Tie — see below |
| 6 | Stack: LR + RF + LGBM, logistic meta-learner | 0.455 | 0.251 ± 0.017 | +0.005 | Stop |

How each verdict was reached, in order:

- **Row 1 beats row 0** by: 0.171 − 0.030 = 0.141 — roughly twelve times the fold sd. The logistic model
  is real; everything after it has to beat *this*, not the majority class.
- **Row 2 is not a result, it is a symptom.** Train 0.982 against validation 0.184 is a memorized forest.
  Reading its +0.013 as "the forest barely helps" would be the wrong conclusion from the wrong fit — the
  gap says the model is untuned, not that the family is weak. Raise the leaf floor and re-ask.
- **Row 3, with the leaf floor at 40**, drops train to 0.336 and lifts validation to 0.207. Gain over the
  last kept rung (row 1): 0.207 − 0.171 = 0.036 — well past the sd of 0.015. Keep.
- **Row 4** over row 3: 0.246 − 0.207 = 0.039 — keep. Note the honest bookkeeping: early stopping chose
  640 rounds on a validation fold, so those rounds are a *fitted* quantity and the fold used to choose them
  is no longer clean for scoring.
- **Row 5 is the interesting one.** Gain of the 60-trial search over row 4: 0.259 − 0.246 = 0.013.
  Against a fold sd of 0.016 the ratio is: 0.013/0.016 = 0.81 — under 1, so the stop rule calls this a tie, not
  an improvement. Repeating the CV (5 repeats of 5 folds) shrinks the sd of the *mean* by at most the
  square root of the repeat count: √5 = 2.24. And it shrinks only the resampling component — the
  finite-sample component does not move. If the repeat still leaves the two inside each other's band,
  declare the tie and choose on cost, not on the third decimal.
- **Row 6** over row 4: 0.251 − 0.246 = 0.005 — while tripling the number of models to serve, retrain, and
  monitor. Stop. A stack that is inside the noise band of its own best member is a maintenance burden
  wearing an accuracy costume.

**Shipped: row 4** — the untuned-but-sane LightGBM, with row 5's configuration recorded in the summary as
*measured, not different*. This is the ordinary outcome of a careful ladder, and it is worth saying plainly:
most of the total gain (0.141 of 0.216, about 65%) came from the first rung, the interpretable one.
Verify: 0.246 − 0.030 = 0.216; 0.141/0.216 = 0.65.

**Turning PR-AUC into a decision.** PR-AUC ranks models; it does not run anything. The team can work
**150 accounts a month**, so the threshold was chosen on validation to emit ~150 alerts per 7,200 accounts,
frozen, and the test set scored once at it:

| Model at the 150-alert budget | TP | FP | Precision | Recall (n = 216) | Lift vs random |
|---|---|---|---|---|---|
| Logistic (row 1) | 44 | 106 | 44/150 = 29.3% | 44/216 = 20.4% | 9.8 |
| LightGBM (row 4) | 62 | 88 | 62/150 = 41.3% | 62/216 = 28.7% | 13.8 |

Random selection of 150 accounts is expected to contain 4.5 positives: 150 × 0.03 = 4.5. Lift figures:
44/4.5 = 9.8; 62/4.5 = 13.8. Test PR-AUC came in at 0.238 against the validation 0.246 —
the small drop is what an honest single scoring of a held-out block usually looks like.

**Is the 44 → 62 difference real?** Two ways to ask, and only one of them is right:

- *The wrong instrument.* Recall standard errors on 216 positives, by the proportion formula in
  `machine-learning-skills:model-evaluation`. Ensemble: √(0.287 × 0.713 / 216) = 0.031 — a 95% band of
  roughly [0.227, 0.347]. Logistic: √(0.204 × 0.796 / 216) = 0.0274 — band roughly [0.150, 0.257].
  **These bands overlap** — and concluding "no significant difference" from that overlap would be a
  mistake, because marginal intervals ignore that both models scored the *same* rows.
- *The right instrument.* Compare them paired. Of the 216 positives, the ensemble caught 23 that the
  logistic model missed and missed 5 that it caught. Discordant difference: 23 − 5 = 18. Headline
  difference: 62 − 44 = 18. They reconcile, as they must. McNemar's statistic on the discordant pairs:
  (23 − 5)^2/(23 + 5) = 324/28 = 11.6 — above the 1-degree-of-freedom chi-square critical value of 10.83
  for p = 0.001. The difference is real.

The lesson to carry out of this example: **the paired comparison is the one that has power**, and the size
of the effect it confirms — 18 additional true churners surfaced per 7,200 accounts per month — is the
number the ship/no-ship conversation is actually about. At a save rate of 25% that is 4.5 retained
accounts a month: 18 × 0.25 = 4.5. Whether 4.5 is worth a gradient-boosting model in production is a business question, and
it is the right question.

## When a linear model genuinely beats a tree ensemble — and how you would know

Five conditions where linear is not the polite starting point but the better model:

1. **Few events per candidate feature.** The widely used rule of thumb is ~10 events per candidate
   predictor (contested in the methods literature, and worth treating as an order-of-magnitude signal
   rather than a bright line). Worked — 300 rows at 12% positive gives 36 positives: 300 × 0.12 = 36.
   Events per candidate feature: 36/25 = 1.44. Fit a penalized linear model, not a booster.
   *What you see if you ignore it:* train AUC near 1.0, cross-validated AUC barely off 0.50 with a fold sd
   around ±0.08, and a top-feature list that reshuffles completely between folds.
2. **Extrapolation is required.** If deployment will present values above the training maximum, a tree
   returns the constant from its last split forever. *What you see:* predictions pinned flat at the top of
   the training range, residuals fanning out at the extremes. A linear model is not merely better here —
   it is the only one that can move.
3. **Wide, sparse inputs.** Thousands of one-hot or text columns, each nonzero in a small fraction of rows.
   A tree must find a split that isolates a rare column; L2 logistic sums thousands of weak signals
   additively and does it cheaply. Rough trigger: p approaching or exceeding n, or a median column density
   under ~1%.
4. **Low signal-to-noise with additive structure.** When the achievable R² is small, variance dominates the
   error and the higher-bias model wins. A booster given mostly noise will find the noise.
5. **The explanation is the product** — an adverse-action reason code, a rule a clinician overrides, a
   model an auditor will make you defend line by line. Here a 0.01 PR-AUC deficit is not a deficit.

**How you would know — a three-test protocol** that turns the question into evidence:

- **Same-CV comparison.** Score both under identical folds. If the ensemble's mean gain sits inside the
  fold sd, the linear model wins on parsimony — cheaper to serve, explain, monitor, and retrain.
- **Read the ensemble's partial dependence.** If the curves are monotone and close to straight, the
  ensemble is spending its capacity approximating lines with staircases; the linear model with the right
  transform will match it.
- **Hand the ensemble's finding to the linear model.** Add the interaction or the spline the partial-
  dependence plot revealed and refit the linear model. If the gap closes, ship the linear model — and you
  now know *what* the nonlinearity was, which is strictly more than the ensemble told you. If the gap does
  not close, the ensemble is exploiting structure you cannot yet name. Keep it, and say so in the summary
  rather than pretending you understand it.

## Class-imbalance tactics, and the thresholds that pick between them

The governing quantity is the **absolute count of minority events**, not the ratio. 1% of 5,000,000 is an
easy problem; 1% of 3,000 is a sample-size problem wearing an imbalance costume.

| Minority events (train) | What is actually broken | First move |
|---|---|---|
| > ~5,000 | Nothing structural — only your metric and your threshold | Leave the data alone. Pick the threshold on cost; report PR-AUC and precision at the operating point |
| ~500–5,000 | The loss under-weights the minority in shallow models and early boosting rounds | `class_weight='balanced'` / `scale_pos_weight`; stratified folds; threshold by cost or alert budget |
| ~50–500 | Variance: model ranking and threshold both wobble between resamples | Class weights + **repeated** stratified CV; prefer the simpler model; any resampling strictly inside folds; report the band, not the point |
| < ~50 | The estimate, not the model | Do not compare models at this size. Widen the label window, aggregate to a coarser entity, reframe as ranking or `machine-learning-skills:anomaly-detection`, or go collect positives |

The 50-event floor has a derivation, not a vibe. At its widest, recall measured on 50 positives has a
standard error of: √(0.25/50) = 0.071 — a 95% band about ±14 points wide, wider than any improvement you
would plausibly be choosing between. Halving that band takes four times the positives.

**Choosing among the tactics.**

- **Class weights are the first move** because they are one argument, change no data, and cannot leak.
  What they do: multiply the minority's contribution to the loss, which changes which splits get taken in
  shallow or early trees and moves where the default 0.5 threshold sits. What they do not do: create
  information. Expect a small or zero change in PR-AUC and a large change in the raw scores.
- **Threshold tuning is not an alternative to anything** — it is mandatory, free, and belongs to
  `machine-learning-skills:model-evaluation`. Doing it well makes most imbalance "problems" evaporate.
- **Reach for resampling only for a specific symptom:** with weights already on, the model still scores
  positives inside the bulk of the negative distribution at every threshold. Preconditions for SMOTE to be
  defensible: enough minority rows that a k = 5 neighbourhood is genuinely local. Interpolating between two
  minority points that are far apart manufactures a positive in a region where no positive lives, and the
  model dutifully learns a boundary around it. And it goes **inside** the CV fold — resampling before the
  split leaks synthetic relatives of validation rows into training.
- **Undersampling the majority is the one resampling move with a clean correction.** Keep a fraction `s` of
  negatives and the training odds are inflated by 1/s; multiply the model's fitted odds by `s` to recover
  the real ones. Worked — 100,000 rows with 2,000 positives, keeping 1 negative in 10. Negatives kept:
  98,000/10 = 9,800. Training prevalence: 2,000/11,800 = 0.169. A model that outputs 0.50 there has odds
  1.0; corrected odds: 1.0 × 0.1 = 0.10; real probability: 0.10/1.10 = 0.091. A "50% risk" is a 9% risk.
  If anything downstream consumes the probability — expected
  cost, a reserve, a price — apply the correction or do not undersample.

**Never resample validation or test.** The precision you then report describes a population that does not
exist; `machine-learning-skills:model-evaluation` works the arithmetic of exactly that mistake.

## Interpretation — what each quantity licenses, and what it is NOT evidence of

| Quantity | Licenses the claim | Is NOT evidence of | Check before you say it aloud |
|---|---|---|---|
| **Standardized linear coefficient** | "Holding the other features *in this model* fixed, a 1-SD move in X is associated with β" | The effect of intervening on X; the effect for any individual; anything about a feature you did not include | Refit on ~20 bootstrap resamples and report sign stability alongside the point estimate |
| **Logistic coefficient / odds ratio** | A multiplicative change in the **odds** | A change in probability of the same size — see the conversion below | Convert to a probability at your actual base rate before it reaches a slide |
| **Lasso's selected set** | One sufficient sparse set among several that fit equally well | "These are the important features" — a correlated twin was dropped by a coin flip | Selection frequency across bootstrap refits; below ~50% it is not a finding |
| **Impurity (gain) importance** | Which features the fitted trees split on, measured on training data | Predictive contribution; any comparison across features of different cardinality | Inject a random high-cardinality column and refit. If the noise column lands in the top decile, your ranking is measuring cardinality |
| **Permutation importance** | The validation-metric drop when X's information is destroyed, **for this fitted model** | What a model *retrained* without X would lose. Two features correlated at r ≈ 0.95 can each score ≈ 0 while dropping both is fatal — each covers for the other during the shuffle | Permute correlated groups together; when the answer matters, compare against a leave-one-covariate-out refit |
| **Partial dependence / ICE** | The model's average response along X | A causal dose-response; anything at all in regions with no training data | Plot the feature's decile marks under the curve and refuse to read it where the data is thin |
| **SHAP** | A per-prediction additive decomposition of **this model's** output | A causal attribution; a reason the world produced the outcome | Verify additivity on a row: base value + Σφ should reproduce the model's output |

**The odds-ratio conversion, worked** — the single most common over-claim in a logistic write-up. Take a
standardized coefficient β = 0.42, so the odds ratio is e^0.42 ≈ 1.52.

- At a 3.0% base rate the base odds are: 0.03/0.97 = 0.0309. One SD higher: 0.0309 × 1.52 = 0.047. As a
  probability: 0.047/1.047 = 0.0449 — about 4.5%. The absolute move, in percentage points: 4.5 − 3.0 = 1.5.
- At a 40% base rate the *same* coefficient does something else entirely. Base odds: 0.40/0.60 = 0.6667.
  Raised odds: 0.6667 × 1.52 = 1.0133. Probability: 1.0133/2.0133 = 0.503 — a move, in points, of:
  50.3 − 40.0 = 10.3.

"52% higher odds", "1.5 points more likely", and "10.3 points more likely" are all faithful readings of one
coefficient. Odds ratios are constant across the base rate; probability differences are not. This is why an
odds ratio on its own can never answer "how much does this matter here" — and why quoting one without the
base rate is where honest analysts accidentally mislead.

**The universal caveat, restated precisely:** every quantity in the table above describes what the *model*
uses, not what *causes* the outcome. Say "the model relies on X," never "X drives the outcome."

## Failure envelopes — where this method stops working, and what you see

| Envelope | What the practitioner actually sees | What to do instead |
|---|---|---|
| **Too few rows or events** (roughly < 500 rows or < 50 events) | Fold sd exceeds every between-model difference; the top-feature list reshuffles across folds | Stop comparing models. Fit one regularized linear model, report the interval, and say the comparison was under-powered |
| **Distribution shift / non-stationarity** | Random-split CV looks strong; the first month in production does not. Time-ordered folds show scores declining with fold date | Evaluate on a time split, set a retraining cadence, monitor the input distributions. If the target is itself a series, `machine-learning-skills:time-series-forecasting` |
| **Target leakage** | PR-AUC implausibly near 1.0; one feature holds most of the importance; that feature is populated at or after the moment the label is decided | The leakage checklist in `machine-learning-skills:model-evaluation`. Re-derive the as-of moment for every feature |
| **Extrapolation with trees** | Predictions clamp at the training extremes; residuals grow at the edges of the range | Linear or a linear-on-transformed-target model for the extrapolating region, or hard bounds plus an explicit out-of-range flag |
| **Selective labels** | The model reproduces the existing decision policy beautifully and adds nothing, because outcomes exist only for the cases the policy already accepted | Say so. The model is valid only under the policy that generated its labels; changing the policy invalidates it. Randomized or held-out policy exceptions are the only clean fix |
| **Heavy collinearity at interpretation time** | Coefficient signs flip between bootstrap refits; every permutation importance sits near zero | Interpret the correlated set as one block, or pick a single named representative and disclose the choice |
| **Noisy or contested labels** | A hard performance ceiling no model family gets past, regardless of capacity | Measure annotator agreement first; the ceiling is the agreement rate. Label quality lives in `machine-learning-skills:model-evaluation` |

## Deliverable contract — the model summary, item by item

A finished model summary contains all twelve. Anything missing is a question someone will ask later, at a
worse moment.

1. **Task line** — target definition including the exact label window and the as-of moment, task type, and
   what one row is.
2. **Data and split** — row count, positive count, split scheme with the dates of each block, and the
   **count of positives in the test set** (this number sets the width of every interval you will report).
3. **The ladder** — every model tried, with train and validation scores and the gain over the last kept
   model. Include the rungs you rejected; a ladder with no rejections has been edited after the fact.
4. **The stop rule** — written before the ladder was run, with the numbers it used.
5. **The pipeline** — ordered steps, an explicit statement of what was fit on train only, and the
   serialized artifact containing all of it. A model without its preprocessing is not a deliverable.
6. **Hyperparameters** — final values, the search space, the number of trials, and how the number of
   trees was chosen (which validation fold early-stopped, at which round).
7. **The test result** — scored once, with an interval and the n behind that interval.
8. **The operating point** — the threshold, which split it was chosen on, the confusion matrix at it, and
   the constraint it satisfies (cost, alert budget, required recall).
9. **Imbalance handling** — what was applied, whether it sat inside or outside the folds, and whether the
   probabilities were recalibrated afterwards.
10. **Interpretation** — coefficients or permutation importances *with their stability across resamples*,
    worded as association; partial dependence for the top few features, with the data-thin regions marked
    as unreadable.
11. **The failure envelope in this model's own terms** — not the generic list above but the instantiated
    one: "tenure beyond 60 months lies outside the training range and the model returns a constant there."
12. **Reproduction and ownership** — seed, library versions, the command that reproduces the test number,
    and the named human who owns the threshold and the error costs.
