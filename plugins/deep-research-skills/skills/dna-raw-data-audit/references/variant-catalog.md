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

**A returned URL proves an identifier EXISTS. It does not prove what the paper IS.** This
distinction cost two citations in this skill, both withdrawn above and in
`interventions-evidence.md`: a PMC ID returned as a bare `pmc.ncbi.nlm.nih.gov/articles/PMCxxxxxxx`
link with **no title beside it**, which a later pass could not re-resolve; and an ID adjacent to a
real one, cited for a paper that turns out to be reported entirely within its neighbour. So:

> **Attach a specific claim only to a record whose TITLE was returned.** A bare URL supports "this
> identifier resolves"; a returned title supports "this identifier is *that* paper". Adjacent
> identifiers (…21 / …23) deserve particular suspicion, because that is what a guessed ID looks like.

**Verified identifier form.** In practice **PMIDs and PMCIDs appear inside returned URLs routinely;
bare DOIs almost never do.** So prefer a PMID or PMCID as the shipping identifier, and treat a DOI
as verified only when it appears inside a publisher URL that was itself returned. A DOI quoted from
prose alone does not ship, however real the paper is.

### The one carve-out: three variants where a number is unavoidable

**The no-frozen-numbers rule has a failure mode, and it has to be named.** It defers every figure to
a live literature pass — and in this environment that pass cannot return a figure. Scholarly
resolvers and direct page fetches are blocked by the egress proxy (see `your-environment.md`); the
only working channel is a search tool whose *records* yield identifiers but whose *numbers* live in
model-written prose. So "go and get the number at analysis time" resolves, in practice, to either
nothing or a confidently-stated invention — and it fails hardest at APOE, where the news is least
welcome and a wrong figure is least likely to be challenged.

**So three variants carry anchored figures here**, each with its provenance graded explicitly. This
is strictly safer than an instruction that cannot be executed, and the grading is the point:

> **Provenance grades used below.** **[R]** the identifier resolved to a retrieved record *and* the
> figure came from that record. **[R/p]** the identifier resolved to a retrieved record, but the
> **figure itself was read from search-result prose** and not from the record — treat it as an
> order-of-magnitude anchor, quote it as a range, and re-verify before it reaches a person.
> **[calc]** computed here from the figures beside it; the derivation is shown so it can be checked.

| Variant | Anchored figures | Grade |
| :--- | :--- | :--- |
| **HFE C282Y homozygosity** (rs1800562) | Documented iron-overload-related disease in **28.4% of male homozygotes (95% CI 18.8–40.2)** and **1.2% of females (95% CI 0.03–6.5)**, in 31,192 people of northern European descent aged 40–69 — Allen et al. 2008, *NEJM* 358(3):221–230 ([PMID 18199861](https://pubmed.ncbi.nlm.nih.gov/18199861/)). The sex asymmetry is the headline, and the female interval is very wide on few events | **[R/p]** |
| **F5 Factor V Leiden heterozygosity** (rs6025) | First-event incidence about **0.45%/year (CI 0.28–0.61)** in carrier relatives vs **0.10%/year (CI 0.02–0.19)** in non-carrier relatives; an independent prospective cohort of asymptomatic carriers gave **0.58%/year (CI 0.26–1.10)** over 1,564 observation-years ([PMID 11583312](https://pubmed.ncbi.nlm.nih.gov/11583312/); systematic review [PMID 19531787](https://pubmed.ncbi.nlm.nih.gov/19531787/)) | **[R/p]** |
| ↳ *what that means over a horizon* | At 0.45%/yr vs 0.10%/yr: **10 years** 4.41% vs 1.00% (ARR 3.41 pp, 34 extra per 1,000, NNH ⌈1/0.0341⌉ = 30); **20 years** 8.63% vs 1.98% (ARR 6.64 pp, 66 extra per 1,000, NNH ⌈1/0.0664⌉ = 16). So **96 of 100 carriers are event-free at 10 years and 91 of 100 at 20** — which is why heterozygosity alone does not warrant anticoagulation. Note the relative risk *shrinks* with horizon (4.5 per-year → 4.43 at 10 years → 4.35 at 20) as both risks compound toward 1, so **state the horizon with the multiple** | **[calc]** |
| **APOE** (rs429358 + rs7412) | Lifetime Alzheimer's risk to age 85, from a semi-dominant model: baseline **11% male / 14% female**; **e3/e4 23% / 30%**; **e4/e4 51% / 60%** — Genin et al. 2011, *Molecular Psychiatry* ([PMC3162068](https://pmc.ncbi.nlm.nih.gov/articles/PMC3162068/), [10.1038/mp.2011.52](https://doi.org/10.1038/mp.2011.52)). **Quote these as the high end of a range, with the design named:** this analysis combined relative risks from case-control data with absolute risks from cohort studies, and cohort-based 20-year cumulative dementia incidence in e4/e4 runs materially lower (roughly 31–40%). Those measure different quantities and are not interchangeable | **[R/p]** |
| ↳ *the dose effect, and its complement* | e3/e4 is **+12 pp male / +16 pp female** over baseline (2.1×); e4/e4 is **+40 pp / +46 pp** (4.6× / 4.3×). Going from one e4 to two roughly **doubles** the heterozygote's absolute risk (2.2× male, 2.0× female). And on the same figures, **49 per 100 male and 40 per 100 female e4/e4 homozygotes reach 85 unaffected** — report that in the same breath, every time | **[calc]** |

**Everything else in this file stays unfrozen.** The carve-out is three variants, not a precedent for
a fourth: it exists because these are the ones a person will insist on a number for, and because a
range with stated provenance beats both silence and invention.

### Anchors that are verified and stable enough to state

| Claim | Record |
| :--- | :--- |
| Direct-to-consumer raw data carries a materially elevated false-positive rate for rare variants, and clinical confirmation is required before action | **Population-scale, the strongest anchor:** [PMID 33753354](https://pubmed.ncbi.nlm.nih.gov/33753354/) / [PMC7879796](https://pmc.ncbi.nlm.nih.gov/articles/PMC7879796/) — ~49,908 people with both chip and sequencing data; chips perform well on common variants and collapse in PPV on very rare ones. **Clinical-laboratory series:** [PMID 29565420](https://pubmed.ncbi.nlm.nih.gov/29565420/) / [PMC6301953](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6301953/), with commentaries [PMID 29950595](https://pubmed.ncbi.nlm.nih.gov/29950595/), [PMID 29955106](https://pubmed.ncbi.nlm.nih.gov/29955106/) and the public-health consequence [PMID 33113957](https://pubmed.ncbi.nlm.nih.gov/33113957/) |
| A professional society has addressed consumer disease-risk testing directly | [PMID 33399428](https://pubmed.ncbi.nlm.nih.gov/33399428/) |
| Third-party interpretation of DTC raw data carries its own burden of error | [PMID 29997392](https://pubmed.ncbi.nlm.nih.gov/29997392/) |
| DTC screening is limited for hereditary breast/ovarian cancer specifically | [PMC10581610](https://pmc.ncbi.nlm.nih.gov/articles/PMC10581610/) |
| Routine MTHFR polymorphism testing is advised against | [PMID 23288205](https://pubmed.ncbi.nlm.nih.gov/23288205) (practice guideline), with the recommendation standing through a later addendum the society lists by title; **[PMID 32587351](https://pubmed.ncbi.nlm.nih.gov/32587351) is the correction notice *about* that addendum, not the addendum** — do not cite it as the amendment. Echoed by a call to action in the thrombosis literature ([PMC9175241](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175241/), a single-author commentary — not a second society position), and the clinical-utility question has been revisited ([PMC11288266](https://pmc.ncbi.nlm.nih.gov/articles/PMC11288266/)) |
| CYP2D6 cannot be called reliably from array data: pseudogene similarity, CYP2D7 hybrids, CNV, and a phasing requirement | [PMC5591463](https://pmc.ncbi.nlm.nih.gov/articles/PMC5591463/), [PMC7997805](https://pmc.ncbi.nlm.nih.gov/articles/PMC7997805/) (WGS-based calling), [PMC7398905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7398905/) (callers disagree on structural variants), [PMC8881578](https://pmc.ncbi.nlm.nih.gov/articles/PMC8881578/) |
| Polygenic scores derived in predominantly European-ancestry cohorts transfer poorly, and the decline is continuous along genetic distance rather than stepwise between labelled groups | [PMC6563838](https://pmc.ncbi.nlm.nih.gov/articles/PMC6563838/) (Martin 2019) and its preprint [bioRxiv 10.1101/441261](https://www.biorxiv.org/content/10.1101/441261); [PMC5384097](https://pmc.ncbi.nlm.nih.gov/articles/PMC5384097/) (Martin 2017); [PMC8764121](https://pmc.ncbi.nlm.nih.gov/articles/PMC8764121/) with correction [PMC8874215](https://pmc.ncbi.nlm.nih.gov/articles/PMC8874215/) (Privé 2022 — strongest design, one cohort for training and testing); [10.1038/s41586-023-06079-4](https://doi.org/10.1038/s41586-023-06079-4) (Ding 2023); [10.1038/s41467-019-11112-0](https://doi.org/10.1038/s41467-019-11112-0) (Duncan 2019). `risk-communication.md` §4 has the table. Cite the dispute over magnitude, not one side |
| Family-ascertained penetrance exceeds population-based penetrance, with the gap narrowing in larger studies | [PMC2447846](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2447846/) (family-based; its title states the point), [PMID 11044354](https://pubmed.ncbi.nlm.nih.gov/11044354/) / [PMC2408797](https://pmc.ncbi.nlm.nih.gov/articles/PMC2408797/) (population-based), [PMID 25192939](https://pubmed.ncbi.nlm.nih.gov/25192939) (population screening), [PMID 16484695](https://pubmed.ncbi.nlm.nih.gov/16484695) |
| Injectable peptides sold outside regulation carry risks independent of efficacy | [PMC13585006](https://pmc.ncbi.nlm.nih.gov/articles/PMC13585006) |

**Dropped for failing the standard**, recorded because the drops are as informative as the keeps:
the ACMG/AMP sequence-variant interpretation guideline (Richards et al.) and the published
*Nature Genetics* version of the polygenic-score portability paper never appeared in a returned
record in this environment, though both are clearly real and are referenced by many records that
did resolve. They are cited here **by framework name with resolvable secondary literature**, never
with an identifier reconstructed from memory.

**Withdrawn on re-check:** an earlier version of this file cited `PMID 39218908` as the
portability anchor and a 2025 medRxiv preprint as the counterweight. A later verification pass
could not re-resolve that PMID to any record, and anchoring one side of a live dispute on a single
non-peer-reviewed preprint is weak on its own terms. Both were replaced by the five records above,
each of which resolved in two independent searches. **An identifier that no longer resolves is
withdrawn, not downgraded to a hedge** — and recording the withdrawal is what stops it reappearing.

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
  The sites in this catalogue verified as palindromic are **rs1799945** (HFE H63D, C/G — and it
  sits in the actionable tier) and **rs9939609** (FTO, A/T). The bundled script carries the
  verified allele pair for each site it knows, so it can say `AMBIGUOUS` or `CLEAR` rather than
  guessing; where the pair is not verified it reports `UNDETERMINED`, which is a statement about
  the catalogue rather than about the site.
- **R3** Rare variant on an array — elevated false-positive rate. Treat as a prompt for a
  confirmatory test, never as a result.
- **R4** Requires phase, copy number, or specialised typing the platform cannot provide. **Do not
  call.**

Report both grades, always. "E1/R3" and "E1/R1" demand completely different responses.

### Why the tiers exist, quantitatively

The maximum absolute-risk shift attributable to **one** genotype spans more than an order of
magnitude across these tiers (computed in `risk-communication.md` §4 for the GWAS rows, and from the
anchored APOE figures in §0 for the last):

```
 typical GWAS hit      per-allele OR 1.10, 0 -> 2 copies      1.8 pp
 strong GWAS hit       per-allele OR 1.50, 0 -> 2 copies      8.2 pp
 APOE e4/e4 vs e3/e3   lifetime to 85, male                  40    pp
```

That is a **23-fold span** from the typical GWAS hit to APOE. **A report that presents both in the
same visual register — same row height, same colour, same confident sentence shape — is actively
misinforming**, and that ratio is the whole reason this catalogue is tiered rather than listed.

---

## §2 Tier A — clinically actionable if confirmed

These can change medical management. **All of them require clinical-grade confirmation first**
(§0 anchor 1), and none should be reported as a result from raw data alone.

| Gene / variant | What it is | Typical grade | Action if confirmed |
| :--- | :--- | :--- | :--- |
| **HFE** C282Y (rs1800562), H63D (rs1799945) | Hereditary haemochromatosis risk alleles. C282Y homozygosity is the main genotype of interest; penetrance is incomplete and lower than early estimates implied. **H63D is c.187C>G — a palindromic C/G site**, so a homozygous call there cannot be oriented from the genotype alone | E1 / R1 (C282Y) · E1 / **R2** (H63D) | Iron studies (ferritin, transferrin saturation) — a cheap phenotype test that settles the question far better than the genotype does. This is the model case: the genotype's value is prompting a *measurement* |
| **F5** Factor V Leiden (rs6025) | Commonest inherited thrombophilia allele | E2 / R1 | Context for a clinician around thrombosis risk, surgery, oestrogen exposure. Does **not** by itself warrant anticoagulation |
| **BRCA1 / BRCA2** founder variants | Some platforms probe a small number of founder variants only | E1 / R3 | Confirmation, then genetics referral. **Critically:** a negative consumer result is near-meaningless here, because only a handful of thousands of possible variants were probed ([PMC10581610](https://pmc.ncbi.nlm.nih.gov/articles/PMC10581610/)) |
| **G6PD** deficiency variants | X-linked; causes haemolysis on oxidative triggers. **X-linkage is the whole interpretation, not a caveat:** a heterozygous female is an X-inactivation mosaic whose enzyme activity can land anywhere, and a genotype cannot say where | E1 / R2–R3 | A real contraindication list for specific drugs and foods (`pharmacogenomics.md` §4 names them). Confirm by quantitative enzyme activity — **better than genotype in hemizygous males and homozygous females, but NOT definitive:** heterozygous females often read normal despite a deficient red-cell population, and reticulocytosis or recent transfusion can falsely normalise anyone's result. A normal assay is not clearance |
| **Genes on a professional actionable-secondary-findings list** | A curated, versioned set of genes a clinical laboratory is advised to report back when doing exome or genome sequencing, even when unrelated to the original indication | E1 / R3 | **Read it for what it is: a laboratory *reporting* instrument, not an actionability filter.** It answers "what should a lab tell the ordering clinician?", not "what should this person act on?" — a distinction worth keeping, because treating it as a personal action list both over-reads it and misses actionable findings outside it. Name the instrument and its version rather than treating it as fixed |

**The HFE pattern generalises and is worth internalising:** the most useful genetic findings are
the ones that point at a cheap, decisive *phenotype* measurement. Iron studies for HFE, an enzyme
assay for G6PD — with the caveat above, which makes it the partial exception rather than the clean
case — a lipid panel for a lipid variant. The genotype earns its keep by prompting the
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
| **ALDH2** rs671 | Reduced aldehyde dehydrogenase activity; the flushing variant. Carries an established association with alcohol-related cancer risk, and the association is **drinking-stratified** — it is a gene-*environment* effect, not a standalone risk ([PMC2684609](https://pmc.ncbi.nlm.nih.gov/articles/PMC2684609/)). **Ship the direction and the stratification, not an odds ratio:** widely-quoted heterozygote ORs in the 3.7–18.1 range come from consumer-facing summaries, while a 31-study meta-analysis pooled a much lower heterozygote OR near 1.4 — a real discrepancy, and a number quoted from either end alone is indefensible | E1 / R1 | Genuinely actionable in one direction only: it strengthens the case for reducing alcohol. No supplement addresses it. Note the self-undermining fact: **flushing is itself a reliable marker, so asking the person beats genotyping them** |
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
([PMID 23288205](https://pubmed.ncbi.nlm.nih.gov/23288205)); the recommendation stood through a later
addendum, and **[PMID 32587351](https://pubmed.ncbi.nlm.nih.gov/32587351) is the correction notice
about that addendum rather than the addendum itself** — an earlier version of this file cited the
erratum as the amendment. The position is echoed by a call to action in the thrombosis literature
([PMC9175241](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175241/)), **a single-author commentary, so
"other professional bodies reached the same position" claimed more than that citation supports.** The
clinical-utility question has been revisited since
([PMC11288266](https://pmc.ncbi.nlm.nih.gov/articles/PMC11288266/)).
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

**Three further observations resolve "uniquely" only because ε1 was admitted**, and they deserve a
caution rather than a confident answer: `(C/C, C/T) → ε1/ε4`, `(C/C, T/T) → ε1/ε1`, and
`(C/T, T/T) → ε1/ε2`. Since ε1 is rare, **a genotyping error at one of the two sites is the likelier
explanation than a true ε1 haplotype** — so re-check both calls before reporting one of these. The
script resolves them and attaches that caution.

**Two technical facts worth carrying, because both are free checks:**

- **A strand flip at either APOE site is DETECTABLE.** Both sites are T/C, and the complement set
  A/G is disjoint from it — so an A or a G at either position is a parsing, mapping or
  strand-handling error, not a genotype, and must be refused rather than complemented into something
  plausible. This is the opposite of FTO rs9939609 (A/T), where the allele set equals its own
  complement and a flip cannot be detected at all (§1, R2).
- **The two sites are 138 bp apart in every build** — c.526 − c.388, both in exon 4 with no intron
  between them. The *spacing* is therefore build-independent and makes a free consistency check on a
  file's own coordinates; the *absolute* positions are build-specific and must be read from the
  file's header, never assumed. A different spacing means a row is mis-mapped.

**On actionability, be careful and be honest.** ε4 carries an established association with
Alzheimer's risk, dose-dependent between heterozygotes and homozygotes, and the absolute lifetime
figures are what matter — a relative multiple quoted alone is close to meaningless here. **This is
the one variant where this file carries anchored figures** (§0, carve-out): quote them as a range,
with the design named and the provenance grade attached, alongside the share of homozygotes who
reach 85 unaffected — and add whatever the live pass can actually resolve for this person's ancestry
and age (`risk-communication.md`). What makes APOE genuinely hard is that **no intervention has been shown
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
