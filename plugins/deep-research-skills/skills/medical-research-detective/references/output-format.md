# Output format — the case file

Read at stage 7. How to present deep research so it is comprehensive *and* understandable, actionable
*and* safe.

## Contents
- [Structure](#structure)
- [The two-layer principle](#the-two-layer-principle)
- [Writing for understanding](#writing-for-understanding)
- [Confidence labels](#confidence-labels)
- [Making it actionable without giving advice](#making-it-actionable-without-giving-advice)
- [Red flags: the urgent-care list](#red-flags-the-urgent-care-list)
- [Safety framing](#safety-framing)
- [Length](#length)

## Structure

Use `assets/case-file-template.md`. Sections in this order:

1. **Bottom line** — 3–6 sentences of plain language. What the research suggests, the single most
   promising lead, and the most important next step. A reader who stops here gets real value.
2. **The case** — the findings, timeline, medications, and what has been ruled out, as understood.
   Lets the user correct a wrong premise before reading conclusions built on it.
3. **Hypotheses considered** — ranked. Each with: what it is, how well it fits, **evidence for**,
   **evidence against**, what it fails to explain, confidence grade, and how it could be checked.
   Include the ones that were ruled out and why — that is how the reader knows the search was wide.
4. **The dot-connections** — the heart of the report. Each connection: the finding(s) linked, the
   proposed mechanism or bridge, its strength grade, the supporting citations, and — explicitly —
   whether any published source connects them directly or whether this is a bridge across separate
   literatures.
5. **Questions for your clinician** — specific, answerable questions, phrased so the user can read
   them aloud, each with a one-line note on why it matters.
6. **Tests or evaluations the literature suggests** — what could distinguish among the hypotheses,
   with what each would show. Framed as "the literature uses X to distinguish Y" — a discussion item
   for the clinician, never an instruction.
7. **Red flags** — symptoms warranting urgent evaluation (see below). Always present.
8. **What we could not establish** — gaps, unrun searches, paywalled sources, contested evidence.
9. **Search log** — queries, databases, hit counts, what was kept (from `search-strategy.md`).
10. **References** — every source with verification status label and country.
11. **Appendix A — excluded-source leads** — the quarantine tier (`source-provenance.md`), only if
    non-empty.

## The two-layer principle

Comprehensive and understandable are not in tension if they are **layered**: plain language on top,
technical grading beneath.

- Every section leads with a sentence a non-specialist can act on, then supplies the graded detail.
- A clinician reading only the technical layer gets a defensible evidence summary; a patient reading
  only the top layer gets an accurate, non-misleading picture. Neither is misled by the other's
  omissions.
- Never bury the actionable conclusion under methodology.

## Writing for understanding

- **Define each technical term once, in place**, then use it consistently: "peripheral neuropathy
  (nerve damage causing numbness or tingling, usually starting in the feet or hands)."
- **Give numbers with context.** Not "significantly increased risk" but "risk rose from about 2 in
  1,000 to about 5 in 1,000 over five years."
- **Say what is uncertain, in words**, not just as a grade: "only two small studies have looked at
  this, and they disagree."
- **Prefer short sentences for the important claims.** Complexity belongs in the evidence, not the
  grammar.
- **Never use certainty language for a lead.** "May," "one possible explanation," and "no study has
  tested this directly" are load-bearing.
- Use tables for parallel comparisons (hypotheses, tests, evidence for/against) — they make the
  weighing visible.

## Confidence labels

Show the grade next to the claim, at the moment it is read. Connection strength grades come from
`dot-connection-method.md`; evidence confidence from `evidence-appraisal.md`:

> **Hypothesis 1 — [drug]-associated [nutrient] deficiency.** Confidence: **Moderate**. Connection:
> **Supported** (several consistent cohort studies; no randomized trial).

Pair every grade with the plain-language equivalent the first few times: "**Lead** — meaning this is
worth checking, not something the research has established."

## Making it actionable without giving advice

The distinction that keeps this useful *and* safe:

| Not this (advice) | This (research + question) |
|---|---|
| "You should start taking B12." | "The literature associates this drug with B12 depletion; ask whether testing your B12 — and methylmalonic acid, which the literature notes is more sensitive — is warranted." |
| "Stop that medication." | "The timing of your symptoms relative to this medication is the kind of pattern the literature flags; ask whether it is worth reviewing." |
| "You have condition X." | "Condition X fits four of your five findings; the literature distinguishes it from Y using test Z." |
| "This dose is too high." | "Dosing in the studies reviewed ranged from A to B in this population; the clinician can say how that maps to your situation." |

Actionability comes from **specificity of the question**, not from telling someone what to do. A user
who walks into an appointment with three precise questions and the citations behind them has gotten
enormous value without ever receiving medical advice.

## Red flags: the urgent-care list

**This list is a triage gate, not a report section.** Run it against the presented findings as
stage 0 — before framing, hypotheses, or searching (SKILL.md). When one is present it leads the
reply; it does not wait at the bottom of a long report. Always include the section in the written
output as well. Tailor it to the case, and always cover the general categories — symptoms that
warrant prompt evaluation rather than more research:

- Chest pain or pressure; sudden shortness of breath
- Sudden weakness/numbness on one side, facial droop, trouble speaking, or the worst headache of
  one's life
- Fainting, or new confusion or altered consciousness
- Coughing or vomiting blood, or black/tarry stools
- High fever with stiff neck, or fever in someone immunosuppressed
- Rapidly worsening or unrelenting pain
- New severe shortness of breath at rest, or a rapidly swelling limb
- Any symptom that is sudden, severe, and unlike anything experienced before
- Thoughts of self-harm

Time-critical presentations that are easy to research past because each looks like a common
complaint until it is asked about specifically:

- **New back pain with saddle numbness, new urinary retention or incontinence, or bowel
  incontinence** — cauda equina syndrome; the window for surgery is measured in hours
- **New headache in an adult over ~50 with scalp tenderness, jaw pain on chewing, or any visual
  change** — giant cell arteritis; untreated, vision loss can be sudden and permanent
- **Rapid-onset hives, lip or tongue swelling, wheeze, or faintness after an exposure** — anaphylaxis
- **A first seizure at any age**
- **Sudden severe testicular pain or scrotal swelling** — testicular torsion; also hours, not days
- **Bleeding, severe abdominal pain, severe headache, or visual change in pregnancy or within six
  weeks of delivery**

Phrase it plainly: "These are reasons to seek care now rather than research further. If any of these
are present, contact emergency services or go to an emergency department."

## Safety framing

State once at the top, clearly and without hedging, and reinforce where it matters:

> This is a review of published research, not medical advice. It cannot diagnose, and it does not
> know things about your body that an examination and your records would reveal. Nothing here is a
> reason to start, stop, or change any medication or treatment. Its purpose is to give you and your
> clinician better questions and the evidence behind them.

Then keep the substantive commitments throughout:
- **No diagnosis.** Hypotheses are named as hypotheses.
- **No dosing**, and no "try this."
- **Never contradict the user's clinician** — the clinician has the examination and the records. Where
  the literature seems to point elsewhere, frame it as a question to raise, not as an error to correct.
- **Do not alarm.** Include base rates when naming a serious possibility; "this is rare, and the
  common explanations should be excluded first" is part of accurate reporting.
- **Do not minimize either.** If the literature genuinely supports concern about a pattern, say so
  plainly and route to the red-flag list.
- **Respect the boundary on request type.** If asked to diagnose or to recommend a treatment, decline
  that specific framing, then deliver the research and the questions instead — which is usually what
  the person actually needed.

## Length

Match the case. A single verification question needs a paragraph and a table; a multi-symptom
investigation earns several pages. Long is fine when every section carries weight — but the **Bottom
line** must stay short regardless, and nothing should be padded to look thorough. If a section has
nothing in it (no excluded-source leads, no red flags applicable), say so in a line or omit it rather
than filling it.
