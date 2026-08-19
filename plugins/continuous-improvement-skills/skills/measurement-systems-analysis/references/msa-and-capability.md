# Measurement systems analysis and capability — working reference

Mechanics for `measurement-systems-analysis`. Part A (§1–§5) qualifies the measurement;
Part B (§6–§7) qualifies the process — in that order, always.

## Contents
1. Variable gage R&R — study design
2. The ANOVA decomposition, explained
3. Acceptance criteria — %GRR and ndc
4. Attribute agreement studies (pass/fail judgments)
4a. Kappa is prevalence-sensitive — read it with the table
5. LLM-as-judge agreement protocol — worked example
5a. What counts as a repeat trial for an LLM judge
5b. Operator-specific biases of an LLM judge, and their MSA controls
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

What the table cannot show is that **%GRR is itself an estimate, and a 10×3×3 study estimates it
loosely.** Simulating the standard design, a system whose *true* %GRR is 8% reads anywhere from
about 5% to 14% across repeat studies (90% of them), a true 15% reads 10–27%, and a true 28% reads
19–45%. Every one of those ranges straddles a boundary above. So a single study landing near a
threshold has not established which side of it the gauge is on — re-run it, or add parts and
trials, before condemning or clearing a measurement system on a boundary reading. For the same
reason, %GRR moving from 12% to 9% after a change is not by itself evidence the change worked. The
thresholds sort; they do not adjudicate a close call.

One arithmetic consequence worth knowing before you quote both numbers as independent evidence:
when %GRR is taken against **study** variation, ndc = 1.41·√(1 − %GRR²)/%GRR, so the two criteria
are the same fact twice — ndc ≥ 5 holds exactly while %GRR ≤ ~27%, and a 30% %GRR necessarily
returns ndc = 4. The last row therefore only bites independently when %GRR is quoted against
**tolerance** (where spec width, not part spread, is the denominator). Say which convention you
used; otherwise "%GRR 28% but ndc 6" is arithmetically impossible and signals a mixed calculation.

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
   85% base rate of "pass", two coin-flippers agree often. **Always report kappa — and never
   report kappa alone.** It is prevalence-sensitive in the opposite direction, so a κ quoted
   without its base rate and its 2×2 table is as misleading as a raw percentage. §4a is the rule.

## 4a. Kappa is prevalence-sensitive — read it with the table

Kappa corrects raw agreement for the agreement two raters would reach by chance:
κ = (p_o − p_e)/(1 − p_e), where p_e is built from the raters' **marginal** rates. That makes κ a
big improvement on p_o — and gives it a well-documented pathology in the other direction: **skewed
marginals inflate p_e, which depresses κ even when the raters disagree about very little.** Feinstein
& Cicchetti named it "high agreement but low kappa" (*Journal of Clinical Epidemiology* 43(6), 1990,
543–549; the companion paper on resolving the paradoxes follows at 551–558) [snippet-only,
cross-checked].

**Same disagreements, two base rates.** Thirty items, six disagreements (three each way) in both
tables — identical raw agreement of 24/30 = **80%**:

*Table A — 70% pass rate:*

| | Rater B: pass | Rater B: fail | row total |
|---|---|---|---|
| **Rater A: pass** | 18 | 3 | 21 |
| **Rater A: fail** | 3 | 6 | 9 |
| **column total** | 21 | 9 | 30 |

*Table B — 50% pass rate:*

| | Rater B: pass | Rater B: fail | row total |
|---|---|---|---|
| **Rater A: pass** | 12 | 3 | 15 |
| **Rater A: fail** | 3 | 12 | 15 |
| **column total** | 15 | 15 | 30 |

- **Table A (70% base rate):** p_o = (18 + 6)/30 = 0.80; p_e = 0.70² + 0.30² = 0.49 + 0.09 = 0.58
  → κ = (0.80 − 0.58)/(1 − 0.58) = 0.22/0.42 ≈ **0.52**.
- **Table B (50% base rate):** p_o = (12 + 12)/30 = 0.80; p_e = 0.50² + 0.50² = 0.50
  → κ = (0.80 − 0.50)/(1 − 0.50) = 0.30/0.50 = **0.60**.

Nothing about the raters changed. The *item mix* changed, and κ moved 0.08 — enough to move a verdict
across a threshold in the middle of the conditional band. Consequences for practice:

- **Never compare kappas across studies with different base rates.** A κ of 0.55 on a 95%-pass item
  set can represent a better judgment system than a κ of 0.65 on a balanced one. The acceptance bars
  in §4 are only meaningful with the base rate stated beside them.
- **Report the 2×2 table itself, always.** Every agreement statistic — p_o, κ, effectiveness — is a
  lossy summary of that table, and the table is four numbers. Publishing it makes the paradox
  self-evident and lets a reader recompute anything.
- **Balance the item set — which §4 already tells you to do for a different reason.** Deliberately
  including borderline cases pushes the base rate toward 50%, which both sharpens diagnosticity
  *and* stops kappa from being artificially depressed. Two benefits, one action.
- **Prevalence-adjusted statistics are a supplement, never a substitute.** PABAK
  (prevalence-adjusted bias-adjusted kappa, Byrt/Bishop/Carlin 1993 [snippet-only, cross-checked])
  is κ computed as though the marginals were balanced; for two categories it reduces to
  `2·p_o − 1`, which here is 2(0.80) − 1 = **0.60** — exactly the balanced-table κ above, as it must
  be. Gwet's AC1 is a related alternative. Report one *beside* κ if the marginals are badly skewed,
  and say which is which. Do not swap κ for PABAK because PABAK is kinder: it earns the higher number
  by discarding real information about the marginals, and that criticism is the standard one made of
  it [background — verify].
- **Thirty items cannot carry a threshold verdict.** Prevalence is only half of why a bare κ
  misleads; the other half is that κ is an *estimate*, and on a 30-item study its standard error runs
  about **0.14–0.17**. Bootstrapping the two tables above gives 95% intervals of roughly
  **[0.44, 1.00]** around a κ of 0.75 and **[0.15, 0.83]** around a κ of 0.52 — the second spans
  every band in §4, from unusable through acceptable. So "κ = 0.52, therefore conditional" is a
  sentence the arithmetic does not support. Quote the interval beside the point estimate, treat §4's
  bars as coarse sorting rather than gates at this size, and enlarge the item set when a verdict has
  to be defended. (The same caution applies to the §4 effectiveness percentage, which is one
  proportion on 30 items.)
- **The verdict sentence, therefore, carries four parts:** "p_o = 0.80 on a 70%-pass set, κ ≈ 0.52
  (95% interval ≈ 0.15–0.83 on 30 items), effectiveness 80% — conditional, and 30 items cannot
  settle it." Any one part alone is arguable in bad faith.

## 5. LLM-as-judge agreement protocol — worked example

An LLM judge is an operator; qualify it like one, *before* its scores drive prompt choices,
skill evals, or model comparisons.

**Setup:** 30 eval transcripts scored pass/fail against a rubric, deliberately including borderline
cases. Judges: the same LLM judge run twice under a **fixed, production-identical configuration**
with only the presentation order re-randomized (J1a, J1b — see §5a for why this, and not a
temperature change, is the legitimate repeat trial), a second model from a different family as
judge (J2), and a human-adjudicated reference on all 30.

**Results (illustrative, with the tables — per §4a).**

*Within-judge repeatability, J1a vs J1b* — 27/30 agree → p_o = **90%** raw:

| | J1b: pass | J1b: fail | |
|---|---|---|---|
| **J1a: pass** | 20 | 1 | (21) |
| **J1a: fail** | 2 | 7 | (9) |
| | (22) | (8) | 30 |

p_e = (21/30)(22/30) + (9/30)(8/30) = 0.5133 + 0.0800 = 0.5933 →
**κ = (0.90 − 0.5933)/(1 − 0.5933) = 0.3067/0.4067 ≈ 0.75.**

*Judge vs human reference* — 24/30 agree → p_o = **80%** raw, at a 70% human pass rate:

| | Reference: pass | Reference: fail | |
|---|---|---|---|
| **J1: pass** | 18 | 3 | (21) |
| **J1: fail** | 3 | 6 | (9) |
| | (21) | (9) | 30 |

p_e = 0.70² + 0.30² = 0.58 → **κ = (0.80 − 0.58)/(1 − 0.58) = 0.22/0.42 ≈ 0.52** — nominally
*conditional*, with the §4a caveat that on 30 items the interval reaches from 0.15 to 0.83.
Effectiveness (share matching the reference) = 24/30 = **80%**, below the ≥ 90% bar.

**Reading — and note the two numbers say different things.** Within-judge κ ≈ 0.75 lands on the
acceptance boundary and judge-vs-human κ ≈ 0.52 lands in the conditional band — but neither point
estimate is what the study actually established, because at 30 items each carries an interval wide
enough to cross bands (§4a). What survives is the *gap between them*: both figures come off the
same 30 items at nearly the same base rate, so the item-mix effect §4a describes pushes on both
alike and the comparison outlives it — the judge agrees with itself more than it agrees with the
human. **Repeatable but not aligned** is a *reproducibility* diagnosis, not a repeatability one —
the judge applies a stable rule that is not the human's rule, which points at the rubric's
operational definitions rather than at decoding noise. And per §4a, both κ figures
must be read with their base rates attached: at this 70% pass rate the same 80% agreement would
score κ = 0.60 on a balanced item set, so 0.52 is partly a property of the item mix, and the honest
verdict line is "p_o = 0.80 on a 70%-pass set, κ ≈ 0.52 (interval ≈ 0.15–0.83 on 30 items),
effectiveness 80% — conditional, and this many items cannot settle it."

Either way, the practical conclusion holds: the judge's scores can support coarse verdicts (clear
passes/fails) but **cannot rank close alternatives** — a 2-point score delta between two prompts is
inside the judge's own noise.

**Fixes, in order:** tighten the rubric's operational definitions (reproducibility problem);
add few-shot anchor examples of adjudicated borderline cases; ensemble judges and take majority;
re-run the study after each change. Item-level disagreement lists are the diagnostic gold —
they show *which kinds* of items the judge misreads (the operator×part interaction, reborn).

Apply the same protocol to any recon match-rate claim: before crediting new rules with a gain,
show two engine runs and two human reviewers agree on what counts as "a match" — else the
"improvement" may be reader noise.

## 5a. What counts as a repeat trial for an LLM judge

Repeatability means **the same operator measuring the same part again under the same conditions**.
Everything in a gage study depends on that "same conditions," and for an LLM judge it is easy to
break in either direction. Two opposite traps, both of which produce a number that looks like
repeatability and is not:

**Trap 1 — varying temperature between trials measures a different system, not the same one twice.**
Temperature is a *setting of the gauge*. Score J1a at 0.2 and J1b at 0.9 and the disagreement you
observe is a mixture of sampling noise and a systematic effect of the setting change — which is not
repeatability at all. In gage vocabulary you have accidentally run a two-level factor and reported
it as a re-trial, the way an operator who changed the micrometer between readings has not
demonstrated a repeatable micrometer. Worse, it is unclear which system you qualified: a judge
certified across 0.2–0.9 certifies neither, and **the configuration you qualify must be the
configuration you ship** (same model version, same prompt, same decoding parameters).

**Trap 2 — temperature 0 manufactures perfect repeatability.** Greedy decoding on identical input is
near-deterministic, so re-running it returns the same verdict and within-judge agreement comes out at
or near 100%, κ ≈ 1.0. That is not evidence; it is a cached function evaluated twice. And it is
exactly the artifact the blinding-and-randomization rule in §1 exists to prevent for humans: an
operator who *remembers* the part gives a flattering repeatability number, and a deterministic decoder
is an operator with perfect memory of every part. (Residual variation you may still see at
temperature 0 — from batching, kernel non-determinism, or routing — is infrastructure noise, not
judgment variability. Do not report it as repeatability either.)

**So what is the legitimate repeat trial?** Hold the configuration fixed and vary the *presentation*,
which is precisely what §1's randomization rule already prescribes for parts:

1. **Swap the order in any pairwise comparison** and require the verdict to be consistent. This is
   the highest-value repeat trial available, because order is the judge's best-documented weakness
   (§5b) and swapped-order agreement is a genuine same-part re-measurement.
2. **Re-randomize item order and batch composition**, and score each item in a **fresh context** with
   no history of the other items. Neighbouring items are the LLM analogue of an operator anchoring on
   the last part.
3. **Re-order the rubric's criteria** between trials while keeping their content identical.
4. **Repeat at the production temperature, whatever it is.** If production runs greedy, say so and
   report that within-judge repeatability is ~1.0 *by construction and therefore uninformative* —
   then get your repeat signal from (1)–(3) instead. Reporting a construction as a pass is the
   failure mode; declaring it is the fix.
5. **If you genuinely want to know how sensitive the judge is to decoding settings**, run that as its
   own labelled arm — a deliberate factor, reported as a setting effect alongside repeatability and
   reproducibility, never folded into either.

## 5b. Operator-specific biases of an LLM judge, and their MSA controls

If an LLM judge is an operator, then it has operator pathologies — and the useful thing about the MSA
frame is that it already contains the controls; they just have to be pointed at the right failure.
Three are well documented in the LLM-as-judge literature (Zheng et al., "Judging LLM-as-a-Judge with
MT-Bench and Chatbot Arena," which names position, verbosity and self-enhancement bias plus limited
reasoning as the method's core limitations) [snippet-only, cross-checked]:

| Bias | What the judge does | MSA reading | Control |
|---|---|---|---|
| **Position / order bias** | Prefers whichever response sits in a given slot — reported preferences for the first position running as high as ~75% for some models, and even strong judges agreeing with themselves on swapped pairs only around two-thirds of the time [snippet-only, cross-checked] | The gauge reads differently depending on how the part was presented — a **repeatability** failure caused by presentation, and the reason presentation must be randomized | **Swap the A/B order and require consistency.** Report swapped-order agreement as a headline statistic; count only consistent verdicts, or record inconsistent pairs as ties. This is an MSA repeat trial in the strict sense (§5a) |
| **Verbosity bias** | Prefers longer, more elaborate answers regardless of quality | A **gauge bias correlated with a nuisance characteristic of the part** — the ruler reads long on long parts | Stratify effectiveness by response length and report whether verdicts track token count; include padded-but-not-better probe items in the reference set; state length limits in the rubric |
| **Self-preference / self-enhancement bias** | Rates its own outputs more favourably than others' [snippet-only, cross-checked] | The operator has a stake in the part — the reason inspection is kept independent of production | **Never let the model that generated the candidates be their only judge.** Use a judge from a different family as J2, blind the judge to authorship (the §1 blinding rule extended from item identity to item *provenance*), and record which model produced each item so the effect is measurable rather than assumed |

Two more worth designing against, though they sit outside the documented trio:
- **Scale compression.** Judges cluster on a few values of a 1–10 scale, which destroys ndc — the
  system cannot resolve as many distinct groupings as the scale implies. Report the actual number of
  distinct scores used, and prefer a short, anchored scale you can defend over a long one you cannot.
- **Rubric drift across a long batch.** Standards shift as a session accumulates context. Fresh
  context per item, and re-randomized order, are the same control (§5a item 2).

Design rule that follows from all of it: **an LLM-judge qualification study reports at least four
things** — swapped-order consistency, within-judge agreement under a fixed production configuration,
between-judge agreement against a judge from another family, and effectiveness against a
human-adjudicated reference — each with its 2×2 table and base rate (§4a). Any one of them alone can
be made to look good.

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
