# The redline cover note — Smart Brevity for legal deliverables

A redline is read by someone with less time than the drafter had. Smart Brevity (VandeHei, Allen &
Schwartz, *Smart Brevity*, 2022) is a discipline for that reader: one strong first sentence that
says what is new, one sentence on why it matters, a scannable body of only what the reader needs,
and a stop. Applied to a contract review, the cover note is not a summary of the redline; it is the
redline's **decision list**. [canon attribution for the Smart Brevity method; the application to
legal deliverables is this skill's.]

Contents: §1 The four moves · §2 The cover note template · §3 The redline table ·
§4 Worked example · §5 Rules that travel with the note · §6 The client paragraph

## §1 The four moves

| Move | In a news item | In a redline note |
|---|---|---|
| **The one thing** | the headline sentence | *What changed* — one sentence: scope of the edits and the one decision that matters most |
| **Why it matters** | one sentence of consequence | the exposure the edits remove, or the decision the reader must make and what turns on it |
| **Go deeper** | bullets, bold lead-ins, white space | the decision list, the verify list, what was not changed and why |
| **Stop** | no padding | no restatement of the redline; the table carries the detail |

## §2 The cover note template

```
**Redline cover note -- [document], [date]**

**What changed:** [N] wording edits across [K] sections, no change of substance except where
flagged below. [One sentence on the biggest single fix.]

**Why it matters:** [The exposure the edits remove, in one sentence -- e.g. "Twelve of the
seventeen 'shall's state rules rather than duties, and three obligations named nobody to perform
them."]

**Needs your call ([n]):**
- § [x.y] [rule] -- [the contested or rail item, the two options, and what turns on it]
- § [x.y] ...

**Verify:** [dangling cross-references, undefined terms, placeholders, numbers that disagree]

**Not changed, and why:** [prescribed wording kept; risk-allocation language proposed alongside
in the table, not applied; anything deliberately left]

**Next step:** [who decides what, by when; whether the counterparty sees the clean or the marked
version]
```

Every line is a sentence with a verb. Bold lead-ins, no headers below the title, nothing that the
redline table already says.

## §3 The redline table

Where tracked changes are not wanted, deliver a three-column table so the reader can accept or
reject line by line:

| § | Original | MSCD version | Why (rule) | Status |
|---|---|---|---|---|
| 2.3 | *Acme shall be entitled to reject …* | *Acme may reject …* | discretion, not duty (`SHALL-DISC`) | edit |
| 5 | *indemnify, defend, and hold harmless* | *indemnify and defend* | *hold harmless* contested; *defend* kept (`DOUBLET`, rail) | **flag — your call** |
| 7.1 | *shall be governed by* | *is governed by* | policy (`SHALL-POLICY`) | edit |

*Status* is the reader's column: *edit* means apply as written; *flag* means decide; *kept* means
deliberately unchanged. The linter's `--json` output has every field needed to generate this table.

## §4 Worked example

Original clause (from a services agreement under negotiation, New York law):

> *Supplier covenants and agrees that it shall use its best efforts to deliver the Goods within
> thirty (30) days of the Order Date; provided, however, that Customer shall be entitled to cancel
> any Order in the event that delivery has not occurred by such date, and any such cancellation
> shall be deemed effective upon notice.*

Cover note:

> **What changed:** one sentence became three, each doing one job; the deadline now states its
> direction and trigger (*no later than 30 days after the Order Date*); the proviso is a plain
> *if*. No change of substance.
>
> **Why it matters:** as drafted, nobody could say whether *within thirty days of* ran forward or
> backward, or whether the proviso was a condition on Supplier's duty or a separate right.
>
> **Needs your call (1):**
> - § 4.1 `EFFORTS` — *best efforts* → *reasonable efforts*, defined. Adams's position is that the
>   gradations are not reliable; some courts read *best* as more demanding. Because this instrument
>   is under negotiation, the change is proposed, not applied.
>
> **Verify:** *Order Date* is used here and in § 3.2 and is not defined.
>
> **Not changed:** the cancellation right and its trigger.
>
> **Next step:** your decision on the efforts standard by Thursday; then the clean version goes to
> the counterparty.

## §5 Rules that travel with the note

- **Say when a position is Adams's rather than settled.** *represents and warrants*, *hold
  harmless*, the efforts hierarchy, and *shall*-versus-*must* are live arguments; the note names
  them as such and proposes rather than applies them in a live instrument. The map of the
  disagreements is `writing-skills:adams-smart-brevity` reference §3b.
- **Risk-allocation and prescribed wording stay in the table, not in the applied edits.** The note
  says they were proposed alongside and why (courts construe them strictly; a rule may require the
  words). Reformatting for readability — structure, white space, bold on a liability cap — is safe
  and is applied; excision is not.
- **An instrument in force gets flags, not edits.** The note says so in the first line.
- **Nothing in the note that is not in the redline, and nothing in the redline that the note
  does not account for.** A reader should be able to reconcile the two in one pass.
- **The note's own language follows the rules.** Active verbs, no archaisms, one idea per sentence.

## §6 The client paragraph

When the reader is a client rather than a lawyer, add one paragraph in the most accessible register
that keeps the meaning exact — what the clause now says, what the client must do, what they may do,
and by when. `writing-skills:adams-plain-grade` owns that register; the cover note above stays for
the lawyer.
