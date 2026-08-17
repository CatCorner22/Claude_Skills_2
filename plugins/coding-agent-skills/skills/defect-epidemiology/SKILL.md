---
name: defect-epidemiology
description: >-
  Treats a confirmed bug as an index case, not a singleton, and contact-traces its spread:
  fingerprints the defective pattern semantically (Type 1–4 code-clone taxonomy), sweeps in
  three passes (literal grep, LLM semantic sweep that catches mutated variants, version-history
  transmission tree), dispositions every contact as patched, not-applicable, or
  accepted-with-reason, finds patient zero (the origin commit, template, tutorial, or shared
  snippet) so reinfection stops at the source, computes the pattern's R0, and quarantines
  high-R0 sources with a template fix plus a lint rule. Grounded in code-clone research
  (ReDeBug, VUDDY, Juergens et al. 2009). Use when a found bug's pattern may live elsewhere, or
  the same bug keeps coming back. Triggers: contact tracing, patient zero, code clone,
  copy-paste bug, everywhere else this appears, outbreak, this bug again, trace the clones,
  quarantine the template.
metadata:
  version: "1.1.0"
---

# Defect epidemiology (contact-trace the bug you just found)

A confirmed bug is evidence about a *population*, not just a line of code. The research is
blunt about it: ReDeBug found unpatched code clones of known-vulnerable code persisting
across entire OS distributions — the patch shipped, and its copies never heard about it
(IEEE S&P 2012) `[snippet-only]`; VUDDY scaled the same hunt with function fingerprints
(IEEE S&P 2017) `[snippet-only]`; and Juergens et al., "Do Code Clones Matter?" (ICSE
2009), found that inconsistent changes to cloned code are frequent and yielded roughly
107 confirmed faults across the commercial and open-source systems studied
`[snippet-only]`. Copy-paste is a transmission vector. This skill is the outbreak
response: index case → fingerprint → contact trace → disposition → patient zero → quarantine.

## When to use
- A bug is confirmed and there is any chance its pattern was copied, templated, generated,
  or independently repeated elsewhere in the codebase (or across repos you own).
- The same class of bug keeps reappearing after being "fixed" — this bug again.
- A vulnerable or defective snippet is known to have circulated: a starter template, a
  wiki example, a tutorial, one prolific person's habit.
- The found-bug step of a change workflow: before closing the fix, trace the contacts.
- Not for: diagnosing and fixing the single bug in front of you — that is ordinary
  debugging, and it happens *before* this skill starts (this skill begins once the
  defective pattern is confirmed and fixed at least once).
- Not for: explaining one incident's causal chain →
  `continuous-improvement-skills:root-cause-analysis` (RCA's unit is the failure and its
  causes; this skill's unit is the *pattern* and its population — retrospective spread
  control, not causal diagnosis).
- Not for: prospective what-could-fail analysis of a design or process →
  `continuous-improvement-skills:fmea` (that anticipates modes before failure; this
  responds to a confirmed one).
- Not for: the review-and-merge workflow itself → `coding-agent-skills:git-and-code-review`
  (this skill adds one step to it: when review finds a real bug, trace the contacts
  before closing).

## Do it
Fingerprinting patterns, the three-pass sweep in detail, the disposition table, R0 math on
a worked example, quarantine patterns, and the outbreak-report template are in
`references/contact-tracing-method.md`.

1. **Confirm the index case and fingerprint the pattern.** Write the defect's *semantic
   signature* — what makes the code wrong and under which conditions it bites — in one or
   two sentences, plus the minimal wrong shape (the smallest code fragment that still
   contains the mistake). The fingerprint must survive renaming and restructuring: "reads
   the length before the null-check, so empty input crashes" traces; the literal text of
   one instance does not.
2. **Trace in three passes, cheap to deep:**
   - *Pass 1 — literal:* grep for the pattern's distinctive tokens and their obvious
     variants. Catches exact and renamed copies (Type 1–2 clones).
   - *Pass 2 — semantic:* the assistant sweeps candidate regions — same subsystem, same
     author clusters, files with similar structure or shared imports — reading for the
     *signature*, not the text. This is the amplification step: restructured and
     semantic-twin clones (Type 3–4) are invisible to grep and prohibitively slow for a
     human to hunt; an LLM reads for meaning at scale.
   - *Pass 3 — genealogy:* walk the version history. When did the pattern first appear,
     and which later commits copied it where? History search on the pattern's distinctive
     tokens plus commit metadata yields the transmission tree (clone-genealogy analysis,
     after Kim et al. `[snippet-only]`).
3. **Disposition every contact in a table.** Each found instance gets a row: location,
   clone type, which pass found it, whether the defect actually triggers there, and
   exactly one disposition — **patched**, **not-applicable** (with the reason the defect
   cannot bite in that context), or **accepted-with-reason** (named owner, written
   rationale, revisit date). No row may be left blank: an undispositioned contact is an
   open transmission chain.
4. **Find patient zero.** Follow the transmission tree to the earliest instance, then ask
   where *it* came from: a tutorial, a public Q&A snippet, an internal wiki page, a
   scaffold or starter template, a code generator, one person's muscle memory. Then the
   critical question — **is the source still infectious?** A patched codebase with an
   unpatched template reinfects on the next project.
5. **Compute R0 and quarantine the high-R0 sources.** R0 here is the average number of
   direct copies each instance spawned (read it off the transmission tree). A pattern
   whose R0 is at or above 1 is still growing. Quarantine acts on sources, not cases: fix
   the template or wiki page itself, add the lint/CI rule that blocks the pattern from
   re-entering, and leave an in-situ warning where the next copy-paster will actually
   look (the old location, the template file, the wiki page).
6. **Close only when every contact is dispositioned, and file the outbreak report:** index
   case, fingerprint, passes run and their coverage, the disposition table, patient zero,
   R0, quarantine actions, and the closure statement. The report is what turns "we fixed
   it everywhere, I think" into a checkable claim.

## Why / learn
The core finding behind this skill is that **patches do not propagate on their own**.
ReDeBug's result generalizes: the fix lands where the bug was *reported*, while the copies
— in other files, other repos, other people's projects scaffolded from the same template —
keep the defect alive `[snippet-only]`. Juergens et al. explain why clones are worse than
mere duplication: the danger is *inconsistent evolution* — one copy gets the fix or the
new requirement and its siblings do not, which is precisely how a fixed bug reappears
`[snippet-only]`. So the closing question after any real fix is never "is this instance
fixed?" but "is this *pattern* extinct or controlled?" — the unit of work is the pattern.

The epidemiological framing earns its keep because each borrowed concept forces a step
people skip. *Index case* forces the reframe from singleton to population. *Contact
tracing* forces exhaustiveness — a sweep is not done when you found "a few more," it is
done when every contact has a disposition, because one undispositioned clone is a live
transmission chain. *Patient zero* forces the origin question, which is what actually
stops recurrence: fixing all current copies while the scaffold that spawns them stays
infectious just schedules the next outbreak. And *R0* forces prioritization by
reproductive power rather than by instance count: a template that spawns four copies per
project matters more than six inert copies in code nobody extends.

The fingerprint must be semantic because transmission mutates. Copy-pasted code gets
renamed, reformatted, and restructured on the way in — the practice-level Type 1–4 clone
taxonomy in the reference maps each mutation level to the pass that can still catch it.
Grep catches Types 1–2; only meaning-level reading catches Types 3–4, which is exactly
where an LLM changes the economics of the sweep (VUDDY industrialized fingerprint matching
for whole ecosystems; a semantic sweep does for your codebase what grep cannot)
`[snippet-only]`. Finally, quarantine prefers *mechanism over memo*: a lint rule that
blocks the pattern at commit time keeps working after everyone has forgotten the outbreak;
an announcement is forgotten by the next hire's first copy-paste.

## Common mistakes
- Fixing the reported instance and closing → the ReDeBug failure mode; the copies stay
  vulnerable. Trace before closing.
- Fingerprinting the literal text → renamed and restructured clones escape; write the
  semantic signature and the minimal wrong shape.
- Grep-only sweeps → Type 3–4 clones are invisible to token search; run the semantic pass
  over candidate regions.
- Sweeping without a disposition table → "I looked around" is not closure; every contact
  gets patched / not-applicable / accepted-with-reason, in writing.
- Patching all copies but not patient zero → the template, wiki page, or scaffold
  reinfects the next project; check whether the source is still infectious.
- Quarantine by announcement → memos decay; add the lint/CI rule and the in-situ warning
  where copy-pasters actually look.
- Treating "not-applicable" as a shrug → it is a claim with a reason (why the defect
  cannot trigger there); an unreasoned N/A is an undispositioned contact.
- Using this skill for a one-off incident diagnosis → that is
  `continuous-improvement-skills:root-cause-analysis`; here the unit is the pattern.

## Tailor to your environment
Wire in your current systems in `references/your-environment.md`: the repositories and
shared code locations a sweep must cover, where your templates/scaffolds/generators and
snippet wikis live (the usual patient-zero habitats), how lint/CI rules are added in your
stack, and where outbreak reports are filed. Keep committed content structural — real
repo names, vulnerability details, or anything sensitive belongs in
`your-environment.private.md` (git-ignored), never in a committed file.

## References
- references/contact-tracing-method.md — the Type 1–4 fingerprinting taxonomy, the
  three-pass sweep, the contact-disposition table, patient-zero analysis with the
  infectious-source checklist, R0 worked on a small example, quarantine patterns, the
  outbreak-report template, and the research anchors
- references/your-environment.md — your sweep scope, template locations, and lint
  infrastructure (fill in)
