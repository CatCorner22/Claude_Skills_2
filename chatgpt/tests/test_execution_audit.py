"""Behavioral checks for the portable audit's accounting and disclosure boundary."""

import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path
from typing import Any

SCRIPT = Path(__file__).parents[1] / "skills/puppet-master/scripts/execution_audit.py"
SPEC = importlib.util.spec_from_file_location("execution_audit", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


def call(call_id: str = "a", **updates: Any) -> dict[str, Any]:
    """Build one metadata record with complete observed counters."""
    return {
        "id": call_id,
        "model": "model-a",
        "usage": {"input_tokens": 1000, "cached_input_tokens": 200, "output_tokens": 100},
        "tool_calls": 1,
        "batch_id": "one",
        **updates,
    }


def document(*calls: dict[str, Any], **updates: Any) -> dict[str, Any]:
    return {"schema_version": 1, "calls": list(calls), **updates}


class AuditTests(unittest.TestCase):
    """Exercise meaningful usage, cost, invalid-input, and privacy contracts."""

    def test_unknown_usage_remains_unknown(self) -> None:
        report = AUDIT.audit(document({"id": "one"}))
        self.assertEqual(report["usage"]["status"], "unavailable")
        for field in (*AUDIT.TOKEN_FIELDS, "processed_tokens"):
            self.assertIsNone(report["usage"][field])
        self.assertIsNone(report["tool_calls"])
        self.assertIsNone(report["batches"])
        self.assertIsNone(report["diagnostics"]["reported_repeated_reads"])
        self.assertIsNone(report["cost"]["usd"])

    def test_cached_math_counts_input_once(self) -> None:
        rates = {"model-a": {"input": 10, "cached_input": 1, "output": 30}}
        report = AUDIT.audit(document(call(), prices=rates))
        self.assertEqual(report["usage"]["processed_tokens"], 1100)
        self.assertEqual(report["cost"]["usd"], "0.0112")
        self.assertEqual(report["cost"]["status"], "complete")

    def test_prices_not_inferred(self) -> None:
        report = AUDIT.audit(document(call()))
        self.assertEqual(report["cost"]["status"], "unavailable_prices")
        self.assertIsNone(report["cost"]["usd"])

    def test_mixed_models_use_separate_rates(self) -> None:
        rates = {
            "model-a": {"input": 10, "cached_input": 1, "output": 30},
            "model-b": {"input": 20, "cached_input": 2, "output": 60},
        }
        report = AUDIT.audit(document(call(), call("b", model="model-b"), prices=rates))
        self.assertEqual(report["cost"]["usd"], "0.0336")
        del rates["model-b"]
        partial = AUDIT.audit(document(call(), call("b", model="model-b"), prices=rates))
        self.assertIsNone(partial["cost"]["usd"])
        self.assertEqual(partial["cost"]["priced_calls"], 1)

    def test_worker_usage_aggregated_only_when_supplied(self) -> None:
        report = AUDIT.audit(document(call(), call("b", actor="worker-1")))
        self.assertEqual(report["usage"]["input_tokens"], 2000)
        self.assertEqual(report["worker_calls"], 1)
        self.assertEqual(report["observed_worker_agents"], 1)
        self.assertIn("omitted workers are unknown", report["coverage"])

    def test_partial_usage_never_extrapolated(self) -> None:
        report = AUDIT.audit(document(call(), call("b", usage={"input_tokens": 5})))
        self.assertEqual(report["usage"]["status"], "partial")
        self.assertEqual(report["usage"]["input_tokens"], 1005)
        self.assertIsNone(report["usage"]["output_tokens"])
        self.assertIsNone(report["usage"]["processed_tokens"])

    def test_zero_usage_is_known(self) -> None:
        report = AUDIT.audit(document(call(usage=dict.fromkeys(AUDIT.TOKEN_FIELDS, 0))))
        self.assertEqual(report["usage"]["status"], "complete")
        self.assertEqual(report["usage"]["processed_tokens"], 0)

    def test_duplicate_ids_rejected(self) -> None:
        with self.assertRaises(AUDIT.InputError):
            AUDIT.audit(document(call(), call()))

    def test_invalid_counts_rejected(self) -> None:
        for value in (-1, True, 1.5, float("inf"), "100", AUDIT.MAX_COUNT + 1):
            with self.subTest(value=value), self.assertRaises(AUDIT.InputError):
                AUDIT.audit(document(call(usage={"input_tokens": value})))

    def test_cached_count_cannot_exceed_input(self) -> None:
        with self.assertRaises(AUDIT.InputError):
            AUDIT.audit(document(call(usage={"input_tokens": 1, "cached_input_tokens": 2})))

    def test_invalid_prices_rejected(self) -> None:
        for value in (-1, True, float("nan"), float("inf"), "10"):
            with self.subTest(value=value), self.assertRaises(AUDIT.InputError):
                AUDIT.audit(document(call(), prices={"model-a": {
                    "input": value, "cached_input": 0, "output": 0
                }}))

    def test_unknown_content_fields_rejected_without_echo(self) -> None:
        with self.assertRaises(AUDIT.InputError) as caught:
            AUDIT.audit(document(call(prompt="private-content")))
        self.assertNotIn("private-content", str(caught.exception))

    def test_dependency_diagnostics_do_not_demand_parallelism(self) -> None:
        report = AUDIT.audit(document(
            call(scheduling="independent-sequential"),
            call("b", scheduling="dependent-sequential"),
            observations={"repeated_reads": 2},
        ))
        self.assertEqual(report["diagnostics"]["independent-sequential"], 1)
        self.assertEqual(report["diagnostics"]["dependent-sequential"], 1)
        self.assertIn("required read-back", report["diagnostics"]["interpretation"])

    def test_cli_valid_json_and_bounded_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "metadata.json"
            path.write_text(json.dumps(document(*(call(str(n)) for n in range(1000)))))
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(AUDIT.main([str(path)]), 0)
            self.assertLess(len(output.getvalue()), 3000)
            self.assertEqual(json.loads(output.getvalue())["calls"], 1000)

    def test_invalid_json_and_nonfinite_json_fail(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "metadata.json"
            for content in (
                "{private-content", '{"schema_version": NaN}', "[]",
                '{"schema_version": 1, "schema_version": 2}', "[" * 2000,
            ):
                path.write_text(content)
                errors = io.StringIO()
                with contextlib.redirect_stderr(errors):
                    self.assertEqual(AUDIT.main([str(path)]), 2)
                self.assertNotIn("private-content", errors.getvalue())

    def test_extreme_price_exponents_fail_without_unbounded_output(self) -> None:
        with self.assertRaises(AUDIT.InputError):
            AUDIT.audit(document(call(), prices={"model-a": {
                "input": Decimal("1e-999999"), "cached_input": 0, "output": 0
            }}))

    def test_zero_price_exponents_do_not_expand_output(self) -> None:
        report = AUDIT.audit(document(call(), prices={"model-a": {
            "input": Decimal("0e-999999"), "cached_input": 0, "output": 0
        }}))
        self.assertEqual(report["cost"]["usd"], "0")

    def test_self_test_runs_without_input(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(AUDIT.main(["--self-test"]), 0)
        self.assertIn("7/7 checks passed", output.getvalue())

    def test_input_is_required_except_for_self_test(self) -> None:
        for args in ([], ["--self-test", "not-read.json"]):
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as caught:
                AUDIT.main(args)
            self.assertEqual(caught.exception.code, 2)

    def test_missing_file_and_oversized_file_fail(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "metadata.json"
            with self.assertRaises(AUDIT.InputError):
                AUDIT.load(path)
            path.write_bytes(b" " * (AUDIT.MAX_BYTES + 1))
            with self.assertRaises(AUDIT.InputError):
                AUDIT.load(path)


if __name__ == "__main__":
    unittest.main()
