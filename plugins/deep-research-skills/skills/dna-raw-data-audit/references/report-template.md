# The report template

Every audit carries these six sections, in this order, under these headings — including the audits
that cannot proceed.

**Contents**
- §1 Executive summary
- §2 Hyper-thorough analysis
- §3 Assessment and reasoning
- §4 Statistics breakdown
- §5 Additional research findings
- §6 Conclusion
- §7 Degraded reports, and the serious-finding path
- §8 Worked skeleton

---

## §1 Executive summary

**Written for someone who will read nothing else.** Plain language. No rsIDs, no grade codes, no
notation. If a sentence needs the rest of the report to parse, it does not belong here.

Must contain:
- **What the files are** and what kind of data they hold — one sentence, in plain terms, including
  whether this is array or sequencing data, because it governs everything else.
- **What was found** — in plain terms, and if the answer is "nothing that changes what you should
  do", say exactly that, here, first.
- **What to do**, as a short list. If the list is empty, say so.
- **What this cannot tell you** — the most under-reported and most important part of a genetic
  report. State it here rather than in a footnote.

Do not soften here and sharpen below, or the reverse. A reader who stops after this section should
not be surprised by the rest.

## §2 Hyper-thorough analysis

The complete evidentiary record. Exhaustive by design; length is not a defect here.

- **The quality pass, first.** Format, declared build, total sites, no-call rate, chromosome count,
  and cross-platform concordance with discordant sites named. **Before any interpretation**, because
  it bounds what the interpretation can claim.
- **The finding ledger**, one row per catalogued site that was called: variant · gene · genotype ·
  source file · imputed or measured · array-reliability grade · evidence grade · effect size in
  absolute terms · action or none.
- **The funnel, stated with its numbers** — how many sites, how many catalogue hits, how many
  reliably called, how many actionable. Showing the funnel emptying is informative.
- **What could not be checked, and why** — never probed, no-called, discordant, strand-unresolved,
  requires phasing, requires copy number, requires HLA typing. Each with its mechanism.

## §3 Assessment and reasoning

Per finding, the reasoning a reader can argue with:

- **Both grades** — evidence strength and array reliability — never collapsed into one.
- **The confirmation requirement**, stated explicitly for anything clinically significant.
- **The reasoning**, in a sentence: why this grade, why this action or why none.
- **No composite "genetic risk score".** Conditions have independent baselines and independent
  evidence quality; a single summary number across them is uninterpretable. Say in the report that
  no such score is produced and why, because a reader or a downstream summariser will otherwise
  compute one.

## §4 Statistics breakdown

Every quantitative claim, with its arithmetic visible:

- **Absolute beside relative**, with the baseline, for every risk figure. Use the template in
  `risk-communication.md` §6.
- **Natural frequencies** — counts of people per 1,000, not percentages of percentages.
- **The measure named**: odds ratio or risk ratio, and the design it came from. Convert where the
  baseline is known, and show the conversion.
- **Age-conditioned** where the literature supports it; stated as unconditioned where it does not.
- **The ancestry caveat applied**, not appended — if the person's ancestry differs from the cohorts
  the estimate came from, that belongs beside the number.
- **Intervals**, not just point estimates.

## §5 Additional research findings

The current-literature pass. Sections 2–4 report what the catalogue and the files establish; this
section reports what the **literature now says**, which is a different question.

- **What supersedes the catalogue** — newer or larger estimates for any finding reported above.
- **What failed to replicate**, and anything reclassified since.
- **Contradicting work**, found by searching against the finding deliberately.
- **Whether the evidence base is representative**, or whether the quoted estimate comes from a
  narrow population.
- **Every citation resolved to a retrieved record**, with the identifier. The retrieved-record
  standard in `variant-catalog.md` §0 applies at full strength here, because these are citations the
  skill is producing on its own authority.
- **The search disclosed**: which databases, roughly how many queries, date range, where you stopped,
  and what you could not reach.

## §6 Conclusion

- **The verdict in a few sentences**, consistent with §1 and adding the nuance §1 omitted.
- **The clinician-ready question list** — the most actionable artifact the skill produces. Format in
  `interventions-evidence.md` §7 and `pharmacogenomics.md` §5.
- **Linked references, in two groups**: the catalogue entries relied on, and the independent research
  from §5, each with a working identifier.
- **A verification line**: how identifiers were checked, and anything that could not be verified.
- **What you chose not to report**, if the person's `your-environment.md` asked for findings to be
  withheld. Note that something was withheld at their request, without naming it.

---

## §7 Degraded reports, and the serious-finding path

**A report that cannot proceed keeps all six headings** and says under each what could not be
determined and why. Collapsing to a one-line apology hides what *was* established and leaves a later
reader unable to tell whether the audit was attempted.

| Failure | What the report does |
| :--- | :--- |
| File unreadable or unrecognised format | §1 says so in the first sentence; §2 carries the parse error; no findings anywhere |
| Build undeclared | Proceed on rsID-based lookups only; state that positional interpretation was not attempted |
| Only one of two files supplied | Proceed, and state that no concordance check was possible — a named reduction in confidence |
| Data is low-pass/imputed | Proceed, and grade every finding accordingly; no clinical finding rests on an imputed call |
| Ancestry unknown | Proceed, but §4 reports every estimate with the portability caveat unresolved rather than silently assuming European-ancestry applicability |
| Funnel empties | **Report the empty funnel.** §1 says nothing changes; §2 shows the numbers that emptied it. This is a complete report, not a failed one |

**The serious-finding path, which needs stating because improvisation here does harm.** If something
genuinely urgent surfaces — a reliably-called, high-penetrance, actionable variant, or a
pharmacogenomic flag against a drug the person is **currently taking, or is scheduled to start**
(a first chemotherapy dose and a booked operation are the cases where deferral is the harm):

1. **Say it first**, in the first sentence of §1, plainly. Do not bury it in a long report.
2. **Name the confirmation step and the clinician to take it to.** The action is a conversation and a
   test, not a decision.
3. **Do not advise stopping or changing a medication**, even one the data flags. Especially then.
4. **State the uncertainty honestly in the same breath** — unconfirmed consumer data, with a
   materially elevated false-positive rate for exactly this class of variant. Both facts are true
   and the person needs both.
5. **Flag the relatives implication** before going further, if the finding is heritable and
   actionable for them.

---

## §8 Worked skeleton

```
# DNA raw-data audit — <platform(s)>, <n> files
Files: <names, formats, builds> · Sites: <n> · No-call rate: <%> · Concordance: <%>

## 1. Executive summary
<What the files are, in plain terms.>
<What was found — or that nothing was.>
What to do: <short list, or "nothing follows from this data">
What this cannot tell you: <the probed-subset limitation, in plain terms>

## 2. Hyper-thorough analysis
### Quality pass
| file | format | build | sites | no-calls | rate |
Concordance: shared / comparable / concordant / discordant (+ named discordant sites)
### Finding ledger
| variant | gene | genotype | source | measured? | R-grade | E-grade | absolute effect | action |
### The funnel
all sites -> catalogue hits -> called -> reliably called -> actionable -> after confirmation
### Not checked
| site | why | mechanism |

## 3. Assessment and reasoning
Per finding: E-grade, R-grade, confirmation requirement, reasoning.
NO COMPOSITE GENETIC SCORE — independent baselines and independent evidence quality.

## 4. Statistics breakdown
Per quantitative finding, via the risk-communication template:
  baseline N in 1,000 -> carrier N in 1,000 -> difference -> relative -> measure, design, interval
  ancestry applicability stated beside the number
### In plain terms
Out of 1,000 people like you, N would ...; with this genotype, about M do.

## 5. Additional research findings
### What supersedes the catalogue
### Failed replications and reclassifications
### Contradicting work
### Is the evidence base representative?
### Search disclosure
databases · queries · date range · stopping point · not reached

## 6. Conclusion
<Verdict, a few sentences.>
### Questions for a clinician
1. <specific, answerable question> — with the finding, the grade, and the confirmatory test
### References
Catalogue entries relied on | Independent research (§5) — each with a resolved identifier
### Verification
<How identifiers were checked; anything unverified, named.>
<Note if findings were withheld at the person's request.>
```
