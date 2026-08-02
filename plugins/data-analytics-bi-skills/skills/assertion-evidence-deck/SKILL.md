---
name: assertion-evidence-deck
description: >-
  Builds assertion-evidence presentations (the Marshall/Alley method: one full-sentence claim per
  slide, proven by a visual, every number sourced) from verified analysis or configuration findings
  — for data-analysis results, Oracle Fusion Cash Management, reconciliation, audit findings, and
  University of Tennessee Controller or leadership updates. Turns verified output into slides; it
  does not run the analysis or Oracle diagnosis. Use when the user asks for a deck, slides,
  PowerPoint, briefing, readout, or leadership/Controller update on Oracle CM, DASH, unreconciled
  items, parse/matching/tolerance/transaction-creation rules, cash positioning, audit remediation,
  or an analysis result — even without saying "assertion-evidence" — or to audit an existing deck.
  Triggers: build a deck, make slides, PowerPoint, briefing, leadership update, Controller update,
  readout, TED-style technical talk, sentence-headline slides, snorkel vs scuba, turn this report
  into slides, audit my deck.
---

# Assertion-evidence deck

Build presentations that survive an auditor, a skeptic, and a busy Controller. Every slide states
one claim in a full sentence and proves it with a picture; every number carries a source.

## When to use
- Turning a verified analysis, an Oracle Cash Management config review, or an audit-response into
  slides — a deck, briefing, readout, or leadership/Controller update.
- Building a "TED-style" technical talk with sentence-headline slides instead of bullet dumps.
- Auditing an existing `.pptx` against the assertion-evidence checklist.
- Not for: performing the underlying data analysis → use the data-analytics/statistics skills; the
  Oracle CM configuration diagnosis → `oracle-fusion-finance-skills:fusion-cm-production-troubleshooting`
  or `oracle-cm-config-review`; XML-level `.pptx` editing the builder can't express → the `pptx`
  skill. This skill turns *verified* output into slides; run the analysis under its own skill first.

## Do it
Run seven stages in order. Each names what it produces, so you can stop, hand off, or resume at any
boundary. **Skipping stage 2 is the failure mode that matters** — a deck that reaches a Controller
with an unsourced number costs more credibility than one that openly reports a gap.

| # | Stage | Produces |
|---|---|---|
| 1 | Scope the talk | Audience, duration, single main claim |
| 2 | Gather evidence | Source ledger of verified facts |
| 3 | Choose the spine | Ordered list of slide headlines |
| 4 | Design each slide | Evidence plan per headline |
| 5 | Build the file | `.pptx` on disk |
| 6 | Audit the file | Lint report + visual check |
| 7 | Deliver | File, source ledger, gap list |

**Stage 1 — Scope the talk.** Settle four things before writing a headline; ask the user rather
than guess at audience or duration. (1) **Audience** — who decides something because of this deck?
(2) **Duration** — budget ~1 minute per body slide (a 15-min slot ≈ 10–12 body slides + title +
summary). (3) **Main claim** — one sentence everything supports; if the user can't state it, draft
2–3 and let them pick. (4) **Depth** — the slide stays at *snorkel* depth (the surface statement a
non-specialist grasps); *scuba* depth (mechanism, caveats, rule IDs) goes in the speaker notes.

**Stage 2 — Gather evidence.** Read `references/evidence-discipline.md` first. Every number, date,
name, and comparison that reaches a slide must trace to a named source with a date, recorded in a
**source ledger** (claim, value, source, source date, tier). Tier each claim: **Verified** (read
from a named artifact this session — goes on a slide), **Reported** (from the user or a prior
summary — slide only with confirmation and an "as reported" tag), **Inferred** (derived/estimated/
remembered — never a bare number on a slide; verify it or convert it to a stated gap). For UT Oracle
CM work, read `references/oracle-cm-domain.md` for vocabulary and where live figures live — treat it
as orientation only, never as evidence.

**Stage 3 — Choose the spine.** Write the headlines first, as a plain numbered list, and show them
to the user before building anything — the headline list *is* the talk. Each headline states a
complete sentence (subject + verb), asserts something falsifiable, and runs ≤ 2 lines (~105 chars
at 28 pt across 11.52 in — verify by rendering, not counting).

| Weak | Strong |
|---|---|
| Transaction Creation Rules | Transaction Creation Rules generate more noise than signal |
| Tolerance settings | A single 30-day tolerance window undermines date integrity |
| Next steps | Enabling AutoRecon requires three configuration changes first |

A narrative arc for a findings/remediation talk: (1) inherited condition → (2) the system as it
actually runs (one map, with scale) → (3) defects, one headline each → (4) what the team built →
(5) evidence it works, honestly bounded → (6) what remains open → (7) the ask → (8) summary
(restate the stage-1 claim).

**Stage 4 — Design each slide.** Read `references/ae-method.md` for the full checklist and
evidence-type guide. Three style rules govern every body slide: (1) the headline is a
sentence-assertion, left-justified, ≤ 2 lines; (2) visual evidence supports it — a diagram, chart,
table, photo, or words/numbers arranged spatially, **not a bullet list**; (3) words appear only
when necessary (design for ≤ 20 words read per minute; ≤ ~20 body words on a one-minute slide).
For each headline write the evidence plan: the claim, the evidence type and what it shows, the 3–8
label words, the source tag, and the speaker note carrying the scuba detail. Match evidence to the
claim — distribution → chart, sequence → flow diagram, magnitude → 2–4 large numbers, structure →
labeled diagram. Over ~40 body words means the claim is too big — split the slide.

**Stage 5 — Build the file.** Prefer **Path A**, the bundled builder: write a deck spec as JSON and
run `python scripts/build_deck.py deck_spec.json -o output.pptx` (add `--brand ut` for the UT
palette). It encodes the geometry, typography, and colors in `references/design-tokens.md`, so
slides come out compliant, and it rejects a headline that busts the two-line budget rather than
overflowing it. `assets/deck_spec_example.json` is a worked example; `--schema` prints the field
list and the eight slide kinds. **Path B** — the official Microsoft template Melissa Marshall
co-authored (PowerPoint → File > New → search `assertion evidence` → Create): deliver slide-by-slide
text keyed to that template. Use Path B when the user asks for the template by name. For anything
the builder can't express, use the `pptx` skill and keep this skill's geometry and evidence rules.

**Stage 6 — Audit the file.** Never deliver a deck you have not seen rendered. Lint it —
`python scripts/ae_lint.py output.pptx` (reports headline violations, bullet characters, word-count
overruns, banned formatting, missing source tags, font problems; exits non-zero on error) — then
**look at every slide**: convert to images and check for overflow, overlap, colliding source tags,
and low contrast, which the linter cannot see. Fix the generator and rebuild; do not hand-patch the
packed XML.

**Stage 7 — Deliver.** Hand over three things together: the **deck** (dated with the build date),
the **source ledger** (claim-to-source table), and the **gap list** (what the deck could not
establish and what would close each gap). Then offer a short prose summary at scuba depth for the
speaker's own preparation — the speaker needs to know more than the slides show.

## Why / learn
A bullet-list slide makes the audience hold fragments in working memory and assemble the argument
themselves while the speaker talks over them — reading and listening compete for one channel, so
they do neither well. An assertion-evidence slide removes that work: the headline hands over the
conclusion in one sentence, the visual supplies the proof, and the audience reads one sentence,
looks at one picture, and listens. The method also disciplines the *speaker* — a headline that
cannot be written as a falsifiable sentence signals a slide with no point, which is worth
discovering while drafting rather than mid-talk. The **snorkel/scuba** split keeps the screen at the
"so what?" level while the mechanism waits in the notes for questions. And the governing evidence
rule is an asymmetry every reconciler already knows: **a wrong number costs more than a missing
number.** A missing figure invites a question you can answer with command of the problem; a wrong
figure, once found, retroactively taints every correct figure beside it, because the audience can no
longer tell which claims were checked. Prefer the honest gap.

## Common mistakes
- Topic-label headline ("Next steps") → write headlines first, as full sentences.
- Headline runs three lines → it holds two claims; split into two slides.
- Bullet list under a good headline → convert to a diagram, table, or labeled 2–4 item trio.
- Chart pasted in with no annotation → circle/arrow/bold the feature the headline names.
- Body text over ~40 words → the claim is too large; split it, move detail to notes.
- Unsourced number → verify it against a named artifact, or convert it to a stated gap.
- Fifty slides for a 20-minute slot → budget ~1 minute per body slide in stage 1 and cut to fit.
- Jargon-only headline for a leadership audience → keep the term, add the consequence ("…, which
  strands real subledger activity").
- Tennessee Orange text on white → it fails WCAG contrast; set text in Smoky Mountain Gray (see
  design-tokens).

## Tailor to your environment
Record your setup in `references/your-environment.md` (keep real figures, client names, and audit
numbers in `your-environment.private.md`, which is git-ignored). Capture your audiences and the
decisions each deck serves, your brand palette and fonts (the tokens ship with the UT System
defaults), the artifacts your figures come from, and any house deck conventions. For UT Oracle Cash
Management work, `references/oracle-cm-domain.md` carries the ecosystem vocabulary and the map of
where live figures live — always re-read the underlying artifact before any figure lands on a slide.

## References
- references/ae-method.md — full checklist, evidence-type guide, failure modes, before/after examples
- references/design-tokens.md — verified geometry, UT System palette and typography, font-substitution rule
- references/evidence-discipline.md — claim tiers, source-ledger format, source-tag wording, gap language
- references/oracle-cm-domain.md — Oracle CM vocabulary, processing chain, where live figures live
- references/your-environment.md — your audiences, brand, and artifacts (add when supplied)

## Scripts
- `scripts/build_deck.py` — deck spec (JSON) → compliant `.pptx`. `--schema` prints the spec format and eight slide kinds; `--brand ut|neutral` and `--font` control theme.
- `scripts/ae_lint.py` — audits any `.pptx` against the assertion-evidence checklist. `--json` for machine output; exits non-zero on error.
