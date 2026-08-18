# Flat-file quirks: symptom → cause → fix

## Contents
- Reading the raw bytes (the 60-second pre-parse)
- Encoding
- Delimiters and quoting
- Numbers (including the join-key destruction hazard)
- Dates
- Structure (headers/footers)
- Fixed-width files
- Keys and joins
- The hardened loader pattern
- Worked example: merging two systems' rosters
- Feed-validation contract template

## Reading the raw bytes (the 60-second pre-parse)

```bash
head -c 500 export.csv | xxd | head -20   # bytes (no xxd? od -An -tx1z works)
file export.csv                           # one-line encoding guess
head -5 export.csv; tail -5 export.csv    # title rows above, total rows below
awk -F',' '{print NF}' export.csv | sort | uniq -c | head   # field counts per line
```

What to look for:
- `ef bb bf` as the first three bytes → UTF-8 BOM → `encoding="utf-8-sig"`.
- Bytes ≥ `0x80` that aren't valid UTF-8 sequences → likely Windows-1252/Latin-1.
- The real delimiter: if every line has one giant field, you guessed wrong.
- `0d 0a` vs `0a` line endings (usually harmless; matters for naive splitting).
- Ragged field counts → unquoted delimiters inside text fields, or footer junk.

## Encoding
| Symptom | Cause | Fix |
|---|---|---|
| `UnicodeDecodeError` on load | File isn't UTF-8 (often Windows-1252 from Excel/ERP) | `encoding="cp1252"` (or `latin-1`); verify accented names look right after |
| `Ã©`, `â€™` in text | Latin-1/Win-1252 bytes decoded as UTF-8 (or double-encoded) | Reload with correct encoding; if double-encoded, `s.encode("cp1252").decode("utf-8")` |
| First column named `\ufeffAccount` | UTF-8 BOM | `encoding="utf-8-sig"` |
| Every row is one giant column | Wrong delimiter assumed | Inspect a raw line; set `sep=";"` / `"\|"` / `"\t"` |
| `latin-1` "works" on everything | It maps every byte to *something* — it can't fail | That silence is the trap: verify text visually; prefer declaring `cp1252` when the source is Windows |

`latin-1` deserves its own warning: because it accepts any byte, it converts an encoding
error you would have seen into mojibake you won't. Use it as a diagnosis tool, not a fix.

## Delimiters and quoting
| Symptom | Cause | Fix |
|---|---|---|
| Columns shift on some rows | Unquoted delimiter inside a text field (e.g. "Smith, John") | Correct quoting at the source; short-term: `engine="python"` + repair rows, or re-export pipe-delimited |
| Stray quotes break parsing | Escaped quotes in a nonstandard style | `quotechar`, `escapechar`, or `csv.QUOTE_NONE` and clean after |
| Line breaks inside fields split rows | Multiline text without proper quoting | Ensure export quotes fields; pandas handles quoted newlines |
| Semicolon-delimited "CSV" | European locale exports (comma is the decimal mark) | `sep=";"` — and expect `decimal=","` in the same file |

RFC 4180 is the closest thing CSV has to a spec: comma-separated, CRLF line endings, fields
containing commas/quotes/newlines wrapped in double quotes, embedded quotes doubled (`""`).
Real exporters deviate from it constantly — which is exactly why the parse must be declared
and validated rather than assumed. When you control the export, RFC 4180-style quoting is
the ask that fixes shifted columns at the source.

## Numbers (including the join-key destruction hazard)
| Symptom | Cause | Fix |
|---|---|---|
| `1,234.56` becomes NaN or string | Thousands separator | `thousands=","` |
| Amounts 1000x too big/small | European `1.234,56` read as US | `decimal=","`, `thousands="."` |
| `(1,234.56)` not negative | Accounting negatives in parens | Post-process: strip parens → negative, or converter function |
| `1.23E+11` in an ID column | Numeric inference on long IDs | `dtype="string"` at read time (too late after) |
| `00123` becomes `123` | Numeric inference drops leading zeros | `dtype="string"` for all identifiers |
| `0006789599` becomes `6789599` — or `6789599.0` once the column also has a null | Numeric inference on an ID: int64 when clean, float64 the moment a null appears (a resave through Excel/pandas does this too) | IDs as strings end to end; never round-trip a key column through numeric types |

The last two rows are one hazard class, and it is the nastiest in this file because it
corrupts *identity* rather than values: every join against the original keys goes quiet, no
error is raised, and the loss surfaces weeks later as "rows that should match, don't." Once
an ID has been coerced, the damage is not reliably reversible (you can zero-pad, but you're
guessing the width). Prevention is the only fix: declare identifier dtypes at the first read.

## Dates
| Symptom | Cause | Fix |
|---|---|---|
| 03/04 ambiguous | US vs day-first convention | Know the source; set `dayfirst` or explicit `format=` |
| Some rows parse, some don't | Mixed formats in one column (two upstream systems) | Parse each format explicitly; `errors="coerce"` then *count and inspect* NaT rows |
| Dates like `45123` | Excel serial dates | `pd.to_datetime(n, unit="D", origin="1899-12-30")` |
| Timezone chaos on timestamps | Mixed local/UTC | Normalize to UTC on ingest; record source tz in the feed doc |

## Structure (headers/footers)
| Symptom | Cause | Fix |
|---|---|---|
| Column names are `Unnamed: 0...` | Title rows above the header | `skiprows=N` or `header=N` |
| Sum is exactly double | Embedded "Total" row(s) | `skipfooter`, or filter rows where the key column is null/"Total" |
| Report re-prints headers every page | Paginated report export, not a data export | Filter repeated header rows; better, get a raw data export |

## Fixed-width files

No delimiter at all — columns are positional. Get the layout from the file spec (never guess
from one sample; a wide value in row 5,000 breaks eyeballed positions):

```python
df = pd.read_fwf("positions.txt",
                 colspecs=[(0, 10), (10, 40), (40, 52), (52, 60)],
                 names=["item_id", "description", "amount", "date"],
                 dtype={"item_id": "string"})
```

Watch for: space-padded IDs (`.str.strip()` after read, then re-check uniqueness), implied
decimal points ("120050" meaning 1200.50 — the spec will say), and sign columns stored
separately from the amount.

## Keys and joins
- Normalize before joining: `df[k] = df[k].str.strip().str.upper().str.zfill(width)` as applicable.
- First join is always `how="outer", indicator=True`; review `_merge` value counts; only then
  choose the join the analysis needs, and document how many rows each side lost and why.
- Duplicated keys multiply rows in a merge — check `df[k].is_unique` on the "one" side first.

## The hardened loader pattern

For any recurring feed, promote the parse into a function that proves itself on every run:

```python
def load_feed(path, expected_cols, min_rows, control_total=None):
    df = pd.read_csv(path, encoding="utf-8-sig", sep=",",
                     dtype={"item_id": "string"}, parse_dates=["date"],
                     na_values=["", "NULL", "N/A"])
    assert list(df.columns) == expected_cols, f"layout changed: {list(df.columns)}"
    assert len(df) >= min_rows, f"suspiciously few rows: {len(df)}"
    assert df["item_id"].notna().all(), "null keys in feed"
    if control_total is not None:
        assert abs(df["amount"].sum() - control_total) < 0.005, "control total mismatch"
    print(f"{path}: {len(df)} rows, total {df['amount'].sum():,.2f}")
    return df
```

The assertions are the feature: when the vendor changes the layout, the load fails at the
door with a named reason instead of poisoning everything downstream.

## Worked example: merging two systems' rosters

Domain-neutral by design — the same shape appears as an analyst reconciling two exports, an
attorney combining two matter lists, an ops manager merging vendor rosters, or a developer
joining a user dump to a license file. Two systems export "the same" people list:

- `hr_export.csv` — UTF-8 with BOM, comma-delimited, `emp_id` zero-padded to 6 (`004217`).
- `badge_export.csv` — Windows-1252, semicolon-delimited, `EMPLOYEE` as a bare number (`4217`).

```python
import pandas as pd

hr = pd.read_csv("hr_export.csv", encoding="utf-8-sig", sep=",",
                 dtype={"emp_id": "string"})
badge = pd.read_csv("badge_export.csv", encoding="cp1252", sep=";",
                    dtype={"EMPLOYEE": "string"})

# Normalize the keys to one convention (zero-pad to the documented width):
badge["emp_id"] = badge["EMPLOYEE"].str.strip().str.zfill(6)

# Prove uniqueness on both sides before merging:
assert hr["emp_id"].is_unique and badge["emp_id"].is_unique

# Audit join first — outer with indicator, and READ the counts:
m = hr.merge(badge, on="emp_id", how="outer", indicator=True)
print(m["_merge"].value_counts())
# both          1482   ← matched
# left_only       21   ← in HR, no badge (new hires? terminations lagging?)
# right_only       3   ← badges with no HR record (contractors? stale badges?)
```

The 24 unmatched rows are the *deliverable* of the merge audit — each one is a question for
the system owners, not noise to drop. Only after they're explained do you choose the final
join type and record why. Note what made this work: bytes inspected first (BOM, cp1252,
semicolons), IDs read as strings on both sides (read numerically, both sides collapse to
`4217` and the documented 6-wide convention is gone; a string/numeric mix then refuses to
merge at all), keys normalized to one convention, uniqueness proven, and the
outer-join audit read before any rows were discarded.

## Feed-validation contract template

Record one of these per recurring feed (in `your-environment.md`):

- **Feed name / source system:** …
- **Encoding / delimiter / quoting:** …
- **Schema:** columns in order, types, which are identifiers (string!)
- **Expected row-count band:** e.g. 900–1,400 per daily file
- **Control figure:** which total, from where, matched to what tolerance
- **Known quirks:** footer total row, European decimals, mixed date formats, …
- **Failure behavior:** loader raises with a named reason; who gets told
