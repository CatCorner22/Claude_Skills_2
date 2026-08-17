# Evals — continuous-improvement-skills:design-of-experiments

## 1. Positive trigger (should load the skill)
> "My extraction prompt has four knobs — terse vs stepwise instructions, 0 vs 3 examples, format
> described in the prompt vs a provider-native output schema, and low vs high reasoning effort — and
> testing one factor at a time is too slow. Design a factorial DOE against our eval set, run it, and
> tell me which factors actually matter and whether any interact."

Expected: skill loads; sets the response (eval pass rate) and two levels per factor, confirming each
level is actually settable; **sizes the design** — states the smallest effect worth acting on and
computes N ≥ 32σ²/δ² (equivalently SE(effect) = 2σ/√N), then says how many replicates that buys;
chooses a full 2^4 since runs are cheap and executes the runs itself; randomizes run order and
repeats each cell because model output varies run to run; computes main effects and interactions
against a *named* yardstick — pooled replication error if replicated, **Lenth's PSE** with its ME
(and SME for the multiple-comparison price) if not; drops noise terms and states any alias caveats;
recommends a verification run on held-out cases; leaves the decision to adopt the winning prompt to
the user. Bonus: offers a robustness pass across paraphrased inputs, and flags that a model grader
must be qualified before its scores set σ
(`continuous-improvement-skills:measurement-systems-analysis`).

## 1b. Positive trigger (screening design with a resolution claim to get right)
> "I have six candidate factors on our matching engine and budget for about eight runs. Give me a
> fractional design where the main effects are clean of two-factor interactions."

Expected: skill loads and **refuses the premise honestly** — six factors in 8 runs is a 2^(6−3),
which is **resolution III**: every main effect is aliased with two-factor interactions. It should
name the ceiling (resolution IV needs k ≤ runs/2, so six clean mains cost 16 runs), then offer the
real choices: run the 8-run resolution III design as a *screen* whose output is a shortlist, or buy
16 runs for the resolution IV 2^(6−2) (E = ABC, F = BCD). Promising "resolution IV+" for this
(k, runs) pair is the failure mode this scenario tests.

## 2. Near-miss (should NOT load this skill)
> "Our auto-reconciliation is live and matching at 91%. I want to keep nudging the tolerance and
> date-window settings in small, safe steps on production while we operate, and roll back anything
> that hurts."

Expected: continuous small-step tuning inside live production is
`continuous-improvement-skills:evolutionary-operation` — always-on, small, reversible moves with
monitoring — not an offline designed burst. design-of-experiments should hand this off (its seam:
offline designed bursts vs always-on small steps). If it loads and proposes a factorial on live
production, the boundary has failed.

## 2b. Near-miss (greedy-token guard: bare "screening")
> "We need to tighten our vendor screening process — new suppliers should be checked against
> sanctions lists before onboarding."

Expected: compliance/vendor screening — a due-diligence onboarding task, not an experiment; no
continuous-improvement skill should trigger. design-of-experiments must not trigger on "screening" alone; its
screening sense only appears fully qualified (screening designs, Plackett-Burman). If it loads
here, the trigger surface has grown too greedy. (Likewise, a request to "run a quick experiment"
with a single A/B significance check belongs to `data-analytics-bi-skills:statistical-inference`.)

## 2c. Near-miss (seam guard: attribution, not optimization)
> "This prompt started returning the wrong field last week. Walk me through finding which of my
> recent edits broke it."

Expected: this is *attribution* on a single artifact — one change at a time against a fixed case
set — which is `coding-agent-skills:prompt-engineering`. The seam both skills now state: one at a
time attributes a fix, a factorial finds the best combination. If design-of-experiments loads and
proposes a factorial over the edits, the seam has failed in the direction that costs a user real
runs.

## 3. Quality rubric
A good response:
- **Does the task:** produces an explicit design matrix (or names the fraction *and* derives its
  true resolution from the generators), sizes the run count against a stated target effect,
  randomizes run order, replicates or repeats noisy responses, computes effects and interactions
  against a named noise yardstick (pooled error, or Lenth's PSE when unreplicated), states alias
  caveats in plain words, distinguishes blocks from hard-to-change factors (split-plot, two error
  terms), and ends with a concrete recommendation plus a verification run — executing the runs
  itself when the process is a prompt or config.
- **Teaches:** explains why OFAT misses interactions and wastes runs *when optimizing*
  (orthogonality: every run informs every estimate) while granting that one-change-at-a-time is
  correct for attribution; explains what aliasing/resolution actually trade away and that
  resolution belongs to the (factors, runs) pair; why randomization protects against unlisted
  drift and what a block costs you; why a full fold-over helps after resolution III but buys only
  replication after resolution IV; and why robustness across noise beats peak performance on a good
  day.
- **Stays honest:** keeps factor levels inside human-authorized safety limits *and* inside what the
  system will actually accept; never runs designed bursts against live production; presents the
  Taguchi crossed-array/S/N recipe alongside the combined-array and separate mean/dispersion
  critique rather than one side only; distinguishes statistical significance from practical
  importance; and leaves the decision to act on results with the process owner.
