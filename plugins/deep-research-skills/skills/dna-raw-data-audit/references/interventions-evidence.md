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

- **For peptides, the genetic evidence is G4 across the board.** There is essentially no established
  gene–interaction evidence for the peptides people ask about. A genotype therefore supplies **no
  basis at all** for recommending one. This rail is what prevents the skill's most likely failure
  mode — becoming a genotype-flavoured supplement and peptide storefront, which is what most of this
  market actually is.
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

**Start from the MTHFR correction**, because it is the field's emblematic case and getting it right
is a good test of whether a tool is trustworthy. A professional-society practice guideline advised
against routine MTHFR polymorphism testing on minimal-clinical-utility grounds
([PMID 23288205](https://pubmed.ncbi.nlm.nih.gov/23288205)), later amended
([PMID 32587351](https://pubmed.ncbi.nlm.nih.gov/32587351)) with the recommendation against testing
standing through the amendment; multiple other professional bodies concur
([PMC9175241](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175241/)), and the clinical-utility question
has been revisited ([PMC11288266](https://pmc.ncbi.nlm.nih.gov/articles/PMC11288266/)).

The methylfolate-protocol industry built on MTHFR is **G3 at best and largely G4**. If a person
arrives already taking a stack because of an MTHFR result, the useful service is the correction —
delivered without contempt, because they were sold this by people who sounded authoritative.

**The narrow set with genuine substance**, and note how modest it is:

| Genotype | What it supports | Grade |
| :--- | :--- | :--- |
| **HFE** C282Y homozygous (confirmed) | Changes iron advice in the *opposite* direction to the default — avoid iron supplementation, and get iron studies. One of the few places a genotype genuinely redirects a supplement decision | G2 / T1 |
| **G6PD** deficiency (confirmed) | A real avoidance list — specific drugs, and fava beans. Avoidance, not supplementation | G1 / T1 |
| **ALDH2** rs671 | Strengthens the case for reducing alcohol. No supplement addresses it | G3 / T1 for the behaviour |
| **MCM6/LCT** rs4988235 | Explains lactose intolerance. Dietary choice follows symptoms | G2 / T2 |
| **Confirmed deficiency on a blood test** | The actual basis for supplementing — and it is a *measurement*, not a genotype | — / T1–T2 |

**The pattern worth stating plainly: measure, don't infer.** Serum 25-OH-D beats any vitamin D
pathway genotype. Ferritin and transferrin saturation beat HFE. A B12 level beats an MTHFR result.
Where a cheap decisive phenotype test exists, the genotype's only real value is prompting it.

**Where the general recommendation does not change based on genotype — the common case — say so.**
That is the correct answer, and the one the industry suppresses because it sells nothing.

---

## §5 Peptides

The owner asked for this explicitly, so it gets a real assessment rather than a refusal. The
assessment is structural: **grade the class, name what is actually established, and apply §2.**

**The GLP-1 contrast case, first, because it calibrates everything else.** GLP-1 receptor agonists
(semaglutide, tirzepatide) are approved medicines with large randomised outcome trials — **T1,
approved**. That is what real evidence for a peptide looks like. Every other class below should be
read against it, and the gap is large. Their genetic evidence is still **G4**: a genotype does not
select them.

**Growth-hormone secretagogues and GHRH analogues** — ipamorelin, CJC-1295, sermorelin, tesamorelin
(which has a narrow approved indication; name it precisely rather than generalising), and MK-677
(frequently sold alongside peptides but not itself a peptide). Evidence for the commonly marketed
uses is **T3–T6**. Theoretical and real concerns centre on sustained IGF-1 elevation. **G4.**

**BPC-157.** Marketed heavily; evidence overwhelmingly preclinical (**T4–T5**). It has been placed
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

**Melanotan I/II and PT-141** — melanocortin agonists. Melanotan carries a specific, concrete
concern about naevi and melanoma that distinguishes it from the "unproven but probably inert"
category. **G4.**

**Three risks that are independent of whether any molecule works**, and which the marketing never
addresses:
1. **Product integrity.** Grey-market injectables carry contamination, mislabelling, dosing-error
   and sterility risk. Review literature on unregulated injectable peptide use documents real harm
   ([PMC13585006](https://pmc.ncbi.nlm.nih.gov/articles/PMC13585006)).
2. **Sport prohibition.** Peptide hormones, growth factors and related substances sit in the WADA
   prohibited classification, with growth-hormone releasing factors prohibited at all times. **Name
   the mechanism and send an athlete to the current published list** — the list is versioned and the
   edition in force changes.
3. **Unknown interactions** with prescribed medication, which nobody is monitoring in a self-sourced
   protocol.

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
