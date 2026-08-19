# Adams rules, forbidden patterns, contract-language categories, and the dual self-audit

Preserved from the source spec (adams-smart-brevity v1.0.0, 2026-08-03), organized for use.

Contents: §1 Core Adams principles · §2 Forbidden patterns · §3 Categories of contract
language · §4 Dual self-audit checklist · §5 Interaction notes

## §1 Core Adams principles

**Primary rule: if language has been litigated, it is bad language.**

- Litigation over meaning is evidence that the wording left room to fight over. (Parties
  also litigate clear language opportunistically — but you cannot tell which case you are
  in from the outside, and the drafting fix is the same either way.)
- The claim that language is "tested" or "settled" by courts is a myth. A court's
  construction resolves one dispute on one record; it does not certify the words for your
  contract, with your facts, in your jurisdiction.
- Use caselaw only as cautionary tales of what not to do.
- Express every concept in modern, precise English so that parties and courts never need to
  interpret it.
- Eliminate archaisms, redundancy (doublets and triplets), needless strings, syntactic and
  semantic ambiguity, lawyerisms, and terms that require specialized decoding.
- Prefer standard modern English. Keep terminology consistent. Keep subject, verb, and
  object close.
- Structure for accessibility, so meaning is controlled rather than accidental.
- Goal: the reader never has to fight over what you meant.

## §2 Forbidden patterns (flag and rewrite on sight)

- "indemnify and hold harmless against any and all claims arising out of or relating to…"
  — **flag, but do not cut on this skill's authority.** This is a risk-allocation provision
  (SKILL.md step 4, second carve-out): "any and all" and "arising out of or relating to" are
  fair game as ambiguity, but the verbs are not interchangeable filler. **"Defend" is a
  distinct and often broader obligation than "indemnify"** in many jurisdictions — triggered by
  what is alleged, not by what is finally owed — so a triplet trimmed to "indemnify" can delete
  a duty worth more than the indemnity. Whether "hold harmless" adds anything is contested
  (Adams says no; some courts read it as broader), which is itself the reason to propose rather
  than excise. Draft the clearer version alongside the original, price each cut, and route it
  to a lawyer in the governing jurisdiction. [canon attribution, jurisdiction-dependent.]
- "null and void", "last will and testament", "due and payable"
- "herein", "hereinafter", "said" (as an adjective), "aforesaid", "witnesseth"
- Vague quantifiers without definition ("reasonable", "material", "substantially") when
  precision is required.
- Long introductory clauses that bury the main point.
- Passive constructions that hide the actor when the actor matters.
- Ambiguous "and/or", misplaced modifiers, unclear pronoun references.
- Template clone language — identical soft/hard-tissue descriptions across clinical visits.

For each: prefer the direct modern equivalent that states the intended meaning without the
historical baggage — except where the pattern sits inside a risk-allocation provision or text a
rule prescribes verbatim, where the two carve-outs in SKILL.md step 4 apply and the move is to
propose alongside, never to excise.

## §3 Categories of contract language

Control meaning by choosing the category deliberately. These six carry most drafting;
Adams's full taxonomy also covers agreement, belief, intention, and recommendation.

| Category | Function | Marker verb form |
|---|---|---|
| Language of performance | Accomplishes an action in the signing itself | "hereby [grants/assigns]" |
| Language of obligation | Imposes a duty on a party | "shall" (reserve it for this alone) |
| Language of discretion | Grants permission or choice | "may" |
| Language of prohibition | Forbids | "shall not" / "must not" |
| Language of policy | States rules governing the contract itself | present tense, no "shall" |
| Language of declaration | States a fact a party asserts (a representation) | present tense — "states that", "acknowledges that" — never "shall" |

Most drafting ambiguity comes from category leakage — one "shall" doing every job in the
table. One category per sentence; the verb form signals which. On declarations Adams's own
preference is "states that" over "represents and warrants": the doublet adds remedies
argument, not meaning.

## §4 Dual self-audit checklist (run before finalizing)

**Adams check**
- [ ] No reliance on "tested" or traditional formulations.
- [ ] No syntactic ambiguity (misplaced modifiers, ambiguous "and/or", unclear pronouns).
- [ ] No redundant pairs or triplets.
- [ ] Terminology consistent throughout.
- [ ] Subject–verb–object tight; active voice where the actor matters.
- [ ] Every sentence would be clear to a competent non-specialist reader on first pass.

**Smart Brevity check**
- [ ] The one most important point appears first.
- [ ] "Why it matters" follows immediately.
- [ ] Short sentences and paragraphs.
- [ ] Bullets and bold used for scanability.
- [ ] Nothing non-essential remains.
- [ ] Total length is the minimum that still delivers complete, precise meaning.

## §5 Interaction notes

- **With `writing-skills:adams-plain-grade`**: same Adams core (clarity first, no tested
  language, no ambiguity), different register — plain-grade targets a 5th-grade reading
  level for accessible audiences; this skill targets professional readers under time
  pressure. Choose by audience.
- **With a clinical litigation-avoidance pass** (a content reviewer; not in this library): the
  pass flags sparse, ambiguous, or incomplete *content*; this skill ensures the suggested or
  generated *language* is free of litigated constructions and maximally clear.
- **With `coding-agent-skills:master-prompt-architect`**: its Kenneth A. Adams Compliance
  Audit is reinforced and extended by this skill.
- **Self-application**: the language of this skill itself follows these rules.
