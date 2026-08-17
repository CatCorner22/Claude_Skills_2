"""FusionCash Architect — analyze Oracle Fusion Cash Management configuration
extracts and generate an interactive, self-contained report.

Pipeline: ingest (openpyxl, strings only) -> analyze (health score, waterfalls,
GL audit) -> report (single-file HTML with local Advanced-Criteria and
parse-rule simulators).
"""
from .ingest import load_all, load_extract, Extract, IngestError
from .analyze import analyze
from .simulate import simulate_criteria, simulate_parse_rule
from .report import render_html, write_report, build_payload

__all__ = [
    "load_all", "load_extract", "Extract", "IngestError",
    "analyze", "simulate_criteria", "simulate_parse_rule",
    "render_html", "write_report", "build_payload",
]

__version__ = "0.1.0"
