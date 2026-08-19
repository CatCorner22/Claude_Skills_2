# Load Manifest method — template, prompts, factors, loaded-test patterns

Contents: §1 The Load Manifest template · §2 Payload-inventory prompts by system type ·
§3 Choosing safety factors and dating their exhaustion · §4 Loaded-test patterns ·
§5 Worked examples · §6 The legend, held honestly

## §1 The Load Manifest template (one page, signed)

A filled-in **fictional example** — the dates and rates are computed from the rows' own
numbers so the arithmetic is reproducible; sign yours with real ones.

```
LOAD MANIFEST — <system>            Owner: <name>   Signed: <date>
Re-review triggers: <payload changes that force a re-review>

LOAD           UNIT       DAY-1   PEAK              GROWTH RATE  SPECIAL LOT       SOURCE
statement lns  lines/day  38k     190k (EOQ day);   +12%/yr      1.9M backfile     12mo feed history
                                  95k/hr batch window
concurrent us. sessions   6       22 (Mon 8a)       flat         audit week: 40    IT logs
attachments    GB total   120     writes 4GB/day pk +80GB/yr     2GB single scan   PACS export

LOAD PATH [governing member: capacity]           FACTOR(min) FLOOR  EXHAUSTS   ONE-WAY DOOR?
stmt lns → parser → staging [idx rebuild:        0.31x†      1.5    STOP†     partition key: YES
  589k lines/day]
concurrent → app pool [pool: 50 sessions]        1.25x*      1.5    STOP*      no
attachments → object store [provision: 480GB]    4.0x        1.5    ~2.5 yr    bucket layout: no

* concurrent factor is the MINIMUM across governing cases: peak 50/22 = 2.3x, but
  special lot (audit week, 40) gives 50/40 = 1.25x — below the 1.5 floor. That is a
  design-time STOP: raise the pool or write the audit-week mitigation before sign-off.

† statement-line factor is likewise the MINIMUM, and this row is the reason the rule exists.
  Peak alone looks comfortable — 589k/190k = 3.1x, which would project ~6.4 yr of headroom —
  but the special lot (1.9M-line backfile) gives 589k/1.9M = 0.31x, four-fifths *below* the
  1.5 floor. No amortization window is written into the manifest, so per the factor-basis rule
  it is a single-period load and 0.31x governs. Recording 3.1x here would be the exact error
  the manifest exists to prevent: a path that passes on the load you measured every day and
  fails on the one you do once. Either write the backfile window into the manifest (and show
  the amortized arithmetic) or treat the backfile as a design-time STOP.

LOADED-TEST PLAN                                        STATUS
replay largest real file (1.9M backfile)                pass <yyyy-mm>
soak 4h at 95k lines/hr (observed EOQ batch-window      pass <yyyy-mm>
  rate — NOT the 190k/day day-average)
special lot: 2GB single attachment                      NOT RUN — accepted unknown,
                                                        retest before imaging go-live

ACCEPTED UNKNOWNS: <what the tests could not reach, stated plainly>
```

Rules: every payload row has all four numbers and a source (or n/a WITH a reason —
e.g., a storage total's "peak" is its peak write/retrieval rate); every load appears in
the path table with its governing (weakest) member's capacity in the load's own unit;
the FACTOR column records the **minimum** across governing cases; every factor has a
written FLOOR and an exhaustion date computed against that floor, or n/a with a reason;
the test plan covers design, peak, and special lot or lists the gap as an accepted
unknown.

## §2 Payload-inventory prompts by system type

- **Data system / integration**: rows per period (day-1/peak/growth), peak in the unit
  the load actually arrives in (a batch window's lines/hour, not the day-average),
  largest single file ever, retention horizon (data carried = data ever kept, not data
  per day), reprocessing bursts (the backfill IS a load), index and join fan-out.
- **App / UI**: concurrent sessions at the worst hour, records per screen at the 95th
  percentile account (not the demo account), attachment sizes, export sizes.
- **Human process**: items per person per day at peak (close week, not mid-month),
  queue depth after a holiday weekend, the biggest single case (the audit request, the
  30-invoice dispute).
- **Storage / archive**: total at horizon (the collection grows and never shrinks),
  peak write and retrieval rates, the special collection (one donor's 400-box gift).
- **Physical**: dead load (the slab, beams, and permanently attached structure itself)
  vs live load (the books, the shelving, the people, the moving cart). In a library
  stack room the live load dominates the design — model codes carry a heavy stack-room
  live-load provision for exactly this [snippet-only] — and the live load is precisely
  what the legend's designer omitted.

## §3 Choosing safety factors and dating their exhaustion

- Anchor on consequence and knowledge, the way structural codes do [snippet-only]:
  well-measured loads with cheap failure → modest factors (~1.5×); estimated loads or
  expensive/irreversible failure (one-way doors) → large factors (3×+ or a redesign).
- **Factor basis**: compute a factor for each governing case — peak; the special lot;
  and the coinciding case (peak with the lot in flight) where they can co-occur — and
  record the **minimum**. A special lot may be amortized over a window only when the
  process genuinely spreads it (write the window into the manifest); otherwise it is a
  single-period load.
- **Exhaustion date** — when the projected load reaches capacity ÷ floor. With current
  load L₀, capacity C, factor F = C/L₀, and floor F_floor:
  - compound growth at rate g: t = ln(F / F_floor) / ln(1 + g) years
    (template row 1's peak-only factor: ln(3.1/1.5)/ln(1.12) ≈ 6.4 years — the date the
    row does *not* record, because its special lot governs and puts it at a STOP);
  - linear growth of ΔL per year: t = (C/F_floor − L₀) / ΔL years — equivalently
    L₀·(F/F_floor − 1)/ΔL (template row 3: (480/1.5 − 120)/80 = 2.5 years).
  Write the floor down; an EXHAUSTS date with no floor is uninterpretable.
- A factor below its floor anywhere is not a risk-register entry; it is a **stop**
  (jidoka) — the design has a defect at design time, the cheapest hour it will ever
  have. Template row 2 shows one caught.

## §4 Loaded-test patterns

- **Replay the record**: the largest real historical file/day/lot, byte-for-byte, not a
  synthetic resembling it (synthetics flatter parsers; real files carry the truncated
  addenda and the mixed encodings). Data handling: replay in an environment cleared for
  production data, or use structure-preserving sanitization (substitute identifiers in
  place, preserving lengths, encodings, and truncations) and record the residual
  fidelity risk in ACCEPTED UNKNOWNS — real client data never leaks into shared or
  committed artifacts (house rule).
- **Soak at peak**: sustained peak rate for hours, in the unit the load actually
  arrives in — the batch window's hourly rate, not the day-average — watching the
  resources that only fail slowly (connection pools, temp space, memory creep).
- **Quarter-end simulation**: the calendar's worst hour reproduced — volume AND
  concurrency AND the humans busy elsewhere.
- **Special-lot injection**: the single biggest item, alone and mid-stream.
- **Growth rehearsal**: run at the year-N projected volume once, now — the cheapest
  time-travel available.
- Epistemics: a test that cannot reach design load may not claim the system holds it —
  it goes in ACCEPTED UNKNOWNS in plain words. Passing empty proves the shell (the
  legend's inspectors approved an unoccupied building).

## §5 Worked examples

**BAI2 feed system.** Payload rows: daily statement lines (38k day-1; 190k at
quarter-end arriving in a ~2-hour batch window ≈ 95k lines/hr — measured from 12-month
history, and the soak runs at the window rate); the 1.9M-line backfile as the special
lot (the prior system held only 18 months at lower volume, which is why the one-time
conversion is 1.9M while the go-forward retention grows toward ~140M lines over 7
years (38k/day ≈ 13.9M/yr, compounding at +12%/yr) — the staging schema's true size is
the archive, not the day). Load path: parser
→ staging table; governing member measured as the index rebuild at 589k lines/day.
Factor, per the minimum rule: peak alone gives 589k/190k = 3.1× against a 1.5 floor,
which would project ≈ 6.4 years of headroom at +12%/yr — but the special lot governs,
589k/1.9M = **0.31×**, so the row records 0.31× and a design-time STOP, not the 6.4-year
date. Resolve it before sign-off by writing an amortization window for the backfile into
the manifest (and showing that arithmetic) or by resizing the path. Partition key flagged
one-way door (changing it post-load = the retrofit). Loaded tests: backfile replay +
batch-window soak.

**Dental imaging storage.** Payload rows: images/patient/visit, patients/day at the
Monday peak, peak write rate, single-scan special lot (2 GB CBCT export), horizon total
(images are never deleted — the collection only grows). One-way door: the storage
layout and patient-ID keying. The empty-building trap here: the app demos beautifully
with 40 sample images; the design basis is year-5's terabytes and the biggest single
scan.

## §6 The legend, held honestly

The commissioning story — a university library designed without the weight of its
books, unoccupied for years until retrofit — is assumed true as given, and versions of
it are told about libraries on many campuses. Whether any single telling is exact
changes nothing here: live-load omission is a real and canonical engineering failure
class, the empty-building inspection is a real epistemic trap, and retrofit economics
are real. Like the space-pen legend next door
(`coding-agent-skills:soviet-space-graphite`), the story is the memory hook; the
discipline is the point.
