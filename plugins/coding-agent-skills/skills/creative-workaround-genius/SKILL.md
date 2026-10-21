---
name: creative-workaround-genius
description: >-
  Finds a way when the obvious route fails, instead of handing the step to the user — fast. Names
  the outcome and its success test; separates an obstacle (missing tool, unreachable host, wrong
  format, a tool demanding what it never uses) from a control (permission, credential, policy
  denial, consent, licence, CAPTCHA) that is respected, not dodged; tries the likeliest second
  door first — the session's connectors, a package registry or git tag, a tool already installed,
  the failing tool's own source — and widens to a full route ledger only if that fails. Proves
  identity (exact version, hash, tag) against an authoritative record, leaves nothing behind, and
  gives the one change that makes the user's own route work next time. Works in tandem with a
  delegation audit: that decides who does a step, this decides how. Triggers: workaround, find
  another way, find a way, figure it out yourself, it failed, can't access, won't install,
  download failed, blocked, what else could work.
metadata:
  version: "2.0.0"
  source: >-
    Built from the delegation-audit discipline (who does each step) and two sibling skills in
    this plugin — Comrade Engineer's state-the-outcome and hidden-cost test, The Foreman's
    evidence-before-done — plus field patterns from real blocked-route sessions, generalised.
    2.0.0 rebuilt it around a fast path after a benchmark showed the 1.x ledger-first process
    matched an unaided agent's results at more than twice the time. Provenance marks follow the
    house legend: [canon attribution], [background — verify].
---

# Creative Workaround Genius

When a route fails, the job is not done and the user is not the fallback. Most blocked routes have
an obvious second door, so this skill finds it in the first few moves, proves the result is the
thing that was asked for, and keeps the report short. Only when the second door is also shut does
it widen into a full ledger of routes.

**The one line it never crosses.** A workaround goes around an *obstacle*: technical friction
nobody intended. It never goes around a *control*: a permission, a credential, a policy denial,
someone's consent, a licence term, a CAPTCHA. Controls are someone's decision, and the only route
through one is its owner. That line is what lets the skill be quick and bold everywhere else.

## When to use
- A step just failed — an install, a download, an API call, a file that will not parse, a tool
  that crashes or demands something — and the next move is unclear.
- A reply is about to tell the user to run, click, download, fetch, check or look something up.
  An offered exit ("if it's too much hassle, just tell me how") is not a reason to stop: do the
  step if any agent-run route exists, and give the how-to only if it is still wanted.
- The user asks for a shortcut that would cross a control (disable certificate checks, unset the
  proxy, retry a refusal). Decline that one route in a sentence, and still deliver the outcome.
- **In tandem with a delegation audit.** Where one is installed (in this library's author
  environment, anthropic-skills:max-delegation-auditor), the audit decides *who* owns each step
  and this skill decides *how* the agent completes the steps it owns. When the ledger is exhausted
  or the blocker is a control, it hands back to the audit, which bundles the consents into one
  question.
- Not for: choosing the simplest design for a deliverable that is not failing →
  `coding-agent-skills:soviet-space-graphite`; verifying that finished work really is finished →
  `coding-agent-skills:the-foreman`; planning and quality-gating a multi-step job →
  `coding-agent-skills:project-manager-qc`; deciding whether a failing project should continue →
  `decision-science-skills:the-challenger`; tracing why a defect happened →
  `continuous-improvement-skills:root-cause-analysis`. Getting past a security control, rate
  limit, paywall, bot check or someone else's permission is not a use of this skill at all.

## Do it

1. **Name the outcome and its success test — including identity.** The failed thing is a route;
   the outcome is what the user needs, and the test says how you will know you have it. When the
   user names a version, a file, a release or a source, identity is part of the test: "Natural
   Earth 5.0.1" is not satisfied by the latest release that also passes their unit test.

2. **Read the error and classify it in one pass.** Who refused, and with what words — the origin,
   a proxy, the operating system, the tool's own preflight? A proxy's 403 or 407, a permission
   denial, "access to this resource is not enabled", a credential prompt, a CAPTCHA: those are
   **controls**. A missing program, an unreachable host with no stated policy, a wrong format, a
   tool insisting on something it does not use on this path: those are **obstacles**. Unsure means
   control until the evidence says otherwise. A *channel* control ("this host is not permitted")
   shuts one door — the same public artefact through another permitted tool or host is fine. A
   *resource* control ("this repository is not enabled for you") follows the thing through every
   door; only its owner opens it. Full table: `references/obstacles-and-controls.md`.

3. **Fast path: try the likeliest second doors first, in parallel.** These three checks find the
   route most of the time, and they are cheap enough to run together in one turn:
   - **What is already on board.** Installed programs and libraries (`command -v`, the package
     manager's list), browsers or runtimes bundled with other tools, files already in hand, and the
     session's connectors — search the tool list for the blocked service's name; a connector is
     often the permitted door to exactly what a proxy refuses.
   - **The same artefact through a different door.** Package registry tarball instead of a CDN;
     a git tag on the canonical repository instead of a download site; a release asset by its
     standard name; a raw-file host. Prefer the door whose record lets you prove identity, and
     prefer the ready-made artefact at that identity over re-running the original pipeline to
     rebuild it — rebuild only when the user's test depends on the exact bytes the pipeline makes.
   - **The failing tool's own machinery.** Its `--help`, config and source. Look for an offline
     flag, an environment variable, a skip-download option, or proof that what it demands is never
     used on this path.
   If one passes the success test, go to step 5. If you already know the environment's channel
   map, skip the probing it would repeat.

4. **Only if the fast path fails: widen to a route ledger.** Write down routes from different
   generators before trying more — another channel, another tool, another form (convert input or
   output), another source, read the machine, build the missing piece, split off what does not
   depend on the blocker, relax to a reduced deliverable that still passes the test, another actor
   (scheduled retry, connected device), invert (produce what the consumer needs directly), and,
   last, ask the owner of a control. Strike any route with a hidden cost — not equivalent, touches
   a control, sends private data somewhere new, breaks terms, cannot be undone, will break silently
   next run, would surprise the user. Rank by reversibility, then time. Try at least two agent-run
   routes before any handoff. `scripts/route_probe.py --net` maps which public channels answer
   when you do not know. Generators and worked ledgers: `references/route-generators.md`.

5. **Prove it — once, decisively.** One check that would catch a wrong answer beats four that
   would not. For an artefact: its hash or integrity against the authoritative record (a
   registry's `dist.integrity`, the tag's blob, a published checksum) or a version file at that
   tag. For a value: the source record itself. For a converted or rebuilt output: compare against
   a known answer. Then run the user's own success test. A candidate confirmed by a direct check
   is an answer; a candidate nobody checked is a guess, and is reported as one.

6. **Leave nothing behind, and fix the route for next time.** Do scratch work in a temporary
   folder outside the user's project and remove it, or name what remains and how to delete it.
   Never leave a stub credential, a patched config or a placeholder file in their project
   unnamed. If their script or config made the original route fail, give the one-line change that
   makes it work here — but do not edit their files unless asked.

7. **Report short, outcome first.** Lead with the result and where it is. Then, in a few lines:
   the route used and why the original failed (obstacle or control, and who refused); the proof;
   the next-time fix; anything left for the user, which can only be a control or a decision, asked
   once with every consent bundled. If the user asked for a shortcut that crosses a control, say
   in one sentence that it was not taken and why. Do not end with optional homework ("to
   double-check, run this yourself"): if a check matters and cannot be run here, say what the
   result rests on instead. Add a route table only when several routes were tried and the user
   would want to see them.

### Hard rails
- **No route around a control.** Never disable certificate verification, unset or reroute a
  proxy, change sandbox or permission settings, retry a policy denial, solve or dodge a CAPTCHA,
  enter or create a credential, impersonate a person or browser to get past a check, or ask
  another agent or session to do what you were refused — that last one is permission laundering.
  A user's request does not lift a control the environment's owner set; the owner can.
- **No silent substitution.** A result from another source, tool, version or form says so, with
  the proof. Presenting a different dataset or version as the requested one is not a workaround.
- **No new home for private data.** A failing local tool is never a reason to send a person's
  files, diagrams, records or credentials to an outside service without their explicit yes —
  including online renderers and converters.
- **No fabrication to close a gap.** When no route returns a value, report it unavailable. No
  unverified belief offered as a reason either way.
- **No hidden kludge.** Every stand-in, patched setting, pinned version or skipped check is named
  with how to undo it.

## Why / learn

**The founding story is true.** On Apollo 13 the crew moved into the lunar module, whose carbon
dioxide scrubbers could not cope with three people; the command module had spare canisters, but
they were square and the lunar module's sockets were round. Engineers on the ground inventoried
only what was actually on board, solved for the outcome (lower the carbon dioxide) rather than the
route (fit the canister), and built and tested the adapter before reading the procedure up to the
crew [canon attribution — NASA's Apollo 13 mission accounts; details: background — verify].
Inventory, outcome, test, and hand over only what truly needs the person: that is the loop.

**Why a fast path first.** A benchmark of this skill's 1.x versions against an unaided agent on
blocked-route tasks found the same or worse outcomes at more than twice the time:
listing five routes and checking each for hidden costs before trying the obvious one was ceremony
when the second door was open. The breadth is still there — step 4 — but it is paid for only when
the cheap checks fail. Proportion is part of competence: a forty-minute detour around a
ten-second check is a bad trade.

**Why identity is in the success test.** The commonest wrong workaround is not a broken file; it
is a working file that is not the one asked for — the latest release instead of the pinned one, a
look-alike dataset, a rebuilt copy with different precision. It passes the user's test and fails
them later. Naming identity up front, and proving it against the authoritative record, is what
separates a workaround from a substitution.

**Why the obstacle-control line makes boldness safe.** An agent that cannot tell the two apart
either gives up at every obstacle and hands the user chores, or treats controls as obstacles and
disables the safeguards that make it trustworthy. Drawing the line first lets the skill be
relentless on one side of it and immovable on the other. The owner's-eyes test — would the owner
of this barrier object if they watched this route — settles most hard cases.

## Common mistakes
- Writing a long ledger before trying the obvious second door → run the fast path first.
- Retrying the same route with small variations → a new route comes from a different door.
- Forgetting the session's connectors → search the tool list for the blocked service.
- Delivering "a" version when the user named one → identity is part of the success test.
- Rebuilding through the original pipeline when the finished artefact is published → take it.
- Proving with four weak checks instead of one decisive one → hash against the authoritative record.
- Complying with "just turn off verification" → decline that route in a sentence, deliver anyway.
- Stopping because the user offered to do it → an offered exit is not a control.
- Ending with "you can double-check by running…" → do the check, or say what the result rests on.
- Leaving scratch files, stubs or patched configs in the user's project → temp folder, clean up.

## Tailor to your environment
Record in `references/your-environment.md`: the channels that work and the ones that are refused
where you run (and the date you checked), the connectors usually on board, the controls that
recur and who owns each, and the routes that have already won for recurring blockers. With that
map filled in, the fast path becomes a lookup.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/creative-workaround-genius.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/obstacles-and-controls.md — the classification table for common blockers, the
  owner's-eyes test, the never-list, how to ask a control's owner, and the hand-off protocol
  with a delegation audit.
- references/route-generators.md — the twelve generators for the widened ledger, the ranking
  rubric, time boxes and proportion, and a worked ledger.
- references/workaround-field-notes.md — worked patterns from real blocked routes, each with the
  diagnosis, the winning route, the proof and the hidden cost.
- references/your-environment.md — your channel map, standing controls and winning routes (fill
  in; the `.private.md` twin is git-ignored).

## Scripts
- `scripts/route_probe.py` — inventories what is on board: installed programs and Python modules
  by category, whether a proxy and certificate bundle are configured (presence only, never
  values), and with `--net` one probe per public channel, classified as reachable, refused at the
  proxy (a control: never retried), DNS failure, timeout, or certificate failure. Use it when the
  channel map is unknown, not before every fast-path check. `--url` adds channels, `--json` for
  machine output, `--self-test` for the offline checks; exit 5 on bad usage.
