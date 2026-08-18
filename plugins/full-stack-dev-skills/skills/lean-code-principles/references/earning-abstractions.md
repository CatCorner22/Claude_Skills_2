# Earning abstractions (reference)

The decidable test for whether an extraction has paid for itself, one example carried
through three versions with the line counts, the cases where duplication is the correct
answer, and the failure envelope where "lean" turns into under-engineering.

## Contents
- The four gates
- Gate 1 in practice: the shared-edit ratio
- Worked example: three CSV exports, three ways
- When duplication is the right answer
- When an indirection is warranted before the third occurrence
- Under-engineering: the failure envelope of lean
- Symptom table: which direction you got it wrong in

## The four gates

An extraction is earned when it passes **all four**. One failure means leave the
duplication and revisit later — duplication is a cost you can see and localize, and the
line usually quoted here is right: it is far cheaper than the wrong abstraction.

**Gate 1 — shared axis of change.** The copies must have a history, or a stated
requirement, of changing *together for the same reason*. Coincidental similarity is the
weakest possible evidence and it is the evidence most extractions are built on. Measured
below.

**Gate 2 — the name and the one-sentence docstring.** Write the docstring before the code.
If it needs "or", "depending on", or "and optionally", you are describing more than one
concept and the extraction will carry a flag for each. Treat `generic`, `base`, `common`,
`util`, `helper`, `manager`, `process`, and `handle` as a signal rather than a rule: each
is a placeholder for a noun you have not found yet, and a concept you cannot name is a
concept you have not isolated.

**Gate 3 — signature projection.** Add the *next* caller on paper, before writing
anything. If it needs a new parameter, a new branch inside the body, or a boolean, you are
building a switchboard: a behaviour-selecting parameter is an `if` you moved to the call
site, so the reader now needs both files instead of one. The arithmetic is the argument —
with k booleans the function has 2^k reachable behaviours; at k = 3 that is 2^3 = 8 paths
while the test suite typically exercises only the 3 combinations the current callers use,
leaving 8 − 3 = 5 paths that compile, are reachable, and have never once run. Those five
are where the next bug lives, and nothing in review will surface them.

**Gate 4 — read-through.** Cover the body of the extracted function, read the call site
aloud, and state what it produces. If you cannot, the parameters are doing the explaining
and you have relocated complexity rather than removed it — at the cost of one jump per
read, paid by every future reader.

### The rule of three, amended
Extract on the third occurrence **and** gate 1, not on the third occurrence alone.

Why three and not two: with two copies, every difference between them is equally plausibly
"the parameter", so you are *inventing* the shape of the parameterization from one
observation. The third copy makes the varying part an intersection of two differences,
which is a much smaller and usually correct set — three is the smallest n where the
abstraction is inferred rather than guessed. Gate 1 is what stops you extracting three
things that merely rhyme.

## Gate 1 in practice: the shared-edit ratio

Ask git how often the candidate files were edited in the same commit:

```bash
A=path/to/first.py; B=path/to/second.py
both=0; total=0
for c in $(git log --format='%h' -n 100 -- "$A" "$B"); do
  total=$((total+1))
  [ "$(git show --name-only --format= "$c" -- "$A" "$B" | grep -c .)" -ge 2 ] && both=$((both+1))
done
echo "$both / $total commits touched both"
```

Read the ratio. The bands below are a reading heuristic — the reasoning for the floor is
given underneath, but the cut points are not a measured result and should be moved if your
repo's commit granularity differs:

| Shared-edit ratio | Reading | Do |
|---|---|---|
| ≥ ~1/3 | The copies live on one axis of change | Extract the part that moved together |
| ~1/10 to 1/3 | Partial overlap | Extract only the sub-block the shared commits actually touched — usually much smaller than the whole function |
| 0 over ≥ 10 commits | They have never once needed to agree | Do not extract |

Ten is the floor because below it you cannot distinguish "never changes together" from
"has not been touched yet": a file pair with three commits between them gives you three
coin flips.

**Where this test stops working, and what you see when it does.** A freshly imported
repository, a squash-merge history that collapses a month of separate edits into one
commit, or a file that was renamed (add `--follow`, and even then a split or a merge loses
the trail) all return a ratio near zero for reasons that have nothing to do with coupling.
The tell is a `total` that is implausibly small for the file's age. Fall back to the
**requirement test**: is there a document outside the code — a wire format, a regulator's
field list, an API contract, a shared vendor spec — that *forces* these to change together?
If yes, gate 1 passes on the document. If the only reason they must agree is that they
currently look alike, gate 1 fails.

## Worked example: three CSV exports, three ways

A service has three export endpoints — invoices, payments, customers — each a handler that
queries, writes CSV, and returns it. They are visibly similar. Line counts below are of the
code exactly as shown; count them yourself.

### Version A — no extraction (what exists)

```python
# app/exports/invoices.py
@router.get("/exports/invoices.csv")
def export_invoices(since: date, db: Session = Depends(get_db)):
    rows = db.query(Invoice).filter(Invoice.issued_at >= since).all()
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["id", "customer", "issued_at", "total"])
    for r in rows:
        w.writerow([r.id, r.customer.name, r.issued_at.isoformat(), f"{r.total:.2f}"])
    buf.seek(0)
    return StreamingResponse(
        buf,
        media_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="invoices.csv"'},
    )
```

14 lines (code lines; the `# path` marker above each block is not one). `payments.py` and
`customers.py` are the same 14 lines with a different model, filter, header row, and row
expression: 14 × 3 = 42 lines.

### Version B — the reflexive DRY extraction

```python
# app/exports/generic.py
def export_csv(db, model, columns, filename, date_field=None, since=None,
               money_fields=(), enum_fields=(), relation_fields=None):
    q = db.query(model)
    if date_field is not None and since is not None:
        q = q.filter(getattr(model, date_field) >= since)
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(columns)
    for r in q.all():
        out = []
        for c in columns:
            v = getattr(r, c, None)
            if relation_fields and c in relation_fields:
                v = getattr(getattr(r, relation_fields[c]), "name", None)
            if c in money_fields:
                v = f"{v:.2f}"
            elif c in enum_fields:
                v = v.value
            elif hasattr(v, "isoformat"):
                v = v.isoformat()
            out.append(v)
        w.writerow(out)
    buf.seek(0)
    return StreamingResponse(
        buf, media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )
```

27 lines, plus each handler becomes:

```python
@router.get("/exports/invoices.csv")
def export_invoices(since: date, db: Session = Depends(get_db)):
    return export_csv(
        db, Invoice,
        columns=["id", "customer", "issued_at", "total"],
        filename="invoices.csv",
        date_field="issued_at", since=since,
        money_fields={"total"},
        relation_fields={"customer": "customer"},
    )
```

10 lines each: 27 + 30 = 57 total, which is 57 − 42 = 15 lines **more** than changing
nothing. It fails gate 2 (the docstring is "export any model as CSV, depending on which
fields are money or enums or relations"), gate 3 (5 of its 9 parameters select behaviour),
and gate 4 (nobody can predict the output of `money_fields={"total"}` without reading the
dispatch). Three of those five — `money_fields`, `enum_fields`, `relation_fields` — shape
each row independently of the others, so the row loop already has 2^3 = 8 reachable
behaviours. It is the version that gets merged, because it *looks* like consolidation.

### Version C — the earned extraction

The part that is genuinely identical **and changes for one reason** is the envelope:
buffer, writer, header row, streaming response, disposition header. The row shaping is
per-endpoint and changes for per-endpoint reasons.

```python
# app/exports/csv_response.py
def csv_response(filename: str, header: Sequence[str], rows: Iterable[Sequence]) -> StreamingResponse:
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(header)
    w.writerows(rows)
    buf.seek(0)
    return StreamingResponse(
        buf,
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )
```

11 lines, and each handler becomes:

```python
@router.get("/exports/invoices.csv")
def export_invoices(since: date, db: Session = Depends(get_db)):
    rows = db.query(Invoice).filter(Invoice.issued_at >= since).all()
    return csv_response(
        "invoices.csv",
        ["id", "customer", "issued_at", "total"],
        ([r.id, r.customer.name, r.issued_at.isoformat(), f"{r.total:.2f}"] for r in rows),
    )
```

8 lines each: 11 + 24 = 35 total, or 42 − 35 = 7 lines removed — and 57 − 35 = 22 fewer
than the DRY version.

### The accounting

| Version | Lines | Params on the shared thing | Behaviour-selecting params | Call site readable unopened? |
|---|---|---|---|---|
| A — none | 42 | — | — | yes |
| B — `export_csv` | 57 | 9 | 5 | no |
| C — `csv_response` | 35 | 3 | 0 | yes |

**The 7 lines are not the point.** Run two real changes through the three versions:

*Change 1 — Excel mangles accented customer names; the CSV needs a UTF-8 BOM.* This is an
envelope change. Version A: three edits, and the third one gets forgotten until a customer
reports it. Version B: one edit, then re-verify 8 flag paths. Version C: one edit, one
place, nothing else can be affected — which is exactly what gate 1 predicted, because the
envelope is where the shared history lives.

*Change 2 — the customers export needs a computed lifetime-value column.* This is a
row-shaping change. Version C: one line inside one handler's generator expression, and the
other two exports cannot break. Version B: a new `computed=` callable parameter, so
parameters go from 9 to 10 and the row loop's independent shapers go from three to four —
2^3 = 8 reachable behaviours become 2^4 = 16, adding 16 − 8 = 8 combinations that have
never run, and every existing caller now flows through a new branch. Version A: one line
in one file.

Note what version A wins and loses. It is the best version for change 2 and the worst for
change 1, and that split *is* the gate-1 question: extract along the axis where the history
shows joint edits, leave the other axis alone.

## When duplication is the right answer

| Situation | Why sharing is worse | Do instead |
|---|---|---|
| The copies answer to **different owners** — a finance report and a marketing report | They look alike today and will diverge on someone else's schedule; the shared version makes each team's change a negotiation | Keep separate; apply a shared change twice and call it cheap |
| Across a **deployment boundary** — two independently released services | A shared package turns one bug fix into: cut a version, upgrade two services, coordinate two deploys, keep a compatibility window | Duplicate up to roughly a page of code; above that publish a versioned package *deliberately*, having priced the release cost |
| **Test arrangement** | A test is a document read top to bottom; a fixture that hides the inputs makes the failure message unreadable, and you debug the fixture instead of the code | Extract only behaviour-neutral builders with overridable defaults; never the inputs under test or the assertions. See `full-stack-dev-skills:testing-strategy` |
| **Coincidental shape** — two validators that both happen to check an email today | The first divergent requirement adds a flag, and the flag never comes out | Wait for gate 1 evidence |
| **Stability gradient** — a stable module made to depend on a volatile one | The shared helper inherits the churn of its most volatile caller; the stable caller is now re-tested and re-reviewed on someone else's schedule | Duplicate into the stable side and freeze it |
| **Generated or vendored code** | The generator owns the shape; your extraction is overwritten on the next run | Do not DRY across a generator boundary; change the template if you must |

## When an indirection is warranted before the third occurrence

These earn a factory, protocol, or interface with one visible implementation, because gate
1 is satisfied by something other than repetition:

- **Two implementations exist today, in production, selected at runtime.** Evidence: both
  are deployed. Not "we might swap vendors" — that migration is a rewrite either way, and
  the wrapper you wrote for it will fit the old vendor's model, not the new one's.
- **The seam sits on a boundary you do not own** — the clock, the filesystem, the network,
  a payment or mail provider. The second implementation is the test environment and it
  exists today. Build *one* fake at the process edge rather than an interface per class:
  a single injectable clock beats patching `datetime.now` in forty tests, and the forty
  patches are the cost you are actually avoiding.
- **Dispatch is driven by data** — a config value, a tenant, a file extension, an event
  name. A registry replaces an `if/elif` chain. Threshold: warranted once the dispatch
  appears in **two or more places**, or once adding a new type requires editing code
  outside that type's own module — both mean the chain will be edited incompletely.
- **Expensive or order-dependent construction reached from more than one entry point**
  (web process, worker, CLI, test bootstrap). The factory deduplicates a startup sequence
  that demonstrably changes together, which is gate 1 satisfied by construction.
- **A boundary someone else has already copied** — a public API, a wire format, a plugin
  point with an external implementer. The indirection is a contract, and you cannot
  unilaterally change a contract later, so the option YAGNI trades on is not open.

The counterweight: **one implementation plus a mock is still one implementation.** If the
only second implementation is a test double you wrote, delete the interface, use the
concrete class, and put the seam at the process edge instead.

## Under-engineering: the failure envelope of lean

YAGNI is an argument about *option value*. It holds exactly where deferring keeps the
option open, and it reverses where deferring closes it or converts a future code change
into a data repair. One question decides which side you are on:

> **If we skip this and turn out to be wrong, is the fix a code change — or a data repair,
> a security disclosure, or a customer-visible incident?**

A code change means YAGNI applies: skip it, add it when the requirement is real, and it
will cost about what it costs today. Anything else means the cost of deferral grows with
every hour of traffic, and building it now is not over-engineering.

Operationally: **reversible in a single migration you would be willing to run at 3 a.m. →
defer. Requires touching rows already written, or a third party already depends on it →
decide now.**

| Class | What the later fix actually is | The cheap version to build now |
|---|---|---|
| Trust-boundary validation and authorization | A disclosure, plus an audit of everything that got through since launch | One schema validated at the edge; deny by default |
| Idempotency wherever a retry exists (queue, client, LB, or a human clicking twice) | Reconciling duplicate writes already committed | An idempotency key column and a unique index, at write time |
| Timeouts and bounded reads on every network call | An outage whose only symptom is that nothing happens, at the worst possible traffic | An explicit timeout argument on the client; several widely used HTTP clients still default to no timeout at all |
| Schema decisions that would need a backfill | Migration plus backfill plus a dual-write window | Choose the wider type, or add the nullable column, now — see `full-stack-dev-skills:database-and-orm` |
| Identifier and wire-format shape | Every consumer changes when you do, on your schedule | Opaque string ids; version the payload from the first release |
| Request-scoped correlation id and structured errors | Debugging by redeploy, on production, at the worst time | One id, logged at every external call, carried in the error |
| Retention and deletion path for personal data | A legal request you cannot service | Know which tables hold it before you store it |

**The tells that "lean" has become an excuse.** Each is what the practitioner actually
observes, not a principle:

- Every test needs a live database or real network, defended as "we'll add the seam when we
  need it". You are already paying for the seam — in test runtime and in the tests nobody
  writes because they are slow.
- Boring, readable code that hides an unbounded `.all()`, a missing row lock, or a call
  with no timeout. Simple to read is not the same as simple under load.
- A 900-line module with no internal seams, defended as simple. Simplicity is measured by
  how much a reader must hold at once. The counter-test: how many lines must you read to
  answer "where does the money amount get rounded?" If the answer is more than a screen,
  the module is not simple, it is undifferentiated — and undifferentiated code is where
  people stop making changes.
- Net-negative diffs pursued as a goal. Deleting the retry that was absorbing a real flake
  is a negative diff and a worse system. Net lines is a diagnostic you read, never a target
  you optimize; the moment it becomes a target it stops measuring anything.

## Symptom table: which direction you got it wrong in

| What you observe | Direction | What was missed |
|---|---|---|
| The same bug fixed three times in three months in near-identical code | too little | Gate 1 was satisfied and ignored — the shared-edit ratio was already there |
| A change requested by one caller breaks two others that never asked for it | too much | Gate 1 failed: coincidental duplication was merged into one function |
| Review argues about which flag combination is under test | too much | Gate 3: behaviour-selecting parameters, 2^k paths, most untested |
| A new engineer opens four files to follow one request | too much | Gate 4: complexity relocated, one jump added per read |
| Every test needs a live database or the real network | under-engineered | No seam at the process edge |
| A retry double-charges a customer | under-engineered | Irreversible-cost class mistaken for a YAGNI candidate |
| A module people route around because "it's simple, but I can't find anything" | under-engineered | Undifferentiated, not simple |
