# Reliability math — formulas and worked examples

All worked examples use synthetic, sanitized data — structure only, no real feeds, incidents,
or accounts.

Contents: §1 The Weibull model · §2 Fitting failure data · §3 The β decision table ·
§4 MTBF, MTTR, availability, and the SLO downtime-budget table · §5 Series/parallel
arithmetic · §6 Weibayes (tiny samples) · §7 Worked case: a BAI2 feed failure log ·
§8 Provenance and evidence

## §1 The Weibull model

Two parameters: shape **β** and scale **η** (the characteristic life — by t = η, 63.2% of
units have failed, at any β).

- Reliability (survival): R(t) = exp[−(t/η)^β]
- Cumulative failure: F(t) = 1 − R(t)
- Hazard (instantaneous failure rate): h(t) = (β/η)(t/η)^(β−1)

β is the exponent of the hazard: β < 1 → falling hazard, β = 1 → constant (the exponential
distribution as a special case), β > 1 → rising hazard. That is the entire bathtub curve in
one parameter.

**B-lives:** B10 is the age by which 10% fail — B10 = η·(−ln 0.9)^(1/β). Replacement
intervals are usually set at a B-life, not at MTBF.

## §2 Fitting failure data

**Median-rank regression (hand-checkable).** Sort the n failure times ascending. Give the
i-th failure the median rank F̂ᵢ ≈ (i − 0.3)/(n + 0.4). Regress y = ln ln[1/(1−F̂)] on
x = ln t; the slope is β and η = exp(x̄ − ȳ/β).

Worked fit — five failure times (days): 55, 70, 85, 95, 110.

| i | tᵢ | F̂ᵢ | x = ln tᵢ | y |
|---|----|------|-----------|-----|
| 1 | 55 | 0.130 | 4.007 | −1.975 |
| 2 | 70 | 0.315 | 4.248 | −0.973 |
| 3 | 85 | 0.500 | 4.443 | −0.367 |
| 4 | 95 | 0.685 | 4.554 | +0.145 |
| 5 | 110 | 0.870 | 4.700 | +0.715 |

Least squares gives **β ≈ 3.8, η ≈ 92 days** → strong wear-out; **B10 ≈ 51 days**, so a
~50-day scheduled replacement keeps expected in-service failures near 10%.

**Censoring.** Units still running at the analysis date and units removed unfailed are
suspensions. In rank methods they consume rank positions without plotting (adjusted ranks);
in MLE they contribute survival probability R(t) instead of density. Either way they must be
in the dataset — a fit on failures alone answers a different question ("of the ones that
failed, when?") than the one you asked ("when will these fail?").

**Small-sample honesty.** With n ≤ ~10, β carries wide confidence bounds. A fitted β of 1.2
on five points does not establish wear-out — the bounds straddle 1; treat as random hazard
until more data arrives, or use Weibayes (§6) with a β you can defend.

## §3 The β decision table

| β | Regime | Typical causes | Policy |
|---|--------|----------------|--------|
| β < 1 | Infant mortality | Bad installs, fresh patches, config errors, manufacturing defects | Burn-in / shake-down before trusting; fix the defect source; no scheduled replacement |
| β ≈ 1 | Random | External shocks, load spikes, operator error — age-independent | Run-to-failure + redundancy + fast repair (attack MTTR); scheduled replacement buys nothing |
| 1 < β ≲ 4 | Early-to-steady wear-out | Fatigue, corrosion, drift, queue growth | Scheduled replacement/refresh at a B-life; condition monitoring |
| β ≫ 4 | Steep wear-out | Tight physical wear mechanisms | Hard replacement interval just below the knee |
| β → ∞ | Deterministic expiry | Certificates, passwords, key rotations, license lapses | Calendar-driven renewal, alarmed well ahead — treat the date as the failure time |

Post-patch failure clustering is the software analogue of infant mortality: if failures pile
up in the days after each patch window, the answer is a burn-in step (run against test input
before trusting the window), not more redundancy.

## §4 MTBF, MTTR, availability, and the SLO downtime-budget table

- **MTBF** = total operating time ÷ number of failures (repairable systems).
- **MTTR** = mean time from failure start (not ticket-open) to restored — detection +
  diagnosis + repair + verification.
- **Availability** A = MTBF ÷ (MTBF + MTTR).

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

## §5 Series/parallel arithmetic

**Series — every element required:** R_sys = ∏Rᵢ.

Worked chain (a bank feed): SFTP delivery 99.5% × transfer job 99.9% × Oracle import 99.7% ×
auto-recon 99.8% = **98.90%**. Four individually respectable steps compound into ~8 hours of
expected trouble a month (from the 99% row's neighborhood) — and no single step "feels" like
the problem. Improving the chain means improving its worst link first: the derivative of the
product is largest there.

**Parallel — any one suffices, IF independent:** R_sys = 1 − ∏(1 − Rᵢ).

Two independent 99% paths: 1 − (0.01)² = **99.99%**. The formula's price of admission:
1. **Demonstrated failover.** The switchover has been exercised under realistic conditions,
   recently and repeatedly. An unexercised standby earns no credit — model it as absent.
   "Untested failover is scenery" is here a theorem: without switchover, the second path never
   enters the math.
2. **Independence.** Shared credential, same patch cycle, same SFTP endpoint, same certificate
   authority, same person maintaining both → the joint failure probability is the common
   cause's, not the product. Audit the pair for shared elements before multiplying.

## §6 Weibayes (tiny samples)

With r failures among n units (r as small as 1–3), assume β from engineering knowledge or the
history of like items, then estimate only the scale:

η̂ = [ Σᵢ tᵢ^β ÷ r ]^(1/β)   (sum over ALL units — failures and suspensions alike)

Worked example: assumed β = 2 (mild wear-out, from history of similar jobs); failures at 400 h
and 650 h; three suspensions at 800 h. η̂ = [(400² + 650² + 3·800²)/2]^(1/2) ≈ **1,119 h**;
B10 ≈ **363 h**. With zero failures, set r = 1 for a conservative lower bound on η. Always
report the assumed β alongside the result — the forecast is conditional on it, and a reader
who would assume β = 1 should see how much the conclusion moves.

## §7 Worked case: a BAI2 feed failure log

Synthetic scenario: over a 182-day window the overnight BAI2 bank-statement feed failed 9
times; mean detection-to-reload time 4 hours; internal commitment: statements loaded and
reconciled by 9 AM, roughly a 99.5% availability target on the feed.

1. **MTBF** = 182 × 24 ÷ 9 ≈ **485 h** (≈ 20 days between failures).
2. **Availability** = 485 ÷ (485 + 4) ≈ **99.18%** — measured downtime ≈ 6.0 h/month against
   a 99.5% budget of 3.65 h/month: **over budget**; the gap must come from failure rate or
   MTTR.
3. **Read the pattern before buying redundancy.** Tagging each failure by date shows 6 of 9
   inside 3 days of a monthly patch window → infant-mortality signature (β < 1 on
   time-since-patch). Policy: burn-in — run the feed against a test statement after each patch
   before the production window — rather than scheduled anything.
4. **The remaining 3 failures** look age-independent (β ≈ 1 on operating time): random-regime
   policy — attack MTTR (auto-retry the load once, then page, so detection isn't the morning
   shift) and consider a parallel path (portal download as the exercised manual fallback —
   which earns parallel credit only once the fallback is actually drilled).
5. **Result:** the same log yields two failure modes with two different policies, and the SLO
   arithmetic says how much each must deliver. Recon breaks can be run through the identical
   loop: MTBF of breaks per account, MTTR as time-to-clear, β over time-since-rule-change.

## §8 Provenance and evidence

- Weibull, W. — "A statistical distribution function of wide applicability," ASME Journal of
  Applied Mechanics (1951): the distribution's namesake paper, a citation classic because the
  shape parameter carries physical meaning across materials, components, and processes.
- US Air Force Weibull-analysis handbook practice and Pratt & Whitney turbine-engine
  reliability work, codified in Abernethy's *The New Weibull Handbook*: the source of the
  Weibayes method and the small-sample doctrine (usable decisions from as few as 2–3
  failures) [snippet-only].
- The "untested failover is scenery" doctrine originates in this library's
  `continuous-improvement-skills:lean-six-sigma-for-software` stability-and-redundancy
  reference (§4 and §7 there); this file supplies the arithmetic that makes it a theorem.
