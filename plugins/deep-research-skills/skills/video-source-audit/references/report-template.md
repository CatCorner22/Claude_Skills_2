# The report template

Every audit this skill produces carries these six sections, in this order, under these headings —
including the audits that fail. What follows is what belongs in each, why, and a worked skeleton.

**Contents**
- §1 Section 1 — Executive summary
- §2 Section 2 — Hyper-thorough analysis
- §3 Section 3 — The grade and reasoning
- §4 Section 4 — Statistics breakdown
- §5 Section 5 — Additional research findings
- §6 Section 6 — Conclusion, with links
- §7 Degraded reports: keeping the structure when the audit fails
- §8 Worked skeleton

---

## §1 Section 1 — Executive summary

**Written for someone who will read nothing else.** Plain language. No notation, no `F3s` codes, no
`RR`, no band thresholds. If a sentence needs the rest of the report to parse, it does not belong
here.

Must contain:
- What the video claims, in one short paragraph — stated fairly, as the creator would recognise it.
- What the audit found, in one short paragraph.
- The three grades, named in words as well as letters ("accuracy: C-, meaning several load-bearing
  claims went further than their sources").
- **The bottom line**: should a reasonable person act on this video? Answer it directly.
- The honest uncertainty. If the audit rests on three claims, or on abstracts only, say so *here* —
  not buried in section 2 where a skimming reader will miss it.

Do not soften the finding for the summary and sharpen it below, and do not do the reverse. A reader
who only reads this section should not be surprised by the rest.

## §2 Section 2 — Hyper-thorough analysis

The complete evidentiary record. This is the section that makes the audit checkable, so it is
exhaustive by design and length is not a defect here.

- **The logical-form summary**: thesis → claims offered in support → evidence offered for each →
  the action the video wants the viewer to take. Note what is asserted with no support at all.
- **The claim ledger**, one row per claim: timecode · verbatim quote · weight class · source ·
  depth tier read (T0–T3) · **the locked comparison target** · fidelity code and secondary tags ·
  the reasoning in one sentence.
- **The comprehensiveness checklist**, scored per load-bearing claim, with `N/A` items shown as
  dropped from the denominator rather than silently removed.
- **What could not be checked, and why** — unreachable sources, on-screen-only citations, paywalled
  full text, ambiguous references. Each with its mechanism, per `acquisition-and-sources.md` §1.

## §3 Section 3 — The grade and reasoning

- The three letters, each with its **provenance line**: the raw score, the band it lands in, which
  cap fired if any, and whether the two mechanisms agree.
- **Boundary disclosure** where a score sits within 0.02 of a band edge.
- **Interlock flags**, printed above the grades with a sentence saying what each means.
- **The explicit no-composite statement.** Say in words that the three axes are not averaged and
  why — otherwise a reader or a downstream summariser will do it.
- **The highest-leverage fix, computed** by re-scoring with each unit set to clean, not guessed at.
  Report the band gain. If the intuitively obvious fix gains nothing, say that too — it is often
  the most useful line in the report.

Full instrument: `grading-rubric.md`.

## §4 Section 4 — Statistics breakdown

Every statistical statement in the video gets a row. For each:

| What the video said | What the source says | The move | Corrected figure |
| :--- | :--- | :--- | :--- |
| verbatim quote + timecode | the source's actual number, with its endpoint and population | the named taxonomy entry | the honest statement |

Then, mandatory:
- **The absolute-vs-relative reconstruction, with its arithmetic shown.** State CER, RRR, and
  compute `ARR = CER × RRR` and `NNT = 1/ARR` in the open so a reader can follow. Where the
  control-arm rate is unavailable, say the absolute effect cannot be determined — do not invent a
  baseline.
- **A natural-frequency translation of every headline number** — the four-part template in
  `statistics-taxonomy.md` §0. Counts of people, not percentages of percentages.
- **The asymmetric-framing table**: every benefit claim and every harm claim with the *scale* each
  was given on, and whether the scales match. Include it even when it comes back clean, because a
  clean result is a finding.

## §5 Section 5 — Additional research findings

The independent literature pass, broken down thoroughly. This is the section that separates
an audit from a fact-check: sections 2–4 ask whether the video quoted its sources correctly; this
one asks whether its picture of the evidence is the right one.

Structure it as the five questions in `acquisition-and-sources.md` §7:

1. **Is the cited evidence representative?** What the wider search returned, and how the video's
   selection compares to it.
2. **Higher-tier evidence the video ignored** — systematic reviews, meta-analyses, guidelines that
   supersede its primary studies.
3. **Contradicting work**, found by searching against the thesis deliberately.
4. **Retractions, corrections, failed replications** affecting anything load-bearing.
5. **What the weight of evidence actually says** — plainly, with its own confidence, including
   "genuinely unsettled" where that is the truth.

Then, non-negotiably:
- **Every finding carries a resolvable identifier and how it was verified.** These are citations the
  video never made, so they are the auditor's own responsibility, and the retrieved-record standard
  in `further-reading.md` §0 applies at full strength.
- **The search disclosure**: which databases, roughly how many queries, what date range, where you
  stopped, and what you could not reach. An independent pass with an undisclosed stopping point is
  an opinion with a bibliography.
- **Publication dates relative to the video.** Work published after the video informs the reader but
  cannot lower the video's accuracy grade; keep the two uses visibly separate.

## §6 Section 6 — Conclusion, with links

- **The verdict in three to five sentences**, consistent with section 1 and adding the nuance that
  section 1 deliberately left out.
- **The linked reference list, in two clearly separated groups:**
  - *The video's sources* — every one, with its identifier, the depth tier it was read at, and its
    fidelity outcome.
  - *The independent research* — everything from section 5, with identifiers.
- **A verification line** stating how identifiers were checked (resolver API, or retrieved search
  records) and naming anything that could not be verified.
- **Further reading** for a reader who wants to get better at this themselves — draw from
  `further-reading.md` and pick the two or three that fit this particular video's failure mode
  rather than pasting the list.

Every identifier must actually resolve. A conclusion whose links are decorative undoes the whole
audit, since checkability is the only thing separating this report from an opinion.

## §7 Degraded reports: keeping the structure when the audit fails

**A `NOT-GRADED` or `INCOMPLETE` report keeps all six headings.** Under each, say what could not be
determined and why. The temptation is to collapse to a one-line apology, and it is the wrong move:
the reader then cannot tell what *was* established, and a later reader cannot tell whether the audit
was attempted at all.

- **Section 1** states plainly that the video could not be audited, and why, in the first sentence.
- **Section 2** carries whatever ledger was built before the failure, even if partial.
- **Section 3** prints `NOT-GRADED` or `INCOMPLETE` with the precondition that failed, in place of
  letters — and still applies the precedence rule, since a cap that fired on verified evidence
  survives a thin sample.
- **Section 4** carries any statistical statements that could be checked, and names those that
  could not.
- **Section 5 is often still possible and still valuable.** Even with no transcript, the independent
  literature pass on the video's *topic* can tell the reader what the evidence says. Do it, and
  label it as answering the topic rather than auditing the video.
- **Section 6** links whatever was resolved, and states the failure mechanism one last time.

## §8 Worked skeleton

```
# Audit — "<video title>" (<channel>, <upload date>)
Source: <url> · Transcript: <fetched|pasted|unavailable> · Audited <n> claims

## 1. Executive summary
<Plain-language paragraph: what it claims.>
<Plain-language paragraph: what we found.>
Grades — Accuracy: C- · Comprehensiveness: D- · Statistics: D
Flags: SELECTION-DISTORTED
Bottom line: <direct answer to "should I act on this?">
Confidence: <what this rests on, and what it does not>

## 2. Hyper-thorough analysis
### Logical form
Thesis · Supporting claims · Evidence offered · Requested action · Asserted without support
### Claim ledger
| # | Time | Claim | Weight | Source | Tier | Comparison target | Code | Reasoning |
### Comprehensiveness checklist
| Item | LB-1 | LB-2 | LB-3 |
### Not checkable
| Claim | Why | Mechanism observed |

## 3. The grade and reasoning
Accuracy:          C-  (score 0.637 -> band C-; cap C- from 2 unsupported load-bearing
                        claims; both mechanisms agree)
                       boundary: 0.017 above the C-/D+ line
Comprehensiveness: D-  (C_raw 0.250 = 7 of 28 applicable items)
Statistics:        D   (S_raw 0.587 -> band C; capped at D by one flatly wrong figure)
NO COMPOSITE GRADE — the three axes fail independently and averaging them is misleading.
Highest-leverage fix (computed): <unit> -> +<n> bands. Note: <the obvious fix> gains 0.

## 4. Statistics breakdown
| Video said | Source says | Move | Corrected |
### Absolute vs relative, worked
CER = ... · RRR = ... · ARR = CER x RRR = ... · NNT = 1/ARR = ...
### In plain terms
Out of 1,000 people, ... would have ...; with ..., ... do. So ... in 1,000 are spared.
### Asymmetric framing
| Claim | Benefit/Harm | Scale used | Match? |

## 5. Additional research findings
### Is the cited evidence representative?
### Higher-tier evidence the video ignored
### Contradicting work
### Retractions, corrections, failed replications
### What the weight of evidence says
### Search disclosure
Databases · queries · date range · stopping point · not reached

## 6. Conclusion
<Verdict, 3-5 sentences.>
### The video's sources
| Source | Identifier | Tier read | Fidelity outcome |
### Independent research
| Source | Identifier | What it establishes |
### Verification
<How identifiers were checked; anything unverified, named.>
### Further reading
<2-3 items matched to this video's failure mode.>
```
