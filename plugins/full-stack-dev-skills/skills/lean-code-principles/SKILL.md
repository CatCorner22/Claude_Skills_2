---
name: lean-code-principles
description: >-
  Applies the lean-code discipline that anchors this plugin — minimizing lines of code by
  leaning on frameworks and the standard library, YAGNI, small public surface area, deleting
  code as a feature, and judging when an abstraction pays for itself versus when it's
  speculative cost. Use when writing or reviewing application code, deciding whether to add a
  dependency/abstraction/layer, simplifying an overgrown module, or setting coding standards
  for a project. Triggers: lean code, minimize lines of code, YAGNI, over-engineering,
  simplify this code, too much boilerplate, do we need this abstraction, code review
  simplicity, delete code, small diff, keep it simple.
metadata:
  version: "1.1.0"
---

# Lean-code principles

## When to use
- Writing new application code, or reviewing code where the question is "is this more code
  than the problem needs?"
- Deciding whether to add a dependency, abstraction, service, or config option.
- Simplifying a module that has grown past understanding.
- Not for: prompt/agent design → see `coding-agent-skills:prompt-engineering` and
  `coding-agent-skills:agentic-workflow-design`. Review *process* (PRs, diffs) → see
  `coding-agent-skills:git-and-code-review`.

## Do it
1. **Solve it with what you already have, in this order:** the language's standard library →
   the framework you already depend on → a well-maintained library → your own code. Every
   hand-rolled retry loop, date parser, or auth scheme is code you now own forever; FastAPI,
   React, SQLAlchemy, and the stdlib have already written most of what an app needs. Name the
   framework-native replacement, don't gesture at one: a hand-rolled `for attempt in range(3)`
   retry with `time.sleep(2 ** attempt)` becomes `httpx.Client(transport=HTTPTransport(retries=3))`
   for connect failures, or `@retry(stop=stop_after_attempt(3), wait=wait_exponential())`
   (tenacity) when you also need to retry on a status or an exception type — both already have
   the backoff, the attempt cap, and the final-failure semantics your loop got approximately.
2. **Apply YAGNI at every decision point.** Build for the requirement in front of you, not the
   one you can imagine. No plugin systems for one implementation, no config options nobody
   asked to configure, no "for future flexibility" parameters. The future requirement, when it
   arrives, will be different from your guess — and cheaper to add then.
3. **Keep the public surface small.** Fewer exported functions, fewer parameters, fewer
   options. A module that exposes 3 functions is testable and learnable; one that exposes 30
   is a liability. Default arguments over configuration objects; one obvious way over three
   flexible ones.
4. **Earn every abstraction** against four gates, all of which must pass — the full test,
   with the thresholds and a worked three-version example, is in
   `references/earning-abstractions.md`:
   (1) **shared axis of change** — the copies have a history of being edited in the same
   commit for the same reason, or a document outside the code forces them to agree;
   (2) **name and one-sentence docstring** — if the docstring needs "or" / "depending on",
   it is more than one concept; (3) **signature projection** — add the next caller on paper,
   and if it needs a new parameter or a boolean you are building a switchboard, not an
   abstraction; (4) **read-through** — cover the body, read the call site, state the output.
   The rule of three still applies but is not sufficient on its own: extract on the third
   occurrence **and** gate 1. A wrong abstraction is worse than duplication, because
   duplication is a visible local cost and a wrong abstraction is an invisible global one
   that every future change fights. Inline trivial helpers; a one-line function called once
   is negative value:

```python
# before — an exported name, a docstring, a test, and an indirection, for one call site
def _normalize_email(value: str) -> str:
    """Lowercase and strip an email address."""
    return value.strip().lower()

def register(payload: SignupIn) -> User:
    return users.create(email=_normalize_email(payload.email))

# after
def register(payload: SignupIn) -> User:
    return users.create(email=payload.email.strip().lower())
```

   −4 lines in the module, −3 in the test file that only asserted `str.strip().lower()`:
   −7 net, −1 exported name. Report the accounting that way in review; "simplified" without a
   number is an opinion.
5. **Make deletion a first-class activity.** Dead code, commented-out blocks, unused deps,
   feature flags that shipped — delete them in their own commits (git remembers). Measure PRs
   by *net* lines: a feature that adds 200 and deletes 150 is better engineering than one that
   only adds 80.
6. **Write the obvious version first.** The straightforward loop, the plain function, the
   boring query. Optimize or generalize only when a measurement or a real second use case
   demands it. Cleverness is a cost: the reader (often future-you or an AI agent) pays it on
   every read.
7. **Before you call it lean, check the irreversible list.** YAGNI is an argument about
   option value, so it holds only where deferring keeps the option open. One question
   decides it: *if we skip this and turn out to be wrong, is the fix a code change — or a
   data repair, a security disclosure, or a customer-visible incident?* A code change means
   skip it; anything else means the cost of deferral grows with every hour of traffic and
   building it now is not over-engineering. Trust-boundary validation, idempotency wherever
   a retry exists, timeouts on every network call, schema choices that would need a
   backfill, identifier and wire-format shape, and a request-scoped correlation id are on
   that list. The full table, and the tells that "lean" has become an excuse for
   under-engineering, are in `references/earning-abstractions.md`.
8. **Review against the checklist** in `references/lean-review-checklist.md` — it's the
   codified version of steps 1–7 for PR review, with the "signs of over-engineering" table
   and the eight-part contract for what a finished lean review actually contains.

## Why / learn
Every line of code is a liability with a maintenance coupon attached: it must be read,
tested, secured, upgraded, and understood by every future reader. "Minimize lines of code"
isn't code golf — cryptic one-liners *increase* the real cost — it's minimizing the amount of
*owned* behavior by delegating to platforms that amortize their maintenance across thousands
of users. That's why the resolution order in step 1 matters: stdlib and framework code is
effectively free (someone else patches it), while your code is expensive (you patch it).
YAGNI works because of an asymmetry: adding a capability later costs roughly the same as
adding it now, but carrying an unused capability costs continuously — and speculative designs
are usually wrong anyway, so you pay twice: once to carry it, once to fight it. Notice the
condition that asymmetry rests on — *later costs about the same as now* — because that is
exactly what step 7 is checking. Where deferring converts a future code change into a data
repair or a disclosure, the asymmetry inverts and YAGNI is the wrong tool, which is why
"lean" and "under-engineered" are distinguishable at all. The
abstraction rule is the same economics: duplication is a visible, local cost, while a wrong
abstraction is an invisible, global one. And small surface area is what makes all of it
compound — code that exposes little can change much, which is the property that keeps a
codebase fast to work in after year one. Lean code is also the best practice for AI-assisted
development specifically: smaller, more boring codebases fit in context windows, generate
fewer hallucinated APIs, and make agent-written diffs reviewable.

## Common mistakes
- Code golf mistaken for lean code → fewer *owned concepts*, not fewer characters; clarity wins.
- Hand-rolling what the framework provides → auth, validation, serialization, retries: use the platform.
- Abstracting on the second occurrence "while I'm here" → wait for the third, and for proof they change together.
- Config options as politeness → every option doubles the test matrix; add them when someone actually needs them.
- Keeping dead code "just in case" → git is the just-in-case; delete it.
- Measuring productivity in lines added → net negative diffs that ship the feature are the win.
- Clever comprehensions/metaprogramming to save lines → you saved lines and spent readability; the reader pays more.
- Skipping the boring version to build the general one → the general one is speculation; ship the boring one and learn.
- Treating a negative net diff as a *target* → Goodhart: deleting the retry that was absorbing a real flake is a negative diff and a worse system. Net lines is a diagnostic you read, never a score you optimize.
- YAGNI applied to things whose later fix is a data repair (idempotency, edge validation, timeouts) → that isn't lean, it's deferred incident cost; see step 7.

## Tailor to your environment
Record your project's lean conventions in `references/your-environment.md`: your resolution
order (which frameworks/libs are "already paid for" here), the abstraction threshold your
team uses, banned patterns, and where you deliberately deviate (and why).

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/lean-code-principles.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/earning-abstractions.md — the four gates with thresholds, a worked example carried
  through three versions with line counts, when duplication beats DRY, when an indirection is
  warranted before the third occurrence, and the under-engineering failure envelope
- references/lean-review-checklist.md — the PR review checklist, over-engineering signs table,
  and the deliverable contract for a finished lean review
- references/your-environment.md — your conventions, approved deps, deviations (fill in)
