# Calibration and the tampering guard

Two disciplines that keep the outside view honest over time: **calibration** (log, score, and
update predictions so judgment improves against a record) and the **tampering guard** (Deming's
funnel rules — don't let single-period misses rewrite the rule).

## Contents
- [Calibration practices (Tetlock)](#calibration-practices-tetlock)
- [The decision journal](#the-decision-journal)
- [Scoring](#scoring)
- [The tampering guard: Deming's funnel rules](#the-tampering-guard-demings-funnel-rules)
- [Common-cause vs. special-cause test](#common-cause-vs-special-cause-test)

## Calibration practices (Tetlock)

From the superforecasting research on what separates consistently accurate forecasters
[snippet-only]:

- **Granular probabilities.** Say 63%, not "likely" — vague words hide miscalibration and make
  scoring impossible. If 63% vs. 70% feels absurdly precise, that feeling is the point: forcing
  the number exposes how much you actually know.
- **Frequent small updates.** Move the estimate a few points as evidence arrives; large jumps
  usually mean the prior was never real. Update on evidence, not on mood or on who asked.
- **Decompose the question.** Break "will receipts hit the number?" into parts you can estimate
  (enrollment locked? calendar shift? payer-mix change?) — Fermi-style decomposition beats
  gestalt guessing.
- **Start from the base rate, then adjust** — the outside view is itself the first calibration
  practice; the inside view supplies increments, not the starting point.
- **Score everything and post-mortem both directions.** Misses show overconfidence; windfall hits
  show underconfidence. Both are calibration errors.

## The decision journal

One entry per material estimate or decision (Klein/Kahneman practice — the journal is a
pre-mortem's paper trail and hindsight-bias vaccine). Template:

```
ID / date:
Decision or prediction:        <the number or the call>
Reference class used:          <definition, n> — ratified by:
Base-rate anchor:              <value at P50>
Final number + certainty:      <value, P-level or probability>
Why (3 lines max):             <the load-bearing reasoning>
What would change my mind:     <named observations>
How I feel making it:          <one line — mood is data for later review>
Review date:                   <when actuals land>
--- at review ---
Actual outcome:
Score:                         <Brier / realized percentile>
Lesson (if any):               <one line; common-cause misses get "none">
```

Keep the journal append-only; editing an entry after the fact defeats its purpose.

## Scoring

- **Probability forecasts → Brier-style score:** for a yes/no outcome, `(p − outcome)²` with
  outcome ∈ {0,1}; average across predictions; lower is better. 0.25 is coin-flipping; a
  calibrated forecaster beats it consistently [snippet-only].
- **Point estimates → realized percentile:** compute the realized ratio `actual/estimate` and note
  where it fell in the reference class. Estimates landing repeatedly above your stated P80 mean
  the uplift is too small; repeatedly hugging P50 means the process is calibrated.
- **Calibration check over many predictions:** of everything called "80%", about 80% should have
  happened. Bucket predictions by stated confidence and compare to hit rates once a quarter.

## The tampering guard: Deming's funnel rules

Deming's funnel experiment: drop marbles through a funnel at a target and try adjustment rules on
the funnel's position [snippet-only]:

- **Rule 1 — leave the funnel alone** (aimed at the target): baseline variance. Best result.
- **Rule 2 — after each drop, shift the funnel opposite the last error:** variance roughly
  **doubles**. This is exactly "we missed by −4% last cycle, so raise next cycle's number 4%".
- **Rule 3 — re-aim relative to the target from the last resting point:** oscillation grows.
- **Rule 4 — aim at wherever the last marble landed:** a random walk; drifts without bound
  (estimate-by-last-actual is this rule).

The estimating rule is the funnel. A single-period miss inside the class's normal spread is the
marble's scatter — adjusting the rule to it *adds* the adjustment's variance to the process's own.
The guard: **classify the miss before touching anything** (next section). Rules change once, with
a diagnosis and a reason — the same discipline the cash-forecasting accuracy loop states as
"diagnose the miss to a driver and correct the rule — do not just overwrite the number".

## Common-cause vs. special-cause test

Before any rule change, test the miss against the reference class itself:

1. **Spread test:** is this cycle's error inside the class's usual range (roughly P10–P90 of the
   error distribution)? Inside → common cause. Leave the rule alone; log and move on.
2. **Run test:** are the last several errors same-signed (e.g., 6+ in a row, or 18 of 22 as in the
   worked tuition example)? A run signals a systematic bias — special cause of the fixable kind.
3. **Magnitude test:** is the error far outside the historical range? Special cause — find the
   event (calendar shift, definition change, one-off) before generalizing from it.
4. **Only special-cause findings change the rule**, and the change is made once, at the driver
   (curve, lag, calendar), with the diagnosis written in the journal. Then the class keeps
   accumulating and the next review checks whether the change worked.

The quiet payoff: this test is also what protects the *reference class* — a class polluted by
rule changes made after every miss no longer measures the process, only the tampering.
