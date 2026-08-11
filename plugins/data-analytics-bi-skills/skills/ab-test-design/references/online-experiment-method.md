# Online experiment method — design, sizing, and trust checks

Depth for `data-analytics-bi-skills:ab-test-design`. Provenance marks carried from the
research dossier (`docs/research/general-use-expansion-research.md` §2):
**[snippet-only, cross-checked]** = verified via convergent web-search snippets, direct source
fetches egress-blocked at research time. Platform success-rate figures are **self-reported** by
their owners — cite them as reported experience, never as measured industry constants.

## Contents
1. [The design worksheet](#1-the-design-worksheet)
2. [Randomization unit and interference](#2-randomization-unit-and-interference)
3. [OEC and guardrails](#3-oec-and-guardrails)
4. [Worked example — sizing an outreach-letter test](#4-worked-example--sizing-an-outreach-letter-test)
5. [Stopping rules and the peeking problem](#5-stopping-rules-and-the-peeking-problem)
6. [Sample ratio mismatch — the first check, with arithmetic](#6-sample-ratio-mismatch--the-first-check-with-arithmetic)
7. [A/A tests](#7-aa-tests)
8. [Novelty and primacy effects](#8-novelty-and-primacy-effects)
9. [Twyman's law and the trust audit](#9-twymans-law-and-the-trust-audit)
10. [Launch checklist](#10-launch-checklist)

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
itself deserves an A/A test (§7) before its first real A/B.

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
- At 1,000 letters/week total, that is ~13 weeks. If that's unacceptable, the honest moves are
  a bigger MDE (declare "we can only detect ≥4-point swings" — n drops 4× to ~1,600/arm), a
  more sensitive OEC, or more traffic. The dishonest move is running 3 weeks and "seeing."
- Calibrate ambition: the canon's practice guidance is that relative MDEs above ~5% are usually
  wishful — Bing's average effect across tens of thousands of experiments was rarely above
  0.3% [snippet-only, cross-checked]. Small teams testing big, rare changes may legitimately
  target larger effects; the point is to *choose* δ consciously, not inherit it from impatience.
- Pre-register the stop: "we read the scorecard after 6,400/arm or on <date>, whichever is
  later, covering whole weeks."

## 5. Stopping rules and the peeking problem

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

## 6. Sample ratio mismatch — the first check, with arithmetic

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

## 7. A/A tests

Run the full machinery — assignment, logging, metric pipeline, analysis — with *identical*
experiences in both arms (2009 survey paper; 2020 book) [snippet-only, cross-checked]:

- A correctly operating system produces p < 0.05 about **5% of the time** — that is the pass
  condition, not a bug. Many A/A runs (or one long one, re-analyzed on schedule) should show
  roughly uniform p-values.
- What failures mean: frequent "significant" A/A results → broken randomization, correlated
  units (§2 mismatch), or variance mis-estimation; SRM in an A/A → assignment/logging bug found
  *before* it could void a real test.
- When: before the first real experiment on any new assignment mechanism (new flag system, new
  letter-merge process, new routing switch), and periodically thereafter.

## 8. Novelty and primacy effects

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

## 9. Twyman's law and the trust audit

**"Any figure that looks interesting or different is usually wrong."** Attribution, told
honestly because it is itself the lesson: named for UK media/market researcher Tony Twyman, who
apparently never published it; the surviving formulation is Ehrenberg's, in *Data Reduction*
(1975); Kohavi et al. devote a chapter to it as the trust reflex [snippet-only, cross-checked].
An attribution onion atop the very skill of distrusting surprising numbers — teach the chain.

The audit, run *before* celebrating any surprising result: SRM (§6) → instrumentation (did a
logging change land mid-test?) → outliers (one whale account moving a mean) → segment
definitions (did a filter quietly condition on post-treatment behavior?) → duration (§8 curve
still moving?) → only then the statistics. Context for calibrating surprise, self-reported by
platform owners and cited as such: roughly ⅓ of ideas positive / ⅓ flat / ⅓ negative at
Microsoft; ~10–20% success in optimized domains; reported failure rates ranging 66% (Microsoft)
to 92% (Airbnb); and the Bing long-ad-titles change — rated low, backlogged for months, then
+12% revenue when tested (Kohavi & Thomke, *HBR* Sept–Oct 2017) [snippet-only, cross-checked].
The base rate of big wins is low; a big win on your dashboard is more often a bug than a
breakthrough, and checking is cheaper than retracting.

## 10. Launch checklist

- [ ] Decision, variants, and owner written down
- [ ] Randomization unit chosen; interference channels named and contained
- [ ] OEC defined (window, denominator); guardrails with veto thresholds
- [ ] Baseline and variance pulled; MDE chosen consciously; n/arm and duration computed
- [ ] Stopping rule pre-committed (fixed horizon or named sequential method)
- [ ] A/A passed on this machinery
- [ ] SRM chi-square scheduled for every readout
- [ ] Full-cycle coverage planned; exposure-week effect plot planned
- [ ] Twyman audit steps agreed for any surprising result
- [ ] Analysis handoff: `data-analytics-bi-skills:statistical-inference` conventions aligned
      (α, power, one/two-sided, multiplicity policy)
