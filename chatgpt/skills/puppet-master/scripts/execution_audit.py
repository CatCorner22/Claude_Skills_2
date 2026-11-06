#!/usr/bin/env python3
"""Audit explicitly supplied call metadata without discovering private transcripts.

Usage input counts include cached input. This is a normalized exchange format,
not a parser for every vendor's raw logs. Python 3.10+; standard library only.
"""

import argparse
import json
import sys
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path
from typing import Any

MAX_BYTES = 10_000_000
MAX_COUNT = 2**63 - 1
TOKEN_FIELDS = ("input_tokens", "cached_input_tokens", "output_tokens")
RATE_FIELDS = ("input", "cached_input", "output")


class InputError(ValueError):
    """Indicate invalid audit metadata without exposing its contents."""


def _object(value: Any, allowed: set[str]) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) - allowed:
        raise InputError("Expected an object with only documented fields.")
    return value


def _count(value: Any) -> int | None:
    if value is None:
        return None
    if type(value) is not int or not 0 <= value <= MAX_COUNT:
        raise InputError("Counts must be nonnegative signed-64-bit integers or null.")
    return value


def _label(value: Any) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > 200:
        raise InputError("Identifiers must be nonempty strings of at most 200 characters.")
    return value


def _rate(value: Any) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        raise InputError("Prices must be finite nonnegative JSON numbers.")
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise InputError("Invalid price.") from exc
    if not result.is_finite() or result < 0 or result > Decimal("1e12"):
        raise InputError("Prices must be finite, nonnegative, and at most 1e12.")
    if result.is_zero():
        return Decimal(0)
    if len(result.as_tuple().digits) > 24 or (
        result != 0 and result.as_tuple().exponent < -12
    ):
        raise InputError("Prices allow at most 24 significant digits and 12 decimal places.")
    return result


def audit(document: Any) -> dict[str, Any]:
    """Validate metadata and return fixed-size aggregates; never return call content.

    Unknown counts remain null. Cost covers all supplied calls or is unavailable;
    no extrapolation is made to hidden worker calls or platform context.
    """
    data = _object(document, {"schema_version", "calls", "prices", "observations"})
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        raise InputError("schema_version must be 1.")
    calls = data.get("calls")
    if not isinstance(calls, list) or not 1 <= len(calls) <= 100_000:
        raise InputError("Supply between 1 and 100000 calls.")
    prices: dict[str, dict[str, Decimal]] = {}
    raw_prices = data.get("prices", {})
    if not isinstance(raw_prices, dict):
        raise InputError("prices must be a model-keyed object.")
    for model, raw in raw_prices.items():
        _label(model)
        row = _object(raw, set(RATE_FIELDS))
        if set(row) != set(RATE_FIELDS):
            raise InputError("Every model price needs input, cached_input, and output rates.")
        prices[model] = {field: _rate(row[field]) for field in RATE_FIELDS}
    observations = _object(data.get("observations", {}), {"repeated_reads"})
    repeated_reads = _count(observations.get("repeated_reads"))

    seen: set[str] = set()
    workers: set[str] = set()
    batches: set[str] = set()
    usage_rows: list[dict[str, int | None]] = []
    tool_counts: list[int | None] = []
    classified = {key: 0 for key in ("independent-sequential", "dependent-sequential", "parallel")}
    worker_calls = complete_calls = any_usage_calls = priced_calls = 0
    all_batches_known = True
    cost = Decimal(0)
    for raw_call in calls:
        call = _object(raw_call, {
            "id", "actor", "model", "usage", "tool_calls", "batch_id", "scheduling"
        })
        call_id = _label(call.get("id"))
        if call_id in seen:
            raise InputError("Duplicate call IDs are not permitted.")
        seen.add(call_id)
        actor = _label(call.get("actor", "main"))
        if actor != "main":
            workers.add(actor)
            worker_calls += 1
        model = None if call.get("model") is None else _label(call["model"])
        batch_id = call.get("batch_id")
        if batch_id is None:
            all_batches_known = False
        else:
            batches.add(_label(batch_id))
        tool_counts.append(_count(call.get("tool_calls")))
        scheduling = call.get("scheduling", "unspecified")
        if scheduling not in (*classified, "unspecified"):
            raise InputError("Invalid scheduling classification.")
        if scheduling in classified:
            classified[scheduling] += 1
        raw_usage = call.get("usage")
        usage = {} if raw_usage is None else _object(raw_usage, set(TOKEN_FIELDS))
        row = {field: _count(usage.get(field)) for field in TOKEN_FIELDS}
        input_count, cached_count, output_count = (row[field] for field in TOKEN_FIELDS)
        if input_count is not None and cached_count is not None and cached_count > input_count:
            raise InputError("Cached input cannot exceed inclusive input tokens.")
        usage_rows.append(row)
        any_usage_calls += any(value is not None for value in row.values())
        if input_count is not None and cached_count is not None and output_count is not None:
            complete_calls += 1
            if model in prices:
                rate = prices[model]
                with localcontext() as context:
                    context.prec = 70
                    cost += (
                        (input_count - cached_count) * rate["input"]
                        + cached_count * rate["cached_input"]
                        + output_count * rate["output"]
                    ) / 1_000_000
                priced_calls += 1

    totals: dict[str, int | None] = {}
    for field in TOKEN_FIELDS:
        values = [row[field] for row in usage_rows]
        totals[field] = sum(value for value in values if value is not None) if all(
            value is not None for value in values
        ) else None
    input_total, output_total = totals["input_tokens"], totals["output_tokens"]
    totals["processed_tokens"] = (
        input_total + output_total if input_total is not None and output_total is not None else None
    )
    usage_status = "complete" if complete_calls == len(calls) else (
        "partial" if any_usage_calls else "unavailable"
    )
    return {
        "schema_version": 1,
        "coverage": "Supplied calls only; hidden calls, context, and omitted workers are unknown.",
        "calls": len(calls),
        "worker_calls": worker_calls,
        "observed_worker_agents": len(workers),
        "tool_calls": sum(value for value in tool_counts if value is not None) if all(
            value is not None for value in tool_counts
        ) else None,
        "batches": len(batches) if all_batches_known else None,
        "usage": {"status": usage_status, "complete_calls": complete_calls, **totals},
        "cost": {
            "status": "complete" if priced_calls == len(calls) else (
                "unavailable_usage" if complete_calls < len(calls) else "unavailable_prices"
            ),
            "usd": format(cost, "f") if priced_calls == len(calls) else None,
            "priced_calls": priced_calls,
            "basis": "Caller-supplied per-model USD rates per million tokens; no fixed prices.",
        },
        "diagnostics": {
            **classified,
            "unclassified_calls": len(calls) - sum(classified.values()),
            "reported_repeated_reads": repeated_reads,
            "interpretation": "Independent sequential calls are review candidates, "
            "not proven waste. Dependent steps stay sequential. Repeated reads may be "
            "required read-back verification.",
        },
        "savings": "Unavailable: no matched baseline or quality-equivalence assessment supplied.",
    }


def _reject_constant(_: str) -> None:
    raise InputError("Nonfinite JSON numbers are not permitted.")


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise InputError("Duplicate JSON object keys are not permitted.")
        result[key] = value
    return result


def load(path: Path) -> Any:
    """Read at most MAX_BYTES from an explicit local JSON file."""
    try:
        with path.open("rb") as handle:
            raw = handle.read(MAX_BYTES + 1)
    except OSError as exc:
        raise InputError("Cannot read the supplied file.") from exc
    if len(raw) > MAX_BYTES:
        raise InputError("Audit input exceeds the 10 MB limit.")
    try:
        return json.loads(
            raw, parse_float=Decimal, parse_constant=_reject_constant,
            object_pairs_hook=_unique_object,
        )
    except InputError:
        raise
    except (UnicodeError, ValueError, RecursionError) as exc:
        raise InputError("Cannot read valid UTF-8 JSON from the supplied file.") from exc


def self_test() -> int:
    """Exercise core accounting and failure guards without files or services."""
    record = {
        "id": "one", "model": "test-model",
        "usage": {"input_tokens": 1000, "cached_input_tokens": 200, "output_tokens": 100},
        "scheduling": "dependent-sequential",
    }
    report = audit({"schema_version": 1, "calls": [record], "prices": {
        "test-model": {"input": 10, "cached_input": 1, "output": 30},
    }})
    unknown = audit({"schema_version": 1, "calls": [{"id": "one"}]})
    checks = [
        report["cost"]["usd"] == "0.0112",
        report["usage"]["processed_tokens"] == 1100,
        unknown["usage"]["input_tokens"] is None,
        unknown["cost"]["usd"] is None,
        report["diagnostics"]["dependent-sequential"] == 1,
    ]
    for calls in ([record, record], [{"id": "one", "tool_calls": -1}]):
        try:
            audit({"schema_version": 1, "calls": calls})
        except InputError:
            checks.append(True)
        else:
            checks.append(False)
    passed = sum(checks)
    print(f"self-test: {passed}/{len(checks)} checks passed")
    return 0 if all(checks) else 1


def main(argv: list[str] | None = None) -> int:
    """Print bounded JSON aggregates; return 2 for invalid or unreadable input."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, nargs="?", help="Explicit local JSON metadata file")
    parser.add_argument("--self-test", action="store_true", help="Run offline accounting checks")
    args = parser.parse_args(argv)
    if args.self_test:
        if args.input is not None:
            parser.error("Do not combine an input file with --self-test.")
        return self_test()
    if args.input is None:
        parser.error("Supply an explicit input file or --self-test.")
    try:
        report = audit(load(args.input))
    except InputError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
