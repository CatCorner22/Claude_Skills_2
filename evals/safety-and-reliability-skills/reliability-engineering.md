# Evals — safety-and-reliability-skills:reliability-engineering

## 1. Positive trigger (should load the skill)
> "Here's six months of failure timestamps for our overnight batch data feed, plus how
> long each outage took to fix. Compute the MTBF and availability, tell me how much downtime a
> 99.5% target actually allows, and whether a Weibull fit says we should be scheduling anything
> or just adding a backup path."

Expected: skill loads and **classifies the data before fitting anything** — one feed repaired and
returned to service is recurrent-event data, so a Weibull on the gaps between failures is the wrong
model; the trend question belongs to the power-law NHPP (Crow-AMSAA), with a Laplace test or a β̂
interval that will straddle 1 on nine-ish failures. It then runs the math on the pasted log — MTBF,
MTTR, availability = MTBF/(MTBF+MTTR), **with the Poisson (chi-square) interval on the rate**, and
measured downtime vs the 99.5% budget (≈3.65 h/month) read as "probably over, by an amount the
point estimate can't pin down." It looks for structure the averages hide (post-patch clustering
tested as clustering — expected count vs observed — not as a Weibull), lands two failure modes with
two policies (burn-in after patches; attack MTTR plus redundancy for the age-independent
remainder), grants parallel credit for a backup path only if independent failover is demonstrated
and common causes are audited, and flags the two human judgments (data honesty, independence)
explicitly. Correcting the user's framing of "a Weibull fit" is the point of this scenario, not a
deviation from it.

## 1b. Positive trigger (non-repairable population, where Weibull is right)
> "We've had five card readers fail at 55, 70, 85, 95 and 110 days, and forty more still running.
> Should we be replacing these on a schedule, and at what interval?"

Expected: this *is* a non-repairable population, so Weibull applies — with the forty survivors
entered as **censored**, not dropped. Expected behaviour: check the fit (Weibull plot straight?
compare against a lognormal) before quoting β; **bootstrap the fit and attach intervals** to β, η,
and B10; then split the verdict — a β interval that stays above 1 supports "wear-out is real, a
schedule is the right kind of policy," while a B10 interval spanning a factor of three refuses to
support a specific date, so the interval and the cost asymmetry set the interval, not the point
estimate. A bare "B10 = 51 days, replace at 50" with no interval is the failure this scenario
tests.

## 2. Near-miss (should NOT load this skill)
> "Our payment-posting service keeps falling over when the third-party eligibility API is slow —
> add timeouts, retries with backoff, and a circuit breaker so it degrades gracefully."

Expected: qualitative resilience-pattern engineering →
`continuous-improvement-skills:lean-six-sigma-for-software` (its stability-and-redundancy
reference). This skill supplies the *math* under those patterns (how much redundancy an SLO
requires, and the availability/error-budget arithmetic), not the patterns themselves, and that
skill also owns the error budget as a release-governance mechanism. If it loads on
pattern-implementation asks with no quantitative frame, tighten the description.

## 2b. Near-miss (generic-token guard)
> "How reliable is our appointment-recall process? Patients keep slipping through — look
> at the process and tell me where it breaks down."

Expected: a qualitative process-diagnosis ask — root-cause / process-improvement territory
(`continuous-improvement-skills:root-cause-analysis` or value-stream work), with no failure
log, no SLO, and no request for math. Bare "reliable"/"reliability" is a generic token; this
skill's triggers are deliberately quantitative (Weibull, MTBF, availability math, downtime
budget). If it loads here, the trigger surface has grown past the quantitative frame.

## 3. Quality rubric
A good response:
- **Does the task:** states whether the data is a non-repairable population or a repairable system
  and picks the matching model; enters censored/suspended units instead of dropping them; separates
  failure modes before fitting; checks the fit (plot linearity, a rival distribution) before
  quoting a shape parameter; attaches an interval to every quoted β, η, B-life, MTBF and
  availability (bootstrap for the fit, chi-square for the failure rate); reads β to a maintenance
  decision via the right table for the right model (burn-in / run-to-failure + redundancy /
  scheduled replacement at a B-life / calendar renewal for deterministic expiry — or, for a
  repairable system, improving vs stable vs degrading-between-repairs); computes MTBF, MTTR, and
  availability with an honest MTTR clock (detection included); converts the SLO into a downtime
  budget, or an event-based error budget with a burn rate where failure is partial; works series
  arithmetic (chains multiply badly — two 99% steps = 98.01%) naming the independence assumption,
  and grants parallel credit only with demonstrated independent failover.
- **Teaches:** explains β as the hazard exponent that makes the bathtub curve decidable *for a
  unit's own age*, and why the NHPP's β is a different claim about the rate of events on one
  system; why scheduled replacement under β ≈ 1 is waste; why the parallel formula flatters when
  paths share a common cause — "untested failover is scenery" as arithmetic, not slogan — while in
  series the same correlation makes the product the pessimistic end of the range; why MTBF is a
  distribution mean, not a lifetime promise; and why an interval can leave a qualitative claim
  standing while destroying the quantitative one built on it.
- **Stays honest:** states small-sample uncertainty with a method rather than a warning (wide
  bootstrap bounds on few points; the upward bias of rank regression at small n; Weibayes results
  conditional on the assumed β, which is always reported alongside what a different defensible β
  would have given); marks the USAF/Pratt & Whitney small-sample evidence as compiled from
  snippets [snippet-only] and the Crow-AMSAA and event-based-SLI attributions as background to
  verify; leaves data quality and the independence assumption as named human judgments rather than
  assuming them.
