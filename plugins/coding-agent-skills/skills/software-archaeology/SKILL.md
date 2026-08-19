---
name: software-archaeology
description: >-
  Excavates an accreted system — codebase, config, rules, or documents — before
  demolition or refactoring: harvests dating evidence (timestamps, commit history,
  style eras), builds Harris-matrix DAG (superposition of layers), clusters into named
  eras, classifies as living/fill/rubble with evidence, removes rubble via reversible
  scream test (disable, wait, see who screams, rollback ready), files site report.
  Chesterton's fence systematized for a whole site. Use when a mature system must be
  understood, pruned, or safely demolished, or when nobody knows which parts are alive.
  Triggers: software archaeology, excavate, dig into this legacy, harris matrix,
  stratigraphy, which of these are dead, scream test, who wrote this and why, safe to delete.
---

# Software archaeology (excavate before you demolish)

Archaeologists never bulldoze a site to find out what is in it. Edward Harris gave the
discipline its recording instrument (the Harris matrix, devised 1973 and formalized in
*Principles of Archaeological Stratigraphy*): a directed graph of before/after/contemporary
relationships between excavation contexts, governed by the law of superposition — what lies
above was deposited after what lies below `[snippet-only]`. Reinhard carried the method
across to software in "Adapting the Harris Matrix for Software Stratigraphy" (*Advances in
Archaeological Practice*, Cambridge) — a program's accreted versions treated as a digital
site obeying Harris's laws `[snippet-only]`. Hunt and Thomas named the wider practice
"software archaeology" (*IEEE Software*, 2002): preserve the artifacts, record as you dig,
and respect the cultural forces that produced the code `[snippet-only]`. This skill turns
all three into one discipline: **record before you remove**.

## When to use
- An accreted system — codebase, configuration store, rule set, feature flags, scheduled
  jobs, a shared-drive document corpus — must be refactored, migrated, pruned, or retired,
  and nobody can say with evidence which parts are still alive.
- "Is this safe to delete?" asked about anything old: a directory nobody owns, a rule that
  fires before yours, a folder literally named `deprecated` that people still fear.
- Reconstructing why a system is shaped the way it is — who wrote this and why — before
  changing it (inherited codebase, departed authors, contractor eras).
- Not for: diagnosing one failure's cause → `continuous-improvement-skills:root-cause-analysis`
  (RCA explains an incident's causal chain; excavation reconstructs the whole deposit's
  history so *safe demolition* is possible).
- Not for: simplicity challenges on new builds → `coding-agent-skills:soviet-space-graphite`
  (its Graphite Test includes the one-fence Chesterton check on a single candidate; this
  skill is the whole-site method when the fences number in the hundreds).
- Not for: version-control workflow and diff reading → `coding-agent-skills:git-and-code-review`.
- Not for: verifying claimed completeness before building the next phase →
  `coding-agent-skills:the-foreman` (that inspects new construction; this excavates old).

## Do it
Full dating taxonomy, Mermaid drafting conventions, a worked example, window-sizing rules,
and the site-report template are in `references/excavation-method.md`.

1. **Bound the site.** Name the system under excavation and the strata question being
   asked ("which of these 300 config files are dead?", "can the v1 module go?"). List what
   counts as an artifact at this dig's grain — file, rule, table, flag, job, document. An
   unbounded dig never finishes; a bounded one produces a deliverable.
2. **Harvest dating evidence** for every artifact, from strongest to weakest: version-control
   history (first commit, last meaningful change, author clusters); naming-convention eras
   (`ALLCAPS.INI` vs `snake_case.yaml` vs `per-service-kebab` are different decades of the
   site); style and toolchain fingerprints (framework idioms, API generations); dependency
   direction (who references whom); runtime evidence (logs, access records); filesystem
   timestamps last (migrations and copies reset them — they lie). Date by convergence of
   independent lines, never by one line alone.
3. **Build the relationship graph** — the Harris matrix. Record, per artifact: what it sits
   *above* (overrides, wraps, consumes, supersedes), what it is *contemporary* with (same
   era, same deposition event), and what *cuts* it (later changes that truncated or replaced
   part of it). This is the step the assistant amplifies: it reads the full inventory —
   hundreds or thousands of artifacts, their references, dates, and naming patterns — and
   emits a draft matrix in minutes, where a human dig would take weeks. Render it as a
   Mermaid diagram (newest strata at top; conventions in the reference). The human then
   corrects edges they know are wrong — the draft is a hypothesis, not a verdict.
4. **Cluster into named eras.** Group contemporaneous artifacts into strata and give each a
   memorable name from its evidence signature: "the Bootstrap era," "the contractor summer,"
   "the compliance push." An era boundary needs at least two independent evidence lines
   (e.g., a naming shift *and* an author-cluster change). Named eras turn a pile of files
   into a history people can reason and argue about.
5. **Classify every layer, with evidence:**
   - **LIVING FLOOR** — in active use now: runtime or reference evidence within the
     artifact's own usage rhythm.
   - **FILL** — inert itself but load-bearing: something living sits on it (references it,
     imports it, fires after it). Removing fill collapses what is above.
   - **RUBBLE** — nothing above it, no runtime evidence across a full usage cycle, its era
     closed. Only rubble is a removal candidate.
   When evidence is insufficient, classify FILL, never RUBBLE — the default must be the
   conservative one. A folder's *label* ("deprecated", "old", "backup") is not evidence.
6. **Remove rubble via the scream test** — the removal step, not a separate project.
   Disable the suspect artifact *reversibly* (flag off, rename, revoke access — never
   delete first); announce or stay silent per your policy (a silent test also catches
   consumers nobody documented); wait a window sized to the artifact's usage rhythm (a
   daily job needs weeks; anything touched by a monthly or quarterly cycle needs that full
   cycle); keep rollback ready and restore within minutes if someone screams. Microsoft's
   documented decommissioning practice found roughly 15% of "unused" servers screamed when
   disabled `[snippet-only]` — that is the measured error rate of confident "nobody uses
   this" claims, and the reason the test exists. Only after a silent window: archive, then
   delete.
7. **File the site report.** What was excavated, the matrix, the eras and their evidence,
   the classification table, what was removed and what screamed, what survived and why,
   and the open questions. Future maintainers inherit your dig — the report is what keeps
   them from excavating the same ground again.

## Why / learn
The law of superposition is the whole trick: in an undisturbed deposit, position *is*
chronology. Software accretes the same way — an override is later than the rule it
overrides, a wrapper is later than what it wraps, a migration is later than the schema it
alters — so the reference-and-override structure of a system encodes its history even when
every document and every author is gone. The Harris matrix just makes that encoding
explicit and checkable: once the relationships are drawn as a DAG, "what happens if I
remove this?" becomes a graph query instead of a guess.

Record-before-remove is Chesterton's fence made procedural. The fence parable says: don't
clear the fence until you know why it was put up. On a one-fence decision, asking "why?" is
enough — that is `soviet-space-graphite`'s Graphite Test. On an accreted site there are
hundreds of fences, and asking "why?" one at a time either stalls forever or degenerates
into vibes. Excavation replaces the question with evidence: superposition tells you what
each fence holds up, dating tells you which era planted it, and classification tells you
which fences hold nothing at all.

The scream test exists because *usage is the only authority on use*. Documentation lies
(it describes intent, not behavior), owners lie (they moved on years ago), and labels lie
(the worked example in the reference is a "deprecated" folder a nightly job still reads).
Disabling-and-listening asks the system itself, and the Microsoft figure — ~15% of
confidently-declared-dead servers turned out alive `[snippet-only]` — quantifies why the
question must be asked even when everyone agrees the thing is dead. Reversibility is what
makes the test cheap: a scream costs minutes of rollback, while a wrong deletion costs a
reconstruction. And the site report closes the loop Hunt and Thomas cared about: code is
produced by cultural forces, and your removals are the next stratum — recorded, they are
history; unrecorded, they are the next generation's mystery.

## Common mistakes
- Classifying by label ("it's in `deprecated/`", "the wiki says retired") → labels are
  claims, not evidence; demand runtime or reference evidence.
- Trusting filesystem timestamps → migrations, copies, and checkouts reset them; use
  version-control history and convergence of independent evidence lines.
- Deleting as the test → the scream test disables *reversibly*; deletion happens only
  after a silent window, with an archive first.
- Sizing every scream window at "a week" → the window must cover the artifact's slowest
  usage rhythm; month-end and quarter-end consumers scream late.
- Skipping the matrix and going straight to a kill list → without the relationship graph,
  fill gets classified as rubble and the structure above it collapses.
- Treating the assistant's draft matrix as ground truth → it is a hypothesis from
  imperfect evidence; the human corrects edges before anything is classified.
- No site report → the next maintainer re-excavates your site, and your removals become
  their mysteries.

## Tailor to your environment
Wire in your current systems in `references/your-environment.md`: the accreted systems you
are likely to dig (repositories, config stores, job schedulers, document shares), where
each one's dating evidence lives (history, logs, access records), your naming-convention
eras as you discover them, your announce-or-silent scream-test policy and standard window
sizes, and where site reports are filed. Keep committed content structural — real system
names, owners, or anything sensitive goes in `your-environment.private.md` (git-ignored),
never in a committed file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/software-archaeology.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/excavation-method.md — dating-evidence taxonomy, Harris-matrix drafting
  protocol with Mermaid conventions, a worked config-directory example, era clustering,
  layer classification with evidence bars, the scream-test protocol with window sizing,
  and the site-report template
- references/your-environment.md — your dig sites, evidence sources, and removal policy (fill in)
