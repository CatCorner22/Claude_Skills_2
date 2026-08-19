---
name: reproducible-analysis
description: >-
  Makes an analysis produce the same numbers twice, rerun by anyone — a discipline
  spanning spreadsheets, notebooks, SQL, and scripts. Defines reproducible (same data
  + code) vs replicable (new data or implementation), then climbs the practice ladder: pin environments and
  record random seeds, make the rerun one command, keep lineage one-directional
  (raw → cleaned → derived, raw never edited), write literate
  analysis with code and narrative together, apply FAIR principles at working level,
  and verify by fresh-clone rerun plus a second person re-deriving the headline
  number. Python environment mechanics stay with
  coding-agent-skills:python-for-analysts. Use when an analysis must survive rerun,
  handoff, audit, or hostile scrutiny. Triggers: reproducible analysis, can someone
  rerun this, rerun the analysis, replication crisis, reproducibility crisis, random
  seed, data lineage, data provenance, literate programming, FAIR data.
metadata:
  version: "1.2.0"
  source: >-
    Built from the general-use expansion research dossier
    (docs/research/general-use-expansion-research.md, §8 reproducible-analysis).
    Provenance legend: [snippet-only] = verified via cross-checked WebSearch result
    blocks; the contested-claims framing (Ioannidis as model, OSC-2015 as disputed
    estimate) is load-bearing content from that dossier, not hedging.
---

# Reproducible analysis (same numbers twice, by anyone)

Define the two words first, because even the field's institutions got them backwards:
following Claerbout & Karrenbach (1992), **reproduce** = same data + same code gives
the same numbers; **replicate** = new data or a new implementation reaches the same
conclusion. The ACM used the two terms with swapped meanings from its 2016 badging
policy until August 2020, when it re-aligned with Claerbout; Plesser's "Reproducibility vs. Replicability:
A Brief History of a Confused Terminology" (2018) maps the mess [snippet-only]. The
confusion is institutional, not personal — so any reproducibility document states its
definitions at the top. The stakes come from the metascience literature, held honestly
in `references/reproducibility-method.md`; the payload here is practitioner-grade: an
analyst's quarterly numbers, an attorney's brief-support damages model, an ops
capacity study, and a developer's benchmark all fail the same ways and are fixed by
the same ladder.

## When to use
- A recurring analysis must be rebuilt cold — by a successor, a colleague, or you next
  quarter — and produce the same numbers from the same inputs.
- An analysis will face scrutiny: opposing counsel rerunning your expert's model, an
  auditor re-deriving a reported figure, a reviewer rerunning a benchmark.
- A "worked on my machine" post-mortem: the rerun produced different numbers and
  nobody changed anything on purpose.
- Not for: writing the Python itself — environments, pandas, script structure →
  `coding-agent-skills:python-for-analysts` (seam: that skill writes the code well in
  Python; this one is the cross-tool reproducibility discipline and audit, whatever
  the tool).
- Not for: file naming, foldering, and sanitization craft →
  `data-tools-skills:data-file-hygiene` (this skill *mandates* raw/derived separation;
  that one owns the naming and folder mechanics).
- Not for: proving code behaves as intended → `full-stack-dev-skills:testing-strategy`
  (tests catch broken behavior; this catches an analysis that cannot be rebuilt — an
  analysis can pass every test and still be unreproducible, and vice versa).
- Not for: whether the measurement itself can be trusted →
  `continuous-improvement-skills:measurement-systems-analysis` (its Gage
  "reproducibility" means agreement across operators — a different technical sense —
  and it is the upstream question: a perfectly rerunnable analysis of an untrustworthy
  metric reproduces noise).
- Not for: parse, query, and workbook mechanics —
  `data-tools-skills:csv-and-flat-file-wrangling`,
  `data-tools-skills:duckdb-local-analytics`,
  `data-tools-skills:excel-automation-python` are the tools this discipline governs.

## Do it
The terminology history, the crisis evidence held honestly, per-rung checklists, and a
worked example are in `references/reproducibility-method.md`.

1. **State the two definitions at the top of the analysis doc** (reproduce vs
   replicate, Claerbout usage) and which one you are promising. Four years of the ACM
   using the words backwards is the proof that "everyone knows what we mean" is false.
2. **Pin the environment and record every seed.** Tool and package versions written
   into the output; the seed of anything random — sampling, train/test splits,
   simulation, jittered charts — set explicitly and logged. Not only Python: the Excel
   version and add-ins, the database engine version, the BI tool release are all part
   of the environment. (Python-specific mechanics: `coding-agent-skills:
   python-for-analysts`.)
3. **Make the rerun one command.** Every step from raw input to final number runs from
   a single entry point — a script, a makefile, a master query, a run-all notebook.
   Any step that genuinely cannot be scripted gets written down as a numbered manual
   step with its exact parameters; an undocumented click is an invisible parameter.
4. **Keep lineage one-directional: raw → cleaned → derived.** Raw files are never
   edited in place — corrections happen in code so they reapply on rerun. Every
   derived artifact names its inputs and the code that produced it. The invariant:
   everything downstream of raw can be deleted and regenerated. (Folder and naming
   craft: `data-tools-skills:data-file-hygiene`.)
5. **Write the analysis literately.** Code and narrative together — Knuth's "Literate
   Programming" (1984) is the intellectual ancestor of notebooks and R Markdown/Quarto
   [snippet-only] — so every figure and headline number is *generated* by adjacent
   code, never pasted in. A pasted number is a silent fork in the lineage.
6. **Apply FAIR at practice level** (Wilkinson et al., "The FAIR Guiding Principles,"
   2016 [snippet-only]): **Findable** — named by convention, indexed where colleagues
   search; **Accessible** — in a shared location with access rules, not one laptop;
   **Interoperable** — open formats (CSV/Parquet over proprietary binaries) where
   possible; **Reusable** — metadata stating source, permissions, and the lineage note.
7. **Run the verification ritual: same numbers twice, by anyone.** (a) *Fresh-clone
   rerun*: check the project out on a clean machine or profile, run the one command,
   diff the headline numbers against the shipped ones. (b) *Second keeper*: a second
   person independently re-derives the headline number from raw — the same discipline
   as `safety-and-reliability-skills:split-tally-evidence`'s second keeper, because
   the author's rerun re-runs the author's blind spots along with the code.

## Why / learn
The crisis literature is the *why*, not the *how* — and it must be taught honestly,
because the honest version teaches more. Ioannidis's "Why Most Published Research
Findings Are False" (2005) is a **model, not a measurement**: Goodman & Greenland's
critique showed the title's conclusion follows from the assumed priors and bias
parameters [snippet-only]. What survives untouched is the mechanisms — underpowered
studies, analytic flexibility, publication bias — which are exactly the failure modes
an unreproducible workflow invites. The Open Science Collaboration (2015) replicated
100 psychology studies: 97% of originals had significant results, 36% of replications
did, and replication effect sizes averaged about half the originals [snippet-only].
The 36% was formally contested in *Science* (Gilbert et al. argued the estimate was
biased downward; the OSC replied) — but both camps agree published effect sizes
overstate, and "36% replicated" must never be flipped into "64% is false": a failed
replication is evidence of shrinkage and uncertainty, not disproof [snippet-only].
Even the field's two key words were institutionally swapped for four years — which is
why the ladder's first rung is definitions, and why a skill preaching honest numbers
opens by showing its own foundational numbers are contested.

The ladder itself is the practitioner translation (Sandve et al.'s "Ten Simple Rules
for Reproducible Computational Research" compresses to the same moves: track how every
result was produced, avoid manual manipulation, version everything, record seeds,
archive environments [snippet-only]). One command matters because every manual step is
a parameter stored in someone's memory — the script *is* the honest record of what was
actually done. Raw stays untouched because a hand-edit destroys both the audit trail
and the regenerate invariant at once: after it, no rerun can ever match. And the
second keeper exists because author-verification shares the author's environment,
habits, and assumptions — independent re-derivation is to analysis what dual custody
is to records. What this discipline buys is transferable across every job this library
serves: the analyst's quarterly number survives their promotion, the attorney's expert
survives discovery, the ops study survives the skeptical VP, the developer's benchmark
survives the reviewer who reruns it.

## Common mistakes
- Using "reproducible" and "replicable" interchangeably → declare the Claerbout
  definitions at the top; the ACM's four backwards years prove the ambiguity is real.
- "I reran it and got the same numbers" offered as verification → the author's rerun
  shares the author's environment and blind spots; fresh clone + second keeper.
- Seedless randomness → any sample, split, or simulation without a recorded seed makes
  the headline number unrepeatable by construction; set it and log it.
- Hand-editing a raw or derived file "just this once" → the regenerate invariant is
  dead from that moment; fix the code and rerun instead.
- Numbers pasted into the write-up → paste forks the lineage silently; generate them
  in place (literate analysis).
- Citing "most published research is false" as a measured fact → it is a
  model-derived claim (Goodman & Greenland); teach the mechanisms, not the slogan.
- Flipping "36% replicated" into "64% of the field is false" → a replication failure
  is not a disproof; the uncontested lesson is effect-size shrinkage.
- Confusing Gage R&R "reproducibility" with rerunnability → different technical sense
  (operator agreement); that question belongs to
  `continuous-improvement-skills:measurement-systems-analysis`.

## Tailor to your environment
Record your reproducibility surface in `references/your-environment.md`: the recurring
analyses and their headline numbers, the tool stack each runs on, where raw data lands
and derived outputs live, the one-command entry point per analysis, who plays second
keeper, and the verification cadence. Keep the committed file structural — real data,
client or matter names, and system credentials belong in
`your-environment.private.md` (git-ignored), never in a committed file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/reproducible-analysis.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/reproducibility-method.md — the terminology history, the crisis evidence
  held honestly (what is solid vs contested), per-rung checklists for the practice
  ladder, the verification-ritual protocol, and a worked example spanning analyst,
  attorney, ops, and developer cases, with provenance marks
- references/your-environment.md — your recurring analyses, stack, lineage layout,
  and second-keeper roster (fill in)
