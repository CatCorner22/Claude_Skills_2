---
name: explanation-design
description: >-
  Designs an explanation for a named audience instead of transcribing the author's
  understanding: writes the one-sentence audience model first, chooses the entry analogy
  deliberately with its break-points marked, orders material concrete-first (worked example →
  general principle → boundary cases, never definition-first), runs the Feynman loop (distilled
  from accounts of Feynman's practice, not a protocol he wrote) to find the author's own gaps,
  strips curse-of-knowledge tells (Pinker's framing: undefined abbreviations, "simply," skipped
  steps), and verifies with teach-back. The assistant plays the smart newcomer, flags jargon and
  hand-waves, drafts analogies with breaks marked, and simulates the teach-back. Use when a
  concept must land with someone who doesn't already know it — onboarding, newcomer docs, or
  "why does nobody get this?". Triggers: explain it well, Feynman
  technique, analogy for, teach this concept, curse of knowledge, make this intuitive,
  teach-back, explain to a newcomer.
metadata:
  version: "1.1.4"
---

# Explanation design

An explanation is a designed artifact with a user, not a transcript of the author's
understanding. Two honest attributions up front, because this library treats labeled legends as
first-class: the "Feynman technique" is a study method popularized after Feynman's death,
distilled from accounts of how he worked and taught — not a protocol he wrote down — and it
earns its name because the plain-language reconstruction it prescribes matches those accounts.
The curse-of-knowledge framing used here is Steven Pinker's (*The Sense of Style*): once you
know something, you cannot easily simulate not knowing it, and that asymmetry — not carelessness
— is the main reason competent people write incomprehensible explanations.

## When to use
- Writing or rewriting anything whose job is to make someone *understand*: onboarding material,
  a concept walkthrough, the "how it works" section of docs, a briefing for a non-specialist.
- Diagnosing why an existing explanation isn't landing ("we wrote it down and they still don't
  get it").
- Generating and stress-testing candidate analogies before one ships.
- Not for: register or grade-level rewriting of text that already explains adequately → see
  `writing-skills:adams-plain-grade`. That skill changes the words; this one designs what the
  words must accomplish.
- Not for: attention-first professional structure — the point first, scannable, for a busy
  reader who already has the background → see `writing-skills:adams-smart-brevity`. Brevity
  serves a reader deciding what to act on; explanation serves a reader building understanding.
- Not for: making understood material stick over time → see
  the archived `learning-skills:spaced-retrieval-learning`. This skill gets the concept *in*; that one keeps
  it there.
- Not for: authoring Agent Skills → see `coding-agent-skills:writing-agent-skills`.

## Do it
The audience-model template, analogy worksheet with a worked example, the Feynman-loop protocol,
the curse-of-knowledge tell list with rewrites, and the teach-back script are in
`references/explanation-method.md`.

1. **Write the audience model first — one sentence.** "A <role> who already knows <X> and needs
   this in order to <do Y>." Every later choice — the analogy's source domain, which terms need
   defining, how much precision the boundary cases carry — is checked against this sentence. If
   you can't write it, you don't yet know who the explanation is for, and it will default to
   being for yourself.
2. **Choose the entry analogy deliberately.** The assistant drafts 2–3 candidates whose *source*
   domain the audience model says the reader already owns. For the chosen one, map the
   source→target correspondences explicitly, then mark where the analogy **breaks** — the places
   where reasoning from the source gives the wrong answer about the target. State the best break
   inside the explanation itself ("the index is like a book's index, *except* that it must be
   updated on every write — a book's never is"). An unmarked break is a future misconception the
   learner will confidently build on.
3. **Order concrete-first.** Worked example → general principle → boundary cases. Walk one
   specific, complete case first, with real values; state the general principle as a compression
   of what the reader just watched happen; then show where the principle bends or stops holding.
   Never definition-first: a definition is a summary for people who already understand.
4. **Run the Feynman loop.** Explain the concept in plain words as if to a smart newcomer →
   notice every place you reach for jargon or wave a hand ("...and then it just sorts itself
   out") → treat each such place as *your* gap, not the reader's → go re-learn that piece → 
   simplify again. Repeat until the plain-words version runs end to end. Label it honestly when
   you name it: a method distilled from accounts of Feynman's practice.
5. **Strip the curse-of-knowledge tells.** Sweep for: abbreviations never expanded; "simply,"
   "obviously," "just," "of course"; steps skipped because they're obvious to the author;
   abstractions with no instance attached; forward references to ideas not yet introduced. Each
   tell marks a place where the author's knowledge silently substituted for the reader's.
6. **Verify with teach-back.** The learner explains the concept back in their own words, to a
   new case if possible. Whatever returns distorted is what you explained badly — the distortion
   is data about the explanation, not a verdict on the learner. Fix the explanation at the
   distorted spot and re-verify.

**Division of labor.** The assistant plays the smart newcomer (it can genuinely not-know on
request, which the expert author cannot), flags jargon and hand-waves, generates candidate
analogies with their break-points already marked, and simulates the teach-back before any human
learner's time is spent. The human owns the audience model and the final call on which analogy
ships — they know the real audience, and they must run the Feynman loop on themselves for the
re-learning step to mean anything.

## Why / learn
**Why definition-first fails.** A definition is a compression of understanding — maximally
useful to someone who already has the understanding and needs a handle for it, nearly useless to
someone who doesn't, because there is no structure yet to hang it on. The concrete worked
example builds the structure; the principle then names what the reader has already seen; the
boundary cases fence it. Definition-first explanations feel rigorous to the author precisely
because the author already understands — which is the curse of knowledge operating on document
structure, not just word choice.

**Generation beats recognition.** Reading an explanation and nodding is recognition; it feels
like understanding and isn't reliable evidence of it. Producing the explanation — the Feynman
loop for the author, teach-back for the learner — is generation, and it fails loudly exactly
where understanding is missing. That asymmetry is why the loop treats every hand-wave as the
author's own gap: fluent jargon can paper over a hole that plain words fall straight into.

**Analogies are load-bearing in proportion to their danger.** A good analogy transfers a whole
inference engine from a domain the reader owns — that's why it accelerates understanding. But
the reader doesn't know where the engine's warranty ends, so they *will* run it past the break.
The analogy that helps most is the one whose breaks are marked; the mapping and the break-list
are one deliverable, not two.

**The curse of knowledge is a bias, not a flaw.** Pinker's point is that it is systematic: your
own mental state is your default model of the reader's, and knowing something makes un-knowing
it effortful. You don't fix a systematic bias with good intentions; you fix it with procedure —
an explicit audience model, a tell-list sweep, and an external test (teach-back) that doesn't
share the author's blind spot.

## Common mistakes
- Starting from the definition → open with a worked example; state the definition after the
  reader has watched the thing happen.
- Shipping an analogy without its breaks marked → map correspondences *and* breaks; say the
  biggest break inside the explanation itself.
- Writing for yourself because no audience was named → write the one-sentence audience model
  first and check every term against it.
- "Simply," "obviously," "just" surviving the edit → each one marks a skipped step; expand the
  step or delete the adverb.
- Treating the Feynman loop as a style rewrite → its output is a list of things the *author*
  must re-learn; if nothing needed re-learning, the loop probably wasn't run.
- Testing with recognition questions ("does that make sense?") → ask for generation: teach-back
  in the learner's own words, applied to a new case.
- Blaming the learner for a distorted teach-back → the distortion locates the defect in the
  explanation; fix that spot and re-verify.
- Stacking three analogies to be safe → each carries its own breaks and they interfere; one
  well-chosen analogy with marked breaks beats three unmarked ones.

## Tailor to your environment
Record your recurring audiences in `references/your-environment.md`: who you explain things to
repeatedly, what each audience can be assumed to know, house terms that never need defining vs.
terms that always do, analogies that have worked or backfired with your readers, and where
finished explanations live. Keep committed content structural — real names, client material, or
sensitive examples belong in `your-environment.private.md` (git-ignored), never in a committed
file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/explanation-design.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/explanation-method.md — the audience-model template, analogy design with break-point
  marking and a worked example, the Feynman-loop protocol, the curse-of-knowledge tell list with
  rewrites, and the teach-back script
- references/your-environment.md — your recurring audiences, assumable knowledge, house glossary
  lines, and analogy track record
