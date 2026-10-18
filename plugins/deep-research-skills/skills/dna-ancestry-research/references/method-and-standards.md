# Method and standards — DNA as one witness among several

How the genealogical layer is worked so that its conclusions survive a second researcher. The
figures here were compiled from secondary sources and search excerpts of the named pages; each
carries a provenance mark, and anything a conclusion will rest on should be re-read from the
primary page at the time of use.

## Contents
- [§1 The proof standard and the DNA standards](#1-the-proof-standard-and-the-dna-standards)
- [§2 Shared cM: ranges and probabilities are two different datasets](#2-shared-cm-ranges-and-probabilities-are-two-different-datasets)
- [§3 Segments: triangulation, floors, pile-ups](#3-segments-triangulation-floors-pile-ups)
- [§4 Endogamy and pedigree collapse](#4-endogamy-and-pedigree-collapse)
- [§5 What X, Y and mtDNA can each establish](#5-what-x-y-and-mtdna-can-each-establish)
- [§6 Citations and the research log](#6-citations-and-the-research-log)
- [§7 Ethics: consent, unexpected parentage, law-enforcement matching](#7-ethics-consent-unexpected-parentage-law-enforcement-matching)

## §1 The proof standard and the DNA standards

The Genealogical Proof Standard has five elements: a reasonably exhaustive search, complete and
accurate citations, analysis and correlation of the evidence, resolution of conflicting evidence,
and a soundly reasoned written conclusion [canon attribution — Board for Certification of
Genealogists]. "Exhaustive" is a test of variety, not volume: many documents of one type do not
satisfy it [snippet-only].

The second edition of *Genealogy Standards* (approved 2018, revised 2021) added DNA-specific
standards numbered 51 to 57, covering planning DNA tests, analysing results, the extent of DNA
evidence, sufficient verifiable data, integrating DNA with documentary evidence, conclusions about
genetic relationships, and respect for privacy [snippet-only, cross-checked]. Three of them shape
this skill's output directly, paraphrased rather than quoted because the standards' wording is
copyrighted:

- A genetic relationship is rarely proven by comparing just two samples (Standard 53).
- The write-up carries enough verifiable detail — testers, data, reasoning — for another
  researcher to check or dispute it (Standard 54).
- DNA conclusions are paired with documentary evidence, and every link in a line of descent from
  the common ancestor to a tester is itself a genealogical conclusion needing documentation
  (Standard 56) [snippet-only].

**What this means in practice.** The deliverable is a proof argument with a research log, not a
chart. Each ancestor link in the ahnentafel gets a grade — *proven by records*, *supported by
DNA plus records*, *hypothesised*, *unknown* — and a hypothesised link names the record class
that would prove it. A match analysis ends in ranked hypotheses, each with the record or test that
would settle it, never in a name presented as a result.

## §2 Shared cM: ranges and probabilities are two different datasets

The reference table for total shared autosomal DNA by relationship is the Shared cM Project,
version 4.0 (March 2020), built from roughly 60,000 crowd-sourced known relationships
[snippet-only, cross-checked]. Credit it as "Blaine T. Bettinger, The Shared cM Project v4.0
(March 2020)" with its licence as stated on the DNA Painter tool page at the time of use; the
project's licence wording has differed between an older project post and the current tool page,
so read the live page rather than relying on either [snippet-only].

Figures as reported by secondary sources citing v4.0 (observed ranges after the project's outlier
handling; averages differ slightly between sources):

| Relationship | Average cM | Observed range cM |
|---|---|---|
| Parent / child | ~3,485 | 2,367–3,720 |
| Full sibling | ~2,613 | 2,209–3,384 |
| Half sibling; grandparent; aunt/uncle; niece/nephew (pooled) | ~1,750 | 1,160–2,436 |
| First cousin | ~866 | [unverified — range not confirmed] |
| First cousin once removed; half first cousin | ~433 | 102–979 |
| Second cousin | ~229 | 41–592 |
| Third cousin | ~73 | 0–217 |
| Fourth cousin; third cousin once removed | ~35 | 0–127 |

All rows [snippet-only, cross-checked]. Two consequences follow from the pooled row: a half
sibling, a grandparent and an aunt or uncle are indistinguishable by total cM alone, and the
tie-breakers are ages, X-sharing, and which other relatives match.

**The probabilities are a different thing.** The percentages the DNA Painter tool and *What Are
The Odds* (WATO) attach to a cM value were not computed from the crowd-sourced ranges; they were
digitised from a figure in AncestryDNA's matching white paper and describe Ancestry's simulations
[snippet-only]. So keep two columns in any write-up — "observed range (crowd-sourced v4.0)" and
"probability (Ancestry simulation via DNA Painter)" — because they answer different questions and
fail differently. WATO scores every hypothesis relative to the least likely one, which is always
1, so scores mean something only within one chart; later versions offer alternative probability
sets, and the tool has limited application to double cousins, three-quarter siblings and
endogamous matches [snippet-only]. Two further cautions: AncestryDNA's Timber algorithm
down-weights totals below about 80 cM, so an Ancestry total is not directly comparable with
another vendor's [snippet-only]; and the self-reported relationships behind the ranges can be
misidentified, which is why the ranges are wide.

## §3 Segments: triangulation, floors, pile-ups

A triangulated group is three or more testers who all match each other on the same overlapping
segment. Overlapping segments in a chromosome browser are not triangulation until every pair has
been checked at that location, and a shared-match list proves nothing about segments at all
[snippet-only, cross-checked]. Even a confirmed group shows only that the segment descends from
one ancestral couple — not which ancestor, and not how far back.

Small segments are mostly false. A trio-based study of roughly 25,000 genotyped Europeans found a
false-positive rate above 67% for segments of 2–4 cM, nearly all from phasing switch errors
[snippet-only — Durand et al. 2014]; AncestryDNA raised its floor from 6 to 8 cM in 2020 after
its own concordance test found about a fifth of 6 cM segments false [snippet-only]. Those two
figures come from different companies, chips and pipelines, so they describe a steep curve rather
than interchangeable constants. Vendor floors as documented (mostly older than 2024 — read the
live help page at the time of use): about 8 cM after Timber at Ancestry; 7 cM and 700 SNPs at
23andMe; one 8 cM segment at MyHeritage; 7 cM and 700 SNPs at GEDmatch, lowerable by the user;
and at FamilyTreeDNA at least one segment of 9 cM when the total is under 20 cM [snippet-only].

Pile-up regions — stretches with excess identity-by-descent across the population — produce
false relationships; one study reported a ten-fold increase in false positives among controls,
and a worked example on chromosome 22 spans roughly 16–25 Mb on build 37 [snippet-only]. Segments
of 7–15 cM are the band most exposed to imputation and pile-up effects [snippet-only].

**Operating rules.** Build candidate groups from shared matches, then confirm every pairwise
overlap. Ignore segments below the vendor floor and treat 7–15 cM segments as needing
corroboration. Check a candidate segment against known excess-IBD regions before relying on it.
Phase against a tested parent whenever one exists. And record the vendor, its floor and whether
the cM figure is weighted beside every number.

## §4 Endogamy and pedigree collapse

In an endogamous population, or after a cousin marriage, descendants inherit identical segments
through more than one path, so totals inflate and predicted relationships come out closer than the
documentary one. The warning sign is heavy overlap among match groups. The practical adjustments
are to rank matches by **longest segment** rather than total, prioritising 20 cM or more (a 23 cM
segment is the suggested floor for a traceable link in Ashkenazi lines), to ignore segments under
about 10 cM when totalling, and to recompute totals at a higher threshold before consulting the
ranges — excluding segments under 7 cM can halve a total [snippet-only, cross-checked]. Say in the
report which adjustment was applied and why.

## §5 What X, Y and mtDNA can each establish

- **Y-DNA** follows the paternal line only. It can show two men share a paternal ancestor and can
  exclude a shared paternal line outright; it never identifies which ancestor. A chip types a fixed
  panel of known SNPs (one chip is described as about 3,000 Y-SNPs) and resolves a lineage only to
  the last probed node; a sequencing test discovers new branch-defining SNPs and resolves to the
  genealogical era, roughly one new SNP per 150 years by one estimate [snippet-only]. Surname
  projects commonly require a positive SNP test or a 111-marker STR panel before accepting a
  member into a named lineage [snippet-only].
- **mtDNA** follows the maternal line only. A match on the control regions alone says only that a
  common maternal ancestor exists within about 28 generations; an extensive mismatch excludes a
  shared maternal line with some confidence. Only a full sequence (all 16,569 positions) has
  genealogical resolution, and even an exact full-sequence match carries only about a 50% chance
  of a common maternal ancestor within roughly five generations, a figure practitioners call
  optimistic [snippet-only].
- **X-DNA** has an inheritance pattern that excludes whole branches (a man's X comes only from his
  mother), so a sizeable X match constrains which lines are possible; the absence of an X match
  proves nothing. Vendors treat it differently — one includes X in totals, one counts an X match
  only when the pair also match elsewhere, one reports it separately — so name the vendor beside
  any X figure [snippet-only].

Use the uniparental markers as **exclusion tests first**: a Y or mtDNA mismatch kills a hypothesis
cheaply, and a match merely keeps it alive.

## §6 Citations and the research log

DNA "is just another form of evidence": cite the actual report or database view consulted, and
keep the proof argument separate from the citation [canon attribution — Elizabeth Shown Mills,
*Evidence Explained*]. The current edition is the fourth (2024), which added a chapter on building
citations from components [snippet-only]. For anything viewed online use the **layered citation**:
one layer for the original record as the image shows it, one for the website or database that
delivered it, and an optional "citing" layer for what the provider says about the original's
location [snippet-only — QuickLesson 19]. Keep the "citing" layer whenever the provider's film or
register number is the only way back to the original. Because match data are visible only to the
tester, a DNA citation must carry enough detail for a reader who cannot see the match list to
judge the conclusion. Auto-generated citations from record sites sometimes name the wrong person
on a page or drop the URL — check them, never paste them [snippet-only].

**Minimum research-log fields** (synthesised from the standards above): objective and hypothesis;
privatised tester and match identifiers; company or upload site and the date viewed; total cM,
longest segment, segment count and X status; chromosome coordinates for any triangulated segment;
the vendor floor and whether the cM figure is weighted; the shared-match cluster; a documented
line of descent with a citation at every link; the Shared cM range and probability consulted with
the tool version; WATO hypotheses and scores; conflicts and their resolution; consent status; and
every negative search.

## §7 Ethics: consent, unexpected parentage, law-enforcement matching

**Consent.** The revised Standard 57 requires publishing personally identifying information about
living test-takers only with their informed consent, and the code of ethics adds that a match list
is not shared privately without the list owner's consent [snippet-only, cross-checked]. The
community's Genetic Genealogy Standards hold that testers own their results and raw data even when
someone else paid, and that presenters privatise or redact living matches' names [snippet-only].
This skill's rule — living people redacted on anything that leaves the machine, matches never
named to a subagent or third party — is the operational form of those standards.

**Unexpected parentage** is a planning item, not an edge case: cited per-generation rates range
from 1–2% to 2–12% depending on population and method [snippet-only — both figures from secondary
sources, neither verified against a primary study], and with autosomal matching alone such events
often go undetected a few generations back. The convergent procedure: verify first on multiple
matches from both sides; pause before any contact; let the affected person choose the terminology
and control disclosure; publish nothing identifying living people. Donor conception raises the
stakes because consumer testing can remove donor anonymity at any stage of a person's life, and at
least one US state has ended anonymous gamete donation on exactly that reasoning [snippet-only].

**Law-enforcement matching differs by database, and the setting is the person's choice.** Record
the date and the setting read. As documented from the sites' own pages (re-read at the time of
use): GEDmatch is strictly opt-in, with opt-in defined as matching against all kits including
law-enforcement kits, and it has acknowledged a period in which some practitioners circumvented
user settings in breach of its terms [snippet-only, cross-checked]; FamilyTreeDNA defaults new
accounts out of its investigative matching feature, with a toggle in the privacy settings
[snippet-only]; AncestryDNA requires a court order or warrant and publishes a transparency report
[snippet-only]; 23andMe's relatives feature is opt-in and research participation is revocable
[snippet-only]. A legislature can also constrain forensic use (one US state regulated it in 2021)
[snippet-only]. The skill explains these as choices and their consequences; it never sets them.

**Custody history is part of the disclosure.** A vendor's breach, bankruptcy or change of owner
changes who holds the data and under what obligations; relay what the live privacy statement says
on the day, including the person's deletion and sample-destruction rights, rather than a
remembered version.
