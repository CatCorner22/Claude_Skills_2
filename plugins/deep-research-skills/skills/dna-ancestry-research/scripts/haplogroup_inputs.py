#!/usr/bin/env python3
"""Prepare consumer-chip genotypes for open haplogroup callers, and screen what the callers return.

Usage:
  haplogroup_inputs.py summary <raw.txt> [--json]
  haplogroup_inputs.py mt-vcf  <raw.txt> -o <out.vcf> [--sample NAME] [--rcrs FASTA]
  haplogroup_inputs.py y-plink <raw.txt> -o <base> [--sample NAME]       # writes <base>.ped and <base>.map
  haplogroup_inputs.py y-genos <raw.txt> -o <out.genos.txt> [--sample NAME]
  haplogroup_inputs.py review  <caller_report> [--json]
  haplogroup_inputs.py --self-test                                       # offline checks, no input files

WHAT THIS DOES
  summary  Counts the file's MT, Y and X sites, no-calls, indel codes and heterozygous-looking calls,
           reports the genome build the file declares, and says whether a Y chromosome is present at
           all. Run it first: it tells you which of the other modes make sense.
  mt-vcf   Writes the mitochondrial calls as a single-sample VCF against the rCRS reference, with
           EVERY genotyped site present (reference calls as GT 0, differences as GT 1). HaploGrep 3
           in --chip mode builds its coverage range from the sites present, so leaving the reference
           calls out makes it score missing sites as "not covered" and inflates the quality score.
  y-plink  Writes the Y-chromosome calls as PLINK text (.ped/.map) for Yleaf's -plink mode, which
           reads no reference genome and needs no bcftools. Refuses a file whose Y sites are
           essentially all no-calls, which is what a person without a Y chromosome produces.
  y-genos  Writes the Y calls in yhaplo's sample-major .genos.txt layout, for anyone who has yhaplo
           installed under its own licence. Nothing here depends on yhaplo.
  review   Reads a HaploGrep 3 extended report or a Yleaf hg_prediction_combined.hg table and screens
           it: for each expected mutation the chip did not show, it checks whether the chip called the
           base's complement at that position (an A<->T or C<->G flip is a strand artefact, not a
           private mutation); for Yleaf it reports whether the trees agree on the terminal marker.

WHAT THIS DELIBERATELY DOES NOT DO
  It calls no haplogroup. HaploGrep 3 and Yleaf carry the trees and the scoring; the skill's
  references carry the interpretation. It assigns no ancestry percentage and no origin.

BUILD SAFETY
  Chip positions are only meaningful against the build the file declares. The converters require a
  declared build 37 (GRCh37/hg19) because the bundled rCRS and Yleaf's hg19 marker tables are build
  37; a build 36 or 38 file, or an undeclared build, exits 3 rather than producing a plausible but
  wrong file.

PRIVACY
  Reads locally and writes only the files you name. A raw genotype file, and every file this script
  derives from it, identifies a person and their relatives: keep them out of any repository
  (the .vcf, .ped, .map and .genos.txt outputs are not ignored by most .gitignore files).

Exit codes:
  0  ok
  2  input unreadable, empty, or not a recognised format
  3  unsafe to proceed (undeclared or unsupported build; no Y chromosome signal)
  5  bad usage
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile

__version__ = "1.0.0"

ASSETS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
RCRS_DEFAULT = os.path.join(ASSETS, "rCRS_NC_012920.1.fasta")
RCRS_LENGTH = 16569
RCRS_MD5 = "c68f52674c9fb33aef52dcf399755519"
COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C"}
NOCALL = {"--", "-", "", "0", "00", "NN", "N", "..", "."}
CHROM_CODES = {"23": "X", "24": "Y", "25": "XY", "26": "MT", "M": "MT", "CHRM": "MT", "CHRMT": "MT",
               "CHRY": "Y", "CHRX": "X"}
Y_CALLED_MIN = 0.50   # below this fraction of called Y sites the file is treated as having no Y


class InputError(Exception):
    pass


class UnsafeError(Exception):
    pass


# ----------------------------------------------------------------------------- parsing

def detect_build(header_lines: list[str]) -> str | None:
    """Return '36', '37' or '38' from the file's own comment header, or None when it says nothing."""
    text = " ".join(header_lines).lower()
    for build, pats in (("38", (r"build\s*38", r"grch38", r"hg38")),
                        ("37", (r"build\s*37", r"grch37", r"hg19")),
                        ("36", (r"build\s*36", r"ncbi36", r"hg18"))):
        if any(re.search(p, text) for p in pats):
            return build
    return None


def norm_chrom(c: str) -> str:
    c = c.strip().strip('"').upper()
    if c.startswith("CHR") and c not in CHROM_CODES:
        c = c[3:]
    return CHROM_CODES.get(c, c)


def parse_raw(path: str) -> dict:
    """Parse 23andMe-style (rsid, chromosome, position, genotype), AncestryDNA-style (rsid, chromosome,
    position, allele1, allele2) and quoted/comma-delimited exports into one structure.

    Returns {"build": str|None, "rows": {chrom: [(rsid, pos, genotype)]}, "nrows": int}. A genotype is the
    uppercased call with quotes stripped; no-calls are kept as '--' so callers can count them."""
    header, rows, n = [], {}, 0
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.rstrip("\r\n")
                if not line.strip():
                    continue
                if line.startswith("#"):
                    header.append(line)
                    continue
                delim = "\t" if "\t" in line else ","
                parts = [p.strip().strip('"') for p in line.split(delim)]
                if len(parts) < 4:
                    continue
                if parts[0].lower() in ("rsid", "snp", "id") or parts[1].lower() in ("chromosome", "chrom", "chr"):
                    header.append(line)
                    continue
                rsid, chrom, pos = parts[0], norm_chrom(parts[1]), parts[2]
                if not pos.isdigit():
                    continue
                gt = (parts[3] + parts[4]) if len(parts) >= 5 and len(parts[3]) == 1 and len(parts[4]) == 1 else parts[3]
                gt = gt.upper()
                if gt in NOCALL or set(gt) <= {"-", "0", "N", "."}:
                    gt = "--"
                rows.setdefault(chrom, []).append((rsid, int(pos), gt))
                n += 1
    except OSError as e:
        raise InputError(f"cannot read {path}: {e}")
    if n == 0:
        raise InputError(f"{path}: no genotype rows recognised (expected rsid / chromosome / position / genotype)")
    return {"build": detect_build(header), "rows": rows, "nrows": n}


def classify_call(gt: str) -> str:
    """'nocall' | 'indel' | 'het' | 'call' for a haploid-context genotype string."""
    if gt == "--":
        return "nocall"
    if any(c in "DI" for c in gt):
        return "indel"
    alleles = set(gt)
    if not alleles <= set("ACGT"):
        return "nocall"
    return "call" if len(alleles) == 1 else "het"


def chrom_stats(rows: list[tuple]) -> dict:
    out = {"sites": len(rows), "call": 0, "nocall": 0, "indel": 0, "het": 0}
    for _, _, gt in rows:
        out[classify_call(gt)] += 1
    out["called_fraction"] = round(out["call"] / out["sites"], 4) if out["sites"] else 0.0
    return out


def require_build37(data: dict) -> None:
    b = data["build"]
    if b is None:
        raise UnsafeError("the file declares no genome build; positions cannot be mapped safely. "
                          "23andMe and AncestryDNA exports state the build in their comment header — if yours "
                          "has been stripped, restore the header or obtain a fresh export.")
    if b != "37":
        raise UnsafeError(f"the file declares build {b}; this tool's reference data (rCRS positions, Yleaf hg19 "
                          f"tables) is build 37. Re-export in build 37 or lift the positions over first.")


# ----------------------------------------------------------------------------- rCRS

def load_rcrs(path: str = RCRS_DEFAULT) -> str:
    try:
        with open(path, encoding="utf-8") as fh:
            seq = "".join(l.strip() for l in fh if not l.startswith(">")).upper()
    except OSError as e:
        raise InputError(f"cannot read rCRS reference {path}: {e}")
    if len(seq) != RCRS_LENGTH:
        raise InputError(f"rCRS reference {path} has length {len(seq)}, expected {RCRS_LENGTH}")
    if hashlib.md5(seq.encode()).hexdigest() != RCRS_MD5:
        raise InputError(f"rCRS reference {path} does not match the expected sequence (md5 mismatch)")
    return seq


# ----------------------------------------------------------------------------- converters

def mt_sites(data: dict) -> tuple[dict, dict]:
    """Return ({pos: base}, counts) for usable haploid MT calls, dropping indel codes, heterozygous-looking
    calls and positions that carry conflicting duplicate rows."""
    counts = {"call": 0, "nocall": 0, "indel": 0, "het": 0, "conflict": 0, "out_of_range": 0}
    calls: dict[int, str] = {}
    conflict: set[int] = set()
    for _, pos, gt in data["rows"].get("MT", []):
        kind = classify_call(gt)
        if kind != "call":
            counts[kind] += 1
            continue
        if not 1 <= pos <= RCRS_LENGTH:
            counts["out_of_range"] += 1
            continue
        base = gt[0]
        if pos in calls and calls[pos] != base:
            conflict.add(pos)
        calls.setdefault(pos, base)
        counts["call"] += 1
    for pos in conflict:
        del calls[pos]
    counts["conflict"] = len(conflict)
    return calls, counts


def write_mt_vcf(data: dict, out_path: str, sample: str = "SAMPLE", rcrs_path: str = RCRS_DEFAULT) -> dict:
    require_build37(data)
    if "MT" not in data["rows"]:
        raise InputError("the file has no MT rows; nothing to convert")
    ref = load_rcrs(rcrs_path)
    calls, counts = mt_sites(data)
    rows, n_ref, n_alt = [], 0, 0
    for pos in sorted(calls):
        base, r = calls[pos], ref[pos - 1]
        if base == r:
            rows.append(f"MT\t{pos}\t.\t{r}\t.\t.\tPASS\t.\tGT\t0")
            n_ref += 1
        else:
            rows.append(f"MT\t{pos}\t.\t{r}\t{base}\t.\tPASS\t.\tGT\t1")
            n_alt += 1
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("##fileformat=VCFv4.2\n")
        fh.write(f"##source=haplogroup_inputs.py v{__version__} (consumer chip calls; every genotyped MT site listed)\n")
        fh.write("##reference=rCRS NC_012920.1\n")
        fh.write(f"##contig=<ID=MT,length={RCRS_LENGTH},assembly=b37>\n")
        fh.write('##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype (haploid)">\n')
        fh.write(f"#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t{sample}\n")
        fh.write("\n".join(rows) + ("\n" if rows else ""))
    return {"out": out_path, "sites_written": len(rows), "reference_calls": n_ref, "variant_calls": n_alt, **counts}


def y_calls(data: dict) -> tuple[list[tuple[str, int, str | None]], dict]:
    """[(rsid, pos, base-or-None)] for Y rows in file order, plus stats; raises UnsafeError when the Y
    chromosome is essentially uncalled."""
    rows = data["rows"].get("Y", [])
    if not rows:
        raise UnsafeError("the file has no Y-chromosome rows at all; Y-haplogroup analysis does not apply")
    st = chrom_stats(rows)
    if st["called_fraction"] < Y_CALLED_MIN:
        raise UnsafeError(f"only {st['call']} of {st['sites']} Y sites are called ({st['called_fraction']:.0%}); "
                          f"this is the pattern of a file from a person without a Y chromosome, so a Y-haplogroup "
                          f"call would be noise. Nothing written.")
    out = []
    for rsid, pos, gt in rows:
        out.append((rsid, pos, gt[0] if classify_call(gt) == "call" else None))
    return out, st


def write_y_plink(data: dict, base: str, sample: str = "SAMPLE") -> dict:
    require_build37(data)
    calls, st = y_calls(data)
    with open(base + ".map", "w", encoding="utf-8") as fh:
        for rsid, pos, _ in calls:
            fh.write(f"Y\t{rsid}\t0\t{pos}\n")
    with open(base + ".ped", "w", encoding="utf-8") as fh:
        genos = " ".join(f"{b} {b}" if b else "0 0" for _, _, b in calls)
        fh.write(f"FAM1 {sample} 0 0 1 -9 {genos}\n")
    return {"map": base + ".map", "ped": base + ".ped", **st}


def write_y_genos(data: dict, out_path: str, sample: str = "SAMPLE") -> dict:
    require_build37(data)
    calls, st = y_calls(data)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("ID\t" + "\t".join(str(pos) for _, pos, _ in calls) + "\n")
        fh.write(sample + "\t" + "\t".join(b if b else "." for _, _, b in calls) + "\n")
    return {"out": out_path, **st}


def summary(data: dict) -> dict:
    out = {"build": data["build"], "rows": data["nrows"], "chromosomes": {}}
    for c in ("MT", "Y", "X"):
        if c in data["rows"]:
            out["chromosomes"][c] = chrom_stats(data["rows"][c])
    y = out["chromosomes"].get("Y")
    out["y_present"] = bool(y and y["called_fraction"] >= Y_CALLED_MIN)
    out["modes"] = {
        "mt-vcf": "MT" in data["rows"] and data["build"] == "37",
        "y-plink": bool(out["y_present"]) and data["build"] == "37",
    }
    return out


# ----------------------------------------------------------------------------- review

def _split_polys(field: str) -> dict[int, str]:
    """'12633A 15452A' -> {12633: 'A', 15452: 'A'}; tolerates annotations in parentheses/brackets."""
    out = {}
    for tok in field.replace('"', "").split():
        m = re.match(r"^(\d+)([ACGTacgt])", tok)
        if m:
            out[int(m.group(1))] = m.group(2).upper()
    return out


def review_haplogrep(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        lines = [l.rstrip("\n") for l in fh if l.strip()]
    if len(lines) < 2:
        raise InputError(f"{path}: no sample rows")
    header = [h.strip('"') for h in lines[0].split("\t")]
    need = {"Haplogroup", "Quality", "Not_Found_Polys", "Input_Sample"}
    if not need <= set(header):
        raise InputError(f"{path}: not a HaploGrep 3 extended report (run classify with --extend-report); "
                         f"missing columns {sorted(need - set(header))}")
    samples = []
    for line in lines[1:]:
        f = dict(zip(header, [v.strip('"') for v in line.split("\t")]))
        expected_missing = _split_polys(f.get("Not_Found_Polys", ""))
        observed = _split_polys(f.get("Input_Sample", ""))
        flips, absent, other = [], [], []
        for pos, exp in sorted(expected_missing.items()):
            obs = observed.get(pos)
            if obs is None:
                absent.append(f"{pos}{exp}")
            elif obs == COMPLEMENT[exp]:
                flips.append(f"{pos}{exp} (chip shows {obs})")
            else:
                other.append(f"{pos}{exp} (chip shows {obs})")
        remaining = f.get("Remaining_Polys", "")
        n_private = len(re.findall(r"\b\d+[ACGT]\b", remaining.replace("(", " (")))
        samples.append({
            "sample": f.get("SampleID", "?"), "haplogroup": f.get("Haplogroup", "?"),
            "quality": f.get("Quality", "?"), "expected_not_found": len(expected_missing),
            "strand_flip_candidates": flips, "not_genotyped_or_reference": absent,
            "other_discrepancies": other, "private_mutations": n_private,
            "note": ("A chip call of the complement base at an expected site is a strand artefact of the probe, "
                     "not a private mutation; any remaining private mutations are chip-only until sequencing "
                     "confirms them." if flips or n_private else ""),
        })
    return {"tool": "haplogrep3", "samples": samples}


def review_yleaf(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        lines = [l.rstrip("\n") for l in fh if l.strip()]
    header = lines[0].split("\t")
    trees = sorted({h[:-3] for h in header if h.endswith("_Hg")})
    if not trees:
        raise InputError(f"{path}: not a Yleaf combined prediction table (no *_Hg columns)")
    samples = []
    for line in lines[1:]:
        f = dict(zip(header, line.split("\t")))
        per = {t: {"haplogroup": f.get(f"{t}_Hg"), "marker": f.get(f"{t}_Hg_marker"),
                   "qc": f.get(f"{t}_QC")} for t in trees}
        markers = {v["marker"] for v in per.values()}
        samples.append({"sample": f.get("Sample_name", "?"), "trees": per,
                        "trees_agree_on_terminal_marker": len(markers) == 1,
                        "terminal_markers": sorted(m for m in markers if m)})
    return {"tool": "yleaf", "samples": samples}


def review(path: str) -> dict:
    try:
        with open(path, encoding="utf-8") as fh:
            first = fh.readline()
    except OSError as e:
        raise InputError(f"cannot read {path}: {e}")
    if "Sample_name" in first and "_Hg" in first:
        return review_yleaf(path)
    if "Haplogroup" in first:
        return review_haplogrep(path)
    raise InputError(f"{path}: neither a HaploGrep 3 report nor a Yleaf combined table")


def print_review(r: dict) -> None:
    for s in r["samples"]:
        if r["tool"] == "haplogrep3":
            print(f"{s['sample']}: {s['haplogroup']} (quality {s['quality']})")
            print(f"  expected mutations not seen on chip: {s['expected_not_found']}")
            if s["strand_flip_candidates"]:
                print("  strand-flip candidates (complement called): " + ", ".join(s["strand_flip_candidates"]))
            if s["not_genotyped_or_reference"]:
                print("  not genotyped, or called reference: " + ", ".join(s["not_genotyped_or_reference"]))
            if s["other_discrepancies"]:
                print("  other discrepancies: " + ", ".join(s["other_discrepancies"]))
            print(f"  chip-only private mutations: {s['private_mutations']}")
            if s["note"]:
                print("  " + s["note"])
        else:
            print(f"{s['sample']}:")
            for t, v in s["trees"].items():
                print(f"  {t:10s} {v['haplogroup']}  terminal marker {v['marker']}  QC {v['qc']}")
            print("  trees agree on the terminal marker: " + ("yes" if s["trees_agree_on_terminal_marker"] else "NO"))


# ----------------------------------------------------------------------------- self-test

def _synthetic_raw(path: str, build: str | None = "37", y_called: bool = True, style: str = "23andme") -> None:
    hdr = ["# synthetic fixture", "# rsid\tchromosome\tposition\tgenotype"]
    if build:
        hdr.insert(1, f"# We are using reference human assembly build {build}.")
    mt = [("i1", "MT", 73, "G"), ("i2", "MT", 263, "G"), ("i3", "MT", 750, "A"), ("i4", "MT", 1438, "A"),
          ("i5", "MT", 310, "D"), ("i6", "MT", 16519, "--"), ("i7", "MT", 3010, "AG"), ("i8", "MT", 7028, "T"),
          ("i9", "MT", 11719, "A"), ("i10", "MT", 11719, "G"), ("i11", "MT", 8860, "G")]
    y = [(f"y{i}", "Y", 2650000 + i * 1000, ("A" if y_called else "--") if i % 5 else "--") for i in range(1, 21)]
    y += [("y21", "Y", 2700000, "AG")]  # heterozygous-looking: must be written as missing
    rows = [("rs1", "1", 10000, "AA"), ("rs2", "X", 300000, "CT")] + mt + y
    with open(path, "w", encoding="utf-8") as fh:
        if style == "23andme":
            fh.write("\n".join(hdr) + "\n")
            for rsid, c, p, g in rows:
                fh.write(f"{rsid}\t{c}\t{p}\t{g}\n")
        elif style == "ancestry":
            fh.write("#AncestryDNA raw data download\n#reference human genome build 37.1\n")
            fh.write("rsid\tchromosome\tposition\tallele1\tallele2\n")
            code = {"MT": "26", "Y": "24", "X": "23"}
            for rsid, c, p, g in rows:
                a = g if len(g) == 2 else g * 2
                a1, a2 = ("0", "0") if g == "--" else (a[0], a[1])
                fh.write(f"{rsid}\t{code.get(c, c)}\t{p}\t{a1}\t{a2}\n")
        else:  # quoted csv
            fh.write("# build 37\n")
            fh.write('"RSID","CHROMOSOME","POSITION","RESULT"\n')
            for rsid, c, p, g in rows:
                fh.write(f'"{rsid}","{c}","{p}","{g}"\n')


def self_test() -> int:
    passed, failed = 0, 0

    def check(cond: bool, label: str) -> None:
        nonlocal passed, failed
        if cond:
            passed += 1
        else:
            failed += 1
            print(f"FAIL: {label}")

    def raises(fn, exc) -> bool:
        try:
            fn()
        except exc:
            return True
        except Exception:
            return False
        return False

    with tempfile.TemporaryDirectory() as td:
        raw = os.path.join(td, "raw.txt")
        _synthetic_raw(raw)
        data = parse_raw(raw)
        # --- parsing and summary
        check(data["build"] == "37", "build 37 detected from the comment header")
        check(len(data["rows"]["MT"]) == 11 and len(data["rows"]["Y"]) == 21, "MT and Y rows counted")
        s = summary(data)
        mt = s["chromosomes"]["MT"]
        check(mt["call"] == 8 and mt["nocall"] == 1 and mt["indel"] == 1 and mt["het"] == 1, "MT call classes counted")
        check(s["y_present"] is True and s["modes"]["mt-vcf"] and s["modes"]["y-plink"], "summary: Y present, modes offered")
        check(detect_build(["# GRCh38 export"]) == "38" and detect_build(["# hg19"]) == "37"
              and detect_build(["# nothing"]) is None, "build detection covers the common spellings")
        # --- rCRS asset
        ref = load_rcrs()
        check(ref[73 - 1] == "A" and ref[7028 - 1] == "C" and ref[11719 - 1] == "G" and ref[16519 - 1] == "T",
              "bundled rCRS has the expected bases at landmark positions")
        bad = os.path.join(td, "bad.fa")
        with open(bad, "w") as fh:
            fh.write(">x\n" + "A" * RCRS_LENGTH + "\n")
        check(raises(lambda: load_rcrs(bad), InputError), "a wrong-content reference of the right length is rejected")
        # --- mt-vcf
        vcf = os.path.join(td, "mt.vcf")
        r = write_mt_vcf(data, vcf, sample="S1")
        lines = [l for l in open(vcf) if not l.startswith("#")]
        by_pos = {int(l.split("\t")[1]): l.rstrip("\n").split("\t") for l in lines}
        check(r["sites_written"] == 6 and r["conflict"] == 1 and r["indel"] == 1 and r["het"] == 1,
              "mt-vcf writes only usable sites and counts what it dropped")
        check(11719 not in by_pos, "a position with conflicting duplicate rows is dropped, not guessed")
        check(by_pos[73][3] == "A" and by_pos[73][4] == "G" and by_pos[73][9] == "1", "73G written as A>G, GT 1")
        check(by_pos[750][3] == "A" and by_pos[750][4] == "." and by_pos[750][9] == "0",
              "a reference call is written with ALT '.' and GT 0 (coverage, not variation)")
        check(by_pos[7028][4] == "T" and by_pos[8860][4] == "G", "7028T and 8860G written as variants")
        check([int(l.split("\t")[1]) for l in lines] == sorted(int(l.split("\t")[1]) for l in lines), "VCF rows sorted")
        header_text = "".join(l for l in open(vcf) if l.startswith("#"))
        check(f"##contig=<ID=MT,length={RCRS_LENGTH},assembly=b37>" in header_text and header_text.rstrip().endswith("S1"),
              "VCF header carries the MT contig and the sample name")
        check(r["reference_calls"] == 2 and r["variant_calls"] == 4, "reference/variant tallies (750A, 1438A reference; 73G, 263G, 7028T, 8860G variant)")
        # --- build guards
        raw38 = os.path.join(td, "raw38.txt")
        _synthetic_raw(raw38, build="38")
        check(raises(lambda: write_mt_vcf(parse_raw(raw38), os.path.join(td, "x.vcf")), UnsafeError),
              "a build 38 file is refused by mt-vcf")
        rawnb = os.path.join(td, "rawnb.txt")
        _synthetic_raw(rawnb, build=None)
        try:
            write_y_plink(parse_raw(rawnb), os.path.join(td, "nb"))
            msg = ""
        except UnsafeError as e:
            msg = str(e)
        check("declares no genome build" in msg, "an undeclared build is refused by y-plink, and the message says the build is missing")
        check(parse_raw(rawnb)["build"] is None and summary(parse_raw(rawnb))["modes"]["mt-vcf"] is False,
              "summary withholds the modes when the build is unknown")
        # --- y-plink
        base = os.path.join(td, "chipY")
        r = write_y_plink(data, base, sample="S1")
        mapl = open(base + ".map").read().splitlines()
        ped = open(base + ".ped").read().split()
        check(len(mapl) == 21 and mapl[0].split("\t") == ["Y", "y1", "0", "2651000"], ".map has one Y row per site")
        check(len(ped) == 6 + 2 * 21 and ped[1] == "S1" and ped[4] == "1", ".ped has FID IID PID MID SEX PHENO + pairs")
        check(ped[6:8] == ["A", "A"] and ped[6 + 2 * 4:8 + 2 * 4] == ["0", "0"], "called site 'A A', no-call '0 0'")
        check(ped[-2:] == ["0", "0"], "a heterozygous-looking Y call is written as missing")
        rawf = os.path.join(td, "rawf.txt")
        _synthetic_raw(rawf, y_called=False)
        check(raises(lambda: write_y_plink(parse_raw(rawf), os.path.join(td, "f")), UnsafeError),
              "a file whose Y sites are all no-calls is refused (no Y chromosome)")
        check(summary(parse_raw(rawf))["y_present"] is False, "summary reports Y absent for that file")
        # --- y-genos
        gen = os.path.join(td, "chipY.genos.txt")
        write_y_genos(data, gen, sample="S1")
        g = open(gen).read().splitlines()
        h, row = g[0].split("\t"), g[1].split("\t")
        check(h[0] == "ID" and h[1] == "2651000" and len(h) == 22 and row[0] == "S1" and row[1] == "A" and row[5] == "."
              and row[-1] == ".", "yhaplo layout: positions header, '.' for missing")
        # --- other vendor layouts
        anc = os.path.join(td, "anc.txt")
        _synthetic_raw(anc, style="ancestry")
        d2 = parse_raw(anc)
        check(d2["build"] == "37" and "MT" in d2["rows"] and "Y" in d2["rows"]
              and dict((p, g) for _, p, g in d2["rows"]["MT"])[73] == "GG", "AncestryDNA layout: numeric chromosomes and two allele columns")
        check(write_mt_vcf(d2, os.path.join(td, "anc.vcf"))["sites_written"] == 6, "AncestryDNA MT calls convert identically")
        csvf = os.path.join(td, "mh.csv")
        _synthetic_raw(csvf, style="csv")
        d3 = parse_raw(csvf)
        check(d3["build"] == "37" and len(d3["rows"]["MT"]) == 11, "quoted comma-delimited layout parses")
        empty = os.path.join(td, "empty.txt")
        open(empty, "w").write("# only a header\n")
        check(raises(lambda: parse_raw(empty), InputError), "a file with no genotype rows is rejected loudly")
        prose = os.path.join(td, "prose.txt")
        open(prose, "w").write("Dear diary, nothing to see here.\nSecond line.\n")
        check(raises(lambda: parse_raw(prose), InputError), "prose is not parsed as genotypes")
        # --- review: HaploGrep
        rep = os.path.join(td, "hg3.txt")
        with open(rep, "w") as fh:
            fh.write('"SampleID"\t"Haplogroup"\t"Rank"\t"Quality"\t"Range"\t"Not_Found_Polys"\t"Found_Polys"\t"Remaining_Polys"\t"AAC_In_Remainings"\t"Input_Sample"\n')
            fh.write('"S1"\t"T1a1j"\t"1"\t"0.8440"\t"1 2"\t"12633A 15452A 9999G 4216C"\t"73G"\t'
                     '"613G (globalPrivateMutation) 5839T (localPrivateMutation)"\t""\t"73G 613G 5839T 12633T 15452T 4216T"\n')
        rv = review(rep)
        s1 = rv["samples"][0]
        check(rv["tool"] == "haplogrep3" and s1["haplogroup"] == "T1a1j" and s1["quality"] == "0.8440", "HaploGrep report parsed")
        check(s1["strand_flip_candidates"] == ["12633A (chip shows T)", "15452A (chip shows T)"],
              "complement calls at expected sites are flagged as strand flips")
        check(s1["not_genotyped_or_reference"] == ["9999G"], "an expected site absent from the input is reported separately")
        check(s1["other_discrepancies"] == ["4216C (chip shows T)"], "a non-complement discrepancy is not called a flip")
        check(s1["private_mutations"] == 2, "private mutations counted from Remaining_Polys")
        plain = os.path.join(td, "plain.txt")
        with open(plain, "w") as fh:
            fh.write('"SampleID"\t"Haplogroup"\t"Rank"\t"Quality"\t"Range"\t"Not_Found_Polys"\n"S1"\t"H"\t"1"\t"0.9"\t"1-16569"\t""\n')
        check(raises(lambda: review(plain), InputError), "a non-extended report is refused with a pointer to --extend-report")
        # --- review: Yleaf
        yl = os.path.join(td, "combined.hg")
        with open(yl, "w") as fh:
            fh.write("Sample_name\tyfull_Hg\tyfull_Hg_marker\tyfull_Valid_markers\tyfull_QC\tftdna_Hg\tftdna_Hg_marker\tftdna_Valid_markers\tftdna_QC\n")
            fh.write("chip\tR-Y21048\tA1333\t1790\t1.0\tR-A1333\tA1333\t1968\t1.0\n")
            fh.write("other\tR-L21\tL21\t1700\t0.9\tR-DF13\tDF13\t1800\t0.8\n")
        ry = review(yl)
        check(ry["tool"] == "yleaf" and ry["samples"][0]["trees_agree_on_terminal_marker"] is True
              and ry["samples"][0]["trees"]["ftdna"]["haplogroup"] == "R-A1333", "Yleaf combined table parsed; agreement detected")
        check(ry["samples"][1]["trees_agree_on_terminal_marker"] is False and ry["samples"][1]["terminal_markers"] == ["DF13", "L21"],
              "tree disagreement on the terminal marker is reported")
        check(raises(lambda: review(prose), InputError), "an unrecognised report is rejected")

    total = passed + failed
    print(f"{passed}/{total} checks passed" + ("" if failed else " — all offline logic checks passed"))
    return 0 if failed == 0 else 1


# ----------------------------------------------------------------------------- cli

def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv == ["--self-test"]:
        return self_test()
    ap = argparse.ArgumentParser(prog="haplogroup_inputs.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--version", action="version", version=__version__)
    sub = ap.add_subparsers(dest="mode", required=True)
    p = sub.add_parser("summary"); p.add_argument("raw"); p.add_argument("--json", action="store_true")
    p = sub.add_parser("mt-vcf"); p.add_argument("raw"); p.add_argument("-o", "--out", required=True)
    p.add_argument("--sample", default="SAMPLE"); p.add_argument("--rcrs", default=RCRS_DEFAULT)
    p = sub.add_parser("y-plink"); p.add_argument("raw"); p.add_argument("-o", "--out", required=True, help="base name; .ped and .map are added")
    p.add_argument("--sample", default="SAMPLE")
    p = sub.add_parser("y-genos"); p.add_argument("raw"); p.add_argument("-o", "--out", required=True)
    p.add_argument("--sample", default="SAMPLE")
    p = sub.add_parser("review"); p.add_argument("report"); p.add_argument("--json", action="store_true")
    try:
        a = ap.parse_args(argv)
    except SystemExit as e:
        return 0 if e.code == 0 else 5
    try:
        if a.mode == "review":
            r = review(a.report)
            print(json.dumps(r, indent=2)) if a.json else print_review(r)
            return 0
        data = parse_raw(a.raw)
        if a.mode == "summary":
            s = summary(data)
            if a.json:
                print(json.dumps(s, indent=2))
            else:
                print(f"build declared: {s['build'] or 'NONE (unsafe to map positions)'}; rows: {s['rows']}")
                for c, st in s["chromosomes"].items():
                    print(f"  {c:3s} sites {st['sites']:6d}  called {st['call']:6d} ({st['called_fraction']:.1%})  "
                          f"no-call {st['nocall']}  indel {st['indel']}  het-looking {st['het']}")
                print("  Y chromosome present: " + ("yes" if s["y_present"] else "no — skip Y-haplogroup work"))
                print("  modes available: " + ", ".join(k for k, v in s["modes"].items() if v) if any(s["modes"].values())
                      else "  modes available: none (see build and Y notes above)")
            return 0
        if a.mode == "mt-vcf":
            r = write_mt_vcf(data, a.out, a.sample, a.rcrs)
            print(f"wrote {r['out']}: {r['sites_written']} MT sites ({r['reference_calls']} reference, {r['variant_calls']} variant); "
                  f"dropped no-call {r['nocall']}, indel {r['indel']}, het-looking {r['het']}, conflicting {r['conflict']}")
            print("next: haplogrep3 classify --in <vcf> --tree phylotree-rcrs@17.3 --chip --extend-report --write-qc --out <report>")
            return 0
        if a.mode == "y-plink":
            r = write_y_plink(data, a.out, a.sample)
            print(f"wrote {r['ped']} and {r['map']}: {r['sites']} Y sites, {r['call']} called ({r['called_fraction']:.1%})")
            print("next: Yleaf -plink <base>.ped -o <dir> --reference_genome hg19 --tree yfull ftdna isogg")
            return 0
        if a.mode == "y-genos":
            r = write_y_genos(data, a.out, a.sample)
            print(f"wrote {r['out']}: {r['sites']} Y sites, {r['call']} called ({r['called_fraction']:.1%})")
            return 0
    except InputError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    except UnsafeError as e:
        print(f"refused: {e}", file=sys.stderr)
        return 3
    return 5


if __name__ == "__main__":
    sys.exit(main())
