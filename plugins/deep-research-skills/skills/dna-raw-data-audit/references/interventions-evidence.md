# Interventions: medicines, supplements, peptides, lifestyle

How to grade anything the skill might discuss, and the rails that keep a genetics tool from becoming
a storefront.

**Contents**
- §1 The grading frame, applied to everything
- §2 The rail: genotype does not justify an intervention by itself
- §3 Medicines
- §4 Supplements and the nutrigenomics correction
- §5 Peptides
- §6 Lifestyle factors, which is where the evidence actually is
- §7 What to hand a clinician

---

## §1 The grading frame, applied to everything

Grade every intervention on **three independent axes** and report all three. Collapsing them is how
a preclinical finding becomes a protocol.

**Regulatory status** — jurisdiction-specific and it *moves*:
- **Approved**, with the indication named.
- **Approved, different indication** — off-label use is legitimate medicine but a different
  evidence question.
- **Compounded** — made by a pharmacy, not an approved manufactured product.
- **Unapproved / research-only** — includes material sold as "research chemical" or "not for human
  consumption".
- **Flagged by a regulator** — e.g. placed in a category identifying significant safety risks for
  compounding.

**Evidence tier** — what has actually been shown:
- **T1** Adequately powered randomised trials with **hard outcomes** (death, events, function).
- **T2** Randomised trials with **surrogate** outcomes only (a biomarker moved).
- **T3** Open-label, observational, or underpowered randomised work.
- **T4** Animal studies.
- **T5** In vitro.
- **T6** Mechanism or anecdote.

**Genetic evidence** — the axis this skill exists to assess:
- **G1** A gene–intervention interaction with guideline-level support (this is essentially
  pharmacogenomics and almost nothing else).
- **G2** An interaction reported and replicated, no guideline.
- **G3** An association with the *outcome* but no evidence the genotype modifies the *response*.
- **G4** None.

**The distinction between G3 and G2 is the one that matters most and the one marketing erases.**
A variant that predicts an outcome but does not modify the response to any intervention is **not
actionable**, however real the association. "Your FTO genotype is associated with higher BMI" is G3;
it does not tell you to do anything different, and the published work suggests it does not blunt
response to lifestyle change either — so the advice is unchanged.

**Never state a regulatory status as a fixed fact.** Name the mechanism and the source, and say it
must be re-checked. This is not pedantry: while building this file, one peptide's regulatory posture
demonstrably shifted across a span of a few years, and a nomination status changed again later.
Anything frozen here would be wrong by the time someone read it.

---

## §2 The rail: genotype does not justify an intervention by itself

**Two conditions must both hold before a genotype supports an intervention:**

1. An intervention exists, with evidence at **T1 or T2**.
2. That intervention has been shown to change the outcome **in carriers specifically** — i.e. the
   genetic evidence is **G1 or G2**, not G3.

Nearly nothing clears both. The honest consequence:

- **For peptides the genetic evidence is G4 for nearly all of them — and the rail must rest on
  non-actionability, not on absence of evidence**, because "none at all" is overstated and a single
  counterexample would otherwise appear to break it. The counterexample is real: **GLP1R rs6923761**
  has reported, partially replicated gene–response data including pre-specified analyses within
  randomised trials ([PMC6003833](https://pmc.ncbi.nlm.nih.gov/articles/PMC6003833),
  [PMC9335902](https://pmc.ncbi.nlm.nih.gov/articles/PMC9335902/)). The findings are small,
  inconsistent in direction across endpoints — better weight response in carriers in some analyses,
  *worse* metabolic response in others — and nowhere near a guideline, so it grades **G2 at best and
  is not clinically usable.** That is the honest shape: **evidence exists and still does not select
  the drug.** A genotype therefore supplies no basis for recommending any peptide, which is what the
  rail needs. This is what prevents the skill's most likely failure mode — becoming a
  genotype-flavoured supplement and peptide storefront, which is what most of this market is.
- **For supplements, it is G3 or G4 with narrow exceptions** (§4).
- **For medicines, pharmacogenomics is the real G1 answer** (§3), and it routes to a prescriber.

When a person asks "what should I take based on my DNA?", the accurate answer for almost every
genotype is: *nothing, on that basis.* Say it, then give them what the data *does* support — usually
a phenotype measurement to request, or a flag to raise with a prescriber.

---

## §3 Medicines

**Pharmacogenomics is the legitimate intersection**, and `pharmacogenomics.md` owns it. The short
version for this file:

- Gene–drug pairs with guideline-level support are **G1** — the only intervention class in this
  entire file that reaches it.
- The action is **never** "change your dose". It is: raise the flag with the prescriber, who can
  order a clinical-grade pharmacogenomic panel and act on a validated result.
- A raw-data pharmacogenomic finding is a **prompt for a test**, not a test result (see the
  false-positive anchor in `variant-catalog.md` §0).
- **Never advise stopping, starting, or changing a prescribed medication.** That includes a
  medication the data appears to flag — especially then, because stopping abruptly carries its own
  risk, and the person's prescriber holds context the genome does not contain.

**No doses, for anything, ever.** Dosing integrates renal and hepatic function, interactions,
indication, age, weight, and goals. A genome contains none of that.

---

## §4 Supplements and the nutrigenomics correction

**Lead with the trial that settles the general question, because it is stronger than any
variant-by-variant argument.** Food4Me was an internet-delivered randomised trial across seven
European countries (1,269 completers) with four arms: conventional advice, personalised on diet
alone, diet plus **phenotype** (anthropometry and blood biomarkers), and diet plus phenotype plus
**genotype** (five diet-responsive variants)
([PMID 27524815](https://pubmed.ncbi.nlm.nih.gov/27524815/),
[10.1093/ije/dyw186](https://doi.org/10.1093/ije/dyw186)). The personalised arms did change
behaviour — less red meat, salt and saturated fat — **and the trial reported no evidence that adding
phenotypic, or phenotypic plus genotypic, information enhanced that effect** *(the conclusion is read
from the abstract; the identifier is record-verified)*.

**That is the finding to lead with: in a real randomised personalised-nutrition intervention, the
genotype layer added nothing on top of phenotype.** So "the recommendation does not change based on
this genotype" is not this skill's caution — it is the trial result.

**And the structural reason a commercial panel always has something to tell you is arithmetic, not
argument.** At an uncorrected α = 0.05 across a candidate panel:

```
   5 SNPs   expected spurious hits 0.25   P(at least one) 22.6%
  20 SNPs                          1.00                   64.2%
  38 SNPs                          1.90                   85.8%
  70 SNPs                          3.50                   97.2%
 100 SNPs                          5.00                   99.4%
```

A panel of the size these products typically report will find something to say about **roughly two
of its variants by chance even if none of them does anything.** No debunking citation is needed; the
probability is the argument, and it is why "your report found three actionable variants" is the
expected outcome of testing many.

**Then the MTHFR correction**, because it is the field's emblematic case and getting it right
is a good test of whether a tool is trustworthy. A professional-society practice guideline advised
against routine MTHFR polymorphism testing on minimal-clinical-utility grounds
([PMID 23288205](https://pubmed.ncbi.nlm.nih.gov/23288205)), later amended
([PMID 32587351](https://pubmed.ncbi.nlm.nih.gov/32587351)) with the recommendation against testing
standing through the amendment; multiple other professional bodies concur
([PMC9175241](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175241/)), and the clinical-utility question
has been revisited ([PMC11288266](https://pmc.ncbi.nlm.nih.gov/articles/PMC11288266/)).

**The causal loop the MTHFR story depends on is also closed at the other end.** The story runs
*variant → higher homocysteine → cardiovascular risk → so lower homocysteine*. But the
homocysteine-lowering trials, pooled, did not reduce cardiovascular events
([PMID 21069462](https://pubmed.ncbi.nlm.nih.gov/21069462/)) — B-vitamin allocation moved the
biomarker and not the outcome. **So even granting every step of the mechanism, the intervention it
implies has been tested and does not work**, which is a stronger objection than disputing the
genotype's effect size. *(The pooled figures are prose-sourced; the review's identifier is
record-verified.)*

The methylfolate-protocol industry built on MTHFR is **G3 at best and largely G4**. If a person
arrives already taking a stack because of an MTHFR result, the useful service is the correction —
delivered without contempt, because they were sold this by people who sounded authoritative.

**The narrow set with genuine substance**, and note how modest it is:

| Genotype | What it supports | Grade |
| :--- | :--- | :--- |
| **HFE** C282Y homozygous (confirmed) | Changes iron advice in the *opposite* direction to the default — avoid iron supplementation, and get iron studies. One of the few places a genotype genuinely redirects a supplement decision | G2 / T1 |
| **G6PD** deficiency (confirmed) | A real avoidance list — specific drugs, and fava beans. Avoidance, not supplementation | G1 / T1 |
| **ALDH2** rs671 | Strengthens the case for reducing alcohol. No supplement addresses it | G3 / T1 for the behaviour |
| **MCM6/LCT** rs4988235 | Explains lactose intolerance — **in European ancestry only.** This variant tags the European lactase-persistence haplotype; independent persistence alleles exist elsewhere, so a "non-persistent" call outside that ancestry is frequently a **false negative**. Dietary choice follows symptoms, which the person already knows | G2 / T2 |
| **Celiac HLA-DQ2/DQ8** | **A rule-out and nothing else, and the asymmetry is arithmetic.** At 1% prevalence with 30–40% population carriage, NPV stays above 99.9% while PPV never exceeds about 3.5% — so a negative makes coeliac disease very unlikely and a positive says almost nothing, because up to 40% of everyone carries it. Two cautions: sensitivity is high but **not** 100%, so do not promise a perfect rule-out, and the test cannot be interpreted at all after a gluten-free diet has already started | G2 / T2, as a rule-out |
| **FUT2** secretor status | **Flips the usual story: it changes the MEASUREMENT, not the requirement.** Non-secretors run different serum B12 levels for the same intake, so the variant is a reason to interpret a *lab value* differently rather than to supplement. That makes it one of the few panel variants with a genuine use — and the use is on the test, not the person | G2 / T2 for interpretation |
| **Confirmed deficiency on a blood test** | The actual basis for supplementing — and it is a *measurement*, not a genotype | — / T1–T2 |

**The pattern worth stating plainly: measure, don't infer.** Serum 25-OH-D beats any vitamin D
pathway genotype — and note *why*: the vitamin D pathway variants explain part of someone's
**baseline** 25(OH)D, not their **response to supplementation**, which is the quantity a
supplementation decision needs. A variant that predicts where you start and not where you end up is
a G3 finding however well replicated it is. Ferritin and transferrin saturation beat HFE. A B12 level beats an MTHFR result.
Where a cheap decisive phenotype test exists, the genotype's only real value is prompting it.

**Where the general recommendation does not change based on genotype — the common case — say so.**
That is the correct answer, and the one the industry suppresses because it sells nothing.

---

## §5 Peptides

The owner asked for this explicitly, so it gets a real assessment rather than a refusal. The
assessment is structural: **grade the class, name what is actually established, and apply §2.**

**The GLP-1 contrast case, first, because it calibrates everything else.** GLP-1 receptor agonists
are approved medicines with large randomised trials — **T1, approved**. That is what real evidence
for a peptide looks like, and every class below should be read against it; the gap is large.

**But do not lump them, because their outcome evidence is not the same.** Semaglutide has a
placebo-controlled cardiovascular-outcome trial reporting superiority on major adverse cardiovascular
events; tirzepatide, at the time of writing, does not have an equivalent completed outcome trial.
Both are approved and both are T1 for their licensed indications, **and only one of them supports a
cardiovascular-benefit claim.** Check each drug's own outcome evidence rather than inheriting it from
the class — this is the same error as inheriting a guideline across a gene–drug pair.

Their genetic evidence is **G2 at best and not usable** (§2): a genotype does not select them.

**Growth-hormone secretagogues and GHRH analogues** — ipamorelin, CJC-1295, sermorelin, tesamorelin,
and MK-677 (frequently sold alongside peptides but not itself a peptide). Evidence for the commonly
marketed uses is **T3–T6**, and concerns centre on sustained IGF-1 elevation. **G4.**

**This class spans three different regulatory categories, and collapsing them is a real error:** a
product with a *narrow approved indication* (tesamorelin), a product that was approved historically
and is **no longer marketed** in some jurisdictions, and compounds **never approved for human use at
all**. "Peptide" is not a regulatory category. Establish each one's current status at source.

**MK-677 is the strongest concrete case in the class, and it argues against use.** A two-year
randomised, double-blind trial in healthy older adults exists
([PMC2757071](https://pmc.ncbi.nlm.nih.gov/articles/PMC2757071/)) — which already puts it above most
of this market on evidence *availability*. What it found is the point: fat-free mass rose, **hard
functional outcomes were not demonstrated, and glucose handling worsened.** So the best-studied
member of the class moved a surrogate (T2) while raising a metabolic concern, and the honest reading
is a negative one. *The specific effect sizes are not quoted here: they appeared only in secondary
summaries that disagreed with each other, and the primary record was not retrievable in this
environment — read them from the paper.*

**BPC-157.** Marketed heavily; evidence overwhelmingly preclinical (**T4–T5**) — one systematic
review of the literature included 36 studies of which **35 were preclinical and 1 clinical**, a ratio
that describes the field better than any adjective. *(That count is read from a review's own text
rather than from a retrieved primary record — treat it as an anchor to re-verify, per
`variant-catalog.md` §0.)* It has been placed
by a regulator in a category identifying substances that **may present significant safety risks**
for use in compounding, with concerns including immunogenicity for certain routes of administration
and peptide-impurity characterisation
([FDA bulk-substances safety-risk page](https://www.fda.gov/drugs/human-drug-compounding/certain-bulk-drug-substances-use-compounding-may-present-significant-safety-risks);
reviews at [PMC12313605](https://pmc.ncbi.nlm.nih.gov/articles/PMC12313605/) and
[PMC12446177](https://pmc.ncbi.nlm.nih.gov/articles/PMC12446177/)). **The specific category and
nomination status have changed over time — re-check the live source rather than quoting this
paragraph.** **G4.**

**TB-500/thymosin beta-4, thymosin alpha-1, epitalon, GHK-Cu, and similar** — assess as a class:
individual human evidence is thin (**T4–T6**), with occasional narrow exceptions worth checking
individually rather than assuming. **G4.**

**Melanotan I/II — and PT-141, which is a different situation entirely.** Both are melanocortin
agonists, and shipping them as one line was an error worth naming.

**Melanotan I/II** carries a specific, concrete concern about naevi that distinguishes it from the
"unproven but probably inert" category: published case reports describe **eruptive naevi and
darkening of pre-existing naevi after use**, in one report within 24 hours of a single injection
([PMC3663356](https://pmc.ncbi.nlm.nih.gov/articles/PMC3663356);
[10.2340/00015555-1130](https://medicaljournals.se/acta/download/10.2340/00015555-1130)). **State
what this evidence is and is not:** case reports establish temporal association, not causation — a
melanoma report in this literature explicitly declined to claim a causal relationship. The honest
version is that a drug which drives melanogenesis in people who are also tanning, with documented
naevus changes, warrants dermatological review rather than reassurance. **T6 on efficacy for the
marketed use, with a named safety signal. G4.**

**PT-141 is bremelanotide, and it is an approved drug** — marketed as Vyleesi for a narrow
indication (acquired, generalised hypoactive sexual desire disorder in premenopausal women), with
randomised placebo-controlled trials behind it
([PMID 31893927](https://pubmed.ncbi.nlm.nih.gov/31893927/), whose title records the approval;
[PMID 27181790](https://pubmed.ncbi.nlm.nih.gov/27181790/) dose-finding RCT;
[PMID 31599847](https://pubmed.ncbi.nlm.nih.gov/31599847/) long-term extension;
[PMC6819021](https://pmc.ncbi.nlm.nih.gov/articles/PMC6819021/) /
[PMC6819023](https://pmc.ncbi.nlm.nih.gov/articles/PMC6819023/) phase 3). So it is **T1/T2 for its
licensed indication, approved** — not a grey-market unknown, and an earlier version of this file
misclassified it. **Two things follow, and the second is the one that matters:** the licensed
indication is narrow and the published effect sizes are modest, and **material sold online as
"PT-141" is not the approved product** — it is the same molecule name attached to an unregulated
supply chain, which is a §5 product-integrity problem rather than an efficacy question. **G4.**

**Three risks that are independent of whether any molecule works**, and which the marketing never
addresses:
1. **Product integrity.** Grey-market injectables carry contamination, mislabelling, dosing-error
   and sterility risk. Review literature on unregulated injectable peptide use documents real harm
   ([PMC13585006](https://pmc.ncbi.nlm.nih.gov/articles/PMC13585006)).
2. **Sport prohibition, and there are TWO mechanisms, not one.** Peptide hormones, growth factors
   and related substances sit in their own prohibited class, with growth-hormone releasing factors
   prohibited at all times. **But the catch-all is the one that sweeps in most of this market:** a
   separate class covers **substances not approved by any governmental regulatory health authority
   for human therapeutic use** — which is precisely what a research-only or grey-market peptide is,
   whatever its pharmacology. So "it isn't on the named-substance list" is not a defence. **Name both
   mechanisms and send an athlete to the current published list** — the list is versioned and the
   edition in force changes.
3. **Unknown interactions** with prescribed medication, which nobody is monitoring in a self-sourced
   protocol.
4. **A hazard in the research step itself, which is this skill's own exposure.** For grey-market
   peptides the searchable literature is **outnumbered by vendor content** — clinic pages, supplement
   wikis and seller "research" write-ups that imitate the form of evidence and are what a search
   returns first. Three consequences, all of which bit while this file was being verified: a search
   summary can be built almost entirely from commercial sources; the same figure appears in several
   vendor pages with different values, creating false corroboration; and the primary regulatory
   sources that would settle it are often unreachable. **So for this class, restrict the search to
   index and publisher domains, treat a vendor page as zero evidence rather than weak evidence, and
   report "no retrievable primary source" as the finding** — which is usually the true answer and is
   more useful than a laundered one.

**What the skill does with a peptide question.** Explain the grading, state the evidence honestly,
name the safety and regulatory considerations, and say clearly that **the genome contributes nothing
to the decision** — because that is the accurate answer and it is the one thing a genetics tool is
uniquely positioned to say. Then route the actual decision to a clinician who can see the whole
person. **No doses. No sourcing. No protocols.**

Being vague would fail the owner, who asked for substance. Being a storefront would fail them worse.

---

## §6 Lifestyle factors, which is where the evidence actually is

Worth stating because it is the honest anchor for almost every report: the interventions with the
strongest outcome evidence are **not genotype-tailored**, and they dominate anything a consumer
genome will suggest.

Physical activity including resistance training, sleep duration and regularity, alcohol reduction,
smoking cessation, and dietary pattern all sit at **T1 for hard outcomes** and apply **regardless of
genotype**. `coding-agent-skills:fitness-nutrition-science` owns the training and nutrition detail;
this skill's job is to avoid implying that a genotype-tailored variation on them is better supported
than the baseline, because it is not.

**The useful framing for a report:** the genome may sharpen *one or two* decisions — a test to
request, a drug class to flag, an avoidance list. It does not reorganise the fundamentals, and a
report implying otherwise has inverted the evidence.

---

## §7 What to hand a clinician

The most actionable artifact this skill produces is usually a page a prescriber can act on:

1. **The specific question**, stated first. "Should I have clinical confirmation of this HFE C282Y
   homozygous call, and iron studies?" beats a genome dump.
2. **The finding**, with the variant, the genotype, the source platform, and the explicit note that
   it is **unconfirmed consumer raw data**.
3. **The two grades** — evidence strength and array reliability — so the clinician can calibrate
   immediately.
4. **The confirmatory test** that would settle it, and the phenotype test if one exists.
5. **Current medications and supplements**, so pharmacogenomic flags are concrete.
6. **What was not examined**, so a negative is not over-read.
7. **Nothing else.** No risk score, no protocol, no suggested prescription.
