---
name: ab-test-design
description: >-
  Designs trustworthy online controlled experiments — the design half of A/B testing, before any
  data arrives: randomization unit and interference, minimum detectable effect sizing, variance
  reduction with CUPED and stratification, sample ratio mismatch as the first validity check, the
  peeking problem and pre-committed stopping rules, guardrails with an overall evaluation criterion,
  A/A tests, novelty and primacy effects, and Twyman's law. Analysis of a finished test belongs to
  data-analytics-bi-skills:statistical-inference; offline factorial studies to
  continuous-improvement-skills:design-of-experiments. Use when planning a live variant test of a
  page, form, letter, cadence, or process. Triggers: design an A/B test, online experiment design,
  online controlled experiment, sample ratio mismatch, SRM, peeking, minimum detectable effect, MDE,
  CUPED, variance reduction, guardrail metric, A/A test, overall evaluation criterion, OEC,
  Twyman's law, novelty effect.
metadata:
  version: "1.3.0"
  source: >-
    Built from docs/research/general-use-expansion-research.md §2 (general-use expansion wave
    dossier; Kohavi/Tang/Xu canon). Provenance marks carried from the dossier: [snippet-only,
    cross-checked] = verified via convergent web-search snippets (direct fetches were
    egress-blocked at research time). Platform success-rate figures are self-reported by their
    owners and are cited as reported experience, never as measured constants. The
    variance-reduction and winner's-curse material added later carries [canon attribution] =
    author/year named from the canon but not independently re-verified; every number in that
    material is computed in-place from its own stated inputs, never quoted from a source.
---

# A/B test design (online controlled experiments)

## When to use
- Planning a two-variant (or few-variant) test on live traffic or live cases, before any data
  exists: a pricing-page variant, an intake-form version, a dunning/outreach letter, a
  notification cadence, a queue-routing change piloted on a random half of cases.
- Auditing whether a running or finished experiment can be *trusted* — assignment counts,
  stopping behavior, exposure time — before anyone believes its scorecard.
- Not for: analyzing the finished test's numbers — hypothesis tests, p-values, confidence
  intervals → `data-analytics-bi-skills:statistical-inference` (it owns the bare "A/B test"
  request; this skill designs and trust-audits, that one analyzes — and it runs the validity
  gates below as a required step before it will interpret a readout). Multi-factor offline studies
  → `continuous-improvement-skills:design-of-experiments` — the seam: DOE is multi-factor
  physical/process tuning in designed offline bursts; this skill is two-variant online/field
  tests on live units. Perpetual small-step tuning of a live process inside owner-set safe
  limits → `continuous-improvement-skills:evolutionary-operation`. Causal claims where nothing
  was randomized → `data-analytics-bi-skills:causal-inference` (this skill's sibling: it takes
  over exactly where randomization was impossible).
- **The sizing split, stated the same way on all three sides:** sizing a **randomized experiment**
  (MDE → n per arm → duration, where n interacts with the randomization unit, the variance-reduction
  choice, and the stopping rule) is **this skill's**, step 3; **margin-of-error sizing for a survey
  estimate** belongs to `data-analytics-bi-skills:survey-and-sampling-design`;
  `data-analytics-bi-skills:statistical-inference` owns the α/power/effect-size machinery all three
  use, and sizes a **non-randomized** comparison (observational two-group, before/after).

## Do it
Worked sizing, the CUPED variance-reduction arithmetic, the ratio-metric delta method, the SRM
chi-square, stopping-rule options, the Type-M worked example, and the launch checklist are in
`references/online-experiment-method.md`.
1. **Write the decision metric before the variant.** One **overall evaluation criterion (OEC)**
   — the single (possibly composite) metric the decision will ride on — plus **guardrail
   metrics** that must not degrade (complaint rate, latency, unsubscribe rate, error rate,
   downstream workload). A test whose success metric is chosen after the results is not a test.
2. **Choose the randomization unit and check for interference.** User, account, case, matter,
   office, or time-slice — pick the unit on which the effect and the measurement both live, and
   ask whether treated units can contaminate controls (shared queues, shared budgets, word of
   mouth, one clerk handling both letter variants). Interference → randomize at the coarser
   unit that contains it, and note the sample-size price.
3. **Size the test before launch.** Pull the step-1 OEC's **baseline level and variance from
   history** first — nothing downstream is computable without them. Then set the **minimum
   detectable effect** — the smallest change worth acting on — and size with the rule of thumb
   n ≈ 16σ²/δ² per arm (two-sided α=0.05,
   80% power; for a proportion, σ² = p(1−p)) [snippet-only, cross-checked]. If the required
   duration is unacceptable, **reduce the variance before you inflate the MDE** (step 4); only then
   shrink scope honestly (a coarser metric, a bigger MDE stated as such) — never quietly shorten the
   run. Practice guidance from the canon: relative MDEs above ~5% are usually wishful; mature
   platforms report average effects far smaller [snippet-only, cross-checked].
4. **Reduce the variance instead of buying traffic.** Because n scales with σ², cutting variance is
   the one lever that buys power without a bigger MDE, more traffic, or a longer run — and it is the
   canon's first answer, not a footnote.
   - **CUPED** (Deng, Xu, Kohavi & Walker, WSDM 2013) [canon attribution]: adjust each
     unit's outcome with a **pre-experiment** covariate — usually the same metric measured over a
     comparable window before assignment — as `Y' = Y − θ(X − X̄)` with `θ = Cov(Y,X)/Var(X)` fitted
     on the pooled arms. Variance falls by a factor `(1 − ρ²)` where ρ = corr(Y, X): at ρ = 0.7,
     `1 − 0.49 = 0.51`, so the required n roughly **halves** on the same traffic. The estimate stays
     unbiased *only* because X is pre-treatment — never adjust on anything measured after assignment.
   - **Stratification / post-stratification**: block on the covariate (country, plan tier, pre-period
     decile) and combine within-stratum effects; same intuition, coarser instrument.
   - **Regression adjustment (ANCOVA)**: the covariate as a regressor, with treatment×covariate
     interactions on centered covariates so finite-sample bias doesn't creep in (Lin 2013's answer to
     Freedman's critique) [canon attribution].
   - **Pre-specified outlier capping / winsorizing** cuts variance too, but it changes the estimand —
     declare the cap before launch, in writing, and report it.
   - **Get the variance *estimate* right, not just small.** For a user-level **ratio metric** whose
     denominator isn't the randomization unit (clicks per pageview, revenue per session, while
     randomizing on users), the naive standard error treats correlated observations as independent and
     understates it. Use the **delta method** on the ratio of per-unit sums:
     `Var(Ȳ/X̄) ≈ (1/(n·X̄²))·[σ²_Y − 2R·σ_XY + R²·σ²_X]`, with R = Ȳ/X̄ and n = the number of
     randomization units (Deng, Knoblich & Lu, KDD 2018) [canon attribution] — or
     bootstrap/cluster at the unit.
5. **Pre-commit the stopping rule.** Either a fixed horizon (a stop date/sample size, no early
   stopping on significance) or a sequential design built for continuous monitoring
   (always-valid p-values / group-sequential plans). The discipline is "decide the stopping
   rule before the data," not "never look."
6. **Run an A/A test first.** Same experience in both arms: a correctly operating system shows
   p < 0.05 about 5% of the time [snippet-only, cross-checked]. It validates the randomizer,
   the logging, and the analysis pipe before any real variant rides on them.
7. **Check sample ratio mismatch first, every readout.** Compare observed assignment counts to
   the designed split with a chi-square. A failed SRM check voids the scorecard — diagnose the
   assignment/logging bug; do not interpret the metrics (Fabijan et al., KDD 2019 taxonomy)
   [snippet-only, cross-checked].
8. **Run full cycles and watch novelty/primacy.** Cover whole weeks/billing cycles; a treatment
   effect that decays with exposure (novelty) or grows (primacy) means week-one numbers are not
   the long-run answer — run long enough to see the curve flatten before deciding
   [snippet-only, cross-checked].
9. **Apply Twyman's law, discount the winner, then hand off the analysis.** Any figure that looks
   unusually good or interesting gets audited before it gets celebrated — SRM, instrumentation,
   outliers, segment definitions. Then discount what you are about to promise: a barely-significant
   win from an underpowered test **overstates** the effect, because crossing the threshold required
   the noise to help (Type-M exaggeration, Gelman & Carlin 2014) [canon attribution]. A test with
   ~17% power for the true effect, conditional on declaring a win, reports an effect roughly
   **2.5× too large** — worked in
   `references/online-experiment-method.md` §11. So forecast the annual impact from a shrunk estimate
   or the CI's lower bound, and re-measure after rollout. Then the finished, trusted data goes to
   `data-analytics-bi-skills:statistical-inference` for the actual inference — it re-runs the SRM,
   stopping-rule, exposure-window and analysis-unit gates before interpreting anything.

## Why / learn
The canon here is Kohavi, Tang & Xu, *Trustworthy Online Controlled Experiments* (2020), and
the title's first word is the point [snippet-only, cross-checked]. The humbling background
statistic — reported by the platform owners themselves, so cite it as experience, not as a
measured constant — is that roughly a third of tested ideas win, a third do nothing, and a
third hurt, with optimized domains reporting success rates nearer 10–20% [snippet-only,
cross-checked]. The canonical story: a long-ad-titles change at Bing, rated low and left in the
backlog for months, produced a +12% revenue gain when finally tested (Kohavi & Thomke, *HBR*
2017) [snippet-only, cross-checked]. Nobody can pick winners by argument — which is exactly why
the *design* discipline matters more than the analysis: the analysis of a sound test is
routine, while no analysis rescues an unsound one. Each design rule guards a specific way tests
lie. **SRM** catches broken randomization: on a large sample even 50.2/49.8 is not "close
enough" — it is a failed chi-square on assignment, meaning some mechanism (a redirect bug, a
bot filter, a logging drop) sorted units non-randomly, and every downstream metric inherits the
bias. **Peeking** is the subtle one, and the honest version is only half the folklore: watching
a *fixed-horizon* test daily and stopping the moment it crosses p < 0.05 inflates the false
positive rate to roughly five times nominal (Johari et al., KDD 2017) — but peeking under a
*sequential* design built for it (their mSPRT "always-valid p-values"; group-sequential plans)
is legitimate by construction [snippet-only, cross-checked]. The sin is unplanned stopping, not
looking. **A/A tests** exist because the machinery, not the idea, is the usual first failure.
**Variance reduction** is the lever most teams never pull, and the arithmetic explains why it beats the
alternatives: required n scales with σ², so anything that shrinks σ² shrinks n proportionally. CUPED's
mechanism is a covariance argument, not a trick — subtracting `θ(X − X̄)` for a *pre-treatment* X leaves
the treatment effect untouched in expectation (X can't respond to an assignment that hadn't happened yet)
while removing the share of each unit's outcome that its own history already explained, leaving variance
`(1 − ρ²)σ²`. At ρ = 0.7 that is 0.51σ², i.e. half the sample for the same power — which is why "we can't
afford the duration" should be answered with a covariate before it is answered with a bigger MDE. The
mirror-image lesson is that **variance can also be understated**: a ratio metric measured per pageview
while randomizing per user hands the analysis correlated rows dressed as independent ones, and the delta
method (or clustering, or bootstrapping at the unit) is what restores the honest standard error. And once
a winner appears, one more correction is owed: **the effect you ship on is not the effect you measured.**
Significance selects on the estimate, so among barely-significant wins the noise was pulling upward —
the shipped lift is systematically exaggerated (Gelman & Carlin's Type-M error), most severely in exactly
the underpowered tests teams run when traffic is scarce. Discount before you forecast.
And **Twyman's law** — "any figure that looks interesting or different is usually wrong" — is
the trust reflex the whole book builds toward, with an attribution that is itself a lesson in
distrusting neat stories: named for media researcher Tony Twyman, who apparently never
published it; the surviving formulation is Ehrenberg's (*Data Reduction*, 1975); Kohavi's line
of work popularized it [snippet-only, cross-checked]. A skill about distrusting interesting
numbers opens on an interesting attribution that is folklore-adjacent — teach the chain, and
apply the law first to your own scorecard.

## Common mistakes
- Launching without an MDE → an underpowered test that "found nothing" and decided nothing.
  Size first; if the duration is unaffordable, change the design, not the honesty.
- Stopping when the dashboard first crosses p < 0.05 → optional stopping on a fixed-horizon
  design inflates Type I error ~5× [snippet-only, cross-checked]. Pre-commit the rule.
- Shrugging at a 50.2/49.8 split on a big sample → run the chi-square; a failed SRM voids the
  test regardless of how exciting the metrics look.
- Randomizing on one unit and measuring on another (assign page-views, report users) →
  correlated observations and phantom precision. Align the units or account for the clustering.
- Ignoring interference → treated and control units share a queue/team/budget, and the control
  arm is quietly treated too. Randomize at the unit that contains the spillover.
- Declaring victory in week one → novelty effects decay; primacy effects build. Run full cycles
  and look for the asymptote.
- Shipping on the OEC while a guardrail degraded → the composite win hid a real cost. Guardrails
  are veto metrics, not commentary.
- Trusting the first-ever test on new machinery → run the A/A first; ~5% false-positive rate is
  the *pass* condition, not a bug.
- Quoting platform success rates as industry constants → they are self-reported experience;
  directionally convergent, never audited. Hedge them the way the dossier does.
- Answering "the duration is too long" with a bigger MDE before trying variance reduction → CUPED or
  stratification on a pre-experiment covariate can halve required n at ρ ≈ 0.7. Cut σ² first.
- Adjusting on a covariate measured *during* the experiment → it can be affected by treatment, so the
  adjustment biases the effect. CUPED covariates must be strictly pre-assignment.
- Reporting a per-pageview (or per-session) ratio metric from a user-randomized test with naive standard
  errors → understated variance, phantom significance. Delta method, clustering, or bootstrap at the unit.
- Forecasting annual impact from a barely-significant win → underpowered wins exaggerate the effect
  (~2.5× at ~17% power). Shrink the estimate or use the CI's lower bound, and re-measure after rollout.

## Tailor to your environment
Record in `references/your-environment.md` what you actually test (pages, letters, cadences,
process pilots), your randomization units and known interference channels, baseline rates and
variances for MDE sizing, which pre-experiment covariates you can join for CUPED (and their
historical correlation with each OEC), whether any OEC is a ratio metric measured below the
randomization unit, your guardrail set, and who owns launch/stop authority. Keep real
metric values, client identifiers, or live results in `your-environment.private.md`
(git-ignored); commit only sanitized, structural examples.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/ab-test-design.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/online-experiment-method.md — the design worksheet, unit/interference drill, a
  worked MDE sizing (outreach-letter test), variance reduction with CUPED arithmetic and the
  ratio-metric delta method, the SRM chi-square with arithmetic, stopping-rule
  options, OEC/guardrail patterns, A/A mechanics, novelty/primacy, Type-M exaggeration, and the
  launch checklist (provenance marks carried from the dossier)
- references/your-environment.md — your tests, units, baselines, guardrails, and authorities
  (fill in)
