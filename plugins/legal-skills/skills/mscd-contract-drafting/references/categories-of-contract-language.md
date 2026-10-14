# Categories of contract language — the taxonomy, the test, and the verb forms

The single most useful idea in *A Manual of Style for Contract Drafting* (Kenneth A. Adams, 5th ed.,
ABA 2023) is that every sentence in the body of a contract is doing one of a small number of jobs,
and each job has a verb form. Decide the job, and the form follows; leave the job undecided, and a
court decides it for you. This file states the system in the skill's own words and marks it
[canon attribution]: it is Adams's framework, paraphrased, not quoted — read the manual for the
chapter-level treatment and the edge cases.

Contents: §1 Why categories · §2 The taxonomy · §3 Conditions · §4 Active and passive ·
§5 The `shall` decisions and the replacement table · §6 Worked rewrite · §7 Where the bar disagrees

## §1 Why categories

A contract does three things: it imposes duties, it grants rights, and it states rules and facts.
Ordinary prose uses the same verbs for all three, which is why the all-purpose `shall` spreads
through a form until it marks nothing. Category leakage is the source of most drafting ambiguity
that is not a modifier-scope problem: *the Term shall survive* (no one has a duty), *Acme shall be
entitled to* (a right wearing a duty's clothes), *the parties agree that Acme shall* (a duty
wrapped in a restatement of the agreement). One category per sentence, and the verb form is the
label.

## §2 The taxonomy

| Category | Job | Form | Example | The test |
|---|---|---|---|---|
| **Agreement** | records that the parties agree | *agree*, once, in the lead-in | *The parties therefore agree as follows.* | Anywhere else, *agrees to* is throat-clearing: delete it and state the duty |
| **Performance** | an act that happens by the signing itself | *hereby* + present-tense verb | *Acme hereby grants Zenith a licence …* | Could the act be done by signing? If the act happens later, it is a duty, not performance |
| **Obligation on the subject** | a duty on the party that is the sentence's subject | *shall* (house alternative: *must*) | *Zenith shall deliver the report by …* | Replace *shall* with *has a duty to*: the sentence must still make sense |
| **Obligation on another / requirement** | a duty whose subject is a thing, or a requirement that functions as a condition | *must* | *Any notice must be in writing.* *The Work must conform to the Specifications.* | Who actually does it is stated elsewhere, or the sentence is really a condition (§3) |
| **Discretion** | grants a choice | *may*; *is entitled to* when the point is a right against someone | *Acme may terminate …* | Would *has the option to* fit? Then *may*, never *shall be entitled to* |
| **Prohibition** | forbids | *shall not* (house: *must not*); *Neither party shall* | *Zenith shall not assign …* | *may not* is ambiguous — prohibition, absence of a right, or possibility (*might not*): avoid it |
| **Policy** | a rule of the contract with no actor | present tense; *will* for a future event | *This agreement terminates on …*; *"Fee" means …*; *Interest accrues at …* | The subject cannot have a duty, so *shall* is wrong |
| **Declaration** | a fact a party asserts or accepts | *states that*; *acknowledges that* | *Acme states that it is duly organised …*; *Zenith acknowledges that the Fee is not refundable.* | Is it a fact at signing? Then it is not a duty, however it is worded |
| **Belief** | what a party believes | *believes that* | rare; mostly in recitals | — |
| **Intention** | what the parties intend | *intend(s) that* | *The parties intend that Zenith is an independent contractor.* | Courts may give intention language little weight; use for interpretive signals only |
| **Recommendation** | advice to the reader | *recommends*; *should* | consumer and licence terms | Never *should* for a duty |

Notes on the forms [canon attribution]:

- **`shall` is reserved for a duty on the subject.** That single restriction clears most of the noise: *shall* with a non-party subject is policy; *shall be entitled to* is discretion; *shall not be required to* is the absence of a duty (*is not required to*); *shall mean* in a definition is policy (*means*). MSCD's test — *has a duty to* — is also the one a reviewer can apply without re-reading the whole clause.
- **`must` does two things in MSCD's scheme:** it carries an obligation whose subject is not the party owing it (*The goods must be delivered in bulk* — someone has to do it, stated elsewhere), and it expresses a requirement that works as a condition (*To be effective, a notice must be in writing*). A house style that uses *must* for every obligation is defensible and common in plain-language drafting; the rule that matters is consistency within one instrument.
- **`will` is for policy about the future** (*If Zenith breaches, this agreement will terminate*). It is not an obligation verb. Mixing *will* and *shall* for duties in one document invites the argument that they mean different things.
- **`may` is a grant of discretion, not a prediction.** *may be terminated* is passive discretion with no actor — say who may terminate. When the clause really creates a right against the other party rather than a mere option, *is entitled to* says that.
- **`hereby` belongs only in performance language.** *Acme hereby grants* performs the grant by signing. *The parties hereby agree* and *is hereby acknowledged* are decoration.
- **Declarations: `states that`.** MSCD's position is that a representation is a statement of fact and *states* says so, with the remedy a matter of law rather than of the verb. The bar's common practice — *represents and warrants* — rests on the belief that the two verbs preserve two remedies (misrepresentation and breach of warranty). That is a live argument, not a settled point: follow MSCD in fresh drafting, and flag rather than change in an instrument under negotiation or in force. *Acknowledges* is for a fact the party accepts as true, usually one the other side asserts.

## §3 Conditions

A condition is something that must happen before a right or duty arises. The failure mode is a
clause that reads as an obligation when a condition was meant (so a court awards damages for its
breach) or as a condition when an obligation was meant (so a party loses a right for a trivial
lapse). MSCD's guidance [canon attribution]: make the conditional structure visible —

- *if* / *unless* / *only if* for the trigger: *Zenith may invoice only if Acme has accepted the Deliverable.*
- *must* for a requirement that is a condition: *To be effective, a notice must be delivered by courier.*
- *subject to Section X* to subordinate one provision to another, sparingly, and with the exception
  stated where it bites rather than by a *notwithstanding* override.
- *It is a condition to Acme's obligation to pay that …* where the stakes justify spelling it out.
- Never *provided that*: a proviso can be read as a condition, an exception, or a new rule, and the
  word does not say which.

## §4 Active and passive

An obligation in the passive — *The report shall be delivered within 30 days* — states a duty and
names nobody to perform it. If no party is named anywhere, it reads as policy and binds no one; if
a *by Zenith* follows, the sentence has simply buried the actor. The fix is mechanical: make the
party the subject (*Zenith shall deliver the report …*). Passive policy is fine (*This agreement is
governed by …*); passive duties are not.

## §5 The `shall` decisions and the replacement table

| You see | It is | Write |
|---|---|---|
| *X shall be entitled to* / *shall have the right to* / *shall be permitted to* | discretion | *X may* (or *X is entitled to* for a right against someone) |
| *X shall not be required to* / *shall have no obligation to* | absence of a duty | *X is not required to* |
| *X shall be obligated to* / *shall be required to* | duty with a redundant wrapper | *X shall* |
| *X shall be responsible for paying* | duty | *X shall pay* (or *X is liable for*, if the point is who bears a cost) |
| *X agrees to* / *covenants and agrees to* / *undertakes to* | duty wrapped in the fact of agreement | *X shall* |
| *The Term shall survive* / *This agreement shall be governed by* / *"Fee" shall mean* | policy | present tense: *survives*, *is governed by*, *means* |
| *X shall be deemed to* | policy creating a legal fiction | *X is deemed to* — and ask whether a fiction is needed at all |
| *X may not* | ambiguous | *X shall not* (prohibition) or *X is not entitled to* (no right) |
| *X will deliver* (alongside *shall* elsewhere) | inconsistent obligation verb | pick one verb for duties and hold it |
| *X represents and warrants that* | declaration | *X states that* in fresh drafting; flag in a live instrument (§7) |
| *The report shall be delivered by X* | passive duty | *X shall deliver the report* |
| *X shall use its best efforts to* | contested standard | *X shall use reasonable efforts to*, with *reasonable efforts* defined — a flag, not an edit (§7) |

## §6 Worked rewrite

Original (one sentence doing four jobs):

> *Supplier covenants and agrees that it shall use its best efforts to deliver the Goods within
> thirty (30) days of the Order Date; provided, however, that Customer shall be entitled to cancel
> any Order in the event that delivery has not occurred by such date, and any such cancellation
> shall be deemed effective upon notice.*

Category tagging:

1. *Supplier covenants and agrees that it shall use its best efforts to deliver the Goods …* —
   **obligation** on the subject, wrapped in agreement language, with a contested efforts standard.
2. *… within thirty (30) days of the Order Date* — a **period** with its direction unstated and the
   number said twice.
3. *provided, however, that Customer shall be entitled to cancel …* — a proviso that is really
   **discretion** conditioned on a trigger.
4. *… in the event that delivery has not occurred by such date* — the **condition**.
5. *any such cancellation shall be deemed effective upon notice* — **policy**.

MSCD version:

> *Supplier shall use reasonable efforts to deliver the Goods no later than 30 days after the Order
> Date. If Supplier has not delivered the Goods by that date, Customer may cancel the Order by
> notice to Supplier. A cancellation is effective when Supplier receives the notice.*

Cover-note lines for this clause: **what changed** — four sentences, each in one category; the
deadline now states its direction and trigger; the proviso is a plain *if*. **Needs your call** —
*best efforts* → *reasonable efforts* changes a standard the bar reads two ways (§7); kept as a
flag. **Not changed** — nothing of substance; the cancellation right and its trigger are the same.

## §7 Where the bar disagrees

The positions below are MSCD's and are contested among practising transactional lawyers. The house
default is to follow MSCD in fresh drafting and to flag, not change, in an instrument under
negotiation or in force. The fuller map, with the standard counter-case for each, is
`writing-skills:adams-smart-brevity` reference §3b, which this skill adopts rather than restates.

- *represents and warrants* → *states*: the two-remedies belief versus Adams's view that remedies do
  not turn on the verb.
- *best efforts* / *commercially reasonable efforts* → one standard, *reasonable efforts*, defined:
  courts have both distinguished the gradations and refused to.
- *shall* reserved for duties versus *must* everywhere: either is defensible; consistency is the rule.
- *hold harmless* adds nothing to *indemnify*: some courts read it as broader; and *defend* is a
  distinct, often broader duty — never cut it as a triplet.
- *may* versus *is entitled to*: a stylistic preference until a clause turns on whether a right
  exists against the other party.

[canon attribution throughout — these are the standard positions, stated for orientation and not
independently re-verified; all of it is jurisdiction-dependent, and a live instrument goes to a
lawyer in the governing jurisdiction.]
