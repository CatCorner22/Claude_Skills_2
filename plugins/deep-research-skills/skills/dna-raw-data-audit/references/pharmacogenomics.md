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

### Genes where common SNPs do capture most of the variation

For several pharmacogenes, a small number of common variants accounts for most functionally relevant
alleles in most populations. These are genuinely capturable — with care, and still subject to the
confirmation rule:

| Gene | Commonly probed | Caveat |
| :--- | :--- | :--- |
| **CYP2C19** | `*2` (rs4244285), `*3` (rs4986893), `*17` (rs12248560) | Covers the common no-function and increased-function alleles |
| **CYP2C9** | `*2` (rs1799853), `*3` (rs1057910) | Additional alleles matter more in non-European ancestries |
| **VKORC1** | rs9923231 | Used jointly with CYP2C9 |
| **SLCO1B1** | `*5` (rs4149056) | |
| **TPMT** | `*3B` (rs1800460), `*3C` (rs1142345) | Must be read with NUDT15 |
| **NUDT15** | `*3` (rs116855232) | Especially important in East Asian ancestry; absent from older panels |
| **DPYD** | `*2A` (rs3918290) and other no-function alleles | **A negative at one or two sites does not clear a person** — several relevant alleles exist, and the consequence of missing one is severe |

**The asymmetry to hold onto:** a *detected* no-function allele at a reliably-called site is
informative (pending confirmation). A *negative* result is only as good as the panel's coverage, and
for several of these genes that coverage is partial. Never report a negative as clearance.

---

## §3 Evidence frameworks: CPIC and PharmGKB

**CPIC** publishes gene–drug guidelines with graded recommendations, assigning gene–drug pairs
evidence levels (A through D) reflecting whether genetic information should change prescribing.
Level A pairs are those where prescribing action is recommended. **Cite the guideline for the
specific gene–drug pair rather than CPIC in general**, and treat the guideline set as versioned —
pairs are added and recommendations are revised, so check the current publication rather than quoting
a remembered state.

**PharmGKB** curates variant–drug annotations with **levels of evidence 1A through 4**, where 1A
denotes annotations supported by a guideline or a well-replicated consensus and 4 denotes a single
study. Use the level explicitly: a level-4 annotation is a research lead, not a prescribing input,
and the distance between 1A and 4 is the distance between medicine and speculation.

**Report the framework level alongside the finding.** "CPIC level A" and "PharmGKB level 3" demand
entirely different language, and a report that omits the level implies more than the evidence
carries.

---

## §4 Gene–drug pairs worth raising

Each of these is clinically significant, has guideline-level support, and is worth mentioning to a
prescriber — **as a flag for proper testing**, never as a dosing instruction.

| Gene | Drug class | Why it matters |
| :--- | :--- | :--- |
| **CYP2C19** | Clopidogrel | A prodrug requiring CYP2C19 activation; reduced-function alleles mean reduced active metabolite, with downstream consequences for antiplatelet efficacy. Also relevant to some proton-pump inhibitors and antidepressants |
| **DPYD** | Fluoropyrimidines (5-FU, capecitabine) | Deficiency causes severe, occasionally fatal toxicity. One of the strongest cases for pre-treatment testing anywhere in medicine |
| **TPMT / NUDT15** | Thiopurines (azathioprine, mercaptopurine) | Reduced activity causes myelosuppression. Both genes must be considered |
| **HLA-B\*57:01** | Abacavir | Strongly associated with hypersensitivity; pre-treatment testing is standard practice. **Requires proper HLA typing** |
| **HLA-B\*15:02** | Carbamazepine | Associated with severe cutaneous reactions, with substantial ancestry-dependent allele frequency variation. **Requires proper HLA typing** |
| **SLCO1B1** | Statins (notably simvastatin) | Reduced transporter function raises systemic exposure and myopathy risk |
| **CYP2C9 + VKORC1** | Warfarin | Both feed published dosing algorithms; the classic multi-gene case |
| **G6PD** | Oxidative drugs | Deficiency causes haemolysis. Enzyme assay is definitive where genotype is partial |
| **CYP2D6** | Codeine, tamoxifen, many antidepressants and antipsychotics | Clinically major — **and not callable from this data** (§2). The finding is the limitation |

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
flag. Especially then: abrupt discontinuation carries its own risk, and the prescriber holds context
the genome does not contain.
