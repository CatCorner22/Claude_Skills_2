# Journal Interpretation Guide

How to read fitness and nutrition research papers critically: methods, confounds, effect
sizes, and mapping to real-world protocol design.

## Section-by-Section Reading Strategy

### Abstract

**What to extract:**
- Study design (RCT, observational, case study, meta-analysis)
- Sample size (N) and population (age, sex, training status)
- Intervention and control conditions
- Primary outcome and effect size (numbers, not just "significant")
- Conclusion as stated by authors

**Red flags:**
- No sample size (often absent in small case studies)
- Outcome statistically significant but effect size trivial (e.g., p < 0.05 but 2% change)
- Conclusion overstates the effect ("proved X prevents Y" when the study shows correlation
  or small effect)

### Methods

**Study design hierarchy (trust order):**
1. Large (N > 100) randomized controlled trial (RCT) with adequate blinding
2. Medium (N > 50) RCT
3. Small (N < 50) RCT
4. Observational cohort study (good for hypothesis generation; confounding is major risk)
5. Case study or small n (N < 10)
6. Mechanistic/cell culture study (confirms pathway; does NOT confirm human effect)

**Critical details to flag:**
- **Randomization and blinding:** Were participants randomly assigned to treatment vs control?
  Was the researcher or participants blinded to allocation? (Single-blind = researcher knows;
  double-blind = neither knows; relevant for fitness because placebo/expectation effects are
  large.)
- **Inclusion/exclusion criteria:** Are participants like your population? College-age men
  trained in the sport generalize poorly to sedentary older women.
- **Adherence measurement:** Did researchers verify that participants actually did the
  intervention? (Self-reported adherence is often inflated.)
- **Dropout rate:** High dropout (>20%) in one arm suggests the intervention is unpleasant or
  ineffective; this weakens the finding.

### Results

**Statistical significance vs effect size — the critical distinction:**

**Statistical significance (p-value):**
- p < 0.05 means "if the null hypothesis (no effect) were true, we would observe a result this
  extreme 5% of the time by chance."
- With large enough sample, trivial effects become significant. (Example: 2% difference in VO₂
  max, N = 500, p < 0.001 is "significant" but meaningless for practice.)
- Do NOT default to "p < 0.05 = true finding." Always check effect size.

**Effect size (d, η, r, percentage change):**
- **Cohen's d:** d = 0.2 (small), d = 0.5 (medium), d = 0.8 (large)
- **Percentage change:** e.g., "4 kg muscle gain over 8 weeks" is human-relevant; "2% increase
  in protein synthesis" requires context (is 2% meaningful over time?).
- **Confidence interval (CI):** e.g., "effect size 0.5 (95% CI 0.1–0.9)" means we are 95%
  confident the true effect is between 0.1 and 0.9. A CI that crosses zero is not significant.

**Example:**
- Study A: "Creatine improves 1RM bench press by 8 kg (95% CI 5–11 kg), p < 0.001, N = 50."
  → Large, precise effect. Use this.
- Study B: "Supplement X improves VO₂ max by 1% (95% CI -1–3%), p = 0.08, N = 200."
  → Effect is trivial and not statistically significant. CI crosses zero. Skip this.

### Discussion & Limitations

**What to look for:**
- Do the authors acknowledge limitations? (Study power, generalizability, confounds they couldn't
  control?)
- Do they overstate their findings? (Common: "proves X causes Y" when the study is observational
  or small)
- Do they discuss real-world applicability? (e.g., "findings apply to resistance-trained men;
  generalization to women or untrained populations is unknown")

**Red flags:**
- Authors don't mention any limitations (either they're not aware or they're hiding them)
- Conclusion is vastly stronger than results (e.g., "suggests" becomes "proves" in the
  conclusion)
- No comparison to existing literature (you have no context for effect size)

## Identifying & Controlling for Common Confounds

### Training Status

**The confound:** A supplement that works for sedentary people may not work for trained
athletes (stronger response to basic stimuli in untrained).

**How to check:** Methods section should state training history (e.g., "resistance-trained
for ≥2 years, regularly lifting 3–5x/week").

**Implication:** An effect found in untrained people (which are easier to study) may not
replicate in the population you care about (trained athletes).

### Controlled vs Ad-Lib Conditions

**The confound:** Feeding and training protocols in labs are supervised and precise;
real-world adherence is messier.

**How to check:** Were meals provided and weighed? Was training supervised and logged?

**Implication:** An effect of "optimal protein timing" (20g whey within 1 hour) in a lab may
vanish if real people eat whenever and wherever they want (total daily protein matters more).

### Protein Confound

**The confound:** Many studies compare "supplement + diet" to "diet alone" without controlling
total protein. Supplement works because total protein increased, not because of the supplement's
unique property.

**How to check:** Do the authors report total protein intake (g/day) in both groups? Is it
equal?

**Implication:** A study showing "BCAAs increase muscle" might actually show "added protein
increases muscle"; BCAAs per se may be irrelevant.

### Selection Bias

**The confound:** Who volunteers for a study is not representative. Motivated people might
adhere better to *any* intervention and see larger effects.

**How to check:** Methods: Were participants recruited from the general population or self-selected
(ads: "seeking motivated athletes")? High self-selection = higher placebo effect.

**Implication:** An intervention showing large effects in self-selected volunteers may show
smaller effects in an average population.

### Publication Bias

**The confound:** Studies with positive results are more likely to be published than negative
results. A literature review biased toward published studies is biased toward positive findings.

**How to check:** Look for meta-analyses; they often report funnel plots (a visual check for
publication bias). If small studies show large effects and large studies show small effects, bias
is likely.

**Implication:** A supplement may appear more effective than it actually is if only the
positive studies made it to print.

## Interpreting Specific Study Types

### Randomized Controlled Trial (RCT)

**Gold standard for establishing causation.** Participants randomly assigned to treatment or
control; outcomes compared.

**Best practice:**
- Large N (> 100)
- Double-blind (neither researcher nor participant knows assignment)
- Low dropout (< 10%)
- Adequate adherence verification

**Effect sizes to expect:**
- Interventions on healthy, trained populations are often smaller (harder to improve already
  good fitness).
- Interventions on sedentary/untrained populations are often larger (low-hanging fruit).

### Meta-Analysis

**Summary of multiple studies; often most reliable.**

**Quality markers:**
- Adequate studies included (> 10 is good; < 5 is risky)
- Studies are homogeneous in design (if one is an RCT and others are observational, averages
  obscure differences)
- Heterogeneity (I²) is reported; high I² (> 75%) means studies disagree (use caution in
  applying the average effect)
- Publication bias assessed (funnel plot reported)

**How to read:**
- If forest plot (visual summary) shows wide confidence intervals, individual study effects
  vary widely; effect is less robust.
- If CIs cross zero, the meta-analysis is not significant despite the abstract's conclusion.

### Observational Study (Cohort, Cross-Sectional)

**Establishes association; NOT causation.** Useful for hypothesis generation but not proof.

**Example:** "People who lift weights have higher testosterone." This is true but could also
mean: (a) lifting raises testosterone, or (b) high-testosterone men are more likely to lift.

**Best practice:** Use observational data to ask a question; then test with an RCT.

### Mechanistic Study (Cell Culture, Animal Model)

**Shows a biological pathway; does NOT prove human effect.**

**Example:** "Creatine increases ATP in muscle cells (in vitro)." True, but does this translate
to strength gains in humans? (It does, as confirmed by RCTs, but mechanism alone is not proof.)

## Red Flags in Abstract & Title

| Red Flag | What It Means |
| --- | --- |
| "Associated with" | Correlation, not causation; observational study |
| "Suggests" | Preliminary finding; not definitive |
| "May increase" | Weak language; equivocal result |
| "Statistically significant" + small N | Likely false positive; small studies have high variance |
| Effect described without confidence interval | Cherry-picked single point; true effect may differ |
| Conclusion contradicts abstract results | Overstatement; read methods |
| No mention of prior literature | Study not contextualized; hard to judge relevance |
| Authors funded by supplement company | Conflict of interest; bias toward positive result (not disqualifying, but higher scrutiny) |

## Real-World Translation

### From Study → Protocol

**Template:**
1. **Study claims:** "[Intervention] increases [outcome] by X%"
2. **Verify:**
   - Is N adequate? (> 50 for pilot; > 100 ideal)
   - Is effect size large or trivial?
   - Does population match yours?
   - Is effect replicated?
3. **Translate to protocol:**
   - Large effect (d > 0.8) + high-N RCT → adopt as main lever
   - Medium effect (d = 0.5) + replicated → secondary optimization
   - Trivial effect (d < 0.2) or unreplicated → skip or monitor
4. **Measure in practice:**
   - Does the effect appear in your cohort? Track and adjust if not.

### Example: Protein Timing

**Study:** "Post-workout protein increases muscle hypertrophy by 5% vs protein consumed hours
later" (N = 20, RCT, college-age men).

**Analysis:**
- Effect size: ~5% is medium
- N = 20 is small; replication needed
- Population: college-age men; may not generalize to older adults or women
- Mechanism: Plausible (MPS window) but confounded if total protein intake differed

**Translation to protocol:**
- Timing is a secondary modulator; total daily protein (0.7–1 g/lb) is primary lever
- If adherence allows, post-workout protein is a minor plus
- If timing creates adherence burden (e.g., person can't eat post-WO), it doesn't matter;
  eat when convenient

## Staying Current

**Reliable secondary sources:**
- PubMed Central (free, primary literature)
- Google Scholar (indexes most journals)
- Meta-analysis papers (JISSN, Sports Medicine, Nutrition Reviews) summarize the field
- Cochrane Reviews (systematic review standard; extremely rigorous)

**How to search:**
- Search: "[outcome] AND [intervention]" (e.g., "hypertrophy AND protein")
- Filter: Recent studies (last 5–10 years) unless a classic paper is foundational
- Read the abstract first; if it matches your question, read methods and results

**Critical reading:**
- Ask: "Would I publish the opposite finding?" If yes, the field is robust. If no, confirmation
  bias may be at play.
- Check for multi-author citations (Schoenfeld et al., Gibala et al.) → often systematic
  reviewers with deep expertise
- Cross-check effect sizes across multiple studies; consistency signals robustness
