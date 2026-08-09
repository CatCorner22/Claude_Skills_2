# Evals — math-foundations-skills:probability-fundamentals

## 1. Positive trigger (should load the skill)
> "About 2% of the files we screen have the defect. The screen catches 95% of true
> defects but also flags 4% of clean files. One of my files just got flagged — what
> are the odds it's actually defective?"

Expected: skill loads and builds a natural-frequency table rather than plugging
into the Bayes formula. Out of 10,000 files: 200 defective (2%), of which 190 flag
(95%) and 10 slip; 9,800 clean, of which 392 flag (4%) and 9,408 pass. Flags total
190 + 392 = 582, so P(defective | flagged) = 190/582 ≈ 33% — and the response shows
the row/column sums as a cross-check. It names the direction flip explicitly (the
95% quoted is P(flag | defect), the question asks P(defect | flag)), explains that
the clean crowd's small error rate out-produces the defective crowd's true flags
because of the 2% base rate, and keeps "odds" vs "probability" straight if it uses
the odds shortcut (prior 200:9,800 × LR 95/4 ≈ 23.75 → posterior ≈ 190:392).

## 2. Near-miss (should NOT load this skill)
> "We A/B tested the new checkout flow: 3.1% conversion on control vs 3.4% on
> variant, about 5,000 visitors each. Is the difference real or noise?"

Expected: `data-analytics-bi-skills:statistical-inference` owns this — it is
sample-to-population reasoning (hypothesis test, confidence interval, p-value), not
event-probability arithmetic. If this skill loads on an A/B significance question,
its description is over-triggering.

## 2b. Near-miss (closer — should NOT load this skill)
> "Before I commit to this project timeline, anchor it on how long projects like
> this actually took — use the base rates from our past deliveries."

Expected: `decision-science-skills:reference-class-forecasting` owns base-rate
*anchoring* of real-world estimates from reference classes. It consumes the
base-rate discipline this skill teaches, but the workflow (class selection,
distribution, uplift, prediction log) is its territory.

## 3. Quality rubric
A good response:
- **Does the task:** builds the natural-frequency table with whole-number counts,
  shows the arithmetic for every cell, and cross-checks that rows and columns sum
  before reading off the answer; applies the right combination rule (overlap
  subtracted for "either", P(A)×P(B|A) for "both", with independence justified —
  never assumed — before it collapses to P(A)×P(B)); distinguishes mutually
  exclusive from independent when either term appears; computes expected value as
  Σ p×payoff and then asks the repeats question and the ruin question before letting
  EV decide.
- **Teaches:** explains conditioning as shrinking the universe to what is known;
  why P(A|B) ≠ P(B|A) (same numerator, different denominators — and the denominator
  ratio is the base rate); why natural frequencies beat percentage talk (the counts
  carry the base rate along); and delivers the one-line inoculation for whichever
  fallacy the prompt brushes against (base-rate neglect, gambler's, conjunction,
  hot-hand).
- **Stays honest:** states the answer's dependence on the quoted inputs (a shifted
  base rate or false-alarm rate moves the result, and the response says by roughly
  how much); refuses to treat a positive EV as sufficient for a one-shot or ruinous
  choice; treats short streaks as weak evidence in either direction rather than
  proof of anything; and routes inference-from-samples, evidence-weighing, and
  failure-time modeling to their owning skills instead of improvising them here.
