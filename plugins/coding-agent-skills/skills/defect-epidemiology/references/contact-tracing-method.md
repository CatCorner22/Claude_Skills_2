# The contact-tracing method

Research anchors, all `[snippet-only]` provenance (cross-checked across independent
search results): ReDeBug, IEEE S&P 2012 — unpatched code clones of known-vulnerable code
found across entire OS distributions; patches routinely fail to propagate to clones.
VUDDY, IEEE S&P 2017 — vulnerable-clone discovery scaled with function-level fingerprints.
Juergens et al., "Do Code Clones Matter?", ICSE 2009 — inconsistent changes to clones are
frequent and yielded ~107 confirmed faults across the commercial and open-source systems
studied. Kim et al.'s clone-genealogy work — clone lineages tracked through version
history.

## Contents
- [Fingerprinting the defective pattern (Type 1–4)](#fingerprinting-the-defective-pattern-type-14)
- [The three-pass sweep](#the-three-pass-sweep)
- [The contact-disposition table](#the-contact-disposition-table)
- [Patient-zero analysis and the infectious-source checklist](#patient-zero-analysis-and-the-infectious-source-checklist)
- [R0, worked on a small example](#r0-worked-on-a-small-example)
- [Quarantine patterns](#quarantine-patterns)
- [The outbreak-report template](#the-outbreak-report-template)

## Fingerprinting the defective pattern (Type 1–4)

The clone taxonomy, at practice level — each type is a mutation distance from the index
case, and each has a cheapest pass that can still catch it:

| Type | What changed in the copy | Caught by |
|---|---|---|
| Type 1 — exact | Only whitespace, comments, formatting | Literal grep |
| Type 2 — renamed | Identifiers, literals, types renamed; structure intact | Token-loosened grep / regex |
| Type 3 — restructured | Statements added, removed, reordered around the copied core | Semantic sweep |
| Type 4 — semantic twin | Same wrong logic, independently or heavily rewritten | Semantic sweep only |

A usable fingerprint has two parts:

1. **The semantic signature** — one or two sentences naming the *mistake and its trigger
   condition*, not the code: "computes the total before filtering exclusions, so excluded
   rows are counted whenever both features are enabled." This survives every mutation
   level, because it describes meaning.
2. **The minimal wrong shape** — the smallest fragment that still contains the mistake
   (often 2–5 lines: the misordered pair of calls, the boundary condition, the missing
   guard). This drives passes 1–2 and gives reviewers something concrete to recognize.

Test the fingerprint before sweeping: it must match the index case, and it must *not*
match the fixed version. A fingerprint that matches both is describing the feature, not
the defect.

## The three-pass sweep

Run cheap-to-deep; record per pass what was searched, so coverage is a checkable claim.

**Pass 1 — literal (Types 1–2).** Grep the codebase for the minimal wrong shape's
distinctive tokens: the unusual identifier, the characteristic constant, the odd call
order. Loosen progressively (drop renamed identifiers, keep structure words). Cheap,
fast, and it also seeds pass 3 with the tokens worth tracing through history.

**Pass 2 — semantic (Types 3–4).** The assistant reads *candidate regions* for the
semantic signature — not the whole codebase line by line, but the places transmission
plausibly reached:
- the same subsystem and its siblings (copy-paste is local before it is global);
- files by the same author cluster around the same period;
- files with similar structure or shared imports (scaffolded from the same origin);
- other repos instantiated from the same template or generator.
For each candidate region, the question is "does this code make the same mistake under
some condition?" — a meaning-level question grep cannot ask. Record hits *and* the regions
cleared, with the same weight: the cleared list is what makes "we checked everywhere
plausible" honest.

**Pass 3 — genealogy (the transmission tree).** Walk version history to date and connect
the instances: when did each contact first appear, and what did its introducing change
copy from? History search on the distinctive tokens (your VCS's pickaxe-style search),
plus commit metadata (author, date, files touched together), usually reveals the copying
events directly — instance C arrived in a commit that visibly duplicated instance A.
Draw the tree: nodes are instances (plus any external source), edges are "copied from."
This is clone genealogy in the Kim et al. sense `[snippet-only]`, done at outbreak scale
rather than corpus scale. The tree's root is your patient-zero lead, and its branching
factors are your R0 data.

## The contact-disposition table

One row per instance found by any pass. No blank dispositions — an undispositioned
contact is an open transmission chain, and the sweep does not close until the column is
full.

| Contact (file:symbol) | Clone type | Found by | Defect triggers here? | Disposition | Evidence / reason | Owner | Date |
|---|---|---|---|---|---|---|---|
| `billing/export.py:sum_rows` | 1 | pass 1 | yes | patched | fix commit ref | — | — |
| `reports/rollup.py:tally` | 3 | pass 2 | no — exclusions filtered upstream | not-applicable | upstream filter noted at call site | — | — |
| `vendor/sync.py:aggregate` | 2 | pass 1 | yes, low traffic | accepted-with-reason | scheduled for next release; risk noted | named owner | revisit date |

Disposition rules:
- **patched** — the fix is applied and verified in that context (not merely copied in).
- **not-applicable** — a *written reason* why the defect cannot trigger there. An
  unreasoned N/A is not a disposition; it is a shrug wearing one's clothes.
- **accepted-with-reason** — a named owner, a written rationale, and a revisit date.
  Acceptance without an owner and date is deferral, and deferrals reopen outbreaks.

## Patient-zero analysis and the infectious-source checklist

Follow the transmission tree to the earliest instance, then take one more step: where did
*that* come from? The usual habitats:

- a public tutorial or Q&A snippet (the pattern arrives already wrong);
- an internal wiki page or "how we do X here" doc;
- a scaffold, starter template, or project generator;
- a shared example repo people copy their first version from;
- one prolific person's habit (the same hands, the same mistake, many sites);
- a code generator or snippet library emitting the pattern.

Then the question that decides whether the outbreak is over — **is the source still
infectious?** The infectious-source checklist:

- [ ] Is the origin snippet/template/page still reachable and still wrong?
- [ ] Is it inside scaffolding that new projects instantiate automatically?
- [ ] Does internal documentation still recommend it?
- [ ] Do code assistants reproduce it — does the codebase's own most-copied example of
      this task still contain the pattern (the examples an assistant or a new hire will
      imitate)?
- [ ] Is the habit-carrier still writing the pattern (a review-time check, kindly)?

Any box ticked means quarantine work remains even if every current contact is patched.

## R0, worked on a small example

R0 at practice level: **the average number of direct copies each instance spawned**, read
off the transmission tree's out-degrees (not an invented epidemiological statistic — just
a name for the tree's branching rate).

Worked example — the sweep found 8 instances (patient-zero template T, its descendants
A–F, and one independent twin G); pass 3's tree shows:

```
template T ──> A ──> B ──> (none)
         ├──> C ──> D ──> (none)
         ├──> E            E, F, G spawned nothing
         └──> F
G (independent Type-4 twin, no edge from T)
```

- Out-degrees: T→4, A→1, C→1, B/D/E/F/G→0.
- Pattern R0 = total transmissions / members of the transmission tree (G, the
  independent twin, arose without transmission and sits outside the tree)
  = 6 / 7 ≈ 0.9 — near 1, so the pattern was still roughly self-sustaining.
- Per-source: **T alone spawned 4** — the high-R0 node. Fixing A–G without fixing T
  leaves expected reinfection on every new project scaffolded from it.
- G is a reminder that R0 isn't everything: independent twins (Type 4) arise without
  transmission, which is why the semantic pass runs even when the tree looks complete.

Decision rule: quarantine effort goes to sources in descending out-degree; a pattern
with R0 ≥ 1, or any live source with out-degree ≥ 2, gets the full quarantine set below.

## Quarantine patterns

Quarantine acts on **sources and pathways**, not on cases (the table already handled the
cases). In descending durability:

1. **Fix the source itself** — the template, scaffold, generator, wiki page, or example
   repo. This is the only action that stops *new* infections.
2. **Lint/CI rule that blocks the pattern** — a mechanical gate at commit or build time,
   with the outbreak-report ID in its failure message so the rule stays explicable years
   later. Mechanism outlives memory.
3. **In-situ warning comment** — placed where the next copy-paster will actually look:
   at the patched sites, in the template, on the wiki page. One or two lines: what the
   trap is, where the fix is, the outbreak-report ID.
4. **Documentation correction** — update the recommending doc; leave a tombstone note at
   the old location if people link to it.

An announcement or team memo is the *least* durable measure and never sufficient alone:
it reaches only the people present, and the next hire copy-pastes from the codebase, not
from the memo.

## The outbreak-report template

```
OUTBREAK REPORT — <pattern short-name>, <date closed>
Index case: <where found, how confirmed, fix ref>
Fingerprint: <semantic signature> | minimal wrong shape: <fragment or link>

SWEEP COVERAGE
Pass 1 (literal): <tokens searched, scope>
Pass 2 (semantic): <candidate regions read AND regions cleared>
Pass 3 (genealogy): <history searched, transmission tree link>

CONTACTS: <N found> — patched <n> / not-applicable <n> / accepted-with-reason <n>
<table or link>

PATIENT ZERO: <earliest instance and its origin>
Source still infectious? <checklist results>

R0: pattern <value>; per-source out-degrees: <top sources>

QUARANTINE: <source fix | lint/CI rule id | in-situ warnings placed | doc corrections>

CLOSURE: all contacts dispositioned <yes/no>; revisit dates: <accepted rows>
```

File it where the next person who meets this pattern will find it — the report's ID in
the lint rule's message is usually how they arrive.
