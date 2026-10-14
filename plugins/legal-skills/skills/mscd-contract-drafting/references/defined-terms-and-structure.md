# Defined terms and the structure of a contract

How MSCD organises a contract — the words that get capitals, the front and back matter that frame
the body, the numbering that makes a clause citable, and the layout that makes it readable. Each
section ends with what the linter checks and what it cannot. [canon attribution throughout: the
positions are Adams's, paraphrased; the manual carries the detail.]

Contents: §1 Defined terms · §2 The front of the contract · §3 The body · §4 The back ·
§5 Layout and typography · §6 Checklist

## §1 Defined terms

A defined term is a label that saves words or removes doubt. It earns its capital letter only when
it does one of those two things.

**When to define.** Define a term when it is used more than once and the definition is shorter or
more precise than repeating the words, or when ordinary meaning is too loose for the deal
(*Business Day*, *Confidential Information*). Do not define a term used once; do not define a
term to give it its ordinary meaning; do not define a party name that is already short.

**Two places to define.** *Autonomous* definitions sit in a definitions section, usually Section 1
or the last article, in alphabetical order, in the form *"Business Day" means …*. *Integrated*
definitions sit in the body where the concept first appears: *… a fee of $30,000 a month (the
"Fee")*. A few terms → integrate; many → a definitions section. With a definitions section it is
acceptable for a term to be used before the section that defines it; an integrated definition
should precede its first use.

**Form.** The term in quotation marks and bold when it is defined (both: the quotation marks mark
the definition, the bold makes it findable); thereafter in plain text with its capital letters.
*means* for an exhaustive definition, *includes* for a non-exhaustive one, *means … and includes
…* when both are needed; never *shall mean*, *refers to* or *shall be deemed to mean*. Define the
singular and let the plural follow; do not write *"Product" or "Products" means*.

**What a definition may not do.** A definition states what a word means. It must not impose a duty
(*"Delivery Date" means the date, which shall be no later than …*), grant a right, or state a
condition. If a sentence does that work inside a definition, move the sentence to the body and
leave the label.

**Consistency.** One label per concept, the same words every time, and no capitalised word that is
not a defined term. A capital that is not a definition is a question: *the Services* when
*Services* was never defined makes a reader hunt, and gives a court a term to construe.

**Party names.** Short, neutral, and not role words that will be confused (*Lessor*/*Lessee* is the
classic trap). *Acme* and *Zenith* beat *Party A* and *Party B*.

Linter: `DEF-UNUSED`, `DEF-UNDEFINED`, `DEF-SHALLMEAN`, `DEF-HEREINAFTER`. It cannot tell whether a
definition is worth having, or whether two labels name one concept.

## §2 The front of the contract

**Title.** A plain noun phrase: *Asset Purchase Agreement*, *Master Services Agreement*. No *THIS*,
no all capitals as a matter of style.

**Introductory clause.** One sentence that identifies the document, dates it, and names the
parties with their entity type and jurisdiction and their short names:

> *This master services agreement is dated October 1, 2026, and is between Acme Industries, Inc.,
> a Delaware corporation ("Acme"), and Zenith Consulting LLC, a New York limited liability company
> ("Zenith").*

*Between* for any number of parties. Not *made and entered into*, not *by and between*, no
*WITNESSETH*. Use *dated as of* only when the parties are deliberately giving the contract a date
other than the signing date, and say so in the concluding clause.

**Background (recitals).** Plain narrative sentences under a heading such as *Background* or
*Recitals*: who the parties are, what they want, what happened before. Nothing operative goes
here — no duties, no definitions that the body depends on — and no *WHEREAS*. The recital of
consideration (*for good and valuable consideration, the receipt and sufficiency of which are
hereby acknowledged*) does nothing: consideration is a fact about the exchange, and reciting it
does not create it.

**Lead-in.** *The parties therefore agree as follows.* That sentence is the one place for language
of agreement; everywhere else, *agrees to* is throat-clearing.

Linter: `BOILERPLATE`, `DOUBLET` (*made and entered into*, *by and between*).

## §3 The body

**Articles and sections.** MSCD's scheme: articles numbered 1, 2, 3 with headings; sections
numbered 1.1, 1.2 with headings; subsections (a), (b); enumerated clauses (i), (ii); a further level
(A), (B) only when unavoidable. Automatic numbering in the word processor, so cross-references
update, and a heading that is a noun phrase, never a sentence that does work (*Payment*, not *Acme
shall pay*). A short *headings do not affect interpretation* provision is harmless; relying on it
to excuse a misleading heading is not.

**Tabulation (enumerated clauses).** Where a sentence lists elements, set them out one per line
with a stem, so the scope of every modifier is visible:

> *Zenith shall deliver to Acme, no later than the fifth Business Day of each month,*
> *(a) a progress report for the previous month;*
> *(b) an invoice for the Fee; and*
> *(c) any Deliverable completed in that month.*

The stem must read grammatically into every element; *and* or *or* goes at the end of the
penultimate element only; each element ends with a semicolon; the last with a period. A trailing
phrase that is meant to modify all the elements goes back in the stem or into its own sentence —
tabulation exists to settle the question *does this modify the last item or all of them?*

**Cross-references.** *Section 4.2*, *Article 7*, *Schedule 1* — never *above*, *below*, *the
foregoing*, *hereof*, or *as set forth herein*. A cross-reference to a section that does not exist
is a drafting error a court cannot repair; the linter checks every *Section n.n* against the
headings it found.

**Attachments.** Call them one thing (*Schedule* for lists and data, *Exhibit* for documents, or
one name for both) and keep the naming consistent; one sentence incorporating them (*The schedules
and exhibits are part of this agreement*) does the work that *attached hereto and incorporated
herein by reference* repeats in every clause.

**Internal rules of interpretation.** One short section if needed: that headings are for
convenience, that the singular includes the plural. An *including* provision is a weak cure for a
restrictive reading (usages §1); restructure the clause instead. Keep it short; a long
interpretation section creates arguments faster than it settles them.

Linter: `XREF-DANGLING`, `XREF-VAGUE`, `SENTENCE` (tabulation hints), `INCLUDING`.

## §4 The back

**Concluding clause.** State what is happening: *The parties are signing this agreement on the
date stated in the introductory clause.* If the signing date differs from the contract date: *…
are signing this agreement on the dates stated under their signatures, with effect from the date
stated in the introductory clause.* Not *IN WITNESS WHEREOF*, not *have executed this Agreement
as of the date first written above*.

**Signature blocks.** Entity name on one line; *By:* with the signature; the signatory's name and
title printed beneath. A counterparts provision in the body is fine; a *signatures delivered
electronically are originals* sentence belongs there too.

Linter: `BOILERPLATE`, `XREF-VAGUE` (*the date first written above*).

## §5 Layout and typography

- No all-capitals for emphasis. Capitals are hard to read; where a rule requires conspicuous text
  (warranty disclaimers under UCC § 2-316; the definition of *conspicuous* in § 1-201(b)(10)
  [canon attribution]), keep it conspicuous — bold or contrasting type can satisfy that and reads
  better — but do not change an existing block on this skill's authority (rail).
- Bold for a defined term where it is defined; nothing else bold except headings.
- Hanging indents for enumerated clauses so the stem and the elements are visually distinct.
- One typeface, left-aligned, numbered pages, and a table of contents for anything over about ten
  pages.
- Dates in one format throughout (*October 1, 2026*); amounts with the currency symbol and digits.

Linter: `CAPS` (flag only), `NUMBERS`.

## §6 Checklist

- [ ] Every capitalised term is defined exactly once, used more than once, and defined with *means*
      or *includes*.
- [ ] No duty, right or condition lives inside a definition.
- [ ] Introductory clause: dated, *between*, entity types, short names; no *made and entered into*.
- [ ] Background in plain sentences; no *WHEREAS*; no recital of consideration.
- [ ] Lead-in present; *agrees to* appears nowhere else.
- [ ] Articles and sections numbered automatically; headings are noun phrases.
- [ ] Every list of three or more elements is tabulated with a grammatical stem.
- [ ] Every *Section n.n* resolves; no *above*, *below*, *foregoing*, *hereof*.
- [ ] Concluding clause states the signing; signature blocks complete.
- [ ] No all-capitals except where a rule requires conspicuousness (flagged, not changed).
