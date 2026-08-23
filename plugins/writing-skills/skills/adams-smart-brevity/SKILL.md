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
  version: "1.5.0"
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
- Clinical documentation defensibility work — this skill governs the quality of the *language*
  only. Whether the content is adequate — the right findings, the pertinent negatives, the
  consent discussion — is a clinician's review, and **this library does not contain one**; do
  not treat that gap as covered by a later pass. See step 5 for the record-integrity rules
  (amend, never edit) that apply before any editing begins.
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
   contract language — performance, obligation, discretion, prohibition, policy, and
   declaration for a fact a party asserts ("the Seller states that…", never "shall"). The
   full table, and the four rarer categories, are in
   `references/adams-and-brevity-checks.md` §3.
3. **Format the rest for scanning**: short paragraphs, bullets, bold key phrases, white
   space; one idea per sentence or bullet; cut everything that is not new, necessary, or
   actionable; stop the moment the point is made — length is not a virtue.
4. **Flag litigated or traditional phrasing** wherever it appears and supply the clearer
   modern alternative (offender list in the reference §2). Treat caselaw as cautionary tales
   of drafting that failed, never as validation.
   - **Say when a position is Adams's rather than settled.** Several of the rules this skill
     applies are live arguments among transactional drafters, not consensus — "hold harmless"
     as a synonym for "indemnify", "represents and warrants" collapsing to "states that", and
     how far to restrict "shall". Reference **§3b** maps each one and the standard counter-case.
     Present those as *this method's position, and here is where the bar disagrees*; presenting
     a contested position as settled is how a drafter takes a rule to a partner, finds it is an
     argument, and stops trusting the method. The archaisms with no contested defence —
     *herein*, *aforesaid*, *witnesseth*, *null and void*, buried leads, ambiguous "and/or" —
     get the axiom at full force, and §3b explicitly does not shelter them.
   - **Carve-out: some wording is legally required to appear verbatim, and clarity does not
     override it.** Statutory or regulatory language a rule prescribes word-for-word,
     safe-harbour text whose protection depends on tracking the statute, conspicuousness
     requirements (a warranty disclaimer that must mention "merchantability" under UCC 2-316),
     required notices in consumer, employment, securities, or medical-consent documents, and
     defined terms already in force elsewhere in the same instrument — all of these are archaic
     *and* load-bearing. Rewriting them for clarity can void the protection they exist to
     create. **Flag them, propose the plain-language version alongside rather than instead of
     the required text, and route the decision to a lawyer.** Never silently modernise language
     that a rule requires; the point of this skill is drafting that survives, and a clearer
     clause that forfeits a safe harbour has not survived.
   - **Second carve-out: risk-allocation provisions, where the caselaw is the specification.**
     Indemnities, defence obligations, limitations of liability, exculpatory and
     hold-harmless clauses, warranty disclaimers, and insurance-procurement covenants are not
     ordinary business terms whose litigation history is a failure log. They are the
     provisions courts construe *strictly and against the drafter*, and their enforceability
     often turns on the presence of particular words. Three consequences that cut directly
     against this skill's default rules:
     - **The doublet may not be a doublet.** "Indemnify, defend, and hold harmless" looks like
       exactly the archaic triplet step 2 says to cut — but in many jurisdictions **"defend" is
       a distinct and broader obligation than "indemnify"**: the duty to defend is triggered by
       what is *alleged* and arises at the outset, while indemnity turns on what is ultimately
       *owed*. Deleting the word as redundancy can silently delete a duty worth more than the
       indemnity itself. (Whether "hold harmless" adds anything to "indemnify" is genuinely
       contested — Adams argues it does not, and some courts read it as broader. That
       disagreement is the reason to flag rather than to cut.) [canon attribution — the
       defend/indemnify distinction is standard doctrine, stated here without re-verification;
       it is jurisdiction-dependent.]
     - **Some allocations require express, conspicuous words to work at all.** An indemnity
       covering the indemnitee's *own* negligence must, in a number of jurisdictions, say so
       expressly and conspicuously or it is unenforceable as to that risk — Texas's express
       negligence doctrine is the sharpest form [canon attribution, not re-verified]. The
       belt-and-suspenders phrasing that offends Adams is sometimes the element that makes the
       clause operative.
     - **Contra proferentem inverts the usual incentive.** Ambiguity in these clauses is
       resolved against the party who drafted them, so tightening one for readability while
       narrowing its scope by accident hands the counterparty the construction.
     **So: in risk-allocation language, do not cut on this skill's authority.** Diagnose as
     normal — name the ambiguity, the archaism, the buried actor — and produce the clearer
     draft *alongside* the original, with the specific risk each proposed cut carries, for a
     lawyer in the governing jurisdiction to decide. Reformatting for scanning (structure,
     white space, defined terms, bold on a liability cap) is safe and valuable here; **excision
     is not.** Where the skill's axiom and the caselaw disagree, the caselaw is the
     specification.
5. **Clinical and other filed records**: controlled vocabulary, explicit
   findings-to-plan chains, zero ambiguous modifiers, no template-clone language (identical
   soft/hard-tissue descriptions across visits are a defensibility hole); Smart Brevity
   structure so the note stays usable under clinical time pressure.
   - **Never edit a signed or filed record — amend it.** Once a note, chart entry, or client
     record is signed or filed, the correction is a **dated, attributed addendum that leaves
     the original legible**, not a revision of the text. This overrides everything else in this
     skill for that document. A cleaner version of a filed note, with the original gone, is the
     single worst outcome an editing pass can produce: the improvement is invisible and the
     alteration is not, and the record's value as evidence depends on its integrity rather than
     its prose. Most systems audit-log this; the ones that silently overwrite are the dangerous
     ones. (`safety-and-reliability-skills:split-tally-evidence` is the same principle applied
     to record design.)
   - **Brevity does not cut the defensive content.** "Cut everything that is not new, necessary,
     or actionable" is a rule about *prose*, and it pulls hard against the items whose whole
     value is that they are on the record: **pertinent negatives, the differential considered
     and rejected and why, the consent discussion, documented non-adherence or refusal, and
     advice given.** They look redundant to an editor and decisive to a reviewer years later.
     Tighten how they are written; do not decide they are surplus.
   - **Whether the content is complete is a clinician's judgment, not this skill's.** This skill
     governs the language. Nothing in this library reviews a clinical record for adequacy of
     content, and no other skill is waiting to catch it — say so plainly rather than implying a
     later pass will.
6. **Stay intellectually honest**: never invent clinical facts, consent language, or legal
   conclusions. Precision includes honesty about what is and isn't established.
7. **In reviews, diagnose before fixing**: identify the sources of potential
   misunderstanding first, then propose the fix for each.
8. **Run the dual self-audit** (Adams check + Smart Brevity check, reference §4) before
   finalizing.

## Why / learn
Litigation over meaning is evidence that the wording left room to fight over — so "tested by
the courts" describes a failure history, not a warranty. A court's construction resolves one
dispute on one record; it does not certify the words for your contract, your facts, or your
jurisdiction. That is why the modern precise formulation is *safer* than the traditional
one, not riskier: it leaves nothing to interpret.

**Know where that axiom stops.** It holds for language whose only job is to convey meaning —
which is nearly everything. It does not hold for the two categories in step 4: text a rule
prescribes word-for-word, and risk-allocation provisions whose effect is fixed by rules of
construction rather than by ordinary reading. In that second category the relationship
inverts. A clause has been litigated *because* it is the operative allocation of a real risk,
and the resulting caselaw is not a record of drafting that failed — it is the specification
telling you which words carry the allocation. Clarity there is still worth pursuing; it is
simply no longer the thing that decides whether the clause works, so it stops being this
skill's call to make alone. Smart Brevity is the same
respect applied to attention instead of meaning — the reader under time pressure gets the
point first, the reason second, and a scannable structure for everything else, because a
precise document nobody finishes still fails. The two systems compose cleanly: Adams decides
what each sentence says; Smart Brevity decides which sentences exist and in what order. And
the discipline is self-applying — writing about clarity in unclear language would refute
itself, so this skill's own text follows its rules.

## Common mistakes
- Defending a formula because it is "tested" or traditional → that history is the argument
  against it; supply the modern equivalent — *unless* it is prescribed verbatim by a rule or
  is a risk-allocation provision, the two carve-outs in step 4.
- Cutting "indemnify, defend, and hold harmless" down to "indemnify" as a triplet → "defend"
  is a separate and often broader obligation in many jurisdictions; propose, do not excise,
  and let a lawyer in the governing jurisdiction decide.
- Tightening an indemnity or liability cap for readability without pricing the scope change →
  these clauses are construed strictly and against the drafter, so an accidental narrowing is
  a gift to the counterparty; reformat freely, excise never.
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
a dirty tree. Copy it into your own project — `.claude/skills-env/adams-smart-brevity.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/adams-and-brevity-checks.md — the Adams rules, forbidden-pattern list, contract
  language categories, and the dual self-audit checklist
- references/your-environment.md — house style, controlled vocabulary, scope decisions (fill in)
