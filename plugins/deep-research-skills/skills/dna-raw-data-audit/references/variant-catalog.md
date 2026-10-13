# Variant catalogue

The sites worth looking at, what each is, whether consumer platforms call it dependably, and what
action — if any — follows.

**Contents**
- §0 The verification standard, and why this file carries no frozen effect sizes
- §1 Grading axes
- §2 Tier A — clinically actionable if confirmed
- §3 Tier B — pharmacogenomic flags
- §4 Tier C — carrier status and reproductive relevance
- §5 Tier D — real but low-actionability
- §6 Tier E — actively over-interpreted
- §7 APOE, in full
- §8 What is not in this catalogue, and why

---

## §0 The verification standard, and why this file carries no frozen effect sizes

**Every citation here was verified against a retrieved index record** — a PMID inside a
`pubmed.ncbi.nlm.nih.gov` URL, a PMC ID inside a PMC URL, or an identifier inside a publisher URL.
A search tool returns two things: retrieved records, and a model-written prose summary beneath them.
**Only the records are evidence.** The prose states confident publishers, years, volumes and DOIs
for items that returned no supporting record; that failure mode was reproduced repeatedly while
building this file, and several plausible-looking citations were dropped because of it.

**This catalogue deliberately does not freeze effect-size numbers.** That is a design decision, not
an omission, for three reasons:

1. **Effect sizes move.** Penetrance and odds-ratio estimates are revised as cohorts grow, and the
   revisions have repeatedly been large and in the direction of *smaller* effects than early studies
   reported. A number frozen in a reference file becomes wrong quietly.
2. **They are population-specific.** A single number is not portable across ancestries, and quoting
   one as though it were is the error `risk-communication.md` §4 exists to prevent.
3. **A number stated without its source is unfalsifiable.** This library's standing rule is that any
   external number carries a provenance mark or an honest hedge. A catalogue of bare effect sizes
   would violate it on every line.

So this file gives what is *stable* — what the variant is, the mechanism, whether the platform calls
it, and whether any action attaches — and the skill's Do-it stage 11 requires a live literature pass
for the numbers, resolved at analysis time. **If you find yourself wanting to quote an effect size
from this file, that is the signal to go and get it from the literature instead.**

### Anchors that are verified and stable enough to state

| Claim | Record |
| :--- | :--- |
| Direct-to-consumer raw data carries a materially elevated false-positive rate for rare variants, and clinical confirmation is required before action | [PMC6301953](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6301953/) — "False-positive results released by direct-to-consumer genetic tests highlight the importance of clinical confirmation testing for appropriate patient care"; companion commentaries [PMID 29950595](https://pubmed.ncbi.nlm.nih.gov/29950595/), [PMID 29955106](https://pubmed.ncbi.nlm.nih.gov/29955106/) |
| Third-party interpretation of DTC raw data carries its own burden of error | [PMID 29997392](https://pubmed.ncbi.nlm.nih.gov/29997392/) |
| DTC screening is limited for hereditary breast/ovarian cancer specifically | [PMC10581610](https://pmc.ncbi.nlm.nih.gov/articles/PMC10581610/) |
| Routine MTHFR polymorphism testing is advised against | [PMID 23288205](https://pubmed.ncbi.nlm.nih.gov/23288205) (practice guideline), amended by [PMID 32587351](https://pubmed.ncbi.nlm.nih.gov/32587351); concurring [PMC9175241](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175241/), [PMC11288266](https://pmc.ncbi.nlm.nih.gov/articles/PMC11288266/) |
| CYP2D6 cannot be called reliably from array data: pseudogene similarity, CYP2D7 hybrids, CNV, and a phasing requirement | [PMC5591463](https://pmc.ncbi.nlm.nih.gov/articles/PMC5591463/), [PMC7997805](https://pmc.ncbi.nlm.nih.gov/articles/PMC7997805/) (WGS-based calling), [PMC7398905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7398905/) (callers disagree on structural variants), [PMC8881578](https://pmc.ncbi.nlm.nih.gov/articles/PMC8881578/) |
| Polygenic scores derived in predominantly European-ancestry cohorts transfer poorly | preprint [bioRxiv 10.1101/441261](https://www.biorxiv.org/content/10.1101/441261.full.pdf); [PMID 39218908](https://pubmed.ncbi.nlm.nih.gov/39218908/); contested in part by a [medRxiv analysis](https://www.medrxiv.org/content/10.1101/2025.09.18.25336069.full.pdf) — cite the dispute, not one side |
| Family-ascertained penetrance exceeds population-based penetrance, with the gap narrowing in larger studies | [PMC2447846](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2447846/) (family-based; its title states the point), [PMID 11044354](https://pubmed.ncbi.nlm.nih.gov/11044354/) / [PMC2408797](https://pmc.ncbi.nlm.nih.gov/articles/PMC2408797/) (population-based), [PMID 25192939](https://pubmed.ncbi.nlm.nih.gov/25192939) (population screening), [PMID 16484695](https://pubmed.ncbi.nlm.nih.gov/16484695) |
| Injectable peptides sold outside regulation carry risks independent of efficacy | [PMC13585006](https://pmc.ncbi.nlm.nih.gov/articles/PMC13585006) |

**Dropped for failing the standard**, recorded because the drops are as informative as the keeps:
the ACMG/AMP sequence-variant interpretation guideline (Richards et al.) and the published
*Nature Genetics* version of the polygenic-score portability paper never appeared in a returned
record in this environment, though both are clearly real and are referenced by many records that
did resolve. They are cited here **by framework name with resolvable secondary literature**, never
with an identifier reconstructed from memory.

---

## §1 Grading axes

Grade every finding on **two independent axes**. A finding can be strong on one and worthless on the
other, and collapsing them is the commonest interpretation error.

**Evidence strength** — what the literature establishes:
- **E1** Established, with an intervention tested in carriers.
- **E2** Established association, no carrier-specific intervention evidence.
- **E3** Replicated but small effect, or effect size still moving.
- **E4** Single study, or preclinical/mechanistic only.
- **E5** Contested, or a professional body advises against testing.

**Array reliability** — whether a consumer platform calls *this site* dependably:
- **R1** Common variant, directly probed, well-clustered. Trust the call; still confirm before
  clinical action.
- **R2** Probed but orientation- or context-sensitive (an A/T or C/G site, or near an indel).
- **R3** Rare variant on an array — elevated false-positive rate. Treat as a prompt for a
  confirmatory test, never as a result.
- **R4** Requires phase, copy number, or specialised typing the platform cannot provide. **Do not
  call.**

Report both grades, always. "E1/R3" and "E1/R1" demand completely different responses.

---

## §2 Tier A — clinically actionable if confirmed

These can change medical management. **All of them require clinical-grade confirmation first**
(§0 anchor 1), and none should be reported as a result from raw data alone.

| Gene / variant | What it is | Typical grade | Action if confirmed |
| :--- | :--- | :--- | :--- |
| **HFE** C282Y (rs1800562), H63D (rs1799945) | Hereditary haemochromatosis risk alleles. C282Y homozygosity is the main genotype of interest; penetrance is incomplete and lower than early estimates implied | E1 / R1 | Iron studies (ferritin, transferrin saturation) — a cheap phenotype test that settles the question far better than the genotype does. This is the model case: the genotype's value is prompting a *measurement* |
| **F5** Factor V Leiden (rs6025) | Commonest inherited thrombophilia allele | E2 / R1 | Context for a clinician around thrombosis risk, surgery, oestrogen exposure. Does **not** by itself warrant anticoagulation |
| **BRCA1 / BRCA2** founder variants | Some platforms probe a small number of founder variants only | E1 / R3 | Confirmation, then genetics referral. **Critically:** a negative consumer result is near-meaningless here, because only a handful of thousands of possible variants were probed ([PMC10581610](https://pmc.ncbi.nlm.nih.gov/articles/PMC10581610/)) |
| **G6PD** deficiency variants | X-linked; causes haemolysis on oxidative triggers | E1 / R2–R3 | A real contraindication list for specific drugs and foods. Confirm by enzyme assay, which is definitive where genotype is not |
| **Genes on a professional actionable-secondary-findings list** | A curated, versioned set of genes where incidental findings are considered medically actionable | E1 / R3 | Use the list as the filter for "is this worth acting on at all". Name the instrument and its version rather than treating it as fixed |

**The HFE pattern generalises and is worth internalising:** the most useful genetic findings are
the ones that point at a cheap, decisive *phenotype* measurement. Iron studies for HFE, an enzyme
assay for G6PD, a lipid panel for a lipid variant. The genotype earns its keep by prompting the
test, not by substituting for it.

---

## §3 Tier B — pharmacogenomic flags

Full treatment, including the callable-versus-not split and what to hand a prescriber, is in
`pharmacogenomics.md`. Summary of what the catalogue extracts:

| Gene | Sites | Grade | Note |
| :--- | :--- | :--- | :--- |
| **CYP2C19** | rs4244285 (*2), rs4986893 (*3), rs12248560 (*17) | E1 / R1 for these SNPs | The common no-function and increased-function alleles are capturable; the diplotype inference still needs care |
| **CYP2C9** | rs1799853 (*2), rs1057910 (*3) | E1 / R1 | Pairs with VKORC1 for warfarin dosing algorithms |
| **VKORC1** | rs9923231 | E1 / R1 | |
| **SLCO1B1** | rs4149056 (*5) | E1 / R1 | Statin myopathy risk |
| **TPMT** | rs1800460 (*3B), rs1142345 (*3C) | E1 / R1–R2 | Thiopurine dosing. **NUDT15 must be read alongside it** |
| **NUDT15** | rs116855232 (*3) | E1 / R2 | Particularly important in East Asian ancestry; omitted from older panels |
| **DPYD** | rs3918290 (*2A) and other no-function alleles | E1 / R2–R3 | Fluoropyrimidine toxicity. A *negative* result at one or two sites does **not** clear a person — several relevant alleles exist |
| **CYP2D6** | rs3892097 and others are present on arrays | **E1 / R4 — do not call** | Deletions, duplications, CYP2D7 hybrids and a phasing requirement place the diplotype beyond array data (§0 anchor). Report the limitation, not a phenotype |
| **HLA-B** alleles (e.g. \*57:01, \*15:02) | — | E1 / R4 unless specifically typed | HLA typing is its own assay. Do not infer an HLA allele from array tag SNPs without validation evidence for that specific platform |

---

## §4 Tier C — carrier status and reproductive relevance

Heterozygous carrier status for recessive conditions is often the most genuinely useful output of
consumer data — and it is also where findings most clearly implicate relatives.

- Consumer platforms probe a **small, specific subset** of variants per condition. "Carrier status
  not detected" means only "none of the probed variants was seen", and for most recessive conditions
  that is a long way from clearance. Say so explicitly every time.
- Carrier status is decision-relevant mainly in a **reproductive** context, and the relevant test
  there is a clinical expanded carrier screen, not raw data.
- **This tier triggers the relatives rail.** A carrier finding is information about parents and
  siblings as much as about the person. Flag that before disclosing.

---

## §5 Tier D — real but low-actionability

Well-established genotypes whose honest answer is usually "this does not change what you should do".
Report them with that framing rather than manufacturing an action.

| Gene / variant | What it is | Grade | Honest action |
| :--- | :--- | :--- | :--- |
| **ALDH2** rs671 | Reduced aldehyde dehydrogenase activity; the flushing variant. Carries an established association with alcohol-related cancer risk | E1 / R1 | Genuinely actionable in one direction only: it strengthens the case for reducing alcohol. No supplement addresses it |
| **MCM6 / LCT** rs4988235 | Lactase persistence regulatory variant | E1 / R1 | Explains a phenotype the person already knows. Dietary choice follows symptoms, not genotype |
| **CYP1A2** rs762551 | Caffeine metabolism | E3 / R1 | Weaker than marketed. Observed caffeine tolerance beats the genotype |
| **FTO** rs9939609 | Commonest BMI-associated locus | E2 / R2 (A/T site — strand-ambiguous) | **None.** The important finding is that it does not appear to blunt response to lifestyle intervention — so the advice is unchanged by genotype |
| **Common GWAS hits generally** | Per-allele odds ratios near 1 | E2–E3 / R1 | Individually uninformative. See `risk-communication.md` §1 |

---

## §6 Tier E — actively over-interpreted

Report these primarily to *correct* the interpretation the person has probably already encountered.

**MTHFR C677T (rs1801133) and A1298C (rs1801131).** The single most over-interpreted pair in
consumer genetics. A professional-society practice guideline advised against routine MTHFR
polymorphism testing on the grounds of minimal clinical utility
([PMID 23288205](https://pubmed.ncbi.nlm.nih.gov/23288205)); it was subsequently amended
([PMID 32587351](https://pubmed.ncbi.nlm.nih.gov/32587351)) and the recommendation against testing
stood through the amendment. Other professional bodies reached the same position
([PMC9175241](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175241/)), and the clinical-utility question
has been revisited since ([PMC11288266](https://pmc.ncbi.nlm.nih.gov/articles/PMC11288266/)).
Grade **E5 / R1** — the genotype is called reliably; the interpretation industry built on it is the
problem. Report the guideline, not a methylfolate protocol.

**"Detox", "methylation" and "mitochondrial" SNP panels.** Collections of variants with mechanistic
stories and no carrier-specific intervention evidence. Grade E4 at best. The honest output is that
no action follows.

**Vitamin D pathway variants.** Associations exist; the intervention question is whether genotype
changes what to do, and the answer has not been established. A serum 25-OH-D measurement is cheap,
decisive, and makes the genotype moot — the §2 phenotype pattern again.

---

## §7 APOE, in full

APOE deserves separate treatment: it is the most consequential common variant most people will find,
and it is also the easiest to get technically wrong.

**It needs two SNPs, not one.** The haplotypes are defined jointly by **rs429358** (Cys112Arg) and
**rs7412** (Arg158Cys):

| Haplotype | rs429358 | rs7412 |
| :--- | :--- | :--- |
| ε2 | T | T |
| ε3 | T | C |
| ε4 | C | C |
| ε1 (rare) | C | T |

**Among the three common haplotypes, all six diplotypes are uniquely determined from the two
unphased genotypes — APOE needs no phasing.** That is a real and useful contrast with star alleles,
and it was verified by enumerating every haplotype pair (the bundled script implements and tests it).

**Exactly one combination is formally ambiguous.** `rs429358 = C/T` with `rs7412 = C/T` is consistent
with both **ε2/ε4** and **ε1/ε3**. ε1 is rare, so ε2/ε4 is overwhelmingly the right read — but it
cannot be *excluded* without phasing, and the honest report says so. The script flags this case
rather than silently resolving it.

**On actionability, be careful and be honest.** ε4 carries an established association with
Alzheimer's risk, dose-dependent between heterozygotes and homozygotes, and the absolute lifetime
figures are what matter — a relative multiple quoted alone is close to meaningless here, and the
numbers must come from the live literature pass with the person's ancestry and age accounted for
(`risk-communication.md`). What makes APOE genuinely hard is that **no intervention has been shown
to change the genotype's effect.** That makes it the clearest case in the whole catalogue where the
correct output is information and support for decisions the person may want to make — planning,
insurance, research participation, whether they wanted to know at all — and *not* a supplement or
peptide protocol. Any tool that answers an ε4 result with a stack recommendation is selling
something. Grade **E2 / R1**: called reliably, established, no carrier-specific intervention.

This is also the variant most likely to be genuinely unwelcome news, which is why the
`your-environment.md` question about what the person does *not* want surfaced is not a formality.

---

## §8 What is not in this catalogue, and why

- **Frozen effect sizes** — §0.
- **Polygenic risk scores** — a score is not a site. `risk-communication.md` §4 covers what they can
  honestly be used for; the short version is that ancestry decides whether the number transfers.
- **Anything requiring phase, copy number, or specialised typing** — R4. Named as a limitation
  rather than estimated.
- **Variants of uncertain significance** — reported as uncertain, never ranked or acted on.
- **Peptide and supplement "genotype matches"** — there is essentially no established
  gene-interaction evidence for peptides, so no genotype supports recommending one.
  `interventions-evidence.md` carries that rail and the reasoning.
- **Ancestry, traits and relatedness** — a different product. Relatedness inference in particular can
  surface family structure nobody asked about; see the relatives rail in `SKILL.md`.
