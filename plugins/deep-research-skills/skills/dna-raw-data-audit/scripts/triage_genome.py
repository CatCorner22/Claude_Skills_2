#!/usr/bin/env python3
"""Parse and quality-check consumer genome raw data, and extract catalogued sites.

Usage:
  triage_genome.py <file> [<file2>] [--json] [--catalog-only]
  triage_genome.py --self-test            # offline logic tests, no network, no input files

WHAT THIS DOES
  - Parses 23andMe-style raw data (rsid / chromosome / position / genotype, tab-delimited) and VCF.
  - Detects the genome build from file headers where it is declared, and refuses to guess when it
    is not. A position lookup against the wrong build silently returns a different variant.
  - Reports total sites, no-call rate, and per-chromosome counts.
  - With two files, reports cross-platform concordance at shared sites. Two platforms genotyping the
    same person is a real quality signal, and a discordant call at a site you were about to
    interpret is itself a finding.
  - Extracts genotypes at a small set of catalogued sites so interpretation happens against
    verified calls rather than assumed ones.
  - Resolves the APOE diplotype from rs429358 + rs7412, and flags the one combination that is
    formally ambiguous.
  - Flags strand-ambiguous (A/T, C/G) sites, where a flipped orientation inverts the call.

WHAT THIS DELIBERATELY DOES NOT DO
  No risk scores. No pathogenicity assignment. No recommendations, doses, or supplement advice.
  Those require literature appraisal, absolute-risk conversion, and clinical judgement that a
  parser has no business simulating. This establishes what the DATA says; the skill's references
  carry the interpretation.

PRIVACY
  Reads locally and writes nothing but its report to stdout. Never send a genome to a third-party
  service, and never commit one: the repository's .gitignore covers the common genomic extensions
  and a genomes/ directory, but the safest place for the file is outside the repo entirely.

Exit codes:
  0  parsed successfully
  2  input unreadable, empty, or not a recognised format
  3  build could not be determined (interpretation would be unsafe)
  5  bad usage
"""

from __future__ import annotations

import argparse
import gzip
import io
import json
import os
import re
import sys
from collections import Counter

# --------------------------------------------------------------------------------------
# Catalogued sites. Genotype extraction targets ONLY — no effect sizes, no actions here.
# Effect sizes, array reliability, and actionability live in references/variant-catalog.md,
# where they can carry citations, absolute-risk framing, and the caveats a dict cannot hold.
# --------------------------------------------------------------------------------------
CATALOG = {
    "rs429358": ("APOE", "APOE haplotype-defining site (Cys112Arg)"),
    "rs7412":   ("APOE", "APOE haplotype-defining site (Arg158Cys)"),
    "rs1799945": ("HFE", "HFE H63D"),
    "rs1800562": ("HFE", "HFE C282Y"),
    "rs6025":    ("F5", "Factor V Leiden"),
    "rs1801133": ("MTHFR", "MTHFR C677T — see the MTHFR corrective before interpreting"),
    "rs1801131": ("MTHFR", "MTHFR A1298C — see the MTHFR corrective before interpreting"),
    "rs671":     ("ALDH2", "ALDH2 Glu504Lys"),
    "rs4988235": ("MCM6/LCT", "lactase persistence regulatory variant"),
    "rs762551":  ("CYP1A2", "CYP1A2 -163C>A"),
    "rs9939609": ("FTO", "FTO intron 1"),
    "rs4149056": ("SLCO1B1", "SLCO1B1 *5 (Val174Ala)"),
    "rs4244285": ("CYP2C19", "CYP2C19 *2"),
    "rs4986893": ("CYP2C19", "CYP2C19 *3"),
    "rs12248560": ("CYP2C19", "CYP2C19 *17"),
    "rs1799853": ("CYP2C9", "CYP2C9 *2"),
    "rs1057910": ("CYP2C9", "CYP2C9 *3"),
    "rs9923231": ("VKORC1", "VKORC1 -1639G>A"),
    "rs3892097": ("CYP2D6", "CYP2D6 *4 tag — NOT sufficient to call a CYP2D6 diplotype"),
    "rs1800460": ("TPMT", "TPMT *3B"),
    "rs1142345": ("TPMT", "TPMT *3C"),
    "rs116855232": ("NUDT15", "NUDT15 *3"),
    "rs3918290": ("DPYD", "DPYD *2A"),
}

AMBIGUOUS_PAIRS = ({"A", "T"}, {"C", "G"})

# APOE haplotypes as (rs429358, rs7412). e1 is rare but must be modelled: it is the sole
# reason one genotype combination is ambiguous.
APOE_HAP = {"e1": ("C", "T"), "e2": ("T", "T"), "e3": ("T", "C"), "e4": ("C", "C")}


def _open(path: str):
    if path.endswith((".gz", ".bgz")):
        return io.TextIOWrapper(gzip.open(path, "rb"), encoding="utf-8", errors="replace")
    return open(path, encoding="utf-8", errors="replace")


def detect_build(header_lines: list[str]) -> str | None:
    """Return a build label if the file declares one, else None. Never guess."""
    blob = "\n".join(header_lines).lower()
    # Order matters: check the 38 family before 37, since "grch38" contains no "37" but
    # some headers name both a source and a target.
    if re.search(r"grch38|hg38|build 38|\bb38\b", blob):
        return "GRCh38"
    if re.search(r"grch37|hg19|build 37|\bb37\b", blob):
        return "GRCh37/hg19"
    return None


def parse_23andme(path: str) -> dict:
    header, calls = [], {}
    nocall = 0
    with _open(path) as fh:
        for line in fh:
            if line.startswith("#"):
                header.append(line.rstrip("\n"))
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            rsid, chrom, pos, geno = parts[0], parts[1], parts[2], parts[3].strip().upper()
            if rsid.lower() in ("rsid", "# rsid"):
                continue  # a column header line that lost its '#'
            if not geno or set(geno) <= {"-", "0", "."}:
                nocall += 1
                calls[rsid] = {"chrom": chrom, "pos": pos, "geno": None}
                continue
            calls[rsid] = {"chrom": chrom, "pos": pos, "geno": geno}
    return {"format": "23andme", "header": header, "calls": calls, "nocall": nocall}


def parse_vcf(path: str) -> dict:
    header, calls = [], {}
    nocall = 0
    with _open(path) as fh:
        for line in fh:
            if line.startswith("##"):
                header.append(line.rstrip("\n"))
                continue
            if line.startswith("#CHROM"):
                header.append(line.rstrip("\n"))
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 10:
                continue
            chrom, pos, vid, ref, alt = parts[0], parts[1], parts[2], parts[3], parts[4]
            gt_field = parts[9].split(":")[0]
            alleles = [ref] + alt.split(",")
            if gt_field in (".", "./.", ".|."):
                nocall += 1
                geno = None
            else:
                idx = re.split(r"[/|]", gt_field)
                try:
                    geno = "".join(sorted(alleles[int(i)] for i in idx if i != "."))
                except (ValueError, IndexError):
                    geno = None
                    nocall += 1
            key = vid if vid.startswith("rs") else f"{chrom}:{pos}"
            calls[key] = {"chrom": chrom, "pos": pos, "geno": geno}
    return {"format": "vcf", "header": header, "calls": calls, "nocall": nocall}


def parse(path: str) -> dict:
    """Dispatch on content, not on the extension — extensions lie."""
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    with _open(path) as fh:
        head = [fh.readline() for _ in range(80)]
    blob = "".join(h for h in head if h)
    if not blob.strip():
        raise ValueError(f"{path}: file is empty")
    if "##fileformat=VCF" in blob or blob.startswith("##"):
        return parse_vcf(path)
    # A 23andMe-style body line: rsid, chromosome, integer position, genotype.
    for line in blob.splitlines():
        if line.startswith("#"):
            continue
        p = line.split("\t")
        if len(p) >= 4 and p[2].strip().isdigit():
            return parse_23andme(path)
    raise ValueError(f"{path}: not a recognised 23andMe-style or VCF format")


def strand_ambiguity(geno: str | None, site_alleles: set[str] | None = None) -> str:
    """Three-state strand-ambiguity assessment.

    Returns 'AMBIGUOUS', 'CLEAR', or 'UNDETERMINED'.

    **Ambiguity is a property of the SITE, not of the observed genotype.** A site whose two
    alleles are A/T or C/G is palindromic: reverse-complementing the pair returns the same pair,
    so orientation cannot be recovered from allele identity. That is true regardless of what this
    person's genotype happens to be.

    The consequence, and the reason this function is three-state rather than boolean: a
    *heterozygous* A/T call reveals the site is palindromic, so it can be flagged from the
    genotype alone. A *homozygous* call reveals nothing — `AA` could sit at an A/T site (where it
    is unresolvable, since the other strand reads TT) or at an A/G site (where it is fine). An
    earlier boolean version of this function returned False for `AA` and therefore silently passed
    the single most dangerous class of call in the file. Without the site's allele pair the honest
    answer is UNDETERMINED, not CLEAR.

    Pass `site_alleles` when the site's two alleles are known from an external reference; then the
    answer is definite either way.
    """
    if not geno:
        return "UNDETERMINED"
    observed = set(geno.upper())
    if site_alleles:
        pair = {a.upper() for a in site_alleles}
        return "AMBIGUOUS" if any(pair == amb for amb in AMBIGUOUS_PAIRS) else "CLEAR"
    if len(observed) == 2:
        # Heterozygous: the observed pair IS the site pair.
        return "AMBIGUOUS" if any(observed == amb for amb in AMBIGUOUS_PAIRS) else "CLEAR"
    # Homozygous, no site data: the site pair is unknown, so ambiguity cannot be ruled out.
    return "UNDETERMINED"


def apoe_diplotypes(rs429358: str | None, rs7412: str | None) -> dict:
    """Resolve APOE from two unphased genotypes.

    Unlike star alleles, APOE needs no phasing among the three common haplotypes: all six
    diplotypes are uniquely determined. Exactly one combination is formally ambiguous once the
    rare e1 haplotype is admitted, and this reports it rather than silently picking the likely
    answer. Verified by enumerating every haplotype pair.
    """
    if not rs429358 or not rs7412:
        return {"resolved": None, "candidates": [], "note": "one or both defining sites missing or no-called"}
    g1, g2 = set(rs429358.upper()), set(rs7412.upper())
    cands = []
    haps = sorted(APOE_HAP)
    for i, h1 in enumerate(haps):
        for h2 in haps[i:]:
            a, b = APOE_HAP[h1], APOE_HAP[h2]
            if {a[0], b[0]} == g1 and {a[1], b[1]} == g2:
                cands.append(f"{h1}/{h2}")
    if not cands:
        return {"resolved": None, "candidates": [],
                "note": "genotype combination matches no APOE haplotype pair — check strand orientation and build"}
    common = [c for c in cands if "e1" not in c]
    if len(cands) == 1:
        return {"resolved": cands[0], "candidates": cands, "note": "uniquely determined"}
    return {"resolved": common[0] if len(common) == 1 else None, "candidates": cands,
            "note": ("ambiguous: " + " or ".join(cands) +
                     f". {common[0]} is far more likely (e1 is rare) but phasing is required to exclude the alternative."
                     if common else "ambiguous")}


def concordance(a: dict, b: dict) -> dict:
    shared = set(a["calls"]) & set(b["calls"])
    comparable = [k for k in shared if a["calls"][k]["geno"] and b["calls"][k]["geno"]]
    agree = [k for k in comparable if set(a["calls"][k]["geno"]) == set(b["calls"][k]["geno"])]
    disagree = sorted(set(comparable) - set(agree))
    return {
        "shared_sites": len(shared),
        "comparable_sites": len(comparable),
        "concordant": len(agree),
        "discordant": len(disagree),
        "rate": (len(agree) / len(comparable)) if comparable else None,
        "discordant_examples": disagree[:20],
    }


def report(files: list[str], as_json: bool, catalog_only: bool) -> int:
    parsed = []
    for p in files:
        try:
            d = parse(p)
        except FileNotFoundError:
            print(f"Cannot read {p}: no such file.", file=sys.stderr); return 2
        except ValueError as e:
            print(str(e), file=sys.stderr); return 2
        d["path"] = p
        d["build"] = detect_build(d["header"])
        parsed.append(d)

    out = {"files": [], "catalog": {}, "apoe": {}, "concordance": None, "warnings": []}

    for d in parsed:
        total = len(d["calls"])
        entry = {
            "path": d["path"], "format": d["format"], "build": d["build"],
            "sites": total, "no_calls": d["nocall"],
            "no_call_rate": round(d["nocall"] / total, 6) if total else None,
            "chromosomes": len({c["chrom"] for c in d["calls"].values()}),
        }
        out["files"].append(entry)
        if d["build"] is None:
            out["warnings"].append(
                f"{d['path']}: genome build NOT declared in the file. Positions cannot be looked up "
                "safely. Determine the build from the provider before interpreting any position."
            )

    builds = {d["build"] for d in parsed if d["build"]}
    if len(builds) > 1:
        out["warnings"].append(
            f"Files declare DIFFERENT builds ({', '.join(sorted(builds))}). Do not compare positions "
            "across them without liftover; rsID-based comparison is safe, positional is not."
        )

    merged = {}
    for d in parsed:
        for rsid, c in d["calls"].items():
            if rsid in CATALOG and c["geno"]:
                merged.setdefault(rsid, []).append((d["path"], c["geno"]))
    for rsid, (gene, what) in CATALOG.items():
        hits = merged.get(rsid)
        if not hits:
            out["catalog"][rsid] = {"gene": gene, "site": what, "genotype": None,
                                    "status": "not present or no-called — the array may never have probed it"}
            continue
        genos = {g for _, g in hits}
        rec = {"gene": gene, "site": what, "genotype": sorted(genos)[0],
               "sources": [p for p, _ in hits]}
        if len({frozenset(g) for g in genos}) > 1:
            rec["status"] = f"DISCORDANT between files: {hits} — do not interpret until resolved"
        else:
            rec["status"] = "called"
        amb = strand_ambiguity(rec["genotype"])
        rec["strand"] = amb
        if amb == "AMBIGUOUS":
            rec["strand_note"] = ("PALINDROMIC site (A/T or C/G): reverse-complement returns the same "
                                  "allele pair, so orientation cannot be recovered from the genotype. "
                                  "Do not count risk alleles here until orientation is established.")
        elif amb == "UNDETERMINED":
            rec["strand_note"] = ("Homozygous call: this site's allele pair is not known to the script, "
                                  "so palindromic ambiguity cannot be ruled out. Check the site's "
                                  "alleles before interpreting.")
        out["catalog"][rsid] = rec

    g1 = out["catalog"].get("rs429358", {}).get("genotype")
    g2 = out["catalog"].get("rs7412", {}).get("genotype")
    out["apoe"] = apoe_diplotypes(g1, g2)

    if len(parsed) == 2:
        out["concordance"] = concordance(parsed[0], parsed[1])

    if as_json:
        print(json.dumps(out, indent=2))
        return 0

    print("=== Files ===")
    for e in out["files"]:
        print(f"  {e['path']}")
        print(f"    format {e['format']} · build {e['build'] or 'UNDECLARED'} · "
              f"{e['sites']} sites · {e['no_calls']} no-calls "
              f"({'' if e['no_call_rate'] is None else format(e['no_call_rate']*100, '.3f') + '%'}) · "
              f"{e['chromosomes']} chromosomes")
    if out["concordance"]:
        c = out["concordance"]
        rate = "n/a" if c["rate"] is None else f"{c['rate']*100:.3f}%"
        print("\n=== Cross-platform concordance ===")
        print(f"  shared {c['shared_sites']} · comparable {c['comparable_sites']} · "
              f"concordant {c['concordant']} · discordant {c['discordant']} · rate {rate}")
        if c["discordant_examples"]:
            print(f"  discordant examples: {', '.join(c['discordant_examples'])}")
    print("\n=== Catalogued sites ===")
    for rsid, r in out["catalog"].items():
        if catalog_only and r.get("genotype") is None:
            continue
        print(f"  {rsid:<12} {r['gene']:<10} {str(r.get('genotype') or '--'):<4} {r['status']}")
        if "strand_note" in r:
            print(f"               ^ [{r['strand']}] {r['strand_note']}")
    print("\n=== APOE ===")
    a = out["apoe"]
    print(f"  diplotype: {a['resolved'] or 'unresolved'} · {a['note']}")
    if out["warnings"]:
        print("\n=== Warnings ===")
        for w in out["warnings"]:
            print(f"  ! {w}")
    print("\nThis output is what the DATA says. It assigns no risk and no pathogenicity, and")
    print("recommends nothing. Interpretation belongs to the skill's references.")
    return 3 if any("build NOT declared" in w for w in out["warnings"]) else 0


# --------------------------------------------------------------------------------------
# Offline self-test
# --------------------------------------------------------------------------------------
def self_test() -> int:
    import tempfile
    failures: list[str] = []
    total = 0

    def check(name: str, cond: bool) -> None:
        nonlocal total
        total += 1
        if not cond:
            failures.append(name)

    # --- APOE algebra. The reason this function exists is the ambiguity case, so assert it. ---
    check("APOE e3/e3", apoe_diplotypes("TT", "CC")["resolved"] == "e3/e3")
    check("APOE e4/e4", apoe_diplotypes("CC", "CC")["resolved"] == "e4/e4")
    check("APOE e2/e2", apoe_diplotypes("TT", "TT")["resolved"] == "e2/e2")
    check("APOE e2/e3", apoe_diplotypes("TT", "CT")["resolved"] == "e2/e3")
    check("APOE e3/e4", apoe_diplotypes("CT", "CC")["resolved"] == "e3/e4")
    amb = apoe_diplotypes("CT", "CT")
    check("APOE double-het is flagged ambiguous", set(amb["candidates"]) == {"e1/e3", "e2/e4"})
    check("APOE double-het still names the likely answer", amb["resolved"] == "e2/e4")
    check("APOE double-het note says phasing", "phasing" in amb["note"].lower())
    # Negative control: a combination matching no haplotype pair must NOT silently resolve.
    check("APOE impossible combination rejected",
          apoe_diplotypes("AA", "GG")["resolved"] is None)
    check("APOE missing site rejected", apoe_diplotypes(None, "CC")["resolved"] is None)
    # Order independence: genotype strings may arrive in either allele order.
    check("APOE genotype order independent",
          apoe_diplotypes("TC", "CC")["resolved"] == apoe_diplotypes("CT", "CC")["resolved"])

    # --- Build detection. Must never guess. ---
    check("build GRCh37 from hg19", detect_build(["# build 37, hg19 coordinates"]) == "GRCh37/hg19")
    check("build GRCh38", detect_build(["##reference=GRCh38"]) == "GRCh38")
    check("build undeclared returns None", detect_build(["# some unrelated comment"]) is None)
    check("build undeclared on empty header", detect_build([]) is None)

    # --- Strand ambiguity. Three-state, because ambiguity is a property of the SITE. ---
    check("het A/T is AMBIGUOUS", strand_ambiguity("AT") == "AMBIGUOUS")
    check("het C/G is AMBIGUOUS", strand_ambiguity("CG") == "AMBIGUOUS")
    check("allele order irrelevant", strand_ambiguity("GC") == "AMBIGUOUS")
    check("het A/G is CLEAR", strand_ambiguity("AG") == "CLEAR")
    check("None is UNDETERMINED", strand_ambiguity(None) == "UNDETERMINED")
    # REGRESSION, and the reason this function was rewritten: a boolean version returned False
    # for a homozygous call, silently passing the most dangerous class of site in the file.
    # A homozygote carries no information about the site's allele pair.
    check("homozygous AA is UNDETERMINED, not CLEAR", strand_ambiguity("AA") == "UNDETERMINED")
    check("homozygous CC is UNDETERMINED, not CLEAR", strand_ambiguity("CC") == "UNDETERMINED")
    check("homozygous GG is UNDETERMINED, not CLEAR", strand_ambiguity("GG") == "UNDETERMINED")
    # With the site's alleles supplied the answer is definite either way, for any genotype.
    check("homozygote at a known A/T site is AMBIGUOUS",
          strand_ambiguity("AA", {"A", "T"}) == "AMBIGUOUS")
    check("homozygote at a known A/G site is CLEAR",
          strand_ambiguity("AA", {"A", "G"}) == "CLEAR")
    check("het at a known C/G site is AMBIGUOUS",
          strand_ambiguity("CG", {"C", "G"}) == "AMBIGUOUS")
    check("site data overrides the genotype heuristic",
          strand_ambiguity("AT", {"A", "T"}) == "AMBIGUOUS")

    with tempfile.TemporaryDirectory() as td:
        # --- 23andMe parsing, including a no-call and a lost-'#' header line ---
        p23 = os.path.join(td, "genome.txt")
        with open(p23, "w") as fh:
            fh.write("# This data file generated by a provider\n")
            fh.write("# build 37\n")
            fh.write("rsid\tchromosome\tposition\tgenotype\n")
            fh.write("rs429358\t19\t45411941\tTT\n")
            fh.write("rs7412\t19\t45412079\tCC\n")
            fh.write("rs6025\t1\t169519049\tGG\n")
            fh.write("rs1801133\t1\t11856378\t--\n")
            fh.write("rs671\t12\t112241766\tGG\n")
        d = parse(p23)
        check("23andme format detected", d["format"] == "23andme")
        check("23andme build read", detect_build(d["header"]) == "GRCh37/hg19")
        check("23andme counts sites", len(d["calls"]) == 5)
        check("23andme counts no-calls", d["nocall"] == 1)
        check("23andme no-call stored as None", d["calls"]["rs1801133"]["geno"] is None)
        check("23andme skips the unprefixed column header", "rsid" not in d["calls"])

        # --- VCF parsing: phased and unphased separators, multi-allelic, missing GT ---
        pvcf = os.path.join(td, "s.vcf")
        with open(pvcf, "w") as fh:
            fh.write("##fileformat=VCFv4.2\n")
            fh.write("##reference=GRCh38\n")
            fh.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tS1\n")
            fh.write("19\t44908684\trs429358\tT\tC\t.\tPASS\t.\tGT\t0/1\n")
            fh.write("19\t44908822\trs7412\tC\tT\t.\tPASS\t.\tGT\t0|0\n")
            fh.write("1\t169519049\trs6025\tG\tA\t.\tPASS\t.\tGT\t./.\n")
            fh.write("12\t111803962\trs671\tG\tA,C\t.\tPASS\t.\tGT\t1/2\n")
        v = parse(pvcf)
        check("vcf format detected", v["format"] == "vcf")
        check("vcf build read", detect_build(v["header"]) == "GRCh38")
        check("vcf het call", set(v["calls"]["rs429358"]["geno"]) == {"C", "T"})
        check("vcf phased separator handled", v["calls"]["rs7412"]["geno"] == "CC")
        check("vcf missing GT is a no-call", v["calls"]["rs6025"]["geno"] is None)
        check("vcf no-call counted", v["nocall"] == 1)
        check("vcf multi-allelic resolved", set(v["calls"]["rs671"]["geno"]) == {"A", "C"})

        # --- Concordance, including a planted disagreement (negative control) ---
        pb = os.path.join(td, "other.txt")
        with open(pb, "w") as fh:
            fh.write("# build 37\n")
            fh.write("rs429358\t19\t45411941\tTT\n")   # agrees
            fh.write("rs7412\t19\t45412079\tCC\n")     # agrees
            fh.write("rs6025\t1\t169519049\tAG\n")     # DISAGREES with GG above
        c = concordance(parse(p23), parse(pb))
        check("concordance finds shared sites", c["shared_sites"] == 3)
        check("concordance counts agreements", c["concordant"] == 2)
        check("concordance catches the planted disagreement", c["discordant"] == 1)
        check("concordance names the discordant site", c["discordant_examples"] == ["rs6025"])
        check("concordance rate computed", abs(c["rate"] - 2 / 3) < 1e-9)

        # --- Format rejection: must fail loudly, not parse garbage into findings ---
        bad = os.path.join(td, "bad.csv")
        with open(bad, "w") as fh:
            fh.write("name,age\nalice,30\nbob,40\n")
        try:
            parse(bad); check("garbage input rejected", False)
        except ValueError:
            check("garbage input rejected", True)
        empty = os.path.join(td, "empty.txt")
        open(empty, "w").close()
        try:
            parse(empty); check("empty input rejected", False)
        except ValueError:
            check("empty input rejected", True)

        # --- An undeclared build must surface as a warning and a non-zero exit ---
        nob = os.path.join(td, "nobuild.txt")
        with open(nob, "w") as fh:
            fh.write("# provider export\nrs6025\t1\t169519049\tGG\n")
        d2 = parse(nob)
        check("undeclared build detected as None", detect_build(d2["header"]) is None)

    print(f"self-test: {total - len(failures)}/{total} checks passed")
    for f in failures:
        print(f"  FAILED: {f}")
    if failures:
        return 1
    print("all offline logic checks passed")
    return 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", help="one or two raw data files (23andMe-style or VCF)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--catalog-only", action="store_true",
                    help="omit catalogued sites that were absent or no-called")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.files:
        ap.error("provide one or two raw data files (or --self-test)")
    if len(args.files) > 2:
        ap.error("at most two files")
    return report(args.files, args.json, args.catalog_only)


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        sys.exit(130)
