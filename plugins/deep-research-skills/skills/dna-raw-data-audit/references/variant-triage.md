# Variant triage

How to get from hundreds of thousands of genotypes to the handful that could change a decision, and
how to grade each one honestly.

**Contents**
- §1 The funnel
- §2 ACMG/AMP classification and ClinVar review status
- §3 The two grading axes, applied
- §4 The false-positive problem and the confirmation rule
- §5 Variants of uncertain significance
- §6 When the honest answer is "nothing here"

---

## §1 The funnel

**Start from the catalogue, not from the file.** An unfiltered scan of a raw data file generates
false positives faster than it generates findings, because the file contains hundreds of thousands of
sites and the prior probability that any given one is both reliably called and decision-relevant is
very low. Scanning everything and then filtering is the wrong order.

```
  all genotypes in the file                      ~600,000 – 1,000,000 (array)
    ↓  restrict to catalogued sites with established effect sizes
  catalogue hits                                  tens
    ↓  drop no-calls and sites absent from the file
  actually called                                 fewer
    ↓  drop sites this platform cannot call reliably (R3/R4)
  reliably called                                 fewer still
    ↓  drop findings with no carrier-specific intervention (G3/G4)
  potentially actionable                          typically 0–3
    ↓  apply the confirmation rule
  actionable AFTER clinical confirmation          0–2
```

**Expect the bottom of the funnel to be nearly empty, and design the report for that.** A skill that
only knows how to narrate findings will invent them to fill the shape. The common, correct outcome is
one or two flags worth raising with a clinician and a clear statement that nothing else changes.

**Where a broader scan is legitimate:** a specific question the person brings ("a relative was found
to carry X — am I at risk?"), in which case look up that variant directly and apply the same grading.
That is a targeted lookup, not a scan.

---

## §2 ACMG/AMP classification and ClinVar review status

**The classification framework.** The professional joint-consensus framework for interpreting sequence
variants assigns each to one of **five tiers** — pathogenic, likely pathogenic, uncertain
significance, likely benign, benign — by combining weighted evidence criteria, each carrying a
direction and a strength. The framework anticipated gene- and disease-specific refinement, and expert
panels have since published specifications and refinements for particular criteria and genes
([PMC6885382](https://pmc.ncbi.nlm.nih.gov/articles/PMC6885382/) on specifications generally;
[PMC6185798](https://pmc.ncbi.nlm.nih.gov/articles/PMC6185798) on the null-variant criterion;
[PMC6709533](https://pmc.ncbi.nlm.nih.gov/articles/PMC6709533) on reputable-source criteria;
[PMC6225902](https://pmc.ncbi.nlm.nih.gov/articles/PMC6225902/) on expert-panel processes).

*Citation note: the originating framework paper did not resolve to a retrieved record in this
environment, so it is referenced by name with the resolvable specification literature above rather
than with an identifier reconstructed from memory. See `variant-catalog.md` §0 for the standard.*

**"Has a ClinVar entry" is not "is pathogenic".** ClinVar aggregates submitted interpretations, and
submitters disagree. Read the **review status** before the assertion:

- **Multiple submitters, no conflicts** or an **expert panel / practice guideline** review status —
  substantial weight.
- **Single submitter**, or **criteria not provided** — weak; one laboratory's opinion.
- **Conflicting interpretations** — the field has not settled it. **Report the conflict, do not pick
  a side.** A variant classified pathogenic by one submitter and benign by three is not a finding;
  it is an open question.
- A variant can be **reclassified**, and reclassification runs predominantly from uncertain toward
  benign as population frequency data accumulates. A pathogenic call from an older submission is
  worth re-checking.

**The frequency sanity check.** A variant asserted pathogenic for a rare dominant condition cannot be
common in population databases. If a flagged variant is present at appreciable frequency in large
reference cohorts, that is strong evidence against the pathogenic assertion — and this is precisely
the failure mode documented in direct-to-consumer interpretation, where variants labelled
"increased risk" turned out benign and common (§4).

---

## §3 The two grading axes, applied

Grade on **evidence strength** and **array reliability** independently, as defined in
`variant-catalog.md` §1. The point of two axes is that the response differs:

| Grade | Meaning | What to do |
| :--- | :--- | :--- |
| **E1 / R1** | Established, reliably called | The best case. Still confirm before clinical action; report with absolute risk and the action |
| **E1 / R3** | Established, unreliably called | **Not a finding — a prompt for a confirmatory test.** This is the most common shape for anything clinically serious |
| **E1 / R4** | Established, uncallable from this data | Report the *limitation*. Do not estimate. CYP2D6 is the archetype |
| **E2 / R1** | Established association, no carrier-specific intervention | Report with absolute risk, and state plainly that no action follows |
| **E3 / R1** | Small or moving effect, reliably called | Report as weak; resist converting it into advice |
| **E5 / R1** | Reliably called, and a professional body advises against testing | Report the *correction*. MTHFR is the archetype |
| **anything / R2** | Strand- or context-sensitive | Resolve orientation first, or report unresolved |

**Report both grades for every finding, always.** A single composite grade loses the information
that decides what to do.

---

## §4 The false-positive problem and the confirmation rule

**This is the most important section in the skill.**

### The anchoring evidence

The strongest study is a **population-scale** one: a retrospective diagnostic evaluation of
**≈49,908 people in UK Biobank who had both SNP-chip and next-generation-sequencing data**, plus a
small set of people who shared consumer test data
([PMID 33753354](https://pubmed.ncbi.nlm.nih.gov/33753354/) /
[PMC7879796](https://pmc.ncbi.nlm.nih.gov/articles/PMC7879796/), BMJ 2021). Its shape is the finding:

- For **common** variants, chip genotyping performed **well** — sensitivity, specificity, PPV and NPV
  all above 99% across >100,000 common variants. Arrays are not broken.
- For **very rare** variants the positive predictive value collapsed, and only a small minority of
  heterozygous chip genotypes were confirmed by sequencing.
- BRCA1/2 served as the clinically-actionable exemplar.

A smaller, earlier clinical-laboratory series reached the same conclusion from the confirmation side
([PMID 29565420](https://pubmed.ncbi.nlm.nih.gov/29565420/) /
[PMC6301953](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6301953/)), with companion commentaries
([PMID 29950595](https://pubmed.ncbi.nlm.nih.gov/29950595/),
[PMID 29955106](https://pubmed.ncbi.nlm.nih.gov/29955106/)) and a later analysis of the public-health
consequence ([PMID 33113957](https://pubmed.ncbi.nlm.nih.gov/33113957/)). Third-party interpretation
adds its own error burden ([PMID 29997392](https://pubmed.ncbi.nlm.nih.gov/29997392/)), and a
professional-society committee opinion addresses consumer disease-risk testing directly
([PMID 33399428](https://pubmed.ncbi.nlm.nih.gov/33399428/)).

*Specific percentages from this literature are not quoted here: they appeared only in search-tool
prose rather than in a retrieved record during verification, and `variant-catalog.md` §0 explains why
that disqualifies a number from shipping. The direction, the common-versus-rare split, and the
clinical consequence are firmly established and are what the rule rests on.*

### The mechanism — and the primary cause is not the one people name

Probe design and genotype-cluster separation are real contributors: arrays are optimised for common
variants, and cluster assignment degrades when almost no samples carry the rare allele.

**But the dominant mechanism is Bayesian and cannot be engineered away.** Positive predictive value
depends on prevalence, not just on assay quality. Take an excellent assay — 99% sensitivity, 99.9%
specificity — applied to a variant carried by 1 in 50,000 people:

```
 per 1,000,000 people tested:
   true carriers        20      -> ~20 detected
   non-carriers    999,980      -> ~1,000 false positives at 99.9% specificity
   positives            ~1,020  of which ~20 are real
   PPV ≈ 2%
```

**The test is 99.9% specific and still wrong about 98% of the people it flags**, purely because the
variant is rare. This is the same arithmetic as the screening-test case in
`deep-research-skills:video-source-audit` → `references/statistics-taxonomy.md` §4, and it is why no
amount of array improvement removes the need for confirmation on rare variants.

### Array and sequencing are not the same problem

**Do not transfer the array false-positive literature to sequencing data.** If one of the files is
whole-genome sequencing, the evidence above does not describe it: the failure modes differ, and
short-read sequencing is strong exactly where arrays are weak for single-nucleotide variants.

The confirmation rule still applies to sequencing, for **different** reasons:
- Consumer sequencing is not performed or reported under clinical-laboratory conditions, and the
  provider's own documentation typically says the data is not for clinical use.
- Short-read sequencing remains weak or blind for **repeat expansions, large structural variants,
  segmental duplications and pseudogene-confounded loci** — so "whole genome" does not mean
  "everything was seen".
- A variant call still needs orthogonal confirmation before it drives a clinical decision, which is
  a statement about the reporting context rather than about the assay's accuracy.

**Grade the two file types separately in the ledger**, and never let an array's weakness be cited
against a sequencing call or vice versa.

### The rule, stated without softening

> **No clinically significant finding from consumer raw data — array or sequencing — supports action
> until a clinical-grade laboratory confirms it.**

**Say it every time, as the finding rather than as a disclaimer.** The sentence that works is "this
needs confirming", not "I have this". Before recording any variant as present:

1. Check it was **called, not no-called** (`data-formats-and-parsing.md` §3).
2. Check **concordance and sample identity** if a second file exists (§5 there).
3. Check the **strand** if the site is or may be palindromic — and note that a homozygous call cannot
   establish this on its own.
4. Check the **population frequency** against the claimed pathogenicity (§2), and compute the PPV
   implied by that frequency.
5. Grade **array reliability** (or sequencing limitation) and state it.
6. State the **confirmatory test**.

**Never convert a tooling or data limitation into a statement about the person.** "The assay did not
call this reliably" and "you do not carry this" are different sentences, and only one of them is
supported.

---

## §5 Variants of uncertain significance

A VUS means the evidence does not currently support classifying the variant either way. It is
**common** — and it is not a weak pathogenic call.

- **Report as uncertain and leave it there.** Do not rank VUSs by suspicion, do not describe one as
  "probably significant", and do not let one drive a test, a screening decision, or a behaviour
  change.
- **Reclassification trends toward benign** as frequency data accumulates, so a VUS is more likely to
  resolve benign than pathogenic.
- **The honest framing for a person:** this is a variant whose meaning is not known, carrying no
  action, and the appropriate response is to leave it with a clinician who can re-check it later.
- A VUS in a gene relevant to a real family history is a reason for **genetics referral**, not for
  the skill to adjudicate.

---

## §6 When the honest answer is "nothing here"

**Design for this outcome, because it is the usual one.**

For most people, a consumer genome yields: a handful of reliably-called common variants with small
or no actionable effect, a few pharmacogenomic flags worth mentioning to a prescriber, possibly one
carrier status worth a conversation, and nothing that changes diet, exercise, supplementation, or
medical surveillance.

**Saying that clearly is the valuable output.** It is what distinguishes this skill from the
interpretation industry, which cannot say it because it has nothing to sell afterwards. The report
should be able to conclude:

> Nothing in these files changes what you should do. The two pharmacogenomic flags in section 3 are
> worth mentioning to a prescriber if you are ever prescribed the relevant drug classes. Everything
> else is either not reliably called by this platform, or established but without any intervention
> that has been shown to change the outcome in carriers.

**A report that always finds something is not more thorough — it is less reliable.** If the funnel
empties, report the empty funnel and the reasoning that emptied it.
