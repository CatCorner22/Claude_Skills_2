# Pharmacogenomics

Where consumer genetic data comes closest to being decision-relevant, and where it fails in ways
users do not expect.

**Contents**
- §1 Why star alleles are the hard part
- §2 What array data can and cannot call
- §3 Evidence frameworks: CPIC and PharmGKB
- §4 Gene–drug pairs worth raising
- §5 What to hand a prescriber

---

## §1 Why star alleles are the hard part

Pharmacogenes are described as **diplotypes** — `*1/*17`, `*4/*4` — not as single SNPs. A star allele
is a **haplotype**: a specific combination of variants occurring together on one chromosome copy.
Metabolic phenotype follows from the *pair* of haplotypes, so the diplotype is the unit of meaning.

**A raw data file is a list of independent, unphased genotypes.** That creates two distinct gaps:

**1. Phase.** Knowing a person is heterozygous at two sites does not tell you whether both variants
sit on the same chromosome copy (one altered allele, one normal) or on opposite copies (two altered
alleles). Those are different diplotypes with different phenotypes, and the genotype list cannot
distinguish them. Short-read and array data generally resolve this only by **statistical phasing**
against population haplotype frequencies — an inference, not a measurement, and one that fails
exactly where haplotypes are unusual.

**2. Copy number and structure.** Some pharmacogenes vary by whole-gene deletion, duplication, and
hybrid formation with a neighbouring pseudogene. None of that is visible in a per-site genotype call.

**3. Allele frequency — a third axis, independent of the first two, and the one usually left out.**
A variant can be perfectly callable in principle, carried on a single probe, with no phase or
copy-number problem, and still be untrustworthy from consumer data **because it is rare**. Positive
predictive value depends on the prior, not only on assay quality: at 99% sensitivity and 99%
specificity, a positive call is right about 92% of the time for a carrier prevalence of 10% and about
**33%** of the time at 0.5% (§2, the same table as the HLA proxies). **DPYD is the case that makes
this axis matter**: no phase problem, no copy-number problem, a severe-toxicity consequence — and
no-function alleles rare enough that a positive array call is a hypothesis rather than a result.
So **grade callability on all three axes**: phase, structure, and frequency.

### Phase ambiguity is real but narrow — and the case that flips the answer

"Two heterozygous sites" does not automatically mean ambiguity, and a skill that always reports
ambiguity is as wrong as one that never does. What decides it is whether any *defined* haplotype
carries both variants in cis:

- **CYP2C19 het at `*2` and `*17`** — exactly **one** consistent diplotype (`*2/*17`), because no
  defined allele carries both. No ambiguity to report.
- **CYP2C19 het at `*4` and `*17`** — **two** consistent diplotypes, because `*4B` is a real defined
  haplotype carrying both in cis. Both candidates carry one no-function allele, so this is a
  nomenclature ambiguity rather than a dosing one — say which kind it is.
- **TPMT het at `*3B` (rs1800460) and `*3C` (rs1142345)** — **two** consistent diplotypes with
  **opposite clinical consequences**: `*1/*3A` carries *one* no-function allele (intermediate
  metabolizer), `*3B/*3C` carries *two* (poor metabolizer). Phase collapses it completely — in cis
  gives `*3A/*1`, in trans gives `*3B/*3C` — and unphased data cannot choose.

**This is the case to name, and the counterweight belongs in the same breath:** the `*3B/*3C`
genotype is vanishingly rare (a guideline supplement put it at roughly 1 in 500,000 in European
ancestry, with none identified at that time). So the posture is **not** alarm. Report both
candidates, state that an **enzyme-activity assay distinguishes them directly**, and escalate only
if clinical signs suggest deficiency. That is the shape of every honest phase report: enumerate,
weight, and name the test that settles it.

**Record the allele-definition source and its version with every call.** Star-allele definitions and
genotype-to-phenotype tables are versioned and do change, so a diplotype quoted without its
definition source is not reproducible — and a re-run months later can legitimately disagree with it.

**APOE is the instructive contrast** (`variant-catalog.md` §7): among the three common haplotypes,
the diplotype *is* uniquely determined from two unphased genotypes, so APOE needs no phasing. That
is a property of APOE's specific allele structure, **not a general rule**, and assuming it
generalises to star alleles is the error this section exists to prevent.

---

## §2 What array data can and cannot call

### CYP2D6 — the canonical refusal

Do not call it. The reasons compound:

- The gene sits adjacent to pseudogenes of very high sequence similarity, so reads and probes
  mis-assign between them.
- **CYP2D6/CYP2D7 hybrid alleles** exist and are not representable as a set of SNP calls.
- **Whole-gene deletions and duplications** are common and change the activity score directly; copy
  number requires its own assay.
- Even with whole-genome sequencing, specialised callers are needed, and **published comparisons
  find those callers disagreeing with each other on structural variants**.

Records: [PMC5591463](https://pmc.ncbi.nlm.nih.gov/articles/PMC5591463/) (sequencing the locus),
[PMC7997805](https://pmc.ncbi.nlm.nih.gov/articles/PMC7997805/) (WGS-based calling),
[PMC7398905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7398905/) (caller disagreement on
structural variants), [PMC8881578](https://pmc.ncbi.nlm.nih.gov/articles/PMC8881578/) and
[PMC9534437](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9534437/) (long-read approaches for
hybrids and CNV).

**A whole-genome VCF does not rescue this, and the reason is worth stating precisely: the limitation
is a property of the REPRESENTATION, not of sequencing depth.** A VCF cannot express the structural
and copy-number variation CYP2D6 allele definitions require — a whole-gene deletion (`*5`) is not
representable in it at all — so **30× whole-genome sequencing written to a plain unphased VCF fails
CYP2D6 identically to a consumer array.** The reference open-source interpretation pipeline refuses
CYP2D6, HLA-A and HLA-B from a VCF regardless of how the VCF was produced, and emits a no-call by
design; its SNP-only research mode is documented as not for clinical use.

**What does change the verdict** is a CYP2D6-specific caller run against the *alignment* (BAM/CRAM)
rather than the VCF — Cyrius is the named example
([PMC7997805](https://pmc.ncbi.nlm.nih.gov/articles/PMC7997805/)) — or a clinical panel with a
copy-number assay. Some sequencing products return alignments, so the honest action for a person with
WGS is **"run a purpose-built caller on the alignment, or order a clinical panel"**, never *"we have
whole-genome data, so CYP2D6 is covered"*. And even a purpose-built caller is imperfect: the
published comparisons report high but not complete concordance against truth sets.

**The output for CYP2D6 is a stated limitation**, phrased so the person can act on it: *"Your data
cannot determine your CYP2D6 metabolizer status. If a prescriber is considering a drug where that
matters, a clinical pharmacogenomic panel can test it properly."* That is more useful than a guess,
and far more useful than a confident guess.

### HLA alleles — not inferable without validation

`HLA-B*57:01`, `HLA-B*15:02` and similar carry strong guideline support and matter a great deal
clinically. But **HLA typing is its own assay.** Some arrays carry tag SNPs with published
correlation to specific HLA alleles, and that can work — *when validated for that specific platform
and that specific allele in the relevant ancestry*. Absent that validation evidence, do not infer an
HLA allele from a tag SNP. Report the limitation and route to proper typing.

**The literature on the best-studied proxy disagrees, and instructively.** For `HLA-B*57:01`, some
cohorts report near-perfect correlation with a neighbouring tag SNP, while other work concludes the
tag does *not* substitute for typing in its population, and a further paper identifies two concrete
failure modes — incomplete linkage disequilibrium, and a **copy-number deletion** at the tag locus
that a consumer array cannot assess at all. So the answer is ancestry- and platform-specific rather
than yes or no.

**And the decision arithmetic is asymmetric, which is the usable finding.** Holding a proxy's
sensitivity and specificity both at 99% and varying only the prior:

| Carrier prevalence | PPV of a positive proxy | NPV of a negative proxy |
| ---: | ---: | ---: |
| 10% | 91.7% | 99.89% |
| 6% | 86.3% | 99.94% |
| 2% | 66.9% | 99.98% |
| 0.5% | 33.2% | 99.995% |

Degrade the proxy to sensitivity 70% / specificity 90% — a realistic figure where LD is weaker — and
at 6% prevalence the PPV falls to **30.9%** while the NPV is still **97.9%**.

> **So a negative proxy may reasonably lower suspicion; a positive proxy is a referral for real
> typing, never a result.** For the pairs where a drug label requires the test, consumer data cannot
> substitute for sequence-based HLA typing in either direction.

### Genes where common SNPs do capture most of the variation

For several pharmacogenes, a small number of common variants accounts for most functionally relevant
alleles in most populations. These are genuinely capturable — with care, and still subject to the
confirmation rule:

| Gene | Commonly probed | Caveat |
| :--- | :--- | :--- |
| **CYP2C19** | `*2` (rs4244285), `*3` (rs4986893), `*17` (rs12248560) | Covers the common no-function and increased-function alleles |
| **CYP2C9** | `*2` (rs1799853), `*3` (rs1057910) | Additional alleles matter more in non-European ancestries |
| **VKORC1** | rs9923231 | Used jointly with CYP2C9 |
| **CYP3A5** | `*3` (rs776746) | The cleanest array-callable case in pharmacogenomics: one SNP, and `*3` homozygosity (non-expresser) is the common state in European ancestry while expresser status is much more common in African ancestry — so ancestry changes what the result means |
| **SLCO1B1** | `*5` (rs4149056) | |
| **TPMT** | `*3B` (rs1800460), `*3C` (rs1142345), and `*2` (rs1800462) where the platform carries it | Must be read with NUDT15. Omitting `*2` understates both the callable set and how little a negative means |
| **NUDT15** | `*3` (rs116855232) | Especially important in East Asian ancestry; absent from older panels |
| **DPYD** | `*2A` (rs3918290) and other no-function alleles | **A negative at one or two sites does not clear a person** — several relevant alleles exist, and the consequence of missing one is severe |

**The asymmetry to hold onto:** a *detected* no-function allele at a reliably-called site is
informative (pending confirmation). A *negative* result is only as good as the panel's coverage, and
for several of these genes that coverage is partial. Never report a negative as clearance.

### A second class arrays cannot type: indels and repeats

CYP2D6 fails for structural reasons (§2). **A whole second class fails for a simpler one: the
functional variant is not a single-base substitution at all.** The clearest example is **UGT1A1
`*28`**, a **TA-repeat length polymorphism in the promoter** — there is no base to probe, so an array
can only carry a *tagging* SNP whose correlation with the repeat length varies by ancestry.

So the refusal generalises: **before trusting any star allele, ask what kind of variant defines it.**
A substitution may be callable; a repeat length, a copy-number change, or a gene conversion is not.
(23andMe also codes insertions and deletions as `DD`/`DI`/`II` rather than as bases, and some
conversion pipelines silently drop them — see `data-formats-and-parsing.md` §6.)

---

## §3 Evidence frameworks: CPIC and PharmGKB

**CPIC runs three separate grading systems, and conflating them is the commonest error in
pharmacogenomics writing.** They are:

| System | Scale | What it grades |
| :--- | :--- | :--- |
| Gene–drug pair level | **A / B / C / D** | **Prescribing ACTIONABILITY** — whether genetic information should change prescribing |
| Recommendation strength | strong / moderate / optional / no recommendation | How firmly a specific recommendation is made |
| Evidence strength | high / moderate / weak | The evidence behind an individual finding or allele-function assignment |

**So never write "CPIC evidence level A".** There is no such thing: A/B/C/D is the actionability
scale. Level **A** means genetic information *should* be used to change prescribing; **B** that it
*could* be; **C** that no prescribing action is recommended; **D** that the basis is too thin or too
conflicted to act on. Combined labels (A/B, B/C) are provisional, and assignments are provisional
until a guideline writing group evaluates them.

**Cite the guideline for the specific gene–drug pair rather than CPIC in general**, and treat the
guideline set as versioned — pairs are added and recommendations revised, so check the current
publication rather than quoting a remembered state.

**PharmGKB** curates variant–drug annotations on its own **levels of evidence (1A through 4)**, which
are a separate system again from either CPIC scale. **Read the tier definitions from PharmGKB itself
rather than from this file**: they could not be verified against a retrieved source in this
environment, and a paraphrased definition of someone else's grading system is exactly the kind of
claim that drifts. The usable shape is directional and safe to rely on: a level-4 annotation is a
research lead, not a prescribing input,
and the distance between 1A and 4 is the distance between medicine and speculation.

**Report the framework level alongside the finding.** "CPIC level A" and "PharmGKB level 3" demand
entirely different language, and a report that omits the level implies more than the evidence
carries.

---

## §4 Gene–drug pairs worth raising

Each of these is clinically significant, has guideline-level support, and is worth mentioning to a
prescriber — **as a flag for proper testing**, never as a dosing instruction.

**Check the guideline status live; do not quote it from this file.** Which pairs carry a guideline,
at what strength, and with what recommendation changes as guidelines are published and revised. This
table is a list of *pairs worth raising* and of *mechanisms*, which are stable. The recommendation
attached to any of them is not, and asserting one from a reference file is how a stale instruction
reaches a prescriber.

| Gene | Drug class | Why it matters |
| :--- | :--- | :--- |
| **CYP2C19** | Clopidogrel; also several proton-pump inhibitors and antidepressants | **The direction inverts across this one row, so never carry it across.** Clopidogrel is a *prodrug* requiring CYP2C19 activation, so reduced function means *less* active metabolite and reduced antiplatelet efficacy. For drugs CYP2C19 *clears*, the same reduced function means *higher* exposure. State which mechanism applies to the drug in question |
| **DPYD** | Fluoropyrimidines (5-FU, capecitabine) | Deficiency causes severe, occasionally fatal toxicity. One of the strongest cases for pre-treatment testing anywhere in medicine |
| **TPMT / NUDT15** | Thiopurines (azathioprine, mercaptopurine) | Reduced activity causes myelosuppression. Both genes must be considered |
| **HLA-B\*57:01** | Abacavir | Strongly associated with hypersensitivity; pre-treatment testing is standard practice. **Requires proper HLA typing** |
| **HLA-B\*15:02** | Carbamazepine | Associated with severe cutaneous reactions, with substantial ancestry-dependent allele frequency variation. **Requires proper HLA typing** |
| **SLCO1B1** | Statins (notably simvastatin) | Reduced transporter function raises systemic exposure and myopathy risk |
| **CYP2C9 + VKORC1** | Warfarin | Both feed published dosing algorithms; the classic multi-gene case |
| **G6PD** | **Named triggers, because "oxidative drugs" is not actionable:** rasburicase (contraindicated in deficiency), primaquine and tafenoquine, dapsone, nitrofurantoin, methylene blue, and — classically, outside medicine — fava beans | Deficiency causes haemolysis on oxidative challenge. **X-linked, which has a consequence this file previously left implicit:** a heterozygous female is a mosaic, her enzyme activity can fall anywhere from near-normal to deficient, and **a genotype cannot resolve where** — so a heterozygous female call is a prompt for an enzyme assay, never reassurance. Enzyme assay is definitive where genotype is partial, and it is also cheap |
| **CYP2D6** | Codeine, tamoxifen, many antidepressants and antipsychotics | Clinically major — **and not callable from this data** (§2). The finding is the limitation |
| **HLA-B\*58:01** | Allopurinol | Associated with severe cutaneous adverse reactions, with strongly ancestry-dependent carriage. **Requires proper HLA typing** — and it is the third HLA pair, alongside abacavir and carbamazepine, that belongs on any list of this kind |
| **CYP3A5** | Tacrolimus | A transplant-immunosuppression dosing gene, and the one genuinely array-callable pair here (§2): expressers clear tacrolimus faster and reach lower trough concentrations on a standard dose |
| **RYR1 / CACNA1S** | Potent volatile anaesthetics and succinylcholine | **The highest-acuity pair in this file, and the one case where the person cannot raise it in the moment** — they will be unconscious. A pathogenic variant implies presumed malignant-hyperthermia susceptibility, which changes the anaesthetic plan rather than a dose. Variant interpretation here is specialist work and a consumer call is not a diagnosis; the action is to carry the question to an anaesthetist **before** any planned procedure |
| **UGT1A1** | Irinotecan (and atazanavir) | Reduced glucuronidation raises exposure and neutropenia risk. Also the standing example of a variant arrays cannot type directly (§2) — `*28` is a promoter TA-repeat, so a consumer "result" here is a tag, not the allele |

---

## §5 What to hand a prescriber

A pharmacogenomic result is useful only if it reaches the person who prescribes. The deliverable:

1. **The question first.** "I have unconfirmed consumer genotype data suggesting a CYP2C19
   reduced-function allele. If clopidogrel is ever considered for me, would you want a clinical
   pharmacogenomic panel first?"
2. **The variant**, its rsID, the observed genotype, the platform, and the explicit statement that it
   is **unconfirmed consumer raw data**.
3. **The framework level** for the gene–drug pair (§3), so the clinician can calibrate without
   looking it up.
4. **The array-reliability grade**, so they know how much to trust the call itself.
5. **The limitations**, named: no phasing, no copy number, CYP2D6 not determinable, HLA not typed,
   and which relevant alleles the platform does not probe.
6. **Current medications and supplements**, so the flags are concrete rather than hypothetical.
7. **Nothing else.** No suggested dose, no suggested drug, no suggested change to an existing
   prescription. The skill's job ends at a well-formed question.

**And never advise stopping or altering a prescribed medication** — including one the data appears to
flag. **This is not merely this skill's caution:** the regulator that authorised a narrow consumer
pharmacogenetic report attached a labelling condition to it that users not stop or change any
medication on the basis of the report, and has separately warned about pharmacogenetic tests making
unapproved claims. The rail is the condition under which this kind of information is allowed to
exist at all. Especially then: abrupt discontinuation carries its own risk, and the prescriber holds context
the genome does not contain.

### The branch for a drug the person is already taking

The list above is written for the *prospective* case — "if this is ever considered for me". The
retrospective case is commoner and needs its own handling, because the temptation to act is higher:

- **Keep taking it.** The flag is unconfirmed consumer data; the prescription reflects a clinical
  decision made with information this analysis does not have.
- **Raise it at the next routine contact**, with the same well-formed question, rather than as an
  emergency. Note that a drug already tolerated for a long period is itself evidence, and it
  frequently outweighs an unconfirmed genotype.
- **Symptoms are a clinical matter, not a genomics one.** If there are signs that could indicate
  toxicity or treatment failure, that is a reason to contact a clinician promptly about *the
  symptoms* — the genotype is context the clinician may want, not the thing being reported.
- **Two exceptions run on a different clock**, because the exposure is scheduled rather than
  ongoing: malignant-hyperthermia susceptibility must be on record **before** any planned
  anaesthesia, and a DPYD or TPMT/NUDT15 flag matters **before** a first dose of the relevant
  chemotherapy — in both cases the question goes to the team *ahead* of the exposure, not after it.
