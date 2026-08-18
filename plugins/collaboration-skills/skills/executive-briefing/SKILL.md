---
name: executive-briefing
description: >-
  Gets a decision from a reader with two minutes: writes the answer-first decision
  document — BLUF per Army writing doctrine (DA Pam 600-67, 1986) with Minto's SCQA
  and Pyramid Principle (1996 ed.: answer first, grouped support) — as a one-page
  decision memo (decision requested, options with costs, recommendation, what happens
  if nothing) that passes the completed-staff-work test: could the reader just sign?
  Calibrates the ask up front — inform, decide, or approve. Turns a long analysis,
  client advisory, process-change pitch, or architecture proposal into the page that
  survives one rapid reading; re-leads buried-conclusion drafts; audits a memo for the
  missing ask. Composes with adams-smart-brevity for register; urgent spoken
  escalation goes to SBAR. Use when a decision-maker must act from one page.
  Triggers: executive briefing, executive summary, BLUF, bottom line up front,
  decision memo, one-pager, SCQA, pyramid principle, completed staff work, brief the
  board.
metadata:
  version: "1.0.0"
  source: >-
    Built from the general-use expansion dossier
    (docs/research/general-use-expansion-research.md §6 executive-briefing) —
    research-verified anchors with the misattribution warnings carried as teaching
    content. [snippet-only] marks claims verified via cross-checked search snippets,
    not primary documents; the dossier flags the BLUF-acronym dating and Minto's
    early edition dates as weak, so this skill dates the doctrine and cites the 1996
    edition.
---

# Executive briefing (the one-page decision memo)

Three honest attributions up front, because this library treats provenance as content.
Answer-first is Army writing doctrine: DA Pam 600-67, *Effective Writing for Army
Leaders* (1986), mandated the bottom line up front and defined the standard as
understandable "in a single rapid reading" — the acronym BLUF came later, and claims
dating its first regulation appearance rest on weak sourcing, so date the doctrine, not
the acronym [snippet-only]. The SCQA/pyramid method is Barbara Minto's — credit her by
name; "McKinsey's method" erases the named author — and the load-bearing citation is
*The Minto Pyramid Principle* (1996 edition; earlier edition dates are genuinely messy)
[snippet-only]. Completed staff work carries a dual attribution: best documented to
Archer L. Lerch (*Army and Navy Journal*, January 1942), it also circulates credited to
Brig. G.E.R. Smith (First Canadian Army, 1943), and even friendly reprints concede the
original source is unclear [snippet-only].

## When to use
- Getting a decision from someone whose attention lasts two minutes: an analyst putting
  a variance finding or vendor recommendation in front of leadership, an attorney
  advising a client or partner, an ops manager pitching a process change, a developer
  pitching an architecture choice.
- Compressing a long working artifact — a 20-page analysis, a design doc, a matter file —
  into the one page that survives a single rapid reading.
- Re-leading a draft that buries its conclusion (the IRAC habit, the chronology habit,
  the methods-first habit).
- Auditing a memo before it goes up: is the ask named? could the reader just sign?
- Not for: sentence-level clarity and scanning mechanics — the register these memos are
  written in → see `writing-skills:adams-smart-brevity`; that skill governs the prose,
  this one the decision-document architecture. The two compose.
- Not for: a briefing delivered as slides → see
  `data-analytics-bi-skills:assertion-evidence-deck`.
- Not for: a briefing that is a meeting → see `collaboration-skills:meeting-design`;
  decision rules and the room live there — this skill often writes its pre-read.
- Not for: time-critical spoken escalation ("this is wrong and someone must act now") →
  see `safety-and-reliability-skills:sbar-structured-communication`. SBAR is the
  spoken/urgent channel; this skill is the written, considered decision document. If the
  deadline is minutes, you are in SBAR territory.
- Not for: making an audience *understand* a concept → see
  `writing-skills:explanation-design`; teaching builds understanding, a briefing moves a
  named decision-maker to act.

## Do it
The memo template, the SCQA worksheet, the completed-staff-work checklist, and worked
examples are in `references/briefing-method.md`.

1. **Calibrate the ask before writing a word.** Which do you need: **inform** (no action
   requested), **decide** (the reader picks among options), or **approve** (you
   recommend; the reader signs or objects)? Say which, in the document, near the top. A
   memo with no named ask defaults to "inform," and nothing happens.
2. **Write the bottom line first — one or two sentences.** The recommendation or finding
   plus the ask: what you want, from whom, by when. If the reader stops here, they still
   know what you need.
3. **Frame the story with SCQA.** Situation (what the reader already accepts) →
   Complication (what changed or broke) → Question (the one the complication forces) →
   Answer (your bottom line, again). Two to four sentences total — it earns the reader's
   attention for the answer they just read.
4. **Build the pyramid under the answer.** Group the support into two to four reasons;
   each reason headed by its own one-line assertion; evidence under each. Groups should
   not overlap and should not leave an obvious gap — that is the working meaning of
   Minto's grouping discipline; you need the check, not the consulting vocabulary. Every
   line at one level summarizes the lines below it.
5. **Write the decision memo to its anatomy**: decision requested (with the by-when),
   options with costs — always including "do nothing" and what it costs — recommendation
   with the reason, and what happens if nothing is decided by the date. Options without
   costs are decoration; a missing do-nothing option hides the price of delay.
6. **Run the completed-staff-work test.** Could the reader indicate approval or
   disapproval and be done — no research left, no "thoughts?", no homework transferred
   upward? If acting requires the reader to finish your work, the staff work is not
   complete. Present the solution, not the problem.
7. **Make the register pass.** Short active sentences, point-first paragraphs, scannable
   structure — apply `writing-skills:adams-smart-brevity`; it owns this layer.
8. **Route the artifact.** Going to a room → `collaboration-skills:meeting-design`
   (this memo is a natural pre-read). Going to slides →
   `data-analytics-bi-skills:assertion-evidence-deck`. Urgent and spoken →
   `safety-and-reliability-skills:sbar-structured-communication`.

Division of labor: the assistant compresses the long artifact into the memo, drafts the
SCQA and the pyramid, re-leads buried-conclusion drafts, and audits for the missing ask;
the human owns the recommendation, the walk-in-the-door numbers, and sending the ask.

## Why / learn
Answer-first works because of an asymmetry: the writer knows the conclusion; the reader
does not, and the reader triages. A decision-maker reading page one of a
conclusion-last document is doing unpaid detective work with no guarantee the conclusion
merits it — so they skim, defer, or ask for "a quick summary," and the decision slips.
Leading with the answer converts reading into verification: the reader knows the claim
and reads only as far down the pyramid as their trust requires. That is also why the
pyramid matters as much as the BLUF — each summary line is a checkpoint where a
satisfied reader can stop, and a skeptical one can descend.

BLUF alone has a documented failure mode: an answer with nothing underneath is a hot
take with good posture. SCQA and completed staff work are the governors. SCQA forces
the writer to establish that the question is real before answering it; the
completed-staff-work test forces the answer to be finished — costed options, a
recommendation someone could sign, consequences of inaction — before it claims a
decision-maker's two minutes. Teach the three together; the dossier behind this skill
flags "BLUF alone" as the standard misuse.

The ask-calibration rail exists because decisions default downward. "For your
awareness" and "would love your thoughts" both read as inform, and inform requires
nothing. If you need approval, the word "approve" must appear with a date attached —
the reader can still say no, but silence stops being an answer.

The attribution honesty is not decoration. This skill's anchors are folklore magnets —
an acronym older in memory than in print, a method credited to a firm instead of its
author, a doctrine memo with two claimed fathers. Carrying the uncertainty visibly
("best documented to Lerch, 1942; also credited to Smith, 1943; original source
unclear") models exactly the evidence discipline a decision memo demands of its own
numbers.

## Common mistakes
- Conclusion on page four (IRAC, chronology, methods-first) → re-lead: bottom line and
  ask first, then the pyramid; the reasoning survives, relocated.
- No named ask → the memo defaults to "inform" and dies politely. State inform / decide /
  approve, with a by-when.
- Options without costs → not options, scenery. Cost every option, including do-nothing.
- "Do nothing" omitted → the price of delay stays hidden, and delay wins. Cost it.
- BLUF with no pyramid under it → a hot take. Run SCQA and the grouping check before it
  ships.
- Homework transferred upward ("happy to discuss," "let me know what data you need") →
  completed staff work presents the finished solution; do the work first.
- Dating the BLUF acronym to a specific regulation revision → weak sourcing; date the
  doctrine (DA Pam 600-67, 1986) and say the acronym came later.
- Reaching for this format when the deadline is minutes → that is spoken escalation;
  use `safety-and-reliability-skills:sbar-structured-communication`.
- Demonstrating effort instead of enabling a decision → the reader is not grading
  thoroughness; move the evidence into the pyramid's lower layers or cut it.

## Tailor to your environment
Record house specifics in `references/your-environment.md`: your decision-makers by
role and what each needs to see before signing, house memo formats and length norms,
sign-off and routing conventions, and where decided memos are filed. Anything sensitive
— real names, live decisions, walk-away numbers — belongs in
`your-environment.private.md` (git-ignored), never in a committed file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/executive-briefing.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/briefing-method.md — the ask-calibration rail, BLUF doctrine and its
  dating, the SCQA worksheet, pyramid grouping checks, the one-page decision memo
  template, the completed-staff-work checklist, and worked examples across roles
- references/your-environment.md — your decision-makers, memo conventions, and filing
  (sanitized stub; real detail goes in the `.private.md` twin)
