---
name: adams-smart-brevity
description: >-
  Applies Ken Adams clarity principles plus Axios Smart Brevity to technical, legal,
  professional, clinical, and documentation writing — rejects the "tested language" myth
  (litigated language is bad language), eliminates archaisms, doublets, ambiguity, and
  lawyerisms, and structures everything for scanning: the one most important point first,
  "why it matters" second, short active sentences, bullets and bold, nothing non-essential.
  Use for drafting, editing, or reviewing documents, contract language, clinical notes,
  emails, report writing, code comments, or any request for clear, brief, precise, or
  litigation-resistant language. Triggers: smart brevity, adams smart brevity, writing
  review, language review, edit for clarity, brevity, drafting, clear and precise,
  litigation-resistant, contract language, clinical note language, ambiguity check, tighten
  this email, report writing.
metadata:
  version: "1.0.0"
  source: "Adapted from the user's adams-smart-brevity v1.0.0 spec (2026-08-03)"
---

# Adams + Smart Brevity technical writing

**Axiom: if language has been litigated, it is bad language.** Write and edit so meaning is
unmistakable on the first reading — prefer formulations that prevent misunderstanding over
formulations that merely survived dispute or tradition. Two complementary systems: **Adams**
governs sentence-level meaning (clarity, precision, modern English); **Smart Brevity**
governs document-level attention (lead with the point, format for scanning, stop when done).

## When to use
- Drafting, editing, or reviewing technical documents, contract language, clinical notes,
  legal analysis, emails, reports, prompts, code comments, or professional communications.
- Requests for clear, brief, precise, or litigation-resistant language; language audits,
  ambiguity checks, style improvements.
- Clinical documentation defensibility work (Smile Notes and similar) — this skill governs
  the quality of the language itself; a separate litigation-avoidance pass (not in this
  library) flags sparse or incomplete content.
- Not for: audiences that need the most accessible register (patients, low-literacy, "plain
  English") → `writing-skills:adams-plain-grade` (same Adams core, 5th-grade target).
  Building a master prompt end to end → `coding-agent-skills:master-prompt-architect`
  (whose Adams compliance audit this skill reinforces when both apply).

## Do it
1. **Lead with the one most important point** — the piece's "what's new" — in one sentence.
   Follow immediately with one sentence answering **"Why it matters."**
2. **Apply the Adams rules to every sentence**: no syntactic or semantic ambiguity, no
   archaisms, no doublets or triplets, no lawyerisms or terms needing specialized decoding;
   consistent terminology; subject, verb, object close; active voice wherever the actor
   matters. Where contract language is involved, control meaning with the categories of
   contract language (performance, obligation, discretion, prohibition, policy — see
   `references/adams-and-brevity-checks.md` §3).
3. **Format the rest for scanning**: short paragraphs, bullets, bold key phrases, white
   space; one idea per sentence or bullet; cut everything that is not new, necessary, or
   actionable; stop the moment the point is made — length is not a virtue.
4. **Flag litigated or traditional phrasing** wherever it appears and supply the clearer
   modern alternative (offender list in the reference §2). Treat caselaw as cautionary tales
   of drafting that failed, never as validation.
5. **Clinical notes** (including Smile Notes): controlled vocabulary, explicit
   findings-to-plan chains, zero ambiguous modifiers, no template-clone language (identical
   soft/hard-tissue descriptions across visits are a defensibility hole); Smart Brevity
   structure so the note stays usable under clinical time pressure.
6. **Stay intellectually honest**: never invent clinical facts, consent language, or legal
   conclusions. Precision includes honesty about what is and isn't established.
7. **In reviews, diagnose before fixing**: identify the sources of potential
   misunderstanding first, then propose the fix for each.
8. **Run the dual self-audit** (Adams check + Smart Brevity check, reference §4) before
   finalizing.

## Why / learn
Litigation over meaning proves the original wording failed to express intent clearly enough
to avoid a fight — so "tested by the courts" describes a failure history, not a warranty.
Courts resolve disputes created by defective drafting; they never validate the words that
caused the dispute. That is why the modern precise formulation is *safer* than the
traditional one, not riskier: it leaves nothing to interpret. Smart Brevity is the same
respect applied to attention instead of meaning — the reader under time pressure gets the
point first, the reason second, and a scannable structure for everything else, because a
precise document nobody finishes still fails. The two systems compose cleanly: Adams decides
what each sentence says; Smart Brevity decides which sentences exist and in what order. And
the discipline is self-applying — writing about clarity in unclear language would refute
itself, so this skill's own text follows its rules.

## Common mistakes
- Defending a formula because it is "tested" or traditional → that history is the argument
  against it; supply the modern equivalent.
- Vague quantifiers ("reasonable", "material", "substantially") where precision is required
  → define them or replace them with the measurable intent.
- Long introductory clauses that bury the main point → the point comes first, always.
- Passive voice that hides the actor when the actor matters → name who must act.
- Template-clone clinical language across visits → each note describes *this* visit.
- Treating length as thoroughness → cut to the minimum that delivers complete, precise
  meaning.
- Ambiguous "and/or", misplaced modifiers, unclear pronouns → the syntactic-ambiguity
  checklist in the reference catches these.

## Tailor to your environment
Record in `references/your-environment.md`: your house style and terminology decisions, the
controlled vocabulary for clinical notes, and which document types get the full treatment vs.
a light pass. Keep anything identifying real patients or clients in
`your-environment.private.md` (git-ignored).

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/adams-smart-brevity.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/adams-and-brevity-checks.md — the Adams rules, forbidden-pattern list, contract
  language categories, and the dual self-audit checklist
- references/your-environment.md — house style, controlled vocabulary, scope decisions (fill in)
