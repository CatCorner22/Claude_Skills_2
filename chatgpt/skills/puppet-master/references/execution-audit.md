# Portable execution audit

Resolve this skill's actual root through the host's skill reader or installed-skill
catalog first. Run the script by that root's absolute local path, independent of
the working directory:

`python /resolved/skill/root/scripts/execution_audit.py /explicit/path/metadata.json`

Use `--self-test` instead of the metadata path for offline accounting checks.
The assistant resolves both paths and runs available checks; do not hand this step
to Blake when an execution route exists.
The script uses Python 3.10+ and its standard library. It reads only that file, up to
10 MB, and prints fixed-size aggregate JSON. It does not discover ChatGPT/Claude
transcripts, inspect credentials, call services, or estimate hidden token usage.

Normalize available call metadata to this schema; omit unknown optional fields.
Unknown usage, individual token/tool counts, model, and batch IDs may also be null:

```json
{
  "schema_version": 1,
  "calls": [
    {
      "id": "unique-call-1",
      "actor": "main",
      "model": "explicit-model-name",
      "usage": {"input_tokens": 1000, "cached_input_tokens": 200, "output_tokens": 100},
      "tool_calls": 2,
      "batch_id": "batch-1",
      "scheduling": "parallel"
    }
  ],
  "observations": {"repeated_reads": 1}
}
```

Only `schema_version`, a nonempty `calls` list, and a unique nonempty `id` for each
call are required. `actor` defaults to `main`; use a distinct actor ID for each
observed worker. Include worker calls individually; parent usage must not already
include them. IDs are not echoed. Usage fields and tool counts must be exact
nonnegative signed-64-bit integers, not floats or booleans. Input tokens **include** cached input;
do not normalize a vendor's additive cache counts without converting this basis.
Output tokens include reasoning tokens when the observed source defines them that way;
never add a nested reasoning count a second time. Unknown fields are rejected.

Scheduling values are `parallel`, `independent-sequential`, `dependent-sequential`,
or `unspecified` (the default). Classify only from actual dependencies. These
caller-supplied classifications identify candidates for review; they do not prove
waste. Required read-back verification may explain repeated reads.

Optionally supply `prices` keyed by the exact call model. Each entry needs all three
nonnegative finite numeric USD rates per million tokens: `input`, `cached_input`,
and `output`, with at most 24 significant digits, 12 decimal places, and a maximum
of 1e12. No prices are built in. Verify rates and their date against the
applicable official pricing source before using them. Cost is:

`((input_tokens - cached_input_tokens) * input_rate + cached_input_tokens * cached_rate + output_tokens * output_rate) / 1,000,000`.

Missing usage yields null totals for each incomplete metric, with explicit coverage.
Missing usage or any required model price yields null full-run cost; the script
does not extrapolate a partial subtotal. Derived call, worker, and scheduling counts
cover supplied records only. Batches and tool totals are null if any call omits
the corresponding metadata. An absent repeated-read observation stays null.

No output from this utility proves savings, actual ChatGPT billing, hidden context
size, quality equivalence, or account-wide installation. Measure savings only with
matched baseline tasks, complete usage coverage, a specified cost basis, and
independent acceptance checks. Preserve failures and uncertainty in that comparison.

## Offline validation recorded October 23, 2026

On Python 3.12.14, the script's `--self-test` passed 7/7 checks and the dedicated
unit suite passed 20 tests. Temporary source copies were mutated independently;
the unchanged suite rejected all 3 variants:

| Deliberate breakage | Result |
| --- | --- |
| Add cached input instead of subtracting it for uncached cost | Caught: 3 test failures |
| Replace unknown aggregate token counts with zero | Caught: 3 test failures |
| Accept duplicate call IDs | Caught: 2 test failures |

The mutation run did not change the production script. These checks validate local
accounting and failure handling; they do not establish ChatGPT token savings.
Ruff and ty were unavailable and absent from the offline tool cache.
