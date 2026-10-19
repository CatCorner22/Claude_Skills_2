# Haplogroups and deep ancestry — calling from chip data, reading the calls, dating the ladder

The uniparental lines are the one place a consumer file supports a precise, reproducible claim —
provided the claim is made at the depth the data reaches and named on a stated tree. This file
gives the recipes, what every output column means, and how to build a dated migration ladder
from published sources. The recipes were run end to end while building this skill (HaploGrep 3
version 3.3.2; Yleaf 4.1.5) on a real chip export; the ages and distributions in §5 come from
secondary sources and search excerpts and carry provenance marks.

## Contents
- [§1 Build safety and the reference question](#1-build-safety-and-the-reference-question)
- [§2 mtDNA with HaploGrep 3](#2-mtdna-with-haplogrep-3)
- [§3 Y-DNA with Yleaf](#3-y-dna-with-yleaf)
- [§4 Trees, names and clocks](#4-trees-names-and-clocks)
- [§5 Building a dated migration ladder](#5-building-a-dated-migration-ladder)
- [§6 Reporting rules](#6-reporting-rules)
- [§7 Other tools and their licences](#7-other-tools-and-their-licences)

## §1 Build safety and the reference question

A chip export lists positions on one genome build, declared in its comment header. The bundled
converter requires a declared **build 37** (GRCh37 / hg19) because its mitochondrial reference and
Yleaf's hg19 marker tables are build 37; a build 36 or 38 file, or a file whose header has been
stripped, is refused rather than guessed, because a position looked up against the wrong build is
a different variant with no warning.

For mitochondrial DNA the build-37 contig **is** the revised Cambridge Reference Sequence (rCRS,
NC_012920.1, 16,569 bases), so a chip's mitochondrial calls are differences from rCRS and the
classifier must use an rCRS-based tree. The alternative reference, the Reconstructed Sapiens
Reference Sequence (RSRS), is an inferred ancestral sequence; classifying rCRS-polarised calls
against an RSRS tree mis-polarises every variant [snippet-only, cross-checked]. The converter
ships `assets/rCRS_NC_012920.1.fasta` (a public-domain NCBI RefSeq record, copied from an
MIT-licensed tree repository) and checks its length and checksum before use.

## §2 mtDNA with HaploGrep 3

**Install.** HaploGrep 3 is MIT-licensed and needs Java 11 or later [snippet-only]. Download the
release archive (`haplogrep3-<version>-linux.tar.gz`) from the project's GitHub releases page,
unpack it, and run `./haplogrep3 trees` to see which trees are present; the archive tested here
carried `phylotree-rcrs@17.3`, and `./haplogrep3 install-tree phylotree-rcrs@17.3` adds it when it is missing. Say
"PhyloTree 17.3 as distributed by HaploGrep" in the report — the 17.x point releases are the
distributor's maintained corrections to the 2016 Build 17, not new upstream builds [snippet-only].

**Convert and classify.**
```
python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-ancestry-research/scripts/haplogroup_inputs.py" mt-vcf "<raw.txt>" -o <private-dir>/chip_mt.vcf --sample me
haplogrep3 classify --in <private-dir>/chip_mt.vcf --tree phylotree-rcrs@17.3 --chip --extend-report --write-qc --out <private-dir>/mt_report.txt
python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-ancestry-research/scripts/haplogroup_inputs.py" review <private-dir>/mt_report.txt
```
The converter writes **every genotyped site** — reference calls as `GT 0` with an empty ALT,
differences as `GT 1` — because in `--chip` mode the classifier builds the sample's coverage range
from the sites present. Tested on the same export both ways: with every genotyped site listed the
range was the genotyped positions and the quality score rose, because expected mutations at
unprobed positions no longer counted against the sample; without `--chip` the range became the
whole molecule and every unprobed expected mutation was scored as missing. Duplicate probes at one
position collapse to one row when they agree and are dropped when they conflict; indel codes and
heterozygous-looking calls are dropped and counted.

**Reading the extended report** (tab-separated, one row per sample):

| Column | Meaning |
|---|---|
| `Haplogroup`, `Rank`, `Quality` | best hit, its rank, and the score (0–1). The QC file warns below 0.9 [observed, 3.3.2]. |
| `Range` | the positions the classifier treated as observed — in chip mode, the genotyped sites |
| `Not_Found_Polys` | mutations the haplogroup expects that the sample does not show **inside the range** — the list to screen |
| `Found_Polys` | expected mutations present |
| `Remaining_Polys` | sample mutations the tree does not expect, each tagged global or local private mutation |
| `AAC_In_Remainings` | amino-acid changes implied by the private mutations (gene and codon) |
| `Input_Sample` | the sample's full difference list from rCRS |

**What the review does with it.** For each expected-but-absent mutation it checks the sample's
own call at that position: if the chip called the **complement** base (A for T, C for G) the probe
reported the other strand and the "missing" mutation is an artefact; if the position is absent,
it was not genotyped or was called reference; anything else is a real discrepancy. It also counts
the private mutations, which on a chip are unconfirmed until a sequence agrees. State the call as
"<haplogroup> on PhyloTree 17.3 (HaploGrep), quality <q>, <n> expected sites not seen of which
<k> are strand artefacts, <m> chip-only private mutations", and add "subclade unresolved by chip"
unless a sequencing result places the person deeper.

**Whole-genome input.** A sequencing VCF of the mitochondrial contig classifies without `--chip`
(absent sites then mean reference, which is true for a complete sequence); keep the `--hetLevel`
default unless heteroplasmy is the question. Where the person already holds a sequencing-based
call (a vendor's full-sequence result, or YFull's placement for a whole genome), the chip call
should sit on that call's path; a disagreement is a finding to explain.

## §3 Y-DNA with Yleaf

**When.** Only when the summary reports a Y chromosome present. The converter refuses a file whose
Y sites are essentially all no-calls, which is what a person without a Y chromosome produces.

**Install.** Yleaf is GPL-3.0 (Erasmus MC) [snippet-only, licence file read]. The project ships
installers and a portable package on its releases page; from source, clone the repository, install
`numpy`, `pandas`, `networkx` and `graphviz` (the Python package), and run it as
`python3 -m yleaf.Yleaf` from the clone's root directory. Its PLINK mode reads the bundled marker
tables and needs neither `bcftools`, `samtools` nor a reference genome — but the program's
start-up check still asks for one and offers to download hg19 (about 3 GB). On a machine that is
online, let it, once. Offline, pass `--ref-fasta` pointing at a small placeholder FASTA whose only
contig is **not** named `chrY` or `Y`, with a pre-built `.fai` beside it; the version tested skips
build validation for such a file and never reads sequence in PLINK mode. Add `--no-update-check`
so a run on a private machine makes no network call [snippet-only, confirmed in the help text].

**Convert and run.**
```
python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-ancestry-research/scripts/haplogroup_inputs.py" y-plink "<raw.txt>" -o <private-dir>/chipY --sample me
Yleaf -plink <private-dir>/chipY.ped -o <private-dir>/yleaf --reference_genome hg19 --tree yfull ftdna isogg --no-update-check
python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-ancestry-research/scripts/haplogroup_inputs.py" review <private-dir>/yleaf/hg_prediction_combined.hg
```
Run more than one tree. The trees differ in how they name and sometimes split nodes, so the honest
comparison is by **terminal marker**, which the review reports; where the marker agrees and the
labels differ, the labels are synonyms and the report lists them together.

**Outputs.** `hg_prediction_combined.hg` has, per tree, the haplogroup, its terminal marker, the
number of valid markers and a QC score (0–1, from three sub-scores); the per-tree `.hg` files
repeat this; the per-sample `<id>.<tree>.out` table lists every marker the chip touched with its
ancestral and derived bases, the called base and a state (`A` ancestral, `D` derived, `NC` no
call); `haplogroup_path_<tree>.json` is the path from the root to the terminal node with each
node's state — the direct source for a migration ladder, because it shows which nodes the chip
actually observed; `report.<tree>.json` is the machine-readable summary; `.info` gives the marker
accounting. An example run on a current 23andMe export observed about two thousand markers with
haplogroup information and landed on the same terminal marker the vendor's own report named —
which is the point of the exercise: an independent, reproducible call on three current trees,
with the marker evidence on disk, rather than a label taken on trust.

**Depth.** A chip resolves to the last probed derived node. Report "<label on each tree>
(terminal marker <M>) — subclade unresolved by chip", and name the sequencing test that would
resolve deeper (a Y-sequencing product; or a whole genome, whose YFull placement is then the
citable artefact).

## §4 Trees, names and clocks

- **Three Y trees, three label systems.** YFull labels nodes by a representative SNP (`R-Y21048`),
  FamilyTreeDNA by a different representative SNP for what may be the same node, and ISOGG by a
  long-form lineage string; synonyms abound (one SNP can carry a project name and a company name).
  The node is the fact; the labels are addresses. Give the terminal marker and every label.
- **Two kinds of age.** YFull publishes *formed* (when the branch split from its parent) and
  *TMRCA* (the most recent common ancestor of its sampled living members); FamilyTreeDNA Discover
  publishes a most-likely TMRCA with a 95% interval. Intervals of roughly ±30% are normal for
  Y-SNP ages [snippet-only]. Report the estimate, the source, its date and the interval where one
  is published; never one bare number.
- **mtDNA has two clocks that disagree on scale.** Phylogenetic (maximum-likelihood) ages date a
  haplogroup's *formation* — for haplogroup T's branches, tens of thousands of years [canon
  attribution — Pala et al. 2012]; genealogical clocks (FamilyTreeDNA, YFull) date the
  *coalescence of sampled living lineages* — thousands of years for the same branches
  [snippet-only]. The difference is methodological, not a contradiction; report both and say
  which is which.
- **Tree versions are part of the result.** PhyloTree 17 is dated 2016 with maintained point
  releases; YFull's tree is versioned and dated on each page; FamilyTreeDNA's tree is continuous;
  ISOGG's snapshot date matters because callers bundle old ones. A newer tree can change the
  label without changing the person.

## §5 Building a dated migration ladder

A ladder is a table of nodes from a deep ancestor to the terminal call, each with an age, its
source, the dated evidence that places it somewhere, a plotting region, and a confidence. The
route on the map is drawn from this table and nothing else.

| Column | What goes in it |
|---|---|
| Node | the tree node (terminal marker and labels) |
| Age | formed / TMRCA with source and date read; or the phylogenetic age for mtDNA, labelled |
| Dated evidence | an ancient sample or a published migration finding that places the node in time and space, cited; or "none — modern distribution only" |
| Plotting region | a place and approximate coordinates, labelled as the author's plotting approximation |
| Confidence | high (ancient samples on the node), medium (ancient samples on a parent node plus modern distribution), low (modern distribution only) |

**Worked macro example, paternal, for a lineage under R-L21** (two-thirds of Irish men and over a
third of British men carry L21, so this example identifies no one [snippet-only]):

| Node | Age (YFull, 2026 tree) | Dated evidence | Plot | Confidence |
|---|---|---|---|---|
| R-M269 | formed ~13,300 / TMRCA ~6,400 ybp | all seven Yamnaya males in one landmark ancient-DNA study carried M269; westward spread after ~3000 BCE | Pontic–Caspian steppe, ~48°N 40°E (origin debated) | medium [canon attribution — Haak et al. 2015] |
| R-L151 → R-P312 | ~5,500/4,800; ~4,800/4,500 ybp | Beaker-associated men overwhelmingly R1b-M269 | central Europe ~50°N 10°E to the Lower Rhine ~52°N 5°E | medium [canon attribution — Olalde et al. 2018] |
| R-L21 | ~4,500/4,500 ybp | the Beaker migration replaced most of Britain's earlier gene pool from ~2450 BCE | Wessex ~51.2°N 1.8°W | medium [snippet-only — Olalde et al. 2018 via secondary sources] |
| L21 in Ireland | — | three Early Bronze Age men from Rathlin Island, ~2026–1534 cal BCE, all R-L21 with steppe ancestry | Rathlin ~55.3°N 6.2°W | high for presence, low for route [canon attribution — Cassidy et al. 2016] |
| below L21 | per node from YFull / FTDNA | usually none — insular expansions without ancient samples on the node | the documented nineteenth-century county, as a proxy: movement within Ireland was limited until the mid-nineteenth century [snippet-only — Irish DNA Atlas] | low |

All ages [snippet-only — YFull pages via secondary sources]; coordinates are plotting
approximations. A later migration into southern Britain in the early first millennium BCE is an
autosomal finding about Britain, not a Y-lineage route into Ireland, and does not belong on this
ladder [canon attribution — Patterson et al. 2022].

**Worked macro example, maternal, for haplogroup T1:** origin of T1 and T2 in the Near East about
21,000 years ago with Late Glacial dispersals 19–12 thousand years ago; T1a1 holds about 80% of
T1 at roughly 15,500 years [canon attribution — Pala et al. 2012]; Early Neolithic European
presence in Starčevo-Criş Romania and the LBK at Karsdorf, Germany; Bronze Age presence on the
Samara steppe [snippet-only — ancient-DNA supplements]; and a diffuse modern presence of
haplogroup T around a tenth of Europeans, rising to a quarter in some eastern populations
[snippet-only]. The honest map for a T lineage therefore shows a Near-Eastern origin and a
**diffuse** European presence with at least two entry routes, not a single line — and marks any
small subclade's position as "unknown — no published population study" when that is the state of
the literature.

## §6 Reporting rules

1. Tool, tree, version, quality and the terminal marker, every time.
2. Depth stated: "subclade unresolved by chip" unless a sequence resolves it.
3. Strand flips and chip-only private mutations separated from real discrepancies.
4. A chip call reconciled against any sequencing call on the same line; disagreement explained.
5. Ages with source, date and interval; two clocks for mtDNA, labelled.
6. Place claims graded by the evidence column of the ladder; "formed within <region>" rests on
   modern distribution alone unless an ancient sample on the node exists, and the report says so.
7. Surname-lineage links come from surname projects and published genealogies, cited as such,
   with their self-selection acknowledged; a project's informal tally is not a population
   frequency.

## §7 Other tools and their licences

| Tool | Licence (as read) | Note |
|---|---|---|
| Yleaf | GPL-3.0 | shell out to it; do not vendor its code |
| HaploGrep 3 | MIT | the mtDNA route above; its tree catalogue `trees.json` lists available tree versions |
| yhaplo (23andMe) | custom, internal non-commercial research only; redistribution restricted [snippet-only — licence paraphrased, read it before relying on it] | hg19 only; ISOGG tree snapshot of January 2016; assumes male samples and calls "A" when no derived upper-branch allele is seen — run its ancestral-SNP option before accepting such a call. The converter's `y-genos` mode writes its sample-major layout for anyone who holds it under its licence. |
| eveHap | PolyForm-Noncommercial [snippet-only] | reads consumer files natively for mtDNA; non-commercial only |
| FamilyTreeDNA Mitotree (via HaploGrep) | non-commercial use only [snippet-only] | opt-in only, with the restriction displayed |
| PhyloTree | citation requested; licence text not located | prefer HaploGrep's versioned distribution |
