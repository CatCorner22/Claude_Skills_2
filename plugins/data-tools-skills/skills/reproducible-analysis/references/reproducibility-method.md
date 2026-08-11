# Reproducibility method — the full ladder

Provenance legend: **[snippet-only]** = verified via cross-checked WebSearch result
blocks (per the general-use expansion dossier, §8). The contested-claims framing below
is load-bearing teaching content from that dossier — teach the disputes, don't smooth
them over.

## Contents
1. [Terminology: a confused history](#1-terminology-a-confused-history)
2. [The crisis evidence, held honestly](#2-the-crisis-evidence-held-honestly)
3. [The practice ladder, rung by rung](#3-the-practice-ladder-rung-by-rung)
4. [The Sandve rules as a compressed checklist](#4-the-sandve-rules-as-a-compressed-checklist)
5. [FAIR at practice level](#5-fair-at-practice-level)
6. [The verification ritual](#6-the-verification-ritual)
7. [Worked example: the quarterly capacity study, rebuilt cold](#7-worked-example-the-quarterly-capacity-study-rebuilt-cold)
8. [The same failure in four careers](#8-the-same-failure-in-four-careers)

## 1. Terminology: a confused history

| Term (Claerbout usage) | Meaning | Test |
|---|---|---|
| **Reproduce** | Same data + same code → same numbers | A stranger reruns your artifact and matches your output |
| **Replicate** | New data and/or new implementation → same conclusion | An independent effort reaches the same finding |

Claerbout & Karrenbach fixed this usage in 1992. The **ACM used the two words with
swapped meanings from 2013 until August 2020**, when it re-aligned with Claerbout;
Plesser's "Reproducibility vs. Replicability: A Brief History of a Confused
Terminology" (*Frontiers in Neuroinformatics*, 2018) documents the whole tangle
[snippet-only]. Consequences for practice:

- Any document promising "reproducibility" defines the term in its first lines.
- When reading others' claims, check which convention they use before comparing.
- Note the false cognates: Gage R&R "reproducibility"
  (`continuous-improvement-skills:measurement-systems-analysis`) means agreement
  across human operators; DOE "replication" means repeated experimental runs
  (`continuous-improvement-skills:design-of-experiments`). Same words, different
  machinery.

## 2. The crisis evidence, held honestly

What to teach, with its epistemic status attached:

- **Ioannidis 2005, "Why Most Published Research Findings Are False" (*PLoS
  Medicine*)** — the metascience landmark [snippet-only]. **Status: a model, not a
  measurement.** Goodman & Greenland's published critique showed the title's
  conclusion follows from the assumed priors and bias parameters — partly circular as
  "proof" [snippet-only]. What survives: the *mechanisms* — low prior odds, small
  samples, analytic flexibility, publication bias — are real, quantifiable, and are
  precisely the failure modes an unreproducible workflow invites. Cite the mechanisms;
  never cite the title as a measured fact.
- **Open Science Collaboration 2015 (*Science*)** — 100 studies from three top
  psychology journals: **97% of originals reported significant results; 36% of
  replications did; replication effect sizes averaged about half the originals**
  [snippet-only]. **Status: contested in magnitude, not in direction.** Gilbert, King,
  Pettigrew & Wilson's *Science* comment argued error, low power, and replication
  infidelities biased the estimate downward; the OSC replied [snippet-only].
  Uncontested across both camps: published effect sizes overstate (the ~half-size
  shrinkage), and "36% replicated" must never be flipped into "64% of psychology is
  false" — a replication failure is not a disproof.
- **Why this is the skill's opening lesson:** a discipline about trustworthy numbers
  whose own flagship numbers are contested must model the honesty it preaches. The
  practitioner cargo is the mechanisms and the shrinkage, not the slogans.

## 3. The practice ladder, rung by rung

**Rung 0 — Definitions.** State reproduce/replicate (Claerbout) and which you promise.

**Rung 1 — Pin the environment; record seeds.**
- [ ] Tool versions recorded *in the output* (not a side note): language/runtime,
      packages, database engine, spreadsheet application and add-ins, BI tool release.
- [ ] A machine-readable manifest where the ecosystem supports one (lockfile,
      `requirements.txt`, container spec) — Python mechanics belong to
      `coding-agent-skills:python-for-analysts`.
- [ ] Every random element — sample draws, train/test splits, simulations, jitter —
      has an explicitly set seed, logged next to the result it produced.
- [ ] Inputs carry checksums or immutable version identifiers where feasible, so "same
      data" is checkable, not assumed.

**Rung 2 — One-command rerun.**
- [ ] A single entry point (script, makefile, master query, run-all notebook) drives
      raw → final.
- [ ] Steps that truly cannot be scripted (a vendor portal download, a GUI export) are
      written as numbered manual steps with exact parameters and expected outputs.
- [ ] The command is documented where a stranger will look first (README / run sheet).
- [ ] Intermediate state is not required: the rerun works from raw alone.

**Rung 3 — Data lineage, one direction.**
- [ ] `raw/` is exactly as received and never edited in place; corrections are code.
- [ ] Every derived artifact names its inputs and the code version that produced it
      (a lineage note or a generated log line beats memory).
- [ ] The regenerate invariant holds: delete everything downstream of raw; the one
      command rebuilds it identically.
- [ ] Folder and naming mechanics per `data-tools-skills:data-file-hygiene`.

**Rung 4 — Literate analysis.** Knuth's "Literate Programming" (*The Computer
Journal*, 1984) — programs written for humans, code and narrative interleaved — is the
intellectual ancestor of notebooks, R Markdown, and Quarto [snippet-only].
- [ ] Every figure and headline number in the write-up is generated by adjacent code.
- [ ] No pasted numbers: a pasted value is a fork in the lineage that no rerun updates.
- [ ] The narrative states decisions (filters, exclusions, definitions) beside the
      code that implements them.

**Rung 5 — FAIR at practice level.** See §5.

**Rung 6 — Verification ritual.** See §6.

## 4. The Sandve rules as a compressed checklist

Sandve, Nekrutenko, Taylor & Hovig, "Ten Simple Rules for Reproducible Computational
Research" (*PLOS Computational Biology*, 2013) [snippet-only] — the rules compress
onto the ladder: track how every result was produced (rungs 2–3); avoid manual
manipulation of data (rung 3); archive exact environments and versions (rung 1);
version-control everything (rungs 1, 3); record seeds (rung 1); store raw data behind
plots and connect results to the code that made them (rung 4); make outputs
inspectable and public where appropriate (rung 5). Use the ladder for building and the
Sandve list as the audit pass afterward.

## 5. FAIR at practice level

Wilkinson et al., "The FAIR Guiding Principles for scientific data management and
stewardship" (*Scientific Data*, 2016) — Findable, Accessible, Interoperable,
Reusable, with distinctive emphasis on machine-actionability [snippet-only].
Working-level translation:

| Principle | Repository-scale meaning | Your-desk meaning |
|---|---|---|
| Findable | Persistent identifiers, indexed metadata | Named by convention, listed where colleagues actually search |
| Accessible | Standard retrieval protocol | Shared location with stated access rules — not one laptop |
| Interoperable | Formal vocabularies | Open formats (CSV/Parquet over proprietary binaries) where possible |
| Reusable | Rich provenance metadata | A lineage note: source, permissions/license, how to rerun |

FAIR is the outward-facing rung: the earlier rungs make the analysis rebuildable by
you; FAIR makes it findable and usable by someone who has never met you.

## 6. The verification ritual

Reproducibility is a claim; the ritual is its test. Two independent checks:

1. **Fresh-clone rerun.** A clean machine, VM, or user profile; check out the project;
   follow only the written instructions; run the one command; diff the headline
   numbers against the shipped ones. Every failure is a finding: an unpinned version,
   an absolute path, a file that lived only in the author's downloads folder.
2. **Second keeper re-derivation.** A second person independently re-derives the
   headline number from raw — ideally by their own route (a different tool is a
   feature, not a bug: agreement across implementations is stronger evidence). This is
   the second-keeper pattern from
   `safety-and-reliability-skills:split-tally-evidence`, the sibling discipline:
   split-tally makes a *record* trustworthy by ensuring no single party can alter it;
   the second keeper makes a *number* trustworthy by ensuring no single mind produced
   it. The author's own rerun cannot serve — it re-runs the author's blind spots along
   with the code.

Log both checks (date, who, environment, match/mismatch, findings) with the analysis.
Cadence: on first delivery, after any method change (MAJOR-style), and on a standing
schedule for recurring analyses.

## 7. Worked example: the quarterly capacity study, rebuilt cold

An ops analyst inherits a quarterly staffing-capacity study: a workbook of pasted
extracts, a notebook with `seed = ?` nowhere, and a headline number ("we are 12% under
capacity") the previous owner cannot explain. Applying the ladder:

- **Rung 0:** the method note opens: "Reproducible here means: same raw extracts +
  this repository at tag `2026-Q2` produce the same Table 1 and the 12% headline."
- **Rung 1:** runtime and package versions written into the output footer; the
  simulation that models absence variability gets `seed = 20260401`, logged beside
  its result; each raw extract gets a checksum recorded at receipt.
- **Rung 2:** `run_study.sh` drives extract-validation → cleaning → model → report.
  The one non-scriptable step (HR portal export) becomes manual step M1 with exact
  filter settings and the expected row count.
- **Rung 3:** the pasted-extract workbook is retired; `raw/` holds untouched exports;
  the two hand-corrections the predecessor made (a mistyped department code, a
  duplicated pay period) become documented code fixes that reapply on rerun.
- **Rung 4:** the notebook interleaves the exclusion decisions with the code that
  applies them; the 12% is computed in the final cell, never typed.
- **Rung 5:** the project lands in the team share under the naming convention, with a
  lineage note naming sources, permissions, and the rerun command.
- **Rung 6:** a colleague fresh-clones on a loaner laptop — and the rerun *fails*: the
  model pulled a calendar file from the author's home directory. Fixed, rerun,
  matched. The second keeper re-derives the headline from raw in SQL and gets 12.4%
  vs the notebook's 11.8% — the diff exposes an undocumented exclusion of contractors,
  which becomes an explicit, written decision. Both checks logged.

The two verification failures are the point: each one was a silent assumption that
would otherwise have surfaced during a hostile review instead of a friendly one.

## 8. The same failure in four careers

| Role | The artifact | The unreproducibility cost | The ladder's payoff |
|---|---|---|---|
| Analyst | Quarterly numbers | Successor can't rebuild Q2; trend breaks | One command + lineage; the series survives turnover |
| Attorney | Expert's damages model | Opposing counsel finds the rerun gives a different figure — credibility, not arithmetic, is now the issue | Pinned assumptions, versioned data, deterministic rerun survive discovery |
| Ops lead | Capacity study | The skeptical VP asks "who checked this?" and the answer is nobody | Second keeper's independent re-derivation is the answer |
| Developer | Benchmark | Reviewer reruns and gets different latencies; the PR stalls | Pinned environment + seeds + fresh-clone check before publishing |
