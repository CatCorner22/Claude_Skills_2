---
name: ab-test-design
description: >-
  Designs trustworthy online controlled experiments — the design-and-operations half of A/B
  testing, before any data arrives: randomization unit choice and interference, minimum
  detectable effect (MDE) sizing, sample ratio mismatch (SRM) as the first validity check,
  the peeking problem and pre-committed stopping rules, guardrail metrics plus an overall
  evaluation criterion (OEC), A/A tests, novelty and primacy effects, and Twyman's law.
  Analysis of a finished test (p-values, significance) belongs to
  data-analytics-bi-skills:statistical-inference; offline multi-factor factorial studies
  belong to continuous-improvement-skills:design-of-experiments.
  Use when planning a live variant test of a page, form, letter, cadence, or process. Triggers:
  design an A/B test, online experiment design, online controlled experiment, sample ratio
  mismatch, SRM, peeking, minimum detectable effect, MDE, guardrail metric, A/A test, overall
  evaluation criterion, OEC, Twyman's law, novelty effect.
metadata:
  version: "1.0.0"
  source: >-
    Built from docs/research/general-use-expansion-research.md §2 (general-use expansion wave
    dossier; Kohavi/Tang/Xu canon). Provenance marks carried from the dossier: [snippet-only,
    cross-checked] = verified via convergent web-search snippets (direct fetches were
    egress-blocked at research time). Platform success-rate figures are self-reported by their
    owners and are cited as reported experience, never as measured constants.
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
  request; this skill designs and trust-audits, that one analyzes). Multi-factor offline studies
  → `continuous-improvement-skills:design-of-experiments` — the seam: DOE is multi-factor
  physical/process tuning in designed offline bursts; this skill is two-variant online/field
  tests on live units. Perpetual small-step tuning of a live process inside owner-set safe
  limits → `continuous-improvement-skills:evolutionary-operation`. Causal claims where nothing
  was randomized → `data-analytics-bi-skills:causal-inference` (this skill's sibling: it takes
  over exactly where randomization was impossible).

## Do it
Worked sizing, the SRM chi-square, stopping-rule options, and the launch checklist are in
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
3. **Size the test before launch.** Set the **minimum detectable effect** — the smallest change
   worth acting on — and size with the rule of thumb n ≈ 16σ²/δ² per arm (two-sided α=0.05,
   80% power; for a proportion, σ² = p(1−p)) [snippet-only, cross-checked]. If the required
   duration is unacceptable, shrink scope honestly (a coarser metric, a bigger MDE stated as
   such) — never quietly shorten the run. Practice guidance from the canon: relative MDEs above
   ~5% are usually wishful; mature platforms report average effects far smaller [snippet-only,
   cross-checked].
4. **Pre-commit the stopping rule.** Either a fixed horizon (a stop date/sample size, no early
   stopping on significance) or a sequential design built for continuous monitoring
   (always-valid p-values / group-sequential plans). The discipline is "decide the stopping
   rule before the data," not "never look."
5. **Run an A/A test first.** Same experience in both arms: a correctly operating system shows
   p < 0.05 about 5% of the time [snippet-only, cross-checked]. It validates the randomizer,
   the logging, and the analysis pipe before any real variant rides on them.
6. **Check sample ratio mismatch first, every readout.** Compare observed assignment counts to
   the designed split with a chi-square. A failed SRM check voids the scorecard — diagnose the
   assignment/logging bug; do not interpret the metrics (Fabijan et al., KDD 2019 taxonomy)
   [snippet-only, cross-checked].
7. **Run full cycles and watch novelty/primacy.** Cover whole weeks/billing cycles; a treatment
   effect that decays with exposure (novelty) or grows (primacy) means week-one numbers are not
   the long-run answer — run long enough to see the curve flatten before deciding
   [snippet-only, cross-checked].
8. **Apply Twyman's law, then hand off the analysis.** Any figure that looks unusually good or
   interesting gets audited before it gets celebrated — SRM, instrumentation, outliers,
   segment definitions. Then the finished, trusted data goes to
   `data-analytics-bi-skills:statistical-inference` for the actual inference.

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

## Tailor to your environment
Record in `references/your-environment.md` what you actually test (pages, letters, cadences,
process pilots), your randomization units and known interference channels, baseline rates and
variances for MDE sizing, your guardrail set, and who owns launch/stop authority. Keep real
metric values, client identifiers, or live results in `your-environment.private.md`
(git-ignored); commit only sanitized, structural examples.

## References
- references/online-experiment-method.md — the design worksheet, unit/interference drill, a
  worked MDE sizing (outreach-letter test), the SRM chi-square with arithmetic, stopping-rule
  options, OEC/guardrail patterns, A/A mechanics, novelty/primacy, and the launch checklist
  (provenance marks carried from the dossier)
- references/your-environment.md — your tests, units, baselines, guardrails, and authorities
  (fill in)
