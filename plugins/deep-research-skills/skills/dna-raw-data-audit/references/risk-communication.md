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

**The same multiple, two baselines** (RR 3.0 throughout):

| | Rare outcome | Common outcome |
| :--- | ---: | ---: |
| Baseline absolute risk | 0.5% | 12.0% |
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

### Case-control designs report odds ratios, and genetic studies are full of them

Much genetic association data comes from case-control designs, which yield **odds ratios**, not risk
ratios. An OR read as an RR always overstates. Converting at a known baseline p₀:

```
RR = OR / (1 − p₀ + p₀·OR)
```

For **OR = 2.0** this simplifies to `RR = 2/(1 + p₀)`, so the relative overstatement from misreading
it equals the baseline risk exactly:

| Baseline | True RR at OR 2.0 | Overstatement from reading OR as RR |
| ---: | ---: | ---: |
| 1% | 1.980 | 1.0% |
| 10% | 1.818 | 10.0% |
| 30% | 1.538 | 30.0% |

Safe to approximate when the outcome is rare; degrades exactly as fast as the baseline rises.
**Always check which measure the source reported** — a paper saying "OR" and a report saying "times
the risk" are not the same claim.

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
([PMID 25192939](https://pubmed.ncbi.nlm.nih.gov/25192939)). There is also more variation *between
families carrying the same variant* than between positions within a gene
([PMID 16484695](https://pubmed.ncbi.nlm.nih.gov/16484695)).

So the rule is **not** "family-based estimates are inflated, discount them". It is:

1. **Use population-based estimates for a person tested without family history** — that is their
   situation, and it is the consumer-genomics situation by definition.
2. **Use family-informed estimates when there is a family history**, because then the family burden
   is real information.
3. **Never quote only one figure, in either direction.** This cuts both ways, and the second
   direction is the one usually missed: quoting only the *population* figure to someone who **does**
   have a strong family history **under-warns them**, and that is its own safety failure. Family-based
   estimates have run materially above population-based ones for the same gene, so the gap is large
   enough for the choice to matter clinically.
4. **Quote a range, not a point.** Any single penetrance figure presented as *the* number is
   overstating what the literature supports.
5. **Report which kind of estimate you used and why** — and, where family history is unknown, report
   both and say which applies under which assumption rather than silently picking.

### Age-conditioning: the birth figure overstates for anyone past young adulthood

Lifetime risk quoted "from birth" includes years the person has already passed without the outcome.
Illustrative, with hazard distributed across decades summing to a 12.0% lifetime risk:

```
 lifetime risk from birth          12.0%
 remaining risk from age 50        10.5%
 quoting the birth figure to a 50-year-old overstates remaining risk by 14.3% (relative)
```

The gap widens sharply with age and with conditions whose incidence is front-loaded. **Always
age-condition when the literature provides the data, and say so when it does not.**

---

## §4 Ancestry portability and polygenic scores

**Establish ancestry before quoting any population estimate.** This determines whether a number
means anything for this person, and it is not a caveat to append at the end.

### Lead with the absolute number, not the AUC

AUC is the figure that gets published, and the one that sounds impressive. It is the wrong headline
for a person, because **AUC is invariant to prevalence and the question is not.** The same score,
the same person:

```
 score explaining 5% of liability variance, top decile flagged
   outcome affecting 1 in 10     baseline 10.0%  ->  top decile 18.2%   (1.8x)
   outcome affecting 1 in 100    baseline  1.0%  ->  top decile  2.4%   (2.4x)
```

Identical discrimination. The *multiple* is larger in the second case while the absolute risk is a
seventh of it — which is exactly why the multiple is the wrong thing to lead with.

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

**So a claim of the form "the top 8% of people are at threefold risk" is a statement about an
extreme tail, not about the score's accuracy for the person in front of you.** The same score, for
the same person, can support "three times the average" while explaining a modest share of total
liability. Ask which cutpoint produced the multiple before repeating it.

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
| Ding et al. 2023, *Nature* — accuracy varies across the genetic ancestry continuum | [10.1038/s41586-023-06079-4](https://doi.org/10.1038/s41586-023-06079-4) | The decline is **continuous along genetic distance, not stepwise between labelled groups — so it is present within a single labelled ancestry** |
| Duncan et al. 2019, *Nat Commun* — usage and performance across diverse populations | [10.1038/s41467-019-11112-0](https://doi.org/10.1038/s41467-019-11112-0) | A census of the literature: the great majority of polygenic-scoring studies were exclusively European-ancestry *(figure from the abstract, not re-resolved to a retrieved record)* |

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

Coverage is the whole story, and for many conditions it is far below 70% on a consumer array.
**Never report "no variants detected" without stating what was probed**, and never let it stand as
clearance for a condition the person has a family history of.

**One assumption inside that formula, which has to be stated when the formula is used.** It is exact
only if `c` is the fraction of carrier *probability mass* probed, not the fraction of the *allele
list*. Panels probe the commonest alleles first, so mass-coverage exceeds list-coverage — which
means using a list-coverage figure for `c` **overstates** the residual risk. That direction is
conservative and therefore acceptable, but say which quantity you used, because the two can differ
by a lot for a gene with one dominant allele and a long tail.

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
clinical-grade carrier screening**, and the tiered professional carrier-screening framework (named,
not cited with a reconstructed identifier — no record for it resolved in this environment) is the
instrument to point at.

---

## §6 The reporting template

Use this for every quantitative genetic finding. All five elements, in this order.

> **[Finding].** Among people [matched on the relevant axes — ancestry, sex, age], roughly
> **[baseline] in 1,000** develop [outcome] by age [X]. With this genotype that figure is about
> **[carrier] in 1,000** — a difference of **[n] per 1,000 people**, or **[pp] percentage points**.
> In relative terms that is **[RR/OR][, reported as an odds ratio from a case-control design]**.
> The estimate comes from **[population-based / family-informed]** data in **[ancestry]** cohorts
> and carries **[interval]**; [state the portability caveat if the person's ancestry differs].
> **What follows from it: [specific action, or "nothing changes"].**

**Worked, using the rare-outcome column from §2:**

> Among people matched on ancestry, sex and age, roughly **5 in 1,000** develop this outcome by age
> 80. With this genotype it is about **15 in 1,000** — **10 more people per 1,000**, or **1.0
> percentage point**. In relative terms, three times the baseline. The estimate is population-based
> in European-ancestry cohorts with a wide interval. **What follows: one screening conversation with
> a clinician — and no change to anything else.**

**Three rules the template enforces:**
- **Natural frequencies before percentages.** Counts of people, never percentages of percentages.
- **No composite "genetic risk score" across findings.** Conditions have independent baselines and
  independent evidence quality; a single number summarising them is uninterpretable, and averaging
  independent axes is a defect this library has already measured elsewhere.
- **End on the action, or on its absence.** A risk number with no attached decision is alarm without
  information, and "nothing changes" is a complete and frequently correct ending.
