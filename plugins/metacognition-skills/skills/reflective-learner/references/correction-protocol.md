# Correction protocol: triage, contradiction diagnosis, restatement craft, the record

The reflection cycle in `reflection-template.md` is what you run *after* a piece of work. This
file is what you run *during* the ten turns after a user corrects you — the moment the skill is
invoked most often and gets wrong most often. It covers the four judgements that decide whether
a correction changes anything: what to store, whether it conflicts with what you already believe,
how to restate it so the restatement is worth reading, and what the stored record must contain
to still work six months later.

## Contents
- Triage: which corrections earn a durable entry
- Contradiction diagnosis: real conflicts vs. under-qualified entries
- Restatement craft: wording that proves comprehension
- The correction record: seven fields and why each survives
- The enforcement ladder: when memory is the wrong site
- Failure envelope: where this stops working
- Deliverable contract: what a finished correction pass contains
- Worked example: six corrections in one session, end to end

## Triage: which corrections earn a durable entry

Most corrections should be applied and forgotten. A durable entry is not free: every stored rule
is scanned at every future session-start load, and the store is the one place noise cannot be
tolerated, because it is read when there is no time to evaluate it. Run four questions in order.
Q1 can end it outright — nothing that recurs, nothing stored. The rest compose rather than
short-circuit: Q2 decides what kind of entry, Q3 decides whether it is written now or held for a
second sighting, and Q4 overrides the type when the correction contradicts evidence you verified.
Q3 does not bind every branch — where the routing table's Explicit column reads *either*, the
entry is written on the first sighting regardless of how Q3 answered, because a missing check is
worth recording before it recurs.

**Q1 — Will the situation recur?** Is the thing being corrected a *class* of work, or one artifact
that will never exist again? "Drop the note about that vendor, the contract ended" governs nothing
future. Apply it; store nothing. An entry that can never fire again is pure scan cost.

**Q2 — Could the right answer have been derived?** Given the request and the materials in front of
you, was the correct output inferable?
- **No — it was arbitrary.** The user reads exceptions first and stops; the user wants dates one
  way; the user hates a word. Nothing in the materials implies it. **Store it as a PREFERENCE.**
  Unguessable knowledge is the highest-value thing a memory store holds, precisely because the only
  way to acquire it is to spend the user's attention, and storing it is the only way that spend
  buys anything. This inverts the intuition that big errors matter more than nitpicks: an
  unguessable nitpick is worth more per byte than a large arithmetic error.
- **Yes — it was derivable.** Three totals did not tie to the source. The *fact* (the totals were
  wrong) is worthless stored; it was recomputable then and will be recomputable next time. What is
  missing is a step. **Store the check, not the fact:** "recompute every total from the source rows
  before sending." A stored check fires on every future artifact; a stored fact fires on none.

**Q3 — How many observations do you have, and who paid for them?** Explicit correction → store on
the **first** occurrence. Silently inferred preference (the user rewrote your headings without
comment, or chose one of your variants) → wait for the **second**.

The split is not fussiness; the two errors are not symmetric. Failing to store a real preference
costs one more correction — the user says it again, and the second time it is explicit, so it will
be caught. Storing a *false* preference costs friction that is invisible to you: it is applied
silently, everywhere, and the user has to notice a pattern across several outputs and then guess
that you are carrying a rule they never gave you. So the threshold sits on the recoverable side of
the asymmetry. And an explicit correction has already paid the observation cost — waiting for a
second one spends the user's attention to buy information you already hold, and being told the same
thing twice is the specific experience that makes people stop trusting a memory system at all.

**Q4 — Is it true, or is it wanted?** When the correction contradicts something you actually
verified, do not promote the user's assertion to a `FACT:`. Apply it — it is their deliverable —
and record it as `PREFERENCE: user wants <X> in <context>`, leaving your evidence in Open
Questions. A preference is safe to apply; a false fact is not, because everything downstream is
derived from it confidently and forever, and nothing in the store will ever mark it suspect. This
is the single most damaging storage error available, and deference is what causes it.

Quick routing summary:

| Recurs? | Derivable? | Explicit? | Store as |
|---|---|---|---|
| No | — | — | nothing (apply only) |
| Yes | No | Yes | `PREFERENCE:` now |
| Yes | No | No (inferred) | candidate in working notes; `PREFERENCE:` on the 2nd sighting |
| Yes | Yes | either | `RULE:`/`METHOD:` naming the missing check |
| Yes | Contradicts verified evidence | Yes | `PREFERENCE:` only — never `FACT:` |

## Contradiction diagnosis: real conflicts vs. under-qualified entries

Most apparent contradictions with stored memory are not contradictions. Flipping an entry that was
merely under-qualified destroys a true statement and starts an oscillation.

**The simultaneity test.** Write out one concrete next action that both the stored entry and the new
instruction govern. *If an action exists that satisfies both, there is no contradiction* — the old
entry is missing a qualifier, and qualifying it is the fix. Only when no single action can satisfy
both is the conflict real.

Four things that look like contradictions and are not:

| Surface conflict | Tell | What it actually is | Fix |
|---|---|---|---|
| Scope | The stored entry names no context; the new instruction names one | Under-qualified entry | Add the qualifier; retract nothing |
| Altitude | One statement is outcome-level, the other cause-level | Two levels of one rule | Keep the cause-level form; demote the other to an example |
| Time | The world changed — role, tool, policy, counterparty | Succession, not conflict | UPDATE annotation, original kept for provenance |
| Occasion | "Just this once", or the instruction names one artifact | Exception | Apply; store nothing durable |

A **real** contradiction has the same scope, the same altitude, the same period, and no action that
satisfies both. Real contradictions are not yours to resolve by picking: surface both entries with
their provenance to the user, and record the flag through
`metacognition-skills:hierarchical-memory-manager`, which owns the annotation form.

**Oscillation is a missing-variable signal.** An entry that has been reversed twice — two UPDATE
notes each undoing the last — is not evidence that the user is inconsistent. It is evidence that the
entry is missing the variable that distinguishes the two occasions (audience, artifact type, stage
of the work, who else will read it). At the *second* reversal, stop annotating and re-derive the
entry as a conditional one naming that variable. The threshold is two because one reversal is
ordinary succession; the second is the first moment the pattern is visible, and each further
reversal teaches every future session the current half of a rule while hiding that the other half
exists.

## Restatement craft: wording that proves comprehension

A restatement earns its place only if the user could answer "no" to some specific clause in it. That
is the whole test: **is it falsifiable in one word?** A restatement the user cannot disagree with
has told them nothing about whether the correction landed.

Four elements make it falsifiable:

1. **The rule at cause level, in different words than the user used.** Different words are
   load-bearing — if you echo their phrasing, a misunderstanding survives intact, because the
   sentence is guaranteed to match no matter what you understood by it.
2. **The scope boundary you inferred** — where it applies and, explicitly, where you are *not*
   applying it. This is usually the only genuinely new claim in the restatement, and the one worth
   the user's two seconds.
3. **A named consequence for something already on the table** — the specific delivered or pending
   output this changes. Proves application, not agreement.
4. **The mechanism** — the check or default you are changing so it holds without you remembering.

Length: two to four sentences. Under one, the boundary does not fit. Past five it becomes
performance, and the checkable clause is buried in the part the user skims.

Three anti-patterns, in their natural wording:

- **Apology-as-restatement** — *"You're absolutely right, I apologize — I'll be more careful with
  that going forward."* Contains no rule, no scope, no consequence. Nothing here can be wrong,
  which is exactly the problem. Put any apology *after* the substance, where it costs nothing.
- **Echo** — *"Got it — you want the exceptions first, not the summary first."* Word-for-word
  receipt. If the misunderstanding is in what "exceptions" covers, this sentence cannot expose it.
- **Over-generalization** — *"Understood, I'll always lead with the most important thing."* The
  restated rule is broader than the correction. The user did not license it, it will now be
  misapplied to artifacts it does not fit, and the next correction will be to narrow it. The tell
  is the word *always* attached to a rule the user stated about one kind of document.

A restatement carrying all four elements, for a correction that three totals did not tie out:

> "The totals are the part that has to survive an auditor re-adding the column, so a figure I
> transcribed rather than recomputed is a defect even when it happens to be right — I carried them
> from the previous version instead of rebuilding them from the export. I'm treating that as
> binding on anything that ties to a source file, not on the narrative counts inside the commentary,
> which you've been fine with rounded. Rebuilding all six totals now, and from here the totals get
> recomputed from source rows before the draft is written rather than checked after. Tell me if the
> boundary is wrong."

Every clause is refusable: the cause, the boundary in, the boundary out, and the mechanism.

## The correction record: seven fields and why each survives

Six months later, the person reading the entry has no memory of the conversation. Each field exists
because a specific question gets asked at that distance and nothing else answers it.

1. **Trigger context** — the situation in which the rule fires. Without it the rule fires
   everywhere or nowhere, and both failures look like the rule working.
2. **The rule, at cause level.** "The totals were wrong" is an outcome and generalizes to nothing.
   "Totals were carried from the prior version rather than recomputed" names the mechanism, and the
   mechanism is what recurs.
3. **Boundary — where it does not apply.** Rules metastasize when nobody wrote the edge. The
   symptom at six months is a rule you find yourself routinely working around, which quietly
   teaches you that rules are negotiable.
4. **Counterfactual — what you would have done without it.** This is what makes an application
   audit possible at all: "applied" can only be distinguished from "never came up" if the unfixed
   behavior is written down. It is also the retirement test — when the counterfactual has become
   impossible, the entry can go.
5. **Origin** — date plus the episode in one clause. An entry that knows where it came from can be
   re-checked and retired; one that does not can only be believed or ignored forever.
6. **Status** — user-stated (binding) or inferred (revisable), with the observation count. Six
   months out this is the difference between "may be relaxed under time pressure, say so out loud"
   and "may not."
7. **Enforcement site** — where the rule actually fires from: a memory entry, a project instruction,
   a line in a template, a check in a script. A rule stored somewhere nobody reads at the moment of
   action is a rule that does not fire, and its failures will be misdiagnosed as carelessness.

The entry grammar and the file layout belong to
`metacognition-skills:hierarchical-memory-manager`; the permanence gates that decide whether the
entry stays belong to `metacognition-skills:knowledge-crystallizer`. This list is what the
correction contributes to them.

## The enforcement ladder: when memory is the wrong site

A correction that arrives **again after the rule was stored** is the only hard evidence that the
loop is broken — everything else is self-report. Read it precisely: it indicts the *site*, not the
discipline. Restating a rule that is already in the store has never worked, because if reading it
were enough it would have worked the first time.

- **1st occurrence** → memory entry. Cheap, reversible, sufficient for most things.
- **Recurs once with the entry in place** → move it to where the work happens: the template's
  default, a line in the checklist that is open while drafting, the project instructions that load
  before the task rather than at session start.
- **Recurs again** → mechanize it. A check that *fails* beats a note that reminds. At this point
  the rule has cost the user three corrections, and a fourth is not a discipline problem to
  apologize for.

Moving up a rung is not an escalation in severity. It is an admission that the previous site was
not read at the moment of action, which is a design fact about the workflow, not a character fact.

## Failure envelope: where this stops working

- **The cause was ambiguity, not error.** If the request genuinely underdetermined the answer, any
  lesson you extract is a guess wearing a rule's clothes, and storing it trains you to guess with
  more confidence next time. *Tell:* the root cause reads "should have asked." *What you see later:*
  a store full of directional preferences that quietly contradict each other. *Right output:* store
  the ambiguity class ("requests of this shape do not determine X — ask, or state the assumption in
  the draft"), and ask the question now.
- **Correlated corrections.** Three or more corrections on a single artifact in one session are not
  three independent observations; they usually share one cause. Running a cycle on each produces
  three narrow rules and inflates the apparent evidence for all of them. At the third, stop doing
  per-correction cycles and run one at the end, against the shared cause.
- **Vague dissatisfaction.** "This isn't what I wanted," with nothing specific attached, contains no
  extractable rule. Root-cause analysis on it manufactures a cause, which then gets stored. Ask one
  question offering two concrete candidate readings; a forced choice is easier to answer than an
  open one and gives you the boundary for free.
- **Assertions you cannot verify.** See Q4 above. Store what is wanted; never upgrade it to a fact.
- **Time-critical work.** Mid-incident, the cycle costs turns the incident needs and the meta-talk
  crowds out the work. Log the correction verbatim into working notes and run the cycle after.
- **Corrections about the relationship rather than the work** ("you're being too formal", "stop
  hedging"). These are real preferences, but reflecting on them *in the conversation* makes the
  meta-discussion the artifact — the thing the user was already tired of. One clause of
  acknowledgment, store the preference, change the next paragraph.
- **The method's own failure mode is silent.** Reflection theater looks exactly like reflection: the
  store grows, the summaries are well-written, nothing changes. It has no internal symptom, which is
  why the external one — the same correction twice — is the only measurement worth keeping.
- **Not this skill at all:** if the correction reports a defect with a chain of causes across a
  process rather than a lesson about how you worked, that is an incident, and
  `continuous-improvement-skills:root-cause-analysis` owns it.

## Deliverable contract: what a finished correction pass contains

1. **A restatement in the conversation**, two to four sentences, carrying the four elements, with
   at least one clause the user can refuse.
2. **The correction visibly applied** — the affected part re-issued, not promised. A promise is
   indistinguishable from having missed the point.
3. **Zero or one durable entries per correction**, in the store's entry grammar, carrying the seven
   fields. Zero is the common and correct outcome; two entries from one correction almost always
   means one of them is an instance, not a rule — a pass covering several corrections totals
   accordingly.
4. **A contradiction flag if one fired**, with both entries' provenance and an explicit resolution
   route (user-confirmed, or standing and visible).
5. **Nothing else in the conversation.** The situation/outcome/strengths/weaknesses prose belongs in
   the store or a note. A correction answered with a retrospective essay reads as deflection.

## Worked example: six corrections in one session, end to end

Context: a recurring vendor-performance summary, assembled from a monthly export. Six corrections
arrive across one session. Four of them land on the summary itself, which is past the
correlated-corrections threshold above — so this is one triage pass run at the end of the session,
not six reflection cycles. Triage is cheap enough to run per correction; the cycle is not.

| # | The correction | Recurs? | Derivable? | Source | Routing |
|---|---|---|---|---|---|
| C1 | "Put the exceptions first — I read the top and stop." | Yes | No — nothing in the materials implies it | Explicit | `PREFERENCE:` stored now |
| C2 | "Three of these totals don't match the export." | Yes | Yes — recomputable from the source | Explicit | `RULE:` storing the missing check |
| C3 | "Drop the note about that vendor, the contract ended." | No | — | Explicit | Apply; store nothing |
| C4 | User silently rewrites two headings from questions to noun phrases | Yes | No | Inferred, 1st sighting | Hold as a candidate in working notes |
| C5 | The same rewrite again, on the next artifact in the session — C4 was the first sighting | Yes | No | Inferred, 2nd sighting | `PREFERENCE:` promoted |
| C6 | "Give me the full detail here, all of it" — store holds *"user wants one-page summaries"* | Yes | No | Explicit, apparent conflict | Diagnose before writing |

Tally — **3** new durable entries (C1, C2, C5), **1** amendment to an existing entry (C6), and **2**
that store nothing (C3, C4). Every correction is accounted for: 3 + 1 + 2 = 6.

**C6, diagnosed.** Simultaneity test: is there one action satisfying both the stored preference and
the new instruction? Yes — a one-page summary with the full detail behind it. So this is a scope
conflict, not a real one: the stored entry was written from an occasion where the *summary* was the
deliverable and never said so. The entry is qualified, not flipped:

```markdown
- PREFERENCE: user wants standing summaries to fit one page. (confirmed <date>)
  (UPDATE <date>: scope qualified — applies to the recurring summary, not to detail packs
  requested for a specific question, where the user wants everything. Contradiction tested by
  simultaneity and found to be a missing qualifier; original kept for provenance.)
```

**C2, restated.** The wording is the four-element restatement quoted earlier in this file.

**C2, recorded.** All seven fields, in the store's grammar:

```markdown
- RULE: when an artifact carries figures that tie to a source file, recompute every total from
  the source rows before the draft is written — never carry a total forward from a prior version.
  (trigger: any tie-out artifact built from an export)
  (boundary: does not apply to approximate counts inside narrative commentary, which the user
  accepts rounded)
  (counterfactual: totals were transcribed from last period's file and spot-checked afterwards)
  (origin: <date> — three of six totals mismatched the export in the vendor summary)
  (status: user-stated, binding; 1 explicit occurrence)
  (site: memory entry — first occurrence, so the cheapest rung; the enforcement ladder above moves it if
  the correction recurs)
```

**The same record, read six months later.** Three questions arrive that the writer never
anticipated; each is answered by exactly one field, and no other field answers it:

- *"Someone asked me for a quick headcount in chat — does this fire?"* → **Boundary.** No: it is
  scoped to artifacts that tie to a source file. Without the boundary the honest reading is "always",
  and a rule that fires on everything gets suspended on everything.
- *"The user is in a hurry and says skip the checks — may I?"* → **Status.** User-stated and
  binding, so it is not silently skippable; the move is to say which check is being skipped and
  what that leaves unverified.
- *"Is this still worth carrying?"* → **Counterfactual plus origin.** If the build now recomputes
  totals mechanically, the counterfactual behavior — transcribing from the prior version — is no
  longer possible, so the entry can be retired to its enforcement site and dropped from the store.
  An entry with no counterfactual can never be shown to be obsolete, which is why stores that omit
  the field only ever grow.

**Three weeks later, the same correction arrives again.** The rule is in the store and the totals
were still carried forward. Do not re-store it and do not restate it; the ladder says the site is
wrong. The rule moves from a memory entry read at session start to a line in the template that is
open while drafting, and the next recurrence mechanizes it as a build-time check that fails on a
total the tool did not compute. What changed is where the rule lives, not how firmly it was
written.
