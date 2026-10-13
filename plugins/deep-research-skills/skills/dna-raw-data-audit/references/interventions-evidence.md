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

1. An intervention exists, with evidence at **T1 or T2** — **or at T3 where the intervention is
   avoidance of a documented hazard and a randomised trial is unobtainable or unethical.** That
   carve-out is necessary rather than convenient: without it the rail disqualifies this file's own
   three strongest findings (HFE, G6PD, ALDH2), none of which has a randomised trial and none of
   which ever will. **State which case you are in.**
2. That intervention has been shown to change the outcome **in carriers specifically** — i.e. the
   genetic evidence is **G1 or G2**, not G3.

Nearly nothing clears both. The honest consequence:

- **For peptides the genetic evidence is G4 for nearly all of them — and the rail must rest on
  non-actionability, not on absence of evidence**, because "none at all" is false and a single
  counterexample would otherwise appear to break the rail.

  **The weak candidate first, because reading it carefully is the lesson.** **GLP1R rs6923761** has
  gene–response data: a pilot pharmacogenetics study found a genotype effect on **gastric emptying**
  — a pharmacodynamic surrogate — with a *non-significant* difference in weight loss
  ([PMC6003833](https://pmc.ncbi.nlm.nih.gov/articles/PMC6003833)), and a randomised pharmacogenomic
  analysis found reduced percentage body fat at **p = 0.062**, not significant, with no significant
  genotype association with weight
  ([PMC9335902](https://pmc.ncbi.nlm.nih.gov/articles/PMC9335902/)). On the endpoint that matters,
  then, the two are a surrogate hit and a borderline null: **G3 to weak G2, not replication** — and
  the disagreement is on the *same* endpoint, not across different ones. An earlier version of this
  file called it "reported and replicated", which those citations do not support.

  **The decisive counterexample is a different drug, and naming it makes the rail stronger rather
  than weaker.** **Setmelanotide** is a peptide whose approved indication is *gated on genotype*:
  chronic weight management in obesity due to POMC, PCSK1 or LEPR deficiency, with the deficiency
  established by genetic testing, plus a Bardet–Biedl syndrome indication. **One detail worth
  checking against the label, because if it holds it is the single real exception to this skill's
  VUS rail:** a secondary drug-profile source describes the gate as admitting variants interpreted
  as pathogenic, likely pathogenic **or of uncertain significance** — a weaker and more interesting
  gate than "pathogenic only". *Prose-sourced and not confirmed against the label here; read the
  label before relying on it*
  ([approval announcement](https://www.biospace.com/rhythm-pharmaceuticals-announces-fda-approval-of-imcivree-setmelanotide-as-first-ever-therapy-for-chronic-weight-management-in-patients-with-obesity-due-to-pomc-pcsk1-or-lepr-deficiency)).
  That is a label-level gene–intervention pair — **G1 by this file's own definition, for a peptide** —
  and it carries the point alone. (**Metreleptin is not a second example**, though an earlier version
  of this file said it was: its approved indication is the complications of leptin deficiency in
  *generalised lipodystrophy* — gated on a **phenotype**, with no gene named, and that condition is
  itself genetically heterogeneous.) A rail resting on "no peptide has gene-interaction evidence"
  would still be false on setmelanotide alone.

  **So state it precisely.** The peptides this market sells have **no** genotype indication; the
  peptides that *are* genotype-selected are prescription drugs for **rare monogenic disease a
  consumer array cannot diagnose** — single-gene deficiencies needing clinical sequencing and expert
  interpretation, not a tagged SNP. **For the peptides anyone is being sold, the genotype supplies no
  basis at all**, and the exception shows the shape of the rule rather than breaking it. This is what
  prevents the skill's most likely failure mode — becoming a genotype-flavoured supplement and
  peptide storefront, which is what most of this market is.
- **For supplements, it is G3 or G4 with narrow exceptions** (§4).
- **For medicines, pharmacogenomics is the real G1 answer** (§3), and it routes to a prescriber.

When a person asks "what should I take based on my DNA?", the accurate answer for almost every
genotype is: *nothing, on that basis.* Say it, then give them what the data *does* support — usually
a phenotype measurement to request, or a flag to raise with a prescriber.

---

## §3 Medicines

**Pharmacogenomics is the legitimate intersection**, and `pharmacogenomics.md` owns it. The short
version for this file:

- Gene–drug pairs with guideline-level support are **G1** — and, with the setmelanotide exception in
  §2, effectively the only intervention class in this
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
is a good test of whether a tool is trustworthy. A professional society advised
against routine MTHFR polymorphism testing on minimal-clinical-utility grounds
([PMID 23288205](https://pubmed.ncbi.nlm.nih.gov/23288205)), with the recommendation standing through
a later **addendum** — and **what that addendum did matters: it reaffirmed the recommendation while
reclassifying the document itself from an evidence-based practice guideline to a clinical practice
resource**, because it no longer met the college's criteria for the former. So the direction survived
and the document's evidentiary standing was downgraded; describe it accordingly rather than citing
"a practice guideline" indefinitely. The addendum is listed by title on the society's own
practice-resources page and is **not** the same record as
[PMID 32587351](https://pubmed.ncbi.nlm.nih.gov/32587351) — **that is a correction notice *about* the
addendum.** An earlier version of this file cited the erratum as its evidence for what the addendum
said, inside the paragraph it calls the field's emblematic case.

The position is echoed in the thrombosis literature by a call to action arguing MTHFR should not form
part of inherited-thrombophilia testing
([PMC9175241](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175241/)) — **a single-author commentary, so
"multiple professional bodies concur" overstated what that citation carries.** The clinical-utility
question has also been revisited
([PMC11288266](https://pmc.ncbi.nlm.nih.gov/articles/PMC11288266/)).

**The causal loop the MTHFR story depends on is also closed at the other end.** The story runs
*variant → higher homocysteine → cardiovascular risk → so lower homocysteine*. But the
homocysteine-lowering trials, pooled, **did not reduce myocardial infarction or all-cause
mortality** — B-vitamin allocation moved the biomarker and not those outcomes. **So even granting
every step of the mechanism, the intervention it implies has been tested and does essentially nothing
for the outcome the MTHFR story is sold on**, which is a stronger objection than disputing the
genotype's effect size.

**State the one exception rather than overclaiming, because it is the only part of the causal loop
that did not close:** a modest reduction in **stroke** does survive pooling in that literature, and
stroke is also the one endpoint where the homocysteine Mendelian-randomisation work has shown
anything. A blanket "no cardiovascular benefit" erases it. *(No identifier ships with this paragraph:
the review previously cited here did not re-resolve on re-check, and the Cochrane review of
homocysteine-lowering interventions is the record to retrieve when a resolver is reachable. The
pooled figures are prose-sourced either way.)*

The methylfolate-protocol industry built on MTHFR is **G3 at best and largely G4**. If a person
arrives already taking a stack because of an MTHFR result, the useful service is the correction —
delivered without contempt, because they were sold this by people who sounded authoritative.

**Three boundaries the correction must carry, because without them it can be heard as advice to stop
folate.** All three were missing from this file until a safety review named them:

1. **Ring-fence periconceptional folic acid.** It is recommended for anyone who could become
   pregnant **regardless of MTHFR genotype**, and nothing in this correction touches it. "The
   methylfolate industry is G4" must never be heard as "folate does not matter".
2. **Severe biallelic MTHFR deficiency is a different thing entirely** — a rare, real and *treatable*
   inborn error with a homocystinuria-like phenotype. The guidance against testing concerns the
   common C677T/A1298C polymorphisms; do not let a corrective about those over-generalise into
   dismissing a genuine diagnosis.
3. **Folate can mask B12 deficiency while neurological damage continues.** This is the actionable
   half of "a B12 level beats an MTHFR result": the reason to measure B12 *before* supplementing
   folate is not tidiness, it is that the supplement can hide the deficiency it does not treat.

**The narrow set with genuine substance**, and note how modest it is:

| Genotype | What it supports | Grade |
| :--- | :--- | :--- |
| **HFE** C282Y homozygous (confirmed) | Changes iron advice in the *opposite* direction to the default — avoid iron supplementation, and get iron studies. One of the few places a genotype genuinely redirects a supplement decision | G2 / **T3** — the downgrade is honest rather than pedantic: there is no randomised trial of iron-supplement avoidance with hard outcomes in C282Y homozygotes, and the evidence is cohort, registry and mechanistic |
| **G6PD** deficiency (confirmed) | **An avoidance list is only useful if it names things, and this is the supplements table, so name the supplement first: high-dose or intravenous vitamin C.** Published haemolysis cases on high-dose vitamin C are concentrated in G6PD deficiency, including a fatal one and cases of methaemoglobinaemia with haemolytic anaemia, and authors have proposed G6PD deficiency as a contraindication to high-dose vitamin C therapy — a mass-market supplement and an IV-clinic staple, which makes this the one row here where naming the item could prevent a crisis. Then the drugs (`pharmacogenomics.md` §4 carries them): rasburicase, contraindicated; primaquine and tafenoquine, dapsone, nitrofurantoin, methylene blue. And fava beans. **Avoidance, not supplementation** | G1 / **T3** — case series and pharmacovigilance, because a randomised trial of oxidant-trigger avoidance in deficient people would be unethical. **Say why the tier is unachievable rather than borrowing a higher one** |
| **ALDH2** rs671 | Strengthens the case for reducing alcohol. No supplement addresses it. **Name the genotype that carries the risk, because it is not the obvious one: heterozygotes.** One inactive allele clears acetaldehyde poorly but leaves alcohol tolerable enough to keep drinking; homozygotes usually self-limit. In meta-analysis the heterozygote-plus-heavy-drinking combination carried a large elevated risk while heterozygotes who drink little or not at all showed no significant elevation — effect modification, not a bare association *(figures prose-sourced; ship the direction)* | **G2** / **T3** for the behaviour — **regraded on both axes.** T1 was wrong because the evidence for alcohol reduction with hard outcomes is observational plus Mendelian randomisation, not randomised. And G3 was wrong because: this is the textbook replicated gene–*environment* interaction, where genotype modifies the effect of an exposure. G3 means "associated with the outcome, modifies no response", which contradicted both the action in the cell beside it and `variant-catalog.md`'s own entry |
| **MCM6/LCT** rs4988235 | Explains lactose intolerance — **in European ancestry only.** This variant tags the European lactase-persistence haplotype; independent persistence alleles exist elsewhere, so a "non-persistent" call outside that ancestry is frequently a **false negative**. Dietary choice follows symptoms, which the person already knows | G2 / T2 |
| **Celiac HLA-DQ2/DQ8** | **A rule-out and nothing else, and the asymmetry is arithmetic.** At 1% prevalence with 30–40% population carriage, NPV stays above 99.9% while PPV never exceeds about 3.5% — so a negative makes coeliac disease very unlikely and a positive says almost nothing, because up to 40% of everyone carries it. Two cautions, and the second is the reverse of what an earlier version of this file said: sensitivity is high but **not** 100%, so do not promise a perfect rule-out — and **diet does not affect this test.** Serology and biopsy go falsely negative once gluten has been withdrawn; a genotype does not change with diet, **which is exactly why HLA typing is the usable rule-out in someone already eating gluten-free, and why it can spare them a gluten challenge.** Telling such a reader the test is uninterpretable removes their one usable option and pushes them toward a challenge that has real symptomatic cost | G2 / T2, as a rule-out |
| **FUT2** secretor status | **Flips the usual story: it changes the MEASUREMENT, not the requirement.** Non-secretors run different serum B12 levels for the same intake, so the variant is a reason to interpret a *lab value* differently rather than to supplement. **The reported direction is *higher* measured serum B12 in non-secretors — which would make a normal B12 weaker reassurance in one — but that direction could not be confirmed against a retrieved record here, so treat it as unverified rather than as the finding.** "Different" alone is unactionable; an unverified direction, labelled, is at least a question someone can take to a clinician. That makes it one of the few panel variants with a genuine use — and the use is on the test, not the person | G2 / T2 for interpretation |
| **Confirmed deficiency on a blood test** | The actual basis for supplementing — and it is a *measurement*, not a genotype | — / T1–T2 |

**The pattern worth stating plainly: measure, don't infer.** Serum 25-OH-D beats any vitamin D
pathway genotype — and note *why*: the vitamin D pathway variants explain part of someone's
**baseline** 25(OH)D, not their **response to supplementation**, which is the quantity a
supplementation decision needs. A variant that predicts where you start and not where you end up is
a G3 finding however well replicated it is. Ferritin and transferrin saturation beat HFE. **Plasma homocysteine — with folate, and B12 — beats
an MTHFR result**, because homocysteine is the measured intermediate the whole MTHFR story runs
through and the analyte the guidance substitutes; B12 belongs there as the co-measurement, for the
masking reason in boundary 3 above, rather than as the headline substitute.
Where a cheap decisive phenotype test exists, the genotype's only real value is prompting it.

**Where the general recommendation does not change based on genotype — the common case — say so.**
That is the correct answer, and the one the industry suppresses because it sells nothing.

---

## §5 Peptides

The owner asked for this explicitly, so it gets a real assessment rather than a refusal. The
assessment is structural: **grade the class, name what is actually established, and apply §2.**

**The GLP-1 contrast case, first, because it calibrates everything else.** GLP-1 receptor agonists
**and the dual GIP/GLP-1 agonist tirzepatide** are approved medicines with large randomised trials — **T1, approved**. That is what real evidence
for a peptide looks like, and every class below should be read against it; the gap is large.

**But do not lump them, because their outcome evidence is not the same *shape*** — which is the
honest statement, and not the one an earlier version of this file made: that tirzepatide had no
equivalent outcome trial. It does. Semaglutide has a placebo-controlled cardiovascular-outcome trial
reporting superiority on major adverse cardiovascular events in a broad at-risk population.
Tirzepatide's placebo-controlled hard-outcome evidence sits in a **specific** population —
obesity-related heart failure with preserved ejection fraction, where the SUMMIT trial (n = 731)
reported a reduction in the composite of cardiovascular death or worsening heart failure, driven by
the heart-failure component
([society trial summary](https://www.acc.org/Latest-in-Cardiology/Articles/2024/11/13/21/17/sat-959am-summit-aha-2024);
*the primary publication's identifier did not resolve here, so the trial is named rather than cited
with a reconstructed PMID*).

Its **general-population** cardiovascular-outcome trial is a different animal again: run against an
active comparator (a GLP-1 receptor agonist with established placebo-controlled benefit) and
reporting **noninferiority**
rather than placebo-controlled superiority — which is the sharper and more durable distinction
between the two drugs.

**So both support a cardiovascular-benefit claim, and what differs is the population and the
comparator.** Check each drug's own outcome evidence rather than inheriting it from the class — the
same error as inheriting a guideline across a gene–drug pair, and one this paragraph committed while
teaching against it.

Their genetic evidence is **G2 at best and not usable** (§2): a genotype does not select them.

**Growth-hormone secretagogues and GHRH analogues** — ipamorelin, CJC-1295, sermorelin, tesamorelin
— among which the approved indication is **tesamorelin's alone**, and should be *named* rather than
called narrow: in substance, reduction of excess abdominal fat in adults with HIV-associated
lipodystrophy, with the label also ruling out what people want it for (not indicated for weight
loss, weight-neutral effect, long-term cardiovascular safety not established). Those limitations are
corroborated close to the label's own words; **which labelled product they belong to, and the exact
wording, come from the provenance note immediately below — there is more than one tesamorelin label
and they are not interchangeable.** And MK-677 (frequently sold alongside peptides but
not itself a peptide). Evidence for the commonly marketed uses is **T3–T6**, and concerns centre on
sustained IGF-1 elevation. **G4.**

**Label provenance for tesamorelin — and a provenance distinction worth keeping.** A search channel
can establish a document's **identity** without returning a word of its **content**, and those are
two different grades. Both were tested here, and the result is mostly the second:

- **Verified with title (a secondary host of the label, not the label):** `Egrifta SV Prescribing
  Information` ([drugs.com/pro/egrifta-sv.html](https://drugs.com/pro/egrifta-sv.html)) and
  `EGRIFTA SV` ([medlibrary.org](https://medlibrary.org/lib/rx/meds/egrifta-sv/)). These are
  republishers. They are good enough to establish that a US prescribing information exists for this
  product and what it is broadly about; they are **not** the label of record, and a copy carries
  whatever date its host last refreshed.
- **Corroborated by a returned record, in close to the label's own words:** the product is a
  growth-hormone-releasing-factor analogue indicated for **reduction of excess abdominal fat in
  HIV-infected adult patients with lipodystrophy**, and the Limitations of Use rule out what people
  want it for — *not indicated for weight loss management as it has a weight neutral effect*, and
  *long-term cardiovascular safety has not been established*.
- **Corroborated, and the part most likely to be got wrong: there is more than one labelled
  tesamorelin product, and they are not interchangeable.** A returned record states in terms that
  the 1 mg-per-vial and 2 mg-per-vial products differ in dosage, number of vials per dose,
  reconstitution and storage, and therefore carry **separate labels**. So "the tesamorelin label" is
  not a thing that exists: any quotation has to name the product. (A third, later-marketed name
  appears in secondary sources; it did not return here and is not asserted.)
- **UNAVAILABLE here:** the label of record itself. `accessdata.fda.gov` and `dailymed.nlm.nih.gov`
  fail at **DNS** in this environment — not TLS, not 403 — so no primary label text is fetchable, and
  no DailyMed SPL set ID is quoted here, because an identifier this channel never returned is not
  one to write down. Read the current label by product name at DailyMed or FDA, and take the exact
  indication sentence, the contraindications, the malignancy warning and anything about the effect
  persisting only while treatment continues **from there, never from this paragraph**.
- **The maintenance question is url-only, so no claim attaches to it.** Two PubMed identifiers
  resolve — [20101189](https://pubmed.ncbi.nlm.nih.gov/20101189/) (a PubMed URL returned) and
  20554713 (only a mirror returned, titled merely "Journal Article") — but **neither record's title
  came back in a result link**, only in generated prose. Under §0 of `variant-catalog.md` that is
  `url-only`: the identifiers exist, what the papers *are* is unestablished here, and the trial
  design read out of that prose is therefore not reported. Resolve them before citing either.

*Two live observations, recorded because they are this file's own hazards happening rather than
being described.* The generated prose **contradicted itself inside one session** — asserting a
pregnancy contraindication, then saying it could not confirm one, then asserting it again, and
answering a question about visceral adipose tissue with a trunk-fat figure. And the searches
surfaced **peptide-vendor wikis and supplier "research" pages** among the results for a prescription
drug, which is the vendor-dominated-search hazard §5 warns about, arriving unprompted. Both are
reasons the grades above are stated flatly instead of hedged.

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
`variant-catalog.md` §0.)* It has been
considered by a regulator in the process that identifies bulk substances which **may present
significant safety risks** in compounding
([regulator's bulk-substances page](https://www.fda.gov/drugs/human-drug-compounding/certain-bulk-drug-substances-use-compounding-may-present-significant-safety-risks);
reviews at [PMC12313605](https://pmc.ncbi.nlm.nih.gov/articles/PMC12313605/) and
[PMC12446177](https://pmc.ncbi.nlm.nih.gov/articles/PMC12446177/)).

**State this substance's OWN documented concerns, which an earlier version of this file got wrong by
importing another peptide's.** The concerns recorded for BPC-157 are about **identity and
characterisation**: it has no standardised pharmacopoeial name, and the review found missing
characterisation data — impurities, aggregates, bioburden, bacterial endotoxins. *Immunogenicity by
route of administration* is the stated rationale for a different nominated peptide, and attaching it
here was a misattribution. **The category, the nomination status and the stated rationale have all
moved over time, and they are per-substance — re-check the live source rather than quoting this
paragraph, and never carry one substance's rationale across to another.** **G4.**

**TB-500/thymosin beta-4, thymosin alpha-1, epitalon, GHK-Cu, and similar** — assess as a class:
individual human evidence is thin (**T4–T6**), with occasional narrow exceptions worth checking
individually rather than assuming. **G4.**

**Three different situations under one street name, and collapsing them is the error this very file
warns about twice** ("peptide is not a regulatory category"). Taken separately:

**Melanotan I is afamelanotide, an APPROVED product with a narrow indication** — reducing
phototoxicity in erythropoietic protoporphyria, authorised on randomised placebo-controlled
evidence. Its regulatory status is "approved, narrow indication" and its tier for the approved use is
**T1/T2**, not unapproved and not T6; an earlier version of this file graded it as grey-market
alongside melanotan II. **Material sold online as "melanotan I" is not that product.** The approved
product's own labelling calls for periodic full-body skin examination — which is the monitoring the
naevus signal below actually implies.

**Melanotan II is unapproved**, is **T6** for the use it is marketed for, and is the one the naevus
signal attaches to: the case report cited below is titled for melanotan II specifically. It carries
a specific, concrete concern about naevi that distinguishes it from the
"unproven but probably inert" category: published case reports describe **eruptive naevi and
darkening of pre-existing naevi after use**, now with three records each carrying its returned
title:

- *"Eruptive naevi and darkening of preexisting naevi 24 h after a single mono-dose injection of
  melanotan II"*
  ([repository record](https://research.uni-luebeck.de/en/publications/eruptive-naevi-and-darkening-of-preexisting-naevi-24-h-after-a-si/))
  — the single-dose case.
- *"Changes of melanocytic lesions induced by Melanotan injections and sun bed use in a teenage
  patient with FAMMM syndrome"* ([PMC3663356](https://pmc.ncbi.nlm.nih.gov/articles/PMC3663356)) —
  a teenager with a familial melanoma syndrome who both injected and used a sun bed, which is the
  **compound** exposure rather than the drug alone.
- An Acta letter describing lentigines and naevi augmented after self-injection
  ([10.2340/00015555-0928](https://medicaljournals.se/acta/download/10.2340/00015555-0928)) — over
  roughly 150 injections, not one.

**And a review of this literature reports a melanoma case while explicitly declining to claim
causation**, noting that the patients shared fair skin, many naevi and tanning-bed use. That is the
honest shape of the signal: a drug that drives melanogenesis in people who are also tanning, with
documented naevus change and no established causal link to melanoma. **The action is dermatological
review, not reassurance** — and for the *approved* melanotan I product, periodic full-body skin
examination is what its own labelling calls for.

*Citation history, kept because the corrections went both ways.* Two identifiers were withdrawn from
this sentence when a pass could not resolve them; a later re-source returned `PMC3663356` **with its
title**, so it is restored — and it is a different journal from the one that pass named. The other
withdrawal stands and was sharpened: `10.2340/00015555-1130` is a letter about *nomenclature* —
which molecule the street name denotes — while **`10.2340/00015555-0928`** is the naevus letter. Two
adjacent DOIs at one journal, one on point and one not (`variant-catalog.md` §0). **State
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
[PMC6819021](https://pmc.ncbi.nlm.nih.gov/articles/PMC6819021/), which reports **both** phase 3
trials in one paper — so the adjacent ID an earlier version cited beside it was withdrawn). So it is **T1/T2 for its
licensed indication, approved** — not a grey-market unknown, and an earlier version of this file
misclassified it. **Two things follow, and the second is the one that matters:** the licensed
indication is narrow and the published effect sizes are modest, and **material sold online as
"PT-141" is not the approved product** — it is the same molecule name attached to an unregulated
supply chain, which is the product-integrity problem below (item 1) rather than an efficacy question. **G4.**

**Three risks that are independent of whether any molecule works**, and which the marketing never
addresses — followed by a fourth item that is a *method* rail rather than a risk the user carries:
1. **Product integrity.** Grey-market injectables carry contamination, mislabelling, dosing-error
   and sterility risk. Review literature on unregulated injectable peptide use documents real harm
   ([PMC13585006](https://pmc.ncbi.nlm.nih.gov/articles/PMC13585006)).
2. **Sport prohibition, and there are TWO mechanisms, not one.** Peptide hormones, growth factors
   and related substances sit in their own prohibited class, with growth-hormone releasing factors
   prohibited at all times. **And a separate class covers substances not approved by any governmental regulatory health
   authority for human therapeutic use** — which is what a research-only peptide is, whatever its
   pharmacology. **Read that class as residual, not as an overlap:** it covers what no other
   section addresses, so a growth-hormone secretagogue is caught by the peptide-hormone section
   rather than by the catch-all, and the two are mutually exclusive by construction. (An earlier
   version of this item said the catch-all "sweeps in most of this market", which the list's own
   structure makes doubtful.) Either way the conclusion stands: **"it isn't on the named-substance
   list" is not a defence.** Check the edition in force. **Name both
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
name the safety and regulatory considerations, and say clearly that **for the peptides this market
sells the genome contributes nothing
to the decision** — because that is the accurate answer and it is the one thing a genetics tool is
uniquely positioned to say. Then route the actual decision to a clinician who can see the whole
person. **No doses. No sourcing. No protocols.**

Being vague would fail the owner, who asked for substance. Being a storefront would fail them worse.

---

## §6 Lifestyle factors, which is where the evidence actually is

Worth stating because it is the honest anchor for almost every report: the interventions with the
strongest outcome evidence are **not genotype-tailored**, and they dominate anything a consumer
genome will suggest.

**Smoking cessation, dietary pattern and physical activity** (including resistance training) sit at
**T1 for hard outcomes** — long-term mortality, events, and major mobility disability as a function
endpoint. **Sleep duration and regularity, and alcohol reduction, sit at T3**: large and consistent
observational evidence, with randomised work limited to surrogate endpoints such as blood pressure.
An earlier version of this paragraph graded all five T1, inflating the tier in the file's own
favoured direction — the error it polices everywhere else. All five apply **regardless of
genotype**, which is the actual point, and none becomes better supported by being
genotype-tailored. `coding-agent-skills:fitness-nutrition-science` owns the training and nutrition detail;
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
