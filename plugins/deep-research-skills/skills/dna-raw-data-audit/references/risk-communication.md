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
| Number needed to harm | 101 | 5 |

Identical headline. One is a rounding error in a life; the other reorganises it. **Reporting "triples
your risk" without the baseline makes those two indistinguishable**, which is why this skill treats
the omission as a defect rather than a simplification.

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
3. **Quote a range, not a point.** Any single penetrance figure presented as *the* number is
   overstating what the literature supports.
4. **Report which kind of estimate you used and why.**

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

**Polygenic risk scores** are the acute case. Scores built predominantly from European-ancestry GWAS
transfer poorly to other ancestries — the mechanism is a compound of linkage-disequilibrium
structure differences, allele-frequency differences, and the fact that the tagged SNP is usually not
the causal one, so a tag that works in one population may not track the causal variant in another.
Resolvable records: the originating preprint
([bioRxiv 10.1101/441261](https://www.biorxiv.org/content/10.1101/441261.full.pdf)) and subsequent
portability work ([PMID 39218908](https://pubmed.ncbi.nlm.nih.gov/39218908/)).

**Cite the dispute, not one side.** At least one analysis argues the fairness consequence is smaller
than claimed for a specific application
([medRxiv](https://www.medrxiv.org/content/10.1101/2025.09.18.25336069.full.pdf)). The honest summary
is that the transferability gap is real and well documented, and its magnitude and consequences are
actively argued.

**What a PRS can honestly be used for:** population-level stratification, research, and — with
ancestry-matched derivation — modest risk refinement alongside conventional risk factors.
**What it cannot:** give an individual a trustworthy personal number when derived in a population
they do not belong to. A score that discriminates well at population level (a respectable AUC) can
still be close to uninformative for one person, because population discrimination and individual
precision are different quantities.

**Single GWAS hits are weaker still.** A per-allele odds ratio near 1 tells an individual almost
nothing; the variance explained by one common variant is typically a fraction of a percent. Reporting
one as personal information is the genetic equivalent of reporting a coin flip as a forecast.

---

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
