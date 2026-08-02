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
   React, SQLAlchemy, and the stdlib have already written most of what an app needs.
2. **Apply YAGNI at every decision point.** Build for the requirement in front of you, not the
   one you can imagine. No plugin systems for one implementation, no config options nobody
   asked to configure, no "for future flexibility" parameters. The future requirement, when it
   arrives, will be different from your guess — and cheaper to add then.
3. **Keep the public surface small.** Fewer exported functions, fewer parameters, fewer
   options. A module that exposes 3 functions is testable and learnable; one that exposes 30
   is a liability. Default arguments over configuration objects; one obvious way over three
   flexible ones.
4. **Earn every abstraction.** The rule of three: duplicate once (fine), duplicate twice
   (note it), on the third occurrence extract — *if* the copies are truly the same concept and
   changing together. A wrong abstraction is worse than duplication, because every future
   change fights it. Inline trivial helpers; a one-line function called once is negative value.
5. **Make deletion a first-class activity.** Dead code, commented-out blocks, unused deps,
   feature flags that shipped — delete them in their own commits (git remembers). Measure PRs
   by *net* lines: a feature that adds 200 and deletes 150 is better engineering than one that
   only adds 80.
6. **Write the obvious version first.** The straightforward loop, the plain function, the
   boring query. Optimize or generalize only when a measurement or a real second use case
   demands it. Cleverness is a cost: the reader (often future-you or an AI agent) pays it on
   every read.
7. **Review against the checklist** in `references/lean-review-checklist.md` — it's the
   codified version of steps 1–6 for PR review, with the "signs of over-engineering" table.

## Why / learn
Every line of code is a liability with a maintenance coupon attached: it must be read,
tested, secured, upgraded, and understood by every future reader. "Minimize lines of code"
isn't code golf — cryptic one-liners *increase* the real cost — it's minimizing the amount of
*owned* behavior by delegating to platforms that amortize their maintenance across thousands
of users. That's why the resolution order in step 1 matters: stdlib and framework code is
effectively free (someone else patches it), while your code is expensive (you patch it).
YAGNI works because of an asymmetry: adding a capability later costs roughly the same as
adding it now, but carrying an unused capability costs continuously — and speculative designs
are usually wrong anyway, so you pay twice: once to carry it, once to fight it. The
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

## Tailor to your environment
Record your project's lean conventions in `references/your-environment.md`: your resolution
order (which frameworks/libs are "already paid for" here), the abstraction threshold your
team uses, banned patterns, and where you deliberately deviate (and why).

## References
- references/lean-review-checklist.md — the PR review checklist and over-engineering signs table
- references/your-environment.md — your conventions, approved deps, deviations (fill in)
