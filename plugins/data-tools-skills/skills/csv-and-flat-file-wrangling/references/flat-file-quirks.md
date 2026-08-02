# Flat-file quirks: symptom → cause → fix

## Contents
- Encoding
- Delimiters and quoting
- Numbers
- Dates
- Structure (headers/footers)
- Keys and joins

## Encoding
| Symptom | Cause | Fix |
|---|---|---|
| `UnicodeDecodeError` on load | File isn't UTF-8 (often Windows-1252 from Excel/ERP) | `encoding="cp1252"` (or `latin-1`); verify accented names look right after |
| `Ã©`, `â€™` in text | Latin-1/Win-1252 bytes decoded as UTF-8 (or double-encoded) | Reload with correct encoding; if double-encoded, `s.encode("cp1252").decode("utf-8")` |
| First column named `\ufeffAccount` | UTF-8 BOM | `encoding="utf-8-sig"` |
| Every row is one giant column | Wrong delimiter assumed | Inspect a raw line; set `sep=";"` / `"|"` / `"\t"` |

## Delimiters and quoting
| Symptom | Cause | Fix |
|---|---|---|
| Columns shift on some rows | Unquoted delimiter inside a text field (e.g. "Smith, John") | Correct quoting at the source; short-term: `engine="python"` + repair rows, or re-export pipe-delimited |
| Stray quotes break parsing | Escaped quotes in a nonstandard style | `quotechar`, `escapechar`, or `csv.QUOTE_NONE` and clean after |
| Line breaks inside fields split rows | Multiline text without proper quoting | Ensure export quotes fields; pandas handles quoted newlines |

## Numbers
| Symptom | Cause | Fix |
|---|---|---|
| `1,234.56` becomes NaN or string | Thousands separator | `thousands=","` |
| Amounts 1000x too big/small | European `1.234,56` read as US | `decimal=","`, `thousands="."` |
| `(1,234.56)` not negative | Accounting negatives in parens | Post-process: strip parens → negative, or converter function |
| `1.23E+11` in an ID column | Numeric inference on long IDs | `dtype="string"` at read time (too late after) |
| `00123` becomes `123` | Numeric inference drops leading zeros | `dtype="string"` for all identifiers |

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

## Keys and joins
- Normalize before joining: `df[k] = df[k].str.strip().str.upper().str.zfill(width)` as applicable.
- First join is always `how="outer", indicator=True`; review `_merge` value counts; only then
  choose the join the analysis needs, and document how many rows each side lost and why.
- Duplicated keys multiply rows in a merge — check `df[k].is_unique` on the "one" side first.
