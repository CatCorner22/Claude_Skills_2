---
name: measurement-systems-analysis
description: >-
  Answers two questions no metric-driven decision should skip: can this measurement be
  trusted, and is the process behind it capable? Part A runs Gage R&R — a crossed study (10
  parts × 3 operators × 3 trials, blind and randomized) decomposed by ANOVA into repeatability,
  reproducibility, and part-to-part variation, judged on %GRR and distinct categories — plus
  attribute agreement studies for pass/fail judgments, including LLM-as-judge scoring, where
  agreement across judges and repeated runs is measured before any eval score is trusted. Part
  B computes process capability, Cp and Cpk against spec limits, only after stability is
  confirmed on a control chart. Use when validating a metric or gauge, measuring inter-rater or
  judge agreement, or judging a stable process against its spec limits. Triggers: gage R&R,
  measurement systems analysis, can I trust this metric, repeatability and
  reproducibility, inter-rater agreement, attribute agreement, LLM judge agreement, process
  capability, Cp, Cpk, capability study.
---

# Measurement systems analysis and process capability

## When to use
- Before improving, reporting, or arguing from any metric: quantify how much of what you see is
  measurement noise (equipment/repeatability) versus disagreement between measurers
  (reproducibility) versus the real thing (part-to-part).
- Pass/fail judgment calls that must be consistent: two reviewers scoring whether a
  reconciliation exception is "a match", audit sampling decisions, and **LLM-as-judge** eval
  scores — including this library's own `evals/` rubrics.
- Judging a *stable* process against spec limits with Cp/Cpk, and deciding whether to center it
  or reduce its variance.
- Not for: building the control chart that establishes stability → the SPC coverage in
  `continuous-improvement-skills:dmaic-problem-solving` (Control phase) and
  `continuous-improvement-skills:lean-six-sigma-for-software` owns the charts — stability is
  their gate; whether the stable process meets spec is this skill's question. Broad ML model
  evaluation (metric choice, cross-validation, leakage) →
  `machine-learning-skills:model-evaluation`; this skill adds the inter-rater rigor on top.
  An "MSA" that is a *master service agreement* is a contract, not a measurement — this skill
  never triggers on the bare acronym.

## Do it
**Part A — can the measurement be trusted?**
1. **Design the study.** Classic variable gage R&R: **10 parts × 3 operators × 3 trials**, parts
   spanning the real range of the process, presented **blind and in randomized order** so nobody
   (human or model) can remember or anchor. For pass/fail judgments run the attribute variant:
   ~30–50 items of known reference answer, each judged repeatedly by each judge
   (`references/msa-and-capability.md` §1, §4).
2. **Decompose the variance by ANOVA** into repeatability (same operator re-measuring the same
   part — the equipment), reproducibility (operator-to-operator), and part-to-part. The LLM runs
   this on a pasted table — no stats package needed (§2).
3. **Judge against the acceptance table:** %GRR **< 10%** and number of distinct categories
   (ndc) **≥ 5** → acceptable; 10–30% → conditional, only with a documented reason and an
   improvement plan; **> 30%** → the metric cannot support decisions; fix the measurement system
   before touching the process (§3).
4. **For LLM-as-judge scoring, measure agreement before trusting scores:** run the same items
   past multiple judges — or the same judge repeatedly, temperature-varied — plus a human
   reference where you can get one, and compute agreement (kappa, effectiveness) exactly as an
   attribute study (§5). If the judge can't agree with itself, its scores can't rank anything.
**Part B — is the process capable?**
5. **Confirm stability first.** Capability math assumes one process with one σ; an out-of-control
   process isn't one process. Point to the control chart (SPC coverage above) showing in-control
   before computing anything.
6. **Compute Cp = (USL − LSL) / 6σ** (potential, spread only) and **Cpk = min(USL − μ, μ − LSL) /
   3σ** (actual — penalizes running off-center). Worked example in §6–§7.
7. **Judge against the owner's threshold and improve in order:** 1.33 is the customary automotive
   floor. **Center first** (usually a free adjustment — Cpk rises toward Cp), **then reduce
   variance** (expensive — raises both). The human gate: spec limits and acceptance thresholds
   are business decisions the process owner sets, never numbers the analyst back-solves from data.

## Why / learn
Every number you observe is two things added together: σ²_observed = σ²_process +
σ²_measurement. When the measurement share is large, "improvements" appear and vanish at random,
and you end up tuning the ruler. That is why measurement systems analysis (the AIAG MSA manual
lineage) comes *before* improvement: Gage R&R splits the measurement share into repeatability
(the gauge) and reproducibility (the people), telling you whether to fix the instrument or the
instructions. The ndc statistic says how many distinct groupings of parts the system can actually
resolve — below 5, the metric is closer to a coin than a caliper. Capability has its own lineage
— Cp from Juran, Cpk formalized by Kane (Journal of Quality Technology, written at Ford)
[snippet-only] — and its own trap: Cp measures spread against the spec width, so a badly
off-center process can carry a flattering Cp while shipping scrap; Cpk is the honest one because
it measures the *nearer* spec edge. Both are meaningless without stability, since an unstable
process has no single σ to plug in. The attribute-agreement variant is an old AIAG procedure that
is arguably the missing rigor for LLM evaluation: an LLM judge is just an operator, so before its
scores drive decisions, it owes the same evidence a human inspector owes — agreement with itself
on repeat, agreement with its peers, agreement with a reference. Concretely: before claiming new
matching rules "raised the match rate", show two runs and two reviewers score the same exceptions
the same way, or the gain may be reader noise. What once needed Minitab literacy the LLM now does
from a pasted table — the thresholds and spec limits stay human.

## Common mistakes
- Computing Cpk on an unstable process → there is no single σ; the index is fiction. Chart first.
- Improving the metric before studying the measurement → you may be tuning noise. Part A first.
- Unblinded or un-randomized trials → operators (and judges) remember items; %GRR comes out
  flattered. Blind and shuffle.
- Treating 10–30% GRR as a pass → it's conditional: document why and plan the fix.
- Back-solving spec limits from the data → limits are the voice of the customer/owner; the data
  is the voice of the process. Never let the process grade itself.
- Trusting single-run LLM-judge scores → repeat runs and multiple judges first; report kappa,
  not vibes.
- Attacking variance before centering → centering is usually free and raises Cpk toward Cp;
  spend on variance only after the mean sits mid-spec.

## Tailor to your environment
Record in `references/your-environment.md` the metrics you actually decide on, how each is
measured (system, query, reviewer), the judges/reviewers involved, and the owner-set spec limits
and thresholds (use `your-environment.private.md`, which is git-ignored, for real system names,
limits, or reviewer names). Never commit real transaction or personnel data — structure only.

## References
- references/msa-and-capability.md — study designs, the ANOVA decomposition explained, the
  %GRR/ndc acceptance table, the LLM-as-judge agreement protocol as a worked example, and Cp/Cpk
  math with the stability precondition and an off-center worked example
- references/your-environment.md — your metrics, measurement systems, judges, and spec limits
