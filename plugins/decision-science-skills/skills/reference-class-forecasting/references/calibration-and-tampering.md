# Calibration and the tampering guard

Two disciplines that keep the outside view honest over time: **calibration** (log, score, and
update predictions so judgment improves against a record) and the **tampering guard** (Deming's
funnel rules — don't let single-period misses rewrite the rule).

## Contents
- [Read this first: the belief moves, the rule does not](#read-this-first-the-belief-moves-the-rule-does-not)
- [Calibration practices (Tetlock)](#calibration-practices-tetlock)
- [The decision journal](#the-decision-journal)
- [Scoring](#scoring)
- [The tampering guard: Deming's funnel rules](#the-tampering-guard-demings-funnel-rules)
- [Common-cause vs. special-cause test](#common-cause-vs-special-cause-test)

## Read this first: the belief moves, the rule does not

The two disciplines in this file look like they contradict each other, and read carelessly they do.
Calibration says **update often, in small increments**. The tampering guard says **do not touch
anything until you have classified the miss**. Both are right, because **they govern different
objects**:

| | The **belief** (a forecast of one open question) | The **estimating rule** (curve, lag, uplift %, class definition) |
|---|---|---|
| What moves it | New information about *this* case | A diagnosed defect in how estimates get produced |
| How often | Continuously — a few points at a time as evidence lands | Rarely — once, with a written diagnosis |
| Governed by | Tetlock: frequent small updates, perpetual beta | Deming: leave the funnel alone unless it is genuinely mis-aimed |
| Failure mode | Hoarding updates for one dramatic reversal | Tampering — re-tuning after every miss, which roughly doubles variance |

**The one-question test: is the new input information about the case in front of me, or the realized
error of a case already closed?**

- *"Enrollment locked 4% below plan; the payer-mix shifted."* Information about the open cycle →
  **move the belief now**, by a few points, and log it.
- *"Last cycle came in 4% above forecast."* The realized error of a closed case → **do not touch the
  rule**; run the common-cause/special-cause test first.

Why the funnel experiment does not license belief-freezing: Deming's operator is adjusting the
*aiming rule* using nothing but *output error*, with no new information about the next drop. That is
the definition of tampering. A forecaster who learns something new about next month is not in that
situation at all — they are not adjusting a rule, they are reading evidence.

**Where the two legitimately meet: the run test.** A single realized error is only an error. A *run*
of same-signed errors is information about the process — which is exactly why the run test (below) is
the one route by which outcome data is allowed to change the rule. So the boundary is not a wall; it
is a gate with a stated key.

This distinction is the same seam `decision-science-skills:bayesian-updating` sits on from the other
side: that skill's "update small and often" applies to the belief, and it hands rule changes here.

## Calibration practices (Tetlock)

From the superforecasting research on what separates consistently accurate forecasters
[snippet-only]:

- **Granular probabilities.** Say 63%, not "likely" — vague words hide miscalibration and make
  scoring impossible. If 63% vs. 70% feels absurdly precise, that feeling is the point: forcing
  the number exposes how much you actually know.
- **Frequent small updates — of the *belief*, not the rule.** Move the estimate for the open
  question a few points as evidence about that case arrives; large jumps usually mean the prior was
  never real. Update on evidence, not on mood or on who asked. This is the practice the section
  above scopes: it never licenses re-tuning the driver curve, the uplift percentage, or the class
  definition after a single miss — that is the funnel, and it is guarded below.
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

The estimating rule is the funnel — **not** your belief about the open question (see the framing
section at the top of this file: the belief updates continuously on new information; only the rule is
guarded here). A single-period miss inside the class's normal spread is the marble's scatter —
adjusting the rule to it *adds* the adjustment's variance to the process's own. The guard:
**classify the miss before touching anything** (next section). Rules change once, with
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
5. **A rule change is also a class break.** When a structural correction is accepted, mark the break
   date and start a new class from the first post-correction cycle — the old cycles describe
   forecasts the old rule produced, so they can no longer supply the bias ratio (they usually still
   describe *spread*). And drop the outside-view bias uplift to ×1.00 for whatever the curve now
   handles, or the estimate carries the correction twice. The full procedure is
   "Correct once, not twice" in `outside-view-method.md`.

The quiet payoff: this test is also what protects the *reference class* — a class polluted by
rule changes made after every miss no longer measures the process, only the tampering.
