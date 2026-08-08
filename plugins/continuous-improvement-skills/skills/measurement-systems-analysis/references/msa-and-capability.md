# Measurement systems analysis and capability — working reference

Mechanics for `measurement-systems-analysis`. Part A (§1–§5) qualifies the measurement;
Part B (§6–§7) qualifies the process — in that order, always.

## Contents
1. Variable gage R&R — study design
2. The ANOVA decomposition, explained
3. Acceptance criteria — %GRR and ndc
4. Attribute agreement studies (pass/fail judgments)
5. LLM-as-judge agreement protocol — worked example
6. Process capability — Cp and Cpk, with the stability precondition
7. Worked capability example — off-center, then centered

## 1. Variable gage R&R — study design

The classic crossed study: **10 parts × 3 operators × 3 trials** (90 measurements).

- **Parts** span the real operating range of the process — not ten near-identical good parts.
  Part-to-part variation is the signal the study measures everything else against.
- **Blind**: parts carry hidden identities; operators never see prior readings (their own or
  anyone's).
- **Randomized**: each operator measures the 10 parts in a fresh random order each trial, with
  the trials separated so memory can't anchor.
- Adaptations: fewer trials or operators shrink the error estimate's quality — keep total
  measurements near 90 where possible. "Operator" generalizes to anything that can disagree:
  two analysts, two script versions, two runs of an engine.

## 2. The ANOVA decomposition, explained

ANOVA splits total observed variance into components:

| Component        | What varies                          | Reads as                       |
|------------------|--------------------------------------|--------------------------------|
| Repeatability    | same operator, same part, re-trial   | the equipment / the instrument |
| Reproducibility  | operator to operator (+ operator×part interaction) | the people / the instructions |
| Part-to-part     | the parts themselves                 | the real process signal        |

- **GRR variance** = repeatability + reproducibility. **Total** = GRR + part-to-part.
- **%GRR = √(σ²_GRR) / √(σ²_total) × 100** (a ratio of standard deviations, not variances — the
  two conventions differ; say which you used. Against a spec width, %GRR to tolerance =
  6·σ_GRR / (USL − LSL) × 100.)
- **ndc = 1.41 × (σ_parts / σ_GRR)**, rounded down — how many distinct groupings of parts the
  system can resolve.
- Reading the split: repeatability dominant → the instrument (or the query/extract) is noisy;
  reproducibility dominant → operators use different definitions — fix the operational
  definition and training, not the gauge. A significant operator×part interaction means some
  operators read some *kinds* of parts differently — the most diagnostic finding of all.
- The LLM runs this from a pasted 10×3×3 table: ask for the variance components, %GRR both ways,
  ndc, and which component dominates.

## 3. Acceptance criteria — %GRR and ndc

| %GRR      | ndc  | Verdict                                                        |
|-----------|------|----------------------------------------------------------------|
| < 10%     | ≥ 5  | Acceptable — the metric can support decisions                  |
| 10–30%    | ≥ 5  | Conditional — acceptable only with documented rationale (cost, importance) and an improvement plan |
| > 30%     | any  | Unacceptable — the measurement system cannot support decisions; fix it before touching the process |
| any       | < 5  | The system can't distinguish parts — effectively attribute data |

These are the AIAG MSA-lineage thresholds; the process owner may set stricter ones. The
threshold choice is a business decision (what's at stake when the metric lies), not a statistic.

## 4. Attribute agreement studies (pass/fail judgments)

When the "measurement" is a judgment — match / no-match, pass / fail, compliant / exception —
run the attribute variant:

1. Assemble **30–50 items** with reference answers where obtainable (adjudicated by the owner or
   an expert panel), deliberately including borderline cases.
2. Each judge assesses every item **at least twice**, blind, randomized, sessions separated.
3. Compute:
   - **Within-judge agreement** (consistency with self on repeat),
   - **Between-judge agreement** (consensus),
   - **Effectiveness** = % of items matching the reference answer, per judge,
   - **Cohen's/Fleiss' kappa** — agreement corrected for chance:
     κ = (p_observed − p_chance) / (1 − p_chance).
4. Customary bars: κ > 0.75 and effectiveness ≥ 90% → acceptable; κ 0.40–0.75 → conditional;
   κ < 0.40 → the judgment system is unusable. Raw percent agreement alone flatters — with an
   85% base rate of "pass", two coin-flippers agree often. Always report kappa.

## 5. LLM-as-judge agreement protocol — worked example

An LLM judge is an operator; qualify it like one, *before* its scores drive prompt choices,
skill evals, or model comparisons.

**Setup:** 30 eval transcripts scored pass/fail against a rubric. Judges: the same LLM judge run
twice at varied temperature (J1a, J1b), a second model as judge (J2), and a human reference on
all 30.

**Results (illustrative):**
- Within-judge (J1a vs J1b): 27/30 agree → 90% raw. Human pass rate 70%, judge pass rate ~73%;
  p_chance = 0.70·0.73 + 0.30·0.27 ≈ 0.59.
- Judge vs human (J1 consensus vs reference): 24/30 → p_o = 0.80,
  **κ = (0.80 − 0.59) / (1 − 0.59) ≈ 0.51** — *conditional*, not acceptable.

**Reading:** κ ≈ 0.5 means roughly half the judge's beyond-chance calls track the human standard.
The judge's scores can support coarse verdicts (clear passes/fails) but **cannot rank close
alternatives** — a 2-point score delta between two prompts is inside the judge's own noise.
**Fixes, in order:** tighten the rubric's operational definitions (reproducibility problem);
add few-shot anchor examples of adjudicated borderline cases; ensemble judges and take majority;
re-run the study after each change. Item-level disagreement lists are the diagnostic gold —
they show *which kinds* of items the judge misreads (the operator×part interaction, reborn).

Apply the same protocol to any recon match-rate claim: before crediting new rules with a gain,
show two engine runs and two human reviewers agree on what counts as "a match" — else the
"improvement" may be reader noise.

## 6. Process capability — Cp and Cpk, with the stability precondition

**Precondition — stability.** Capability assumes one process with one mean and one σ. Confirm
in-control on a control chart first (the SPC coverage in
`continuous-improvement-skills:dmaic-problem-solving` /
`continuous-improvement-skills:lean-six-sigma-for-software` owns the charts). An unstable
process has no single σ — any index computed from it is fiction.

- **Cp = (USL − LSL) / 6σ** — *potential* capability: could the spread fit the spec if perfectly
  centered? Ignores where the mean actually sits.
- **Cpk = min(USL − μ, μ − LSL) / 3σ** — *actual* capability: distance from the mean to the
  **nearer** spec edge, in 3σ units. Off-center processes are penalized; Cpk ≤ Cp always, with
  equality only when centered.
- **Thresholds:** 1.33 is the customary automotive floor (a 4σ cushion); 1.00 means the spec is
  exactly 3σ away — no margin. The floor you require is the owner's business decision.
- One-sided specs use only the relevant half: Cpk = (USL − μ)/3σ or (μ − LSL)/3σ.
- σ here is the within-process estimate from the control chart (e.g. R̄/d₂), not a casual
  standard deviation over mixed data.

## 7. Worked capability example — off-center, then centered

A stable posting process must land a value between **LSL = 95 and USL = 105** (spec width 10).
Control chart: in-control, **μ = 98.2, σ = 1.5**.

- Cp = (105 − 95) / (6 × 1.5) = 10 / 9 ≈ **1.11** — the spread *could* nearly fit with margin.
- Cpk = min(105 − 98.2, 98.2 − 95) / (3 × 1.5) = min(6.8, 3.2) / 4.5 ≈ **0.71** — the process
  runs close to the lower edge; expect steady out-of-spec output on that side.

**Center first** (an adjustment, usually cheap): shift μ to 100.
- Cpk = min(5, 5) / 4.5 ≈ **1.11** = Cp. The full potential recovered without touching variance.

**Then reduce variance** (expensive — real improvement work): σ 1.5 → 1.2.
- Cp = Cpk = 10 / 7.2 ≈ **1.39** — now above the 1.33 floor.

The order matters because the two moves cost differently: centering is turning a knob; variance
reduction is a DMAIC project. Cpk tells you which one you owe: Cpk ≪ Cp → center; Cpk ≈ Cp but
low → variance.
