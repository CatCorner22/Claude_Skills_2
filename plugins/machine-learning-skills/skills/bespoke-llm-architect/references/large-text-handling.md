# Large-text handling protocol (datasets, logs, long contexts)

> **Provenance.** Near-verbatim from the user's spec "Cursor Bespoke LLM Architect Skills Master
> Prompt (Oneshot)", version 2026.08, section "Foundational Skills Integration §2 Large-Txt-Handler
> Skill".

## Contents
- Purpose
- Core principles
- Assessment protocol
- Chunking strategies
- Processing patterns
- Recommended tools
- Output guidelines

## Purpose

Process, analyze, summarize, search, extract from, edit, or transform large and complex plain-text
files, datasets, training logs, multi-file codebases, and ultra-long contexts without exceeding
memory or context limits.

## Core principles

- Never load an entire large file into model context or full memory. Assess size and structure
  first.
- Prefer streaming, generators, range access, external CLI tools, and hierarchical map-reduce
  patterns.
- Provide progressive results: high-level overview first, then details on demand.
- Always report assessment, strategy used, coverage, and next steps.
- Detect encoding and structure automatically. Preserve line numbers or byte offsets for all
  citations and extracts.

## Assessment protocol

1. Size in bytes, approximate line count, estimated tokens (chars/4 heuristic).
2. Encoding detection (prefer utf-8; errors="replace").
3. Sample beginning, middle, end (and random locations).
4. Classify structure: free prose, timestamped logs, JSONL/NDJSON, CSV/TSV,
   hierarchical/outline/source code, multi-section document, mixed dump.
5. Note special issues (extremely long lines, binary pollution).
6. Select strategy based on size + structure + user goal.

## Chunking strategies

- Fixed-size with overlap (4k–8k tokens, 10–20% overlap).
- Paragraph or blank-line aware.
- Structure-aware (logs by time windows, hierarchical by headers/indentation, JSONL by complete
  records, code by function/class boundaries).
- Hierarchical / map-reduce: coarse outline first, then fine-grained relevant chunks.
- Adaptive: coarser for overview, finer in high-relevance regions.

## Processing patterns

- **Summarization:** structural overview → map per chunk → reduce hierarchical synthesis.
- **Search/Q&A:** fast grep/rg first pass → windows of context with line numbers → optional
  temporary inverted index.
- **Extraction:** streaming pattern matching → aggregate, deduplicate, count, samples.
- **Transformation:** streaming read-transform-write or unified diff/patch. Confirm before
  destructive changes. Prefer atomic replace via temporary file.

## Recommended tools

- Bash: `wc`, `head`, `tail`, `sed -n`, `grep -n`, `split`, `rg`.
- Python: streaming generators, `mmap` for random access, Hugging Face Datasets with streaming,
  Arrow.
- For compressed: `gzip` / `zcat`.

## Output guidelines

Begin every response with a concise assessment block. Deliver value progressively. Cite every
quotation with line numbers or byte offsets. Explicitly state coverage. End with actionable
next-step suggestions.
