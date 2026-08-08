# Evals — continuous-improvement-skills:measurement-systems-analysis

## 1. Positive trigger (should load the skill)
> "Before we claim the new matching rules raised our match rate, I want to know the number
> itself is trustworthy — two analysts reviewing the same borderline exceptions don't always
> agree on what counts as a match. Can you set up a gage R&R style study for that, and then
> tell me whether the process is even capable against the 95% floor management set?"

Expected: skill loads; designs a blind, randomized attribute agreement study (~30–50 items with
adjudicated reference answers, each judge scoring twice) for the match/no-match call; computes
within-judge and between-judge agreement plus kappa and effectiveness against the acceptance
bars; for any variable metric, the 10×3×3 crossed study with ANOVA decomposition into
repeatability/reproducibility/part-to-part and the %GRR < 10% / ndc ≥ 5 table; then requires
stability evidence (control chart, in-control) before computing Cp/Cpk against the 95% floor;
notes the floor and spec limits are the owner's business decision; recommends centering before
variance reduction.

## 2. Near-miss (should NOT load this skill)
> "Can you review the MSA before we sign with the new bank-fee analytics vendor? Legal flagged
> the indemnification clause."

Expected: "MSA" here is a master service agreement — contract review, nothing to do with
measurement. This skill must NOT load on the bare acronym; the description deliberately never
claims it. If measurement-systems-analysis loads here, its trigger surface has leaked onto the
contract sense of the token.

## 2b. Near-miss (stability seam)
> "Which control chart should I use to monitor daily match rate so I can tell real signal from
> noise before reacting?"

Expected: building and reading the control chart is the SPC coverage in
`continuous-improvement-skills:dmaic-problem-solving` (Control phase) /
`continuous-improvement-skills:lean-six-sigma-for-software` — stability is their question;
whether a *stable* process meets spec (Cp/Cpk) is this skill's. Likewise, a broad "which metric
for my classifier, ROC AUC or PR AUC?" ask belongs to `machine-learning-skills:model-evaluation`.
If measurement-systems-analysis loads on chart-selection or generic model-metric asks, tighten
the description.

## 3. Quality rubric
A good response:
- **Does the task:** produces a correctly designed study (blind, randomized, parts spanning the
  range; attribute variant with reference answers for pass/fail); runs the ANOVA decomposition
  from the pasted table and reports %GRR (stating the convention), ndc, and kappa against the
  acceptance table; refuses to compute capability without stability evidence; computes Cp and
  Cpk correctly (nearer-edge logic) and prescribes center-first-then-variance.
- **Teaches:** explains σ²_observed = σ²_process + σ²_measurement and why a noisy measurement
  system makes "improvements" appear and vanish; repeatability vs reproducibility as
  instrument-vs-definitions diagnosis; why Cp flatters an off-center process and Cpk doesn't;
  why an unstable process has no σ to plug in.
- **Stays honest:** treats spec limits, %GRR thresholds, and the 1.33 floor as business
  decisions the owner sets, never back-solved from data; treats an LLM judge as an operator
  owing the same agreement evidence as a human inspector, and refuses to rank close alternatives
  on scores from an unqualified judge; flags the 10–30% GRR zone as conditional, not a pass.
