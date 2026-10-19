# Vendor ancestry reports — what each product computes, and how to restate it

Every number a vendor shows is the output of a method with a panel, a version and a threshold.
This file gives the method behind each product so the report can restate the figure in those
terms. Compiled from the vendors' own help pages, blogs and patents as reached through search
excerpts, plus the published method papers; marked accordingly, and re-read the live page for
anything the person will act on.

## Contents
- [§1 The ladder of resolution, and the phrasing rule](#1-the-ladder-of-resolution-and-the-phrasing-rule)
- [§2 23andMe](#2-23andme)
- [§3 AncestryDNA and MyHeritage](#3-ancestrydna-and-myheritage)
- [§4 Nebula Genomics and YFull](#4-nebula-genomics-and-yfull)
- [§5 Third-party calculators and QC-grade labels](#5-third-party-calculators-and-qc-grade-labels)
- [§6 Why vendors disagree, and why siblings differ](#6-why-vendors-disagree-and-why-siblings-differ)

## §1 The ladder of resolution, and the phrasing rule

Confidence falls as the claim gets finer, and the report should say which rung it is on:

| Rung | What it rests on | Robustness |
|---|---|---|
| Continental assignment | allele-frequency classifier against a large panel | robust across vendors |
| Sub-continental split (e.g. one European region vs another) | the same classifier on closely related panels | model- and version-dependent; moves between versions; vendors disagree by roughly ten to twenty-five percentage points on the same person [snippet-only] |
| County or district | identity-by-descent matching to customers who report four grandparents from one place | an IBD statistic about recent relatives, not a residence claim; validation unpublished |
| Named ancestor | records plus triangulated segments | only as good as the proof argument (`method-and-standards.md`) |

The phrasing rule, after the population geneticist Marcus Feldman: "thirty percent confident that
your DNA indicates ancestry from X" is not "thirty percent X" [snippet-only]. So a composition
figure is restated as *the share of this person's segments most similar to the vendor's reference
people from X, at this confidence, on version N*; a genetic-group result as *shares recent
relatives with customers who report roots in X*; and a timeline estimate as *the vendor's model
date under its single-ancestor assumption*. Keep the version beside the number everywhere.

## §2 23andMe

**Ancestry Composition** is a three-stage local-ancestry pipeline: a support-vector machine labels
each short, statistically phased window; a hidden Markov model corrects phasing errors and smooths
the labels; and isotonic regression recalibrates the confidence so that stated confidence matches
observed accuracy [canon attribution — Durand et al. 2014, and the vendor's own help article]. The
percentage shown is an aggregate of recalibrated per-window probabilities thresholded by the
confidence slider, so moving the slider changes the percentages without changing the genome.

The reference panel is built mainly from customers: the granted patent describes roughly
14,400 unrelated people across 45 populations, most of them research-consented customers, with
about 2,000 from public datasets [snippet-only — patent text]. The qualifying rule is four
grandparents born in one country; populations are hierarchical ("British & Irish" within
"Northwestern European" within "European"), and the vendor itself distinguishes regional
populations, which reflect ancestry several hundred years back, from the more recent country
matches [snippet-only].

**Versions move the numbers.** The September 2025 release ("Version 7") added dozens of European
and American populations, replaced the phasing pipeline, and removed the "Broadly" and
"Unassigned" categories from the default view; it reaches only customers on the current chip, and
updates for older chips stopped in 2020 [snippet-only]. Post-2025 percentages therefore look more
specific than earlier ones without the underlying data having changed — say so when comparing a
person's old and new reports. The only per-population accuracy figures located are old and the
quoting source warns they are out of sync with the current model [snippet-only].

**Genetic Groups (formerly Recent Ancestor Locations)** are a separate evidence type: exact
identity-by-descent matches against a reference set of customers of known ancestry, with a region
assigned when the customer matches a threshold number of reference people from it, strength
adjusted for reference size, framed by the vendor as roughly the last two hundred years
[snippet-only]. Tiers reported by third parties are "highly likely", "likely" and "possible" at
descending match proportions [snippet-only]. No independent validation of this layer was found, so
a county result is phrased as shared recent relatives, never as where a named ancestor lived.

**Ancestry Timeline** assumes all ancestry from a population came through a single ancestor,
ignores the X chromosome, does not update when a parent connects, and converts generations to
years with a fixed thirty-year generation [snippet-only — vendor help article]; against a
documented pedigree it placed an ancestor born in the eighteenth century in the early twentieth
[snippet-only]. Quote it, if at all, as the model's output under those assumptions.

**Neanderthal ancestry** is a count of variants from a vendor-maintained list, reported as a
percentile against other customers; the list changed with the chip, so the figure is comparable
only within one chip and report version [snippet-only].

**Haplogroups** on the vendor's pages are called with its own caller against an ISOGG Y tree
snapshot from early 2016 [snippet-only — vendor blog], and current reports name the terminal
marker directly; the open callers reproduce that call on the current YFull, FamilyTreeDNA and
ISOGG trees with the marker evidence on disk. The haplogroup reference has the recipes.

**DNA Relatives** detects a relative from one continuous shared region above a length and SNP
floor (documented as 7 cM and 700 SNPs), and the vendor states that the shared amount is only a
guide [snippet-only]; its relationship-prediction intervals for half-siblings, avuncular and
grandparental pairs overlap so heavily that it relies on self-reported ages to decide
[snippet-only]. The underlying method links identity-by-descent to kinship over roughly the last
one to three hundred years and found average sharing differs by orders of magnitude between
founder-effect and continental populations [canon attribution — Henn et al. 2012].

**Custody.** The company's recent history — a large credential-stuffing breach, a settlement with
mandatory two-factor authentication, bankruptcy and sale to a nonprofit, and multi-state
settlements preserving deletion and sample-destruction rights [snippet-only, cross-checked] — is
part of what a person weighing continued participation should hear. Relay the live privacy
statement, not a remembered one.

## §3 AncestryDNA and MyHeritage

AncestryDNA's composition splits some regions that other vendors merge (France and Germany, for
example), weights match totals with its Timber algorithm, and raised its match floor to 8 cM in
2020 [snippet-only]. Its tree-based match features and most shared-match views sit behind a
subscription tier [snippet-only — check the live product page]. MyHeritage reports one segment
floor for a match and shows further segments to a lower floor [snippet-only]. Neither vendor's
raw file parses differently for this skill's scripts — the AncestryDNA two-allele layout and the
MyHeritage quoted CSV are both accepted — but each vendor's **upload** rules are time-sensitive
and belong in the platform ledger of `records-and-documentary-research.md` §3.

## §4 Nebula Genomics and YFull

Nebula sells whole-genome sequencing with full Y-chromosome and mitochondrial coverage and
delegates the deep-ancestry analysis to YFull: customers transfer Y and mtDNA data, receive the
terminal Y haplogroup and tree position free, and pay to unlock the full report with SNPs, STRs
and matches; YFull's servers are stated to be in Russia [snippet-only — vendor blog]. No
reachable page documents the reference panel, algorithm, population count or confidence behind
Nebula's autosomal "ancestry breakdown", and a community source reports a change of laboratory
process after 2024 that may have reduced coverage [snippet-only — single unverified source].

**Rules.** Treat the YFull tree placement, with its tree version and date, as the citable deep-
ancestry artefact. Present any Nebula autosomal percentage as an unvalidated vendor estimate with
an unknown panel, and do not compare it numerically with another vendor's figure. Ask for the kit
date and the coverage stated in the QC report before relying on Y or mtDNA calls from a recent
kit. A whole-genome VCF can be classified directly by HaploGrep 3 for mtDNA (not in chip mode) and
by Yleaf for Y-DNA when the alignment or a suitable VCF is available; the haplogroup reference has
the recipes.

## §5 Third-party calculators and QC-grade labels

GEDmatch's admixture projects (Dodecad, Eurogenes, HarappaWorld and others) are hobbyist
supervised allele-frequency models whose calculator files date from blog and forum posts of
2011–2013; the site recommends calculators by ancestry type, not measured accuracy, and no
peer-reviewed validation of any of them was found [snippet-only, cross-checked]. Label them
"community-built, unvalidated heuristics", never use one as a tie-breaker, and never translate a
component name such as "North Atlantic" into an ethnicity.

A principal-components call against the 1000 Genomes samples (the kind a sequencing QC tool such
as peddy produces) yields a continental label: "nearest GBR" means proximity to a 91-person
British sample and "nearest CEU" to 99 Utah residents of northern and western European ancestry
[snippet-only]. It separates neither British from Irish nor either from Dutch or German, and is
reported as a QC label, never as an ancestry result.

## §6 Why vendors disagree, and why siblings differ

The cleanest evidence that disagreement is algorithmic rather than data-driven is a study of
identical twins tested at three companies: agreement of roughly 95–99% within a company but only
about 53–84% between companies [snippet-only — Huml et al. 2019], and a journalistic replication
found twins' raw data essentially identical while no two companies' results matched
[snippet-only]. Admixture-style outputs can produce misleading histories when a group deviates
from the model's assumptions, and identical bar plots arise from different demographic histories
[canon attribution — Lawson et al. 2018]. Full siblings legitimately differ because each inherits
a different recombined draw, so one can carry a distant ancestor's segment the other lacks.

Genuine fine structure exists in north-west Europe — haplotype-based studies resolve regional
clusters in Britain and divide Ireland into about ten clusters with a barrier in the north
[canon attribution — Leslie et al. 2015; Gilbert et al. 2017] — but it is subtle enough that an
allele-frequency classifier keeps "British & Irish" as one population and pushes finer claims
onto the identity-by-descent layer. Tribal and community membership rests on documented descent
and the community's own rules, never on a percentage [snippet-only — NHGRI].
