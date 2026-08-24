# Online experiment method — design, sizing, and trust checks

Depth for `data-analytics-bi-skills:ab-test-design`. Provenance marks carried from the
research dossier (`docs/research/general-use-expansion-research.md` §2):
**[snippet-only, cross-checked]** = verified via convergent web-search snippets, direct source
fetches egress-blocked at research time. Platform success-rate figures are **self-reported** by
their owners — cite them as reported experience, never as measured industry constants.
**[canon attribution]** = author/year named from the experimentation canon at authoring time and
**not** independently re-verified (no dossier entry, direct fetches unavailable) — treat the
attribution as a pointer to check before quoting it. No figure in this file is taken from a
[canon attribution] source: every number in §5, §6 and §11 is computed here from its own stated
inputs, so the arithmetic stands even if an attribution needs correcting.

## Contents
1. [The design worksheet](#1-the-design-worksheet)
2. [Randomization unit and interference](#2-randomization-unit-and-interference)
3. [OEC and guardrails](#3-oec-and-guardrails)
4. [Worked example — sizing an outreach-letter test](#4-worked-example--sizing-an-outreach-letter-test)
5. [Variance reduction — CUPED, stratification, adjustment](#5-variance-reduction--cuped-stratification-adjustment)
6. [Ratio metrics and the delta method](#6-ratio-metrics-and-the-delta-method)
7. [Stopping rules and the peeking problem](#7-stopping-rules-and-the-peeking-problem)
8. [Sample ratio mismatch — the first check, with arithmetic](#8-sample-ratio-mismatch--the-first-check-with-arithmetic)
9. [A/A tests](#9-aa-tests)
10. [Novelty and primacy effects](#10-novelty-and-primacy-effects)
11. [Type-M exaggeration — the winner's curse](#11-type-m-exaggeration--the-winners-curse)
12. [Twyman's law and the trust audit](#12-twymans-law-and-the-trust-audit)
13. [Launch checklist](#13-launch-checklist)

## 1. The design worksheet

Fill every line *before* launch; a blank line is a decision you'll otherwise make after seeing
the data, which is where tests quietly rot:

| Field | Entry |
|---|---|
| Decision this test serves | ship / don't-ship what, decided by whom |
| Variants | control (exact current state) + treatment(s) |
| Randomization unit | user / account / case / office / time-slice |
| Interference channels considered | shared queues, budgets, staff, word of mouth |
| OEC | the one decision metric (window and definition fixed) |
| Guardrails | metrics that must not degrade, with veto thresholds |
| Baseline + variance of the OEC | from history |
| MDE | smallest effect worth acting on, in real units |
| n per arm and duration | from §4; full weeks/cycles |
| Stopping rule | fixed horizon date/n, or named sequential method |
| A/A run | date and result |
| SRM check cadence | every readout, chi-square threshold |

The canon behind all of it: Kohavi, Tang & Xu, *Trustworthy Online Controlled Experiments*
(Cambridge UP, 2020); predecessor survey Kohavi et al., *Data Mining and Knowledge Discovery*
18(1) (2009) [snippet-only, cross-checked].

## 2. Randomization unit and interference

Pick the unit on which the effect operates *and* on which you will measure. Candidates, coarse
to fine: site/office → team → account/matter → user → session → page-view. Two rules:

- **Analysis unit = randomization unit**, or account explicitly for the mismatch. Randomizing
  page-views while reporting per-user metrics treats correlated observations as independent —
  the variance is understated and the "significance" is phantom.
- **Interference means the arms are not independent.** If treated units can change what control
  units experience — one clerk handles both letter variants and drifts toward the new script; a
  faster-routed queue steals staff from the control queue; treated users talk to control users —
  the comparison is contaminated. Fix: randomize at the coarser unit that *contains* the
  spillover (per-office instead of per-clerk; per-week time-slices instead of per-case), and
  accept the sample-size price: fewer, chunkier units need bigger effects to detect.

Developer shape: a feature flag is the randomization unit's implementation — the flag
assignment IS the experiment assignment, exposure logs are the denominator, and the flag system
itself deserves an A/A test (§9) before its first real A/B.

## 3. OEC and guardrails

The **overall evaluation criterion** is the single metric (possibly a weighted composite) the
ship decision rides on — terminology popularized by the Kohavi line of papers and the 2020 book
[snippet-only, cross-checked]. Choose it for: sensitivity within the test's horizon,
directional agreement with long-term value, and resistance to gaming (clicks are sensitive but
gameable; long-run retention is faithful but too slow — composites trade these off).

**Guardrails are veto metrics, not commentary.** Typical sets, domain-neutral:
- Outreach/letter test: OEC = response or payment within 30 days; guardrails = complaint rate,
  opt-out/unsubscribe rate, escalations.
- Pricing-page variant: OEC = completed purchases per visitor; guardrails = refund rate,
  support contacts, page latency.
- Queue/process pilot: OEC = cycle time; guardrails = error/rework rate, staff overtime,
  customer-visible misses.

A treatment that wins the OEC while breaching a guardrail does not ship — that rule is decided
now, in writing, not renegotiated in front of a green dashboard.

## 4. Worked example — sizing an outreach-letter test

Two variants of a follow-up letter (collections, client intake, donor renewal — same
arithmetic). OEC: response within 30 days. Historical baseline p = 0.20. The team decides the
smallest effect worth a template change is **2 percentage points absolute** (δ = 0.02, i.e., a
10% relative lift). *(Baseline and MDE illustrative; the formula and its conditions are the
dossier-verified content.)*

Rule of thumb (Kohavi, Deng, Longbotham & Xu, "Seven Rules of Thumb for Web Site
Experimenters," KDD 2014): **n ≈ 16σ²/δ² per arm** for two-sided α = 0.05 at 80% power
[snippet-only, cross-checked]. For a proportion, σ² = p(1−p):

- σ² = 0.20 × 0.80 = 0.16
- n ≈ 16 × 0.16 / (0.02)² = 2.56 / 0.0004 = **6,400 per arm** (~12,800 letters total)

Consequences to confront *now*:
- At 1,000 letters/week total, that is ~13 weeks. If that's unacceptable, the moves in order are:
  **cut the variance** (§5 — CUPED/stratification on a pre-period covariate; measure ρ on your own
  history before assuming a reduction, because a binary response rate like this one typically sits at
  ρ ≈ 0.1–0.3 and buys ~9%, not the ~49% a continuous metric would), then a **bigger MDE** (declare "we can only detect
  ≥4-point swings" — n drops 4× to ~1,600/arm), then a **more sensitive OEC**, then **more traffic**.
  The dishonest move is running 3 weeks and "seeing."
- Calibrate ambition: the canon's practice guidance is that relative MDEs above ~5% are usually
  wishful — Bing's average effect across tens of thousands of experiments was rarely above
  0.3% [snippet-only, cross-checked]. Small teams testing big, rare changes may legitimately
  target larger effects; the point is to *choose* δ consciously, not inherit it from impatience.
- Pre-register the stop: "we read the scorecard after 6,400/arm or on <date>, whichever is
  later, covering whole weeks."

## 5. Variance reduction — CUPED, stratification, adjustment

Sizing scales with **σ²** (`n ≈ 16σ²/δ²`), so halving the variance halves the sample for the same MDE.
This is the canon's first answer to "we can't afford the duration," and the one most often skipped.

**CUPED** — *Controlled-experiment Using Pre-Experiment Data* (Deng, Xu, Kohavi & Walker, WSDM 2013)
[canon attribution]. For each unit take a **pre-assignment** covariate `X` (best choice: the
same metric over a comparable window before the test) and analyse the adjusted outcome

```
Y' = Y − θ (X − X̄)          with θ = Cov(Y, X) / Var(X),  X̄ and θ pooled across both arms
```

- **Why it's unbiased:** `X` is measured before assignment, so its distribution is the same in both arms
  in expectation; subtracting a function of it removes variance, not signal. Adjust on anything measured
  *after* assignment and you can absorb part of the treatment effect — that is the one way to get this
  wrong, and it is fatal.
- **How much it buys:** `Var(Y') = Var(Y)(1 − ρ²)` where `ρ = corr(Y, X)`. Applied to §4's 6,400/arm:

| ρ (pre-period vs in-test metric) | variance multiplier `1 − ρ²` | n needed vs unadjusted | 6,400/arm becomes |
|---|---|---|---|
| 0.3 | 0.91 | 91% | 5,824 |
| 0.5 | 0.75 | 75% | 4,800 |
| 0.7 | 0.51 | 51% | 3,264 |
| 0.9 | 0.19 | 19% | 1,216 |

Each row is `6,400 × (1 − ρ²)`: 0.91 → 5,824; 0.75 → 4,800; 0.51 → 3,264; 0.19 → 1,216.

**Which row you are on depends on the metric type, and §4's worked example is not on the ρ = 0.7 row.**
ρ ≈ 0.5–0.8 is routine for a *continuous* per-unit metric — spend, sessions, revenue — where a unit's
pre-period value genuinely predicts its in-test value. §4 sizes a **binary response rate** (p = 0.20),
and a 0/1 indicator across waves typically correlates with its own pre-period at **ρ ≈ 0.1–0.3**: the
outcome carries one bit, most of its variance is irreducible Bernoulli noise, and there is no
per-unit magnitude for the covariate to track. That is the top row — a **9% reduction, to ~5,824/arm**,
not 51%. For a fresh outreach campaign it is usually worse, because the same bullet below applies: units
with no pre-period take X = 0 and dilute ρ further, and on a new campaign that is most of the file.

So do not carry a number down from this table into a plan. **Measure ρ on your own history first, then
re-size** — it is a single regression of this period's metric on the prior period's for the same units,
and it costs less than discovering mid-test that the sample was set for a variance reduction that never
arrived.

- **Where ρ comes from:** measure it on history *before* the test (regress this period's metric on the
  prior period's for the same units). Units with no pre-period (new users, first-time cases) get X = 0 or
  an imputed value, which dilutes ρ — report the share of units without history.
- **Practical notes:** fit θ once on the pooled arms (fitting it per-arm reintroduces the treatment into
  the adjustment); the point estimate of the effect is essentially unchanged while the CI narrows; and
  CUPED composes with the sequential/fixed-horizon choice in §7 rather than replacing it.

**Stratification / post-stratification.** Block units on a pre-experiment variable (region, plan tier,
pre-period decile), estimate the effect within each stratum, and combine with stratum weights. Same
covariance intuition, coarser instrument, no θ to fit — useful when the covariate is categorical or the
pipeline can't carry a continuous adjustment.

**Regression adjustment (ANCOVA).** Put the covariate in a regression alongside the treatment indicator.
Include **treatment × centered-covariate interactions** — Lin (2013) shows that form is never worse
asymptotically than the unadjusted difference in means, which answers Freedman's finite-sample critique
of naive OLS adjustment [canon attribution].

**Pre-specified capping / winsorizing.** Trimming a heavy tail cuts σ² sharply, but it *changes the
estimand* (you are no longer measuring the mean of the full distribution). Legitimate only if declared
before launch, with the cap and its rationale in the design worksheet, and reported in the readout.

**What variance reduction is not:** it does not fix interference, a broken randomizer, a mismatched
analysis unit, or an unplanned stop. It only buys power.

## 6. Ratio metrics and the delta method

Cutting variance is half the job; *estimating* it correctly is the other half. When the OEC is a **ratio**
whose denominator is finer than the randomization unit — clicks per pageview, revenue per session, minutes
per case, while randomizing on users/accounts — treating the fine-grained rows as independent understates
the standard error and manufactures significance.

Two correct routes:

1. **Aggregate then delta method.** Compute each randomization unit's numerator sum `Yᵢ` and denominator
   sum `Xᵢ`; those `n` unit-level pairs are the independent observations. For `R = Ȳ/X̄`:

   ```
   Var(R) ≈ (1 / (n · X̄²)) · [ σ²_Y − 2R·σ_XY + R²·σ²_X ]
   ```

   (the first-order Taylor expansion of `Ȳ/X̄`; Deng, Knoblich & Lu, "Applying the delta method in metric
   analytics," KDD 2018) [canon attribution]. Note it needs the **covariance** term — dropping
   it is the common half-fix, and it can err in either direction.
2. **Cluster or bootstrap at the unit.** Cluster-robust standard errors, or a bootstrap that resamples
   whole randomization units, get the same protection without the algebra.

The failure this prevents is the same one `data-analytics-bi-skills:statistical-inference` gates on
(analysis unit = randomization unit) — design it here so the analysis doesn't have to rescue it.

## 7. Stopping rules and the peeking problem

Watching a fixed-horizon test continuously and stopping the moment p < 0.05 inflates the Type I
error to roughly **5× nominal** (Johari, Koomen, Pekelis & Walsh, "Peeking at A/B Tests," KDD
2017) [snippet-only, cross-checked]. Intuition: each look is another chance for noise to cross
the line; take enough looks and noise always does. Popular precursor: Evan Miller, "How Not To
Run An A/B Test" (2010) [snippet-only, cross-checked].

The honest framing — load-bearing, from the dossier: **"peeking is cheating" is only half
true.** The sin is *unplanned stopping on a fixed-horizon design*. Legitimate options, chosen
before launch:

1. **Fixed horizon, hands off.** Pre-registered n/date; dashboards may display "no decision
   before <date>" but nobody acts early. Simplest; fine for letter tests and process pilots.
2. **Sequential by construction.** Always-valid p-values (the mSPRT of Johari et al., shipped
   in Optimizely from January 2015 [snippet-only, cross-checked]) or group-sequential plans
   with pre-set interim looks and adjusted thresholds. Continuous monitoring is then valid by
   design — the price is somewhat larger samples for the same power.

Rule: decide the stopping rule before the data, then obey it. A "significant" result obtained
by rule-breaking is not evidence; it is the peeking artifact wearing a decision's clothes.

## 8. Sample ratio mismatch — the first check, with arithmetic

Designed split 50/50; the scorecard is read only after this check passes. Compare observed
assignment counts to expected with a one-degree-of-freedom chi-square:

χ² = Σ (observed − expected)² / expected

Worked numbers: 50,000 units, expected 25,000/25,000, observed **25,300 / 24,700** (a
"harmless-looking" 50.6/49.4):

- χ² = 300²/25,000 + 300²/25,000 = 3.6 + 3.6 = **7.2** → p ≈ 0.007. **Failed.**
- At larger scale even 50.2/49.8 fails: 1,000,000 units, observed 502,000/498,000 gives
  χ² = 2,000²/500,000 × 2 = **16** → p ≈ 0.00006. "Close to 50/50" is not a percentage
  judgment; it is a chi-square judgment scaled by n.

A failed SRM check means the *assignment process* is biased — a redirect that drops slow
clients from one arm, a bot filter that fires asymmetrically, a logging path that loses
exposures — and every metric downstream inherits the bias, usually in an unknowable direction.
The response is diagnosis, never interpretation: Fabijan et al., "Diagnosing Sample Ratio
Mismatch in Online Controlled Experiments" (KDD 2019) gives the practitioner taxonomy of causes
drawn from four companies / 25+ products [snippet-only, cross-checked]. Practitioner write-ups
report SRM in roughly 6–10% of tests — a soft, self-reported figure; treat it as "common enough
to check every time," not as a constant [snippet-only, cross-checked]. SRM is Twyman's law
applied to your own scorecard: the most interesting number on it may be the assignment split.

## 9. A/A tests

Run the full machinery — assignment, logging, metric pipeline, analysis — with *identical*
experiences in both arms (2009 survey paper; 2020 book) [snippet-only, cross-checked]:

- A correctly operating system produces p < 0.05 about **5% of the time** (across independent
  replicates) — that is the pass condition, not a bug. **Many independent A/A runs** should
  show roughly uniform p-values: separate runs, disjoint time windows analyzed independently,
  or repeated re-randomization of one historical exposure log. Do not substitute one long run
  re-analyzed on a schedule — nested looks at an accumulating sample are the §7 peeking setup
  and will condemn a healthy randomizer.
- What failures mean: frequent "significant" A/A results → broken randomization, correlated
  units (§2 mismatch), or variance mis-estimation; SRM in an A/A → assignment/logging bug found
  *before* it could void a real test.
- When: before the first real experiment on any new assignment mechanism (new flag system, new
  letter-merge process, new routing switch), and periodically thereafter.

## 10. Novelty and primacy effects

Two time-shapes that make early readouts lie (2009 survey; formal long-term estimator in
Sadeghi et al., *Technometrics* 2022) [snippet-only, cross-checked]:

- **Novelty:** the effect decays with exposure — users click the new thing because it is new;
  staff over-comply with the new process while it is watched. Week-one lift, month-three
  nothing.
- **Primacy:** the effect grows with exposure — the change is initially disruptive (retraining,
  habit friction) and pays off only after adaptation. Week-one dip, month-three win.

Discipline: plot the treatment effect *by exposure week*, not just cumulatively; run long
enough to see the curve flatten; and treat any decision made on a still-moving curve as
provisional. Cover whole weeks/cycles regardless — day-of-week and cycle mix are the cheapest
confounders to avoid.

## 11. Type-M exaggeration — the winner's curse

A test that passes its significance bar has been **selected on its estimate**, and selection biases what
you ship on. Gelman & Carlin (2014) name this the **Type-M (magnitude) error**, alongside Type-S (sign)
— the questions "how exaggerated?" and "could the direction be wrong?" that a plain power number
doesn't answer [canon attribution].

Mechanism, with the arithmetic done here. Two-sided α = 0.05 means you declare a win only when
`|δ̂| ≥ 1.96 SE`. Suppose the **true** effect is `δ = 1.0 SE` — an ordinary underpowered situation:

- **Power** = `P(Z > 1.96 − 1) + P(Z < −1.96 − 1)` = `P(Z > 0.96) + P(Z < −2.96)`
  = `0.1685 + 0.0015` ≈ **17%**.
- **What the winners report.** Conditional on `δ̂ > 1.96 SE`, the expected estimate is
  `δ + SE · φ(0.96)/(1 − Φ(0.96))` = `SE · (1 + 0.2516/0.1685)` = `SE · (1 + 1.49)` ≈ **2.49 SE** —
  about **2.5×** the true effect of 1.0 SE. (Truncated-normal mean; the ~0.15% wrong-sign tail ignored.)
- The exaggeration shrinks as power rises: it is a property of *underpowered* winners, which is exactly
  the regime a traffic-starved team operates in — and exactly when the roll-out business case gets written.

What to do with it:
- **Discount before forecasting.** Project annual impact from the CI's lower bound, or from a shrunk
  (empirical-Bayes style) estimate, not from the point estimate that won.
- **Re-measure after rollout.** A holdback slice or a re-test on fresh traffic is the only honest
  confirmation; the second measurement is not selected on its own significance.
- **Or fix the cause:** power the test properly (§4–§5). Variance reduction is a Type-M countermeasure as
  well as a duration one — higher power means less exaggeration in the wins you keep.
- **Never** report the winning estimate as the expected future lift without saying which of the above
  you did.

## 12. Twyman's law and the trust audit

**"Any figure that looks interesting or different is usually wrong."** Attribution, told
honestly because it is itself the lesson: named for UK media/market researcher Tony Twyman, who
apparently never published it; the surviving formulation is Ehrenberg's, in *Data Reduction*
(1975); Kohavi et al. devote a chapter to it as the trust reflex [snippet-only, cross-checked].
An attribution onion atop the very skill of distrusting surprising numbers — teach the chain.

The audit, run *before* celebrating any surprising result: SRM (§8) → instrumentation (did a
logging change land mid-test?) → outliers (one whale account moving a mean) → segment
definitions (did a filter quietly condition on post-treatment behavior?) → duration (§10 curve
still moving?) → only then the statistics. Context for calibrating surprise, self-reported by
platform owners and cited as such: roughly ⅓ of ideas positive / ⅓ flat / ⅓ negative at
Microsoft; ~10–20% success in optimized domains; reported failure rates ranging 66% (Microsoft)
to 92% (Airbnb); and the Bing long-ad-titles change — rated low, backlogged for months, then
+12% revenue when tested (Kohavi & Thomke, *HBR* Sept–Oct 2017) [snippet-only, cross-checked].
The base rate of big wins is low; a big win on your dashboard is more often a bug than a
breakthrough, and checking is cheaper than retracting.

## 13. Launch checklist

- [ ] Decision, variants, and owner written down
- [ ] Randomization unit chosen; interference channels named and contained
- [ ] OEC defined (window, denominator); guardrails with veto thresholds
- [ ] Baseline and variance pulled; MDE chosen consciously; n/arm and duration computed
- [ ] Variance reduction decided: CUPED covariate (pre-assignment only) with its measured ρ,
      stratification, or ANCOVA — and the revised n; any capping rule pre-specified
- [ ] Ratio-metric standard errors planned (delta method / cluster / bootstrap at the randomization unit)
- [ ] Stopping rule pre-committed (fixed horizon or named sequential method)
- [ ] A/A passed on this machinery
- [ ] SRM chi-square scheduled for every readout
- [ ] Full-cycle coverage planned; exposure-week effect plot planned
- [ ] Twyman audit steps agreed for any surprising result
- [ ] Winner's-curse policy agreed: what gets forecast from a barely-significant win, and the
      holdback/re-measure plan
- [ ] Analysis handoff: `data-analytics-bi-skills:statistical-inference` conventions aligned
      (α, power, one/two-sided, multiplicity policy) and its validity gates (SRM counts, the
      stopping rule as followed, exposure window, analysis unit) supplied with the data
