# Live routing and listing-degradation findings — 2026-08-18

> ## ⚠ CORRECTED 2026-08-19 — this document's central mechanism claim was wrong
>
> An independent audit of this file (deliberately run by agents that did **not** write it, because
> its author could not check its own numbers) found that §1 and §2 as originally published were
> wrong in mechanism and wrong in severity. Both sections have been rewritten below and the
> superseded text is quoted inline so the error stays legible. In summary:
>
> | Originally published | Actually true (read from the shipped binary, v2.1.235) |
> |---|---|
> | "a **sequential fill in listing order, with a hard cutoff** … **not** a priority ordering by usage" | It **is** a priority ordering by usage: candidates are sorted descending by `usageCount × max(0.5^(daysSinceUse/7), 0.1)`, then greedily upgraded, **skipping and continuing** rather than cutting off. |
> | The 2026-07-18 folklore ("trims least-used descriptions") is "corrected" | The folklore was **closer to the truth than this document's correction of it.** It named the right variable. |
> | "19 FULL … about **2.3% of a 200K-token window**" | Measured in a session whose real budget was ~30,000 chars, i.e. a ~750K context. At the genuine 200K default the budget is **8,000 chars** and only **3 of 121** skills keep a description. The published figure *understated* the problem. |
> | "**101 of 121 NAMEONLY**" | Obtained by asking a model to introspect its own system reminder — an instrument that does not reproduce reliably. Superseded by the mechanical simulation in §2. |
>
> What survived the audit: the two settings named below are real and their defaults are correct
> (one auditor wrongly reported that `skillListingBudgetFraction` does not exist in the CLI; it
> does, four times, and the CLI's own over-budget warning tells the user to raise it). The
> tokenizer cost figures in §3 reproduced to the digit. The live routing results in §4 stand.

This document records measurement, and now also records where that measurement was
over-generalized. Everything in §3–§5 was produced by the real Claude Code harness — the actual
skill-loading mechanism and the actual `Skill` tool — not by a simulation. Method, tooling, and
every number are recorded so the next person can reproduce or falsify any of it; §1 and §2 are
the worked example of why that matters.

## 0. How this was run

`claude plugin eval` and `claude plugin marketplace` are real, shipped commands
(`claude plugin --help` lists them), gated behind a per-organization early-access flag. The gate
can be opened for a single shell via `CLAUDE_CODE_WALNUT_SPIRE=1`, set in the environment — not
committed to any repo settings file, which is why this file records the *finding*, not the
enablement mechanism, as the thing to reuse.

Setup performed:
```bash
CLAUDE_CODE_WALNUT_SPIRE=1 claude plugin marketplace add /home/user/Claude_Skills_2
CLAUDE_CODE_WALNUT_SPIRE=1 claude plugin install <plugin>@treasury-analyst-skills   # all 14
```
All 14 plugins were installed at `user` scope, so this session's real skill listing genuinely
carried all 121 skills, exactly as an end user's would after `/plugin install` on every plugin
in this marketplace — plus this session's own separately-installed personal skill set (~20-30
skills, not inventoried here), which competes for the same budget.

Total real spend across everything below: **≈ $0.93** (one $0.33 baseline run before a target
was correctly resolved, plus seven $0.06–$0.11 live routing cases). Disclosed in full because
`claude plugin eval` spends real money per run and the number should be checkable.

## 1. The real degradation mechanism — read from the code, not inferred from behaviour

`MEMORY.md` carried a single anecdotal lesson from 2026-07-18, from an unrelated prior project:
*"With ~100 installed skills, the skill-listing context budget trims least-used descriptions to
name-only."* The 2026-08-18 pass declared that folklore corrected. **The folklore was closer to
the truth.** It named the right variable — usage — and the "correction" replaced it with a wrong
one. What follows is decompiled from the shipped binary rather than inferred from observed
output, which is why it can be stated without hedging.

**The settings** (real, and their `describe()` text is the product's own documentation):

- `skillListingBudgetFraction` — default `0.01`, the fraction of the context window (**in
  characters**) reserved for the skill listing. The CLI's own over-budget warning names it:
  *"descriptions will be truncated. Run /skills to disable some, or raise
  skillListingBudgetFraction in settings."*
- `skillListingMaxDescChars` — default `1536`, per-skill description cap.

**The budget, exactly.** `SLASH_COMMAND_TOOL_CHAR_BUDGET` wins if set; otherwise the budget is
`max(1, floor(context_tokens × 4 × fraction))`, where `4` is the harness's chars-per-token
constant and the default context is `200000`. So:

> **default budget = 200,000 × 4 × 0.01 = 8,000 characters.**

**The algorithm, exactly.** Reconstructed from the shipped code path:

1. Start from a baseline where **every** candidate skill is rendered name-only as `- name`
   (cost `len(name) + 2`), plus one newline per entry.
2. **Bundled skills are protected** and always keep their full text — they are added to the
   protected set before any trimming and never compete. Only plugin and user skills are
   candidates. *(This is a finding the original pass missed entirely, and it matters: the
   built-in skills you did not install are not what is crowding out the ones you did.)*
3. Sort the candidates **descending by a usage score**:
   `usageCount × max(0.5^(daysSinceUse / 7), 0.1)` — a 7-day half-life, floored at 0.1. **A skill
   that has never been used scores exactly 0.**
4. Walk that sorted list and greedily upgrade each candidate from name-only to full **if its
   incremental cost fits the remaining budget; otherwise skip it and continue.** There is no
   cutoff — a long description can be skipped while a shorter one later in the order still fits.
5. Emit each entry as its full form if protected or upgraded, else as `- name`.

So the listing genuinely is a **mixed** set of full and name-only entries, prioritised by recent
usage. Two consequences the original pass got backwards:

- **It is usage-prioritised.** The superseded text asserted the pattern was "**not** a priority
  ordering by usage, importance, or size." That is false.
- **The install-order pattern that was observed is real but is the degenerate case.** In a fresh
  session nothing has been used, so every candidate scores 0; with all keys tied, the sort is
  stable and the candidates retain their original listing order. That is why an install-order
  fill was observed. It is what the usage algorithm does *when there is no usage yet* — not a
  different algorithm. The practical implication is the opposite of what was published: the
  arbitrariness is **temporary**, and a returning user's frequently-used skills do keep their
  descriptions.

**On the original live observation (101 of 121 NAMEONLY, 19 FULL).** That came from asking a
fresh non-interactive session to introspect its own skill listing and report
`plugin:skill<TAB>FULL|NAMEONLY` pairs. The independent audit re-ran that instrument and could
not reproduce it stably (the same skill reported FULL in one run and NAMEONLY in another, and
the reported skill count varied). **The instrument is not trustworthy for this purpose and the
figure is withdrawn**; §2 replaces it with a simulation of the algorithm above, which needs no
introspection. The direction of the original finding — that most of this library loses its
descriptions on a full install — survives, and gets worse.

One detail from the original scan does stand independently:
`machine-learning-skills:bespoke-llm-architect` sets `disable-model-invocation: true` and does
not appear in the general listing at all, consistent with its by-design invoke-only status.

The one not applicable is `machine-learning-skills:bespoke-llm-architect`, which sets
`disable-model-invocation: true` — it does not appear in the general listing at all, consistent
with its by-design invoke-only status (already known from the trigger-test protocol's Tier D
exclusion).

> **Superseded text, kept for the record.** The original §1 continued: *"The pattern is a
> **sequential fill in listing order, with a hard cutoff** — everything before the cutoff keeps
> its full text, everything after loses it entirely — not a priority ordering by usage,
> importance, or size."* Both halves are wrong: the fill skips-and-continues rather than cutting
> off, and the ordering *is* by usage. The supporting observation — that within
> `coding-agent-skills` the FULL skills were its first 14 in alphabetical order and the NAMEONLY
> ones the last 6 — is consistent with the all-zero-usage degenerate case, and the apparent
> clean "cutoff" is explained by those descriptions being of similar length, not by a cutoff
> existing in the code.

**Reproducibility check.** A second, differently-worded query without explicit name-tagging
produced answers that did not match the first scan — investigated, and the mismatch was a
methodology defect (the model's unlabeled reply couldn't be reliably position-matched to the
four skills asked about), not evidence that the underlying state is unstable. Re-run with
explicit `name<TAB>status` pairs required for every answer, the second query reproduced the
first exactly (`gonzo`=FULL, `sparring-partner`=NAMEONLY, `agent-harness-config`=FULL,
`value-stream-mapping`=NAMEONLY, matching the full scan). **Lesson for reuse: never ask this kind
of live-introspection question in a form that lets the model drop the label — the three prior
occurrences in this protocol of "the test prompt was the defect" all trace to the same root
cause, an under-specified prompt.**

## 2. The real severity, computed from the algorithm rather than introspected

The original §2 reported **17,104 characters / 19 FULL skills ≈ 2.3% of a 200K window**. That
framing does not hold: the session it was measured in had a real budget of ~30,000 characters
(the harness's own over-budget log recorded `129115 chars > 30000 budget`), which corresponds to a
context of roughly 750K, not 200K. Reporting a large-context measurement as a fraction of 200K
made the situation look **milder than it is**.

Simulating the §1 algorithm directly against this library's 121 real frontmatter descriptions —
no model introspection involved, name-only cost taken exactly as `len(name) + 2` from the code:

| Context window | Budget (1%) | Skills keeping a full description | Name-only |
|---|---:|---:|---:|
| **200K (the default)** | **8,000 chars** | **3** | **118** |
| 750K | 30,000 chars | 27 | 94 |
| 1M | 40,000 chars | 38 | 83 |

The name-only baseline for 121 skills is **5,575 characters**, so at the default budget only
~2,400 characters remain for descriptions — roughly three of them. The full undegraded listing
for this library is **113,645 characters**, i.e. **14.2%** of a 200K window's character
equivalent.

Three things follow:

1. **On a default 200K session, a full install of this library routes on bare names alone**, for
   118 of 121 skills. That is the honest headline, and it is considerably worse than the
   withdrawn 83% figure.
2. **The arbitrariness is temporary, not permanent.** Which skills survive is decided by recent
   usage, so a returning user's working set does keep its descriptions. A *first* session with a
   fresh install is the worst case, not the steady state. The original claim that "there is no
   way to install the important skills first as a mitigation" is true as far as it goes, but the
   mitigation that does exist is simpler: use the skills you care about, and they win the budget.
3. **Subsetting is still the right lever, and now for a precise reason.** Not because descriptions
   are too long — trimming them was the wrong pass — but because 121 skills cannot fit any
   plausible budget, while a 20–30 skill subset fits 8,000 characters comfortably. The per-plugin
   cost table in §3 is the tool for choosing that subset.

## 3. Real token cost, cross-checked against a second, independent measurement

`claude plugin details <plugin>` reports a harness-computed "always-on" token cost per plugin,
using the actual tokenizer rather than a chars-per-token estimate. Summed across all 14 plugins:

| Plugin | Always-on (real tokenizer) |
|---|---:|
| coding-agent-skills | ~6,806 |
| collaboration-skills | ~1,727 |
| continuous-improvement-skills | ~5,152 |
| data-analytics-bi-skills | ~3,595 |
| data-tools-skills | ~2,087 |
| decision-science-skills | ~4,932 |
| deep-research-skills | ~346 |
| full-stack-dev-skills | ~3,102 |
| learning-skills | ~892 |
| machine-learning-skills | ~2,047 |
| math-foundations-skills | ~2,000 |
| metacognition-skills | ~1,188 |
| safety-and-reliability-skills | ~3,319 |
| writing-skills | ~1,611 |
| **Total** | **~38,804** |

This repo's own `scripts/measure-listing-cost.py` estimated **29,638–29,718 tokens** for the same
121 skills across this session's measurements, using a 3.7-characters-per-token approximation.
The real, tokenizer-computed figure is **≈ 30% higher**. Spot-checking five individual skills
(writing-skills' full component breakdown) shows the same ~27–29% gap consistently — this is not
noise in one plugin, it is a systematic property of this prose style under the real tokenizer
(heavy use of em dashes, backticks, and punctuation that a flat chars/token ratio undercounts).

**Corrected headline: a full install costs not 14.8% but closer to 19.4% of a 200K window**
(38,804 / 200,000), using the harness's own accounting rather than this repo's estimate. The
`3.7 chars/token` divisor `measure-listing-cost.py` uses is documented as an *estimate*, and this
is the first time it has been checked against the real tokenizer — the check shows the estimate
runs consistently light for this library's prose.

> **Corrected 2026-08-19.** This paragraph originally claimed *"Every place this repo quotes
> 14.8%/14.9% is now corrected to cite both figures, with the real one primary."* That was false
> when written — the audit found two uncorrected instances still standing in `MEMORY.md`
> (lines 218 and 409), one of which also restated the superseded mechanism. Both are now fixed.
> The lesson is narrow and worth keeping: **a sweep is not done because the sweeper says it is.**
> Claiming "every place" requires actually grepping every place, and this document asserted
> completeness it had not verified.

## 4. Live routing tests via the real `Skill` tool — 7 cases, real agent turns

Beyond listing visibility, seven cases were run as genuine agent turns (`claude plugin eval
<plugin> --runs 1 --ablation none --case <name>`), each grading on `tool_used: Skill,
input_match: <skill>` against the actual tool-call transcript. This is the harness's own
mechanism, not a text-matching stand-in.

| Case | Prompt (abridged) | Target | Target's live status | Result |
|---|---|---|---|---|
| d1-live | "Get gonzo on this quarterly report…" | `writing-skills:gonzo` | FULL | **Skill called 1×. PASS.** |
| d2-live | "…bring it up to the bar you'd hold yourself to." | `full-stack-dev-skills:elite-python-engineer` | NAMEONLY | Skill called 0×. |
| a1-live | "Review this Python module… principal engineer…" | `full-stack-dev-skills:elite-python-engineer` | NAMEONLY | Skill called 0×. |
| c10-live | "Refactor this paragraph so it reads better." | must NOT be `elite-python-engineer` | NAMEONLY | Skill called 0× (guard held, but uninformative — see below). |
| d9-live | "Tear our new pricing model apart…" | `coding-agent-skills:chicken-little-executive-advisor` | **FULL** | Skill called 0×. |
| c13-live | "…dates come in three different formats. Clean this up." | must NOT be `script-wizard` | FULL | Skill called 0× (guard held). |
| c16-live | "Our refund policy has an edge case… Stress test it." | must NOT be `script-wizard` | FULL | Skill called 0× (guard held). |

**The load-bearing result is d2-live and a1-live.** Both prompts are the exact repaired-seam
prompts from the Tier D re-run, which the blind-simulation method scored as fixed (43/45,
description-level repair confirmed). Run for real, against a session where
`elite-python-engineer`'s description is currently invisible, **both fail with zero Skill calls
— not a wrong pick, an absent one.** This directly confirms, with the real mechanism, the thing
the whole simulation-based trigger-test protocol could never test: **a routing fix verified by
simulation is conditional on the description being visible at all, and in a realistic full
install, it frequently is not.** Every "PASS" this protocol has recorded to date was measured
against a full, undegraded listing — an upper bound the live deployment does not reliably meet.

**d9-live is a second, weaker finding, reported at its true confidence.** Its target
(`chicken-little-executive-advisor`) *is* FULL in this session, yet the live agent still did not
invoke `Skill` for a prompt the repaired description should match ("business model...process...
attacked whole"). This is one data point (n=1) and is not treated as a confirmed pattern — it
may be prompt-specific (the agent judged it could just answer the critique directly without a
formal tool call, since nothing about the task *requires* the tool to satisfy the user) rather
than a routing failure in the same sense as the invisible-description cases. Recorded as an open
question, not a conclusion: **does the real agent under-invoke `Skill` even for visible,
matching descriptions, separately from the listing-truncation risk?** This needs more than one
live sample to answer and was not pursued further here on cost grounds.

**c10/c13/c16 "PASS" results are real but weaker than they look.** In two of the three
(`c13`/`c16`), the grader itself was authored with a bug (`max: 0` alone, without an explicit
`min: 0`, silently produced an impossible `1..0` expected range) — the printed score was FAIL
regardless of actual behavior, but the raw "Skill called 0×" trace is the real signal and shows
the guard held. `c10` targeted an already-invisible skill, so its "0 calls" proves nothing new.
Recorded so the grader bug is not repeated: **`tool_used` graders asserting absence need `min: 0`
stated explicitly.**

## 5. Item 3 — checked, not extended

Before writing more Tier C guards on the pattern that caught `script-wizard`, the library was
searched for a second skill carrying the same defect signature: an explicit, unqualified
breadth claim in the description ("any work of real substance," "even when phrased casually," or
equivalent). Only `script-wizard` carries it. The next-broadest candidate,
`coding-agent-skills:sparring-partner` ("any work product"), was checked against the same
standard that flagged `script-wizard` and found meaningfully different: it carries **one**
description-level boundary clause repaired this session (against
`chicken-little-executive-advisor`), and no narrower same-purpose sibling exists in this library
for generic single-artifact critique — unlike `script-wizard`, whose breadth competed directly
with specific-purpose siblings that own more precise vocabulary (`data-cleaning`,
`git-and-code-review`, `rule-stress-testing`, `value-stream-mapping`).

**Conclusion: no second skill warrants a new guard row** — but see the correction below before
relying on that.

> **Corrected 2026-08-19.** This section originally claimed `sparring-partner` "already carries
> two reciprocal boundary clauses repaired this session (against `script-wizard` itself and
> against `chicken-little-executive-advisor`)". Checked: its description contains **zero**
> mentions of `script-wizard` and one of `chicken-little-executive-advisor`, and
> `script-wizard`'s description does not name `sparring-partner` either. The only
> `script-wizard` reference lives in `sparring-partner`'s **body** — which §1 and §4 of this
> same document establish the router never reads. This is the identical error class retracted at
> the top of this file: a body-level seam counted as a routing-level one. It recurred here in a
> different section, which is itself the finding — one correction did not sweep to its siblings.
>
> The conclusion survives on its other leg (no narrower same-purpose sibling competes for generic
> single-artifact critique, unlike `script-wizard`), but it is now standing on one leg rather than
> two. **The `script-wizard` ↔ `sparring-partner` seam is unguarded at the description level and
> has never been tested live.** Treat that as an open item, not a settled negative.

## 6. What this changes going forward

1. `README.md`, `MEMORY.md`, `docs/library-review-2026-08.md`, `docs/trigger-test.md` and
   `docs/trigger-test-results.md` cite the real mechanism — a character budget of
   `floor(context_tokens × 4 × 0.01)` filled by a **usage-ranked** greedy upgrade with no cutoff —
   and the real cost figure (harness-tokenizer-computed, ~30% above this repo's own chars/token
   estimate). *This item originally said the mechanism was a "sequential fill, not usage-based
   name-only trimming"; that was the error this document now retracts at the top.*
   `scripts/simulate-listing-budget.py` reimplements the algorithm so every number in §2 can be
   re-derived offline in one command — the answer to the fair criticism that this document's
   original evidence lived only in an uncommitted plugin cache.
2. Every PASS this protocol has ever recorded — including the freshly-repaired D2/D9 seams — is
   now understood to be conditional on full-listing visibility, which a realistic full install
   does not provide. This is the single most consequential correction from this pass: **the
   trigger-test protocol has never once tested the condition its own users will actually be
   in.**
3. A live sampling method now exists and is documented (`claude plugin eval` under
   `CLAUDE_CODE_WALNUT_SPIRE=1`) for anyone who wants to extend this beyond the seven cases run
   here. It costs real money per run; budget accordingly.
