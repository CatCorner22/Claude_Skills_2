# Evals — safety-and-reliability-skills:reliability-engineering

## 1. Positive trigger (should load the skill)
> "Here's six months of failure timestamps for our overnight batch data feed, plus how
> long each outage took to fix. Compute the MTBF and availability, tell me how much downtime a
> 99.5% target actually allows, and whether a Weibull fit says we should be scheduling anything
> or just adding a backup path."

Expected: skill loads; runs the math on the pasted log — MTBF, MTTR, availability =
MTBF/(MTBF+MTTR), measured downtime vs the 99.5% budget (≈3.65 h/month); checks for censoring
and mixed failure modes before fitting; reads β to a policy (post-patch clustering → burn-in;
age-independent remainder → attack MTTR plus redundancy); grants parallel credit for a backup
path only if independent failover is demonstrated and common causes are audited; flags the two
human judgments (data honesty, independence) explicitly.

## 2. Near-miss (should NOT load this skill)
> "Our payment-posting service keeps falling over when the third-party eligibility API is slow —
> add timeouts, retries with backoff, and a circuit breaker so it degrades gracefully."

Expected: qualitative resilience-pattern engineering →
`continuous-improvement-skills:lean-six-sigma-for-software` (its stability-and-redundancy
reference). This skill supplies the *math* under those patterns (how much redundancy an SLO
requires), not the patterns themselves. If it loads on pattern-implementation asks with no
quantitative frame, tighten the description.

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
- **Does the task:** enters censored/suspended units instead of dropping them; separates
  failure modes before fitting; reads β to a maintenance decision via the decision table
  (burn-in / run-to-failure + redundancy / scheduled replacement at a B-life / calendar renewal
  for deterministic expiry); computes MTBF, MTTR, and availability with an honest MTTR clock
  (detection included); converts the SLO into a downtime budget and compares measured against
  it; works series arithmetic (chains multiply badly — two 99% steps = 98.01%) and grants
  parallel credit only with demonstrated independent failover.
- **Teaches:** explains β as the hazard exponent that makes the bathtub curve decidable; why
  scheduled replacement under β ≈ 1 is waste; why the parallel formula flatters when paths
  share a common cause — "untested failover is scenery" as arithmetic, not slogan; why MTBF is
  a distribution mean, not a lifetime promise.
- **Stays honest:** states small-sample uncertainty (wide β bounds on few points; Weibayes
  results conditional on the assumed β, which is always reported); marks the USAF/Pratt &
  Whitney small-sample evidence as compiled from snippets [snippet-only]; leaves data quality
  and the independence assumption as named human judgments rather than assuming them.
