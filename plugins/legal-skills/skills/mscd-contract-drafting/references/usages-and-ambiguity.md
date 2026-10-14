# Usages and ambiguity — the words that carry the disputes

The first half is a table of the usages MSCD singles out, each with its position, the form to
write, whether the position is contested, and the linter rule that catches it. The second half is
an ambiguity taxonomy with a before-and-after pair for each kind, so a reviewer can name what is
wrong with a clause rather than sense it. [canon attribution: the positions are Adams's,
paraphrased. Items marked *contested* are live arguments among drafters; items marked
*snippet-only* were confirmed only from published excerpts of the manual.]

Contents: §1 Usages · §2 Archaisms and doublets · §3 Ambiguity taxonomy · §4 The audit procedure

## §1 Usages

| Usage | MSCD position | Write | Contested? | Linter |
|---|---|---|---|---|
| *best efforts*, *commercially reasonable efforts*, *reasonable best efforts*, *good-faith efforts* | one standard — *reasonable efforts* — and define it; the gradations do not reliably mean different things, and courts have gone both ways on whether *best* is more demanding | *shall use reasonable efforts to …*, with a definition that states what the efforts standard requires and does not require (for example, that it does not require a party to act against its own commercial interests) | **yes** — a flag | `EFFORTS` |
| *including, but not limited to* / *including without limitation* | the tail is redundant, and it is also not a cure: courts have read *including* restrictively with and without it, and an interpretation provision is no more reliable. Where a restrictive reading would hurt, restructure — state the general class so it stands on its own and give the examples separately — rather than lean on the tail [snippet-only] | *including* alone where examples are meant; restructure where the general words must carry the weight | no | `INCLUDING` |
| *provided that* / *provided, however, that* | do not use: a proviso can introduce a condition, an exception or a separate rule, and the word does not say which | restate as *if* / *only if*, *except that* / *but*, or a new sentence | no | `PROVISO` |
| *notwithstanding anything to the contrary* | a precedence puzzle; two provisions each claim to win | state the exception where it applies (*except as provided in Section 4.2*) or subordinate with *subject to Section 4.2* | no | `NOTWITHSTANDING` |
| *subject to* | acceptable to subordinate one provision to another; overused as a blanket | *subject to Section X* with a specific section | no | — |
| *material* / *materially* / *material adverse change* | vague by design; acceptable when the parties want a vague standard, dangerous when they think they have a precise one | define *Material Adverse Change* if it matters; for everything else, say what the threshold is | no | — |
| *deemed* | for a legal fiction only (*is deemed received on the third Business Day after posting*); not for an ordinary rule | *is deemed*, never *shall be deemed* | no | `SHALL-POLICY` |
| *respectively* | acceptable where it pairs two lists; usually better restructured | pair the items explicitly | no | — |
| *and/or* | avoid; it has been read as *and*, as *or*, and as both | *A or B, or both*; *one or more of A, B and C* | no | `AND-OR` |
| *any* / *each* / *every* / *all* | *any* is ambiguous between one and all; *each* and *every* distribute; *all* collects | choose the one that matches the intended scope; in obligations, *each* | no | — |
| *such* (as a pointer), *said*, *the same*, *the foregoing* | lawyer dialect for *that*, *the*, *it*, *those* | *that*, *the*, *it*; *such … as* is a different, legitimate use | no | `ARCHAISM`, `XREF-VAGUE` |
| numbers | words for whole numbers one through ten, digits for 11 and above; digits always for amounts of money, percentages, times of day and numbers in lists; never words and digits together; consistency matters more than the convention [snippet-only] | *30 days*, *$30,000*, *10%*, *two parties* | no | `NUMBERS` |
| periods and deadlines | *within N days of X* leaves direction and trigger open; *by [date]* leaves the day itself open; *from X to Y* and *between X and Y* leave the endpoints open | *no later than 30 days after [event]*; *before [date]*; *from October 1 through October 31, inclusive* or *beginning on … and ending on …* | no | `TIME` |
| time of day | a time of day is a boundary between two periods, not a span, so *11:59 p.m.* and *12:01 a.m.* are illogical workarounds; the problem with *midnight* is that every date has two of them | *midnight at the end of October 31, 2026* (or *at the beginning of*), with the time zone [snippet-only] | no | `TIME` |
| *biweekly*, *bimonthly* | each means two things | *every two weeks*, *twice a month* | no | `TIME` |
| *between* / *among* | *between* for any number of parties | *between* | no | — |
| *per annum* | *per year* | *per year* | no | `ARCHAISM` |
| *from time to time* | legitimate to signal a recurring right; redundant with *at any time* | keep where it signals recurrence; cut *at any time and from time to time* to *at any time* | no | `LAWYERISM` |
| *to the extent* | fine when a matter of degree is meant; wrong as a synonym for *if* | *if* when the matter is binary | no | — |
| *as the case may be* | restructure so each case is stated | — | no | `LAWYERISM` |
| *in the event that*, *prior to*, *subsequent to*, *pursuant to*, *in accordance with*, *set forth in* | *if*, *before*, *after*, *under*, *under* / *as required by*, *stated in* | the short word | no | `LAWYERISM` |
| *for the avoidance of doubt* | if there is doubt, resolve it in the rule; the phrase announces an afterthought | delete, and fix the rule | no | `LAWYERISM` |
| *mutatis mutandis* | state the changes | — | no | `ARCHAISM` |
| *terminate* / *expire* | the distinction is neither necessary nor reliable: *This agreement terminates on [date]* is correct for the scheduled end, and *expiration* as a separate concept invites the argument that the two were meant to differ | *terminates* for both; where the ground matters, cite the section (*terminated under Section 9.2*); never *terminates and expires* [snippet-only] | no | — |
| gender | *he or she* / *his/her* are clutter that still miss cases | repeat the defined term; *it* for an entity; *they* if the house style allows | no | `GENDER` |
| *hereby* | performance language only | *Acme hereby grants*; nowhere else | no | `ARCHAISM` |
| *represents and warrants* | *states* | *Acme states that …* in fresh drafting; flag in a live instrument | **yes** | `REPS` |
| *successors and assigns*, *right, title and interest* | conveyancing formulas with some content; keep where the distinction is intended | keep or simplify deliberately | mild | `DOUBLET` (flag) |

## §2 Archaisms and doublets

**Archaisms to retire on sight** (no contested defence): *herein, hereof, hereto, hereunder,
hereinafter, thereof, therein, thereto, thereunder, therefor, whereof, wherein, whereby,
aforesaid, aforementioned, witnesseth, forthwith, whatsoever, said* (as an adjective), *such*
(as a pointer), *the parties hereto, in witness whereof, know all men by these presents, now
therefore, whereas*.

**Doublets and triplets** that say one thing twice: *null and void* (→ *void*), *any and all*,
*each and every*, *full and complete*, *due and payable* (→ *due*), *terms and conditions* (→
*terms*), *covenants and agrees* (→ *shall*), *sole and exclusive* (pick one; they differ), *final
and binding* (say which), *free and clear* (→ *free of*), *made and entered into*, *by and between*,
*cease and desist* (→ *stop*), *true and correct* (→ *accurate*), *in full force and effect* (→
*in effect*), *power and authority* (→ *authority*), *unless and until* (pick one), *if and when*
(pick one).

**Doublets that are not doublets** — rail territory: *indemnify, defend and hold harmless*. In
many jurisdictions *defend* is a distinct and often broader obligation (triggered by what is
alleged, arising at the outset, often worth more than the indemnity), and whether *hold harmless*
adds anything to *indemnify* is contested. Never cut these as redundancy; propose the clearer
version alongside and route it to a lawyer in the governing jurisdiction. The same caution applies
to any belt-and-suspenders phrasing inside a risk-allocation provision, where express-negligence
and conspicuousness rules can make the extra words the element that makes the clause work
[canon attribution; jurisdiction-dependent].

## §3 Ambiguity taxonomy

Ambiguity is a word or structure with two or more specific meanings. It is different from
**vagueness** (a single meaning with fuzzy edges — *reasonable*, *promptly*), which can be
deliberate, and from **uncertainty** (the parties did not address the case at all), which no
wording fixes. A reviewer who can name the kind can name the fix.

**Lexical** — one word, two meanings.
- *Before:* *Zenith shall report biweekly.*
- *After:* *Zenith shall report every two weeks.*

**Syntactic: modifier scope** — a modifier that could attach to one item or several.
- *Before:* *charitable institutions or societies* (is *charitable* attached to *societies*?)
- *After:* *charitable institutions and charitable societies*, or tabulate.

**Syntactic: closing modifier** — a trailing phrase after a list.
- *Before:* *employees and contractors of Acme* (contractors of Acme, or all employees too?)
- *After:* *Acme's employees and Acme's contractors* — or tabulate with the modifier in the stem.

**Syntactic: `and` / `or` with negation.**
- *Before:* *Zenith shall not sell or lease the Equipment* — fine (both prohibited); but *Zenith
  shall not sell and lease the Equipment* prohibits only doing both.
- *After:* state each prohibition: *Zenith shall not sell the Equipment, and Zenith shall not lease
  the Equipment.*

**Syntactic: inclusive or exclusive `or`.**
- *Before:* *Acme may terminate for breach or insolvency* (both at once?)
- *After:* *Acme may terminate if either of the following occurs: (a) …; (b) ….*

**Contextual** — two provisions that each claim to govern.
- *Before:* Section 3 says payment is due in 30 days; Section 9 says *notwithstanding anything to the
  contrary* payment is due on delivery.
- *After:* put the exception in Section 3: *… except that payment for an Expedited Order is due on
  delivery.*

**Antecedent** — *it*, *such*, *the same*, *the foregoing* with two candidates.
- *Before:* *Acme shall deliver the Report and the Invoice, and Zenith shall approve it.*
- *After:* *… and Zenith shall approve the Report.*

**Number** — singular/plural subjects with distributive duties.
- *Before:* *The Guarantors shall pay $1,000,000* (each, or together?)
- *After:* *Each Guarantor shall pay $1,000,000* or *The Guarantors are jointly and severally liable
  to pay $1,000,000.*

**Enumeration** — a trailing qualifier after a list.
- *Before:* *(a) reports, (b) invoices and (c) notices sent by email* (only notices by email?)
- *After:* tabulate with *sent by email* in the stem, or in its own sentence.

**Time** — endpoints and direction.
- *Before:* *between June 1 and June 10*; *within 10 days of delivery*.
- *After:* *from June 1 through June 10, inclusive*; *no later than 10 days after delivery*.

**Undefined capital** — a label with no definition.
- *Before:* *the Services* (never defined).
- *After:* define it once, or use lowercase if ordinary meaning is intended.

**Category leakage** — the verb form claims the wrong job (the subject of
`references/categories-of-contract-language.md`).
- *Before:* *The Term shall survive termination.*
- *After:* *Sections 5, 6 and 9 survive termination.*

## §4 The audit procedure

For any clause that moves money or allocates risk, read it four times, once for each question, and
write down the answer each time:

1. **Who acts?** Find the subject of every verb. A duty with no party as subject is passive or
   policy; a passive duty gets its actor.
2. **What category?** Tag each sentence from the taxonomy. Anything tagged twice is split.
3. **What is the scope of every modifier?** For each adjective, adverb, phrase and trailing
   qualifier, ask which words it attaches to; if the answer is not forced, tabulate or repeat.
4. **What are the conditions, and are they conditions?** For each *if*, *unless*, *provided*,
   *subject to*, *notwithstanding*: is this a condition, an exception or a new rule, and does the
   form say so?

Then run the linter on the revised clause and confirm the only findings left are flags with named
owners.
