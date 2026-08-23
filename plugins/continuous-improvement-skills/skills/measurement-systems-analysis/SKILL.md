---
name: measurement-systems-analysis
description: >-
  Answers two questions no metric-driven decision should skip: can this measurement be trusted,
  and is the process capable?
  Part A runs Gage R&R — a crossed study (10 parts × 3 operators × 3 trials, blind and
  randomized) decomposed by ANOVA into repeatability, reproducibility, and part-to-part
  variation, judged on %GRR and ndc — plus attribute agreement studies for
  pass/fail judgments, including LLM-as-judge scoring, where agreement across judges and
  repeated runs is measured before any eval score is trusted. Part B computes capability,
  Cp and Cpk against spec limits, only after stability is confirmed on a control chart.
  Use when validating a metric or gauge,
  measuring inter-rater or judge agreement, or judging a stable process against its spec limits.
  Triggers: gage R&R, measurement systems analysis, can I trust this metric, repeatability and
  reproducibility, inter-rater agreement, attribute agreement, LLM judge agreement, process
  capability, Cp, Cpk, capability study.
metadata:
  version: "1.5.0"
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
   before touching the process (§3) — reading %GRR near a boundary settles nothing, because a
   10×3×3 study estimates it loosely enough to straddle one (§3). For the pass/fail (attribute) variant the bars are κ > 0.75
   and effectiveness ≥ 90% — but **kappa is prevalence-sensitive**, so quote it only with its base
   rate and its 2×2 table beside it, and never compare kappas across item sets with different base
   rates (§4a). κ is also an *estimate*, and at the low end of the 30–50 items step 1 asks for its
   own standard error runs about **0.14–0.17** — wide enough to cross those bars. It shrinks with
   the item count (SE scales as 1/√n, so ~0.12 by 50 items), which is the argument for the top of
   that range whenever a verdict rides on the number. Quote the interval alongside the point
   estimate either way, and treat the bars as coarse sorting rather than gates at that size (§4a).
4. **For LLM-as-judge scoring, measure agreement before trusting scores — and define a repeat
   trial correctly.** First, identify what the gauge's settable parameters actually *are* on your
   model: several current generations **reject `temperature`/`top_p`/`top_k` outright**
   (`coding-agent-skills:prompt-engineering`), so on those the gauge settings are the prompt and
   rubric version, the effort/thinking configuration, the context policy, and the model version —
   not decoding parameters. Where the knobs do not exist, the traps below still apply, with those
   settings substituted for "temperature". Hold the configuration fixed (model version, prompt,
   decoding parameters where they exist —
   *the one you will ship*) and get your repeat signal by re-randomizing **presentation**: swap the
   A/B order and require the verdict to hold, re-shuffle item order, score each item in a fresh
   context. Do **not** vary temperature between trials — that changes the gauge rather than
   re-measuring the part — and do not report the ~100% self-agreement a greedy/temperature-0 judge
   produces as repeatability; determinism is an operator with perfect memory, which is exactly what
   the blinding rule in step 1 exists to defeat (§5a). Then run a second judge **from a different
   model family** and a human-adjudicated reference, and test the three operator-specific biases:
   **position/order**, **verbosity**, and **self-preference** — never let the model that produced
   the candidates be their only judge (§5b). Compute agreement as an attribute study (kappa,
   effectiveness), reporting each 2×2 table and base rate (§4a). If the judge can't agree with
   itself under a fixed configuration, its scores can't rank anything.
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

Take that "just an operator" claim seriously and it pays twice, because the frame does not only
transfer the *procedure* — it predicts the *failure modes* and already contains their controls. A
judge that prefers whichever answer sits first is a gauge whose reading depends on how the part was
presented, which is why the answer is to swap the order and demand consistency: that swap is a
same-part re-measurement, i.e. a repeat trial in the strict Gage R&R sense, and it happens to test
the best-documented weakness LLM judges have. A judge that rewards length is a gauge biased by a
nuisance characteristic of the part, caught by stratifying effectiveness against a reference rather
than by inspecting agreement. A model grading its own output is an operator with a stake in the
part — the reason inspection is kept independent of production in every quality system ever built,
long before anyone had a language model to worry about.

The chance-correction statistic deserves the same scepticism the skill applies to everything else.
Raw percent agreement flatters, so kappa is the right instinct — but kappa's correction is built
from the raters' marginal rates, and **skewed marginals depress it**, the "high agreement but low
kappa" paradox (Feinstein & Cicchetti, 1990) [snippet-only, cross-checked]. The same six
disagreements out of thirty items score κ ≈ 0.52 on a 70%-pass set and κ = 0.60 on a balanced one,
with nothing about the raters changed. So a hard verdict drawn off a bare kappa repeats, one level
up, the error of drawing one off a bare percentage: report p_o, the base rate, and the 2×2 table
together — the table is four numbers and every statistic is a lossy summary of it. And balance the
item set with borderline cases, which the study design already asks for on diagnosticity grounds
and which happens to be the cleanest mitigation for the paradox too.

## Common mistakes
- Computing Cpk on an unstable process → there is no single σ; the index is fiction. Chart first.
- Improving the metric before studying the measurement → you may be tuning noise. Part A first.
- Unblinded or un-randomized trials → operators (and judges) remember items; %GRR comes out
  flattered. Blind and shuffle.
- Treating 10–30% GRR as a pass → it's conditional: document why and plan the fix.
- Condemning or clearing a gauge on a single boundary %GRR → the study's own spread straddles the
  boundary. Re-run, or add parts and trials, before the number decides anything.
- Back-solving spec limits from the data → limits are the voice of the customer/owner; the data
  is the voice of the process. Never let the process grade itself.
- Trusting single-run LLM-judge scores → repeat runs and multiple judges first; report kappa,
  not vibes.
- Varying temperature between a judge's "trials" → that changes the gauge, not the measurement;
  the disagreement is a setting effect. Fix the configuration you will ship and re-randomize
  presentation instead.
- Reporting ~100% self-agreement from a temperature-0 judge as repeatability → determinism is an
  operator with perfect memory, the artifact blinding exists to prevent. Declare it uninformative
  and get the repeat signal from swapped order and reshuffled items.
- No order-swap check on pairwise judging → position bias is the best-documented LLM-judge
  pathology; swap A/B, require consistency, and report that consistency rate.
- Letting a model judge its own output → self-preference bias; inspection stays independent of
  production. Use a judge from another family and blind the judge to authorship.
- Ignoring response length → verbosity bias reads long parts high; stratify effectiveness by
  length and include padded-but-not-better probe items.
- Quoting kappa without its base rate and 2×2 table → skewed marginals depress kappa (the same
  80% agreement gives 0.52 at a 70% base rate and 0.60 at 50%). Report p_o, prevalence, and the
  table; never compare kappas across differently-balanced item sets.
- Reading a 30-item kappa against the acceptance bars as a verdict → at that size the interval
  spans whole bands (roughly 0.15–0.83 around a κ of 0.52). Quote the interval, and enlarge the
  item set before a threshold call has to be defended.
- Swapping kappa for PABAK because PABAK is kinder → it buys the higher number by discarding the
  marginals. Report it beside kappa, labelled, if at all.
- Attacking variance before centering → centering is usually free and raises Cpk toward Cp;
  spend on variance only after the mean sits mid-spec.

## Tailor to your environment
Record in `references/your-environment.md` the metrics you actually decide on, how each is
measured (system, query, reviewer), the judges/reviewers involved, and the owner-set spec limits
and thresholds (use `your-environment.private.md`, which is git-ignored, for real system names,
limits, or reviewer names). Never commit real transaction or personnel data — structure only.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/measurement-systems-analysis.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/msa-and-capability.md — study designs, the ANOVA decomposition explained, the
  %GRR/ndc acceptance table, kappa's prevalence sensitivity read off the 2×2 table, the
  LLM-as-judge agreement protocol as a worked example with what counts as a repeat trial and the
  position/verbosity/self-preference biases mapped to their MSA controls, and Cp/Cpk
  math with the stability precondition and an off-center worked example
- references/your-environment.md — your metrics, measurement systems, judges, and spec limits
