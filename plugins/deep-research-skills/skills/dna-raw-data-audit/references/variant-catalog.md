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

**The rule cuts both ways, and one identifier has already come back.** `PMC3663356` was withdrawn
when a pass could not re-resolve it; a later search returned it **with its title**, so it is
restored in `interventions-evidence.md` — attached to what the title actually says, which is not
what the pass that named it claimed. **A withdrawal is provisional in the same way an identifier
is**, and the same search also showed that two *adjacent* DOIs at one journal
(`10.2340/00015555-0928` and `-1130`) are a naevus case letter and a nomenclature letter
respectively. **Adjacency is a reason to check, not a verdict either way.**

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
> **[p]** the figure came from search-result prose and **no identifier resolved for it at all** —
> the weakest grade here. A `[p]` figure is a placeholder for a number someone must still go and
> get, and **it does not reach a person.** **[calc from [p]]** correct arithmetic on unsourced
> inputs: the computation is checkable, the magnitude is not.

| Variant | Anchored figures | Grade |
| :--- | :--- | :--- |
| **HFE C282Y homozygosity** (rs1800562) | Documented iron-overload-related disease in **28.4% of male homozygotes (95% CI 18.8–40.2)** and **1.2% of females (95% CI 0.03–6.5)**, in 31,192 people of northern European descent aged 40–69 — Allen et al. 2008, *NEJM* 358(3):221–230 ([PMID 18199861](https://pubmed.ncbi.nlm.nih.gov/18199861/)). The sex asymmetry is the headline, and the female interval is very wide on few events | **[R/p]** |
| **F5 Factor V Leiden heterozygosity** (rs6025) | Two papers, two designs, and they must not be merged. **Retrospective family study** (Middeldorp et al., *Ann Intern Med* 1998;128:15–20, *"The incidence of venous thromboembolism in family members of patients with factor V Leiden mutation and venous thrombosis"*): first-event incidence **0.45%/year (95% CI 0.28–0.61)** in carrier relatives against **0.10%/year (0.02–0.19)** in non-carriers, **RR 4.2 (1.8–9.9)**, rising with age from about 0.25%/yr under 30 to about 1.1%/yr over 60. **Prospective cohort of asymptomatic carriers** (Middeldorp et al., *Ann Intern Med* 2001;135:322–327): **9 events in 1,564 observation-years = 0.58%/year**, and **0.26%/year for spontaneous events** — the authors concluded the absolute risk does not justify routine family screening. Cited by title against returned repository records; **no PubMed record was returned for either in this environment, so no PMID ships.** Systematic review: [PMID 19531787](https://pubmed.ncbi.nlm.nih.gov/19531787/) | **[R/p]** |
| ↳ *two withdrawn attributions, recorded so neither returns* | This row once cited `PMID 11583312`, which resolves to a **pooled case-control analysis reporting odds ratios** — a different study and a different estimand, incapable of supporting an annual-incidence claim. A verification pass then proposed attributing the 0.58%/1,564-observation-year figure to **Simioni 2002** (*Blood* 99:1938–42); **that is also wrong** — a re-source shows those are Middeldorp 2001's own numbers. Simioni 2002 exists and is a separate prospective cohort whose figures were not retrieved. **A proposed correction is a claim like any other and gets checked too** | — |
| ↳ *what that means over a horizon* | **These derive from figures that currently carry no identifier (row above), so they are shape, not magnitude — do not quote "96 of 100" to a person until the inputs are re-sourced, and note that the conclusion about anticoagulation rests on clinical guidance rather than on these two rates.** The arithmetic itself reproduces exactly and stands as a worked illustration. At 0.45%/yr vs 0.10%/yr: **10 years** 4.41% vs 1.00% (ARR 3.41 pp, 34 extra per 1,000, NNH ⌈1/0.0341⌉ = 30); **20 years** 8.63% vs 1.98% (ARR 6.64 pp, 66 extra per 1,000, NNH ⌈1/0.0664⌉ = 16). So **96 of 100 carriers are event-free at 10 years and 91 of 100 at 20** — which is why heterozygosity alone does not warrant anticoagulation. Note the relative risk *shrinks* with horizon (4.5 per-year → 4.43 at 10 years → 4.35 at 20) as both risks compound toward 1, so **state the horizon with the multiple** | **[calc from [p]]** — correct arithmetic on unsourced inputs. A `[calc]` grade asserts only that the computation is right; **it cannot launder the provenance of what went into it** |
| **APOE** (rs429358 + rs7412) | Lifetime Alzheimer's risk to age 85, from a semi-dominant model: **all-genotype population baseline 11% male / 14% female** (this is *not* the ε3/ε3 risk); **e3/e4 23% / 30%**; **e4/e4 51% / 60%** — Genin et al. 2011, *Molecular Psychiatry* ([PMC3162068](https://pmc.ncbi.nlm.nih.gov/articles/PMC3162068/), [10.1038/mp.2011.52](https://doi.org/10.1038/mp.2011.52)). **Quote these as the high end of a range, with the design named:** this analysis combined relative risks from case-control data with absolute risks from cohort studies, and cohort-based cumulative-incidence estimates over a fixed follow-up are generally **lower**, because they measure a different quantity than lifetime risk to 85. *(A specific percentage for that comparison was removed: it carried no identifier at all, and an unsourced number that revises a risk estimate **downward** is the most consequential kind in this file — it is the one a reader quotes as reassurance.)* Get the cohort figure from the literature at analysis time | **[R/p]** |
| ↳ *the dose effect, its complement, and the comparator trap* | e3/e4 is **+12 pp male / +16 pp female** over baseline (2.1×); e4/e4 is **+40 pp / +46 pp** (4.6× / 4.3×). Going from one e4 to two roughly **doubles** the heterozygote's absolute risk (2.2× male, 2.0× female). And on the same figures, **49 per 100 male and 40 per 100 female e4/e4 homozygotes reach 85 unaffected** — report that in the same breath, every time. **Critically: the 11%/14% baseline is the ALL-GENOTYPE population figure, so every multiple here is genotype-versus-population.** Published APOE relative risks are almost always computed against **ε3/ε3**, which is lower than the population mean because the population contains the ε4 carriers — so those multiples are larger and **are not comparable to these.** State the referent, or a reader will conclude one of the two sources is wrong | **[calc]** |

**Everything else in this file stays unfrozen.** The carve-out is three variants, not a precedent for
a fourth: it exists because these are the ones a person will insist on a number for, and because a
range with stated provenance beats both silence and invention.

### Anchors that are verified and stable enough to state

| Claim | Record |
| :--- | :--- |
| Direct-to-consumer raw data carries a materially elevated false-positive rate for rare variants, and clinical confirmation is required before action | **Population-scale, the strongest anchor:** [PMID 33589468](https://pubmed.ncbi.nlm.nih.gov/33589468/) / [PMC7879796](https://pmc.ncbi.nlm.nih.gov/articles/PMC7879796/) / [BMJ 2021;372:n214](https://www.bmj.com/content/372/bmj.n214) — roughly fifty thousand people with both chip and sequencing data; chips perform well on common variants and collapse in PPV on very rare ones. *(This row previously carried `PMID 33753354`, which resolves to nothing matching; the corrected ID was returned with the exact title in two independent searches. And the participant count is now approximate, because the precise figure is prose-sourced like the percentages this file declines to quote.)* **Clinical-laboratory series:** [PMID 29565420](https://pubmed.ncbi.nlm.nih.gov/29565420/) / [PMC6301953](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6301953/), with the published exchange around it — [PMID 29950595](https://pubmed.ncbi.nlm.nih.gov/29950595/) and [PMID 29955106](https://pubmed.ncbi.nlm.nih.gov/29955106/), **the latter authored from inside the company whose data was criticised, so cite it as a party's response and not as independent commentary** — and the public-health consequence [PMID 33113957](https://pubmed.ncbi.nlm.nih.gov/33113957/) |
| A professional society has addressed consumer disease-risk testing directly | [PMID 33399428](https://pubmed.ncbi.nlm.nih.gov/33399428/) |
| Third-party interpretation of DTC raw data carries its own burden of error | [PMID 29997392](https://pubmed.ncbi.nlm.nih.gov/29997392/) |
| DTC screening is limited for hereditary breast/ovarian cancer specifically | [PMC10581610](https://pmc.ncbi.nlm.nih.gov/articles/PMC10581610/) |
| Routine MTHFR polymorphism testing is advised against | [PMID 23288205](https://pubmed.ncbi.nlm.nih.gov/23288205) (practice guideline), with the recommendation standing through a later addendum the society lists by title; **[PMID 32587351](https://pubmed.ncbi.nlm.nih.gov/32587351) is the correction notice *about* that addendum, not the addendum** — do not cite it as the amendment. Echoed by a call to action in the thrombosis literature ([PMC9175241](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175241/), a single-author commentary — not a second society position), and the clinical-utility question has been revisited ([PMC11288266](https://pmc.ncbi.nlm.nih.gov/articles/PMC11288266/)) |
| CYP2D6 cannot be called reliably from array data: pseudogene similarity, CYP2D7 hybrids, CNV, and a phasing requirement | [PMC5591463](https://pmc.ncbi.nlm.nih.gov/articles/PMC5591463/), [PMC7997805](https://pmc.ncbi.nlm.nih.gov/articles/PMC7997805/) (WGS-based calling), [PMC7398905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7398905/) (callers disagree on structural variants), [PMC8881578](https://pmc.ncbi.nlm.nih.gov/articles/PMC8881578/) |
| Polygenic scores derived in predominantly European-ancestry cohorts transfer poorly, and the decline is continuous along genetic distance rather than stepwise between labelled groups | [PMC6563838](https://pmc.ncbi.nlm.nih.gov/articles/PMC6563838/) (Martin 2019) and its preprint [bioRxiv 10.1101/441261](https://www.biorxiv.org/content/10.1101/441261); [PMC5384097](https://pmc.ncbi.nlm.nih.gov/articles/PMC5384097/) (Martin 2017); [PMC8764121](https://pmc.ncbi.nlm.nih.gov/articles/PMC8764121/) with correction [PMC8874215](https://pmc.ncbi.nlm.nih.gov/articles/PMC8874215/) (Privé 2022 — strongest design, one cohort for training and testing); [10.1038/s41586-023-06079-4](https://doi.org/10.1038/s41586-023-06079-4) (Ding 2023); [10.1038/s41467-019-11112-0](https://doi.org/10.1038/s41467-019-11112-0) (Duncan 2019). `risk-communication.md` §4 has the table. Cite the dispute over magnitude, not one side |
| Family-ascertained penetrance exceeds population-based penetrance, with the gap narrowing in larger studies | [PMC2447846](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2447846/) (family-based; its title states the point), [PMID 11044354](https://pubmed.ncbi.nlm.nih.gov/11044354/) / [PMC2408797](https://pmc.ncbi.nlm.nih.gov/articles/PMC2408797/) (population-based), [PMID 25192939](https://pubmed.ncbi.nlm.nih.gov/25192939) (population screening — **counter-evidence in this row: it found population-ascertained risks comparable to family-ascertained ones**, in founder-variant carriers ascertained through healthy relatives), [PMID 16484695](https://pubmed.ncbi.nlm.nih.gov/16484695) (a large US series putting absolute cumulative risks at the lower end of the published range, with wide intervals) |
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

**Both axes assume a European-ancestry reference, and neither is portable without thought.** The
grades, allele frequencies and penetrance anchors in this file come predominantly from
European-ancestry cohorts. The consequence lands on the *reliability* axis, not only on the
risk numbers, and it is easy to miss:

- **A negative result at an ancestry-specific allele conveys almost nothing outside that ancestry.**
  F5 Factor V Leiden and HFE C282Y are both essentially European-ancestry variants, so "no Factor V
  Leiden" tells a non-European reader little about inherited thrombophilia.
- **A positive call at an allele that is rare in the person's ancestry is a rare-variant call**, and
  §0's PPV argument applies to it: effectively **R3 for that person**, whatever this file's row says.
  Reliability is a property of the assay *and* of the prior.

So read every R grade as "R-grade in a population where this allele is common", and downgrade it when
it is not. `risk-communication.md` §4 carries the portability arithmetic.

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
  **R2 marks the SITE as unorientable; it does not condemn every call at that site.** A
  heterozygote at a palindromic site carries one copy of each allele under either orientation, so
  its **dosage is unambiguous and the call is usable**; only a **homozygote** there is
  unresolvable. The sites in this catalogue verified as palindromic are **rs1799945** (HFE H63D,
  C/G — and it sits in the actionable tier) and **rs9939609** (FTO, A/T). The bundled script
  carries each known site's allele pair and grades the **call**: `CLEAR` for any heterozygote,
  `AMBIGUOUS` for a homozygote at a palindromic site, `UNDETERMINED` where the pair is not
  verified — see `data-formats-and-parsing.md` §2 for the worked table and for the two opposite
  errors the script had to shed.
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
 typical GWAS hit      per-allele OR 1.10, 0 -> 2 copies      1.77 pp
 strong GWAS hit       per-allele OR 1.50, 0 -> 2 copies      8.2 pp
 APOE e4/e4 vs POPULATION baseline, lifetime to 85, male     40    pp
```

That is a **22-fold span** from the typical GWAS hit to APOE (40 / 1.77). **A report that presents both in the
same visual register — same row height, same colour, same confident sentence shape — is actively
misinforming**, and that ratio is the whole reason this catalogue is tiered rather than listed.

---

## §2 Tier A — clinically actionable if confirmed

These can change medical management. **All of them require clinical-grade confirmation first**
(§0 anchor 1), and none should be reported as a result from raw data alone.

| Gene / variant | What it is | Typical grade | Action if confirmed |
| :--- | :--- | :--- | :--- |
| **HFE** C282Y (rs1800562) — **homozygous** | The genotype of interest in hereditary haemochromatosis. Penetrance is incomplete and lower than early estimates implied, and sex-asymmetric by more than an order of magnitude (§0 carries the anchored figures) | E1 / R1 | Iron studies (ferritin, transferrin saturation) — a cheap phenotype test that settles the question far better than the genotype does. **This is the model case: the genotype's value is prompting a *measurement*** |
| **HFE** H63D (rs1799945) | **Graded down deliberately, and it matters because this allele is common** (roughly one in ten European-ancestry chromosomes), so it fires on a large fraction of real files. **H63D homozygosity is not an established cause of clinically significant iron overload**, and C282Y/H63D compound heterozygotes develop iron-overload disease at low frequency; variant databases carry H63D as a risk factor rather than a penetrant allele. Presenting it in the same cell and at the same evidence grade as C282Y homozygosity is exactly the error §1's effect-size ladder warns about. **Also c.187C>G — a palindromic site**, so a *homozygous* call cannot be oriented from the genotype alone (a heterozygous one can; §1, R2) | **E3** / R2 | The same cheap action, which is the saving grace: iron studies. They cost little and settle either allele. **Do not report H63D as haemochromatosis** |
| **Familial hypercholesterolaemia** — LDLR and APOB founder variants | A monogenic cause of severe lifelong LDL elevation and premature cardiovascular disease, with an effective treatment. **Consumer platforms probe a handful of founder variants at most**, so a negative is close to meaningless and a positive is a rare-variant call (§0 anchor 1) | E1 / R3 | **A lipid panel, which is the measurement that matters and does not need the genotype at all** — then clinical confirmation and cascade testing of relatives if the lipids support it. This is the file's model pattern stated in §2 ("a lipid panel for a lipid variant"), and the catalogue previously carried no lipid variant to attach it to |
| **F5** Factor V Leiden (rs6025) | Commonest inherited thrombophilia allele | E2 / R1 | Context for a clinician around thrombosis risk, surgery, oestrogen exposure. Does **not** by itself warrant anticoagulation |
| **BRCA1 / BRCA2** founder variants | Some platforms probe a small number of founder variants only | E1 / R3 | Confirmation, then genetics referral. **Critically:** a negative consumer result is near-meaningless here, because only a handful of thousands of possible variants were probed ([PMC10581610](https://pmc.ncbi.nlm.nih.gov/articles/PMC10581610/)) |
| **G6PD** deficiency variants (the commonest probed are the two defining the A− haplotype, rs1050828 and rs1050829; many causal variants exist and most are not probed) | X-linked; causes haemolysis on oxidative triggers. **X-linkage is the whole interpretation, not a caveat:** a heterozygous female is an X-inactivation mosaic whose enzyme activity can land anywhere, and a genotype cannot say where | E1 / R2–R3 | A real contraindication list for specific drugs and foods (`pharmacogenomics.md` §4 names them). Confirm by quantitative enzyme activity — **better than genotype in hemizygous males and homozygous females, but NOT definitive:** heterozygous females often read normal despite a deficient red-cell population, and reticulocytosis or recent transfusion can falsely normalise anyone's result. A normal assay is not clearance |
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
| **APOE** | rs429358 + rs7412 (§7) | E1 / R1 | **ε4 dose stratifies ARIA risk with anti-amyloid monoclonal antibodies**, and the labelling for that class directs establishing ApoE ε4 status before treatment. Relevant only if that drug class is ever under consideration — and then it is decision-relevant, which is why APOE appears here as well as in §7. Check the current labelling rather than quoting this row |
| **CYP2C19** | rs4244285 (*2), rs4986893 (*3), rs12248560 (*17) | E1 / R1 for these SNPs | The common no-function and increased-function alleles are capturable; the diplotype inference still needs care |
| **CYP2C9** | rs1799853 (*2), rs1057910 (*3) | E1 / R1 | Pairs with VKORC1 for warfarin dosing algorithms — **and those two are not the whole set:** CYP4F2 (rs2108622) also feeds them, and rs12777823 matters specifically in African-ancestry patients, so a two-gene warfarin answer is ancestry-incomplete |
| **VKORC1** | rs9923231 | E1 / R1 | |
| **SLCO1B1** | rs4149056 (*5) | E1 / R1 | Statin myopathy risk |
| **TPMT** | rs1800460 (*3B), rs1142345 (*3C) | E1 / R1–R2 | Thiopurine dosing. **NUDT15 must be read alongside it** |
| **NUDT15** | rs116855232 (*3) | E1 / R2 | Particularly important in East Asian ancestry; omitted from older panels |
| **DPYD** | rs3918290 (*2A) and other no-function alleles | E1 / R2–R3 | Fluoropyrimidine toxicity. A *negative* result at one or two sites does **not** clear a person — several relevant alleles exist |
| **CYP2D6** | rs3892097 and others are present on arrays | **E1 / R4 — do not call** | Deletions, duplications, CYP2D7 hybrids and a phasing requirement place the diplotype beyond array data (§0 anchor). Report the limitation, not a phenotype |
| **RYR1 / CACNA1S** | **Not array-reachable, and the dash means that rather than "no site exists":** susceptibility rests on a long and growing list of variants across two large genes, consumer platforms probe few of them, and interpretation is specialist work. **The referral is the output** — a malignant-hyperthermia diagnostic service, before any planned anaesthetic | E1 / R3 | **The highest-acuity pair in the skill, and the one the person cannot raise in the moment** — malignant-hyperthermia susceptibility with volatile anaesthetics and succinylcholine. Consumer arrays probe few of the relevant variants and call rare ones poorly, so a flag is a prompt for diagnostic testing and a **pre-operative** conversation, and a negative is not clearance (`pharmacogenomics.md` §4) |
| **TPMT `*2`** | rs1800462 | E1 / R1–R2 | A further no-function allele; omitting it understates the callable set and how little a negative means |
| **CYP3A5 `*3`** | rs776746 | E1 / R1 | Tacrolimus. The sibling file calls this the cleanest array-callable case; expresser frequency differs greatly by ancestry, so ancestry changes what the result means |
| **MT-RNR1** | m.1555A>G | E1 / R3 | Aminoglycosides, irreversible hearing loss. **Some platforms genotype mitochondrial sites, so unlike most of this table it may actually be in the file** — heteroplasmy and platform-specific mtDNA handling make the call unreliable, so it is a prompt for proper testing |
| **UGT1A1 `*28`** | tag SNPs only | E1 / **R4** | Irinotecan. `*28` is a promoter TA-repeat, so an array carries a *tag*, not the allele (`pharmacogenomics.md` §2) |
| **HLA-A\*31:01** | **No rsID: an HLA allele is not a SNP.** Proper typing is the only route | E1 / R4 unless typed | Carbamazepine, in European and Japanese ancestry where `*15:02` is rare |
| **HLA-B\*58:01** | **No rsID**, same reason | E1 / R4 unless typed | Allopurinol — the third HLA pair, and strongly ancestry-dependent |
| **HLA-B** alleles (e.g. \*57:01, \*15:02) | — | E1 / R4 unless specifically typed | HLA typing is its own assay. Do not infer an HLA allele from array tag SNPs without validation evidence for that specific platform |

---

## §4 Tier C — carrier status and reproductive relevance

Heterozygous carrier status for recessive conditions is often the most genuinely useful output of
consumer data — and it is also where findings most clearly implicate relatives.

- Consumer platforms probe a **small, specific subset** of variants per condition. "Carrier status
  not detected" means only "none of the probed variants was seen", and for most recessive conditions
  that is a long way from clearance. Say so explicitly every time.
- **One worked example, because a tier with no named variant cannot be checked.** Cystic fibrosis:
  **CFTR F508del** is the commonest pathogenic variant in European-ancestry populations and is
  probed by consumer platforms — but over a thousand pathogenic CFTR variants are known, so a
  negative at F508del alone leaves most of the carrier probability untouched, and the residual
  depends on ancestry (`risk-communication.md` §5 computes it). *Named rather than cited: no rsID
  ships here because none was verified against a retrieved record in this environment.*
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
| **ALDH2** rs671 | Reduced aldehyde dehydrogenase activity; the flushing variant. Carries an established association with alcohol-related cancer risk, and the association is **drinking-stratified** — it is a gene-*environment* effect, not a standalone risk ([PMC2684609](https://pmc.ncbi.nlm.nih.gov/articles/PMC2684609/)). **Ship the direction and the stratification, not an odds ratio** — and note *why* the published figures differ, because it is not a dispute. The large odds ratios come from **drinking-stratified** analyses; a pooled estimate that does not stratify dilutes a gene–environment effect across non-drinkers in whom it is near-null. **They are not rival estimates of one quantity.** So quote a stratified figure with its stratum named, and **never a pooled figure to someone who drinks.** No figure ships here: this row sits outside §0's three-variant carve-out, and the pooled estimate carries no identifier | E1 / R1 | Genuinely actionable in one direction only: it strengthens the case for reducing alcohol. No supplement addresses it. Note the self-undermining fact: **flushing is itself a reliable marker, so asking the person beats genotyping them** |
| **MCM6 / LCT** rs4988235 | Lactase persistence regulatory variant | E1 / R1 | Explains a phenotype the person already knows. Dietary choice follows symptoms, not genotype |
| **CYP1A2** rs762551 | Caffeine metabolism | E3 / R1 | Weaker than marketed. Observed caffeine tolerance beats the genotype |
| **FTO** rs9939609 | Commonest BMI-associated locus | E2 / R2 (A/T site — strand-ambiguous) | **None.** The important finding is that it does not appear to blunt response to lifestyle intervention — so the advice is unchanged by genotype |
| **Common GWAS hits generally** | Per-allele odds ratios near 1 | E2–E3 / R1 | Individually uninformative. See `risk-communication.md` §1 |

---

## §6 Tier E — actively over-interpreted

Report these primarily to *correct* the interpretation the person has probably already encountered.

**MTHFR C677T (rs1801133) and A1298C (rs1801131).** The single most over-interpreted pair in
consumer genetics. A professional society advised against routine MTHFR
polymorphism testing on the grounds of minimal clinical utility
([PMID 23288205](https://pubmed.ncbi.nlm.nih.gov/23288205)); the recommendation stood through a later
addendum **which simultaneously reclassified the document from an evidence-based practice guideline
to a clinical practice resource** — the direction survived, its evidentiary standing was downgraded —
and **[PMID 32587351](https://pubmed.ncbi.nlm.nih.gov/32587351) is the correction notice
about that addendum rather than the addendum itself** — an earlier version of this file cited the
erratum as the amendment. The position is echoed by a call to action in the thrombosis literature
([PMC9175241](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175241/)), **a single-author commentary, so
"other professional bodies reached the same position" claimed more than that citation supports.** The
clinical-utility question has been revisited since
([PMC11288266](https://pmc.ncbi.nlm.nih.gov/articles/PMC11288266/)).
Grade **E5 / R1** — the genotype is called reliably; the interpretation industry built on it is the
problem. Report the guideline, not a methylfolate protocol.

**And name the measurement, because this file's own pattern offers one where the MTHFR section
otherwise stops at a refusal:** a **plasma homocysteine level** is the cheap, decisive test, and the
guidance cited above makes exactly that substitution — measure the phenotype rather than genotyping
the pathway. That is the same move as iron studies for HFE and an enzyme assay for G6PD. *(And see
`interventions-evidence.md` §4 for what follows if it is raised: the homocysteine-lowering trials
did not reduce myocardial infarction or mortality.)*

**"Detox", "methylation", and mitochondrial *haplogroup* or "mito-optimisation" panels.**
Collections of variants with mechanistic stories and no carrier-specific intervention evidence.
Grade E4 at best. The honest output is that no action follows.

**One exception, and it is not optional.** An earlier version of this item said "mitochondrial SNP
panels" without qualification, which would file the single highest-consequence mitochondrial finding
in the domain under "no action follows". **MT-RNR1 m.1555A>G is a genuine, guideline-level
aminoglycoside contraindication causing irreversible hearing loss, and some consumer platforms do
genotype mitochondrial sites** (`pharmacogenomics.md` §4); m.3243A>G is a second real variant. **A
mitochondrial panel is Tier E by default, not by rule — check for MT-RNR1 before dismissing it.**

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
to reduce the ε4-attributable increment in Alzheimer's *incidence*.** That makes it the clearest case
in the whole catalogue where the correct output is information and support for decisions the person
may want to make — planning, insurance, research participation, whether they wanted to know at all —
and *not* a supplement or peptide protocol. Any tool that answers an ε4 result with a stack
recommendation is selling something.

**But the flat claim "no intervention attaches to APOE" is now false, and the exception is the single
most actionable APOE fact available to someone who finds ε4/ε4 in raw data.** ε4 dose is the
principal risk stratifier for **amyloid-related imaging abnormalities (ARIA)** with the anti-amyloid
monoclonal antibodies: ARIA rates rise steeply with ε4 copy number, and the product labelling for
that class directs that ApoE ε4 status be established before treatment specifically to inform that
risk. That is a **carrier-specific, prescribing-relevant consequence** — so APOE has a
pharmacogenomic axis as well as a risk axis:

- **Alzheimer's incidence axis: E2 / R1** — established, called reliably, no intervention shown to
  change the outcome in carriers.
- **Pharmacogenomic axis (anti-amyloid mAb ARIA risk): E1 / R1** — an intervention decision that
  turns on carrier status. It is **only relevant if the person is ever considering that drug class**,
  which most are not, and the raw-data call still needs clinical confirmation first.

**No identifier ships with this axis**, and the disclosure matters in a file whose first sentence is
that every citation was verified against a retrieved record: the labelling is a living regulatory
document and none resolved to a retrieved record here. **Name the drug class and the labelling
section, and read the version in force at analysis time** rather than quoting figures from this file
(`pharmacogenomics.md` §4's rule).

**And non-carriage is not clearance:** ARIA occurs in ε4 non-carriers too, so ε3/ε3 changes the
*intensity* of the monitoring conversation, not whether it happens.

### ε2 exists, and a section headed "in full" has to say so

ε2 appeared nowhere in this section except inside the haplotype algebra, which leaves an ε2 carrier
to infer their own result from a discussion of ε4. Two things to report:

- **ε2 carriage is associated with *lower* Alzheimer's risk** than ε3/ε3. For someone who came
  looking for an ε4 answer, that is the finding, and omitting it is its own kind of mis-report.
- **ε2/ε2 has a lipid axis of its own.** It is the genotype underlying **familial
  dysbetalipoproteinaemia** (type III hyperlipoproteinaemia): a severe mixed hyperlipidaemia with
  premature atherosclerosis that responds well to lipid-lowering therapy. **Most ε2/ε2 people never
  express it** — penetrance is low and generally needs a second metabolic hit — so this is a
  *prompt*, not a diagnosis. Both defining SNPs are R1 and the script resolves ε2/ε2 directly.

So APOE carries a **third axis**:

- **Lipid axis — ε2/ε2 only: E2–E3 / R1.** The resolving action is a **fasting lipid panel**, which
  is §2's "the genotype's value is prompting a *measurement*" pattern exactly — the same shape as
  iron studies for HFE. §2 even names "a lipid panel for a lipid variant" without previously
  connecting it to the one APOE genotype that fits.

### When only one of the two sites is called

**A single-site APOE call is not a partial answer; it is no answer.** rs7412 alone cannot distinguish
ε4 from ε3, and rs429358 alone cannot distinguish ε2 from ε3 — which is why the haplotypes are
defined jointly. If one site is a no-call, or absent from a variants-only VCF, **report the
limitation rather than the likely diplotype.** The bundled script refuses here and says which site
failed; the honest sentence is "your APOE could not be determined from this file, and here is why",
not a hedged guess.

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
