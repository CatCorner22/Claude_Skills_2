# Evals — data-analytics-bi-skills:ab-test-design

## 1. Positive trigger (should load the skill)
> "We want to try a new follow-up letter against our current one on live cases — help me design
> the A/B test: what do we randomize on, how many letters do we need before we can see anything,
> how long do we run it, and what should we watch so we don't fool ourselves?"

Expected: skill loads; writes the OEC (e.g., response within 30 days) and guardrails (complaint/
opt-out rate) before discussing variants; picks the randomization unit and checks interference
(one clerk handling both variants); sizes with n ≈ 16σ²/δ² per arm from a historical baseline and
confronts the duration honestly; pre-commits a stopping rule (fixed horizon or a named sequential
method — not "run until significant"); schedules an SRM chi-square for every readout and an A/A
test on new machinery; plans full-cycle coverage with a novelty/primacy check; routes the finished
data to statistical-inference for analysis.

## 2. Near-miss (should NOT load this skill — statistical-inference seam)
> "Our A/B test finished: variant B converted at 4.1% vs 3.8% for A over two weeks. Is that
> difference statistically significant, and how do I interpret the p-value?"

Expected: this is *analysis of a finished test* — `data-analytics-bi-skills:statistical-inference`
owns it (including the bare "A/B test" trigger and the p-value machinery). ab-test-design may be
cross-referenced for trust checks (was there SRM? was the stop pre-committed?) but must not load
as the primary skill. If it does, tighten the description/cross-links.

## 3. Near-miss (should NOT load this skill — design-of-experiments seam)
> "We have five candidate factors for the renewal-notice process — template, send time, sender
> name, length, and discount — set up a design of experiments to screen which factors actually
> matter in the fewest runs."

Expected: multi-factor factorial/screening design →
`continuous-improvement-skills:design-of-experiments` (it owns "design of experiments/DOE/
factorial"). The seam sentence both skills carry: DOE is multi-factor physical/process tuning in
designed offline bursts; ab-test-design is two-variant online/field tests on live units. If
ab-test-design loads as primary here, the routing is broken.

## 4. Quality rubric
A good response:
- **Does the task:** produces a complete pre-launch design — OEC + guardrails with veto
  thresholds, randomization unit with interference reasoning, MDE and n-per-arm arithmetic shown,
  pre-committed stopping rule, A/A plan, SRM check cadence, full-cycle duration — and an explicit
  analysis handoff to statistical-inference.
- **Teaches:** why optional stopping on a fixed-horizon test inflates false positives (~5×
  nominal per the KDD 2017 peeking paper) and why sequential designs make looking legitimate;
  why a failed SRM chi-square voids a scorecard even at 50.2/49.8 on a large sample; why week-one
  winners can be novelty; why nobody can pick winners by argument (the humbling base rates).
- **Stays honest:** cites platform success rates as self-reported experience, never as measured
  constants; tells Twyman's law with its real attribution chain (Twyman apparently never
  published it; Ehrenberg's 1975 formulation survives); presents "peeking is cheating" as only
  half true — the discipline is deciding the stopping rule before the data, not never looking;
  and never invents baselines — sizing numbers come from the user's history or are labeled
  illustrative.
