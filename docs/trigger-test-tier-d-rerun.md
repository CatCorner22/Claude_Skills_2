# Tier D re-run — persona-named skills (2026-08-18)

**Method:** blind-router simulation. Five fresh agents each saw only the 121 `name` +
`description` pairs and nine opaque-id prompts. The answer key was withheld *structurally* — held
in a separate file the scoring agents never had — not by instruction. 15 rows × 3 columns = 45
prompts. Trigger-phrase leakage verified at 0 by `scripts/check-trigger-test.py`.

**Headline:** 41/45 prompts scored as expected. All 15 by-name prompts loaded their target
(15/15). All 15 out-of-scope guards held (15/15) — **no skill in this tier is OVER**. The
in-scope column, which is the one this tier exists to exercise, went **11/15**: four
persona-named skills are reachable *only* by someone who already knows the name.

---

## Reading the four NAME-ONLY rows: two are by design, two are defects

The tier reports four skills as name-only reachable. Checking each against its own stated
When-to-use splits them cleanly, and only two are findings:

**By design — the test confirms the design, it does not fault it.**

| Skill | Its own When-to-use | Verdict |
|---|---|---|
| `coding-agent-skills:chicken-little` | "Use when the user asks for Chicken Little or Aether **by name**." | Working as written. Name-only is the whole contract. |
| `writing-skills:gonzo` | "Use when the user asks for the gonzo treatment, weird-mode commentary, or a Thompson-flavored read." | All three paths are requests for the register by name. Name-gated on purpose. |

**Defects — the description promises reach it does not have.**

| Skill | Its own When-to-use | What happened |
|---|---|---|
| `full-stack-dev-skills:elite-python-engineer` | "Use for **any** production-grade Python task — new code, code review, refactoring, architecture…" | "This module works but I would not put it in front of a paying customer. Bring it up to the bar you would hold yourself to." routed to `coding-agent-skills:script-wizard`, with elite-python-engineer only the runner-up. A description claiming *any* production Python task lost one. |
| `coding-agent-skills:chicken-little-executive-advisor` | "Use when the user says 'deploy advisor' **or asks for an adversarial strategic autopsy** of a business model, project, process, or design." | "Tear our new pricing model apart like someone who wants it to fail" routed to `coding-agent-skills:sparring-partner`, which owns the literal trigger `tear this apart`. The second, non-name path the description advertises does not work. |

Both are **seam defects, not vocabulary defects** — in each case the target was the runner-up, so the
description carries the scent and loses a race. The protocol's prescribed repair therefore applies:
a reciprocal `Not for: … → see plugin:other` line in **both** skills naming the boundary in matching
words. Never fix a WRONG by deleting the loser's trigger; that is what produced the orphaned-phrase
defect Tier C exists to catch.

## `script-wizard` is the library's general-work attractor — two methods now agree

Outside this tier's scope but converging with an independent finding. `script-wizard` absorbed two
separate prompts here on the strength of "improve any script, tool, document, or technical artifact
of real substance — even when phrased casually", including one that belonged to
`elite-python-engineer`.

The five-lens trim ranking reached the same conclusion by a different route: the reach lens placed
`script-wizard` **2nd of 121** while every other lens placed it near the bottom — the single largest
disagreement in that exercise. Its cost is not its own tokens; it is the precision it takes from
neighbours. It deserves a Tier C-style guard row, and the elite-python-engineer seam above is the
first concrete instance.

## 1. Why this re-run exists

The first execution of Tier D reported 24/24 and had not earned it.

Tier D asks three questions per skill: does the name reach it, does a user who does *not* know the
name reach it, and does it stay out of work that isn't its own. The middle column is the whole
point. In version 1, **seven of the eight middle-column prompts contained a literal trigger phrase
of their own target** — `is this ready to build on`, `simpler solution`, `will it hold at real
volumes`, `future outcomes`, `refactor`, and so on. A prompt containing the target's own trigger
string asks the router exactly the question the by-name column already asked: *is this substring in
the description?* Both columns therefore passed for the same trivial reason, and the tier reported a
clean bill of health for a property it never tested.

Worse, version 1 scored the middle column in the wrong *direction* — it treated a load as a defect,
so run as written it would have recorded correct routing as over-triggering and invited deleting
real routes.

All prompts were rewritten in natural user language with zero trigger overlap, the middle column was
re-defined as **should load**, and the tier was extended from 8 rows to 15 to cover every genuinely
name-gated skill in the library. (`machine-learning-skills:bespoke-llm-architect` is excluded by
construction: `disable-model-invocation: true` means no prompt can reach it.)

---

## 2. Verdict table

| # | Skill | By-name | In-scope | Out-of-scope | Classification |
|---|---|---|---|---|---|
| D1 | `writing-skills:gonzo` | PASS | **MISS** | PASS | **NAME-ONLY** |
| D2 | `full-stack-dev-skills:elite-python-engineer` | PASS | **WRONG** | PASS | **NAME-ONLY** |
| D3 | `coding-agent-skills:chicken-little` | PASS | **MISS** | PASS | **NAME-ONLY** |
| D4 | `coding-agent-skills:sparring-partner` | PASS | PASS | PASS | HEALTHY |
| D5 | `decision-science-skills:minority-report` | PASS | PASS | PASS | HEALTHY |
| D6 | `coding-agent-skills:the-foreman` | PASS | PASS | PASS | HEALTHY |
| D7 | `coding-agent-skills:soviet-space-graphite` | PASS | PASS | PASS | HEALTHY |
| D8 | `safety-and-reliability-skills:weight-of-the-books` | PASS | PASS | PASS | HEALTHY |
| D9 | `coding-agent-skills:chicken-little-executive-advisor` | PASS | **WRONG** | PASS | **NAME-ONLY** |
| D10 | `coding-agent-skills:chicken-little-technical-compiler` | PASS | PASS | PASS | HEALTHY |
| D11 | `coding-agent-skills:extreme-ownership` | PASS | PASS | PASS | HEALTHY |
| D12 | `coding-agent-skills:stay-hard-accountability` | PASS | PASS | PASS | HEALTHY |
| D13 | `coding-agent-skills:master-prompt-architect` | PASS | PASS | PASS | HEALTHY |
| D14 | `writing-skills:adams-plain-grade` | PASS | PASS | PASS | HEALTHY |
| D15 | `coding-agent-skills:board-review` | PASS | PASS | PASS | HEALTHY |

**11 HEALTHY · 4 NAME-ONLY · 0 OVER.**

MISS = nothing loaded. WRONG = a different, plausible skill loaded. For the purposes of *reachability*
both are the same finding — the user who does not know the name does not get the skill — so both
classify the row NAME-ONLY. They differ only in the fix (MISS → add vocabulary; WRONG → also name the
boundary against the competitor).

Two by-name prompts were deliberately adversarial, using a name the skill's **own text presents to
the user but which is absent from its trigger list**. Both passed anyway, at confidence 5:

- **D11** `Bring in The Commander on this postmortem.` — `extreme-ownership`'s triggers are `jocko`,
  `extreme ownership`, `laws of combat`; "The Commander" appears only in the opening clause
  `Acts as "The Commander"`. A careful reader still routes on it. **This is an upper bound, not a
  clearance** — see §7.
- **D14** `Run adams-plain-grade over this notice.` — hyphenated, where the trigger reads
  `adams plain grade` with spaces. The When-to-use clause `Use when the user asks for
  adams-plain-grade by name` carried it.

---

## 3. The name-only-reachable skills (headline finding)

Four skills answered to their name and did not answer to their job.

### D1 — `writing-skills:gonzo`

- **In-scope prompt:** `Write this up the way a magazine columnist would — first person, in the room, no corporate hedging.`
- **Loaded instead:** nothing (`NONE`, confidence 2). `gonzo` was named as runner-up and then
  *actively declined*.
- **Why:** the description is gated on its own proper nouns. `Use when the user asks for the gonzo
  treatment, weird-mode commentary, or a Thompson-flavored read`, plus the standing qualifier
  `on explicit request`. The reasoning recorded verbatim: "The user asked for a magazine columnist's
  first-person voice, never gonzo/Thompson." The trigger list is `gonzo, get gonzo, get weird,
  hunter s. thompson, thompson treatment, fear and loathing take, gonzo commentary, savage take,
  gonzo dispatch, ride shotgun on this` — ten entries, ten of them proper nouns or in-house
  coinages. Not one describes the *register*.
- **What a user would have to type:** the word "gonzo", "weird", or "Hunter S. Thompson". Nothing
  else in the library reaches it.
- **Vocabulary the description is missing:** `first person`, `participatory reporting`,
  `narrative voice`, `no corporate hedging`, `write this like a columnist`, `immersive/subjective
  reporting`, `voice-driven piece`. Note the tension the owner has to resolve: `on explicit request`
  is a deliberate gate, and the fix is not to remove it — it is to widen what counts as the request
  from *the skill's name* to *the effect the user is asking for*.

### D2 — `full-stack-dev-skills:elite-python-engineer`

- **In-scope prompt:** `This module works but I would not put it in front of a paying customer. Bring it up to the bar you would hold yourself to.`
- **Loaded instead:** `coding-agent-skills:script-wizard` (confidence 3), with
  `elite-python-engineer` as runner-up.
- **Why:** the description is a **toolchain manifest**, not a quality-bar promise — `uv, Ruff,
  Pyright strict / ty, Python 3.14+, Pydantic v2, FastAPI, Polars, structlog`, and triggers
  `pythagoras, write python, refactor, … pydantic, ruff, ty type checker, structlog, type hints`.
  Everything it advertises is a *named tool*. The user's prompt names none of them and — critically
  — never says the word "Python". `script-wizard`'s far broader claim (`build, write, fix, review,
  scope, or improve any script, tool, document, or technical artifact of real substance — even when
  phrased casually`) swallowed it by default.
- **What a user would have to type:** `pythagoras`, or the name of a tool in the manifest, or the
  literal word "Python" plus "production".
- **Vocabulary the description is missing:** `production-ready`, `ship-quality`, `raise the bar`,
  `not customer-ready`, `harden this`, `bring this up to standard`. The description already promises
  `Delivers complete, ready-to-ship solutions` in its *body sentence* — the phrase "ready-to-ship"
  simply never reaches the trigger list or the `Use for` clause in user-facing words.

### D3 — `coding-agent-skills:chicken-little`

- **In-scope prompt:** `Three dashboards went red this morning and everyone is in a war room. Is this actually an emergency?`
- **Loaded instead:** nothing (`NONE`, confidence 2). Runner-up was
  `safety-and-reliability-skills:detection-system-tuning` — **not** the target, so unlike D1 and D9
  this is not even a near miss. The description did not register at all.
- **Why:** `Use when the user asks for Chicken Little or Aether by name.` That is the entire
  When-to-use clause. It is a self-declared name-only skill; the test merely confirms it. The
  triggers `chicken little, aether, chicken little mode, sky is falling` are all the persona.
- **What a user would have to type:** `chicken little`, `aether`, or `sky is falling`. There is no
  other door.
- **Vocabulary the description is missing:** anything at all describing the *situation* the skill is
  for. Its "is the sky actually falling" judgement — proportionality of alarm — never appears in
  user words: `is this actually an emergency`, `how bad is this really`, `are we overreacting`,
  `calibrate the panic`, `war room`, `severity triage`. This is the row where the fix is largest,
  and also the row where the owner may legitimately decide name-only is the intent.

### D9 — `coding-agent-skills:chicken-little-executive-advisor`

- **In-scope prompt:** `Tear our new pricing model apart like someone who wants it to fail — where does the whole thing come undone?`
- **Loaded instead:** `coding-agent-skills:sparring-partner` (confidence 5), with the advisor as
  runner-up. This is a **seam defect**, not a description gap: `sparring-partner` owns the literal
  trigger `tear this apart` and claims `projects, deliverables, scripts, code, plans, writing, any
  work product`. The router was not wrong; two descriptions are competing for adversarial critique
  and neither names the boundary.
- **Why:** the advisor gates on `Use when the user says "deploy advisor"`, and its triggers —
  `deploy advisor, deploy_advisor, executive chicken little, activate executive chicken little,
  strategic autopsy, operational autopsy, red team my business, blocker protocol, stand down` — are
  in-house command words. `red team my business` is the only one written in user language, and the
  prompt did not say "red team".
- **What a user would have to type:** `deploy advisor`, `strategic autopsy`, or `red team my
  business`.
- **Vocabulary the description is missing** — and the reciprocal boundary lines: the advisor needs
  `business model`, `pricing`, `strategy critique`, `where does this fall apart`, `tear apart` in
  business framing; and both skills need a `Not for:` line — sparring-partner → *"critiquing a
  business model or pricing strategy → see `coding-agent-skills:chicken-little-executive-advisor`"*,
  advisor → *"general work-product critique of code, writing, or deliverables → see
  `coding-agent-skills:sparring-partner`"*. Per the protocol, **do not fix this by deleting
  `tear this apart` from sparring-partner** — that is exactly the orphaned-phrase defect Tier C
  records.

---

## 4. Where the runner-up was the target

Three of the four failures named the correct skill and then rejected it. That is the good news
buried in the finding: the descriptions are *close*, and the gap is a phrase or two, not a rewrite.

| Row | Column | Got | Runner-up | Reading |
|---|---|---|---|---|
| D1 | in-scope | `NONE` (conf 2) | **`writing-skills:gonzo`** | Identified and deliberately declined on the `on explicit request` gate. The scent is there; the permission is not. |
| D2 | in-scope | `script-wizard` (conf 3) | **`elite-python-engineer`** | Lost to a broader generic claim, not to absence. |
| D9 | in-scope | `sparring-partner` (conf 5) | **`chicken-little-executive-advisor`** | Lost to a verbatim trigger owned by a competitor. A seam, not a gap. |
| D13 | out-of-scope | `prompt-engineering` (conf 5) | **`master-prompt-architect`** | The guard held, but only just — the two prompt skills are adjacent enough that the target was second choice on a prompt it must not take. Watch, do not change. |

D3 is the exception: its runner-up was `detection-system-tuning`, an unrelated skill. Nothing about
`chicken-little`'s description registered on its own subject matter.

The reverse case — an out-of-scope prompt where the *target* was runner-up, i.e. a near-OVER — occurs
only at D13 above. The other 14 guards were not close.

---

## 5. Confidence analysis

**No by-name pass was weak.** All 15 by-name prompts scored **confidence 5** — including the two
adversarial ones (D11 "The Commander", D14 hyphenated `adams-plain-grade`) that use a name absent
from the trigger list. Under ideal conditions, every persona name in this tier reaches its skill
decisively. There is no "name that barely reaches" in the confidence-1-2 sense.

The weak scores are concentrated where the tier expected them:

| Confidence | Column | Rows |
|---|---|---|
| 5 | by-name | all 15 |
| 5 | in-scope (pass) | D5, D6, D8, D11, D12, D13 |
| 4 | in-scope (pass) | D4, D7, D10, D14, D15 |
| 3 | in-scope (fail) | D2 |
| 2 | in-scope (fail) | D1, D3 |

The five **confidence-4 in-scope passes** are the watch list — reachable without the name, but not
comfortably: D4 `sparring-partner` (`push back hard`), D7 `soviet-space-graphite` (six-month build a
spreadsheet could do), D10 `chicken-little-technical-compiler` (single load-bearing dependency), D14
`adams-plain-grade` (left school at fourteen), D15 `board-review` (several specialists at once).
Under listing degradation these are the next rows to fall.

Low confidence on an **out-of-scope** row is not a weakness — there, `NONE` at confidence 1-2 is the
correct and desired answer (Q011 sleep hours, Q041 last quarter's numbers, Q038 team capacity). Those
are guards working as designed.

**One cross-cutting observation, outside the tier's scope but visible in its data:**
`coding-agent-skills:script-wizard` absorbed both `Implement the design we agreed on last week.`
(D7 out-of-scope, conf 2) and `This module works but I would not put it in front of a paying
customer.` (D2 in-scope, conf 3), each time on the strength of `improve any script, tool, document,
or technical artifact of real substance — even when phrased casually`. Both were scored PASS and
WRONG respectively for Tier D purposes, and neither is a Tier D defect. But script-wizard is
functioning as the library's general-work attractor, and that is worth a Tier C-style guard row of
its own.

---

## 6. Full 45-row log

Result key: **PASS** = expected outcome. **MISS** = nothing loaded where the target should have.
**WRONG** = a different plausible skill loaded where the target should have. **OVER** = the target
loaded on a prompt it must stay out of.

| id | row | column | prompt | expected | got | conf | result |
|---|---|---|---|---|---|---:|---|
| Q028 | D1 | by-name | `Get gonzo on this quarterly report.` | `writing-skills:gonzo` | `writing-skills:gonzo` | 5 | PASS |
| Q007 | D1 | in-scope | `Write this up the way a magazine columnist would — first person, in the room, no corporate hedging.` | `writing-skills:gonzo` | `NONE` | 2 | **MISS** |
| Q004 | D1 | out-of-scope | `Proofread this quarterly report for typos and grammar.` | not `gonzo` | `NONE` | 2 | PASS |
| Q030 | D2 | by-name | `Bring in Pythagoras for this module.` | `full-stack-dev-skills:elite-python-engineer` | `full-stack-dev-skills:elite-python-engineer` | 5 | PASS |
| Q003 | D2 | in-scope | `This module works but I would not put it in front of a paying customer. Bring it up to the bar you would hold yourself to.` | `full-stack-dev-skills:elite-python-engineer` | `coding-agent-skills:script-wizard` | 3 | **WRONG** |
| Q021 | D2 | out-of-scope | `What's the difference between a list and a tuple in Python?` | not `elite-python-engineer` | `NONE` | 3 | PASS |
| Q044 | D3 | by-name | `Chicken Little, look at this integration.` | `coding-agent-skills:chicken-little` | `coding-agent-skills:chicken-little` | 5 | PASS |
| Q015 | D3 | in-scope | `Three dashboards went red this morning and everyone is in a war room. Is this actually an emergency?` | `coding-agent-skills:chicken-little` | `NONE` | 2 | **MISS** |
| Q026 | D3 | out-of-scope | `What could go wrong with this integration?` | not `chicken-little` | `continuous-improvement-skills:fmea` | 3 | PASS |
| Q008 | D4 | by-name | `Be my sparring partner on this strategy.` | `coding-agent-skills:sparring-partner` | `coding-agent-skills:sparring-partner` | 5 | PASS |
| Q014 | D4 | in-scope | `I have talked myself into this plan and I no longer trust my own judgement on it. Push back hard.` | `coding-agent-skills:sparring-partner` | `coding-agent-skills:sparring-partner` | 4 | PASS |
| Q010 | D4 | out-of-scope | `Summarize this strategy document in three bullets.` | not `sparring-partner` | `NONE` | 2 | PASS |
| Q009 | D5 | by-name | `Run precog on the next two quarters.` | `decision-science-skills:minority-report` | `decision-science-skills:minority-report` | 5 | PASS |
| Q040 | D5 | in-scope | `Give me three genuinely different ways the next two quarters could go, not a best and worst case.` | `decision-science-skills:minority-report` | `decision-science-skills:minority-report` | 5 | PASS |
| Q041 | D5 | out-of-scope | `What were last quarter's actual numbers?` | not `minority-report` | `NONE` | 1 | PASS |
| Q032 | D6 | by-name | `Deploy the Foreman on this codebase.` | `coding-agent-skills:the-foreman` | `coding-agent-skills:the-foreman` | 5 | PASS |
| Q002 | D6 | in-scope | `The team says this feature is done. I do not believe them. How do I check what is actually finished?` | `coding-agent-skills:the-foreman` | `coding-agent-skills:the-foreman` | 5 | PASS |
| Q033 | D6 | out-of-scope | `Write the release notes for this version.` | not `the-foreman` | `writing-skills:technical-documentation` | 3 | PASS |
| Q017 | D7 | by-name | `Comrade Engineer — is there a pencil for this?` | `coding-agent-skills:soviet-space-graphite` | `coding-agent-skills:soviet-space-graphite` | 5 | PASS |
| Q037 | D7 | in-scope | `We have three engineers on a six-month build for something I suspect a spreadsheet could do.` | `coding-agent-skills:soviet-space-graphite` | `coding-agent-skills:soviet-space-graphite` | 4 | PASS |
| Q001 | D7 | out-of-scope | `Implement the design we agreed on last week.` | not `soviet-space-graphite` | `coding-agent-skills:script-wizard` | 2 | PASS |
| Q045 | D8 | by-name | `Weight of the books on this schema.` | `safety-and-reliability-skills:weight-of-the-books` | `safety-and-reliability-skills:weight-of-the-books` | 5 | PASS |
| Q035 | D8 | in-scope | `It flies in staging with our seed data. What happens in March when the real volume shows up?` | `safety-and-reliability-skills:weight-of-the-books` | `safety-and-reliability-skills:weight-of-the-books` | 5 | PASS |
| Q022 | D8 | out-of-scope | `Write the migration to add this column.` | not `weight-of-the-books` | `full-stack-dev-skills:database-and-orm` | 4 | PASS |
| Q018 | D9 | by-name | `Deploy advisor on our new pricing model.` | `coding-agent-skills:chicken-little-executive-advisor` | `coding-agent-skills:chicken-little-executive-advisor` | 5 | PASS |
| Q005 | D9 | in-scope | `Tear our new pricing model apart like someone who wants it to fail — where does the whole thing come undone?` | `coding-agent-skills:chicken-little-executive-advisor` | `coding-agent-skills:sparring-partner` | 5 | **WRONG** |
| Q023 | D9 | out-of-scope | `Summarize the pricing model in a paragraph for the board deck.` | not `chicken-little-executive-advisor` | `collaboration-skills:executive-briefing` | 3 | PASS |
| Q013 | D10 | by-name | `Deploy compiler on this service.` | `coding-agent-skills:chicken-little-technical-compiler` | `coding-agent-skills:chicken-little-technical-compiler` | 5 | PASS |
| Q042 | D10 | in-scope | `Which single dependency in this service, if it went away tomorrow, takes everything down with it?` | `coding-agent-skills:chicken-little-technical-compiler` | `coding-agent-skills:chicken-little-technical-compiler` | 4 | PASS |
| Q024 | D10 | out-of-scope | `Add a health-check endpoint to this service.` | not `chicken-little-technical-compiler` | `full-stack-dev-skills:deploy-and-operate` | 5 | PASS |
| Q016 | D11 | by-name | `Bring in The Commander on this postmortem.` | `coding-agent-skills:extreme-ownership` | `coding-agent-skills:extreme-ownership` | 5 | PASS |
| Q036 | D11 | in-scope | `This writeup blames three other teams. Rewrite it so we own our part.` | `coding-agent-skills:extreme-ownership` | `coding-agent-skills:extreme-ownership` | 5 | PASS |
| Q038 | D11 | out-of-scope | `Who on the team has capacity to pick up this ticket?` | not `extreme-ownership` | `NONE` | 1 | PASS |
| Q025 | D12 | by-name | `Hold up the mirror on this project.` | `coding-agent-skills:stay-hard-accountability` | `coding-agent-skills:stay-hard-accountability` | 5 | PASS |
| Q027 | D12 | in-scope | `Status says green but I know it isn't. Tell me the real state in plain words.` | `coding-agent-skills:stay-hard-accountability` | `coding-agent-skills:stay-hard-accountability` | 5 | PASS |
| Q011 | D12 | out-of-scope | `How many hours of sleep should I be getting?` | not `stay-hard-accountability` | `NONE` | 1 | PASS |
| Q031 | D13 | by-name | `Master prompt architect: build me a system prompt.` | `coding-agent-skills:master-prompt-architect` | `coding-agent-skills:master-prompt-architect` | 5 | PASS |
| Q006 | D13 | in-scope | `I need a system prompt for a customer-facing agent, and I want the requirements pinned down before you write a line of it.` | `coding-agent-skills:master-prompt-architect` | `coding-agent-skills:master-prompt-architect` | 5 | PASS |
| Q039 | D13 | out-of-scope | `Why does my prompt sometimes return prose instead of JSON?` | not `master-prompt-architect` | `coding-agent-skills:prompt-engineering` | 5 | PASS |
| Q043 | D14 | by-name | `Run adams-plain-grade over this notice.` | `writing-skills:adams-plain-grade` | `writing-skills:adams-plain-grade` | 5 | PASS |
| Q034 | D14 | in-scope | `Rewrite this so someone who left school at fourteen can act on it without asking anyone.` | `writing-skills:adams-plain-grade` | `writing-skills:adams-plain-grade` | 4 | PASS |
| Q029 | D14 | out-of-scope | `Tighten this memo for the executive team — they have two minutes.` | not `adams-plain-grade` | `collaboration-skills:executive-briefing` | 5 | PASS |
| Q020 | D15 | by-name | `Run the board on this module.` | `coding-agent-skills:board-review` | `coding-agent-skills:board-review` | 5 | PASS |
| Q019 | D15 | in-scope | `I want several specialists looking at this from different angles at once, not one opinion.` | `coding-agent-skills:board-review` | `coding-agent-skills:board-review` | 4 | PASS |
| Q012 | D15 | out-of-scope | `Is this function's variable naming consistent with the rest of the file?` | not `board-review` | `NONE` | 2 | PASS |

**Column totals:** by-name 15/15 · in-scope 11/15 · out-of-scope 15/15 · **overall 41/45**.

---

## 7. What this still does not prove

**A simulation is an upper bound.** Five careful agents read 121 descriptions with unlimited
attention and reasoned about which one fits. The runtime router does not do that. Every result here
is the *best case*: a row that fails in simulation cannot pass at runtime, but a row that passes in
simulation may still fail there. The four NAME-ONLY findings are therefore solid, and the eleven
HEALTHY verdicts are provisional.

Specifically, this run does **not** establish:

1. **That the runtime router matches these choices.** The blind agents saw name + description, which
   is what the router sees — but they applied deliberate reasoning to it. Confidence-4 in-scope
   passes (D4, D7, D10, D14, D15) are the ones most likely to diverge.
2. **That D11 and D14's by-name results hold.** Both passed on a name that is *not in the trigger
   list*, recovered from prose elsewhere in the description (`Acts as "The Commander"`; the
   hyphenated form in the When-to-use clause). A reader parsing full prose finds those. A matcher
   working the trigger list does not. These two passes are the least transferable in the tier.
3. **Name-only listing truncation.** This is the big one. The protocol's premise is that past roughly
   100 installed skills the least-used descriptions get trimmed to name-only, silently. This library
   ships 121. Under that regime, a NAME-ONLY skill is not merely hard to find — it becomes findable
   *only* by its exact name, and the four rows above become four dead skills for anyone who has not
   memorised them. The simulation gave every agent all 121 descriptions in full and therefore
   reproduced none of it.

   **Caveat on the threshold itself.** The ~100-skill figure traces to a *single uncontrolled
   observation* recorded in `MEMORY.md`. It is a landmark, not a cliff: it has not been replicated,
   the mechanism has not been confirmed, and no one has established whether trimming is a hard cutoff,
   a gradual pressure, or a function of something other than skill count. Treat 121 > 100 as a reason
   to run the live test, not as a measurement. Both the finding and its stated stakes rest on it.
4. **Anything about a focused install.** Every row here was scored against the full 121-pair listing.
   A user with only `coding-agent-skills` installed is running a different experiment.

The live fresh-session run specified in `trigger-test.md` — one fresh session per prompt, 45 sessions
for this tier alone — remains unperformed and is the only thing that converts these findings from
"the description cannot route this" to "the router does not route this."

**No skill description was edited in producing this report.** Diagnosis only; the fixes in §3 are
recommendations for the owner.
