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
# Third element is the site's allele pair where it has been VERIFIED against a retrieved record,
# else None. Supplying it lets strand_ambiguity() be definitive for a homozygous call, which it
# cannot otherwise be (see that function's docstring). None means "not verified" — never guessed,
# because a wrong allele pair would turn a correct CLEAR into a wrong AMBIGUOUS or vice versa.
# ALLELE-PAIR CONVENTION. Pairs are given on the **dbSNP plus strand**, which is what consumer
# arrays emit — because the whole point of carrying a pair is settling orientation, so an
# inconsistent convention here would be worse than carrying no pair at all. Two entries below are
# labelled in **cDNA** orientation (`C677T`, `-13910C>T`) for genes transcribed from the minus
# strand; the *label* is cDNA and the *pair* must be plus-strand, and those two are flagged inline
# as needing confirmation against dbSNP. **Where a pair is not confirmed, it is `None`** — the
# script then reports UNDETERMINED, which is a statement about this catalogue rather than about the
# site. A wrong pair is worse than `None`.
#
# This catalogue is a deliberate SUBSET of references/variant-catalog.md: single-SNP sites a
# consumer file plausibly contains. RYR1/CACNA1S, MT-RNR1, the HLA alleles and the BRCA founder
# variants are not here and must be looked up by hand.
CATALOG = {
    "rs429358": ("APOE", "APOE haplotype-defining site (Cys112Arg)", {"T", "C"}),
    "rs7412":   ("APOE", "APOE haplotype-defining site (Arg158Cys)", {"C", "T"}),
    # HFE H63D is c.187C>G -> a C/G site, therefore PALINDROMIC. It sits in the actionable tier,
    # so this is exactly the combination the skill warns about: high stakes, unresolvable strand.
    "rs1799945": ("HFE", "HFE H63D (c.187C>G — palindromic site)", {"C", "G"}),
    "rs1800562": ("HFE", "HFE C282Y (c.845G>A)", {"G", "A"}),
    "rs6025":    ("F5", "Factor V Leiden", None),
    # cDNA-labelled, minus-strand gene: the C/T pair below is the cDNA orientation and is NOT
    # confirmed plus-strand, so it is withheld rather than asserted. Neither orientation is
    # palindromic, so no current verdict changes — this is a latent trap, not a live one.
    "rs1801133": ("MTHFR", "MTHFR C677T (cDNA label; plus-strand pair unconfirmed) — see the MTHFR corrective before interpreting", None),
    "rs1801131": ("MTHFR", "MTHFR A1298C — see the MTHFR corrective before interpreting", None),
    "rs671":     ("ALDH2", "ALDH2 Glu504Lys (c.1510G>A)", {"G", "A"}),
    # Same situation as rs1801133: cDNA label, minus-strand gene, pair withheld pending dbSNP.
    "rs4988235": ("MCM6/LCT", "lactase persistence regulatory variant (-13910C>T, cDNA label; plus-strand pair unconfirmed)", None),
    "rs762551":  ("CYP1A2", "CYP1A2 -163C>A", None),
    # FTO rs9939609 is an A/T site (A is the risk allele relative to T) -> PALINDROMIC.
    "rs9939609": ("FTO", "FTO intron 1 (A/T — palindromic site)", {"A", "T"}),
    "rs4149056": ("SLCO1B1", "SLCO1B1 *5 (Val174Ala)", None),
    "rs4244285": ("CYP2C19", "CYP2C19 *2", None),
    "rs4986893": ("CYP2C19", "CYP2C19 *3", None),
    "rs12248560": ("CYP2C19", "CYP2C19 *17", None),
    "rs1799853": ("CYP2C9", "CYP2C9 *2", None),
    "rs1057910": ("CYP2C9", "CYP2C9 *3", None),
    "rs9923231": ("VKORC1", "VKORC1 -1639G>A", None),
    "rs3892097": ("CYP2D6", "CYP2D6 *4 tag — NOT sufficient to call a CYP2D6 diplotype", None),
    "rs1800460": ("TPMT", "TPMT *3B", None),
    "rs1142345": ("TPMT", "TPMT *3C", None),
    "rs116855232": ("NUDT15", "NUDT15 *3", None),
    "rs3918290": ("DPYD", "DPYD *2A", None),
    # Added after a cross-file audit found these named in the references but absent from the funnel.
    "rs776746":  ("CYP3A5", "CYP3A5 *3 — the cleanest array-callable PGx site; ancestry changes what it means", None),
    "rs1800462": ("TPMT", "TPMT *2 — a further no-function allele; omitting it understates how little a negative means", None),
    "rs2108622": ("CYP4F2", "CYP4F2 V433M — feeds warfarin dosing algorithms alongside CYP2C9/VKORC1", None),
    "rs12777823": ("CYP2C-cluster", "warfarin dose-associated variant of particular relevance in African ancestry", None),
    "rs601338":  ("FUT2", "FUT2 secretor status — changes how a serum B12 level is interpreted, not the requirement", None),
    "rs1050828": ("G6PD", "G6PD A- (V68M) — X-LINKED: a heterozygous female is a mosaic and a genotype cannot resolve her activity", None),
    "rs1050829": ("G6PD", "G6PD A (N126D) — X-LINKED, read with rs1050828; enzyme activity is the better test and is still not definitive", None),
}

AMBIGUOUS_PAIRS = ({"A", "T"}, {"C", "G"})

# APOE haplotypes as (rs429358, rs7412). e1 is rare but must be modelled: it is the sole
# reason one genotype combination is ambiguous.
APOE_HAP = {"e1": ("C", "T"), "e2": ("T", "T"), "e3": ("T", "C"), "e4": ("C", "C")}

# The two APOE sites are c.388 and c.526, both in exon 4 with no intron between them, so they sit
# 526 - 388 = 138 bp apart in every build. The spacing is therefore a free, build-independent
# consistency check on a file's own coordinates — unlike the absolute positions, which must be read
# from the file's header and never assumed.
APOE_SITE_GAP_BP = 138

# A gVCF reference block records "no variant called across this interval". It is not a genotype.
SYMBOLIC_REF_ALTS = ("<NON_REF>", "<*>")


def _norm_geno(geno: str | None) -> str | None:
    """Normalise a genotype to a sorted allele string, dropping VCF phase separators.

    Sorting makes "AG" and "GA" the same genotype, which is correct. It deliberately does NOT
    collapse ploidy: "C" stays one character and "CC" stays two, so a half-call can never be
    mistaken for a homozygote downstream.
    """
    if not geno:
        return None
    g = re.sub(r"[/|]", "", geno.strip().upper())
    return "".join(sorted(g)) if g else None


def _norm_chrom(c) -> str:
    """Normalise a chromosome label, so "chr1", "1" and "CHR1" are one chromosome.

    Positional matching between two files that use different conventions finds nothing, and
    finding nothing looks exactly like two files with no sites in common.
    """
    s = str(c).strip()
    if s.lower().startswith("chr"):
        s = s[3:]
    s = s.upper()
    return "MT" if s in ("M", "MT") else s


def read_header(path: str) -> list[str]:
    """Read the leading comment block only — enough to detect the build without parsing a body.

    The build has to be known *before* the body is read, because it decides whether positions from
    one file may be used to key another, and a whole-genome body is the thing worth not reading
    twice.

    Collects exactly what `parse_vcf` collects — `##` metadata and the `#CHROM` line — and
    nothing else. It used to take every line beginning with a single `#`, so a stray `#build 37`
    comment was visible to the build GATE and invisible to the build the report PRINTS: positional
    keying then ran against a build the same report called undeclared. One definition, one answer.
    """
    out = []
    with _open(path) as fh:
        for line in fh:
            if not line.startswith("#"):
                break
            if line.startswith("##") or line.startswith("#CHROM"):
                out.append(line.rstrip("\n"))
    return out


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
    nocall = total = 0
    chroms = set()
    duplicated: set[str] = set()
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
            total += 1
            chroms.add(_norm_chrom(chrom))
            # A duplicated rsID is not just a counting problem: the LAST row used to win, so a
            # stray second row published ITS coordinate as that rsID's position, and any VCF
            # record sitting at that bogus coordinate was then reported as the catalogued site's
            # genotype — while the array's own real call for the rsID had been overwritten, so
            # nothing was left to raise DISCORDANT. Keep the FIRST row and record the conflict;
            # `position_index` withholds the rsID entirely.
            if rsid in calls:
                duplicated.add(rsid)
                continue
            if not geno or set(geno) <= {"-", "0", "."}:
                nocall += 1
                calls[rsid] = {"chrom": chrom, "pos": pos, "geno": None}
                continue
            calls[rsid] = {"chrom": chrom, "pos": pos, "geno": geno}
    return {"format": "23andme", "header": header, "calls": calls, "nocall": nocall,
            "sites": total, "chrom_count": len(chroms), "retained": len(calls),
            "restricted": False, "duplicated_rsids": duplicated}


SNV_ALLELES = set("ACGT")


def position_index(d: dict) -> dict:
    """Map (chromosome, position) → rsID using the coordinates a file carries itself.

    The coordinates come from the data, never from this script. Asserting a catalogued variant's
    coordinates from memory is the exact fabrication this audit exists to catch, and a position
    quoted in the wrong build silently returns a different variant. A position claimed by two
    different rsIDs is dropped rather than guessed at.
    """
    idx, dropped = {}, set()
    conflicted = d.get("duplicated_rsids") or set()
    for rsid, c in d["calls"].items():
        if not rsid.startswith("rs") or not str(c["pos"]).strip().isdigit():
            continue
        if rsid in conflicted:
            continue   # the file disagreed with itself about this rsID; its coordinate is unusable
        k = (_norm_chrom(c["chrom"]), str(c["pos"]).strip())
        if k in idx and idx[k] != rsid:
            dropped.add(k)
        idx[k] = rsid
    for k in dropped:
        idx.pop(k, None)
    return idx


def _vcf_key(chrom, pos, vid, ref, alt, pos_index):
    """Resolve the key a VCF record is filed under, and report how it was resolved.

    An rsID when the file carries one. Otherwise a position, but **only** when another file has
    supplied a (chromosome, position) → rsID map drawn from its own rows and declaring the same
    build. Otherwise "chrom:pos", which matches nothing in the catalogue — correctly, because
    nothing has identified it.

    This matters because a sequencing provider's VCF often ships with `ID` as `.`, and a catalogue
    keyed on rsIDs then matches zero records: every finding reads as absent for a reason of
    annotation rather than of biology.

    Positional resolution is restricted to SNV-shaped records. An indel, a symbolic allele or a
    spanning deletion at a catalogued SNP's position is not that SNP, and comparing its genotype
    against an array call would manufacture a discordance at the one site someone is reading.
    A gVCF's `<NON_REF>` is stripped before that test rather than disqualifying the record, since
    in a gVCF every record carries it, real variant calls included.

    The ID field is a **semicolon-separated list** in VCF 4.x — dbSNP emits merged rsIDs that way
    — so it is split rather than used verbatim. Used verbatim, `rs1800562;rs2071303` matched no
    catalogue entry and the site read as *absent* while still counting as annotated, which
    suppressed both the nothing-keyable gate and the positional fallback: a present homozygous
    variant reported as not present, with the file certified as fully annotated.
    """
    for part in str(vid).split(";"):
        part = part.strip()
        if part.startswith("rs"):
            return part, "rsid"
    if pos_index:
        # Strip symbolic alts (gVCF <NON_REF>, <*>) before judging the shape; a spanning
        # deletion '*' is not a base and must still disqualify.
        alts = [a for a in alt.split(",") if a not in SYMBOLIC_REF_ALTS]
        if (alts and len(ref) == 1 and ref.upper() in SNV_ALLELES
                and all(len(a) == 1 and a.upper() in SNV_ALLELES for a in alts)):
            hit = pos_index.get((_norm_chrom(chrom), str(pos).strip()))
            if hit:
                return hit, "position"
    # The coordinate fallback is the one chromosome string that used to skip normalisation, so
    # two files labelling chromosomes differently ("chr1" vs "1") shared no coordinate keys at
    # all — which silently emptied the identity gate while the normalised chromosome COUNT shown
    # in the report looked identical.
    return f"{_norm_chrom(chrom)}:{str(pos).strip()}", "coordinate"


def vcf_keys(path: str, pos_index: dict | None = None, within: set | None = None) -> set:
    """Key-only pass over a VCF: the identifiers, none of the records.

    Comparing two whole-genome VCFs needs each file's site list, and holding both files' records
    to get it is the cost the restriction in `report` exists to avoid. `within` narrows the pass
    to an already-known key set, so the second file's pass costs the intersection rather than the
    genome.
    """
    out = set()
    with _open(path) as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 10:
                continue
            key, _ = _vcf_key(parts[0], parts[1], parts[2], parts[3], parts[4], pos_index)
            if within is None or key in within:
                out.add(key)
    return out


def parse_vcf(path: str, keep: set | None = None, pos_index: dict | None = None) -> dict:
    """Read a VCF, keeping the distinction between a genotype and the absence of one.

    Three VCF-specific traps are handled here because each one turns absence into a confident
    call downstream:

    - **Variants-only vs all-sites.** A variants-only file has no line at a reference site, so
      "homozygous reference" and "never covered" are the same observation: nothing. The file kind
      is recorded so the report can say that instead of reading absence as reference.
    - **Reference blocks.** A gVCF block (symbolic `<NON_REF>`/`<*>` ALT, or an `END=` interval)
      asserts that no variant was called across a span. It is not a genotype at any position
      inside it, so no genotype is taken from one.
    - **Zero depth.** A pipeline can emit `0/0` with `DP=0`. A call with no supporting reads is
      no information, and is discarded rather than counted as a reference call.

    `keep` bounds what is held in memory. Measured on HaplotypeCaller-shaped records, a retained
    record costs 537 bytes and the cost is linear in record count, so a 30x whole-genome VCF's
    4-6 million records is 2-3 GB resident before a single line of interpretation — on many
    machines that is the difference between an audit and an OOM kill. Nothing downstream reads
    `calls` at an arbitrary key: the catalogue, the APOE pair and the other file's sites are the
    whole demand, so restricting retention to that union changes no reported number. The counters
    below are still taken over **every** record, because the quality pass describes the file and
    not the retained subset.
    """
    header, calls = [], {}
    nocall = ref_blocks = zero_depth = 0
    total = rsid_records = pos_matched = sites_only = collapsed = 0
    chroms = set()
    samples: list[str] = []
    all_sites = False
    with _open(path) as fh:
        for line in fh:
            if line.startswith("##") or line.startswith("#CHROM"):
                header.append(line.rstrip("\n"))
                if line.startswith("#CHROM"):
                    # Columns 10+ are samples. parse_vcf reads column 10 and only column 10, so a
                    # trio or family VCF would otherwise produce a confident report attributed to
                    # "this file" while silently discarding two other people's genotypes — at a
                    # locus someone is about to act on. Count them and refuse downstream.
                    samples = line.rstrip("\n").split("\t")[9:]
                continue
            parts = line.rstrip("\n").split("\t")
            # A sites-only VCF (8 columns, no FORMAT/sample) carries no genotypes, but it DOES
            # carry records. Skipping it wholesale reported "0 sites, 0 chromosomes, NO dbSNP
            # rsIDs (0 of 0 records)" for a fully annotated file — three false statements.
            if len(parts) < 8:
                continue
            chrom, pos, vid, ref, alt, info = parts[0], parts[1], parts[2], parts[3], parts[4], parts[7]
            total += 1
            if len(parts) < 10:
                sites_only += 1
                chroms.add(_norm_chrom(chrom))
                for part in str(vid).split(";"):
                    if part.strip().startswith("rs"):
                        rsid_records += 1
                        break
                continue
            chroms.add(_norm_chrom(chrom))
            if any(p.strip().startswith("rs") for p in str(vid).split(";")):
                rsid_records += 1
            field = dict(zip(parts[8].split(":"), parts[9].split(":")))
            gt_field = field.get("GT", ".")
            dp = int(field["DP"]) if field.get("DP", "").isdigit() else None
            key, keyed_by = _vcf_key(chrom, pos, vid, ref, alt, pos_index)
            if keyed_by == "position":
                pos_matched += 1
            wanted = keep is None or key in keep
            rec = {"chrom": chrom, "pos": pos, "geno": None, "ploidy": None, "dp": dp,
                   "keyed_by": keyed_by}

            # In a GATK gVCF **every** record's ALT carries <NON_REF>, real variant calls
            # included ("A,<NON_REF>" with GT 0/1). A substring test therefore classified called
            # heterozygotes and homozygous-alts at catalogued sites as reference blocks and threw
            # their genotypes away, so the catalogue row read as absent with exit 0. A record is a
            # reference block only when the symbolic allele is the ONLY alt.
            alt_set = {a.strip() for a in alt.split(",")}
            if alt_set <= set(SYMBOLIC_REF_ALTS) | {".", ""} or "END=" in info:
                all_sites = True
                ref_blocks += 1
                rec["kind"] = "reference-block"
                rec["note"] = ("reference block, not a site call: homozygous-reference cannot be "
                               "asserted at a catalogued position from a block record")
                if wanted:
                    calls[key] = rec
                continue
            if gt_field in (".", "./.", ".|."):
                nocall += 1
                rec["kind"] = "no-call"
                if wanted:
                    calls[key] = rec
                continue
            alleles = [ref] + alt.split(",")
            idx = [i for i in re.split(r"[/|]", gt_field) if i != "."]
            try:
                obs = sorted(alleles[int(i)] for i in idx)
            except (ValueError, IndexError):
                nocall += 1
                rec["kind"] = "unparseable-GT"
                if wanted:
                    calls[key] = rec
                continue
            if not obs:
                nocall += 1
                rec["kind"] = "no-call"
                if wanted:
                    calls[key] = rec
                continue
            if dp == 0:
                zero_depth += 1
                rec["kind"] = "zero-depth"
                rec["note"] = ("a genotype was emitted with DP=0 — no supporting reads, therefore no "
                               "information, and not a reference call")
                if wanted:
                    calls[key] = rec
                continue
            rec["geno"] = "".join(obs)
            rec["ploidy"] = len(obs)
            rec["kind"] = "call" if len(obs) == 2 else "non-diploid call"
            if wanted:
                # A `bcftools norm -m-` pipeline emits one ALT per line, so several records can
                # land on one key. The last used to win silently, which made the reported
                # genotype depend on LINE ORDER — at APOE that fabricated a diplotype the
                # pre-restriction code had correctly reported as absent. Collapse is treated the
                # way cross-file disagreement is: no genotype survives it.
                prior = calls.get(key)
                if prior is not None and prior.get("geno") and prior["geno"] != rec["geno"]:
                    collapsed += 1
                    prior["geno"] = None
                    prior["ploidy"] = None
                    prior["kind"] = "multi-record-unresolved"
                    prior["note"] = (
                        "two or more records in this file resolve to this same site with "
                        "different genotypes (split multi-allelic records, or a duplicate "
                        "position). No genotype is taken: which one 'wins' would depend on line "
                        "order. Re-run against a VCF normalised with `bcftools norm -m+`")
                    continue
                calls[key] = rec
    return {"format": "vcf", "header": header, "calls": calls, "nocall": nocall,
            "ref_blocks": ref_blocks, "zero_depth": zero_depth,
            "vcf_kind": "gvcf-or-all-sites" if all_sites else "variants-only",
            "sites": total, "chrom_count": len(chroms), "rsid_records": rsid_records,
            "pos_matched": pos_matched, "retained": len(calls), "restricted": keep is not None,
            "samples": samples, "sites_only": sites_only, "collapsed": collapsed}


def sniff(path: str) -> str:
    """Decide the format from content, not from the extension — extensions lie.

    Separated from `parse` so the caller can learn what a file is before reading its body: the
    array files have to be parsed first to supply the position map and the key set that bound the
    sequencing file's parse.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    with _open(path) as fh:
        head = [fh.readline() for _ in range(80)]
    blob = "".join(h for h in head if h)
    if not blob.strip():
        raise ValueError(f"{path}: file is empty")
    if "##fileformat=VCF" in blob or blob.startswith("##"):
        return "vcf"
    # A 23andMe-style body line: rsid, chromosome, integer position, genotype.
    for line in blob.splitlines():
        if line.startswith("#"):
            continue
        p = line.split("\t")
        if len(p) >= 4 and p[2].strip().isdigit():
            return "23andme"
    raise ValueError(f"{path}: not a recognised 23andMe-style or VCF format")


def parse(path: str, keep: set | None = None, pos_index: dict | None = None) -> dict:
    """Dispatch on content, not on the extension — extensions lie."""
    if sniff(path) == "vcf":
        return parse_vcf(path, keep=keep, pos_index=pos_index)
    return parse_23andme(path)


def strand_ambiguity(geno: str | None, site_alleles: set[str] | None = None) -> str:
    """Three-state assessment of whether a call's RISK-ALLELE DOSAGE survives a strand flip.

    Returns 'AMBIGUOUS', 'CLEAR', or 'UNDETERMINED'.

    **Two different things get conflated here, and an earlier version of this function conflated
    them in the direction that suppresses real findings.**

    - *Unorientability* is a property of the SITE. A site whose alleles are A/T or C/G is
      palindromic: reverse-complementing the pair returns the same pair, so allele identity alone
      cannot say which strand the file is reporting.
    - *Ambiguity of a CALL* is a property of the (site, genotype) pair, and it is what actually
      matters, because what gets interpreted is a **dosage**.

    Work it through at a C/G site where C is the risk allele. A **heterozygous** `CG` call carries
    one copy of each allele; flip the strand and the C reads as G and the G reads as C — still one
    copy each, so **the dosage is 1 under either orientation and the call is CLEAR.** A
    **homozygous** `CC` call is 2 copies on one orientation and 0 on the other, so it is genuinely
    **AMBIGUOUS**.

    So: any two-allele heterozygous call is dosage-invariant. A homozygous call is AMBIGUOUS at a
    known palindromic site, CLEAR at a known non-palindromic one, and UNDETERMINED when the site's
    allele pair is not known — because then palindromy cannot be ruled out.

    (A previous version returned AMBIGUOUS for *every* call at a palindromic site once the pair was
    supplied, which told the reader not to count a heterozygote that was never in doubt. The
    version before that had the opposite defect, returning "not ambiguous" for a homozygote. Both
    directions are errors, and only one of them is loud.)

    Pass `site_alleles` when the site's two alleles are known from an external reference.
    """
    g = _norm_geno(geno)
    if not g or set(g) <= {"-", ".", "0"}:
        return "UNDETERMINED"
    observed = set(g)
    if len(g) == 2 and len(observed) == 2:
        # Heterozygous: one copy of each allele, which no strand flip can change.
        return "CLEAR"
    if site_alleles:
        pair = {a.upper() for a in site_alleles}
        return "AMBIGUOUS" if any(pair == amb for amb in AMBIGUOUS_PAIRS) else "CLEAR"
    # Homozygous or non-diploid, with no external allele pair: palindromy cannot be ruled out.
    return "UNDETERMINED"


def site_is_palindromic(site_alleles: set[str] | None) -> bool | None:
    """True / False / None (unknown) for the SITE's orientability, independent of any genotype."""
    if not site_alleles:
        return None
    pair = {a.upper() for a in site_alleles}
    return any(pair == amb for amb in AMBIGUOUS_PAIRS)


def apoe_diplotypes(rs429358: str | None, rs7412: str | None) -> dict:
    """Resolve APOE from two unphased genotypes.

    Unlike star alleles, APOE needs no phasing among the three common haplotypes: all six
    diplotypes are uniquely determined. Exactly one combination is formally ambiguous once the
    rare e1 haplotype is admitted, and this reports it rather than silently picking the likely
    answer. Verified by enumerating every haplotype pair.

    Ploidy is validated before anything else. An earlier version compared `set(geno)`, and
    set("C") == set("CC"), so a half-call or a truncated field was read as a homozygote and
    returned a confident **e4/e4** — the most consequential call this script makes, fabricated
    from a single observed allele. Anything that is not a two-allele diploid call is refused.
    """
    out: dict = {"resolved": None, "candidates": [], "note": ""}
    if not rs429358 or not rs7412:
        out["note"] = "one or both defining sites missing or no-called"
        return out

    norm = {}
    for site, raw in (("rs429358", rs429358), ("rs7412", rs7412)):
        g = _norm_geno(raw)
        if g is None or set(g) <= {"-", ".", "0"}:
            out["note"] = f"{site} is a no-call — APOE cannot be called, and absence is not a genotype"
            return out
        if len(g) != 2:
            out["note"] = (f"{site} is not a diploid call ({raw!r}): APOE cannot be resolved from one "
                           "observed allele, and reading one allele as a homozygote is exactly how a "
                           "false e4/e4 gets reported. Establish the genotype before interpreting.")
            return out
        if not set(g) <= {"T", "C"}:
            out["note"] = (f"{site} carries {sorted(set(g))}. Both APOE sites are T/C, and the "
                           "complement set A/G is disjoint from it — so a strand flip here is "
                           "DETECTABLE rather than ambiguous. This is a parsing, mapping or "
                           "strand-handling error, not a genotype, and it is refused rather than "
                           "complemented into something plausible.")
            return out
        norm[site] = g

    g1, g2 = set(norm["rs429358"]), set(norm["rs7412"])
    cands = []
    haps = sorted(APOE_HAP)
    for i, h1 in enumerate(haps):
        for h2 in haps[i:]:
            a, b = APOE_HAP[h1], APOE_HAP[h2]
            if {a[0], b[0]} == g1 and {a[1], b[1]} == g2:
                cands.append(f"{h1}/{h2}")
    out["candidates"] = cands
    if not cands:
        out["note"] = ("genotype combination matches no APOE haplotype pair — check that both calls "
                       "come from the intended sites and the intended build")
        return out

    common = [c for c in cands if "e1" not in c]
    if len(cands) == 1:
        out["resolved"] = cands[0]
        if common:
            out["note"] = "uniquely determined"
        else:
            # Formally unique, but only because e1 was admitted. e1 is rare, so the likelier
            # explanation of such an observation is an error at one of the two sites.
            out["note"] = (f"{cands[0]} is the only diplotype consistent with these calls, but it "
                           "invokes the rare e1 haplotype. A genotyping error at one of the two "
                           "sites is the more likely explanation — re-check both calls rather than "
                           "reporting a confident rare diplotype.")
            out["caution"] = "rare-haplotype-or-genotyping-error"
        return out

    out["resolved"] = common[0] if len(common) == 1 else None
    out["note"] = ("ambiguous: " + " or ".join(cands) +
                   (f". {common[0]} is far more likely (e1 is rare) but phasing is required to "
                    "exclude the alternative." if len(common) == 1 else ""))
    return out


AUTOSOMES = {str(i) for i in range(1, 23)}   # compared against _norm_chrom(), never a raw label

# Thresholds for the identity gate below. These are heuristics with a stated basis, not published
# cut-offs: consumer genotyping error rates run well under one percent, while the
# opposite-homozygote rate between two *unrelated* people is a few percent — a gap of roughly an
# order of magnitude, which is what makes the test usable at all. The minimum-sites floor matters
# more than the rate: a handful of overlapping sites cannot support any verdict.
IDENTITY_MIN_SITES = 1000
IDENTITY_FAIL_RATE = 0.01
IDENTITY_SUSPECT_RATE = 0.001


def _comparable_keys(a: dict, b: dict, allow_coordinates: bool) -> tuple[set, dict]:
    """The keys two files may legitimately be compared at, and why the others were excluded.

    A key of the form "chrom:pos" **identifies nothing**: it is a coordinate, and a coordinate only
    names the same locus in two files when both declare the same build. Intersecting coordinate
    keys across builds compared GRCh37 loci against GRCh38 loci and fed the result to the identity
    gate — in both directions. One person's two files were declared a probable sample mix-up
    (IDENTITY_FAILURE, exit 3) off 3,000 cross-build pairings; and two genuinely different people
    passed as "consistent with one person" because 2,000 junk pairings filled the 1,000-site floor
    and diluted a real 1-of-1 opposite homozygote to 0.05%, under the SUSPECT threshold.

    So coordinate keys are admitted only when both files declare the same, non-None build. rsID
    and position-resolved keys are build-independent identifiers and are always admitted.
    """
    shared = set(a["calls"]) & set(b["calls"])
    usable, excluded = set(), 0
    for k in shared:
        ka = a["calls"][k].get("keyed_by")
        kb = b["calls"][k].get("keyed_by")
        # A 23andMe record has no keyed_by: it is filed under its own rsID, which identifies.
        coord = (ka == "coordinate") or (kb == "coordinate")
        if coord and not allow_coordinates:
            excluded += 1
            continue
        usable.add(k)
    return usable, {"shared_total": len(shared), "coordinate_excluded": excluded}


def sample_identity(a: dict, b: dict, allow_coordinates: bool = True) -> dict:
    """Are these two files the same person? Ask BEFORE interpreting anything.

    `data-formats-and-parsing.md` §5 states the rule — "sample identity comes before concordance,
    and before any interpretation… if identity fails, stop" — and nothing implemented it, so the
    rule could not fail. A low concordance rate has two very different explanations: genotyping
    error, or **two different people**. Mislabelled kits, a relative's export and a file saved
    under the wrong name are all realistic.

    The measure is **opposite homozygotes**: sites where one file is homozygous for one allele and
    the other homozygous for a different allele, so the two genotypes share no allele at all. For
    one person that is bounded by the error rate; for two people it rises sharply.

    Restricted to autosomal, both-called, diploid, **non-palindromic** sites, because a palindromic
    site can appear to disagree purely from orientation and would manufacture a false failure.
    """
    checked = opposite = 0
    examples: list[str] = []
    usable, keyinfo = _comparable_keys(a, b, allow_coordinates)
    for k in sorted(usable):
        ca, cb = a["calls"][k], b["calls"][k]
        ga, gb = _norm_geno(ca["geno"]), _norm_geno(cb["geno"])
        if not ga or not gb or len(ga) != 2 or len(gb) != 2:
            continue
        if _norm_chrom(ca.get("chrom")) not in AUTOSOMES:
            continue
        sa, sb = set(ga), set(gb)
        if len(sa) != 1 or len(sb) != 1:
            continue                      # only homozygote-vs-homozygote is informative here
        if any((sa | sb) == amb for amb in AMBIGUOUS_PAIRS):
            continue                      # palindromic: apparent disagreement may be orientation
        checked += 1
        if not (sa & sb):
            opposite += 1
            if len(examples) < 20:
                examples.append(k)
    rate = (opposite / checked) if checked else None
    if checked < IDENTITY_MIN_SITES:
        verdict = "INSUFFICIENT_DATA"
        note = (f"only {checked} comparable homozygous autosomal sites (need "
                f"{IDENTITY_MIN_SITES}); identity was NOT tested, so do not treat the "
                "cross-platform comparison as coming from one person")
    elif rate is not None and rate > IDENTITY_FAIL_RATE:
        verdict = "IDENTITY_FAILURE"
        note = (f"{opposite} of {checked} sites share no allele ({rate*100:.2f}%). For one person "
                "this is bounded by the error rate. **These files are probably not the same "
                "person — STOP. Interpret nothing.** An audit of two people's data merged as one "
                "is worse than no audit")
    elif rate is not None and rate > IDENTITY_SUSPECT_RATE:
        verdict = "SUSPECT"
        note = (f"{opposite} of {checked} sites share no allele ({rate*100:.3f}%) — above a "
                "plausible genotyping-error rate and below an unrelated-person rate. Explain it "
                "before interpreting: a quality problem, a relative, or a sample mix-up")
    else:
        verdict = "CONSISTENT"
        note = (f"{opposite} of {checked} sites share no allele ({(rate or 0)*100:.3f}%), "
                "consistent with one person. Note this is identity, not accuracy")
    if keyinfo["coordinate_excluded"]:
        note += (f"; {keyinfo['coordinate_excluded']} shared key(s) were coordinates rather than "
                 "identifiers and were EXCLUDED — a coordinate names the same locus in two files "
                 "only when both declare the same build")
    return {"verdict": verdict, "checked_sites": checked, "opposite_homozygotes": opposite,
            "rate": rate, "note": note, "examples": examples,
            "shared_keys": keyinfo["shared_total"],
            "coordinate_keys_excluded": keyinfo["coordinate_excluded"]}


def concordance(a: dict, b: dict, allow_coordinates: bool = True) -> dict:
    """Compare two files site by site.

    Both sides are normalised and required to be diploid before comparison. An earlier version
    compared `set(geno)`, which scored a homozygote against a half-call at the same allele
    ("CC" vs "C") as agreement — inflating the very quality gate the audit depends on. Comparing
    sorted strings keeps "AG" == "GA" without collapsing ploidy.

    Non-diploid comparisons are excluded and counted rather than resolved: a haploid
    sex-chromosome or mitochondrial call and a truncated field look identical here, and neither
    can be compared as a diploid genotype.
    """
    shared, keyinfo = _comparable_keys(a, b, allow_coordinates)
    comparable, agree, disagree, non_diploid = [], [], [], []
    for k in sorted(shared):
        ga, gb = _norm_geno(a["calls"][k]["geno"]), _norm_geno(b["calls"][k]["geno"])
        if not ga or not gb:
            continue
        if len(ga) != 2 or len(gb) != 2:
            non_diploid.append(k)
            continue
        comparable.append(k)
        (agree if ga == gb else disagree).append(k)
    return {
        "shared_sites": len(shared),
        "coordinate_keys_excluded": keyinfo["coordinate_excluded"],
        "comparable_sites": len(comparable),
        "concordant": len(agree),
        "discordant": len(disagree),
        "non_diploid_excluded": len(non_diploid),
        "rate": (len(agree) / len(comparable)) if comparable else None,
        "discordant_examples": disagree[:20],
        "non_diploid_examples": non_diploid[:20],
    }


def report(files: list[str], as_json: bool, catalog_only: bool) -> int:
    # The parse is staged by format rather than run file by file, for two reasons that both only
    # show up on real data.
    #
    # Memory: a retained VCF record costs 537 bytes (measured, linear in record count), so a 30x
    # whole-genome VCF's 4-6 million records is 2-3 GB resident before any interpretation. The
    # array files are parsed first so their site list can bound what the sequencing file keeps.
    #
    # Keying: a provider's VCF frequently ships with `ID` as `.`, and this catalogue is keyed on
    # rsIDs, so such a file matches *nothing* and every finding reads as absent. The array files
    # carry (rsID, chromosome, position) in their own rows, which is a position map that does not
    # depend on this script asserting any coordinate from memory — usable, and only usable, where
    # both files declare the same build.
    kinds = []
    for p in files:
        try:
            kinds.append((p, sniff(p)))
        except FileNotFoundError:
            print(f"Cannot read {p}: no such file.", file=sys.stderr); return 2
        except ValueError as e:
            print(str(e), file=sys.stderr); return 2

    by_path, staging_warnings = {}, []
    for p, kind in kinds:
        if kind == "vcf":
            continue
        d = parse_23andme(p)
        d["path"], d["build"] = p, detect_build(d["header"])
        by_path[p] = d
        if d["sites"] > len(d["calls"]):
            staging_warnings.append(
                f"{p}: {d['sites'] - len(d['calls'])} duplicate rsID row(s) collapsed — the later "
                "row won. Two rows for one rsID is a provider or concatenation artefact; if the "
                "duplicates disagree, the genotype reported here is arbitrary."
            )

    observations: dict[str, dict] = {}
    for d in by_path.values():
        if d["build"]:
            # dict.update() let a later array file's mapping silently overwrite an earlier
            # one, so "a position claimed by two rsIDs is dropped" held only WITHIN a file. The
            # observations are pooled first and the rule applied once over the union.
            for k, v in position_index(d).items():
                observations.setdefault(d["build"], {}).setdefault(k, set()).add(v)

    indexes: dict[str, dict] = {}
    for build, obs in observations.items():
        keep_map, conflicts = {}, []
        for k, rsids in obs.items():
            if len(rsids) == 1:
                keep_map[k] = next(iter(rsids))
            else:
                conflicts.append((k, sorted(rsids)))
        indexes[build] = keep_map
        for (chrom, pos), rsids in conflicts[:10]:
            staging_warnings.append(
                f"position {chrom}:{pos} ({build}) is claimed by more than one rsID across the "
                f"array files supplied ({', '.join(rsids)}); it has been dropped from the position "
                "map rather than guessed at, so a VCF record there stays unidentified."
            )

    def _pos_index_for(path: str):
        """The position map usable for this VCF: same declared build on both sides, or none."""
        b = detect_build(read_header(path))
        return (indexes.get(b), b) if b else (None, None)

    keep = set(CATALOG)
    # Cross-file keys are needed only when a comparison will actually run, which is exactly two
    # files. With three or more, retaining 1.18M records for an identity pass the report itself
    # says did not run cost 672 MiB to produce nothing.
    if len(files) == 2:
        for d in by_path.values():
            keep |= set(d["calls"])

    # Identity and concordance are computed for exactly two files (below), so cross-file keys are
    # only needed then. Two sequencing files get a key-only prepass — strings, not records.
    vcfs = [p for p, kind in kinds if kind == "vcf"]
    if len(files) == 2 and len(vcfs) == 2:
        first = vcf_keys(vcfs[0], _pos_index_for(vcfs[0])[0])
        shared = vcf_keys(vcfs[1], _pos_index_for(vcfs[1])[0], within=first)
        first = None
        keep |= shared
        staging_warnings.append(
            f"Two sequencing files: {len(shared)} site key(s) are present in both and were "
            "retained for the identity and concordance pass. Sites unique to one file are counted "
            "but not held, since a comparison cannot use them."
        )

    for p in vcfs:
        pi, pi_build = _pos_index_for(p)
        d = parse_vcf(p, keep=keep, pos_index=pi)
        d["path"], d["build"] = p, detect_build(d["header"])
        d["pos_index_build"] = pi_build if pi else None
        by_path[p] = d

    parsed = [by_path[p] for p in files]

    out = {"files": [], "catalog": {}, "apoe": {}, "concordance": None, "warnings": []}
    blocking_flags: set[str] = set()

    out["warnings"].extend(staging_warnings)
    if len(parsed) > 2:
        out["warnings"].append(
            f"{len(parsed)} files were supplied. The identity gate and the concordance pass compare "
            "exactly two files, so NEITHER RAN. Re-run pairwise before interpreting anything "
            "cross-platform: an audit that merges two people's data as one is worse than no audit, "
            "and that is the check that was skipped."
        )

    for d in parsed:
        total = d.get("sites") or len(d["calls"])
        entry = {
            "path": d["path"], "format": d["format"], "build": d["build"],
            "sites": total, "no_calls": d["nocall"],
            "no_call_rate": round(d["nocall"] / total, 6) if total else None,
            "chromosomes": d.get("chrom_count", len({c["chrom"] for c in d["calls"].values()})),
        }
        if d["format"] == "vcf":
            entry["vcf_kind"] = d.get("vcf_kind")
            entry["reference_blocks"] = d.get("ref_blocks", 0)
            entry["zero_depth_discarded"] = d.get("zero_depth", 0)
            entry["records_with_rsid"] = d.get("rsid_records", 0)
            entry["records_keyed_by_position"] = d.get("pos_matched", 0)
            entry["records_retained"] = d.get("retained", len(d["calls"]))
            entry["samples"] = len(d.get("samples") or [])
            if len(d.get("samples") or []) > 1:
                blocking_flags.add("more than one sample in the file")
                out["warnings"].append(
                    f"{d['path']}: this VCF carries {len(d['samples'])} samples "
                    f"({', '.join(d['samples'][:6])}{'…' if len(d['samples']) > 6 else ''}). "
                    "Only the FIRST sample column was read, and everything reported for this file "
                    "is that one person's. A family or trio VCF read as one person is the same "
                    "class of error as merging two people's files — and worse here, because "
                    "nothing in the output would look wrong. Extract a single sample "
                    "(`bcftools view -s <sample>`) and re-run."
                )
            if d.get("collapsed"):
                out["warnings"].append(
                    f"{d['path']}: {d['collapsed']} site(s) had two or more records resolving to "
                    "them with different genotypes — split multi-allelic records, or duplicate "
                    "positions. NO genotype was taken from those sites, because which record won "
                    "would depend on line order. Normalise with `bcftools norm -m+` and re-run."
                )
            if d.get("sites_only"):
                out["warnings"].append(
                    f"{d['path']}: {d['sites_only']} record(s) carry no FORMAT/sample column. A "
                    "sites-only VCF lists variants without saying who has them, so no genotype "
                    "can be read from those records — they are counted here and interpreted "
                    "nowhere."
                )
        out["files"].append(entry)
        if d["format"] == "vcf" and not d.get("rsid_records") and not d.get("pos_matched"):
            blocking_flags.add("no variant identifiers could be keyed")
            out["warnings"].append(
                f"{d['path']}: the ID column carries NO dbSNP rsIDs (0 of {total} records) and no "
                "position map was usable, so NOTHING in this file could be matched to the "
                "catalogue or to the other file. Every catalogue row below reads as absent for a "
                "reason of ANNOTATION, NOT BIOLOGY, and the identity gate had nothing to compare. "
                "This is a blocking defect, not a finding: annotate the file against dbSNP "
                "(`bcftools annotate -c ID -a <dbSNP.vcf.gz> -o out.vcf.gz`) and re-run, or supply "
                "an array export from the same person in the SAME declared build so positions can "
                "key it. Do not hand-match positions across builds: a GRCh37 coordinate and a "
                "GRCh38 coordinate are different places in the genome."
            )
        elif d["format"] == "vcf" and 0 < d.get("rsid_records", 0) < total / 2:
            out["warnings"].append(
                f"{d['path']}: only {d['rsid_records']} of {total} records carry an rsID. A "
                "catalogued variant that happens to sit on an unannotated record cannot be matched "
                "and will read as absent, so treat absence in this file as unresolved rather than "
                "as a reference call."
            )
        if d.get("pos_matched"):
            out["warnings"].append(
                f"{d['path']}: {d['pos_matched']} record(s) were keyed to an rsID BY POSITION, "
                f"using coordinates taken from the other file's own rows with both files declaring "
                f"{d.get('pos_index_build')}, and restricted to SNV-shaped records. Two "
                "consequences to hold onto. The identity gate reads opposite homozygotes, and an "
                "array probe that reports the opposite strand at a non-palindromic site becomes an "
                "apparent opposite homozygote under positional keying — so weigh a borderline "
                "SUSPECT verdict with that in mind rather than concluding a sample mix-up. And a "
                "position is only as good as the build declaration it rests on."
            )
        if d.get("restricted") and total > d.get("retained", total):
            out["warnings"].append(
                f"{d['path']}: {d['retained']} of {total} records were held in memory — the "
                "catalogue, the APOE pair, and the sites the other file genotypes. A whole-genome "
                "file cannot be held whole (537 bytes per retained record, measured), and nothing "
                "here reads a genotype outside that set, so every reported figure is unchanged. "
                "The file-level counts above (sites, no-calls, reference blocks, chromosomes) are "
                "taken over the WHOLE file, not over the retained subset."
            )
        if d["build"] is None:
            blocking_flags.add("genome build not declared")
            out["warnings"].append(
                f"{d['path']}: genome build NOT declared in the file. Positions cannot be looked up "
                "safely. Determine the build from the provider before interpreting any position."
            )
        if d.get("vcf_kind") == "variants-only":
            out["warnings"].append(
                f"{d['path']}: variants-only VCF. A catalogued site with no line in this file is NOT a "
                "homozygous-reference call — homozygous-reference and never-covered are the same "
                "observation here, which is no observation. In particular, an APOE e3/e3 person is "
                "reference at BOTH defining sites and is therefore invisible in a variants-only file: "
                "never infer e3/e3 from absence."
            )
        if d.get("ref_blocks"):
            out["warnings"].append(
                f"{d['path']}: {d['ref_blocks']} reference-block record(s). A block asserts that no "
                "variant was called across an interval; it asserts no genotype at any catalogued "
                "position inside it, and none was taken from one."
            )
        if d.get("zero_depth"):
            out["warnings"].append(
                f"{d['path']}: {d['zero_depth']} genotype(s) emitted with DP=0 and discarded. A call "
                "with no supporting reads is no information, not a reference call."
            )

    builds = {d["build"] for d in parsed if d["build"]}
    if len(builds) > 1:
        out["warnings"].append(
            f"Files declare DIFFERENT builds ({', '.join(sorted(builds))}). Do not compare positions "
            "across them without liftover; rsID-based comparison is safe, positional is not."
        )

    # What "absent" means differs by file kind, and conflating the two is how a variants-only
    # VCF's silence becomes a reference call.
    if any(d.get("vcf_kind") == "variants-only" for d in parsed):
        absent_status = ("absent: no line in a variants-only VCF (and no array call) — "
                         "homozygous-reference and never-covered are indistinguishable, so this is "
                         "no information rather than a reference genotype")
    else:
        absent_status = "not present or no-called — the array may never have probed it"
    # A file nothing could be keyed in has not reported absence; it has reported nothing. Saying
    # "absent" of such a file states a fact about the person that the data never addressed.
    unkeyed = [d["path"] for d in parsed
               if d["format"] == "vcf" and not d.get("rsid_records") and not d.get("pos_matched")]
    if unkeyed:
        absent_status += ("; and nothing in " + ", ".join(unkeyed) + " could be keyed at all "
                          "(no rsIDs, no usable position map), so this row is unexamined rather "
                          "than negative")

    merged = {}
    for d in parsed:
        for rsid, c in d["calls"].items():
            if rsid in CATALOG and c["geno"]:
                merged.setdefault(rsid, []).append((d["path"], c["geno"]))
    for rsid, (gene, what, site_alleles) in CATALOG.items():
        hits = merged.get(rsid)
        if not hits:
            out["catalog"][rsid] = {"gene": gene, "site": what, "genotype": None,
                                    "status": absent_status}
            continue
        genos = {g for _, g in hits}
        # A discordant site has no genotype. Returning one — the alphabetically first, as an
        # earlier version did — let the APOE stage read a call the row beside it had already
        # condemned, and print "e4/e4 · uniquely determined" from two files that disagreed.
        discordant = len({frozenset(g) for g in genos}) > 1
        rec = {"gene": gene, "site": what,
               "genotype": None if discordant else sorted(genos)[0],
               "observed": sorted(genos) if discordant else None,
               "sources": [p for p, _ in hits]}
        rec["status"] = (f"DISCORDANT between files: {hits} — do not interpret until resolved"
                         if discordant else "called")
        # A discordant site has no genotype to orient, so a strand verdict there is noise that
        # distracts from the actual finding.
        if discordant:
            out["catalog"][rsid] = rec
            continue
        # The catalogue carries a VERIFIED plus-strand allele pair for several sites, and
        # apoe_diplotypes already refuses a genotype outside its pair ("DETECTABLE rather than
        # ambiguous"). The general path did not, so a positionally-keyed record whose REF/ALT are
        # disjoint from the catalogued pair — i.e. a different variant at the same coordinate —
        # was printed as a normal call with strand CLEAR. The same refusal now applies here.
        if site_alleles and not set(rec["genotype"]) <= {a.upper() for a in site_alleles}:
            keyed = {c.get("keyed_by") for p, c in
                     ((p, d["calls"].get(rsid)) for d in parsed for p in [d["path"]]) if c}
            rec["status"] = (
                f"REFUSED — observed alleles {sorted(set(rec['genotype']))} are not in this site's "
                f"verified pair {sorted(a.upper() for a in site_alleles)}. That is a detectable "
                "error, not a strand question: the record is a different variant at this "
                "coordinate, a mis-mapped row, or a parsing fault"
                + (", and it was keyed BY POSITION, which is the way a different variant at the "
                   "same coordinate gets here" if "position" in keyed else "")
            )
            rec["genotype"] = None
            rec["observed"] = sorted(genos)
            out["catalog"][rsid] = rec
            continue
        amb = strand_ambiguity(rec["genotype"], site_alleles)
        rec["strand"] = amb
        rec["site_palindromic"] = site_is_palindromic(site_alleles)
        if amb == "AMBIGUOUS":
            rec["strand_note"] = ("HOMOZYGOUS call at a PALINDROMIC site (A/T or C/G): the allele "
                                  "pair is its own reverse complement, so this call is 2 copies on "
                                  "one orientation and 0 on the other. Do not count risk alleles "
                                  "here until the platform's orientation is established.")
        elif amb == "UNDETERMINED":
            rec["strand_note"] = ("Homozygous or non-diploid call, and this site's allele pair is "
                                  "NOT verified in the catalogue, so palindromy cannot be ruled "
                                  "out. Establish the site's alleles before interpreting.")
        elif rec["site_palindromic"]:
            rec["strand_note"] = ("This site IS palindromic, but the call is heterozygous — one "
                                  "copy of each allele under either orientation — so the DOSAGE is "
                                  "unambiguous and the call is usable. Only the allele labels "
                                  "depend on orientation.")
        out["catalog"][rsid] = rec

    # Free consistency check: the two APOE sites are 138 bp apart in every build, so a different
    # spacing in the file's own coordinates means a row is mapped to the wrong place.
    for d in parsed:
        a1, a2 = d["calls"].get("rs429358"), d["calls"].get("rs7412")
        if a1 and a2 and str(a1["pos"]).isdigit() and str(a2["pos"]).isdigit():
            gap = abs(int(a1["pos"]) - int(a2["pos"]))
            if gap != APOE_SITE_GAP_BP:
                out["warnings"].append(
                    f"{d['path']}: the two APOE sites are {gap} bp apart in this file; they are "
                    f"{APOE_SITE_GAP_BP} bp apart in every build (c.526 − c.388, both in exon 4). One "
                    "of the two rows is mapped to the wrong position — do not call APOE from this "
                    "file until that is explained."
                )

    discordant_apoe = [r for r in ("rs429358", "rs7412")
                       if str(out["catalog"].get(r, {}).get("status", "")).startswith("DISCORDANT")]
    if discordant_apoe:
        out["apoe"] = {"resolved": None, "candidates": [],
                       "note": ("unresolved — the two files disagree at "
                                + ", ".join(discordant_apoe)
                                + ", so neither call can be used until that is explained")}
    else:
        g1 = out["catalog"].get("rs429358", {}).get("genotype")
        g2 = out["catalog"].get("rs7412", {}).get("genotype")
        out["apoe"] = apoe_diplotypes(g1, g2)

    if len(parsed) == 2:
        # Coordinate keys identify a locus only within one declared build. Both files must declare
        # a build, and the same one, before a "chrom:pos" key may be compared at all.
        builds = [d["build"] for d in parsed]
        allow_coords = bool(builds[0]) and builds[0] == builds[1]
        out["identity"] = sample_identity(parsed[0], parsed[1], allow_coords)
        out["concordance"] = concordance(parsed[0], parsed[1], allow_coords)
        if not allow_coords and out["identity"].get("coordinate_keys_excluded"):
            out["warnings"].append(
                f"{out['identity']['coordinate_keys_excluded']} shared key(s) between these files "
                "are coordinates, not identifiers, and were excluded from BOTH the identity gate "
                "and the concordance rate because the files do not declare the same build. A "
                "GRCh37 coordinate and a GRCh38 coordinate are different places, so comparing "
                "them measures nothing — and it moves the identity verdict in both directions: it "
                "has declared one person's files a mix-up, and it has let two different people "
                "pass as one by diluting a real disagreement."
            )
        if out["identity"]["verdict"] == "IDENTITY_FAILURE":
            blocking_flags.add("sample identity failure")
            out["warnings"].insert(0, "SAMPLE IDENTITY FAILURE: " + out["identity"]["note"])

    # The exit code is a property of the data, not of the output format. An earlier version
    # returned 3 in text mode and 0 under --json for the same undeclared-build file, so a
    # pipeline reading the exit status got the opposite answer from a human reading the report.
    #
    # Three conditions are blocking, and each one means the audit did not happen rather than that
    # it came back clean — which is exactly what a caller reading only the status would otherwise
    # conclude. An undeclared build makes every position lookup unsafe. A sample-identity failure
    # means two people's data were about to be merged as one. A file nothing could be keyed in
    # examined nothing, so its empty finding list is not a negative result.
    # Blocking conditions are recorded WHERE THEY ARE DECIDED. An earlier version derived them by
    # substring-searching the warning list — and every per-file warning is formatted as
    # f"{path}: ...", so a file whose NAME contained "NO dbSNP rsIDs" or "build NOT declared"
    # forged a blocking condition that never occurred, including "sample identity failure" on a
    # single file where the gate never ran. Prose is derived from flags, never the reverse.
    order = ["genome build not declared", "sample identity failure",
             "no variant identifiers could be keyed", "no genotypes could be extracted",
             "more than one sample in the file"]
    # "Nothing was examined" is not only an unannotated ID column. A file whose records were all
    # reference blocks or DP=0, an array with no rs-prefixed keys, and an array that is 100%
    # no-calls each extracted zero genotypes and exited 0 — a clean-looking report of nothing.
    extracted = sum(1 for d in parsed for c in d["calls"].values() if c.get("geno"))
    if not extracted:
        blocking_flags.add("no genotypes could be extracted")
        out["warnings"].append(
            "NO genotypes were extracted from any file supplied. Whatever the rows below say, "
            "nothing was read: this is a statement about the input, not about the person."
        )
    out["blocking"] = [b for b in order if b in blocking_flags]
    exit_code = 3 if out["blocking"] else 0
    if as_json:
        out["exit_code"] = exit_code
        print(json.dumps(out, indent=2))
        return exit_code

    print("=== Files ===")
    for e in out["files"]:
        print(f"  {e['path']}")
        print(f"    format {e['format']} · build {e['build'] or 'UNDECLARED'} · "
              f"{e['sites']} sites · {e['no_calls']} no-calls "
              f"({'' if e['no_call_rate'] is None else format(e['no_call_rate']*100, '.3f') + '%'}) · "
              f"{e['chromosomes']} chromosomes")
        if e.get("vcf_kind"):
            print(f"    vcf kind {e['vcf_kind']} · {e.get('reference_blocks', 0)} reference blocks · "
                  f"{e.get('zero_depth_discarded', 0)} zero-depth calls discarded")
    if out.get("identity"):
        i = out["identity"]
        print("\n=== Sample identity (asked BEFORE concordance, and before any interpretation) ===")
        print(f"  {i['verdict']} · {i['note']}")
        # Only show the sites when the verdict rests on them. Printing them under
        # INSUFFICIENT_DATA reads as evidence of failure when the finding is "not tested".
        if i["examples"] and i["verdict"] in ("IDENTITY_FAILURE", "SUSPECT"):
            print(f"  sites sharing no allele: {', '.join(i['examples'])}")
    if out["concordance"]:
        c = out["concordance"]
        rate = "n/a" if c["rate"] is None else f"{c['rate']*100:.3f}%"
        print("\n=== Cross-platform concordance ===")
        print(f"  shared {c['shared_sites']} · comparable {c['comparable_sites']} · "
              f"concordant {c['concordant']} · discordant {c['discordant']} · rate {rate}")
        if any(d.get("vcf_kind") == "variants-only" for d in parsed):
            print("  ! one input is a variants-only VCF, so this rate is NOT comparable to an "
                  "array-vs-array figure: the overlap is only the sites that file chose to record, "
                  "which are disproportionately non-reference. Read it as a rate over that "
                  "overlap, not over the genome.")
        if c["comparable_sites"] < 1000:
            print(f"  ! only {c['comparable_sites']} comparable sites — too few for the rate to "
                  "mean anything. Report the count, not the percentage.")
        if c.get("non_diploid_excluded"):
            print(f"  {c['non_diploid_excluded']} non-diploid comparison(s) excluded (haploid "
                  "sex-chromosome/mitochondrial calls, or truncated fields) — these cannot be "
                  "compared as diploid genotypes")
        if c["discordant_examples"]:
            print(f"  discordant examples: {', '.join(c['discordant_examples'])}")
    print("\n=== Catalogued sites ===")
    for rsid, r in out["catalog"].items():
        # --catalog-only hides sites with nothing to say. A DISCORDANT site has plenty to say and
        # now carries no genotype (by design), so filtering on genotype alone would hide the
        # finding — which is the opposite of what this flag is for.
        if (catalog_only and r.get("genotype") is None
                and not str(r.get("status", "")).startswith("DISCORDANT")):
            continue
        shown = r.get("genotype") or ("/".join(r["observed"]) if r.get("observed") else "--")
        print(f"  {rsid:<12} {r['gene']:<10} {shown:<8} {r['status']}")
        if "strand_note" in r:
            print(f"               ^ [{r['strand']}] {r['strand_note']}")
    print("\n=== APOE ===")
    a = out["apoe"]
    print(f"  diplotype: {a['resolved'] or 'unresolved'} · {a['note']}")
    for r in ("rs429358", "rs7412"):
        st = str(out["catalog"].get(r, {}).get("status", ""))
        if st.startswith("DISCORDANT"):
            print(f"  ! {r} is discordant between the files — no APOE call is possible")
    if a.get("caution"):
        print(f"  ! caution: {a['caution']}")
    if out["warnings"]:
        print("\n=== Warnings ===")
        for w in out["warnings"]:
            print(f"  ! {w}")
    if out["blocking"]:
        print("\n=== BLOCKING ===")
        print("  This audit did not complete on the data as supplied: "
              + "; ".join(out["blocking"]) + ".")
        print("  An empty or clean finding list above is NOT a negative result — resolve the")
        print("  blocking item and re-run before anything here is interpreted.")
    print("\nThis output is what the DATA says. It assigns no risk and no pathogenicity, and")
    print("recommends nothing. Interpretation belongs to the skill's references.")
    return exit_code


# --------------------------------------------------------------------------------------
# Offline self-test
# --------------------------------------------------------------------------------------
def self_test() -> int:
    import contextlib
    import io
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
    # REGRESSION, the worst defect this script has had: `set("C") == set("CC")`, so a half-call was
    # read as a homozygote and reported as a confident e4/e4 — a fabricated finding at the single
    # most consequential site. Each of these resolved under the old code.
    half_e4 = apoe_diplotypes("C", "CC")
    check("APOE half-call does NOT resolve to e4/e4", half_e4["resolved"] is None)
    check("APOE half-call says why", "diploid" in half_e4["note"])
    check("APOE half-call at the other site does NOT resolve",
          apoe_diplotypes("T", "CC")["resolved"] is None)
    check("APOE three-allele field refused", apoe_diplotypes("CTT", "CC")["resolved"] is None)
    check("APOE half-call on the second site refused",
          apoe_diplotypes("CC", "C")["resolved"] is None)
    # A no-call must be diagnosed as a no-call, not as a strand or build problem.
    nc = apoe_diplotypes("--", "CC")
    check("APOE no-call refused", nc["resolved"] is None)
    check("APOE no-call diagnosed as a no-call", "no-call" in nc["note"])
    check("APOE no-call not misdiagnosed as strand/build", "orientation" not in nc["note"])
    # Both APOE sites are T/C and the complement set A/G is disjoint, so a flip is DETECTABLE.
    flip = apoe_diplotypes("AG", "CC")
    check("APOE non-T/C allele refused", flip["resolved"] is None)
    check("APOE flip reported as detectable", "DETECTABLE" in flip["note"])
    # VCF separators must survive normalisation.
    check("APOE accepts VCF separators", apoe_diplotypes("C/T", "C|C")["resolved"] == "e3/e4")
    # The three observations that resolve uniquely ONLY by invoking the rare e1 haplotype must
    # carry a caution, because an error at one of the two sites is the likelier explanation.
    e1 = apoe_diplotypes("CC", "CT")
    check("APOE e1/e4 resolves", e1["resolved"] == "e1/e4")
    check("APOE e1 resolution carries a caution", e1.get("caution") is not None)
    check("APOE e1 caution names the error explanation", "genotyping error" in e1["note"])
    check("APOE e1/e1 carries a caution", apoe_diplotypes("CC", "TT").get("caution") is not None)
    check("APOE e1/e2 carries a caution", apoe_diplotypes("CT", "TT").get("caution") is not None)
    check("APOE common diplotype carries NO caution",
          apoe_diplotypes("TT", "CC").get("caution") is None)

    # --- Genotype normalisation: sorts alleles, keeps ploidy ---
    check("norm sorts alleles", _norm_geno("GA") == "AG")
    check("norm strips VCF separators", _norm_geno("C|T") == "CT")
    check("norm preserves a half-call's length", _norm_geno("C") == "C")
    check("norm passes None through", _norm_geno(None) is None)

    # --- Build detection. Must never guess. ---
    check("build GRCh37 from hg19", detect_build(["# build 37, hg19 coordinates"]) == "GRCh37/hg19")
    check("build GRCh38", detect_build(["##reference=GRCh38"]) == "GRCh38")
    check("build undeclared returns None", detect_build(["# some unrelated comment"]) is None)
    check("build undeclared on empty header", detect_build([]) is None)

    # --- Strand ambiguity. Three-state, and about DOSAGE rather than about the site alone. ---
    # A heterozygote at a palindromic site carries one copy of each allele under either
    # orientation, so its dosage is 1 either way. Only a homozygote is genuinely ambiguous.
    # Both earlier versions of this function got this wrong, in opposite directions.
    check("het A/T is CLEAR — dosage 1 under either orientation",
          strand_ambiguity("AT") == "CLEAR")
    check("het C/G is CLEAR — same reason", strand_ambiguity("CG") == "CLEAR")
    check("allele order irrelevant", strand_ambiguity("GC") == strand_ambiguity("CG"))
    check("het A/G is CLEAR", strand_ambiguity("AG") == "CLEAR")
    check("None is UNDETERMINED", strand_ambiguity(None) == "UNDETERMINED")
    check("no-call is UNDETERMINED", strand_ambiguity("--") == "UNDETERMINED")
    # REGRESSION 1: a boolean version returned False for a homozygous call, silently passing the
    # most dangerous class of call in the file. A homozygote tells you nothing about the pair.
    check("homozygous AA is UNDETERMINED, not CLEAR", strand_ambiguity("AA") == "UNDETERMINED")
    check("homozygous CC is UNDETERMINED, not CLEAR", strand_ambiguity("CC") == "UNDETERMINED")
    check("homozygous GG is UNDETERMINED, not CLEAR", strand_ambiguity("GG") == "UNDETERMINED")
    # With the site's alleles supplied, a HOMOZYGOTE resolves definitively either way.
    check("homozygote at a known A/T site is AMBIGUOUS",
          strand_ambiguity("AA", {"A", "T"}) == "AMBIGUOUS")
    check("homozygote at a known C/G site is AMBIGUOUS",
          strand_ambiguity("CC", {"C", "G"}) == "AMBIGUOUS")
    check("homozygote at a known A/G site is CLEAR",
          strand_ambiguity("AA", {"A", "G"}) == "CLEAR")
    # REGRESSION 2, the opposite error and the reason for this rewrite: supplying the pair made
    # the function return AMBIGUOUS for EVERY call at a palindromic site, including a
    # heterozygote whose dosage was never in doubt — suppressing a real finding.
    check("het at a known C/G site is CLEAR, not AMBIGUOUS",
          strand_ambiguity("CG", {"C", "G"}) == "CLEAR")
    check("het at a known A/T site is CLEAR, not AMBIGUOUS",
          strand_ambiguity("AT", {"A", "T"}) == "CLEAR")
    check("het verdict does not depend on whether the pair was supplied",
          strand_ambiguity("AT") == strand_ambiguity("AT", {"A", "T"}) == "CLEAR")
    # The site property is reported separately, because it is still worth saying.
    check("site palindromy reported independently of genotype",
          site_is_palindromic({"C", "G"}) is True and site_is_palindromic({"C", "T"}) is False)
    check("unknown pair gives unknown palindromy", site_is_palindromic(None) is None)
    # And the catalogue's own two palindromic sites must be identified as such.
    check("catalogue flags rs1799945 as a palindromic site",
          site_is_palindromic(CATALOG["rs1799945"][2]) is True)
    check("catalogue flags rs9939609 as a palindromic site",
          site_is_palindromic(CATALOG["rs9939609"][2]) is True)
    check("catalogue flags rs1800562 as non-palindromic",
          site_is_palindromic(CATALOG["rs1800562"][2]) is False)

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
        # REGRESSION: set() comparison scored a homozygote against a half-call at the same allele
        # as agreement, inflating the audit's own quality gate.
        ph = os.path.join(td, "half.txt")
        with open(ph, "w") as fh:
            fh.write("# build 37\n")
            fh.write("rs429358\t19\t45411941\tT\n")     # half-call vs TT above
            fh.write("rs7412\t19\t45412079\tCC\n")      # agrees
            fh.write("rs6025\t1\t169519049\tGG\n")      # agrees
        ch = concordance(parse(p23), parse(ph))
        check("half-call excluded from comparable sites", ch["comparable_sites"] == 2)
        check("half-call NOT scored as concordant", ch["concordant"] == 2)
        check("half-call counted as a non-diploid exclusion", ch["non_diploid_excluded"] == 1)
        check("half-call named", ch["non_diploid_examples"] == ["rs429358"])
        # Heterozygote allele order must still agree — the property set() got right.
        pord = os.path.join(td, "order.txt")
        with open(pord, "w") as fh:
            fh.write("# build 37\nrs6025\t1\t169519049\tGA\n")
        pord2 = os.path.join(td, "order2.txt")
        with open(pord2, "w") as fh:
            fh.write("# build 37\nrs6025\t1\t169519049\tAG\n")
        check("het allele order still concordant",
              concordance(parse(pord), parse(pord2))["concordant"] == 1)

        # --- VCF semantics: absence, reference blocks, and zero depth ---
        check("variants-only VCF identified", v["vcf_kind"] == "variants-only")
        pg = os.path.join(td, "g.vcf")
        with open(pg, "w") as fh:
            fh.write("##fileformat=VCFv4.2\n##reference=GRCh38\n")
            fh.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tS1\n")
            # The APOE region as a zero-coverage reference block: an e3/e3 person looks identical.
            fh.write("19\t44908684\trs429358\tT\t<NON_REF>\t.\t.\tEND=44908900\tGT:DP\t0/0:0\n")
            fh.write("19\t44908822\trs7412\tC\t<NON_REF>\t.\t.\tEND=44908900\tGT:DP\t0/0:0\n")
            # A called variant with no supporting reads.
            fh.write("1\t169519049\trs6025\tG\tA\t.\tPASS\t.\tGT:DP\t0/1:0\n")
            # A haploid call.
            fh.write("12\t111803962\trs671\tG\tA\t.\tPASS\t.\tGT:DP\t1:30\n")
        gv = parse(pg)
        check("gVCF identified as all-sites", gv["vcf_kind"] == "gvcf-or-all-sites")
        check("reference blocks counted", gv["ref_blocks"] == 2)
        check("reference block yields NO genotype", gv["calls"]["rs429358"]["geno"] is None)
        check("reference block labelled", gv["calls"]["rs7412"]["kind"] == "reference-block")
        check("zero-depth genotype discarded", gv["calls"]["rs6025"]["geno"] is None)
        check("zero-depth counted", gv["zero_depth"] == 1)
        check("haploid call kept but marked", gv["calls"]["rs671"]["ploidy"] == 1)
        check("haploid call not a diploid call", gv["calls"]["rs671"]["kind"] == "non-diploid call")
        # THE FABRICATION THIS GUARDS: a zero-coverage APOE region must not become e3/e3.
        check("no APOE call from reference blocks",
              apoe_diplotypes(gv["calls"]["rs429358"]["geno"],
                              gv["calls"]["rs7412"]["geno"])["resolved"] is None)

        # --- End-to-end: the report must SAY that absence in a variants-only VCF is not reference
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([pvcf], False, False)
        txt = buf.getvalue()
        check("report flags variants-only semantics", "variants-only VCF" in txt)
        check("report warns against inferring e3/e3 from absence",
              "never infer e3/e3 from absence" in txt)
        check("report never prints a bare risk verdict", "assigns no risk" in txt)

        # --- REGRESSION: a discordant catalogue site must yield no genotype, and no APOE call.
        # Measured old behaviour: the row said "DISCORDANT ... do not interpret" and the same run
        # printed "diplotype: e4/e4 - uniquely determined", built from the alphabetically first
        # of the two disagreeing calls. Fabrication at the highest-stakes locus in the skill.
        pd1 = os.path.join(td, "disc_a.txt")
        with open(pd1, "w") as fh:
            fh.write("# build 37\nrs429358\t19\t45411941\tTT\nrs7412\t19\t45412079\tCC\n")
        pd2 = os.path.join(td, "disc_b.txt")
        with open(pd2, "w") as fh:
            fh.write("# build 37\nrs429358\t19\t45411941\tCC\nrs7412\t19\t45412079\tCC\n")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([pd1, pd2], False, True)
        txt = buf.getvalue()
        check("discordant APOE site yields no diplotype", "e4/e4" not in txt)
        check("discordant APOE site is named in the APOE block",
              "rs429358 is discordant between the files" in txt)
        check("discordant site still reported as discordant", "DISCORDANT between files" in txt)
        # And the JSON path must agree, including on the exit code.
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([pd1, pd2], True, True)
        j = json.loads(buf.getvalue())
        check("discordant site carries no genotype in JSON",
              j["catalog"]["rs429358"]["genotype"] is None)
        check("discordant site records what was observed",
              j["catalog"]["rs429358"]["observed"] == ["CC", "TT"])
        check("JSON APOE unresolved on discordance", j["apoe"]["resolved"] is None)

        # --- REGRESSION: the exit code is a property of the data, not the output format ---
        nb = os.path.join(td, "nobuild2.txt")
        with open(nb, "w") as fh:
            fh.write("rs6025\t1\t169519049\tGG\n")
        with contextlib.redirect_stdout(io.StringIO()):
            rc_text = report([nb], False, False)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc_json = report([nb], True, False)
        check("undeclared build exits 3 in text mode", rc_text == 3)
        check("undeclared build exits 3 under --json too", rc_json == 3)
        check("JSON carries the exit code", json.loads(buf.getvalue())["exit_code"] == 3)

        # --- APOE spacing invariant: 138 bp in every build ---
        pgap = os.path.join(td, "gap.txt")
        with open(pgap, "w") as fh:
            fh.write("# build 37\n")
            fh.write("rs429358\t19\t45411941\tTT\n")
            fh.write("rs7412\t19\t45413079\tCC\n")   # 1,138 bp away — mis-mapped
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([pgap], False, False)
        check("mis-mapped APOE spacing warned", "138 bp apart in every build" in buf.getvalue())
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([p23], False, False)
        check("correct APOE spacing not warned", "bp apart in every build" not in buf.getvalue())

        # --- Sample identity: the rule the references state and nothing implemented ---
        def _synth(path, flip_fraction, n=4000):
            """Two synthetic genomes: `flip_fraction` of sites made opposite homozygotes."""
            with open(path, "w") as fh:
                fh.write("# build 37\n")
                for i in range(n):
                    # Deterministic, no RNG: every k-th site is flipped to the other homozygote.
                    flip = flip_fraction and (i % max(1, int(1 / flip_fraction)) == 0)
                    geno = "AA" if not flip else "GG"
                    fh.write(f"rsid{i}\t{(i % 22) + 1}\t{1000 + i}\t{geno}\n")
        base = os.path.join(td, "id_base.txt")
        _synth(base, 0.0)
        same = os.path.join(td, "id_same.txt")
        _synth(same, 0.0)
        idr = sample_identity(parse(base), parse(same))
        check("identity CONSISTENT for two identical files", idr["verdict"] == "CONSISTENT")
        check("identity checked enough sites to judge", idr["checked_sites"] >= 1000)
        other = os.path.join(td, "id_other.txt")
        _synth(other, 0.05)          # 5% opposite homozygotes — two different people
        idf = sample_identity(parse(base), parse(other))
        check("identity FAILURE on 5% opposite homozygotes", idf["verdict"] == "IDENTITY_FAILURE")
        check("identity failure says stop", "STOP" in idf["note"])
        suspect = os.path.join(td, "id_suspect.txt")
        _synth(suspect, 0.005)       # 0.5% — above error, below unrelated
        check("identity SUSPECT in the middle band",
              sample_identity(parse(base), parse(suspect))["verdict"] == "SUSPECT")
        # The floor matters more than the rate: a handful of sites supports no verdict at all.
        check("identity refuses to judge on too few sites",
              sample_identity(parse(p23), parse(pb))["verdict"] == "INSUFFICIENT_DATA")
        # Palindromic sites must be excluded, or orientation manufactures a false failure.
        pal_a = os.path.join(td, "pal_a.txt")
        pal_b = os.path.join(td, "pal_b.txt")
        for path, geno in ((pal_a, "AA"), (pal_b, "TT")):
            with open(path, "w") as fh:
                fh.write("# build 37\n")
                for i in range(2000):
                    fh.write(f"rsid{i}\t{(i % 22) + 1}\t{1000 + i}\t{geno}\n")
        check("palindromic sites excluded from the identity test",
              sample_identity(parse(pal_a), parse(pal_b))["verdict"] == "INSUFFICIENT_DATA")
        # And an identity failure must reach the report as the first warning.
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([base, other], False, True)
        rep = buf.getvalue()
        check("report leads with the identity failure", "SAMPLE IDENTITY FAILURE" in rep)
        check("report prints the identity section before concordance",
              rep.index("Sample identity") < rep.index("Cross-platform concordance"))

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

        # --- Chromosome-label normalisation. "chr1" and "1" are one chromosome, and a positional
        # match that silently finds nothing looks exactly like two files with no shared sites. ---
        check("chrom label normalised", _norm_chrom("chr7") == _norm_chrom("7") == "7")
        check("mitochondrial aliases unified", _norm_chrom("chrM") == _norm_chrom("MT") == "MT")

        # --- Memory restriction. The counters must describe the FILE; retention must not. ---
        wide = os.path.join(td, "wide.vcf")
        with open(wide, "w") as fh:
            fh.write("##fileformat=VCFv4.2\n##reference=GRCh38\n")
            fh.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tS1\n")
            fh.write("19\t44908684\trs429358\tT\tC\t.\tPASS\tDP=30\tGT:DP\t0/1:30\n")
            for i in range(500):
                fh.write(f"1\t{200000 + i}\trs9{i:06d}\tA\tG\t.\tPASS\tDP=30\tGT:DP\t0/1:30\n")
        full = parse_vcf(wide)
        lean = parse_vcf(wide, keep={"rs429358"})
        check("restriction keeps only the wanted key", set(lean["calls"]) == {"rs429358"})
        check("restriction does not change the genotype",
              lean["calls"]["rs429358"]["geno"] == full["calls"]["rs429358"]["geno"])
        check("restricted parse still counts the whole file", lean["sites"] == full["sites"] == 501)
        check("restricted parse reports what it dropped", lean["retained"] == 1)
        check("restriction is disclosed", lean["restricted"] is True and full["restricted"] is False)
        check("rsID records counted", lean["rsid_records"] == 501)

        # --- A VCF with no rsIDs: the failure mode that silently empties the whole report. ---
        bare = os.path.join(td, "bare.vcf")
        with open(bare, "w") as fh:
            fh.write("##fileformat=VCFv4.2\n##reference=GRCh37\n")
            fh.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tS1\n")
            fh.write("19\t45411941\t.\tT\tC\t.\tPASS\tDP=30\tGT:DP\t0/1:30\n")
            fh.write("19\t45412079\t.\tC\tT\t.\tPASS\tDP=30\tGT:DP\t0/1:30\n")
            fh.write("1\t169519049\t.\tGTT\tG\t.\tPASS\tDP=30\tGT:DP\t0/1:30\n")
        unkeyed = parse_vcf(bare, keep=set(CATALOG))
        check("no-rsID VCF matches nothing", unkeyed["calls"] == {})
        check("no-rsID VCF says so", unkeyed["rsid_records"] == 0)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([bare], False, True)
        bare_out = buf.getvalue()
        check("no-rsID VCF raises the annotation warning", "NO dbSNP rsIDs" in bare_out)
        check("no-rsID warning names the remedy", "bcftools annotate" in bare_out)
        # --catalog-only hides absent rows, so the per-row wording is checked on the full report.
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([bare], False, False)
        check("no-rsID absence is not reported as negative", "unexamined rather" in buf.getvalue())

        # --- Positional keying rescues it, but only from the data and only in the same build. ---
        idx = position_index(parse(p23))           # p23 declares build 37; rows carry positions
        keyed = parse_vcf(bare, keep=set(CATALOG), pos_index=idx)
        check("position keying recovers a catalogued site",
              set(keyed["calls"]) == {"rs429358", "rs7412"})
        check("position keying is recorded on the record",
              keyed["calls"]["rs429358"]["keyed_by"] == "position")
        check("position keying counted", keyed["pos_matched"] == 2)
        check("an indel at a catalogued position is NOT keyed to it", "rs6025" not in keyed["calls"])
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([p23, bare], False, True)
        pos_out = buf.getvalue()
        check("positional keying is disclosed in the report", "BY POSITION" in pos_out)
        check("positional keying warns about strand-flipped probes", "opposite strand" in pos_out)
        # And it must NOT happen across builds: bare declares 37 here, so a 38 array must not key it.
        p38 = os.path.join(td, "arr38.txt")
        with open(p38, "w") as fh:
            fh.write("# build 38\nrsid\tchromosome\tposition\tgenotype\n")
            fh.write("rs429358\t19\t45411941\tTT\n")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([p38, bare], False, True)
        xb = buf.getvalue()
        check("no positional keying across declared builds", "BY POSITION" not in xb)
        check("cross-build mismatch still warned", "DIFFERENT builds" in xb)

        # --- A position claimed by two rsIDs is dropped, not guessed at. ---
        dup = os.path.join(td, "dup.txt")
        with open(dup, "w") as fh:
            fh.write("# build 37\nrsid\tchromosome\tposition\tgenotype\n")
            fh.write("rs111\t1\t500\tAA\n")
            fh.write("rs222\t1\t500\tAA\n")
            fh.write("rs333\t1\t600\tAA\n")
        didx = position_index(parse(dup))
        check("conflicting position dropped", ("1", "500") not in didx)
        check("unambiguous position kept", didx.get(("1", "600")) == "rs333")

        # --- Duplicate rsID rows are collapsed, and that must be said out loud. ---
        dup2 = os.path.join(td, "dup2.txt")
        with open(dup2, "w") as fh:
            fh.write("# build 37\nrsid\tchromosome\tposition\tgenotype\n")
            fh.write("rs6025\t1\t169519049\tGG\n")
            fh.write("rs6025\t1\t169519049\tAG\n")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([dup2], False, True)
        check("duplicate rsID rows disclosed", "duplicate rsID row" in buf.getvalue())

        # --- Key-only prepass: identifiers, no records. ---
        ks = vcf_keys(wide)
        check("key prepass returns every key", len(ks) == 501 and "rs429358" in ks)
        check("key prepass honours `within`",
              vcf_keys(wide, within={"rs429358", "rsX"}) == {"rs429358"})

        # --- Blocking conditions must reach the EXIT STATUS, not only the prose. A caller that
        # reads the status and not the report must not be told a non-audit went fine. ---
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc_id = report([base, other], True, True)
        check("identity failure is a blocking exit", rc_id == 3)
        check("blocking reasons carried in JSON",
              "sample identity failure" in json.loads(buf.getvalue())["blocking"])
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            check("unkeyable file is a blocking exit", report([bare], True, True) == 3)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            check("a keyable, build-declaring pair exits 0", report([p23, wide], True, True) == 0)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([bare], False, True)
        check("blocking section printed in text mode", "=== BLOCKING ===" in buf.getvalue())
        check("blocking section refuses the clean reading",
              "NOT a negative result" in buf.getvalue())

        # ===================================================================================
        # Controls for the ORIGINAL whole-genome patch's own features. The review's sharpest
        # finding was that the suite shipped with that patch was decorative: four different wrong
        # keep-unions, five of the seven counters, and every one of its disclosure warnings could
        # be broken with the suite still green. These assertions are what make them load-bearing.
        # ===================================================================================

        ctl = os.path.join(td, "ctl.vcf")
        with open(ctl, "w") as fh:
            fh.write("##fileformat=VCFv4.2\n##reference=GRCh38\n")
            fh.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tS1\n")
            fh.write("19\t44908684\trs429358\tT\tC\t.\tPASS\tDP=30\tGT:DP\t0/1:30\n")   # catalogued
            fh.write("1\t100\trs90001\tA\tG\t.\tPASS\tDP=30\tGT:DP\t0/1:30\n")          # array-shared
            fh.write("1\t200\trs90002\tA\tG\t.\tPASS\tDP=30\tGT:DP\t0/1:30\n")          # neither
            fh.write("1\t300\trs90003\tA\t<NON_REF>\t.\t.\tEND=400\tGT:DP\t0/0:30\n")   # ref block
            fh.write("1\t500\trs90004\tA\tG\t.\tPASS\tDP=0\tGT:DP\t0/1:0\n")            # zero depth
            fh.write("1\t600\trs90005\tA\tG\t.\tPASS\t.\tGT\t./.\n")                    # no-call
        ctl_arr = os.path.join(td, "ctl_arr.txt")
        with open(ctl_arr, "w") as fh:
            fh.write("# build 38\nrsid\tchromosome\tposition\tgenotype\n")
            fh.write("rs90001\t1\t100\tAG\n")

        # --- The keep-union is exactly (catalogue) ∪ (the other file's keys), no more, no less. ---
        full = parse_vcf(ctl)
        lean = parse_vcf(ctl, keep=set(CATALOG) | {"rs90001"})
        check("keep-union retains the catalogued site", "rs429358" in lean["calls"])
        check("keep-union retains the other file's site", "rs90001" in lean["calls"])
        check("keep-union drops what neither file needs", "rs90002" not in lean["calls"])
        check("restriction changes no genotype it keeps",
              lean["calls"]["rs429358"]["geno"] == full["calls"]["rs429358"]["geno"])

        # --- All SEVEN per-file counters are taken over the WHOLE file, not the retained subset. ---
        for name in ("sites", "chrom_count", "rsid_records", "nocall", "ref_blocks",
                     "zero_depth", "pos_matched"):
            check(f"counter '{name}' is unchanged by the keep restriction",
                  lean[name] == full[name])
        check("counters actually counted something",
              full["sites"] == 6 and full["ref_blocks"] == 1 and full["zero_depth"] == 1
              and full["nocall"] == 1 and full["rsid_records"] == 6)
        check("retention really was restricted", lean["retained"] < full["retained"])

        # The checks above drive parse_vcf directly, so they cannot see a wrong union BUILT in
        # report(). These go end to end, which is the control the review said was missing.
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([ctl], True, False)
        e2e = json.loads(buf.getvalue())
        check("end-to-end: the catalogue is still in report()'s keep-union",
              e2e["catalog"]["rs429358"]["genotype"] is not None)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([ctl_arr, ctl], True, False)
        pair = json.loads(buf.getvalue())
        check("end-to-end: the other file's sites are in report()'s keep-union",
              pair["concordance"]["shared_sites"] >= 1
              and pair["concordance"]["comparable_sites"] >= 1)

        # `sites` must be the file's record count, never the retained count.
        check("the 'sites' counter is the file's, not the retained subset's",
              lean["sites"] == 6 and lean["retained"] < 6)

        # read_header must STOP at the body. A concatenated or malformed file with a '##' line
        # below the body would otherwise be read as declaring a build the report denies.
        liar = os.path.join(td, "liar.vcf")
        with open(liar, "w") as fh:
            fh.write("##fileformat=VCFv4.2\n")
            fh.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tS1\n")
            fh.write("19\t44908684\trs429358\tT\tC\t.\tPASS\t.\tGT\t0/1\n")
            fh.write("##reference=GRCh37\n")          # below the body: must NOT be read
        check("read_header does not read past the body",
              detect_build(read_header(liar)) is None)

        # --- An UNDECLARED build must disable positional keying, not merely a differing one. ---
        nob_vcf = os.path.join(td, "nobuild.vcf")
        with open(nob_vcf, "w") as fh:
            fh.write("##fileformat=VCFv4.2\n")          # no reference line at all
            fh.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tS1\n")
            fh.write("19\t45411941\t.\tT\tC\t.\tPASS\tDP=30\tGT:DP\t0/1:30\n")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([p23, nob_vcf], True, True)
        nb = json.loads(buf.getvalue())
        check("an undeclared VCF build disables positional keying",
              nb["files"][1]["records_keyed_by_position"] == 0)
        check("an undeclared build is still blocking",
              "genome build not declared" in nb["blocking"])

        # --- The SNV-shape gate must reject a MIXED multi-allelic ALT, not just a pure indel. ---
        mixed_key, mixed_how = _vcf_key("19", "45411941", ".", "T", "C,TA",
                                        {("19", "45411941"): "rs429358"})
        check("a mixed SNV+indel ALT is not keyed by position", mixed_how == "coordinate")
        pure_key, pure_how = _vcf_key("19", "45411941", ".", "T", "C",
                                      {("19", "45411941"): "rs429358"})
        check("a clean SNV still IS keyed by position", pure_how == "position")
        gv_key, gv_how = _vcf_key("19", "45411941", ".", "T", "C,<NON_REF>",
                                  {("19", "45411941"): "rs429358"})
        check("a gVCF SNV with <NON_REF> is still keyed by position", gv_how == "position")
        star_key, star_how = _vcf_key("19", "45411941", ".", "T", "C,*",
                                      {("19", "45411941"): "rs429358"})
        check("a spanning-deletion ALT is not keyed by position", star_how == "coordinate")

        # --- read_header must stop at the body AND collect only ##/#CHROM. ---
        hdr = read_header(ctl)
        check("read_header stops at the first body line", len(hdr) == 3)
        check("read_header collects the #CHROM line", any(h.startswith("#CHROM") for h in hdr))
        check("read_header agrees with parse_vcf's own header",
              detect_build(hdr) == detect_build(parse_vcf(ctl)["header"]))

        # --- vcf_keys(within=) is the two-whole-genome memory bound; it must actually bound. ---
        allk = vcf_keys(ctl)
        bounded = vcf_keys(ctl, within={"rs429358"})
        check("vcf_keys(within=) returns only the intersection", bounded == {"rs429358"})
        check("vcf_keys(within=) is strictly smaller than the full pass", len(bounded) < len(allk))

        # --- Every disclosure warning the patch added needs a negative control. ---
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([ctl_arr, ctl], False, False)
        disc = buf.getvalue()
        for frag, why in (
            ("records were held in memory", "the memory-restriction disclosure"),
            ("reference-block record", "the reference-block disclosure"),
            ("DP=0 and discarded", "the zero-depth disclosure"),
        ):
            check(f"disclosure present: {why}", frag in disc)
        # ctl.vcf carries an END= block, so it is a gVCF; the variants-only disclosure is a
        # property of a DIFFERENT file kind and has to be asserted against one.
        check("a file with a reference block is not called variants-only",
              parse_vcf(ctl)["vcf_kind"] == "gvcf-or-all-sites")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([wide], False, False)
        check("disclosure present: the variants-only absence-semantics disclosure",
              "variants-only VCF" in buf.getvalue()
              and parse_vcf(wide)["vcf_kind"] == "variants-only")

        # ===================================================================================
        # Regressions from the adversarial review of the whole-genome patch. Each one shipped,
        # each was reproduced by execution, and each assertion below fails if the fix is reverted.
        # ===================================================================================

        def vcf(path, body, build="GRCh38", sample_cols="S1"):
            with open(path, "w") as fh:
                fh.write(f"##fileformat=VCFv4.2\n##reference={build}\n")
                fh.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t"
                         + sample_cols + "\n")
                fh.write(body)
            return path

        # --- A coordinate key identifies nothing, so it may not be compared across builds. ---
        # Direction 1: one person's two files declared a mix-up off cross-build pairings.
        b37 = vcf(os.path.join(td, "c37.vcf"),
                  "".join(f"1\t{1000+i}\t.\tA\tG\t.\tPASS\t.\tGT\t"
                          f"{'1/1' if i % 25 else '0/0'}\n" for i in range(1500)), build="GRCh37")
        b38 = vcf(os.path.join(td, "c38.vcf"),
                  "".join(f"1\t{1000+i}\t.\tA\tG\t.\tPASS\t.\tGT\t"
                          f"{'0/0' if i % 25 else '1/1'}\n" for i in range(1500)), build="GRCh38")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc_x = report([b37, b38], True, True)
        xb = json.loads(buf.getvalue())
        check("cross-build coordinate keys are excluded from the identity gate",
              xb["identity"]["coordinate_keys_excluded"] > 0
              and xb["identity"]["checked_sites"] == 0)
        check("cross-build pairings cannot manufacture an IDENTITY_FAILURE",
              xb["identity"]["verdict"] == "INSUFFICIENT_DATA")
        check("cross-build exclusion is disclosed", "coordinates, not identifiers" in
              " ".join(xb["warnings"]))
        # Direction 2: the SAME build is a legitimate comparison and must still work.
        b38b = vcf(os.path.join(td, "c38b.vcf"),
                   "".join(f"1\t{1000+i}\t.\tA\tG\t.\tPASS\t.\tGT\t"
                           f"{'1/1' if i % 25 else '0/0'}\n" for i in range(1500)), build="GRCh38")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([b38, b38b], True, True)
        same = json.loads(buf.getvalue())
        check("same-build coordinate keys ARE still compared",
              same["identity"]["checked_sites"] > 1000)

        # --- The coordinate key is normalised, or two files share nothing. ---
        k1, _ = _vcf_key("chr7", "100", ".", "A", "G", None)
        k2, _ = _vcf_key("7", "100", ".", "A", "G", None)
        check("coordinate key normalises the chromosome", k1 == k2 == "7:100")

        # --- A VCF-legal semicolon rsID list must still find the catalogue. ---
        merged = vcf(os.path.join(td, "merged.vcf"),
                     "6\t26092913\trs1800562;rs2071303\tG\tA\t.\tPASS\t.\tGT:DP\t1/1:30\n")
        mv = parse_vcf(merged)
        check("merged rsID list resolves to its first rsID", "rs1800562" in mv["calls"])
        check("merged rsID genotype survives", mv["calls"]["rs1800562"]["geno"] == "AA")

        # --- In a gVCF every record carries <NON_REF>, variant calls included. ---
        gv2 = vcf(os.path.join(td, "gvcf2.vcf"),
                  "19\t44908684\trs429358\tT\tC,<NON_REF>\t.\tPASS\t.\tGT:DP\t0/1:30\n"
                  "19\t44908822\trs7412\tC\t<NON_REF>\t.\t.\tEND=44908900\tGT:DP\t0/0:30\n")
        g2 = parse_vcf(gv2)
        check("a gVCF variant record with <NON_REF> is a CALL, not a reference block",
              set(g2["calls"]["rs429358"]["geno"] or "") == {"C", "T"})
        check("a true reference block is still refused",
              g2["calls"]["rs7412"]["kind"] == "reference-block")

        # --- A multi-sample VCF is one person's file read as everyone's. ---
        multi = vcf(os.path.join(td, "trio.vcf"),
                    "19\t44908684\trs429358\tT\tC\t.\tPASS\t.\tGT:DP\t0/1:30\t1/1:30\t0/0:30\n",
                    sample_cols="CHILD\tMOTHER\tFATHER")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc_multi = report([multi], True, True)
        mj = json.loads(buf.getvalue())
        check("multi-sample VCF is detected", mj["files"][0]["samples"] == 3)
        check("multi-sample VCF is blocking", "more than one sample in the file" in mj["blocking"]
              and rc_multi == 3)

        # --- Split multi-allelic records must not let line order pick the genotype. ---
        split = vcf(os.path.join(td, "split.vcf"),
                    "19\t44908684\t.\tT\tC\t.\tPASS\t.\tGT:DP\t0/1:30\n"
                    "19\t44908684\t.\tT\tA\t.\tPASS\t.\tGT:DP\t1/1:30\n")
        idx_ap = {("19", "44908684"): "rs429358"}
        sp = parse_vcf(split, pos_index=idx_ap)
        check("collapsed records yield NO genotype", sp["calls"]["rs429358"]["geno"] is None)
        check("the collapse is counted", sp["collapsed"] == 1)

        # --- A duplicated array rsID must not publish its coordinate. ---
        dupidx = os.path.join(td, "dupidx.txt")
        with open(dupidx, "w") as fh:
            fh.write("# build 37\nrsid\tchromosome\tposition\tgenotype\n")
            fh.write("rs429358\t19\t45411941\tTT\n")
            fh.write("rs429358\t19\t99999999\tCC\n")
        dd = parse(dupidx)
        check("a duplicated rsID keeps the FIRST row", dd["calls"]["rs429358"]["pos"] == "45411941")
        check("a duplicated rsID is recorded", "rs429358" in dd["duplicated_rsids"])
        check("a conflicted rsID is withheld from the position map",
              position_index(dd) == {})

        # --- A position claimed by two rsIDs across two array files is dropped, not overwritten. ---
        pa = os.path.join(td, "pa.txt"); pb2 = os.path.join(td, "pb2.txt")
        for pth, rs in ((pa, "rs111"), (pb2, "rs222")):
            with open(pth, "w") as fh:
                fh.write("# build 37\nrsid\tchromosome\tposition\tgenotype\n")
                fh.write(f"{rs}\t1\t500\tAA\n")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([pa, pb2], False, True)
        check("a cross-file position conflict is dropped and disclosed",
              "claimed by more than one rsID" in buf.getvalue())

        # --- A blocking condition must not be forgeable by a FILE NAME. ---
        evil_dir = os.path.join(td, "NO dbSNP rsIDs build NOT declared")
        os.makedirs(evil_dir, exist_ok=True)
        evil = os.path.join(evil_dir, "SAMPLE IDENTITY FAILURE.txt")
        with open(evil, "w") as fh:
            fh.write("# build 37\nrsid\tchromosome\tposition\tgenotype\n")
            fh.write("rs429358\t19\t45411941\tTT\n")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc_evil = report([evil], True, True)
        check("a file NAME cannot forge a blocking condition",
              json.loads(buf.getvalue())["blocking"] == [] and rc_evil == 0)

        # --- Zero extracted genotypes is a blocking condition, not a clean report. ---
        empty_arr = os.path.join(td, "allnocall.txt")
        with open(empty_arr, "w") as fh:
            fh.write("# build 37\nrsid\tchromosome\tposition\tgenotype\n")
            for i in range(20):
                fh.write(f"rs{i}\t1\t{1000+i}\t--\n")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc_empty = report([empty_arr], True, True)
        check("a run that extracted no genotypes blocks",
              "no genotypes could be extracted" in json.loads(buf.getvalue())["blocking"]
              and rc_empty == 3)

        # --- A genotype outside the catalogue's verified pair is refused, not printed. ---
        wrongpair = os.path.join(td, "wrongpair.txt")
        with open(wrongpair, "w") as fh:
            fh.write("# build 37\nrsid\tchromosome\tposition\tgenotype\n")
            fh.write("rs429358\t19\t45411941\tGG\n")       # APOE site is T/C; G is impossible
            fh.write("rs7412\t19\t45412079\tCC\n")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([wrongpair], True, True)
        wp = json.loads(buf.getvalue())
        check("an allele outside the catalogued pair is refused",
              wp["catalog"]["rs429358"]["genotype"] is None
              and "REFUSED" in wp["catalog"]["rs429358"]["status"])

        # --- sample_identity must normalise the chromosome label, not match it raw. ---
        ch1 = os.path.join(td, "chr_a.txt"); ch2 = os.path.join(td, "chr_b.txt")
        for pth, lab in ((ch1, "chr1"), (ch2, "1")):
            with open(pth, "w") as fh:
                fh.write("# build 37\nrsid\tchromosome\tposition\tgenotype\n")
                for i in range(1200):
                    fh.write(f"rs{i}\t{lab}\t{1000+i}\tAA\n")
        ident = sample_identity(parse(ch1), parse(ch2))
        check("identity gate normalises the chromosome label",
              ident["checked_sites"] >= 1000 and ident["verdict"] == "CONSISTENT")

        # --- A sites-only VCF has records; reporting 0 of 0 is three false statements. ---
        so = os.path.join(td, "sitesonly.vcf")
        with open(so, "w") as fh:
            fh.write("##fileformat=VCFv4.2\n##reference=GRCh38\n")
            fh.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")
            fh.write("19\t44908684\trs429358\tT\tC\t.\tPASS\t.\n")
        sov = parse_vcf(so)
        check("a sites-only VCF counts its records", sov["sites"] == 1)
        check("a sites-only VCF counts its rsIDs", sov["rsid_records"] == 1)
        check("a sites-only VCF yields no genotype", sov["calls"] == {})

        # --- The three-file path must be reachable from the CLI, since the docs describe it. ---
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc3 = main([p23, pb, wide, "--json"])
        check("the CLI accepts three files", rc3 in (0, 3))
        check("three files are reported as uncompared", "NEITHER RAN" in buf.getvalue())

        # --- Three files: the identity gate cannot run, and silence about that is the bug. ---
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            report([p23, pb, wide], False, True)
        check("three files warn that identity did NOT run", "NEITHER RAN" in buf.getvalue())

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
    ap.add_argument("files", nargs="*",
                    help="raw data files (23andMe-style or VCF). Identity and concordance compare "
                         "exactly two; more are parsed and reported, with no comparison.")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--catalog-only", action="store_true",
                    help="omit catalogued sites that were absent or no-called")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.files:
        ap.error("provide at least one raw data file (or --self-test)")
    # Three or more files used to be a usage error, which made the documented behaviour — "hand it
    # three and it says neither ran" — unreachable dead code that only the self-test could see.
    # They are now parsed and reported; report() says plainly that no comparison was performed.
    return report(args.files, args.json, args.catalog_only)


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        sys.exit(130)
