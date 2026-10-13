# Risk communication for genetic findings

How to turn a genotype into a number a person can actually use, and the three ways genetic risk
figures mislead that general statistics guidance does not cover.

**Contents**
- §1 What is already covered elsewhere — cross-link, do not rewrite
- §2 Absolute beside relative, worked
- §3 Penetrance, ascertainment, and age-conditioning
- §4 Ancestry portability and polygenic scores
- §5 Negative results and what a panel did not probe
- §6 The reporting template

---

## §1 What is already covered elsewhere — cross-link, do not rewrite

Duplication is a real defect in this library. The general machinery already exists and is verified:

| Topic | Owner — use it, don't restate it |
| :--- | :--- |
| ARR/RRR/NNT, the three identities, odds-ratio-vs-risk-ratio divergence, natural frequencies, base rates and PPV, truncated axes, the full misrepresentation taxonomy | `deep-research-skills:video-source-audit` → `references/statistics-taxonomy.md` |
| Evidence hierarchy, GRADE-lite grading, retraction and predatory-venue checks | `deep-research-skills:medical-research-detective` → `references/evidence-appraisal.md` |
| Effect size vs significance, confidence intervals, publication bias, heterogeneity | `coding-agent-skills:fitness-nutrition-science` → `references/journal-interpretation-guide.md` |
| Hypothesis testing, interval interpretation | `data-analytics-bi-skills:statistical-inference` |
| Confounding, colliders, why filtering is conditioning | `data-analytics-bi-skills:causal-inference` |
| Making a technical finding land for a non-specialist | `writing-skills:explanation-design` |

**What is genetics-specific, and therefore belongs here:** penetrance and ascertainment bias,
age-conditioned remaining risk, ancestry portability, and the weakness of a negative result from a
panel that probed a subset. Those four are this file's contribution; everything else is a link.

---

## §2 Absolute beside relative, worked

**The rule: a relative figure is unreportable without its baseline.** Not discouraged — unreportable.
A genotype's relative risk is routinely published against a population baseline the reader does not
know, so the multiple alone conveys almost nothing.

**The same multiple, two baselines** (RR 3.0 throughout). **Read the first row carefully: it is the
risk in NON-carriers, the referent group the ratio was measured against** — not the population
average, which already contains the carriers:

| | Rare outcome | Common outcome |
| :--- | ---: | ---: |
| Baseline absolute risk **in non-carriers** | 0.5% | 12.0% |
| Carrier absolute risk | 1.5% | 36.0% |
| Absolute increase | 1.00 pp | 24.00 pp |
| Per 1,000 people | 5 → 15 (10 extra) | 120 → 360 (240 extra) |
| Number needed to harm | 100 | 5 |

Identical headline. One is a rounding error in a life; the other reorganises it. **Reporting "triples
your risk" without the baseline makes those two indistinguishable**, which is why this skill treats
the omission as a defect rather than a simplification.

**NNH is ⌈1 / ARR⌉** — here 1 / 0.010 = 100 exactly in the rare column, and ⌈1 / 0.24⌉ = 5 in the
common one. **One computation trap, because it put a wrong 101 in that cell until a verification
pass recomputed it:** in floating point `0.015 - 0.005` is `0.009999999999999998`, so `1/arr` is
`100.00000000000001` and `ceil()` returns 101. Measured over integer NNH targets from 2 to 1,000,
formed as `baseline + 1/n` minus `baseline`, the bare `ceil()` is off by one for **30% of them at a
0.5% baseline, 37% at 1% and 47% at 10%** — and `ceil(round(1/arr, 9))` gets all of them right.
The lesson generalises past this cell: **an off-by-one in a derived integer is invisible to review
because it looks like a rounding convention**, so recompute them rather than reading them.

### Multiplying a POPULATION baseline by a relative risk inflates the answer

The shortcut everyone takes — population baseline × the published RR — is wrong in the unsafe
direction, because a population average already includes the carriers. With carrier frequency `f` and
carrier risk `RR × r₀`:

```
 K = (1 − f)·r₀ + f·RR·r₀        so        r₀ = K / (1 + f·(RR − 1))
```

At RR 3.0 and f = 0.10, a 12.0% *population* risk implies a **10.0%** non-carrier risk and a 30.0%
carrier risk — not the 36% the shortcut gives. On the rare column, a 0.5% population risk implies
0.42% in non-carriers and **1.25%** in carriers, so the extra risk is 0.83 pp and the NNH is 120,
not 100.

> **"Baseline" and `p₀` mean the risk in people WITHOUT the variant throughout this file** — the
> reference-genotype group, never the population average. For a **rare** high-penetrance variant the
> two coincide to within rounding, which is why the columns above are safe as written. For a
> **common** risk allele they do not, and the gap runs in the alarming direction.
>
> **So the shortcut is adequate only when the risk genotype is rare** — at a carrier frequency of a
> few percent the correction is within rounding. Above that, divide by `1 + f·(RR − 1)` first. **And say
> which baseline you used**, because §4 of this file calibrates the other way (genotype-weighted mean
> equal to the prevalence), and a file that uses both conventions silently is a file that will be
> quoted wrongly.

### Case-control designs report odds ratios, and genetic studies are full of them

Much genetic association data comes from case-control designs, which yield **odds ratios**, not risk
ratios. Converting at a known baseline p₀:

```
RR = OR / (1 − p₀ + p₀·OR)
```

**The error from reading an OR as an RR has an exact signed form:**

```
 (OR − RR) / RR  =  p₀ · (OR − 1)
```

Read that carefully, because it says two things the usual advice misses:

1. **It is signed.** For `OR > 1` the OR overstates the risk ratio. **For a protective `OR < 1` it
   UNDERSTATES it** — the true RR is closer to 1 than the OR, so the variant looks more protective
   than it is. Protective ORs are everywhere in genetic data, since the same variant is reported
   with either allele as reference, and this is the **false-reassurance** direction.
2. **It scales with `(OR − 1)`, not with the baseline alone.** At OR = 2 the relative overstatement
   happens to equal p₀ exactly, which is why that case gets quoted as the rule — but at OR = 3 it is
   twice the baseline and at OR = 5 it is four times.

| OR | Baseline p₀ | True RR | Error from reading OR as RR |
| ---: | ---: | ---: | ---: |
| 2.0 | 1% | 1.980 | +1.0% |
| 2.0 | 10% | 1.818 | +10.0% |
| 2.0 | 30% | 1.538 | +30.0% |
| 3.0 | 30% | 1.875 | +60.0% |
| 5.0 | 30% | 2.273 | +120.0% |
| **0.5** | **30%** | **0.588** | **−15.0%** — "halves your risk" overstates the benefit |

Safe to approximate when the outcome is rare *and* the OR is near 1; it degrades in proportion to
both the baseline and `(OR − 1)`. **Always check which measure the source reported** — a paper
saying "OR" and a report saying "times the risk" are not the same claim.

---

## §3 Penetrance, ascertainment, and age-conditioning

**Penetrance is the genetics word for absolute risk**: the probability a carrier develops the
condition. It is the number that matters, and it is the number most often quoted wrongly.

### Ascertainment bias — and the honest, narrower version of the rule

Estimates derived from families selected *because* they contained many affected members describe
those families. Someone who finds the same variant incidentally, with no family history, is a
different case.

**The defensible statement, which is narrower than the usual one.** For BRCA1/2 — the canonical
example — family-ascertained lifetime estimates ran substantially above population-based ones in the
older literature; one family-based study's title makes the point directly, that risks quoted should
reflect the cancer burden in the family
([PMC2447846](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2447846/)), against population-based
series ([PMID 11044354](https://pubmed.ncbi.nlm.nih.gov/11044354/) /
[PMC2408797](https://pmc.ncbi.nlm.nih.gov/articles/PMC2408797/)). **But newer and larger estimates
overlap considerably**, and at least one population-screening study found risks in
population-ascertained carriers comparable to family-ascertained ones
([PMID 25192939](https://pubmed.ncbi.nlm.nih.gov/25192939)), and a large US series put absolute
cumulative risks at the lower end of the published range with wide intervals
([PMID 16484695](https://pubmed.ncbi.nlm.nih.gov/16484695)) — which is an argument for rule 4 below.

**Two disciplines on this comparison, both learned by getting it wrong here:**

- **The gap is a BRCA1 result in the records cited, not a both-genes result.** Scope the claim to the
  gene you can support it for, and do not let "for the same gene" stand in for "for either gene".
- **The two records are not comparable on age horizon** — one reports penetrance to 70, the other to
  80. Comparing across horizons is precisely the error the next subsection forbids, and it was
  committed inside the paragraph that establishes this file's safety argument. **Read the horizon off
  each record and state it beside each figure.** The figures are not reproduced here because they did
  not resolve to a retrieved record in this environment (`variant-catalog.md` §0); get them from the
  records, with their intervals and their carrier counts, which are small.

*Withdrawn on re-check: an earlier version of this paragraph claimed, citing PMID 16484695, that
variation between families carrying the same variant exceeds variation between positions within a
gene. A verification pass could not find that result in the cited paper, which is a
penetrance-estimation study rather than a variance partition. The claim is withdrawn rather than
rehedged, and the record is kept for what it does establish.*

So the rule is **not** "family-based estimates are inflated, discount them". It is:

1. **Use population-based estimates for a person tested without family history** — that is their
   situation, and it is the consumer-genomics situation by definition.
2. **Use family-informed estimates when there is a family history**, because then the family burden
   is real information.
3. **Never quote only one figure, in either direction.** This cuts both ways, and the second
   direction is the one usually missed: quoting only the *population* figure to someone who **does**
   have a strong family history **under-warns them**, and that is its own safety failure. For BRCA1,
   family-ascertained estimates have run well above population-based ones, and that gap is large
   enough for the choice to matter clinically — quote both, with their age horizons.
4. **Quote a range, not a point.** Any single penetrance figure presented as *the* number is
   overstating what the literature supports.
5. **Report which kind of estimate you used and why** — and, where family history is unknown, report
   both and say which applies under which assumption rather than silently picking.

### Age-conditioning: condition first, then state the direction — it is not always downward

Lifetime risk quoted "from birth" includes years the person has already passed without the outcome.
**Conditioning is a division, and it is the step that gets skipped:**

```
 remaining risk from age a  =  ( F(end) − F(a) )  /  ( 1 − F(a) )
```

where `F` is cumulative incidence. Worked on an explicit, checkable distribution — incidence
(unconditional probability of a first event in that decade), summing to a 12.0% lifetime risk:

| by 40 | 40–49 | 50–59 | 60–69 | 70–79 | 80–89 | total |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.5% | 1.0% | 1.5% | 2.5% | 3.5% | 3.0% | 12.0% |

```
 lifetime risk from birth                              12.00%
 unconditional risk after 50 (the decades summed)      10.50%   <- NOT the answer
 realised by 50                                         1.50%
 remaining risk GIVEN event-free at 50 = 10.5 / 98.5   10.66%   <- the answer
 so the birth figure overstates a 50-year-old's remaining risk by 12.6%
 the same arithmetic at 70:  6.5 / 94.5 = 6.88%,  overstating by 74.5%
```

**Dividing by the probability of having reached that age event-free is the whole operation**, and
skipping it — reporting the summed post-index decades as though they were conditional — is an easy
and quiet error. The gap widens sharply with age and with conditions whose incidence is front-loaded.

**Summed decade *incidence* is not summed *hazard*.** If a source gives hazards, cumulative incidence
is `1 − exp(−Σh)`, which for Σh = 0.12 is 11.3%, not 12.0%.

### The direction is not fixed, and assuming it is was an error in this file

The block above has no **competing mortality** in it, and that omission is what makes the answer look
one-directional. In reality two forces oppose each other: the person has **passed through some
incidence** (which lowers their remaining risk) and has also **survived the other-cause mortality
that would have removed them from the denominator** (which raises it). Which wins depends on where
the incidence sits relative to the mortality curve.

Computed on a discrete competing-risk life table (Gompertz–Makeham other-cause mortality, two
disease-hazard shapes each calibrated to a **12.00%** birth-cohort lifetime risk):

| Age | Mid-onset condition | Late-onset condition (nothing before 60) |
| ---: | :--- | :--- |
| 40 | 12.10% — birth figure **understates** by 0.8% | 12.34% — **understates** by 2.7% |
| 50 | 11.47% — **overstates** by 4.6% | 12.54% — **understates** by 4.3% |
| 60 | 9.96% — **overstates** by 20.5% | 12.94% — **understates** by 7.3% |
| 70 | 7.52% — **overstates** by 59.5% | 12.74% — **understates** by 5.8% |
| 80 | 4.69% — **overstates** by 156.0% | 11.05% — **overstates** by 8.6% |

**For a late-onset condition, quoting the from-birth lifetime figure to a 50-year-old UNDERSTATES
their remaining risk** — the opposite of the intuition, and the under-warning direction. For a
mid-onset condition past 50 the usual intuition holds, and the overstatement becomes large with age.

**And naive subtraction is biased, always downward, with the bias growing in exactly the range where
age-conditioning matters.** On the mid-onset shape above, subtracting pre-index incidence from the
lifetime total gives 10.85% at 50 against a correct 11.47%, and 6.09% at 70 against 7.52%. Dividing
by the probability of being alive and event-free is not a refinement; it is the calculation.

> **The rule, direction-neutral: age-condition, then say which way it went and why.** Never assert
> that a from-birth figure overstates — check it against the condition's onset profile, and say so
> when the literature does not give you enough to check.

### Three more ways a published ratio is not the multiplier it looks like

**1. A hazard ratio is not a multiplier on lifetime penetrance.** Under proportional hazards the
survival function is raised to the power of the HR, so the risk ratio you can report is always
*smaller* than the HR, and the gap widens as the baseline rises:

| Baseline lifetime risk | HR 2 → carrier risk (actual risk ratio) | HR 3 | HR 5 |
| ---: | :--- | :--- | :--- |
| 5% | 9.75% (1.95×) | 14.26% (2.85×) | 22.62% (4.52×) |
| 12% | 22.56% (1.88×) | 31.85% (2.65×) | 47.23% (3.94×) |
| 30% | 51.00% (1.70×) | 65.70% (2.19×) | 83.19% (2.77×) |

So "HR 3 on a 12% baseline" is a **31.9% absolute risk and a 2.65× risk ratio** — not 36% and not
3×. Multiplying a baseline penetrance by an HR overstates, mildly for rare outcomes and materially
for common ones.

**2. Check what the ratio is measured against.** Genotype relative risks silently switch comparators
between *versus non-carriers* and *versus the population average*, and the population average
already contains the carriers. With a 20% carrier frequency, a 5% non-carrier risk and a 3× carrier
effect, the population average is 7.0% — so the same finding is "3× " against non-carriers and
"2.1× " against the population. **A 40% difference in the headline, with no disagreement about the
biology.** Report the comparator, every time.

**3. `OR²` for a homozygote is a small-effect approximation, and it breaks loudly.** The log-additive
model says the per-allele odds ratio squares for two copies — on the **odds** scale. Treating `OR²`
as a multiplier on *risk* works only while risks are small:

```
 per-allele OR 2.0, baseline  5%:   OR^2 as a risk multiplier 20.0%   on the odds scale 17.4%
 per-allele OR 2.0, baseline 20%:                             80.0%                      50.0%
 per-allele OR 4.0, baseline 20%:                            320.0%  <- impossible       80.0%
```

**Convert on the odds scale and back, and if a figure comes out above 100% that is the model failing,
not the person's risk.** For the high-OR rare variants this skill triages, the approximation is
unusable.

---

## §4 Ancestry portability and polygenic scores

**Establish ancestry before quoting any population estimate.** This determines whether a number
means anything for this person, and it is not a caveat to append at the end.

### Lead with the absolute number, not the AUC

AUC is the figure that gets published, and the one that sounds impressive. It is the wrong headline
for a person, and the precise reason matters: **AUC does not depend on how many cases are in the
study sample, so it cannot be read as this person's risk.** (It is *not* independent of prevalence
under a fixed model — that is a common misstatement, and this file made it. Moving the liability
threshold changes the score distributions themselves.) The same score, two prevalences:

```
 score explaining 5% of liability variance, top decile flagged
   outcome affecting 1 in 10     baseline 10.0%  ->  top decile 18.2%   (1.8x)   AUC 0.62
   outcome affecting 1 in 100    baseline  1.0%  ->  top decile  2.4%   (2.4x)   AUC 0.67
```

The *multiple* is larger in the second case while the absolute risk is a seventh of it — and the AUC
is *higher* there too, which makes the point sharper rather than weaker: **the figure that improved
is the one that tells the person least.**

**The quantities to report are the top-decile absolute risk and the share of cases that fall
outside the flagged group.** Computed under a liability-threshold model with a normally distributed
score at 10% population prevalence — this is arithmetic, not a literature claim, and it is
reproducible from the model as stated:

| Variance explained (liability scale) | AUC | Top decile | Bottom decile | Top-vs-bottom OR |
| ---: | ---: | ---: | ---: | ---: |
| 1% | 0.56 | 13.3% | 7.2% | 1.99 |
| 3% | 0.60 | 16.1% | 5.4% | 3.35 |
| 5% | 0.62 | 18.2% | 4.4% | 4.88 |
| 10% | 0.67 | 22.4% | 2.8% | 10.2 |
| 20% | 0.74 | 29.3% | 1.2% | 35.3 |

At AUC 0.62 — a respectable published figure — the individual-level reading is the part that gets
dropped:

- in the flagged top decile, **18 in 100 develop the outcome and 82 do not**;
- **81.8% of everyone who develops it is outside the flagged decile**, so the score misses most
  cases while sounding like a test;
- the headline multiple is substantially a **choice of cutpoint**, not a property of the person:
  top 20% → 16.2% (1.6×), top 10% → 18.2% (1.8×), top 5% → 20.1% (2.0×), top 1% → 24.1% (2.4×).

**So ask for the cutpoint *and* the variance explained before repeating a multiple — and do the
check, because the two constrain each other.** A claim that "the top 8% of people are at threefold
risk" cannot come from a modest score: at 10% prevalence it requires a score explaining about **19%**
of liability variance (AUC ≈ 0.73), stronger than every row of the table above bar the last. For the
5%-variance score this section has been using, threefold is first reached at roughly the **top
0.1%** (top 1% gives 2.4×, top 0.1% gives 2.9×).

So a big multiple at a *wide* cutpoint means a genuinely strong score, and a big multiple at a very
narrow one is a tail statement. **Neither is the person's risk**, which is the absolute number — but
dismissing the first as a cutpoint artefact would be wrong, and an earlier version of this file
invited exactly that.

### Portability, and what it does to the number

Scores built predominantly from European-ancestry GWAS transfer poorly to other ancestries. The
mechanism compounds three things: linkage-disequilibrium structure differences, allele-frequency
differences, and the fact that the tagged SNP is usually not the causal one — so a tag that tracks
the causal variant in the discovery population need not track it elsewhere.

Records that resolved (see §0 of `variant-catalog.md` for what "resolved" means here):

| Work | Record | Why it is the one to cite |
| :--- | :--- | :--- |
| Martin et al. 2019, *Nat Genet* — clinical use of current scores may exacerbate disparities | [PMC6563838](https://pmc.ncbi.nlm.nih.gov/articles/PMC6563838/); preprint [bioRxiv 10.1101/441261](https://www.biorxiv.org/content/10.1101/441261) | The statement of the problem |
| Martin et al. 2017, *AJHG* — demographic history impacts risk prediction | [PMC5384097](https://pmc.ncbi.nlm.nih.gov/articles/PMC5384097/) | The mechanism, from population history |
| Privé et al. 2022, *AJHG* — portability of 245 scores across 9 ancestry groups | [PMC8764121](https://pmc.ncbi.nlm.nih.gov/articles/PMC8764121/), correction [PMC8874215](https://pmc.ncbi.nlm.nih.gov/articles/PMC8874215/) | **Strongest design:** training and testing inside one cohort, which removes environmental and genotyping confounding |
| Ding et al. 2023, *Nature* — accuracy varies across the genetic ancestry continuum | **Named, not cited with a verified identifier.** Its DOI appeared in prose and inside an aggregator URL rather than inside a returned publisher URL, so by `variant-catalog.md` §0's own rule it does not ship as a citation | The decline is **continuous along genetic distance, not stepwise between labelled groups — so it is present within a single labelled ancestry** |
| Duncan et al. 2019, *Nat Commun* — usage and performance across diverse populations | **Named, not cited with a verified identifier**, for the same reason | A census of the literature: the great majority of polygenic-scoring studies were exclusively European-ancestry *(figure from the abstract)* |

**What portability does to the person's number**, propagated through the table above. The retained
fraction is a **sensitivity sweep chosen to show the shape** — not a published multiplier, because
the real degradation is trait- and ancestry-specific and no single number is defensible:

```
 variance retained   AUC    top decile   multiple   top-vs-bottom OR
   100% (R2 0.050)   0.62      18.2%       1.8x           4.88
    75% (R2 0.038)   0.61      16.9%       1.7x           3.90
    50% (R2 0.025)   0.59      15.5%       1.6x           3.01
    25% (R2 0.013)   0.56      13.8%       1.4x           2.16
```

The degradation is undramatic in AUC and decisive in interpretation: a score that was weak
stratification in the population it was built in becomes nearly uninformative elsewhere, while the
report it generates looks exactly the same.

**Cite the dispute, not one side.** The transferability gap is real, well documented and actively
argued over in magnitude and in consequence. Prefer characterising that disagreement to anchoring it
on a single preprint — and note that the Privé correction above is the concrete demonstration that
these analyses themselves get revised, which is the honest reason to quote direction rather than a
decimal.

**What a PRS can honestly be used for:** population-level stratification, research, and — with
ancestry-matched derivation — modest risk refinement alongside conventional risk factors.
**What it cannot:** give an individual a trustworthy personal number when derived in a population
they do not belong to. A score that discriminates well at population level can still be close to
uninformative for one person, because population discrimination and individual precision are
different quantities.

**Single GWAS hits are weaker still, and the arithmetic is worth carrying.** Under a multiplicative
odds model calibrated so the genotype-weighted mean risk equals a 10% prevalence exactly, with a
risk-allele frequency of 0.30:

```
 per-allele OR   risk at 0/1/2 copies      one copy   two copies   AUC of that SNP alone
     1.05        9.74 / 10.17 / 10.63%     +0.44 pp    +0.89 pp          0.508
     1.10        9.48 / 10.33 / 11.25%     +0.85 pp    +1.77 pp          0.516
     1.20        9.01 / 10.62 / 12.48%     +1.61 pp    +3.47 pp          0.531
     1.50        7.81 / 11.27 / 16.01%     +3.46 pp    +8.20 pp          0.570
```

A typical hit (OR ≈ 1.10) moves one carrier from roughly **95 in 1,000 to roughly 103 in 1,000**,
and even a strong common-variant hit leaves an individual predictor under AUC 0.57. Reporting one
as personal information is the genetic equivalent of reporting a coin flip as a forecast.

## §5 Negative results and what a panel did not probe

**A negative consumer result is weak reassurance**, and quantifying how weak is more honest than
hedging. For a panel probing a subset of causal alleles, the post-negative carrier probability is:

```
P(carrier | negative) = p·(1 − c) / (1 − p·c)
```

where `p` is the pre-test carrier probability and `c` the fraction of causal alleles probed. With
`p = 1/400` and 70% coverage:

```
 pre-test carrier probability    0.250%
 post-negative probability       0.075%
 relative reduction              69.9%  — reduced, NOT eliminated
```

**70% coverage flatters the case, and the realistic consumer figure is starker.** A consumer panel
probing selected variants rather than sequencing the gene may detect a small minority of carriers
outside a founder population. At the same pre-test probability:

```
 c = 70%   post-negative 0.075%   reduction 69.9%
 c = 30%   post-negative 0.175%   reduction 29.9%
 c = 10%   post-negative 0.225%   reduction 10.0%
```

At 10% coverage the negative has moved the question by a tenth. **The reduction equals the coverage
almost exactly** at these small pre-test probabilities — which is the clearest way to say it: *a
negative result is worth exactly what the panel's coverage is worth, and nothing more.*

Coverage dominates the result, and for many conditions it is far below 70% on a consumer array.
**Never report "no variants detected" without stating what was probed**, and never let it stand as
clearance for a condition the person has a family history of.

**And do not report NPV for a rare variant.** Negative predictive value is near 100% for anything
rare whatever the test does — it is dominated by the prior, so it reads as reassurance and carries
almost no information. **Report the negative likelihood ratio** — `(1 − sensitivity) / specificity` —
**and the post-test odds**, which say how much the negative actually moved the question. The same
caution applies to the HLA-proxy NPV column in `pharmacogenomics.md` §2: it is high because the
allele is uncommon, not because the proxy is good.

**`c` is clinical sensitivity, not a count of alleles — and conflating the two breaks the formula in
both directions.** `c` must be *the fraction of carriers in this person's ancestry whose variant the
panel probes*, not the fraction of distinct causal alleles probed. Those two quantities differ by
orders of magnitude in exactly the case this skill is about: a consumer panel probing three BRCA1/2
founder variants covers a negligible fraction of known pathogenic alleles, yet detects the large
majority of carriers **in the founder population** and a small minority outside it. So:

- plug in the **allele-count** fraction and the post-negative probability barely moves — overstating
  residual risk, which at least errs safe;
- plug in a **founder panel's headline sensitivity** for someone outside that population and the
  number is falsely reassuring, which does not.

**The error is ancestry-dependent, so state the ancestry with the figure.**

**And there is a second assumption, which errs the other way — so the two do not cancel.** The
formula also assumes the panel **never misses an allele it does probe** and **never miscalls a
non-carrier**: perfect analytic sensitivity on the probed set, perfect specificity. On a consumer
array none of that holds — no-calls, low-confidence calls, strand-ambiguous sites and plain
genotyping error all produce a negative in a true carrier. Every one of those pushes the true
residual probability **up**, while the mass-versus-list approximation pushes the reported figure up
too. **So the output is a floor, not a bound.** Where the panel reports an analytic sensitivity, use
it in `c`. "Coverage dominates" is the honest version of "coverage is the whole story".

### The number a reproductive decision actually turns on is the couple's, not the person's

An individual carrier result is the wrong quantity. The decision-relevant figure is
P(affected child), which needs **both** partners. Worked for a recessive condition with carrier
frequency 1/25 and a 1-in-4 transmission risk when both are carriers:

```
 neither partner tested                                    0.0400%   (1 in 2,500)
 person is a known carrier, partner untested               1.0000%   (1 in 100)
 person carrier, partner NEGATIVE at 95% detection         0.0520%   (1 in 1,924)   -94.8%
 person carrier, partner NEGATIVE at 60% detection         0.4098%   (1 in 244)     -59.0%
```

**"My partner tested negative" is not one fact.** Its entire value is the detection rate of that
panel *for that gene* — the residual risk after the weaker test is **7.9× higher** than after the
stronger one. A consumer array probes selected variants rather than sequencing the gene, so its
detection rate for most recessive conditions is unknown-to-low. **A reproductive decision needs
clinical-grade carrier screening.** The professional instrument is a **tiered carrier-screening
framework** that sets which conditions should be offered by carrier frequency — but no record for it
resolved in this environment, and an earlier version of this paragraph promised a name in place of an
identifier and then supplied neither. **So the followable instruction is the one to give: ask a
genetic counsellor or the ordering clinician which tier of carrier screening applies, and what the
panel's detection rate is for this person's ancestry.** That question is answerable; a framework
name quoted from memory is not.

---

## §6 The reporting template

Use this for every quantitative genetic finding. All five elements, in this order.

> **[Finding].** Among people [matched on the relevant axes — ancestry, sex, age] **who do not carry
> this variant**, roughly **[baseline] in 1,000** develop [outcome] by age [X]. With this genotype that figure is about
> **[carrier] in 1,000** — a difference of **[n] per 1,000 people**, or **[pp] percentage points**.
> In relative terms that is **[RR/OR][, reported as an odds ratio from a case-control design]**.
> The estimate comes from **[population-based / family-informed]** data in **[ancestry]** cohorts
> and carries **[interval]**; [state the portability caveat if the person's ancestry differs].
> The call itself is **[array-reliability grade]** and is **[unconfirmed consumer raw data /
> clinically confirmed]**.
> **What follows from it: [confirm the genotype first, then the specific action — or "nothing
> changes"].**

**Worked, using the rare-outcome column from §2:**

> Among people matched on ancestry, sex and age who do not carry this variant, roughly **5 in 1,000**
> develop this outcome by age 80. With this genotype it is about **15 in 1,000** — **10 more people per 1,000**, or **1.0
> percentage point**. In relative terms, three times the baseline. The estimate is population-based
> in European-ancestry cohorts with a wide interval. The call is a directly-probed common variant
> (R1) and is **unconfirmed consumer raw data**. **What follows: confirm the genotype in a clinical
> laboratory, and if confirmed, one screening conversation with a clinician — and no change to
> anything else.**

**Four rules the template enforces:**
- **The confirmation status travels with the number.** A template that can emit a genotype, an
  absolute risk and an action without stating that the call is an unconfirmed array probe defeats the
  skill's own hard rail, and this one could until a review caught it.
- **Natural frequencies before percentages.** Counts of people, never percentages of percentages.
- **No composite "genetic risk score" across findings.** Conditions have independent baselines and
  independent evidence quality; a single number summarising them is uninterpretable, and averaging
  independent axes is a defect this library has already measured elsewhere.
- **End on the action, or on its absence.** A risk number with no attached decision is alarm without
  information, and "nothing changes" is a complete and frequently correct ending.

### Carrying the interval through the conversion

The template demands an interval, and the conversion is where intervals get dropped. **Multiply the
baseline by each confidence limit**, then report the absolute range:

```
 baseline            5 per 1,000
 reported RR         3.0  (95% CI 1.8 to 5.1)
 absolute risk      15 per 1,000   (95% CI  9 to 26)
 extra cases        10 per 1,000   (95% CI  4 to 21)
```

**A five-fold span on the extra cases is the finding**, and it is invisible if only the point
estimate survives the conversion. Where the source reports an interval that wide — and penetrance
estimates off a handful of carriers routinely do — **the interval is the headline and the point
estimate is decoration.**

### Two findings bearing on the same outcome

The ban on composite scores leaves a real case open, so state the substitute. When two findings bear
on **the same** outcome, the correct output is **one combined absolute estimate from a model that
included both**, not two relative multiples side by side — a reader will multiply them, and that is
usually wrong.

**If no joint estimate exists, do not build one.** Multiplying two relative figures assumes the
effects are independent *and* that the variants are not in linkage disequilibrium with each other;
when they are correlated the product double-counts the same signal. Report them separately, say they
bear on the same outcome, and say explicitly that they cannot be combined from the data in hand.
That is a complete answer, and it is more useful than a number that cannot be defended.
