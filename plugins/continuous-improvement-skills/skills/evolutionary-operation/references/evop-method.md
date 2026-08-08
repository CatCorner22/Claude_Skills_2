# EVOP method — phases, cycles, significance, and safe bounds

Working mechanics for `evolutionary-operation`. Everything here assumes the process owner has
already set safe operating limits (§6 — read it first if that hasn't happened).

## Contents
1. The pattern
2. Cycles and phases
3. Worked example — recon matching tolerances, 2×2 plus center
4. Significance from small samples
5. Shifting the center and rotating factors (stopping rules)
6. The safe-bounds discipline

## 1. The pattern

For two factors, the standard EVOP pattern is a 2×2 factorial plus the current operating point:

```
factor B (high) |  (3)          (4)
                |        (0)            0 = current center
factor B (low)  |  (1)          (2)
                +---------------------
                  A (low)     A (high)
```

- Five settings total; every one sits **inside the owner's safe limits**.
- Steps are deliberately small — small enough that output at every point stays in spec, and small
  enough that operations barely notices the pattern is running. If a step would need sign-off as a
  "change", it is too big for EVOP.
- For three factors, use a 2³ (8 corners) or a half-fraction (4 corners) plus center. Beyond three
  factors, the pattern stops being unobtrusive — that's designed-experiment territory
  (`continuous-improvement-skills:design-of-experiments`).

## 2. Cycles and phases

- **Cycle** = one pass through all pattern points, in randomized order, recording every response
  (improvement responses *and* guard responses) at each point. In a batch process a "point" is a
  batch; in a daily recon run, a point can be one day (or one statement-file slice) run at that
  setting.
- **Phase** = a sequence of cycles at one pattern position, ended when the effects are judged.
  Classic practice: expect no verdict before 3 cycles; many phases run 5–10.
- **The EVOP log (information board)** carries, per response: the running mean at each pattern
  point, each factor's effect estimate, its standard error, and the cycle count. Historically a
  wall chart maintained by a statistician; here, a table the LLM updates every cycle. No log, no
  error estimate, no conclusions — keep it from cycle one.

## 3. Worked example — recon matching tolerances, 2×2 plus center

Setting: an auto-reconciliation engine matching bank statement lines to system transactions.
Current operating point: amount tolerance **T = $1.00**, date window **W = 3 days**. Owner-set
bounds: T ≤ $2.00, W ≤ 5 days, and a hard guard: **false-match rate ≤ 0.05%** of matched lines
(false matches post wrong cash), with any breach stopping the experiment and reverting to the
known-good center.

Pattern (all inside bounds): T ∈ {0.75, 1.25}, W ∈ {2, 4}, plus center (1.00, 3).
Responses per point per cycle: auto-match rate % (improve) and false-match rate % (guard),
false matches counted by the independent audit pass, not by the engine grading itself.

Match-rate observations over three cycles (one day per point, randomized order):

| Point (T, W)      | Cycle 1 | Cycle 2 | Cycle 3 |
|-------------------|---------|---------|---------|
| center (1.00, 3)  | 91.2    | 91.0    | 91.4    |
| 1 (0.75, 2)       | 90.8    | 90.9    | 90.7    |
| 2 (1.25, 2)       | 91.5    | 91.6    | 91.8    |
| 3 (0.75, 4)       | 91.4    | 91.2    | 91.5    |
| 4 (1.25, 4)       | 92.1    | 92.0    | 92.3    |

Effect of **T** per cycle = mean(points 2, 4) − mean(points 1, 3): 0.70, 0.75, 0.95 → mean **+0.80**.
Effect of **W** per cycle = mean(points 3, 4) − mean(points 1, 2): 0.60, 0.35, 0.65 → mean **+0.53**.
Interaction per cycle = mean(points 1, 4) − mean(points 2, 3): −0.05, +0.05, −0.15 → mean −0.05.

Guard readings stayed inside the bound at every point (worst: 0.031% at point 4, vs 0.05% limit)
— but note the *trend*: false-match rate rises with T. The guard is closest to its cliff exactly
where the improvement response is best. That trend goes to the owner alongside the effects.

## 4. Significance from small samples

Each cycle yields one estimate of each effect, so after n cycles you have n replicate estimates:

- effect = mean of the n per-cycle effects
- s = standard deviation of the per-cycle effects; **SE = s / √n**
- rule of thumb: act only when |effect| > **2 × SE** (≈ 95% two-sided for the shop floor; with n
  as small as 3, a t-critical near 4.3 is the honest bar — say which one you used).

For the example: T effect 0.80, s ≈ 0.132, SE ≈ 0.076 → 0.80 ≫ 2×0.076: **signal**. W effect
0.53, s ≈ 0.165, SE ≈ 0.095 → clears 2×SE, but not the small-n t bar — run more cycles before
leaning on W. Interaction −0.05: noise.

Historical note: classic EVOP worksheets estimated s from *ranges* (range × a d₂-style constant)
so plant crews could run it without computing variances. With an LLM keeping the ledger, compute
the t-statistics directly — but keep publishing the effect ± 2·SE form on the log, because that is
what the owner reads. Two disciplines the arithmetic doesn't excuse: randomize run order within
each cycle (defeats day-of-week and month-end confounds — or block on them explicitly), and never
stop a phase the moment an effect first crosses the line (that's optional stopping; fix the phase
length in advance).

## 5. Shifting the center and rotating factors (stopping rules)

- **A direction wins** (effect clears the bar, guard trend acceptable): propose the new center —
  here (T 1.25, W 4) pending more W cycles, or conservatively (T 1.25, W 3) on T alone. The
  **owner ratifies** the shift and re-states limits around the new center. Begin the next phase
  there: EVOP climbs in small ratified steps, indefinitely.
- **Effects flat for two consecutive phases**: the local surface is level. Hold the center and
  rotate in a different factor (swap W for, say, a reference-cleaning toggle), or ask the owner to
  approve a slightly wider pattern.
- **Guard trending toward its bound** even while in-bound: cap movement in that direction; the
  guard's limit, not the improvement response, defines the edge of the map.
- **Any excursion out of spec, any guard breach, any process upset**: stop, revert to the last
  known-good center, and investigate before resuming (that investigation is
  `continuous-improvement-skills:root-cause-analysis` work, not EVOP).

## 6. The safe-bounds discipline

The non-negotiables that make in-production experimentation defensible:

- **Limits precede perturbation.** The process owner sets factor bounds and guard limits before
  the first cycle, in writing, in the EVOP log header. The analyst proposes; the owner disposes.
- **Guards are hard, not advisory.** A guard limit (false-match rate, forecast bias, SLA breach)
  is a stop condition, not a note. Measure the guard independently of the mechanism being tuned —
  on a recon engine, by the audit pass, never by the engine's own claim.
- **Every setting must be individually safe**, not just safe on average across the pattern.
- **Reversibility**: every pattern point and center shift must be revertible in one step; record
  the revert path next to each setting.
- **One experiment per process at a time**, and the pattern pauses during known upsets (bank
  format changes, fiscal close) rather than absorbing them as "noise".
- **The log is the audit trail**: settings, dates, responses, effects, decisions, ratifications.
  If someone asks "why is the tolerance $1.25 now?", the log answers.
