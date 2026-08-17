# Evals — continuous-improvement-skills:measurement-systems-analysis

## 1. Positive trigger (should load the skill)
> "Before we claim the new matching rules raised our match rate, I want to know the number
> itself is trustworthy — two analysts reviewing the same borderline exceptions don't always
> agree on what counts as a match. Can you set up a gage R&R style study for that, and then
> tell me whether the process is even capable against the 95% floor management set?"

Expected: skill loads; designs a blind, randomized attribute agreement study (~30–50 items with
adjudicated reference answers, deliberately including borderline cases, each judge scoring twice)
for the match/no-match call; computes within-judge and between-judge agreement plus kappa and
effectiveness against the acceptance bars — **and reports each kappa with its base rate and its 2×2
table**, noting that skewed marginals depress kappa so a bare κ cannot carry a hard verdict; for any
variable metric, the 10×3×3 crossed study with ANOVA decomposition into
repeatability/reproducibility/part-to-part and the %GRR < 10% / ndc ≥ 5 table; then requires
stability evidence (control chart, in-control) before computing Cp/Cpk against the 95% floor;
notes the floor and spec limits are the owner's business decision; recommends centering before
variance reduction.

## 1b. Positive trigger (LLM-judge qualification — the repeat-trial and bias traps)
> "We're using an LLM as the judge for our eval suite. I ran it twice on the same 30 transcripts
> at temperature 0.2 and 0.9 to get a repeatability number, and it agreed with itself 27 out of 30
> times — 90%. It's also the same model that generated the answers it's grading, and we always show
> the new prompt's answer second. Good enough to start ranking prompt variants?"

Expected: skill loads and says **no, and the 90% is not a repeatability number at all**. Names both
temperature traps: varying temperature *between* trials changes the gauge rather than re-measuring
the part, so the disagreement observed is a setting effect (and it is unclear which configuration was
qualified — the one qualified must be the one shipped); conversely, had they run at temperature 0
they would have seen ~100% self-agreement, which is a cached function evaluated twice, not evidence —
determinism is the machine version of an operator who remembers every part, exactly what the
blinding/randomization rule exists to defeat. Prescribes the legitimate repeat trial: fix the
production configuration and re-randomize **presentation** — swap the A/B order and require the
verdict to hold, reshuffle item order, fresh context per item. Flags **position bias** on the
"always show the new prompt second" design as the best-documented LLM-judge pathology, with the
order-swap consistency rate as a headline statistic; flags **self-preference bias** because the
generating model is the judge, and requires a judge from a different model family plus blinding to
authorship; flags **verbosity bias**, with effectiveness stratified by response length. Reports
kappa, not just 90% raw, with the base rate and 2×2 table. And refuses the actual ask — ranking close
prompt variants — until the judge is qualified, since small score deltas sit inside an unqualified
judge's noise.

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
  range; attribute variant with reference answers for pass/fail, borderline cases included); runs the
  ANOVA decomposition from the pasted table and reports %GRR (stating the convention), ndc, and
  kappa against the acceptance table — kappa always accompanied by its 2×2 table and the item set's
  base rate; for an LLM judge, defines the repeat trial as a presentation re-randomization under a
  fixed shipped configuration (never a temperature change), reports swapped-order consistency, uses a
  second judge from a different model family, and tests verbosity and self-preference exposure;
  refuses to compute capability without stability evidence; computes Cp and
  Cpk correctly (nearer-edge logic) and prescribes center-first-then-variance.
- **Teaches:** explains σ²_observed = σ²_process + σ²_measurement and why a noisy measurement
  system makes "improvements" appear and vanish; repeatability vs reproducibility as
  instrument-vs-definitions diagnosis (and reads "repeatable but not aligned to the human" as a
  reproducibility/rubric problem, not a decoding-noise one); why "same conditions" is load-bearing,
  so a temperature change is a gauge change and determinism is an operator with perfect memory; why
  the LLM-judge biases are *predicted* by the operator frame and each has an MSA-shaped control —
  order swap as a genuine repeat trial for position bias, length-stratified effectiveness for
  verbosity bias, independence of inspection from production for self-preference; why kappa's
  chance correction makes it prevalence-sensitive, so the same disagreements score differently on
  differently-balanced item sets; why Cp flatters an off-center process and Cpk doesn't;
  why an unstable process has no σ to plug in.
- **Stays honest:** treats spec limits, %GRR thresholds, and the 1.33 floor as business
  decisions the owner sets, never back-solved from data; treats an LLM judge as an operator
  owing the same agreement evidence as a human inspector, and refuses to rank close alternatives
  on scores from an unqualified judge; flags the 10–30% GRR zone as conditional, not a pass; never
  presents near-100% self-agreement from a deterministic judge as a pass, and never draws a hard
  verdict from a bare kappa or a bare percent agreement; reports PABAK (if at all) beside kappa and
  labelled, not instead of it; carries provenance marks on the external citations (Feinstein &
  Cicchetti on the kappa paradox; the LLM-judge bias literature).
