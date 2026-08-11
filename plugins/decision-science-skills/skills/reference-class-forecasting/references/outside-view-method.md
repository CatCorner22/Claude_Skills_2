# The outside-view method: class selection, distribution, and uplift math

Method lineage: Kahneman/Tversky's inside-vs-outside view and planning fallacy; Flyvbjerg's
reference-class forecasting (2006 PMI formalization) and the optimism-bias uplifts adopted in UK
appraisal guidance (HM Treasury Green Book; Department for Transport tables) [snippet-only].

## Contents
- [Choosing the reference class](#choosing-the-reference-class)
- [Building the outcome distribution](#building-the-outcome-distribution)
- [Anchoring and placement](#anchoring-and-placement)
- [Adjustment rules and uplift math](#adjustment-rules-and-uplift-math)
- [Worked example: a cash-driver anchor from MAPE/bias history](#worked-example-a-cash-driver-anchor-from-mapebias-history)
- [The inside-vs-outside reconciliation memo](#the-inside-vs-outside-reconciliation-memo)
- [When the class is thin](#when-the-class-is-thin)

## Choosing the reference class

The class must be **broad enough for statistics, narrow enough to be comparable**. Heuristics:

- **Match on the mechanism that drives the outcome**, not on surface labels. For a cash driver,
  the mechanism is the payer population and calendar (tuition cycles behave like tuition cycles);
  for a software feature, it is team + codebase + feature size, not the feature's subject matter.
- **Prefer your own history when it exists.** Twenty-four cycles of your own forecast-vs-actual
  errors beat an industry benchmark of someone else's projects — same process, same people, same
  measurement.
- **Size guidance:** 20+ cases support stable percentiles; 10–20 support a median and rough P80;
  below ~10, report the thinness and widen (see [When the class is thin](#when-the-class-is-thin)).
- **Exclude cases only for stated, outcome-independent reasons** (different mechanism, definition
  change), never because their outcomes look extreme — the extremes are the information.
- **Freeze the class before computing outcomes.** Class-shopping after seeing the numbers is the
  inside view sneaking back in.
- The assistant should propose 2–3 candidate classes with trade-offs (broader/noisier vs.
  narrower/thinner); the human ratifies one. Record the choice and its rationale in the memo.

## Building the outcome distribution

1. Express every case as a comparable, scale-free outcome measure:
   - **Ratio form:** `r = actual / estimate` (cost, duration, receipts).
   - **Signed-error form:** `e = (actual − estimate) / estimate` — the same "variance %" and
     signed-bias convention operational forecast-accuracy loops use.
2. Sort the values and read empirical percentiles: P10, P50 (median), P80, P90. With n cases, the
   Pk value is the `ceil(k/100 × n)`-th sorted value — no distributional assumption needed.
3. Report **mean, median, and spread together**. Overrun distributions are typically right-skewed
   and fat-tailed: the mean sits above the median, and the tail is where plans die. A class
   summarized by its mean alone hides exactly the risk the method exists to expose.
4. Segment only when the mechanism differs (e.g., separate distributions per driver, or
   small vs. large projects) and each segment still has enough cases.

## Anchoring and placement

- The **naive anchor** is the class P50 applied to the raw inside estimate:
  `anchor = estimate × r_P50`.
- Write this number down before any discussion of the case's specifics. It is the burden-shifting
  device: from here on, the estimate moves only by written argument or by policy uplift.
- Also place the inside estimate in the class: "your number assumes this case lands at the class's
  P15" is often the whole conversation.

## Adjustment rules and uplift math

Two disciplines; pick one per estimate:

- **(a) Written adjustment.** A short memo (template below) argues why this case sits above or
  below the class median, and by how much. Anything not argued in writing stays at the anchor.
- **(b) Required uplift at a chosen certainty level** (Department-for-Transport style). Choose an
  acceptable chance of the estimate being exceeded — accepting a 20% chance means the P80:
  `uplift% = r_P80 − 1`, `estimate_P80 = estimate × r_P80`.
  No case-by-case argument; the policy does the adjusting.

**Direction matters.** Uplift the numbers where being over hurts (costs, disbursements, schedule);
haircut the numbers where being under hurts (receipts feeding a liquidity floor): for receipts use
a low percentile, e.g. `estimate_P20 = estimate × r_P20`, so that in 80% of comparable cycles at
least that much arrived. Certainty level is a risk-appetite decision the human owns; record it.

## Worked example: a cash-driver anchor from MAPE/bias history

Setting: the tuition-receipts driver in a rolling 13-week direct-method cash process. The
accuracy loop already tracks per-cycle variance — MAPE and signed bias — so the reference
class is sitting in the variance file.

1. **Class:** the driver's own last 24 cycles of `(actual − forecast) / forecast`, same
   definition as the accuracy reference. Ratified: same payer population, same calendar; two
   cycles during a fee-definition change excluded for a stated, outcome-independent reason.
2. **Distribution (illustrative):** MAPE 6.2%; signed bias **+3.5%** (actuals persistently above
   the projection — systematic under-projection). Ratios `r = actual/forecast`, sorted:
   P20 = 0.99, P50 = 1.03, P80 = 1.07.
3. **Anchor:** next cycle's inside number is $18.40M. Naive anchor = 18.40 × 1.03 = **$18.95M**.
   The +3.5% bias is not noise — 18 of 22 cycles were same-signed — so anchoring at the raw
   $18.40M would repeat a known, measured error.
4. **Uplift/haircut by use:**
   - Feeding the *expected* cash position: use the anchor, $18.95M.
   - Feeding a *liquidity floor* check (can we cover the payroll run if receipts disappoint?):
     use P20 → 18.40 × 0.99 = **$18.22M**.
   - If this driver were a disbursement, the P80 figure (×1.07) would be the prudent number.
5. **Log and score:** journal the prediction (number, percentile basis, class, review date); when
   actuals land, compute the realized ratio, note which percentile it fell at, and append the
   cycle to the class. The same-signed run also feeds back to the *model* owner: a persistent
   +3.5% bias is a driver-curve correction for the forecast owner to make once, with a reason —
   not something to chase cycle-by-cycle (see `calibration-and-tampering.md`).

This is the loop-closing move: the forecast process already measures MAPE and bias; this method turns that
measurement into next-cycle anchors and uplifts per driver (tuition receipts, payroll, grant
drawdowns), instead of letting the accuracy history sit unread.

## The inside-vs-outside reconciliation memo

Half a page, drafted by the assistant, signed by the human:

- **Estimate under review:** <what, for when, raw inside number>
- **Reference class:** <definition, n, inclusion/exclusion reasons> — ratified by <name>
- **Class distribution:** <P10 / P50 / P80, mean, skew note>
- **Base-rate anchor:** <estimate × r_P50>
- **Inside-view placement:** <the percentile the raw estimate implies>
- **Adjustments claimed:** <each with its written justification, or "none — policy uplift at P__">
- **Final number and certainty level:** <value, P-level, direction rationale>
- **Prediction logged:** <journal ID, review date>

## When the class is thin

- Fewer than ~10 cases: report the thinness explicitly; give the range rather than fine
  percentiles; widen the class one notch (all receipt drivers, not just tuition; all features,
  not just this module) and show both views.
- No internal history at all: use published external classes (e.g., cost-overrun distributions by
  project type from the Flyvbjerg literature [snippet-only]) as the starting anchor, state the
  comparability caveats, and start logging your own outcomes now — the internal class builds
  itself within a year of scoring.
- Never respond to thinness by reverting to the pure inside view; a thin base rate with stated
  uncertainty still beats an optimistic story with none.
