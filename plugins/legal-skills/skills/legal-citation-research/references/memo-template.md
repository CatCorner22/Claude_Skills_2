# The Smart Brevity research memo (and its brief and client-update variants)

Contents: §1 The template · §2 Worked example · §3 Variants · §4 What stays out

## §1 The template

```
**Memo -- [question in six words] -- [date], [jurisdiction]**

**Bottom line:** [The answer in one sentence.] Confidence: [high / moderate / low], because
[the one reason -- binding authority on point / persuasive only / unsettled / fact-dependent].

**Why it matters:** [The consequence for the client or the matter, in one sentence.]

**The rule:**
- [Element or rule 1] -- [Authority, pinpoint] (binding / persuasive)
- [Element or rule 2] -- [Authority, pinpoint]
- Contrary authority: [case, or "none found: searched X, Y on DATE"]

**Applied here:** [Two to four sentences mapping the facts to the elements. Name the fact that
decides it.]

**Open questions / not checked:**
- [A fact you do not have and what it would change]
- [An authority not yet read, a citator not run, a jurisdiction not covered]

**Next step:** [Who does what, by when.]

---
Verification ledger
| Authority | Existence (how, date) | Support (pinpoint read?) | Currency (how, date) | Status |
| ... | ... | ... | ... | ... |
```

Rules of the form: bottom line before anything; confidence stated and reasoned; every authority
pinpointed and labelled binding or persuasive; the unknowns named; no authority in the body that
is missing from the ledger.

## §2 Worked example

> **Memo — sanctions for unverified citations — 2026-10-14, S.D.N.Y.**
>
> **Bottom line:** A filing that cites decisions counsel did not verify exposes counsel to Rule 11
> sanctions, and the court need not find that counsel knew the citations were false at filing;
> continued reliance after they are questioned is what established bad faith in the leading case.
> Confidence: high on the duty; moderate on the measure of sanction, which is discretionary.
>
> **Why it matters:** the firm's draft opposition contains three citations the verifier reports
> NOT FOUND, and it is due Friday.
>
> **The rule:**
> - Counsel who signs a filing certifies a reasonable inquiry into the legal contentions —
>   Fed. R. Civ. P. 11(b)(2) (binding).
> - Citing non-existent decisions and maintaining them after inquiry supports sanctions under
>   Rule 11 and the court's inherent power — *Mata v. Avianca, Inc.*, 678 F. Supp. 3d 443
>   (S.D.N.Y. 2023) (binding in this district as persuasive district authority; pinpoint to be
>   added on reading).
> - Contrary authority: none found (searched CourtListener and Google Scholar, "Rule 11"
>   "fabricated citation", 2026-10-14).
>
> **Applied here:** the three NOT FOUND citations must be removed or replaced before filing; if
> they came from a generative tool, the court's standing order on disclosure applies (check
> `your-environment.md`); the remaining citations are VERIFIED but not yet read against their
> propositions.
>
> **Open questions / not checked:** whether this judge has a standing order on tool-generated
> citations; the pinpoint in *Mata* for the bad-faith finding (the opinion is open, not yet read
> through).
>
> **Next step:** replace or remove the three citations today; read *Mata* and pinpoint; check the
> judge's rules page; re-run the verifier on the final draft.
>
> ---
> | Authority | Existence | Support | Currency | Status |
> | Fed. R. Civ. P. 11(b)(2) | uscourts.gov rules, 2026-10-14 | text read | current rules page | OK |
> | *Mata v. Avianca*, 678 F. Supp. 3d 443 | CourtListener API VERIFIED, 2026-10-14 | not yet | cited-by scan pending | PENDING |

The example is honest about its own gaps: the ledger shows one authority still PENDING, and the
memo says so in the body rather than implying a finished check.

## §3 Variants

- **Brief or motion**: the same order inside the court's required structure — the argument heading
  is the bottom line, the first sentence under it is why it matters, authorities follow with
  pinpoints. The ledger stays in the file, not the filing.
- **Client update**: bottom line, why it matters, what the client should do, what happens next;
  authorities by name only, the ledger kept internally. For a non-lawyer reader, write the
  bottom line in the most accessible register that keeps the meaning exact
  (`writing-skills:adams-plain-grade` owns that register).
- **Internal quick answer**: the first three lines of the template and the ledger; nothing else.

## §4 What stays out

The search narrative ("I first looked at…"), the authorities considered and rejected (they go in
the ledger with a one-word reason), block quotations longer than the proposition needs, and any
citation that is not in the ledger with every cell filled.
