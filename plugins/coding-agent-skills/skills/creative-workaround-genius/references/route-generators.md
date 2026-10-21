# Route generators — twelve questions that produce genuinely different routes

A route ledger is only as good as the variety in it. Three variations on the failed command are
one idea; a different channel, a converter and a smaller deliverable are three. Each generator
below is a different question. Ask at least three of them before ranking anything, and write
down at least five candidate routes.

## Contents
- [The twelve generators](#the-twelve-generators)
- [Ranking the ledger](#ranking-the-ledger)
- [Time boxes and proportion](#time-boxes-and-proportion)
- [A worked ledger](#a-worked-ledger)

## The twelve generators

| # | Generator | The question | Typical moves | Usual hidden cost to check |
|---|---|---|---|---|
| 1 | Another channel | Is the same thing available through a different door? | package registry instead of CDN; raw file host or `git clone` instead of a restricted API; listing tags with `git ls-remote` and fetching a release asset by its standard name; a connector instead of a browser; a local cache or an earlier download | is it the *same* artefact (version, checksum)? is the channel permitted, not merely reachable? |
| 2 | Another tool | Can a different instrument do the same job? | a system program already installed (`pdftotext`, `convert`, `pandoc`, `jq`); the standard library instead of a missing package; a different reader for the same format | does it handle the edge cases the original did (encodings, tables, units)? |
| 3 | Another form | Can I convert what I have into what the available tool accepts? | write a small converter (text export to VCF, CSV to the expected layout, JSON to the schema); change the output format the consumer reads | is the conversion lossless? prove it on a known case |
| 4 | Another source | Can the same fact come from somewhere else? | a file already in hand; a printed report or PDF the person shared; a dataset that embeds the fact; the tool's own bundled data; the person's connected drive or mail | is the source as current and authoritative? cite it as what it is |
| 5 | Read the machine | Does the tool really need what it demands? | read `--help`, config files and source; find an offline flag, an environment variable, a cache path, a skip option; find what the preflight check is really checking | is the check protecting correctness? if so, it is not an obstacle |
| 6 | Build it | Is the missing piece smaller than the detour? | a parser, an adapter, a renderer, a tiny server, a test fixture | carry cost: who maintains it? add a self-test |
| 7 | Split | Which parts do not depend on the blocker? | do them now; shrink the blocker to one isolated remainder; deliver the rest | does the partial result mislead without the missing part? label it |
| 8 | Relax | Would a reduced deliverable still pass the success test? | bundle data instead of fetching live; a lower resolution; partial coverage stated plainly; an earlier pinned version | is the reduction disclosed? does it still meet the need? |
| 9 | Another actor | Is there someone or something else that can do this step? | a subagent; a scheduled task; a device the person connected; their existing automation; the person only for a control | does the actor have the same permissions? never use it to launder a refusal |
| 10 | Another time | Is the blocker transient? | schedule a retry or check-in; subscribe to the event; queue the step after a dependency lands | does the person know it is pending? |
| 11 | Invert | What does the consumer of this step actually need? | produce that directly and skip the failed step; work backward from the success test | is anything downstream relying on the skipped step's side effects? |
| 12 | Ask the owner | Is this a control or a decision? | one bundled question, with everything prepared and the after-yes plan stated | is it truly theirs, or is it just unfamiliar? |

Two cheap additions to every ledger: **the pencil** (is the blocked step needed at all? — Comrade
Engineer's first rung) and **the original route, re-diagnosed** (did the error say something you
skipped?).

## Ranking the ledger

1. Strike every route that fails the hidden-cost check (equivalence, control, privacy, terms,
   reversibility, carry cost, surprise). Write why.
2. Order the survivors by **reversibility** first — a route that can be undone cleanly is worth
   trying before a better one that cannot.
3. Then by **expected time to pass the success test**, including the proof.
4. Then by **cost** (money, compute, the person's attention).
5. Run independent routes in parallel when they do not interfere (two read-only probes, two
   downloads to different paths). Never run two routes that write to the same place at once.

## Time boxes and proportion

- Size each time box to the value of the step: minutes for a one-off convenience, longer for a
  step that blocks the whole deliverable, longest for a step that will recur.
- **Two-route minimum** before any handoff, matching the delegation audit's re-audit rule.
- **Proportion stop:** when the next route would cost more than the person's step, and the step
  is a one-off decision rather than a chore, ask — with the ledger attached. A recurring chore is
  the opposite case: a route that automates it pays for itself.
- **Exhaustion stop:** when every route is struck or failed, report the ledger and the one
  control or missing fact that would unlock the best route.

## A worked ledger

*Outcome:* a world countries topology file in `./data` that the map page renders. *Success test:*
valid JSON, a `countries` object with the expected number of features, and the page draws it.
*Failed original:* the build script's CDN download — the proxy refused the tunnel (a control on
that host).

| # | Route | Generator | Hidden-cost check | Result |
|---|---|---|---|---|
| 1 | CDN download (original) | — | — | refused at the proxy: control, not retried |
| 2 | the same package version from the npm registry, unpacked | another channel | same artefact, same version; public; permitted channel | **passed** |
| 3 | the package's source repository via `git clone`, then its build step | another channel | equivalent only if the build reproduces the published file | ready as fallback |
| 4 | Natural Earth GeoJSON from the public code host, converted to topology | another source + another form | different source, same underlying data; conversion must preserve feature count | ready as fallback |
| 5 | a copy found in an earlier project folder | another source | version unknown; checksum against route 2 before use | not needed |
| 6 | ask the network owner to allow the CDN | ask the owner | changes a control; only if every route fails | not needed |
| 7 | change the request headers so the CDN is reached anyway | — | struck: evasion of a control | not run |

*Proof:* the file from route 2 parsed, held the expected feature count, and matched the package
registry's published checksum. *Carry cost:* the build script still points at the CDN — the
report says so and offers the one-line change to the registry URL.
