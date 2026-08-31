# Statistics misrepresentation taxonomy

For each move: the definition, the arithmetic, the plain-language translation, and the literal
question that detects it in a transcript. Every number here has been recomputed from its own inputs.

**Contents**
- §0 The plain-language method (this is technique, not tone)
- §1 The centerpiece: absolute vs relative
- §2 Odds ratios, hazard ratios, and other ratios that are not risk
- §3 Significance, p-values, and intervals
- §4 Base rates and the 2×2
- §5 Endpoints: surrogate, composite, selective
- §6 Analysis-set and selection effects
- §7 Aggregation paradoxes
- §8 Evidence-base effects
- §9 Framing and presentation
- §10 What is already owned elsewhere in this library

---

## §0 The plain-language method

"Explain it like I'm five" is a *technique* here, not a register. Breezy paraphrase fails; the
following reliably works, and it works because people reason far more accurately about natural
frequencies (counts of people) than about conditional probabilities or percentages of percentages.

**The four-part template — apply to every statistic in the report:**

1. **Fix a reference class of real people**, sized so the smallest cell is a whole number ≥ 1.
   "Out of 10,000 people like you", not "0.75%". Use 100 / 1,000 / 10,000 / 100,000.
2. **State the before and after as counts.** "4 in 1,000 would have had a heart attack. With the
   drug, 2 in 1,000 do."
3. **Name the difference in the same units.** "So 2 people out of every 1,000 are spared."
4. **Then, and only then, give the headline number and reconcile it.** "That is the '50% reduction'
   you heard — it is 50% *of a small number*."

Never present a percentage of a percentage. Never give a relative figure without its baseline in
the same breath.

---

## §1 The centerpiece: absolute vs relative

**The six quantities.** CER = control event rate (the base rate). EER = experimental event rate.

| | Definition |
| :--- | :--- |
| RR (risk ratio) | EER / CER — 1 means no effect |
| RRR (relative risk reduction) | 1 − RR = (CER − EER)/CER — **the headline number** |
| ARR (absolute risk reduction) | CER − EER — measured in percentage **points** |
| NNT (number needed to treat) | 1 / ARR — round **up**, report as an integer |
| NNH (number needed to harm) | 1 / ARI, where ARI = EER − CER when treatment increases the event |
| OR (odds ratio) | [EER/(1−EER)] / [CER/(1−CER)] |

**The three identities that do all the work:**

```
ARR = CER × RRR          ← the reconstruction identity
NNT = 1 / (CER × RRR)    ← RRR alone can NEVER give an NNT
RR  = 1 − RRR
```

The second line is the whole argument. A relative reduction, by itself, is mathematically
incapable of telling you how many people benefit. It needs the baseline.

**Worked: the same "50% reduction", twice.**

| | Common outcome | Rare outcome |
| :--- | ---: | ---: |
| CER | 20.0% | 0.4% |
| RRR | 50% | 50% |
| ARR = CER × RRR | 10.0 pp | 0.20 pp |
| EER | 10.0% | 0.2% |
| NNT = 1/ARR | **10** | **500** |
| per 1,000 people | 200 → 100 events; 100 spared | 4 → 2 events; 2 spared |

Identical headline. In one case you treat 10 people to help one; in the other, 500. The relative
number is the same in both columns, which is exactly why quoting it alone is the move.

**Plain language:** "Out of 1,000 people, 4 would have had the event. With treatment, 2 do. So 2
people in every 1,000 are spared — that is what 'cuts the risk in half' means here."

**The corrective is not to discard the relative number.** RRR is often more stable across
populations than ARR, which is why trials report it and why it transfers. The honest presentation
is *both, with the baseline*: "a 50% relative reduction, from 0.4% to 0.2%, so 2 fewer events per
1,000 people treated."

**Reconstructing absolute risk when only relative is reported.** You need exactly one extra number:
the control-arm event rate over the study's follow-up. Find it, in descending reliability: (1) the
primary results table, events/N per arm — compute everything yourself; (2) event counts in the
abstract; (3) a Kaplan–Meier curve read at the endpoint, CER ≈ 1 − S_control(t); (4) the registry
record or supplementary appendix; (5) a population reference rate, clearly labelled as an
approximation. If none is available, say the absolute effect **cannot be determined** — do not
invent a baseline to make the arithmetic work.

**Detection question:** *Does every relative figure in the transcript appear with its baseline?*
If a video says "reduces risk by X%" and never states the starting risk, that is finding O1+O2.

---

## §2 Ratios that are not risk

### Odds ratio read as a risk ratio

**Direction rule, proved by exhaustive sweep** (p₀ from 0.01 to 0.99 × RR ∈ {0.1, 0.3, 0.5, 0.8,
1.2, 1.5, 2.0}, 594 combinations, **zero violations**): an OR is always at least as far from 1 as
the corresponding RR. So reading an OR as a risk ratio **always exaggerates**, never understates.

Divergence with the true RR held at 0.50 and only the base rate moving:

| CER | OR | RRR if you misread OR as RR | true RRR |
| ---: | ---: | ---: | ---: |
| 0.1% | 0.4997 | 50.0% | 50.0% |
| 1% | 0.4975 | 50.3% | 50.0% |
| 5% | 0.4872 | 51.3% | 50.0% |
| 10% | 0.4737 | 52.6% | 50.0% |
| 30% | 0.4118 | 58.8% | 50.0% |
| 50% | 0.3333 | 66.7% | 50.0% |

**Rule of thumb:** the approximation is safe when the outcome is rare (roughly under 10%) and
degrades fast above that. **Detection:** *does the source report an odds ratio while the video says
"X times more likely" or "X% more likely"?*

### Hazard ratios

An HR is a ratio of instantaneous event *rates*, averaged over follow-up. It is not a risk ratio and
not a ratio of survival times.

**The big defect is that an HR is scale-free.** The same HR maps to wildly different absolute
benefit. Under proportional hazards (S_treated = S_control^HR), with HR = 0.70:

| Control 5-year survival | Treated survival | Absolute gain | NNT |
| ---: | ---: | ---: | ---: |
| 50% | 61.56% | 11.56 pp | **9** |
| 95% | 96.47% | 1.47 pp | **68** |

An identical "30% reduction in hazard" is worth 7.5x more in one population than the other.
**Detection:** *does the video convert a hazard ratio into a personal risk without naming the
baseline survival?*

---

## §3 Significance, p-values, and intervals

### What p actually is

p = P(data at least this extreme | H₀ true, **and** all model and design assumptions hold). It is
computed *assuming* the null, so it cannot be a probability *about* the null.

**Catch these literal transcript strings:**
- "only a 3% chance this is a fluke / happened by chance" → false; p is not P(H₀ | data).
- "so we're 97% sure it's real" → false; 1 − p is nothing.
- "p = 0.03 means it'll replicate 97% of the time" → false; replication probability tracks power.
- "p was 0.06 so there's no effect" → false; absence of evidence is not evidence of absence.

**The difference-of-significance fallacy** — "A worked, B didn't" derived from two p-values on
opposite sides of 0.05. A difference between "significant" and "non-significant" is not itself
significant; that requires a test of the *interaction*. Highly detectable in transcripts.

### Confidence intervals

The 95% is a property of the *procedure's* long-run capture rate, not a probability about the one
interval in front of you. The useful diagnostic is not width in the abstract but **where the
interval sits relative to a threshold of practical importance named in advance**:

- RR 2.0, CI 1.8–2.2 → ratio 1.22x. Precise; every value means the same thing.
- RR 2.0, CI 1.01–14.5 → ratio 14.4x. "Significant" and nearly uninformative.
- RR 0.98, CI 0.95–1.06 → crosses 1 and is *narrow*. This is an informative **null**, not a failure.

"Crosses the null" and "wide" are independent. A narrow interval around the null is evidence of
absence; a wide one crossing the null is absence of evidence. Videos conflate them constantly.

### Power, and why a small significant study is probably exaggerated

Sizing constant: (z₀.₉₇₅ + z₀.₈₀)² = (1.95996 + 0.84162)² = **7.8489**.
For proportions, n per arm = 7.8489 × [p₁(1−p₁) + p₂(1−p₂)] / (p₁−p₂)².
For 10% vs 8%: 7.8489 × (0.0900 + 0.0736) / 0.0004 = **3,211 per arm**. A video citing an n = 200
trial that "found" a 2-point difference is describing a study with almost no power to find it.

**Type-M (magnitude) error.** With α = 0.05 two-sided and a true effect of 1.0 SE, power = **17.0%**,
and the expected published estimate *among the studies that reach significance* is **2.49 SE** —
roughly 2.5x the truth. Underpowered significant results are systematically inflated. This is why
"a study found" plus a small sample is a red flag rather than a reassurance.

**Detection:** *how many participants, and is the reported effect large relative to what that
sample could reliably detect?*

---

## §4 Base rates and the 2×2

Sensitivity, specificity, PPV, and base-rate neglect are **one entry**, because they are one table.
Sensitivity = TP/(TP+FN) and specificity = TN/(TN+FP) are properties of the **test**. PPV = TP/(TP+FP)
is a property of the test **and the population**. Videos state the first pair and let viewers hear
the second.

**Worked, in natural frequencies.** Test 90% sensitive, 90% specific; disease prevalence 1%; 10,000 people:

```
   100 have it      →  90 test positive,  10 missed
 9,900 don't        → 990 test positive (false),  8,910 correctly negative
 positives = 90 + 990 = 1,080
 PPV = 90 / 1,080 = 0.0833 = 8.3%
```

A "90% accurate" test, in a population where 1% have the condition, is **wrong about 92% of the
people it flags**. Nothing about the test changed; only the base rate.

**Detection:** *does the video give a test's accuracy without the prevalence?* If yes, the viewer
cannot compute what a positive result means, and the omission is the finding.

---

## §5 Endpoints

### Surrogate vs hard endpoints

A surrogate stands in for an outcome people care about. It is valid only if the treatment's effect
on the surrogate reliably transmits to the hard outcome — an empirical claim about that treatment,
not a property of the marker.

**The canonical real case — CAST** (Cardiac Arrhythmia Suppression Trial, preliminary report, NEJM
1989, doi 10.1056/NEJM198908103210629). Encainide and flecainide suppressed premature ventricular
contractions exactly as designed. The surrogate worked. Total mortality:

```
 drug     56/730 = 7.67%
 placebo  22/725 = 3.03%
 RR = 2.53      ARI = 4.64 pp      NNH = 22
```

Arrhythmic death or cardiac arrest: 33/730 (4.52%) vs 9/725 (1.24%), RR 3.64. Per 1,000 treated,
about 46 extra deaths. The surrogate improved and people died at two and a half times the rate.

**Detection:** *is the outcome the video cares about the outcome the study measured?*

### Composite endpoints

A composite counts a patient as having "the event" if **any** of several outcomes occurs. It buys
power at the cost of interpretability, because the components are neither equally important nor
equally affected.

Worked (constructed; composite = death, MI, or hospitalisation for angina; 1,000 per arm):

```
 Composite: 120/1,000 control vs 90/1,000 treated
   RR 0.75 · RRR 25.0% · ARR 3.0 pp · NNT 34          ← the headline
 Components:
   death           20 vs 20  → RRR  0.0%,  ARR 0.00 pp
   MI              25 vs 24  → RRR  4.0%,  ARR 0.10 pp
   angina hosp.    75 vs 46  → RRR 38.7%,  ARR 2.90 pp   ← carries the entire effect
```

The headline is real and the drug does nothing measurable to death or MI. **Detection:** *does the
video say "heart attacks and deaths" where the source's effect lives entirely in the softest
component?*

### Selective endpoint and subgroup reporting

**Multiplicity arithmetic.** With k independent tests at α = 0.05, P(≥1 false positive) = 1 − 0.95^k:

| k | 1 | 5 | 8 | 10 | 12 | 20 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| P | 5.0% | 22.6% | 33.7% | 40.1% | 46.0% | 64.2% |

**The canonical real case — ISIS-2.** Asked by reviewers to break the aspirin result down by
subgroup, the investigators subdivided roughly 17,000 patients by astrological birth sign. Aspirin
appeared not to work for those born under Gemini or Libra, and to work exceptionally well for
Capricorn — published deliberately, and placed first, to show readers what subgroup analyses are
worth. The point is not that the astrology was silly; it is that *statistically it is no different*
from the clinically-plausible subgroup analyses that routinely change practice.

**Detection:** *is the video's headline number the primary endpoint in the whole population, or a
slice? And how many slices were examined?*

---

## §6 Analysis-set and selection effects

### Intention-to-treat vs per-protocol

ITT analyses everyone as randomized, regardless of what they did. Per-protocol keeps only those who
completed the protocol — which conditions on post-randomization behaviour, a collider, and
reintroduces confounding. Adherers differ from non-adherers in many ways besides adherence.

Worked (constructed; 1,000 per arm). Treatment arm: 800 adherent with 40 events (5.0%), 200
non-adherent with 30 (15.0%) → 70/1,000 = 7.0%. Control: 90/1,000 = 9.0%.

```
 ITT:            RR 0.778 · RRR 22.2% · ARR 2.0 pp · NNT 50
 Per-protocol:   RR 0.556 · RRR 44.4% · ARR 4.0 pp · NNT 25
```

The per-protocol analysis doubles the apparent effect without the drug doing anything more.

### Regression to the mean

Select cases for being extreme on a first measurement and they will, on average, be less extreme on
a second — with no intervention at all. With equal SDs and test–retest correlation r:
E[post | pre] = μ + r·(pre − μ).

Worked: μ = 100, SD = 15, r = 0.60, select everyone scoring 130 (2 SD high), apply an inert
intervention. E[retest] = 100 + 0.60 × 30 = **118**. Apparent improvement = 12 points = **0.80 SD**
— a large effect size, from nothing. **Detection:** *were participants selected for being extreme,
and is there a control group?* Without a control arm, this alone can produce the whole result.

### Survivorship bias

The sample contains only what survived a selection process, and the process is invisible in the
data. **Detection:** *who or what is missing from this dataset because it did not make it in?*

---

## §7 Aggregation paradoxes

### Simpson's paradox

An association present in every subgroup can reverse in the aggregate, because the aggregate is a
share-weighted blend and the shares differ.

```
 Programme A: easy 90/100 = 90.0% · hard 30/100 = 30.0% · total 120/200 = 60.0%
 Programme B: easy 170/200 = 85.0% · hard 5/20 = 25.0% · total 175/220 = 79.5%
```

A beats B on easy cases **and** on hard cases, and loses overall — because A's caseload is 50.0%
hard and B's is 9.1%. It is not a paradox; it is a weighting fact.

### Ecological fallacy

Inferring an individual-level relationship from group-level aggregates. Constructed, 1,000 people
per district:

```
 District 1: 300 immigrants (30% share), 70.0% literate; 700 natives, 98.6% → overall 90.0%
 District 2: 100 immigrants (10% share), 70.0% literate; 900 natives, 81.1% → overall 80.0%
```

Across districts, more immigrants tracks with *higher* literacy. Within both districts, immigrant
literacy is *lower* (70.0% vs 98.6% and 81.1%). Both facts are true; only one is about people.

---

## §8 Evidence-base effects

**Publication bias.** Positive, novel, significant results are published more and faster, so the
visible literature is a biased sample of the conducted literature and a meta-analysis inherits the
bias exactly. **Funnel plot:** effect against precision; absent bias, small studies scatter
symmetrically at the bottom. A *missing corner* where small null results should be is the signal.
Honest caveat most treatments omit: funnel asymmetry is **not** synonymous with publication bias —
genuine small-study effects and heterogeneity produce it too.

**Heterogeneity.** I² is the share of variability due to real differences between studies rather
than chance. Above roughly 75%, a pooled point estimate can be close to meaningless: the studies
are not estimating the same thing. A prediction interval (where a *future* study would land) is
usually far wider than the confidence interval around the pooled mean, and is the more honest
number. **Detection:** *does the video say "meta-analysis" as though it settled the question?*

---

## §9 Framing and presentation

### Asymmetric framing — the highest-value check, run it first

The same video quotes the **relative** number for the effect it likes and the **absolute** number
for the effect it dislikes: "cuts your risk 30%" beside "side effects in under 1% of people". Both
numbers can be perfectly correct. The pairing is the lie, because the two are on different scales
and cannot be compared by the listener.

**Detection:** build a two-column table of every benefit claim and every harm claim with the
**scale** of each, and check whether the scales match. A mismatch is a first-class finding *even
when every individual number is accurate* — which is why this check must be run explicitly rather
than emerging from claim-by-claim fidelity coding, which would pass all of them.

### Percentage points vs percent change

The difference between two percentages is in percentage **points**; expressing it as a percent
divides by the base and gives a different, also-true number.

```
 2.0% → 3.0%   : +1.00 point   · +50.0% relative
 47%  → 52%    : +5.00 points  · +10.6% relative
 0.02% → 0.04% : +0.02 points  · +100% relative
```

The trap runs both ways: "rates rose 2%" understates a 4%→6% move; "conversions jumped 50%" oversells
a 2%→3% move. The honest sentence carries both. This is the same arithmetic as §1 in different
clothing — ARR is in points, RRR is in percent.

### Per-capita vs raw counts, and denominator choice

```
 Country X: 500,000 deaths / 330M = 1,515 per million
 Country Y: 130,000 deaths /  67M = 1,940 per million
```

Raw counts make X look 3.8x worse; per-capita makes Y 28% worse. Both true. The deeper move is
**denominator selection**: per-capita, per-adult, per-100,000, per person-*year*, per exposure, per
mile, per trip can each rank the same two units differently. **Detection:** *what is the
denominator, and would another obvious one reverse the ranking?*

### Truncated axes and visual distortion

Bar charts encode value by **length**, so a truncated baseline breaks the encoding. Quantify it:

> exaggeration factor = (visual ratio of the marks) ÷ (true ratio of the values)

Two bars, 47% and 52%. From zero: 52/47 = 1.106. From 45: (52−45)/(47−45) = 7/2 = 3.500.
Exaggeration = 3.500 / 1.106 = **3.16x**.

Report it as a number: "the chart at 04:09 truncates the y-axis at 45%, inflating a 5-point gap by
a factor of 3.2." (Line charts showing change over time are the legitimate exception — they encode
by position, not length.) Note this is a **visual** finding: it needs the frame, not the transcript,
so it can only be audited when the user supplies the chart or describes it.

---

## §10 What is already owned elsewhere in this library

Cross-link these rather than restating them. Duplication is a real defect here.

| Topic | Owner |
| :--- | :--- |
| p-value and CI misreadings in general practice, hypothesis testing | `data-analytics-bi-skills:statistical-inference` |
| Confounding, colliders, backdoor criterion, the identification ladder, why filtering is conditioning | `data-analytics-bi-skills:causal-inference` |
| Type-M/winner's curse in experiments, peeking, SRM, MDE, variance reduction | `data-analytics-bi-skills:ab-test-design` |
| Evidence hierarchy, GRADE-lite grading, retraction and predatory-venue checks, NNT/NNH in clinical context | `deep-research-skills:medical-research-detective` (`references/evidence-appraisal.md`) |
| Effect size vs significance, Cohen's d bands, funnel plots, I², abstract red-flag language | `coding-agent-skills:fitness-nutrition-science` (`references/journal-interpretation-guide.md`) |
| Absolute-vs-relative and diagnostic-accuracy statistics applied to your own project's metrics | `continuous-improvement-skills:project-command-center` |
| Making a technical finding land for a non-specialist audience | `writing-skills:explanation-design` |

**This skill's own contribution** is the layer those do not have: the arithmetic, the
plain-language translation, and the **transcript-detection question** for each move — the operational
bridge from a statistical concept to a sentence someone actually said on camera.
