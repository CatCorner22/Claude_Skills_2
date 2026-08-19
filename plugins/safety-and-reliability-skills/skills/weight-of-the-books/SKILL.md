---
name: weight-of-the-books
description: >-
  Prevents the sinking-library failure — a design that never accounted for the load it
  exists to carry — with a design-basis load review before commitment: name every payload
  (data volumes, rates, users, documents, weight), quantify each at day one, at peak, on
  the growth curve, and at the special-collections outlier (the biggest single lot ever
  swallowed), trace every load to a named component with stated capacity, apply written
  safety factors with margin-exhaustion dates, and require acceptance tests to run LOADED
  at design and peak values. Output: a
  one-page signed Load Manifest, re-reviewed on every payload change. Use when sizing or
  design-reviewing a system, feature, migration, or process against its real volumes.
  Triggers: weight of the books, sinking library, design load, load basis, load manifest,
  will it hold at real volumes, size it for production, test loaded not empty, biggest
  single lot, special-collections outlier.
metadata:
  version: "1.2.1"
  source: >-
    Commissioned by the user on the campus legend of a university library designed
    without accounting for the weight of its books, unoccupied for years until
    retrofitted. Assumed true as commissioned; the legend is told of many campuses, and
    the lesson stands either way.
---

# Weight of the Books (design-basis load review)

A library exists to hold books; a design that forgets their weight has designed the
shell and omitted the purpose. Software fails the same way: the system passes every test
empty and dies under the load it was built to carry — discovered in production, fixed at
retrofit prices. This skill makes the payload a first-class design input with a signed
artifact, before commitment.

## When to use
- Sizing or design-reviewing a system, feature, database, integration, migration, or
  human process against the volumes it will actually carry.
- Before go-live on anything whose acceptance tests ran on sample data.
- When a working system approaches a payload change: a new feed, a new clinic, a new
  collection, a growth inflection.
- Not for: imagining all the ways a plan fails → `decision-science-skills:pre-mortem`
  (this skill quantifies ONE failure class — payload omission — with an artifact);
  scoring failure modes broadly → `continuous-improvement-skills:fmea`; failure-data and
  availability/redundancy math → `safety-and-reliability-skills:reliability-engineering`
  (that skill quantifies failures and sizes redundancy; this one catches payload
  omission in the design basis); the hostile-input gauntlet (fuzzing, property tests,
  chaos) → `continuous-improvement-skills:lean-six-sigma-for-software` — it complements
  but does not include loaded testing; the loaded-test patterns live in this skill's own
  references/load-manifest-method.md §4; full adversarial architecture autopsy →
  `coding-agent-skills:chicken-little-technical-compiler` (this skill quantifies only
  the payload and its bearers).

## Do it
1. **Name the payload.** What does this thing exist to carry? Books, not floors: data
   volumes, transaction rates, concurrent users, documents, records, queue depths,
   physical weight, approval throughput. Write the payload inventory — each load with
   its unit. The test for completeness: if the system carried zero of a listed load, it
   would have no reason to exist. A purpose that isn't on the list is the sinking
   library.
2. **Quantify the design basis — four numbers per load.** (a) Day one; (b) **peak**,
   not average (quarter-end close, Monday 8 a.m., open-enrollment week); (c) the
   **growth curve** to a stated horizon; (d) the **special-collections case** — the
   largest single lot the system must ever swallow (the 2 GB "CSV," the 4,000-line
   statement file, the donor batch, the 50-visit treatment plan). Source the numbers by
   measurement, never estimate what can be weighed: count the actual books (genchi
   genbutsu), pull the real feed histories, and anchor growth on a reference class of
   comparable systems (`decision-science-skills:reference-class-forecasting`), not on
   hope.
3. **Trace every load to its bearer.** For each load, name the component that carries it
   — the table and its indexes, the queue, the API and its timeout, the human approver,
   the spreadsheet, the slab — and that component's stated capacity in the same unit.
   **An un-owned load is the defect this skill exists to catch**: if no component claims
   it, the design has omitted it. Chains count: the load lands on every component in its
   path, and the path's capacity is its weakest member.
4. **Apply explicit margin.** Safety factor = stated capacity ÷ design load, chosen
   deliberately per load with a written floor (structural engineering publishes its
   factors; pick yours and write them down — a margin that isn't written down is a
   hope). Compute the factor for each governing case — peak, the special lot, and the
   coinciding case — and record the minimum. Then date the margin: the exhaustion date
   is when projected load reaches capacity ÷ floor (formulas in
   references/load-manifest-method.md §3). "The building is full in year N" is a design
   output, and so is what happens then.
5. **Test loaded, not empty.** The acceptance plan must exercise design load, peak load,
   and the special-collections lot with realistic payload — an empty-building inspection
   proves the paint, not the purpose. Soak at sustained peak; replay the largest real
   historical file; simulate quarter-end, not a quiet Tuesday. Tests that cannot reach
   design load must say so in the manifest as an accepted unknown (the
   preserve-the-possibility-of-failure doctrine in
   `continuous-improvement-skills:project-command-center` governs what such a pass may
   claim).
6. **Run the retrofit clock.** For each sizing decision, ask: if this number is wrong,
   what does fixing it cost AFTER occupancy? Separate the one-way doors (schema keys,
   partition strategy, building columns) from the cheap-to-grow (another worker, another
   shelf) — one-way doors get the largest margins and the hardest tests, because the
   library sat unoccupied for years precisely because columns are not a patch.
7. **Sign the Load Manifest.** One page: payload inventory, the four numbers per load,
   load paths with capacities, factors and their exhaustion dates, the loaded-test plan,
   accepted unknowns, an owner, and the re-review triggers (any payload change: new
   feed, new clinic, new collection). The manifest is a living control — unreviewed
   after a payload change, it is scenery.

## Why / learn
The sinking-library failure is not a math error; it is a **category omission** — the
design conversation was about the artifact (the building, the app, the schema) and never
about the payload, because the payload felt like the obvious part. That is why the
countermeasure is a named artifact, not vigilance: a Load Manifest forces the purpose
into the design basis where omission becomes visible as an empty row. Peak-not-average
matters because systems fail at their worst hour, not their mean one; the
special-collections case matters because payloads have tails, and the tail — not the
median book — cracks the slab. Explicit safety factors are institutionalized humility:
they price in the certainty that the estimate is wrong without knowing which direction.
The loaded-test rule is the epistemics of the whole skill: an empty building passes
every inspection the same way a 100-row test file passes every assertion, so a test
that never reaches design load can only validate the shell — which is exactly what the
legend's inspectors validated. And the retrofit clock is the economics: design-time
sizing costs a meeting; occupied-building sizing costs years of an unusable asset. The
skill quantifies one narrow thing and defends it relentlessly, because this failure
class hides best in plain sight — everyone involved knew the library was for books.

## Common mistakes
- Designing to averages → peak and the special-collections lot are the design basis;
  the average never broke anything.
- Estimating what can be measured → weigh the books: pull the real feed sizes, count
  the real users, replay the real file.
- Loads with no named bearer → every load lands on a component with a stated capacity,
  or the manifest has found its defect.
- Unwritten margins → a safety factor that lives in someone's head is a hope; write
  the number and its exhaustion date.
- The empty-building test pass → green suites on sample data validate the shell;
  acceptance runs loaded or admits it couldn't.
- One-and-done manifests → the payload changes (new collection, new feed); the
  manifest re-reviews on every payload change or becomes scenery.
- Gold-plating every component in response → margins are chosen per load and priced;
  the biggest factors go to the one-way doors, not everywhere
  (`coding-agent-skills:soviet-space-graphite` keeps the pencil honest on the rest).

## Tailor to your environment
Record in `references/your-environment.md`: your standing payloads and their measured
values (feed sizes, statement-line volumes, patient counts), your chosen safety factors
per load class, the one-way doors in your current architecture, and where signed
manifests live. Real volumes from production systems stay in
`your-environment.private.md` (git-ignored) if they are sensitive.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/weight-of-the-books.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/load-manifest-method.md — the manifest template, payload-inventory
  prompts by system type, factor-selection guidance, loaded-test patterns, worked
  examples (BAI2 feed system; dental imaging storage)
- references/your-environment.md — your payloads, factors, and one-way doors (fill in)
