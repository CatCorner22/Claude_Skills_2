# Load Manifest method — template, prompts, factors, loaded-test patterns

Contents: §1 The Load Manifest template · §2 Payload-inventory prompts by system type ·
§3 Choosing safety factors · §4 Loaded-test patterns · §5 Worked examples ·
§6 The legend, held honestly

## §1 The Load Manifest template (one page, signed)

```
LOAD MANIFEST — <system>            Owner: <name>   Signed: <date>
Re-review triggers: <payload changes that force a re-review>

LOAD           UNIT      DAY-1    PEAK        GROWTH→<yr>   SPECIAL LOT      SOURCE
statement lns  lines/day  38k     190k (EOQ)  +12%/yr       1.9M backfile    12mo feed history
concurrent us. sessions   6       22 (Mon 8a) flat          audit week: 40   IT logs
attachments    GB total   120     n/a         +80GB/yr      2GB single scan  PACS export

LOAD PATH & CAPACITY                         FACTOR  EXHAUSTS   ONE-WAY DOOR?
statement lns → parser → staging tbl (idx)   3.1x    2029-Q2    partition key: YES
concurrent    → app pool (50)                2.3x    n/a        no
attachments   → object store (2TB provision) 4.0x    2031       bucket layout: no

LOADED-TEST PLAN                              STATUS
replay largest real file (1.9M backfile)      pass 2026-08
soak 4h at EOQ peak (190k/day rate)           pass 2026-08
special lot: 2GB single attachment            NOT RUN — accepted unknown, retest before imaging go-live

ACCEPTED UNKNOWNS: <what the tests could not reach, stated plainly>
```

Rules: every payload row has all four numbers and a source; every load appears in the
path table; every factor has an exhaustion date or "n/a" with a reason; the test plan
covers design, peak, and special lot or lists the gap as an accepted unknown.

## §2 Payload-inventory prompts by system type

- **Data system / integration**: rows per period (day-1/peak/growth), largest single
  file ever, retention horizon (data carried = data ever kept, not data per day),
  reprocessing bursts (the backfill IS a load), index and join fan-out.
- **App / UI**: concurrent sessions at the worst hour, records per screen at the 95th
  percentile account (not the demo account), attachment sizes, export sizes.
- **Human process**: items per person per day at peak (close week, not mid-month),
  queue depth after a holiday weekend, the biggest single case (the audit request, the
  30-invoice dispute).
- **Storage / archive**: total at horizon (the collection grows and never shrinks),
  the special collection (one donor's 400-box gift), retrieval rate when someone
  actually needs it.
- **Physical**: dead load (the shelf) vs live load (the books, the people, the moving
  cart) — the legend's distinction; live load governs.

## §3 Choosing safety factors

- Anchor on consequence and knowledge, the way structural codes do [snippet-only]:
  well-measured loads with cheap failure → modest factors (~1.5×); estimated loads or
  expensive/irreversible failure (one-way doors) → large factors (3×+ or a redesign).
- The factor applies to PEAK plus special lot, not day-1 average.
- Growth eats factors: the exhaustion date is the factor divided by the growth curve —
  write it down and put the re-review ahead of it.
- A factor below 1.0 anywhere is not a risk register entry; it is a stop
  (jidoka — the design has a defect at design time, the cheapest hour it will ever
  have).

## §4 Loaded-test patterns

- **Replay the record**: the largest real historical file/day/lot, byte-for-byte, not a
  synthetic resembling it (synthetics flatter parsers; real files carry the truncated
  addenda and the mixed encodings).
- **Soak at peak**: sustained peak rate for hours, watching the resources that only
  fail slowly (connection pools, temp space, memory creep).
- **Quarter-end simulation**: the calendar's worst hour reproduced — volume AND
  concurrency AND the humans busy elsewhere.
- **Special-lot injection**: the single biggest item, alone and mid-stream.
- **Growth rehearsal**: run at the year-N projected volume once, now — the cheapest
  time-travel available.
- Epistemics: a test that cannot reach design load may not claim the system holds it —
  it goes in ACCEPTED UNKNOWNS in plain words. Passing empty proves the shell
  (the legend's inspectors approved an unoccupied building).

## §5 Worked examples

**BAI2 feed system.** Payload rows: daily statement lines (38k day-1; 190k at
quarter-end peak from 12-month history — measured, not estimated), the 1.9M-line
backfile (special lot: the one-time conversion IS a load), retention (7 years of lines
carried in the staging schema — the table's true size is the archive, not the day).
Load path: parser → staging table with indexes → recon engine passes; the weakest
member was the index rebuild at backfill volume. Factor 3× on peak; exhaustion dated;
partition key flagged one-way door (changing it post-load = the retrofit). Loaded tests:
backfile replay + quarter-end soak.

**Dental imaging storage.** Payload rows: images/patient/visit, patients/day at the
Monday peak, single-scan special lot (2 GB CBCT export), horizon total (images are
never deleted — the collection only grows). One-way door: the storage layout and
patient-ID keying. The empty-building trap here: the app demos beautifully with 40
sample images; the design basis is year-5's terabytes and the biggest single scan.

## §6 The legend, held honestly

The commissioning story — a university library designed without the weight of its
books, unoccupied for years until retrofit — is assumed true as given, and versions of
it are told about libraries on many campuses. Whether any single telling is exact
changes nothing here: dead-load-vs-live-load omission is a real and canonical
engineering failure class, the empty-building inspection is a real epistemic trap, and
retrofit economics are real. Like the space-pen legend next door
(`coding-agent-skills:soviet-space-graphite`), the story is the memory hook; the
discipline is the point.
