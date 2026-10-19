---
name: dna-ancestry-research
description: >-
  Turns a genome into an evidenced ancestry story — reads 23andMe, AncestryDNA and Nebula Genomics
  results, calls Y-DNA and mtDNA haplogroups from chip data with open tools (HaploGrep 3, Yleaf),
  explains what vendor ancestry percentages actually measure, works DNA matches and records under
  the Genealogical Proof Standard (Shared cM, triangulation, WATO, endogamy), and draws lineage
  maps as SVG: dated haplogroup migration routes, composition shading, ancestor places and a
  pedigree chart. Researches and delegates on its own. Research only — a medical reading of the
  file is dna-raw-data-audit, and it never tests relatedness on people who did not consent. Use
  for where a family comes from, haplogroup questions, DNA-match puzzles, or mapping a lineage.
  Triggers: ancestry, heritage, haplogroup, Y-DNA, mtDNA, maternal line, paternal line, family
  tree, genealogy, DNA matches, shared cM, GEDmatch, lineage map, migration map, ethnicity
  estimate, genetic genealogy.
metadata:
  version: "1.0.0"
  source: >-
    Built from a five-stream research pass (genetic-genealogy standards and ethics; what the vendor
    reports measure; haplogroup origins, ages and migration; open callers and map data with their
    licences; Irish and US record sources), then validated by running both bundled scripts against
    a real chip export and two open callers. Provenance marks in the references follow the house
    legend: [snippet-only], [canon attribution], [background — verify], [unverified], [rule text].
---

# DNA ancestry research — genome to lineage, with maps

Takes what a person has — a chip export, a whole-genome result, a vendor's ancestry report, a
match list, a half-built tree, family stories — and turns it into three layers of ancestry, each
graded by what the evidence actually supports: **deep ancestry** (the Y-DNA and mtDNA lines, on a
scale of thousands of years), **population composition** (what the vendor's percentages mean, on a
scale of centuries), and **genealogy** (named people in records, within the last two hundred years
or so). Then it draws the maps that make the story legible and says, on each one, what is known,
what is inferred, and what is not known at all.

**The discipline this skill exists to enforce.** Ancestry reporting is where confident storytelling
outruns evidence fastest: a percentage becomes a nationality, a haplogroup becomes a tribe, a shared
segment becomes a named ancestor. Every claim here therefore carries its layer, its source, its
version, and its uncertainty — and the maps carry them too, in their footers, because a map
without its sources is the most persuasive wrong thing a person can be handed.

## When to use
- Someone has consumer DNA results (23andMe, AncestryDNA, MyHeritage, Nebula Genomics, FamilyTreeDNA
  or a YFull report) and wants to know where their family comes from, what their haplogroups mean,
  or how far the data can really take them.
- Someone wants their Y-DNA or mtDNA haplogroup called or checked from a chip file, or wants a
  vendor's call reconciled with another vendor's or with a sequencing result.
- Someone has DNA matches, shared-centimorgan figures or a GEDmatch kit and wants help working out
  how a match connects, or whether a hypothesis about a parent, grandparent or great-grandparent
  holds up.
- Someone wants a family tree built or extended from DNA plus records, with the proof standard
  applied, and the lineage drawn on a map or a pedigree chart.
- Not for: health, carrier, pharmacogenomic or risk questions about the same file →
  `deep-research-skills:dna-raw-data-audit` (that skill reads the genome as medicine; this one
  reads it as history, and the two must not blur). A clinical question with no genome in it →
  `deep-research-skills:medical-research-detective`. Checking whether a video's ancestry or
  genetics claims match its cited sources → `deep-research-skills:video-source-audit`. A statistics
  question with no genome attached → `data-analytics-bi-skills:statistical-inference`.

## Do it

Work the stages in order. Stage 1 is the only one that may not be skipped under any time pressure,
and several later stages can legitimately end with "the data cannot establish this".

1. **Set up privately, establish whose genome this is, and agree what will not be surfaced.** A
   genome identifies a person and every biological relative they have, none of whom consented to
   this analysis. Keep the raw file, and every file derived from it (the VCF, PLINK and genos
   outputs this skill writes, the caller reports, the maps with real names), outside any repository
   and any shared drive, and never paste genotypes into a third-party service. Before any file goes
   near version control run `git check-ignore -v <file>` and get a hit — the common genomic
   extensions are ignored in the repository this skill ships from, but that protection does not
   travel with the installed plugin, and the `.ped`, `.map` and `.genos.txt` outputs are not
   covered by most ignore files at all. Then ask three things before reading anything: **whose
   file is this** (if not the asker's, say what changes — the subject has not consented, findings
   about them are not the asker's to receive, and a minor's file gets no deep-ancestry surprises);
   **what should not be surfaced** (unexpected parentage, a specific branch, living relatives'
   details, a donor-conception question); and **what may leave the machine** (which maps and
   files, with what redaction). Record the answers in the tailoring file (see below) so a later
   session honours them without re-asking.

2. **Audit the plan for delegation before executing it.** List every step from inventory to
   delivery and mark who does it. The person's only jobs are consent, decisions and anything in the
   limits that stay with them (passwords, accounts, uploads to a matching site, purchases); every
   other step — file conversion, running the callers, the research, the records look-ups, the
   maps, the writing — is this skill's. If a delegation-audit skill is installed (in this
   library's author environment it is anthropic-skills:max-delegation-auditor), invoke it on the
   plan and adopt what it finds; otherwise run that audit inline: for each step the plan hands to
   the person, name the tool that could do it instead or the limit that forbids it. Bundle every
   consent the plan needs into one question rather than a drip of them.

3. **Inventory the inputs and run the summary before any call.** Collect what exists: the chip
   export (23andMe, AncestryDNA or MyHeritage layouts all parse), the whole-genome deliverables
   (Nebula's own haplogroup placement comes from YFull; the VCF or CRAM if the person has it), the
   vendor's ancestry report (composition with its **version**, genetic groups or recent-ancestor
   locations, the timeline, the haplogroup pages), match lists or GEDmatch kit numbers, any tree or
   GEDCOM, and the family's own knowledge. Then run the summary:
   ```
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-ancestry-research/scripts/haplogroup_inputs.py" summary "<raw.txt>"
   ```
   It reports the declared build, the MT, Y and X site counts and no-call rates, whether a Y
   chromosome is present at all, and which conversions are safe to run. A file that declares no
   build, or a build other than 37, stops here: positions are only meaningful against the build the
   file declares, and the converters refuse rather than guess (`references/haplogroups-and-deep-ancestry.md` §1).

4. **Call the deep-ancestry haplogroups with open tools, then review the calls.** Two licence-clean
   callers cover both lines; the exact recipes, install notes, tree versions and what each output
   column means are in `references/haplogroups-and-deep-ancestry.md` §2–4.
   - *mtDNA:* convert, then classify with HaploGrep 3 in chip mode, against PhyloTree 17.3 as
     distributed by HaploGrep, with the extended report and QC file on:
     ```
     python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-ancestry-research/scripts/haplogroup_inputs.py" mt-vcf "<raw.txt>" -o <private-dir>/chip_mt.vcf --sample me
     haplogrep3 classify --in <private-dir>/chip_mt.vcf --tree phylotree-rcrs@17.3 --chip --extend-report --write-qc --out <private-dir>/mt_report.txt
     ```
     The converter writes **every genotyped site**, reference calls included, because chip mode
     builds its coverage range from the sites present; an alt-only VCF makes the tool treat the
     rest of the molecule as unobserved and the quality score stops meaning what it says.
   - *Y-DNA (only when the summary says a Y chromosome is present):* convert to PLINK text and run
     Yleaf against more than one tree, so the names can be reconciled rather than trusted singly:
     ```
     python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-ancestry-research/scripts/haplogroup_inputs.py" y-plink "<raw.txt>" -o <private-dir>/chipY --sample me
     Yleaf -plink <private-dir>/chipY.ped -o <private-dir>/yleaf --reference_genome hg19 --tree yfull ftdna isogg
     ```
   - *Review both reports before quoting anything:*
     ```
     python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-ancestry-research/scripts/haplogroup_inputs.py" review <private-dir>/mt_report.txt
     python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-ancestry-research/scripts/haplogroup_inputs.py" review <private-dir>/yleaf/hg_prediction_combined.hg
     ```
     The review names the expected mutations the chip did not show and sorts them into **strand
     flips** (the chip called the complement base — a probe artefact, not a private mutation),
     sites not genotyped, and real discrepancies; it counts chip-only private mutations, which stay
     unconfirmed until a sequence agrees; and for Yleaf it says whether the trees agree on the
     terminal marker. Report each call with the tool, the tree and its version, the quality score,
     and the **depth limit**: a chip resolves a lineage only as far as its probes reach, so the
     honest form is "R-L21 — subclade unresolved by chip", never a deeper name borrowed from
     someone else's sequencing. Where a sequencing result exists (Nebula via YFull, Big Y, a full
     mitochondrial sequence), reconcile: the chip call should sit on the sequencing call's path,
     and a disagreement is a finding to explain, not a tie to break by preference.

5. **Read the vendor's ancestry report for what it measures, and restate every number in those
   terms.** A composition percentage is the share of the person's DNA segments assigned, by a
   classifier, to the reference population they most resemble, at a stated confidence, on a stated
   version of the panel — and the vendors re-draw the panels, so the same person's numbers move
   between versions without their ancestry changing. Genetic groups or recent-ancestor locations
   are a different layer (identity-by-descent matching to customers who report four grandparents
   from one place), framed by the vendors in the last two centuries; the timeline feature assumes a
   single ancestor per population; the relatives list has segment-length and SNP-count floors
   below which matches are suppressed; and a whole-genome vendor's autosomal breakdown may have no
   published panel at all. Translate each figure into "most similar to reference people from X, at
   this confidence, on version N", keep the version beside it everywhere it is quoted, and route
   anything about deep ancestry from the composition back to the haplogroup layer where it belongs.
   `references/vendor-reports.md` carries what each product does and the limits that bind it.

6. **Run the research pass, with a privacy brief.** The haplogroups, the places, the surnames and
   the record classes each need current literature and current record availability, and those
   move. If a deep-research coordinator skill is installed (in this library's author environment it
   is anthropic-skills:deep-research), invoke it with the question decomposed into: the origin,
   age, distribution and migration of each haplogroup, with dated nodes from the published clocks
   and ancient-DNA papers; the surname and regional history; the record classes that exist for the
   places and periods in play; and anything the vendor has changed since the report was issued.
   Otherwise spawn that fan-out yourself, three to five researchers in one turn. Either way the
   brief to every researcher carries **only haplogroup labels, surnames and places — never the
   file, never a genotype, never a match's name** — and every claim that comes back must resolve
   to a retrieved record and carry a provenance mark; a search tool's generated prose is not a
   source. `references/method-and-standards.md` §6 has the citation forms.

7. **Work the genealogical layer under the proof standard.** Seed an ahnentafel from what the
   person knows (a person n has father 2n and mother 2n+1), then for every link ask what record
   class would prove it and whether it has been seen — a civil or church register, a census, a
   land or probate record, a passenger or naturalisation file — and grade the link: proven by
   records, supported by DNA, hypothesised, unknown. For matches, use the Shared cM ranges to
   bound a relationship rather than name it, triangulate (three or more testers all matching each
   other on the same overlapping segment) before calling a segment ancestral, run the hypotheses
   through a probability tool such as WATO where a parentage or grandparentage question is open,
   and apply the endogamy adjustments where the population calls for them. Every answer to a
   match puzzle is a ranked set of hypotheses with the record that would settle each, not a name.
   Method: `references/method-and-standards.md` §1–5; sources: `references/records-and-documentary-research.md`.

8. **Draw the maps, each with its sources in the footer.** Use the bundled renderer, which draws
   exactly what the spec says and nothing it was not told:
   ```
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-ancestry-research/scripts/lineage_maps.py" map <spec.json> -o <private-dir>/<name>.svg
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-ancestry-research/scripts/lineage_maps.py" pedigree <persons.json> -o <private-dir>/pedigree.svg --redact
   ```
   Four maps carry the three layers: a **deep-ancestry map** with the Y and mtDNA routes as
   schematic lines between dated, sourced waypoints; a **composition map** shading the vendor's
   regions with the vendor's own numbers and version; an **ancestor-places map** of the documented
   people by line; and the **pedigree chart**. Keep the spec JSON beside each SVG so the map can be
   re-drawn when a source changes, and redact living people on anything that leaves the machine.
   `references/lineage-maps.md` has the spec recipes, the honesty rules for routes, and the data
   licence.

9. **Deliver in the fixed shape, and end on what would resolve the open questions.** Six sections,
   every time (the contract is below). The final section names the specific test or record that
   would answer each open question — a Y-sequencing test for the subclade, a full mitochondrial
   sequence for the private mutations, a parish register for an unproven link — and states, for
   any upload the person is weighing, what the receiving site does with the data and which
   matching settings they would be choosing. The person decides; this skill informs.

### Deliverable contract — six sections, every time
1. **Executive summary** — plain language; the three layers, what each established, and what none
   of them can tell this person.
2. **Deep ancestry** — each haplogroup call with tool, tree, version, quality and depth limit; the
   dated migration ladder with its sources; the deep-ancestry map.
3. **Population composition** — the vendor's figures restated with version, panel and confidence;
   genetic groups as a separate layer; the composition map; what moved between versions and why.
4. **Genealogy** — the ahnentafel with an evidence grade per link; match and segment analysis as
   ranked hypotheses; the pedigree chart and ancestor-places map.
5. **Research log** — every source retrieved, every claim's provenance mark, and every item that
   could not be verified, stated as unverified rather than smoothed over.
6. **Next steps and privacy** — the test or record that would resolve each open question; what was
   redacted or withheld and why; what in this report is safe to share and what names relatives.

### Hard rails
- **No relatedness test on a third party, and no volunteered family-structure inference.** The
  arithmetic for comparing two files is simple; the result can tell someone who is not in the
  conversation something irreversible. Decline the comparison, say why, and route to a genetic
  counsellor or a genealogist who handles unexpected results. If the data implies non-paternity,
  consanguinity or an unexpected parent, say such inferences are possible and ask whether the
  person wants them addressed at all — before, not after; and when asking is impossible, state
  the assumption and leave the inference unrun.
- **The exclusion list is honoured in full.** Ancestry findings have no clinical urgency, so there
  is no override: an excluded topic is noted as "a finding in an excluded category exists" and left
  there.
- **Living people are redacted on anything that leaves the machine**, and matches are never
  named to a researcher, a subagent or a third party.
- **A percentage is never an identity.** No composition figure makes someone a member of a nation,
  tribe or people; tribal and community membership rests on documented descent and the
  community's own rules, and the report says so when the question arises.
- **A haplogroup is never a story without a source.** "Viking", "Celtic", "Pictish" and their
  cousins are claims about dated populations; they attach to a lineage only through a published
  clock or ancient sample, cited, and otherwise stay out.
- **No upload of raw data anywhere without the person's explicit yes**, and every upload offer
  names the current terms, what the site keeps, and the law-enforcement matching setting the person
  would be choosing. The platforms' acceptance rules change; check the live page, never a memory.
- **Not a medical reading.** A health, carrier or pharmacogenomic question about the same file is
  routed, not answered.

## Why / learn

**Three layers, three clocks.** The Y chromosome and the mitochondrion pass down a single line
each, unmixed, so their mutations can be arranged on a tree with dated nodes — but the tree reaches
back thousands of years and says nothing about the other thousands of ancestors a person has at any
depth. Autosomal composition averages the whole genome against reference panels of living people
and so answers "whom do my segments resemble", at a resolution of roughly the last few centuries,
with no fixed boundaries: redraw the panel and the answer redraws. Identity-by-descent matching
finds specific shared segments and so reaches named people, but only inside the window where
segments survive recombination — a handful of generations. Each layer is honest at its own depth
and misleading when quoted at another's, which is why the report keeps them apart.

**Why a chip stops short.** A genotyping array interrogates a chosen few thousand Y and
mitochondrial sites. Any branch of the tree that no probe touches is invisible, so a chip-based
call lands at the last *probed* node on the person's path and the caller cannot see beyond it. The
same lineage sequenced lands deeper and acquires a different name on each tree — YFull, FamilyTreeDNA
and ISOGG each label nodes differently and sometimes split them differently — so reconciliation is
by terminal marker, not by label, and the tree and version are part of the result.

**Why rCRS, and why reference calls go in the VCF.** Consumer chips report mitochondrial positions
on the build-37 coordinate system, whose mitochondrial contig is the revised Cambridge Reference
Sequence; a caller that expects the reconstructed ancestral reference instead would mis-polarise
every variant. And a chip observes only its probed sites, so the caller must be told which sites
were seen: a VCF that lists only differences makes every unprobed site look like a reference call,
and the quality score rewards the silence.

**Why the vendor numbers move.** The composition classifier is trained on a reference panel of
people with four grandparents from one place, and the vendors add populations and retrain. A
person's segments do not change; which labelled neighbours they most resemble does. That is also
why two vendors disagree about the same person and why siblings' results differ: the segments they
inherited differ, and the panels differ. The version number is part of the number.

**Why the proof standard.** A shared segment has many possible explanations and a name attached to
one of them is not evidence of it. The Genealogical Proof Standard asks for a reasonably exhaustive
search, complete citations, analysis and correlation, resolution of conflicts, and a written
conclusion; the DNA-specific standards add that the test-takers, the data and the reasoning are
reported so another researcher can check them. Working that way is slower and produces fewer
named ancestors — and the ones it produces stay produced.

**Why relatives are the first consideration, not a footnote.** Every result here is also a result
about parents, siblings, children and cousins who did not ask. A Y-haplogroup is shared by a whole
paternal line; an unexpected-parentage finding changes someone else's life; a match's name is a
person's. The rails are the minimum that keeps a research tool from becoming a disclosure engine.

**Why the maps carry their sources.** A route drawn as a line looks like a path someone walked. It
is a sequence of dated, located nodes inferred from modern and ancient samples, with wide error on
both axes. The footer is where that difference lives; strip it and the map becomes the strongest
false claim in the report.

## Common mistakes
- Quoting a sequencing-depth subclade from a chip file → report the last probed node and say
  "subclade unresolved by chip".
- Classifying an alt-only VCF in chip mode → write every genotyped site; the converter does this.
- Treating a chip-only private mutation, or the complement of an expected mutation, as real → run
  the review; strand flips are artefacts, and private mutations wait for a sequence.
- Reading a composition percentage as nationality, tribe or "blood" → restate as resemblance to a
  reference panel at a confidence and version.
- Comparing two vendors' percentages as if they measured the same thing → different panels,
  different versions; compare the haplogroups and the matches instead.
- Naming a shared-match ancestor from one segment → triangulate, bound the relationship with the
  cM ranges, rank hypotheses, name the record that would settle it.
- Applying standard cM ranges to an endogamous population → lengthen the segment floor and
  recompute the totals as the method reference describes.
- Letting a researcher subagent see the file or a match's name → haplogroup labels, surnames and
  places only.
- Drawing a route without dates and sources, or a map of living people without redaction → the
  spec's notes field and the pedigree's `--redact` flag exist for exactly this.
- Writing the VCF, PLINK or genos outputs into a repository → they are the genome in another
  shape; keep them in the private directory.

## Tailor to your environment
Record in `references/your-environment.md`: which files you hold, their vendor, chip version and
declared build; any haplogroup result already received and the tree it was named on; the seed of
your tree in ahnentafel form; the surnames and places in play; which matching sites hold your kit
and what their matching settings are; the topics you do **not** want surfaced; who may receive
the report and with what redaction; and where the private working directory lives.

**The exclusion list is not optional.** Some findings cannot be unlearned and some implicate
relatives; decide before the analysis what you want to know.

**Keep your filled-in copy outside the plugin, and keep the genome outside it entirely.** This file
ships as a *template* inside the installed plugin, where a `/plugin marketplace update` can
overwrite it. Copy it to `.claude/skills-env/dna-ancestry-research.private.md` in your own project — and note
that **the `.private.md` suffix is what keeps it out of git — the plain `.md` form is NOT
ignored**, so confirm with `git check-ignore -v` before writing anything into it.

## References
- references/method-and-standards.md — the Genealogical Proof Standard and the DNA standards,
  Shared cM ranges and how to use them, triangulation, WATO, endogamy and pedigree collapse, what
  X, Y and mtDNA can each establish, ethics and law-enforcement matching, citation forms.
- references/vendor-reports.md — what 23andMe, AncestryDNA, Nebula Genomics (via YFull) and
  third-party calculators actually compute, their reference panels, versions, confidence levels
  and match thresholds, and how to restate each figure honestly.
- references/haplogroups-and-deep-ancestry.md — build safety, the HaploGrep 3 and Yleaf recipes
  with install notes, reading their outputs, tree naming and clocks, and how to build a dated
  migration ladder from published sources.
- references/records-and-documentary-research.md — Irish and United States record classes with
  where each lives and its known gaps, the platforms' current upload rules, and citation templates.
- references/lineage-maps.md — the map and pedigree spec recipes, which four maps to draw, the
  honesty rules for routes and shading, redaction, and the map-data licence.
- references/your-environment.md — the tailoring template (copy to the `.private.md` twin).

## Scripts
- `scripts/haplogroup_inputs.py` — `summary` (build, site counts, whether Y is present),
  `mt-vcf` (chip MT calls → rCRS VCF with every genotyped site, for HaploGrep 3 `--chip`),
  `y-plink` (chip Y calls → PLINK text for Yleaf `-plink`; refuses a file with no Y signal),
  `y-genos` (yhaplo layout, for anyone holding that tool under its own licence), `review` (screens a
  HaploGrep 3 extended report or a Yleaf combined table for strand flips, unobserved sites, private
  mutations and tree agreement). `--self-test` runs the offline checks; exit 2 unreadable input,
  3 unsafe (build or no-Y), 5 usage.
- `scripts/lineage_maps.py` — `map spec.json -o out.svg` (routes, points, shaded countries on
  bundled public-domain outlines), `pedigree persons.json -o out.svg [--redact]` (ahnentafel chart),
  `demo -o <dir>` (synthetic examples), `--self-test`.
