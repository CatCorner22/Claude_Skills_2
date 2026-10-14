---
name: mscd-contract-drafting
description: >-
  Drafts, reviews and redlines contract language to Ken Adams's A Manual of Style for Contract
  Drafting (MSCD) — the categories of contract language (shall only for a party's duty, present
  tense for policy, may for discretion), defined terms, efforts standards, provisos, "including",
  numbers and time periods — and delivers every edit as a Smart Brevity redline note: what changed,
  why it matters, what needs a lawyer's call. Ships a linter that keys findings to sections and
  never cuts risk-allocation or prescribed wording. Use for drafting a clause, redlining or
  reviewing an agreement, converting a template to MSCD style, or explaining why a clause is
  ambiguous. Not for memos or emails → writing-skills:adams-smart-brevity. Triggers: MSCD, Ken
  Adams, contract drafting, redline this agreement, review this contract, draft a clause, shall vs
  must, categories of contract language, defined terms, contract style guide, lint this contract,
  plain-language contract.
metadata:
  version: "1.0.0"
  source: >-
    Built on the approach of Kenneth A. Adams, A Manual of Style for Contract Drafting (5th ed.,
    ABA 2023), paraphrased and attributed, never quoted at length — own the book. MSCD positions are
    marked [canon attribution] where not re-verified against the text; contested positions are
    stated as contested. Smart Brevity (VandeHei, Allen & Schwartz, 2022) supplies the delivery
    format for cover notes.
---

# MSCD contract drafting (with Smart Brevity delivery)

Contract language is a stylized dialect with one job: to state the deal so precisely that nobody
has to interpret it. Ken Adams's *A Manual of Style for Contract Drafting* is the most rigorous
account of how to do that, and this skill applies its system — **decide what each sentence is doing,
then use the verb form that does exactly that** — to drafting, reviewing and redlining. A bundled
linter does the mechanical half; the judgment calls stay with the drafter, with the test to apply
written next to each one. Every deliverable leaves in Smart Brevity form, because the reader is a
partner or a client who will read the first two lines and decide.

## When to use
- Drafting a clause, a schedule or a whole agreement, from a term sheet or from scratch.
- Reviewing or redlining the other side's paper, or your own template, for clarity and consistency.
- Converting a legacy form ("WITNESSETH", "shall" on every line) to MSCD style.
- Explaining to a colleague or client why a clause is ambiguous and what the fix is.
- Not for: memos, emails, client letters and other prose → `writing-skills:adams-smart-brevity`
  (same Adams core, document-level attention rules). A plain-English summary for a non-lawyer →
  `writing-skills:adams-plain-grade`. Finding and verifying the authorities a clause relies on →
  `legal-skills:legal-citation-research`. What an employment agreement, handbook or release must
  contain → `legal-skills:employment-law-issues` (this skill then drafts the words).

## Do it

1. **Fix the frame before touching a word.** Record: the governing law; whether the instrument is
   a fresh draft, a template conversion, or an agreement under negotiation or already in force; the
   house verb of obligation (`shall`, MSCD's default, or `must`); and who owns the decisions the
   review will surface. An instrument in force changes every contested item from *edit* to *flag*,
   because a wording change there can change the deal.

2. **Run the linter first, and read its first four lines before any finding.**
   ```
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/mscd-contract-drafting/scripts/mscd_lint.py" contract.docx
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/mscd-contract-drafting/scripts/mscd_lint.py" contract.docx --review
   ```
   The header counts every `shall` and sorts them into obligation-looking, policy, discretion and
   passive — that ratio is the state of the document in one line. Findings are keyed to the section
   they sit in, so work section by section. Three severities: `edit` is a replacement you can apply
   as written; `flag` is a lawyer's decision (contested, or inside a rail); `info` is a heuristic
   worth a look. Nothing the linter says is a verdict on substance.

3. **Put every sentence in its category of contract language.** This is the core of MSCD and of
   this skill: the verb form signals what the sentence does. The working set —
   | Category | What it does | Verb form |
   |---|---|---|
   | Obligation (on the subject) | imposes a duty on the party that is the subject | *Acme shall pay* |
   | Obligation (on someone else) / requirement | a duty whose subject is not the party, or a condition | *Notice must be in writing* |
   | Discretion | grants a choice | *Acme may terminate* |
   | Prohibition | forbids | *Acme shall not assign* |
   | Policy | a rule of the contract, no actor | *This agreement terminates on …*, *"Fee" means …* |
   | Declaration | a fact a party asserts | *Acme states that …*, *Zenith acknowledges that …* |
   | Performance | an act done by the signing itself | *Acme hereby grants* |
   | Agreement / intention / belief / recommendation | the rarer four | *agrees*, *intends*, *believes*, *recommends* |
   The one test that resolves most disputes: **swap `shall` for `has a duty to`; if the sentence
   still makes sense, `shall` is right, otherwise it is not.** "This Agreement *has a duty to*
   terminate" fails, so it is policy: *terminates*. Full taxonomy, the `will`/`must`/`may not`
   decisions and a worked rewrite: `references/categories-of-contract-language.md`.

4. **Discipline the defined terms.** Define a term only if it is used more than once and the
   definition saves words or removes doubt; `"Term" means …` (never *shall mean*); no obligations
   hidden inside definitions; the same words for the same thing every time, and nothing else ever
   capitalised. The linter reports terms defined but unused and terms used like defined terms but
   never defined. `references/defined-terms-and-structure.md` §1.

5. **Fix the structure: front, body, back.** A plain introductory clause (*This agreement is
   dated … and is between …*), background in narrative sentences, the lead-in *The parties
   therefore agree as follows*, articles and sections with enumerated clauses tabulated so each
   element's scope is visible, and a concluding clause that says what is happening (*The parties
   are signing this agreement on the date stated in the introductory clause*). No *WHEREAS*, no
   recital of consideration, no *IN WITNESS WHEREOF*. `references/defined-terms-and-structure.md` §2–§4.

6. **Work the usages that carry most of the ambiguity.** Efforts standards (one standard,
   *reasonable efforts*, defined); *including* without the tail; provisos restated as what they are;
   *notwithstanding* replaced by a located exception; numbers stated once; periods and deadlines
   with their direction, trigger and endpoints; *and/or*, *such*, *said*, *herein* retired.
   `references/usages-and-ambiguity.md` §1.

7. **Run the ambiguity audit on anything that allocates money or risk.** Modifier scope, *and*/*or*
   with negation, closing modifiers, singular/plural subjects, antecedents for *it* and *such*, and
   the difference between vague and ambiguous. `references/usages-and-ambiguity.md` §2.

8. **Respect the two rails, and say so in the note.** In a *risk-allocation* provision — indemnity,
   defence, hold harmless, limitation of liability, warranty disclaimer, insurance, release,
   liquidated damages — the words can *be* the allocation and courts construe them strictly, so
   diagnose, draft the clearer version **alongside**, price each proposed cut, and route it to a
   lawyer in the governing jurisdiction. Where a rule prescribes wording verbatim or conspicuously,
   keep it. The linter tags both rails; the reasoning is
   `writing-skills:adams-smart-brevity`'s reference §3b, which this skill adopts rather than
   restates.

9. **Deliver in Smart Brevity.** A redline (tracked changes, or a three-column table: original,
   MSCD version, why) and a cover note that leads with what changed and why it matters, lists what
   needs the reader's decision, and says what was left alone and why. `--review` emits the
   skeleton; `references/redline-cover-note.md` has the template and a worked example. For a
   client, add one plain paragraph — `writing-skills:adams-plain-grade` owns that register.

10. **Verify, then stop.** Re-run the linter on the revised text: the `shall` ratio should have
    moved toward obligation-only and the edit count toward zero, and every remaining `flag` should
    have a named owner in the note. Then stop; a clean draft does not need a second pass of polish.

## Why / learn

MSCD's premise is that contract prose is not expository writing: it does not persuade, narrate or
explain, it *regulates conduct and states facts*, and the English for that is small and can be
systematised. Most contract ambiguity comes from category leakage — one `shall` doing every job in
the table — and most archaism survives because nobody asked what a sentence was for. Once each
sentence has a category, the verb form follows mechanically, the archaisms have nowhere to hide,
and a reader (or a court) is never asked to guess whether *shall survive* imposed a duty on
somebody. That is also why the linter can be deterministic: the hard part is classification, and
the classification has a test.

**The "tested language" myth, and where it stops.** Litigation over a formula is evidence that the
formula left room to fight, not a warranty that it works; the modern precise version is the safer
one. That axiom holds for everything whose only job is to convey meaning — which is nearly
everything — and it stops at the two rails in step 8, where the caselaw is the specification rather
than a failure log. Several of MSCD's positions are also genuinely contested among transactional
lawyers (*represents and warrants* → *states*; whether *hold harmless* adds anything; whether
*best efforts* outranks *reasonable efforts*). This skill follows MSCD in fresh drafting and
**says when a position is Adams's rather than settled**, because a drafter who takes a contested
rule to a partner as if it were settled loses trust in the whole method.

**Why Smart Brevity for the deliverable.** The redline is read by someone with less time than you
had. If the first two lines do not say what changed and why it matters, the review is reopened
from scratch, and the most important flag — the one that needs a decision — is found last or not at
all. The cover note is not a summary of the redline; it is the redline's decision list.

**Copyright posture.** This skill teaches MSCD's approach in its own words and names the book as the
authority. It does not reproduce the manual's tables or text. The manual itself is the reference
for chapter-level detail and for anything this skill marks [canon attribution]; own a copy.

## Common mistakes
- Replacing every `shall` with `must` or `will` → that changes the verb, not the thinking; classify
  first, then the form follows (and a house style that uses `must` for obligations is fine if it is
  consistent).
- "Fixing" `indemnify, defend, and hold harmless` as a triplet → *defend* is a distinct and often
  broader duty; propose alongside, never excise (rail, step 8).
- Modernising conspicuous all-capitals disclaimers → if a rule requires conspicuousness, the format
  may be load-bearing; flag, do not reformat on your own authority.
- Treating the linter's `edit` as applied → it is a proposal; the drafter applies it, and in an
  instrument in force every contested edit is a flag.
- Defining a term and using it once, or using a capitalised word that was never defined → both
  invite a court to ask what the capital meant.
- `within 30 days of` → direction and trigger unstated; *no later than 30 days after [event]*.
- Words and digits together ("thirty (30)") → say it once; a mismatch is a live dispute.
- A proviso doing the work of a condition, an exception and a new rule at once → restate as the one
  it is.
- Presenting a contested MSCD position as settled → say which it is; the reference maps the live
  arguments.
- Cover note that summarises the redline instead of listing the decisions → lead with what changed
  and what needs a call.

## Tailor to your environment
Record in `references/your-environment.md`: the house verb of obligation; defined-term formatting
(bold, quotation marks, both); the numbering scheme; recurring prescribed-wording clauses (statutory
notices, conspicuous disclaimers) that the linter should always flag rather than edit; a
`--known-terms` list of terms defined in master agreements so a schedule is not reported for using
them; and the templates that are in force (edits there are flags). Keep anything identifying a client
or a deal in the `.private.md` twin.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/mscd-contract-drafting.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- `references/categories-of-contract-language.md` — the full taxonomy, the has-a-duty-to test, shall/must/will/may decisions, passive voice, performance language, and a worked clause rewrite
- `references/defined-terms-and-structure.md` — defined terms, front/body/back of the contract, numbering and tabulation, cross-references, layout
- `references/usages-and-ambiguity.md` — efforts, including, provisos, notwithstanding, numbers, time, the archaism and doublet lists, and the ambiguity taxonomy with before/after pairs
- `references/redline-cover-note.md` — the Smart Brevity cover note and redline table, with a worked example and the "say when it is Adams's position" rule
- `references/your-environment.md` — house style, prescribed clauses, known terms, templates in force (fill in; the `.private.md` twin is git-ignored)

## Scripts
> Paths use `${CLAUDE_PLUGIN_ROOT}` so they resolve from **any** working directory once the plugin
> is installed. A bare `scripts/…` path only works inside a clone of the marketplace repo.
- `python3 "${CLAUDE_PLUGIN_ROOT}/skills/mscd-contract-drafting/scripts/mscd_lint.py" <file.docx|.txt|.md> [--json] [--review] [--house-style shall|must] [--max-words N] [--known-terms FILE]` —
  deterministic MSCD lint. Reads `.docx` directly (accepted-changes view) or plain text. Reports a
  header (paragraphs, sections, defined terms, and every `shall` sorted into obligation / policy /
  discretion / passive), then findings keyed to the section they sit in, each with the matched text,
  a suggested edit and the reason. Rules cover the `shall` family, `may not`, `and/or`, doublets,
  archaisms, lawyerisms, *including*, efforts, provisos, *notwithstanding*, words-and-digits
  numbers (and mismatches), boilerplate, defined-term hygiene, dangling and vague cross-references,
  time and deadline wording, gendered pairs, sentence length, all-capitals runs and unfilled
  placeholders. Two rails downgrade an edit to a flag: risk-allocation paragraphs and prescribed
  wording. `--review` prints the Smart Brevity cover-note skeleton; `--json` the full report.
  Exit 0 no findings, 1 findings, 2 unreadable input. `--self-test` runs the fixture suite,
  including the false-positive controls (*hereby grants* is not an archaism; *reasonable efforts*
  is not flagged; a proper noun is not an undefined term; a short numbered sentence is not a
  heading) and the docx round trip. It is a pattern matcher: it does not know the governing law
  and cannot judge substance.
