# The outside-view method: class selection, distribution, and uplift math

Method lineage: Kahneman/Tversky's inside-vs-outside view and planning fallacy; Flyvbjerg's
reference-class forecasting (2006 PMI formalization) and the optimism-bias uplifts adopted in UK
appraisal guidance (HM Treasury Green Book; Department for Transport tables) [snippet-only].

## Contents
- [Choosing the reference class](#choosing-the-reference-class)
- [Building the outcome distribution](#building-the-outcome-distribution)
- [Anchoring and placement](#anchoring-and-placement)
- [Adjustment rules and uplift math](#adjustment-rules-and-uplift-math)
- [Aggregation: never sum the P80s](#aggregation-never-sum-the-p80s)
- [Worked example: a cash-driver anchor from MAPE/bias history](#worked-example-a-cash-driver-anchor-from-mapebias-history)
- [Correct once, not twice: uplift or curve, never both](#correct-once-not-twice-uplift-or-curve-never-both)
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

**And the certainty level attaches to ONE commitment.** A P80 per line item, added up across a
portfolio, is not a P80 portfolio — it is a much more expensive number wearing an P80 label. That is
the next section, and skipping it is how this method backfires.

## Aggregation: never sum the P80s

**The rule: P50 per item, plus one contingency at the portfolio level, sized at the portfolio's own
P80. Never item-by-item P80s added together.**

Everything above is correct for a *single* commitment: one project, one covenant, one deliverable
you must individually meet. The moment you own the **sum** — a program budget, a department's annual
plan, a 13-week cash total across a dozen drivers — applying the house percentile to each line and
adding is a double count, because **independent overruns partially cancel**. Variances add;
standard deviations do not. For independent items, `σ_sum = √(Σσᵢ²)`, while summing the item
uplifts charges you `Σσᵢ`.

**Worked, ten independent lines.** Each line: P50 = $1.00M, P80 = $1.20M (so each line's own uplift
is +20%). Treating each line as roughly symmetric, `σᵢ ≈ (P80 − P50)/0.8416 ≈ 0.2376`, since the
80th percentile of a normal sits 0.8416σ above the median.

| Method | Contingency | Total booked |
|---|---|---|
| Sum of ten line-item P80s | $2.00M (+20%) | **$12.00M** |
| P80 of the portfolio: `σ_sum = 0.2376 × √10 ≈ 0.7514`; `0.8416 × 0.7514 ≈ 0.6324` | $0.63M (+6.3%) | **$10.63M** |

The line-item policy books **$1.37M of contingency it cannot justify** — 3.16× what the portfolio's
own P80 requires, and that multiple is exactly `√10`, which is the whole mechanism in one number.
Worse, ask what confidence level the $12.00M actually represents: `2.00 / 0.7514 ≈ 2.66` standard
deviations above the mean, or about the **P99.6** of the portfolio. The team believes it funded to
80% and has in fact funded to 99.6% — for all ten lines to land at their own 80th percentiles in the
same period would take a remarkable run of bad luck.

**Correlation is the dial, and it is the reason not to memorise "divide by √n."** The √n result
assumes the lines are independent. Real portfolios share drivers — one labour market, one vendor,
one weather year, one regulatory change — and shared drivers create genuine positive correlation.
With every pair correlated at ρ and identical lines, `σ_sum = σ · √(n(1 + (n−1)ρ))`:

| ρ across the ten lines | σ_sum (in units of one line's σ) | Portfolio-P80 contingency | Total |
|---|---|---|---|
| 0 (independent) | 3.16σ (= √10) | $0.63M | $10.63M |
| 0.3 (typical shared drivers) | 6.08σ (= √37) | $1.22M | $11.22M |
| 1.0 (one common cause moves everything) | 10σ (= n) | $2.00M | $12.00M |

At ρ = 1 the sum of the P80s is exactly right — which tells you what the sum-of-P80s policy is
implicitly assuming: **that every line goes wrong together.** Naming that assumption out loud is
usually enough to settle the argument. So the procedure is not "apply √n"; it is: *build the
portfolio distribution with the correlations you actually believe (simulate it if the lines are
many or lumpy), and take one contingency off that.*

**Two reasons this is a governance fix and not only an arithmetic one:**
- **Distributed padding is invisible and unreclaimable.** Buffer scattered across forty line items
  belongs to forty owners, so nobody can see it, price it, or release it — and it gets spent, because
  a line with room in it finds a use for the room. One named contingency held centrally has an
  owner, a release rule, and a balance you can report.
- **Chronic underspend costs credibility the same way overruns do.** A team that comes in 15% under
  every year stops being believed about *any* number, gets its request cut on principle next cycle,
  and has then lost the very authority this method exists to build. Over-budgeting is the mirror
  image of the optimism bias, not the cure for it.

**Where the rule does NOT apply — check before using it:**
- **Each item must independently stand up.** A per-entity covenant, a hard per-item cap, a
  contractual per-deliverable deadline, a grant whose budget cannot be crossed line to line: you
  carry each risk separately, so each one is its own commitment and takes its own P80. Aggregation
  relief requires that a surplus on line 3 can actually pay for the overrun on line 7.
- **Schedules do not aggregate like costs.** Durations on one serial path add, so the √n logic
  applies along a path — but a milestone fed by several *parallel* chains takes the **maximum**, and
  the maximum of several uncertain finishes is later than any one of them. With three independent
  feeding chains of equal risk, the milestone's median lands near each chain's **P79**
  (0.5^(1/3) ≈ 0.794) and the milestone's P80 near each chain's **P93** (0.8^(1/3) ≈ 0.928). This
  *merge bias* runs the opposite direction from cost pooling: parallelism makes the joint milestone
  worse, not better. Size schedule contingency by simulating the network, never by a sum rule.

## Worked example: a cash-driver anchor from MAPE/bias history

Setting: the tuition-receipts driver in a rolling 13-week direct-method cash process. The
accuracy loop already tracks per-cycle variance — MAPE and signed bias — so the reference
class is sitting in the variance file.

1. **Class:** the driver's own last 24 cycles of `(actual − forecast) / forecast`, same
   definition as the accuracy reference. Ratified: same payer population, same calendar; two
   cycles during a fee-definition change excluded for a stated, outcome-independent reason.
2. **Distribution (illustrative):** MAPE 6.2%; signed bias **+3.5%** (actuals persistently above
   the projection — systematic under-projection). Ratios `r = actual/forecast`, sorted:
   P20 = 0.99, P50 = 1.03, P80 = 1.07. (Note the mean bias +3.5% and the median ratio +3.0% are
   *different statistics*, as they will be on any right-skewed error distribution. Which one you
   correct by matters — see the next section.)
3. **Anchor:** next cycle's inside number is $18.40M. Naive anchor = 18.40 × 1.03 = **$18.95M**.
   The +3.5% bias is not noise — 18 of 22 cycles were same-signed — so anchoring at the raw
   $18.40M would repeat a known, measured error.
4. **Uplift/haircut by use:**
   - Feeding the *expected* cash position: use the anchor, $18.95M.
   - Feeding a *liquidity floor* check (can we cover the payroll run if receipts disappoint?):
     use P20 → 18.40 × 0.99 = **$18.22M**.
   - If this driver were a disbursement, the P80 figure would be the prudent number:
     18.40 × 1.07 = **$19.69M**.
   - **If several drivers are being anchored for one total**, do not add up each driver's P80 —
     see [Aggregation](#aggregation-never-sum-the-p80s). The total takes one contingency at the
     total's own P80.
5. **Log and score:** journal the prediction (number, percentile basis, class, review date); when
   actuals land, compute the realized ratio, note which percentile it fell at, and append the
   cycle to the class.
6. **Decide who fixes the bias — the anchor or the model. Exactly one.** The same-signed run is a
   real finding and it can be acted on in either place, but acting in both double-corrects the
   estimate. See the next section before doing anything with it.

This is the loop-closing move: the forecast process already measures MAPE and bias; this method turns that
measurement into next-cycle anchors and uplifts per driver (tuition receipts, payroll, grant
drawdowns), instead of letting the accuracy history sit unread.

## Correct once, not twice: uplift or curve, never both

The worked example above contains a trap that this method invites, because both of its outputs are
correct in isolation:

- Step 3 multiplies the estimate by the class's P50 ratio (**×1.03**). That uplift *is* the bias
  correction — it exists precisely because the model under-projects.
- Step 6 hands the run of same-signed misses to the model owner as a **+3.5% driver-curve
  correction**, made once with a diagnosis.

Do both and the number carries the correction twice — roughly +6.6% (1.03 × 1.035 = 1.066) where
+3% to +3.5% was warranted. The over-correction is invisible, because each half was signed off by a
different person doing their job correctly.

**The rule: pick the layer, write down which one, and tell the other party.**

| Route | What happens | The anchor becomes |
|---|---|---|
| **(A) Outside-view layer owns it** | The model stays as it is; the reference class keeps measuring its known bias and the anchor keeps carrying the ×1.03. Cheapest, and reversible. | ×1.03 (unchanged) |
| **(B) Model owner fixes the curve** | The driver curve, lag, or calendar is corrected once, with the diagnosis in the journal. The bias should now be ≈0, so the anchor must **drop its bias uplift to ×1.00** for the corrected component. | ×1.00 for bias (spread-based uplifts unaffected) |

Route B has a second consequence that gets missed: **a structural correction invalidates the
reference class.** The class's ratios describe forecasts produced by the *old* curve; once the curve
changes, those cycles are no longer comparable cases — the same "definition change" exclusion the
class-selection rules already require for outcome-independent reasons. So on any accepted structural
correction:

1. **Mark the break date** in the class definition and in the journal.
2. **Start a new class** from the first post-correction cycle. Keep the pre-break cycles as a
   labelled prior segment (they are still evidence about *spread*, which usually survives a level
   correction), but stop using them to compute the *bias* ratio.
3. **Report the class as thin again** — because it is — and follow
   [When the class is thin](#when-the-class-is-thin) until enough post-correction cycles accumulate.
4. **Verify at the next review that the correction worked**, exactly as the special-cause protocol
   in `calibration-and-tampering.md` requires. A curve change is a hypothesis, not a result.

And match the statistic to the route: a curve correction aimed at removing *mean* bias (+3.5%) and
an anchor built on the *median* ratio (+3.0%) are different numbers. Stacking them compounds a
mismatch as well as a duplication.

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
