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
    """
    out = []
    with _open(path) as fh:
        for line in fh:
            if not line.startswith("#"):
                break
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
            if not geno or set(geno) <= {"-", "0", "."}:
                nocall += 1
                calls[rsid] = {"chrom": chrom, "pos": pos, "geno": None}
                continue
            calls[rsid] = {"chrom": chrom, "pos": pos, "geno": geno}
    return {"format": "23andme", "header": header, "calls": calls, "nocall": nocall,
            "sites": total, "chrom_count": len(chroms), "retained": len(calls),
            "restricted": False}


SNV_ALLELES = set("ACGT")


def position_index(d: dict) -> dict:
    """Map (chromosome, position) → rsID using the coordinates a file carries itself.

    The coordinates come from the data, never from this script. Asserting a catalogued variant's
    coordinates from memory is the exact fabrication this audit exists to catch, and a position
    quoted in the wrong build silently returns a different variant. A position claimed by two
    different rsIDs is dropped rather than guessed at.
    """
    idx, dropped = {}, set()
    for rsid, c in d["calls"].items():
        if not rsid.startswith("rs") or not str(c["pos"]).strip().isdigit():
            continue
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
    """
    if vid.startswith("rs"):
        return vid, "rsid"
    if pos_index:
        alts = alt.split(",")
        if (len(ref) == 1 and ref.upper() in SNV_ALLELES
                and all(len(a) == 1 and a.upper() in SNV_ALLELES for a in alts)):
            hit = pos_index.get((_norm_chrom(chrom), str(pos).strip()))
            if hit:
                return hit, "position"
    return f"{chrom}:{pos}", "coordinate"


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
    total = rsid_records = pos_matched = 0
    chroms = set()
    all_sites = False
    with _open(path) as fh:
        for line in fh:
            if line.startswith("##") or line.startswith("#CHROM"):
                header.append(line.rstrip("\n"))
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 10:
                continue
            chrom, pos, vid, ref, alt, info = parts[0], parts[1], parts[2], parts[3], parts[4], parts[7]
            total += 1
            chroms.add(_norm_chrom(chrom))
            if vid.startswith("rs"):
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

            if any(sym in alt for sym in SYMBOLIC_REF_ALTS) or "END=" in info:
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
                calls[key] = rec
    return {"format": "vcf", "header": header, "calls": calls, "nocall": nocall,
            "ref_blocks": ref_blocks, "zero_depth": zero_depth,
            "vcf_kind": "gvcf-or-all-sites" if all_sites else "variants-only",
            "sites": total, "chrom_count": len(chroms), "rsid_records": rsid_records,
            "pos_matched": pos_matched, "retained": len(calls), "restricted": keep is not None}


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


AUTOSOMES = {str(i) for i in range(1, 23)} | {f"chr{i}" for i in range(1, 23)}

# Thresholds for the identity gate below. These are heuristics with a stated basis, not published
# cut-offs: consumer genotyping error rates run well under one percent, while the
# opposite-homozygote rate between two *unrelated* people is a few percent — a gap of roughly an
# order of magnitude, which is what makes the test usable at all. The minimum-sites floor matters
# more than the rate: a handful of overlapping sites cannot support any verdict.
IDENTITY_MIN_SITES = 1000
IDENTITY_FAIL_RATE = 0.01
IDENTITY_SUSPECT_RATE = 0.001


def sample_identity(a: dict, b: dict) -> dict:
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
    for k in sorted(set(a["calls"]) & set(b["calls"])):
        ca, cb = a["calls"][k], b["calls"][k]
        ga, gb = _norm_geno(ca["geno"]), _norm_geno(cb["geno"])
        if not ga or not gb or len(ga) != 2 or len(gb) != 2:
            continue
        if str(ca.get("chrom")) not in AUTOSOMES:
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
    return {"verdict": verdict, "checked_sites": checked, "opposite_homozygotes": opposite,
            "rate": rate, "note": note, "examples": examples}


def concordance(a: dict, b: dict) -> dict:
    """Compare two files site by site.

    Both sides are normalised and required to be diploid before comparison. An earlier version
    compared `set(geno)`, which scored a homozygote against a half-call at the same allele
    ("CC" vs "C") as agreement — inflating the very quality gate the audit depends on. Comparing
    sorted strings keeps "AG" == "GA" without collapsing ploidy.

    Non-diploid comparisons are excluded and counted rather than resolved: a haploid
    sex-chromosome or mitochondrial call and a truncated field look identical here, and neither
    can be compared as a diploid genotype.
    """
    shared = set(a["calls"]) & set(b["calls"])
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

    indexes: dict[str, dict] = {}
    for d in by_path.values():
        if d["build"]:
            indexes.setdefault(d["build"], {}).update(position_index(d))

    def _pos_index_for(path: str):
        """The position map usable for this VCF: same declared build on both sides, or none."""
        b = detect_build(read_header(path))
        return (indexes.get(b), b) if b else (None, None)

    keep = set(CATALOG)
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
        out["files"].append(entry)
        if d["format"] == "vcf" and not d.get("rsid_records") and not d.get("pos_matched"):
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
        out["identity"] = sample_identity(parsed[0], parsed[1])
        out["concordance"] = concordance(parsed[0], parsed[1])
        if out["identity"]["verdict"] == "IDENTITY_FAILURE":
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
    blocking = []
    if any("build NOT declared" in w for w in out["warnings"]):
        blocking.append("genome build not declared")
    if any(w.startswith("SAMPLE IDENTITY FAILURE") for w in out["warnings"]):
        blocking.append("sample identity failure")
    if any("NO dbSNP rsIDs" in w for w in out["warnings"]):
        blocking.append("no variant identifiers could be keyed")
    out["blocking"] = blocking
    exit_code = 3 if blocking else 0
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
