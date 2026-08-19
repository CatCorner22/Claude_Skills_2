# Reliability math — formulas and worked examples

All worked examples use synthetic, sanitized data — structure only, no real feeds, incidents,
or accounts.

Contents: §1 First question: repairable or not · §2 The Weibull model (non-repairable) ·
§3 Fitting failure data, checking the fit, and bounding it · §4 The β decision table ·
§4b Dormant protective functions and the proof-test interval ·
§5 Recurrent failures of one repairable system: the power-law NHPP · §6 MTBF, MTTR,
availability (time-based and event-based), and the SLO downtime-budget table ·
§7 Series/parallel arithmetic · §8 Weibayes (tiny samples) · §9 Worked case: an overnight
feed failure log · §10 Provenance and evidence

## §1 First question: repairable or not

Answer this before choosing any formula, because the two cases use different models and the
same Greek letter means different things in each.

| | **Non-repairable population** | **Repairable system** |
|---|---|---|
| Data shape | Many units, each contributing **one** time-to-first-failure (plus censored survivors) | **One** system (or a few), each contributing a *sequence* of failure times — it is repaired and put back in service |
| Examples | Certificates, disks, pumps, one-shot devices; also "each patch cycle until its first failure" if cycles are independent | A data feed, a scheduled job, a service, a machine kept running by maintenance |
| Model | **Weibull** time-to-failure (§2–§3) | **Recurrent-event** model: power-law NHPP / Crow-AMSAA (§5), or a renewal process if repair truly restores as-good-as-new |
| What the shape parameter means | Hazard shape *within one lifetime*: β>1 = each unit's risk rises with its own age | Trend in the *rate of events* on one system: β>1 = failures arriving faster over time, i.e. repairs are not restoring it |
| Right summary | R(t), B-lives, MTTF | Failure intensity u(t), cumulative and instantaneous MTBF |

The common mistake is to take one repaired system's nine failure gaps, treat them as nine
lifetimes, and fit a Weibull. That estimate mixes the hazard shape with the reliability
trend, and then the β→policy table in §4 gets read off a parameter that does not mean what
the table says. If your data is one system's repeated failures, you are in §5. If you can
honestly describe your data as a *population of units each observed until its first failure*,
you are in §2–§3.

## §2 The Weibull model (non-repairable populations)

Two parameters: shape **β** and scale **η** (the characteristic life — by t = η, 63.2% of
units have failed, at any β).

- Reliability (survival): R(t) = exp[−(t/η)^β]
- Cumulative failure: F(t) = 1 − R(t)
- Hazard (instantaneous failure rate): h(t) = (β/η)(t/η)^(β−1)

β is the exponent of the hazard: β < 1 → falling hazard, β = 1 → constant (the exponential
distribution as a special case), β > 1 → rising hazard. That is the entire bathtub curve in
one parameter — for a *unit's own age*.

**B-lives:** B10 is the age by which 10% fail — B10 = η·(−ln 0.9)^(1/β). Replacement
intervals are usually set at a B-life, not at MTBF.

## §3 Fitting failure data, checking the fit, and bounding it

**Median-rank regression (hand-checkable).** Sort the n failure times ascending. Give the
i-th failure the median rank F̂ᵢ ≈ (i − 0.3)/(n + 0.4). Plot y = ln ln[1/(1−F̂)] against
x = ln t, then fit the line. Abernethy's handbook fits **x on y** ("rank regression on X") on
the argument that t is the measured quantity carrying the error, so β = 1/slope; fitting y on
x instead makes β = slope. Either way η = exp(x̄ − ȳ/β).

Worked fit — five failure times (days): 55, 70, 85, 95, 110.

| i | tᵢ | F̂ᵢ | x = ln tᵢ | y |
|---|----|------|-----------|-----|
| 1 | 55 | 0.1296 | 4.0073 | −1.9745 |
| 2 | 70 | 0.3148 | 4.2485 | −0.9727 |
| 3 | 85 | 0.5000 | 4.4427 | −0.3665 |
| 4 | 95 | 0.6852 | 4.5539 | +0.1448 |
| 5 | 110 | 0.8704 | 4.7005 | +0.7145 |

- Rank regression on X: **β = 3.84, η = 91.7 days**, B10 = 51.0 days.
- Regression of y on x: β = 3.83, η = 91.7 days, B10 = 51.0 days.

The two agree to 0.3% here only because these five points are nearly collinear (r² = 0.998);
the gap widens with scatter, so state which direction you fitted. Do not treat the agreement
as validation of either.

### Does the Weibull even fit? (do this before quoting β)

1. **Look at the plot.** On Weibull paper the points should be straight. Systematic curvature
   is information, not noise: a concave/convex sweep often means a **failure-free period** (a
   three-parameter Weibull with threshold t₀), a distinct **knee with two straight segments**
   almost always means **two failure modes** mixed in one dataset (split them and fit each), and
   a flattening tail usually means censoring was handled wrongly.
2. **Compare against a rival distribution.** The lognormal is the usual competitor. Plot
   x = ln t against z = Φ⁻¹(F̂) and compare r². On this dataset: **Weibull r² = 0.9976,
   lognormal r² = 0.9806** — Weibull fits better, and the honest gloss is that a 0.017
   difference on five points settles nothing. Both plots look straight to the eye at n = 5.
3. **Don't use r² as proof.** With few points r² is high almost regardless; it is a check for
   gross misfit, not evidence of the right family. (Abernethy's handbook supplies critical
   correlation-coefficient thresholds for this test `[background — verify before citing]`.)
4. **The strongest fit check is physical.** Does a rising hazard match a mechanism you can
   name — fatigue, corrosion, log growth, queue growth, cache filling? A β > 1 with no
   candidate mechanism is a hypothesis, not a finding.

### Censoring

Units still running at the analysis date and units removed unfailed are suspensions. In rank
methods they consume rank positions without plotting (adjusted ranks); in MLE they contribute
survival probability R(t) instead of density. Either way they must be in the dataset — a fit
on failures alone answers a different question ("of the ones that failed, when?") than the
one you asked ("when will these fail?").

### Putting bounds on β, η, and B10 — a bootstrap

A point estimate with no interval cannot support a policy. The most teachable interval is a
**parametric bootstrap**, which needs no distribution theory and works for any derived
quantity (B10, MTTF, a survival probability at some age):

1. Fit β̂, η̂ from your data.
2. Draw a synthetic sample of the **same size n** from Weibull(β̂, η̂):
   t = η̂ · (−ln U)^(1/β̂) with U uniform on (0,1).
   - **If your data are censored, you must simulate the censoring too, or the interval is wrong.**
     This draw produces complete lifetimes only. Resampling a censored fit as if every unit had
     failed throws away the suspensions, so the synthetic samples carry more information than the
     real one and the resulting interval comes out **too narrow** — it will understate the
     uncertainty in β exactly where reliability decisions are most sensitive to it. Simulate the
     observation scheme, not just the lifetimes: draw t as above, draw or reuse each unit's censoring
     time c (its real inspection age or time in service), and record `min(t, c)` with the indicator
     `t <= c`. Then step 3's "same estimator" is genuinely the same estimator — the censored MLE —
     applied to data of the same shape.
3. Refit with **the same estimator** and record β*, η*, B10*.
4. Repeat a few thousand times. The 2.5th and 97.5th percentiles of each collection are a 95%
   percentile interval. Report the number of resamples — the last digit is Monte Carlo noise.

On the five-point fit above (20,000 resamples, rank regression on X, reproduced across two
seeds):

| Quantity | Point estimate | 95% bootstrap interval | Span |
|---|---|---|---|
| β | 3.84 | **1.7 – 11.0** | 6.4× |
| η | 91.7 days | 69 – 113 days | 1.6× |
| B10 | 51.0 days | **22 – 81 days** | 3.6× |

Two things fall out of that table, and both change the recommendation:

- **The wear-out claim survives.** About 0.02% of resamples put β below 1, so "the hazard rises
  with age" is supportable from five points. Scheduled replacement is the right *kind* of
  policy here.
- **The 50-day interval does not survive.** B10 is somewhere between about three weeks and
  three months. So the honest prescription is *"wear-out is real; a scheduled replacement is
  justified; the interval is provisional at ~50 days with a plausible range of 22–81 days —
  set it from the cost asymmetry (nearer 22 if an in-service failure is expensive, nearer 81 if
  early replacement is) and re-fit as failures accumulate."* Not "replace at 50 days."
- The estimator is also **biased upward at small n**: the mean bootstrap β is 4.48 against a
  point estimate of 3.84, about +17%, so the fit leans steeper than the truth. (B10 came out
  roughly median-unbiased here — bootstrap median 50.7 vs point 51.0 — because the β and η
  biases partly cancel in it. Check the quantity you actually quote; do not assume.)

**Small-sample honesty.** With n ≤ ~10, β carries wide bounds — as the table shows, wider than
most people guess. A fitted β of 1.2 on five points does not establish wear-out: its bounds
straddle 1, so treat it as random hazard until more data arrives, or use Weibayes (§8) with a
β you can defend. The rule this file follows: **no policy recommendation without an interval
attached, and no interval without saying how it was produced.**

## §4 The β decision table

Read this table only for a **non-repairable** fit (§2–§3) — for one repaired system, use §5's
interpretation instead.

**And only for an item whose failure is *announced*.** Everything in this table assumes you
find out when the thing breaks — that is what makes "run to failure" a policy rather than a
gamble. A protective function that sits idle and acts only on demand (see §4b) breaks the
assumption completely, and the β ≈ 1 row is actively wrong for it.

| β | Regime | Typical causes | Policy |
|---|--------|----------------|--------|
| β < 1 | Infant mortality | Bad installs, fresh patches, config errors, manufacturing defects | Burn-in / shake-down before trusting; fix the defect source; no scheduled replacement |
| β ≈ 1 | Random | External shocks, load spikes, operator error — age-independent | Run-to-failure + redundancy + fast repair (attack MTTR); scheduled replacement buys nothing |
| 1 < β ≲ 4 | Early-to-steady wear-out | Fatigue, corrosion, drift, queue growth | Scheduled replacement/refresh at a B-life; condition monitoring |
| β ≫ 4 | Steep wear-out | Tight physical wear mechanisms | Hard replacement interval just below the knee |
| β → ∞ | Deterministic expiry | Certificates, passwords, key rotations, license lapses | Calendar-driven renewal, alarmed well ahead — treat the date as the failure time |

Post-patch failure clustering is the software analogue of infant mortality: if failures pile
up in the days after each patch window, the answer is a burn-in step (run against test input
before trusting the window), not more redundancy. Note the modelling care that claim needs —
"time since patch" is only a lifetime clock if each patch cycle is treated as a unit in its own
right, with cycles that survived the whole window entered as censored (§9).

## §4b Dormant protective functions: the failure you do not hear about

Every model above is for something that runs. A large class of the things reliability work
actually cares about does not run: the interlock, the relief valve, the alarm, the failover
path, the backup restore, the smoke detector, the escalation rule that fires only when the
primary misses. These sit idle and are asked to act **on demand**. Their failures are
**hidden** — nothing tells you the valve seized, because nothing has asked it to move.

That breaks the table's arithmetic in a specific way. `A = MTBF/(MTBF + MTTR)` prices repair
time, and MTTR is measured from when you *noticed*. For a dormant item nobody notices, so the
"down" period is not the repair — it is everything from the moment it failed until the moment
someone next exercises it. The β ≈ 1 row therefore reads exactly backwards: "run-to-failure,
attack MTTR, scheduled replacement buys nothing" is sound advice for a running item with a
constant hazard, and for a dormant one it means *never find out*.

**The governing quantity is the probability of failure on demand (PFD): the chance the
function is already broken when it is finally called.** For a constant hazard rate λ and a
proof-test interval T — the interval at which you deliberately exercise the function and
repair what you find — the standard approximation is

> **PFD_avg ≈ λT / 2**

with the average taken over the interval, because the item is fresh just after a test and
worst just before the next one. The lever in that expression is not λ and not repair speed.
**It is T.** Halving the test interval roughly halves the average unavailability; adding
redundancy without ever testing it adds a second thing that can be silently dead. This is why
"how often do we actually exercise it?" is the only question that moves the number, and why an
untested backup, an untested failover and an untested escalation path are all the same object.

Three consequences worth carrying:

- **A test that does not exercise the real function is not a proof test.** Checking that the
  monitoring job ran green is not testing the alarm; restoring a file is testing the backup.
  The test must invoke the same path the demand would.
- **Redundancy multiplies only if the redundant elements are tested and fail independently.**
  Two channels on the same power supply, the same firmware, or the same untested assumption
  are one channel. Common-cause failure is what dominates redundant protective systems in
  practice.
- **Staggered testing beats simultaneous testing.** Proof-testing every channel on the same
  day maximises the window in which they are all equally stale.

Cross-references: `safety-and-reliability-skills:bowtie-barrier-analysis` requires an assurance
test per barrier and defaults to quarterly — `PFD_avg ≈ λT/2` is the arithmetic behind
choosing that interval rather than inheriting it, and it is how you tell which barriers deserve
a shorter one. `safety-and-reliability-skills:rebuild-rehearsal` is the same idea applied to
knowledge and process: a capability nobody exercises is a dormant function, and its rehearsal
cadence is its proof-test interval.

[The PFD_avg ≈ λT/2 approximation and the proof-test framing are standard functional-safety
material (the IEC 61508 / 61511 family). Canon attribution — stated here for the shape of the
reasoning, not re-derived; a system with a safety-integrity-level requirement needs the full
treatment and a competent assessor, not this paragraph.]

## §5 Recurrent failures of one repairable system: the power-law NHPP

When one system fails, gets repaired, and fails again, the object to model is the **failure
intensity** u(t) — events per unit time as a function of the system's age — not a lifetime
distribution. The standard model is the **power-law non-homogeneous Poisson process**, known in
reliability-growth work as **Crow-AMSAA** (it is the statistical footing under Duane's
observation that cumulative MTBF plots straight on log-log paper)
`[background — verify before citing]`:

- cumulative expected failures: **N(t) = λ t^β**
- failure intensity: **u(t) = λ β t^(β−1)**

**MLE for one system observed to time T with n failures at t₁ … tₙ (time-terminated):**

> **β̂ = n ÷ Σᵢ ln(T / tᵢ)**  and  **λ̂ = n ÷ T^β̂**

(If you stopped *at* the nth failure instead, the observation window is tₙ itself and the sum
collapses to the n−1 earlier failures: β̂ = n ÷ Σᵢ₌₁ⁿ⁻¹ ln(tₙ/tᵢ).)
Both of those are maximum-likelihood estimates and both lean **high** at small n —
E[β̂] = β·n/(n−1) time-terminated, β·n/(n−2) failure-terminated — so below about ten failures
quote the bias-corrected form beside the MLE: multiply β̂ by (n−1)/n when you stopped at a clock
time, by (n−2)/n when you stopped at a failure. **The failure-terminated factor needs n ≥ 3 and
is still violent at n = 3**: it multiplies by (n−2)/n, which is 0 at n = 2 (any β̂ collapses to
zero) and 1/3 at n = 3, so a β̂ of 1.00 reads as 0.33. Below about five failures report the raw
MLE with its interval and say the small-sample bias runs high; do not publish a "corrected"
number that the correction itself has destroyed. On §9's log that turns β̂ = 0.86 into 0.76,
which does not change the reading (the interval straddles 1 either way) but does show which
direction the small-sample error runs.
An approximate standard error is SE(β̂) ≈ β̂/√n, so **n = 9 failures gives roughly ±30%** on β
— enough to spot a strong trend, never enough to grade a weak one.

**What β means here, and why it is not the Weibull β:**

| β (NHPP) | The system is | Policy |
|---|---|---|
| β < 1 | **Improving** — failures arriving more slowly; fixes are sticking (reliability growth) | Keep doing what you are doing; forecast with the *instantaneous* MTBF, not the cumulative one |
| β ≈ 1 | **Stable** — homogeneous Poisson, constant rate, age irrelevant | Random regime: redundancy and fast repair; MTBF is a meaningful rate |
| β > 1 | **Degrading between repairs** — failures arriving faster; repair returns it bad-as-old or worse | Renew or replace the unit, or change repair practice. This is *not* a burn-in finding and *not* a per-unit wear-out claim |

**Cumulative vs instantaneous MTBF.** Cumulative MTBF = T/N(T) = T^(1−β)/λ; instantaneous
MTBF = 1/u(T). They differ whenever β ≠ 1, and it is the instantaneous one that forecasts
forward. Quoting a cumulative MTBF for a degrading system flatters it.

**Or is it a renewal process?** If repair genuinely restores the system to as-good-as-new, the
gaps between failures *are* i.i.d. and Weibull-on-inter-arrivals is legitimate. Test the
assumption instead of asserting it — the **Laplace trend test** is arithmetic you can do by
hand for a system observed to T with n failures:

> U = (t̄ − T/2) ÷ (T · √(1/(12n))), compared against the standard normal

U near zero means no trend (renewal/HPP survives); U > 1.96 means the rate is rising, U < −1.96
falling, and either way an NHPP is required. Worked on §9's data: t̄ = 789/9 = 87.67,
T/2 = 91, denominator = 182 × √(1/108) = 17.51, so **U = −0.19** — no trend, which agrees with
the β̂ interval there.

## §6 MTBF, MTTR, availability, and the SLO downtime-budget table

- **MTBF** = total operating time ÷ number of failures (repairable systems).
- **MTTR** = mean time from failure start (not ticket-open) to restored — detection +
  diagnosis + repair + verification.
- **Availability** A = MTBF ÷ (MTBF + MTTR).

**MTBF has bounds too, and they are wide.** For failures counted over a fixed observation
window T, exact Poisson (chi-square) limits on the rate are

> rate ∈ [ χ²₀.₀₂₅,₂ₙ ÷ 2T , χ²₀.₉₇₅,₂ₙ₊₂ ÷ 2T ],  MTBF = 1/rate

Worked on §9's log — 9 failures in 182 days: χ²₀.₀₂₅,₁₈ = 8.231 and χ²₀.₉₇₅,₂₀ = 34.170, so the
rate lies in [8.231/364, 34.170/364] = [0.0226, 0.0939] per day and **MTBF ∈ [10.7, 44.2] days
(256 – 1061 h) around a point estimate of 20.2 days (485 h)** — a factor of four. Feed those
ends through A = MTBF/(MTBF+MTTR) with MTTR = 4 h and availability lands in
**[98.46%, 99.62%]**. Any statement of the form "we are at 99.18%" needs that interval beside
it, or it will be spent as though it were exact.

### Time-based availability

Downtime a given SLO allows:

| SLO | Per year | Per month | Per week |
|------|---------|-----------|----------|
| 99% | 3.65 days | 7.31 h | 1.68 h |
| 99.5% | 1.83 days | 3.65 h | 50.4 min |
| 99.9% | 8.77 h | 43.8 min | 10.1 min |
| 99.95% | 4.38 h | 21.9 min | 5.04 min |
| 99.99% | 52.6 min | 4.38 min | 1.01 min |
| 99.999% | 5.26 min | 26.3 s | 6.05 s |

Read the table backwards to size the response: a 99.9% target with an MTTR of 4 hours allows
roughly one failure every five to six months (8.77 h/yr ÷ 4 h ≈ 2.2 failures/yr) — if failures
are monthly, either MTTR must drop below ~44 minutes or the failure rate must fall, and the
arithmetic says which is cheaper.

### Event-based availability and the error budget

Time-based availability suits something that is up or down *for everyone*: a batch window, a
feed, a machine. It fits a request-serving service badly, because partial failure is the normal
case — a service returning errors on 3% of requests records zero minutes of "downtime" while
3% of its users are broken. Site-reliability practice therefore defines the indicator on
**events** `[background — verify before citing]`:

> **SLI = good events ÷ valid events** — successful requests ÷ total valid requests, statements
> loaded on time ÷ statements due, jobs completed ÷ jobs scheduled

and turns the shortfall into an **error budget** over a window:

> **budget = (1 − SLO) × valid events**

Worked: a 99.9% SLO over a 30-day window carrying 1,000,000 valid events allows
0.001 × 1,000,000 = **1,000 bad events**, i.e. 33.3 per day at an even burn. Suppose 300 bad
events land in the first 3 days: that is 100/day, a **burn rate of 100 ÷ 33.3 = 3.0**, and the
month's budget is exhausted on **day 10**. Burn rate is the number to alert on — burn rate 1
means the budget lasts exactly the window by construction.

Two cautions worth stating out loud:

- **The two definitions do not convert into each other.** 99.9% of events is 43.8 minutes a
  month only if traffic is uniform in time. An outage in peak hour spends far more of an
  event-based budget than the same minutes overnight, which is exactly why event-based is the
  fairer measure for a service — and why you must say *which* definition your SLO is written
  against before comparing anything to the table above.
- **The budget is a governance mechanism, not just a number** — spend it on releases, stop
  releasing when it is gone. That policy layer is
  `continuous-improvement-skills:lean-six-sigma-for-software` (its stability-and-redundancy
  reference, §1); this file supplies the arithmetic underneath it.

## §7 Series/parallel arithmetic

**Series — every element required:** R_sys = ∏Rᵢ, **assuming the elements fail
independently.**

Worked chain (a data feed): delivery 99.5% × transfer job 99.9% × import 99.7% ×
auto-match 99.8% = **98.90%**. Four individually respectable steps compound into ~8.0 hours of
expected trouble a month (1 − 0.98904 = 0.01096 × 730.5 h) — and no single step "feels" like
the problem. Improving the chain means improving its worst link first: the derivative of the
product is largest there.

**The independence assumption, stated where it is used.** Multiplying is exact only if the
steps' up/down states are independent. The bounds are easy to see:

- If outages **never overlap**, unavailabilities simply add: 1 − (0.005+0.001+0.003+0.002) =
  **98.90%**.
- If outages **always overlap** (one shared cause takes several steps down together), the
  system is only as unavailable as its worst step: 1 − 0.005 = **99.50%**.

So for small unavailabilities the independence product sits at the **pessimistic** end of the
range — for two 99% steps, the product 98.01% against a true range of 98.00% (never overlap)
to 99.00% (always). Two consequences: the series product is a safe number to plan with, *and*
that safety is no reason to skip the shared-cause audit — a common cause makes each incident
bigger and blast-wider even as it flatters the availability arithmetic, and it destroys the
parallel formula below outright. If you need precision rather than a bound, compute
availability from the actual overlapping downtime records instead of multiplying.

**Parallel — any one suffices, IF independent:** R_sys = 1 − ∏(1 − Rᵢ).

Two independent 99% paths: 1 − (0.01)² = **99.99%**. The formula's price of admission:
1. **Demonstrated failover.** The switchover has been exercised under realistic conditions,
   recently and repeatedly. An unexercised standby earns no credit — model it as absent.
   "Untested failover is scenery" is here a theorem: without switchover, the second path never
   enters the math.
2. **Independence.** Shared credential, same patch cycle, same endpoint, same certificate
   authority, same person maintaining both → the joint failure probability is the common
   cause's, not the product. Audit the pair for shared elements before multiplying.

## §8 Weibayes (tiny samples)

With r failures among n units (r as small as 1–3), assume β from engineering knowledge or the
history of like items, then estimate only the scale:

η̂ = [ Σᵢ tᵢ^β ÷ r ]^(1/β)   (sum over ALL units — failures and suspensions alike)

Worked example: assumed β = 2 (mild wear-out, from history of similar jobs); failures at 400 h
and 650 h; three suspensions at 800 h. η̂ = [(400² + 650² + 3·800²)/2]^(1/2)
= (2,502,500/2)^(1/2) ≈ **1,119 h**; B10 = 1,119 × √0.10536 ≈ **363 h**. With zero failures,
set r = 1 for a conservative lower bound on η. Always report the assumed β alongside the
result — the forecast is conditional on it, and a reader who would assume β = 1 should see how
much the conclusion moves. (Show them: at β = 1, η̂ = Σtᵢ/r = (400+650+2400)/2 = 1,725 h and
B10 = 1,725 × 0.10536 = **182 h** — half the earlier answer. The assumption is doing more work
than the data.)

## §9 Worked case: an overnight feed failure log

Synthetic scenario: over a 182-day window an overnight batch data feed failed 9 times, on days
2, 33, 47, 62, 93, 108, 122, 152, 170. Mean detection-to-reload time 4 hours. Internal
commitment: data loaded and processed by 9 AM, roughly a 99.5% availability target on the feed.
Patch windows fall on days 1, 31, 61, 91, 121, 151.

**Step 0 — classify the data (§1).** This is *one* system, repaired and returned to service
nine times. It is **recurrent-event data, not nine lifetimes**, so §5 applies and the §4
β-table does not. Anything that follows about "β" is an NHPP trend parameter.

1. **MTBF and availability.** MTBF = 182 × 24 ÷ 9 = **485 h** (≈ 20.2 days).
   Availability = 485 ÷ (485 + 4) = **99.18%**. Measured downtime = 9 × 4 h = 36 h over
   182/30.44 = 5.98 months = **6.0 h/month**, against a 99.5% budget of 3.65 h/month:
   **over budget.** With the §6 bounds attached: MTBF ∈ [10.7, 44.2] days, availability ∈
   [98.46%, 99.62%]. The interval's top end touches the target, so the honest reading is "we
   are probably over budget, and the point estimate is not precise enough to say by how much."
   Which is fine, because the strong evidence in this log is structural, not in the averages.
2. **Trend test before any shape claim.** Laplace U = −0.19 (§5 arithmetic) — no trend.
   Crow-AMSAA agrees: Σ ln(182/tᵢ) = 10.49, so β̂ = 9/10.49 = **0.86**, λ̂ = 9/182^0.86 = 0.104,
   with SE(β̂) ≈ 0.86/3 = 0.29 and a 95% interval of roughly **[0.30, 1.42]** — straddling 1.
   Report it as "no detectable trend in failure intensity," *not* as reliability growth. (For
   the record: instantaneous MTBF at day 182 = 1/u(182) = 23.6 days against a cumulative 20.2 —
   the gap is what β̂ < 1 buys, and it is well inside the noise.)
3. **Find the structure the averages hide.** Tag each failure by its distance from a patch
   window. Six of the nine (days 2, 33, 62, 93, 122, 152) fall in the 3 days following a patch.
   Those windows are 6 × 3 = **18 of 182 days = 9.9% of the exposure**, so a constant-rate process
   would put 9 × 0.099 = **0.89** failures there. Observing 6 has probability
   P(X ≥ 6 | Binomial(9, 0.0989)) = **6.0 × 10⁻⁵**. That is the finding: failures are
   concentrated after patches, and it needed a clustering test, not a Weibull.
   **Policy:** burn-in — run the feed against a test input after each patch, before the
   production window — rather than scheduled anything.
4. **The remaining three failures** (days 47, 108, 170) fall in the 164 non-patch days: rate
   3/164 = 0.0183/day, **MTBF ≈ 55 days**, no clustering. Random-regime policy: attack MTTR
   (auto-retry the load once, then page, so detection isn't the morning shift) and consider a
   parallel path — which earns parallel credit only once the fallback is actually drilled (§7).
5. **If you want a genuine hazard-shape claim on "time since patch," build the population.**
   Treat each patch cycle as a unit and record the time from patch to its first failure, with
   cycles that survived the whole window entered as **censored** at the cycle length. That is a
   legitimate non-repairable Weibull question (§2–§3) about a repeating renewal, and a β < 1
   there really would mean front-loaded risk inside a cycle. With six cycles it will not settle
   anything (§3's bounds table shows what five points buy) — which is the point: the clustering
   test in step 3 is decisive at n = 9, and the Weibull fit would not be.
6. **Result:** the same log yields two failure modes with two different policies, and the SLO
   arithmetic says how much each must deliver — with every number carrying its interval, and
   with the method matched to the data shape at every step.

## §10 Provenance and evidence

- Weibull, W. — "A statistical distribution function of wide applicability," ASME Journal of
  Applied Mechanics (1951): the distribution's namesake paper, a citation classic because the
  shape parameter carries physical meaning across materials, components, and processes.
- US Air Force Weibull-analysis handbook practice and Pratt & Whitney turbine-engine
  reliability work, codified in Abernethy's *The New Weibull Handbook*: the source of the
  Weibayes method and the small-sample doctrine (usable decisions from as few as 2–3
  failures) [snippet-only]. That handbook fits rank regression on **X** rather than the y-on-x
  least squares many tools default to; §3 gives both and shows the gap on one dataset.
- The power-law NHPP for repairable systems is associated with Crow's reliability-growth work
  at the US Army's AMSAA, giving statistical footing to Duane's log-log observation; hence the
  name **Crow-AMSAA** `[background — verify before citing]`.
- Event-based SLIs (good events ÷ valid events), error budgets, and burn-rate alerting come
  from the site-reliability-engineering literature `[background — verify before citing]`.
- The "untested failover is scenery" doctrine originates in this library's
  `continuous-improvement-skills:lean-six-sigma-for-software` stability-and-redundancy
  reference (§4 and §7 there); this file supplies the arithmetic that makes it a theorem, and
  that reference (§1) owns the error budget as a release-governance mechanism.
- Every number in §3, §5, §6, §7, §8 and §9 was recomputed from the inputs shown; the bootstrap
  intervals in §3 come from 20,000 parametric resamples and were checked against a second
  random seed.
