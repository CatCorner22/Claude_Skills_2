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
  version: "1.0.0"
  source: "Adapted from the user's adams-plain-grade v1.0.0 spec (2026-08-04)"
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
- Not for: professional, technical, or internal writing where the audience handles jargon —
  that is the companion adams-smart-brevity style (not yet in this library; both share the
  same Adams core). Precision contract drafting or clause review — keep the Adams/MSCD
  discipline there, but the grade targets here don't apply.

## Do it
1. **Find the one most important point.** Say it first, in the simplest true sentence.
2. **Tell why it matters** in one short sentence.
3. **Add the rest** in short bullets or very short paragraphs — one main idea per sentence,
   subject–verb–object kept close, active voice, concrete examples.
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

## Tailor to your environment
Record in `references/your-environment.md`: your audience's region and dialect notes, house
terms with their approved plain glosses, and any regulatory phrases that must appear verbatim
(quote them, then explain them in plain words right after). Keep anything identifying real
patients or clients out of git — raw detail goes in `your-environment.private.md`
(git-ignored).

## References
- references/grade-targets-and-checks.md — grade targets, readability measures, the Adams
  rules, and the pre-delivery self-check
- references/your-environment.md — your audience, house glosses, must-keep phrases (fill in)
