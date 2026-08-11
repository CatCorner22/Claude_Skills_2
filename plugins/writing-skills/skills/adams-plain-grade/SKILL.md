---
name: adams-plain-grade
description: >-
  Writes and edits to Ken Adams clarity principles at a 5th-grade reading level (US
  Southeast), falling back to 8th grade only when precision demands it — short active
  sentences, everyday concrete words, one idea per sentence, technical terms explained in
  place, and a hard rejection of litigated "tested language," archaisms, doublets, and
  ambiguity, while keeping meaning exact. Use when the user asks for adams-plain-grade by
  name, or wants plain English, patient or client materials, easy-read text, or writing for
  low-literacy audiences. Triggers: adams plain grade, plain grade, plain english, 5th grade
  reading level, easy to read, easy-read, patient materials, low literacy, simplest accurate
  version.
metadata:
  version: "1.1.0"
  source: >-
    Adapted from the user's adams-plain-grade v1.0.0 spec (2026-08-04). The readability
    lineage in references/grade-targets-and-checks.md §5 is verified via web-search
    snippets; those claims are marked [snippet-only].
---

# Adams plain-grade writing

**Axiom: if language has been litigated, it is bad language.** Write the simplest true
version that still keeps the exact meaning.

## When to use
- Patient or client materials, public notices, and explanations for any audience that needs
  the most accessible accurate version.
- Requests for "plain English," "simple," "5th grade," "easy to read," or low-literacy
  audiences.
- Rewriting dense prose down to an accessible grade without losing exact meaning.
- Not for: professional, technical, or internal writing where the audience handles jargon →
  `writing-skills:adams-smart-brevity` (the companion skill; both share the same Adams
  core). Precision contract drafting or clause review → also
  `writing-skills:adams-smart-brevity` — the grade targets here don't apply there.
- Not for: designing *what* an explanation must accomplish (audience model, entry analogy,
  teach-back) → `writing-skills:explanation-design`; that skill decides what the words must
  do, this one brings the words down to grade.
- Not for: the other ask-for-it-by-name register in this family — participatory, savage
  commentary → `writing-skills:gonzo`.
- Not for: escalations, handoffs, and instructions between professionals, where the fix is
  structure (SBAR, read-back), not reading level →
  `safety-and-reliability-skills:sbar-structured-communication`.

## Do it
1. **Find the one most important point.** Say it first, in the simplest true sentence. (If
   the text's real job is to make the reader *understand* a concept, design the explanation
   first — audience model, entry analogy, concrete-first ordering — with
   `writing-skills:explanation-design`, then apply this register to its words.)
2. **Tell why it matters** in one short sentence.
3. **Add the rest** in short bullets or very short paragraphs — one main idea per sentence,
   subject–verb–object kept close, active voice, concrete examples. If part of the text is
   steps the reader must *perform* (not prose to understand), give that part checklist form —
   `safety-and-reliability-skills:checklist-design` owns the format for action items; this
   skill keeps the surrounding prose at grade.
4. **Enforce the Adams rules while you write** (full list in
   `references/grade-targets-and-checks.md`): no litigated formulas, no archaisms, no
   doublets or triplets, no ambiguity; the simplest accurate modern word; a technical term is
   said once, then explained immediately in plain words; the structure never makes the reader
   guess.
5. **Check the grade.** 5th grade preferred: sentences average 10–14 words, everyday 1–2
   syllable words, Flesch Reading Ease near 90–100 (Flesch-Kincaid near 5.0). Fall back to
   8th grade (sentences up to 15–18 words) only where a precise idea cannot stay accurate at
   5th. Never above 8th. Never fuzz the meaning to hit a lower grade — meaning always wins.
6. **Read it aloud.** It should sound like a clear adult talking to a smart 11-year-old from
   the US Southeast.
7. **Run the self-check** (bundled in the reference) before delivering.

## Why / learn
Courts fight over words exactly because those words failed to say one thing clearly — so
"tested language" is language with a documented failure history, kept alive by precedent
rather than clarity. The simplest accurate modern words carry the same meaning without the
ambiguity that caused the fights. Grade level is a measurement, not a dumbing-down: short
sentences and concrete words cut the reader's parsing work, and the fallback ladder
(5th → 8th, never higher) exists so that precision can never become an excuse for needless
complexity — when accuracy genuinely needs a harder sentence, you take the 8th-grade
allowance instead of blurring the idea. Reading level is not intelligence: busy experts also
read plain text faster and misread it less. The read-aloud test is the real judge because
readability formulas can be gamed by choppy fragments; a text that *sounds* like a clear
adult explaining something is doing the work the numbers only approximate.

## Common mistakes
- Fuzzing the meaning to hit 5th grade → meaning always wins; take the 8th-grade fallback.
- Reaching for "tested" or traditional formulas (herein, aforesaid, indemnify-and-hold-
  harmless doublets) → use the simplest accurate modern word.
- Explaining a technical term late, or never → say it once, explain it right away in plain
  words.
- Long glue sentences with stacked clauses → one main idea per sentence; subject, verb,
  object close together.
- Going above 8th grade because the topic "is complex" → topic complexity never justifies
  sentence complexity.
- Treating the readability score as the goal → it is a check; choppy fragments can game it,
  the read-aloud test cannot be gamed.
- Applying this register to a jargon-fluent professional audience → that flattens precision
  they can handle; route to `writing-skills:adams-smart-brevity`.

## Tailor to your environment
Wire in your current role here — the register is domain-neutral and serves whoever your
accessible-audience readers are wherever you work next: an analyst's public summary, an
attorney's client letters, an ops manager's staff notices, a developer's user-facing
messages. Record in `references/your-environment.md`: your audience's region and dialect
notes, house terms with their approved plain glosses, and any regulatory phrases that must
appear verbatim (quote them, then explain them in plain words right after). Keep anything
identifying real patients or clients out of git — raw detail goes in
`your-environment.private.md` (git-ignored).

## References
- references/grade-targets-and-checks.md — grade targets, readability measures, the Adams
  rules, the pre-delivery self-check, where the targets come from, a worked before/after
  example, and the plain-word ladder
- references/your-environment.md — your audience, house glosses, must-keep phrases (fill in)
