# Claim audit method

Turning a transcript into a defensible ledger: what counts as a claim, what kind of claim it is,
what in the source it gets compared against, how faithfully it was represented, and what was left out.

**Contents**
- §1 Decomposing the transcript into claims
- §2 The claim typology
- §3 Locking the comparison target (the highest-leverage rule here)
- §4 The fidelity precedence ladder
- §5 The comprehensiveness checklist
- §6 Worked example

---

## §1 Decomposing the transcript into claims

A **claim** is a statement that could in principle be checked against something outside the video.

**Counts as a claim:** an assertion of fact, a number, a causal statement, an attribution ("Dr. X
found"), a comparison, a prediction with a stated basis, a definition presented as standard.

**Does not count:** opinion clearly marked as such, rhetorical questions, jokes, sponsor reads,
personal anecdote offered as anecdote, hedged speculation explicitly flagged ("I suspect, though
nobody's tested this"). Auditing these produces noise and inflates the denominator.

**Procedure.** Walk the transcript in order. For each claim record: timecode, verbatim quote,
paraphrase, and weight class.

**Weight classes** — assign before auditing, so the audit cannot be motivated:
- **Load-bearing** — the video's thesis fails without it. **Pre-register 3–5.** If you cannot name
  them before checking sources, you do not yet understand the video's argument.
- **Supporting** — buttresses a load-bearing claim but is not itself decisive.
- **Aside** — background, colour, framing.

Claims built across several minutes are recorded once, at the timecode where the assertion
completes, with the span noted. Do not split a single argument into six claims to inflate a count —
and note that the grading instrument is rate-based partly so that this kind of splitting cannot
change the grade much.

---

## §2 The claim typology

Different claim types need different verification. Naming the type prevents applying the wrong test.

| Type | Example | What verification actually requires |
| :--- | :--- | :--- |
| Empirical-quantitative | "cut mortality 30%" | the source's number, its arm rates, its interval, its endpoint |
| Empirical-qualitative | "most participants improved" | the source's reported proportion; "most" is checkable |
| Causal | "X causes Y" | the source's *design*, not its wording — an observational study cannot license this |
| Mechanistic | "X depletes Y, which explains Z" | whether the source tested the chain or only a link; mechanism is a lead, not a finding |
| Predictive | "this will halve cases by 2030" | the model, its assumptions, its stated uncertainty |
| Definitional | "insulin resistance means…" | a standard reference; a nonstandard definition quietly changes every downstream claim |
| Attributive | "Dr. X says…" | that X said it, **in that context** — the commonest quote-mining site |
| Negative/existential | "no study has ever shown" | asymmetric: hard to prove, easy to refute with one counterexample. Search specifically before accepting or rejecting |
| Comparative | "better than the standard treatment" | a head-to-head source, or an explicit statement that the comparison is indirect |
| Normative | "you should…" | not checkable as fact; audit whether the stated evidence supports the strength of the recommendation |

---

## §3 Locking the comparison target

**Do this before classifying anything.** It is the rule that makes fidelity classification
reproducible instead of arbitrary.

The same video claim can be faithful or overstated depending purely on *which part of the source*
you compare it against. A claim of "cuts risk in half" is overstated against a trial's primary
result and faithful against one of its subgroups. If the auditor picks the comparison after seeing
the claim, the classification is chosen, not found — and two auditors will never agree.

**The rule:** compare against the source's **prespecified primary analysis** — the primary endpoint,
in the whole randomized population, as the protocol defined it. Record what that is, in the ledger,
before classifying.

**Then, separately**, if the video's number matches a *secondary* result — a subgroup, a secondary
endpoint, a per-protocol analysis, a post-hoc slice — that is not a rescue. It is a distinct
finding, coded `SELECTIVE-ANALYSIS`, and it belongs in the ledger as such. The number being real is
exactly what makes the move effective; a viewer cannot catch it by checking whether the figure
appears in the paper, because it does.

---

## §4 The fidelity precedence ladder

Mutually exclusive categories are impossible here — a mouse finding stated as a human causal fact
with an inflated number is simultaneously scope-inflated, strength-inflated, and overstated. Forcing
one choice makes the code arbitrary. So: **run the ladder top-down, take the first code that fires
as the primary, and record the rest as secondary tags.**

| Code | Name | Fires when | Score |
| :--- | :--- | :--- | ---: |
| **F6** | Fabricated | the cited source does not exist, or does not resemble the claim at all (confirm reachability first — see acquisition §5) | 0.00 |
| **F5** | Reversed | the source's finding points the other way, or the video states as established what the source rejected | 0.00 |
| **F4** | Unsupported | the source exists and is real but simply does not contain the claim | 0.10 |
| **F3** | Scope-inflated | true of the studied population, stated for a wider one — mice to humans, one subgroup to everyone, short trial to lifelong use | 0.25 |
| **F3s** | Strength-inflated | correlation stated as causation; a lead or mechanism stated as a finding; "may" become "does" | 0.25 |
| **F2** | Overstated | direction right, magnitude or certainty inflated enough to change the practical conclusion | 0.50 |
| **F2u** | Understated | the mirror image: a real effect or a real harm minimized. Most taxonomies omit this and thereby only catch hype, not burial | 0.50 |
| **F1** | Imprecise | loose but conclusion-preserving — rounding, informal phrasing | 0.85 |
| **F0** | Faithful | a reader of the source would recognise the video's version | 1.00 |
| **NC** | Not checkable | source unreachable or claim unfalsifiable — **excluded from the denominator**, never scored 0 | — |

Secondary tags that ride alongside the primary code: `SELECTIVE-ANALYSIS`, `QUOTE-MINED`,
`CHERRY-PICKED` (true, but the source's own contradicting result is omitted), `OUT-OF-CONTEXT`,
`STALE` (source retracted or superseded — note this grades on *comprehensiveness*, not accuracy).

### The conclusion-change test — the F2/F1 boundary

This boundary is where inter-rater agreement dies, because "is this overstated?" is a graded
aesthetic judgment. Replace it with one binary question:

> **Would a reasonable viewer who heard the video's version reach a different practical conclusion
> than a reader who saw the source's version?**

**No → F1. Yes → F2.**

- "8,432 people" rendered as "about 10,000 people" — changes no conclusion → **F1**.
- "A randomized trial found sleep extension dropped blood pressure 4 points", where the source is
  n=40, −4.1 mmHg, 95% CI −9.2 to +1.0, p=0.11, and a *secondary* endpoint. Every word is
  defensible. But the video's viewer concludes "sleep extension lowers blood pressure" and the
  source's reader concludes "suggestive, unproven" → **F2**, tagged `SELECTIVE-ANALYSIS`.

### The video is right and the source is wrong

Keep these separate, always. A video that faithfully reports a study that was later retracted, or
that failed to replicate, has **not** misrepresented its source. Coding that as an accuracy failure
breaks the axis's meaning and is unreproducible, because auditors will disagree about what the
creator should have known. Route it to comprehensiveness (omission O7, §5) and raise the
`FAITHFUL-TO-BAD-SOURCE` interlock flag so the accuracy letter is never read alone.

The same routing applies to press-release distortion: when the exaggeration is already present in
the source's own press release and the video repeated it, say so. That is a failure to check, not
an act of invention, and the report should name which one it found.

---

## §5 The comprehensiveness checklist

"Did the video omit anything important?" is unbounded — an auditor can always name one more missing
paper, so two auditors never converge. **Bound it.** Score these items per load-bearing claim,
yes/no, answerable from the transcript alone:

1. **Source identified** — named or shown specifically enough to find.
2. **Design stated** — RCT, cohort, case report, animal, in vitro, modelling.
3. **Population/scope stated** — who it was studied in, and who it therefore applies to.
4. **Absolute terms given** — the effect in absolute terms, or the baseline alongside the relative.
5. **Uncertainty conveyed** — an interval, a sample size, or at minimum "one small trial".
6. **A limitation noted** — any real limitation of the evidence, including the source's own.
7. **Contrary evidence acknowledged** — the main contradicting finding named, or a correct
   statement that none exists.
8. **Representativeness** — whether the cited source is typical of the body of evidence, or an
   outlier selected from it. This is the item that catches cherry-picking.
9. **Conflicts disclosed** — funding or COI where material. Score `N/A` and drop from the
   denominator when none exists.

Plus two video-level items: a **scope statement** (what the video is not claiming), and whether
**corrections** are surfaced (pinned comment, on-screen note) where the creator has issued any.

**Omission types worth naming in the report:** O1 base rate omitted · O2 absolute effect omitted ·
O3 uncertainty omitted · O4 population narrowed in the source but not the video · O5 contrary
literature omitted · O6 harms or side effects omitted while benefits are given · O7 relies on a
retracted, superseded, or failed-to-replicate source without noting it · O8 funding/COI omitted.

Score `C_raw` = items satisfied ÷ items applicable. Expect genuine, well-intentioned explainers to
land at roughly 25–45%: the checklist is demanding by construction, which is why comprehensiveness
gets its **own** band table in the grading rubric rather than sharing accuracy's.

---

## §6 Worked example

Illustrative and invented — not an audit of any real creator. Every number below is recomputed
from the setup.

**The source (fictional trial):** 2,000 randomized, 1,000 per arm. Primary endpoint, whole
population: 120/1,000 events on control (12.0%), 90/1,000 on treatment (9.0%).
RR = 0.09/0.12 = **0.75**, 95% CI 0.579–0.972. RRR = 25.0%. ARR = 3.0 percentage points.
NNT = 1/0.03 = 33.3 → **34**.

One of eight prespecified subgroups, men under 65 (400 per arm): 60/400 control (15.0%), 30/400
treatment (7.5%). RR = **0.50**, 95% CI 0.330–0.758. ARR = 7.5 pp. NNT = 13.3 → **14**.
With 8 subgroups examined at α = 0.05, P(at least one false positive) = 1 − 0.95⁸ = **33.7%**.

**The claims:**

| # | Timecode | Claim | Weight | Primary code | Tags | Reasoning |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 02:14 | "This drug cuts your risk in half." | Load-bearing | **F2** | `SELECTIVE-ANALYSIS` | 0.50 is real — it is the men-under-65 subgroup. Against the locked target (primary, whole population) the figure is 0.75. A viewer concludes "halves risk"; a reader concludes "cuts it by a quarter" → conclusion changes → F2, not F1. |
| 2 | 03:40 | "In a trial of two thousand people." | Supporting | **F0** | — | Correct. |
| 3 | 05:02 | "So about one in three people benefit." | Load-bearing | **F4** | — | Nothing in the source supports this. ARR is 3.0 pp, i.e. 3 in 100 benefit, NNT 34. The claim is off by roughly an order of magnitude and is not a rounding of anything the paper reports. |
| 4 | 07:55 | "Researchers said it was a breakthrough." | Aside | **F3s** | `QUOTE-MINED` | The paper's discussion says "warrants further study". Strength inflated from hedge to endorsement. |

**Comprehensiveness on claim 1** (9 items, COI `N/A` → denominator 8): source identified ✓;
design stated ✓ ("a trial"); population ✗ (the subgroup restriction is never mentioned);
absolute terms ✗; uncertainty ✗; limitation ✗; contrary evidence ✗; representativeness ✗.
C_raw for this claim = 2/8 = **0.250**.

**What the audit says.** The video's headline number exists in the paper — that is precisely why it
works. The finding is not "they made it up"; it is "they quoted a subgroup result as the headline
without saying it was a subgroup, in a trial that examined eight subgroups, where the chance of at
least one spuriously large subgroup effect was about one in three." That sentence is the audit.
