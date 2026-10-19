#!/usr/bin/env python3
"""Draw lineage maps as SVG from a JSON spec -- haplogroup migration routes, ancestry-composition
shading, ancestor places, and an ahnentafel pedigree chart. Pure Python, no dependencies.

Usage:
  lineage_maps.py map spec.json -o map.svg          # routes, points and shaded countries on a map
                                                    # (a custom box inside Europe uses the finer outlines)
  lineage_maps.py pedigree persons.json -o tree.svg  # ahnentafel pedigree chart
  lineage_maps.py demo -o <dir>                      # writes example specs and SVGs (synthetic data)
  lineage_maps.py --self-test                        # offline checks, no input files

MAP SPEC (JSON object)
  title, subtitle          strings (optional)
  extent                   "world" | "europe" | "atlantic" | "ireland-britain" | [minlon, minlat, maxlon, maxlat]
  width, height            map panel in px (default 1200 x 640); the footer (legend, numbered key, notes)
                           is laid out below the panel and the canvas grows to fit it
  shade                    [{"country": "Ireland", "value": 4.3, "label": "Irish 4.3%"}, ...]
                           value 0..100 drives six colour bands (0-1, 1-5, 5-10, 10-25, 25-50, 50-100 %)
                           and a value label at the country's centre; country is a Natural Earth ADMIN
                           name or ISO-A3 code (case-insensitive); the band legend is added automatically
  points                   [{"lon": -8.47, "lat": 51.9, "label": "Cork", "sub": "b. 1842", "group": "paternal"}, ...]
  routes                   [{"label": "Y-DNA: M269 -> L21", "color": "#b5452c", "dash": "6 4",
                             "waypoints": [{"lon": 45, "lat": 48, "label": "steppe", "when": "~5,000 ya"}, ...]}, ...]
                           waypoints are drawn as numbered markers and listed in a key under the legend;
                           a waypoint with no label and no "when" only bends the line
  legend                   [{"color": "#hex", "label": "..."}, ...]  (route labels and point groups are added)
  notes                    ["Sources: ...", "Dates approximate ..."]  (wrapped into the footer)

PEDIGREE (JSON object keyed by ahnentafel number as a string)
  {"1": {"name": "...", "birth": "1982", "death": "", "place": "..."}, "2": {...father...}, "3": {...mother...}}
  Person n's father is 2n and mother is 2n+1. Missing numbers render as dashed "unknown" boxes.
  Option --generations N (default 5). Pass --redact to replace names of living people (no death
  date, birth within 100 years) with "living" -- for anything that leaves your own machine.

WHAT THIS DELIBERATELY DOES NOT DO
  It draws what the spec says. It does not know where a haplogroup came from, what a percentage
  means, or whether a pedigree is proven; the skill's references carry that, and every map should
  carry its sources in `notes`. Map outlines: Natural Earth (public domain), simplified and
  bundled beside this script in ../assets/.

Exit codes: 0 ok; 2 input unreadable or spec invalid; 5 bad usage.
"""
from __future__ import annotations

import argparse
import datetime
import json
import math
import os
import re
import sys
import tempfile
from xml.sax.saxutils import escape

__version__ = "1.1.0"
ASSETS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
EXTENTS = {
    "world": (-180.0, -58.0, 180.0, 84.0),
    "atlantic": (-110.0, 10.0, 60.0, 72.0),
    "europe": (-25.0, 33.0, 45.0, 72.0),
    "ireland-britain": (-11.5, 49.5, 2.5, 59.5),
}
RAMP = ["#f4efe6", "#eadcc3", "#dcbf94", "#cda06a", "#b97f45", "#9c5f2a"]   # six bands, finer below 25%
RAMP_BANDS = [(0, 1), (1, 5), (5, 10), (10, 25), (25, 50), (50, 100)]
GROUP_COLOURS = ["#2a5d8f", "#b5452c", "#3c7a49", "#7a4b8f", "#8a6d1f", "#1f7a8a"]


class SpecError(Exception):
    pass


# ----------------------------------------------------------------------------- map data

def load_outlines(extent_name: str, box=None) -> list[dict]:
    """World outlines for the world/atlantic extents; the finer Europe file for the Europe extents and for any
    custom box that lies inside the Europe extent."""
    fine = extent_name in ("europe", "ireland-britain")
    if extent_name == "custom" and box is not None:
        e = EXTENTS["europe"]
        fine = e[0] <= box[0] and e[1] <= box[1] and box[2] <= e[2] and box[3] <= e[3]
    fn = "europe_50m_compact.json" if fine else "world_110m_compact.json"
    path = os.path.join(ASSETS, fn)
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)["countries"]


def resolve_extent(extent) -> tuple[str, tuple[float, float, float, float]]:
    if isinstance(extent, str):
        if extent not in EXTENTS:
            raise SpecError(f"unknown extent {extent!r}; use one of {sorted(EXTENTS)} or [minlon, minlat, maxlon, maxlat]")
        return extent, EXTENTS[extent]
    if isinstance(extent, (list, tuple)) and len(extent) == 4:
        a, b, c, d = map(float, extent)
        if not (-180 <= a < c <= 180 and -90 <= b < d <= 90):
            raise SpecError("extent box must be [minlon, minlat, maxlon, maxlat] with min < max")
        return "custom", (a, b, c, d)
    raise SpecError("extent must be a named extent or a four-number box")


class Projection:
    """Equirectangular, standard parallel at the extent's mid-latitude, centred on the canvas."""

    def __init__(self, box, width, height, margin=(60, 60, 60, 110)):
        self.minlon, self.minlat, self.maxlon, self.maxlat = box
        top, right, bottom, left = margin
        self.midlat = (self.minlat + self.maxlat) / 2
        self.cos = max(0.2, math.cos(math.radians(self.midlat)))
        avail_w, avail_h = width - left - right, height - top - bottom
        dlon, dlat = self.maxlon - self.minlon, self.maxlat - self.minlat
        self.s = min(avail_w / (dlon * self.cos), avail_h / dlat)
        self.map_w, self.map_h = dlon * self.cos * self.s, dlat * self.s
        self.x0 = left + (avail_w - self.map_w) / 2
        self.y0 = top + (avail_h - self.map_h) / 2

    def xy(self, lon: float, lat: float) -> tuple[float, float]:
        return (self.x0 + (lon - self.minlon) * self.cos * self.s,
                self.y0 + (self.maxlat - lat) * self.s)

    def inside(self, lon: float, lat: float) -> bool:
        return self.minlon <= lon <= self.maxlon and self.minlat <= lat <= self.maxlat


def _ring_path(ring, proj: Projection) -> str:
    pts = [proj.xy(x, y) for x, y in ring]
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"


def _bbox_intersects(ring, box) -> bool:
    xs = [p[0] for p in ring]
    ys = [p[1] for p in ring]
    return not (max(xs) < box[0] or min(xs) > box[2] or max(ys) < box[1] or min(ys) > box[3])


def shade_colour(value: float) -> str:
    """Band colour for a 0..100 value; bands are finer below 25% because composition sub-labels live there."""
    v = max(0.0, min(100.0, float(value)))
    for col, (lo, hi) in zip(RAMP, RAMP_BANDS):
        if v < hi:
            return col
    return RAMP[-1]


# ----------------------------------------------------------------------------- map render

def _wrap(text: str, max_chars: int) -> list[str]:
    """Greedy word wrap for footer text (approximate: ~5.3 px per char at 10 px font)."""
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > max_chars:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}" if cur else w
    if cur:
        lines.append(cur)
    return lines or [""]


def _ring_centre(ring) -> tuple[float, float]:
    xs = [p[0] for p in ring]
    ys = [p[1] for p in ring]
    return (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2


def _hexid(colour: str) -> str:
    return "".join(ch for ch in colour if ch.isalnum())


def _halo_text(x: float, y: float, inner: str, attrs: str) -> str:
    """Text drawn twice: a white stroked copy underneath, the coloured copy on top. Works in every rasteriser,
    unlike paint-order, which some render as a white blob over the glyphs."""
    base = re.sub(r'\s*(?:fill|class)="[^"]*"', "", attrs)
    return (f'<text class="halo" x="{x:.1f}" y="{y:.1f}" {base} fill="#fff" stroke="#fff" stroke-width="3.5" stroke-linejoin="round">{inner}</text>'
            f'<text x="{x:.1f}" y="{y:.1f}" {attrs}>{inner}</text>')


def render_map(spec: dict) -> str:
    """Draw the map panel at width x height, then append a footer sized to its legend, key and notes."""
    if not isinstance(spec, dict):
        raise SpecError("spec must be a JSON object")
    width = int(spec.get("width", 1200))
    panel_h = int(spec.get("height", 640))
    name, box = resolve_extent(spec.get("extent", "world"))
    top, side = 64, 40
    proj = Projection(box, width, panel_h, margin=(top, side, 12, side))
    countries = load_outlines(name, box)
    shade = {}
    for s in spec.get("shade", []) or []:
        key = str(s.get("country", "")).strip().lower()
        if not key:
            raise SpecError("each shade entry needs a country")
        shade[key] = s
    routes = spec.get("routes", []) or []
    for i, r in enumerate(routes):
        if len(r.get("waypoints") or []) < 2:
            raise SpecError(f"route {r.get('label', i)!r} needs at least two waypoints")
    route_colours = [r.get("color") or GROUP_COLOURS[i % len(GROUP_COLOURS)] for i, r in enumerate(routes)]
    # --- footer content (computed first so the canvas can be sized to fit it)
    groups = {}
    for p in spec.get("points", []) or []:
        g = str(p.get("group", "")) or "default"
        groups.setdefault(g, GROUP_COLOURS[len(groups) % len(GROUP_COLOURS)])
    legend = list(spec.get("legend", []) or [])
    for g, colour in groups.items():
        if g != "default" and not any(l.get("label") == g for l in legend):
            legend.append({"color": colour, "label": g})
    for r, colour in zip(routes, route_colours):
        if r.get("label") and not any(l.get("label") == r["label"] for l in legend):
            legend.append({"color": colour, "label": r["label"], "line": True, "dash": r.get("dash", "")})
    if shade:
        legend.append({"ramp": True, "label": "shading: " + " / ".join(f"{a}–{b}%" for a, b in RAMP_BANDS)})
    max_chars = int((width - 2 * side) / 5.3)
    key_lines = []   # (colour, text) numbered waypoint key, one entry per labelled waypoint, wrapped
    n = 0
    for r, colour in zip(routes, route_colours):
        for w in r.get("waypoints") or []:
            lab, when = str(w.get("label", "")).strip(), str(w.get("when", "")).strip()
            if not (lab or when):
                continue   # an unlabelled waypoint only shapes the line
            n += 1
            text = f"{n}. {lab}" + (f" — {when}" if when else "")
            for k, line in enumerate(_wrap(text, max_chars - 4)):
                key_lines.append((colour if k == 0 else None, line))
    notes = list(spec.get("notes", []) or [])
    note_lines = []
    footer_h = 14 + 16 * len(legend) + (8 if key_lines else 0) + 13 * len(key_lines) + 8
    # --- canvas
    out = [None,  # svg element placeholder (height known at the end)
           '<defs>']
    for colour in sorted(set(route_colours)):
        out.append(f'<marker id="arrow-{_hexid(colour)}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
                   f'orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{colour}"/></marker>')
    out.append(f'<clipPath id="mapclip"><rect x="{proj.x0:.1f}" y="{proj.y0:.1f}" width="{proj.map_w:.1f}" height="{proj.map_h:.1f}"/></clipPath></defs>')
    bg_idx = len(out)
    out.append(None)  # background rect placeholder
    out.append(f'<rect x="{proj.x0:.1f}" y="{proj.y0:.1f}" width="{proj.map_w:.1f}" height="{proj.map_h:.1f}" fill="#dfe9f1" stroke="#9fb3c4"/>')
    out.append('<g clip-path="url(#mapclip)">')
    n_drawn = 0
    shaded_hits = set()
    value_labels = []
    for c in countries:
        key_n = (c.get("n") or "").lower()
        key_a = (c.get("a3") or "").lower()
        entry = shade.get(key_n) or shade.get(key_a)
        fill = shade_colour(entry["value"]) if entry and "value" in entry else "#f4f1ea"
        if entry:
            shaded_hits.add(key_n if key_n in shade else key_a)
        biggest = None
        for ring in c["rings"]:
            if not _bbox_intersects(ring, box):
                continue
            out.append(f'<path class="country" d="{_ring_path(ring, proj)}" fill="{fill}" stroke="#8c8c8c" stroke-width="0.6"/>')
            n_drawn += 1
            if biggest is None or len(ring) > len(biggest):
                biggest = ring
        if entry and "value" in entry and biggest is not None:
            cx, cy = _ring_centre(biggest)
            if proj.inside(cx, cy):
                x, y = proj.xy(cx, cy)
                value_labels.append(_halo_text(x, y, f'{float(entry["value"]):g}%',
                                               'class="value" text-anchor="middle" font-size="11" font-weight="bold" fill="#222"'))
    out.extend(value_labels)
    missing = [str(shade[k]["country"]) for k in sorted(set(shade) - shaded_hits)]
    # routes: line with arrowhead, numbered waypoint markers, names in the key below the map
    n = 0
    for r, colour in zip(routes, route_colours):
        wps = r.get("waypoints") or []
        pts = [proj.xy(float(w["lon"]), float(w["lat"])) for w in wps]
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        out.append(f'<path class="route" d="{d}" fill="none" stroke="{colour}" stroke-width="2.4" stroke-linejoin="round" '
                   f'stroke-dasharray="{r.get("dash", "")}" marker-end="url(#arrow-{_hexid(colour)})" opacity="0.9"/>')
        for (x, y), w in zip(pts, wps):
            if not (str(w.get("label", "")).strip() or str(w.get("when", "")).strip()):
                out.append(f'<circle class="bend" cx="{x:.1f}" cy="{y:.1f}" r="2.5" fill="{colour}"/>')
                continue
            n += 1
            out.append(f'<circle class="waypoint" cx="{x:.1f}" cy="{y:.1f}" r="8" fill="#fff" stroke="{colour}" stroke-width="2"/>')
            out.append(f'<text x="{x:.1f}" y="{y + 3.5:.1f}" text-anchor="middle" font-size="9.5" font-weight="bold" fill="{colour}">{n}</text>')
    # points: dot plus label; the label sits on the side with more room (toward the panel's centre)
    for i, p in enumerate(spec.get("points", []) or []):
        g = str(p.get("group", "")) or "default"
        x, y = proj.xy(float(p["lon"]), float(p["lat"]))
        colour = p.get("color") or groups[g]
        out.append(f'<circle class="point" cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{colour}" stroke="#fff" stroke-width="1.4"/>')
        lab, sub = escape(str(p.get("label", ""))), escape(str(p.get("sub", "")))
        if lab or sub:
            right = x < proj.x0 + proj.map_w / 2
            tx, anchor = (x + 8, "start") if right else (x - 8, "end")
            inner = lab + (f'<tspan x="{tx:.1f}" dy="12" font-size="10" fill="#555">{sub}</tspan>' if sub else "")
            out.append(_halo_text(tx, y + 4, inner, f'class="label" text-anchor="{anchor}" font-size="11.5" fill="#111"'))
    out.append('</g>')
    # titles
    if spec.get("title"):
        out.append(f'<text x="{width/2:.0f}" y="30" text-anchor="middle" font-size="22" font-weight="bold" fill="#111">{escape(str(spec["title"]))}</text>')
    if spec.get("subtitle"):
        out.append(f'<text x="{width/2:.0f}" y="50" text-anchor="middle" font-size="13" fill="#444">{escape(str(spec["subtitle"]))}</text>')
    # footer: legend, then the numbered key, then notes and attribution
    ly = proj.y0 + proj.map_h + 20
    lx = side
    for item in legend:
        if item.get("ramp"):
            for k, col in enumerate(RAMP):
                out.append(f'<rect x="{lx + k*14:.1f}" y="{ly - 9:.1f}" width="14" height="10" fill="{col}" stroke="#999" stroke-width="0.4"/>')
            out.append(f'<text x="{lx + 14*len(RAMP) + 6:.1f}" y="{ly:.1f}" font-size="11" fill="#333">{escape(str(item["label"]))}</text>')
        elif item.get("line"):
            out.append(f'<line x1="{lx:.1f}" y1="{ly - 4:.1f}" x2="{lx + 22:.1f}" y2="{ly - 4:.1f}" stroke="{item["color"]}" stroke-width="2.6" stroke-dasharray="{item.get("dash", "")}"/>')
            out.append(f'<text x="{lx + 28:.1f}" y="{ly:.1f}" font-size="11" fill="#333">{escape(str(item["label"]))}</text>')
        else:
            out.append(f'<circle cx="{lx + 6:.1f}" cy="{ly - 4:.1f}" r="5" fill="{item.get("color", "#333")}"/>')
            out.append(f'<text x="{lx + 16:.1f}" y="{ly:.1f}" font-size="11" fill="#333">{escape(str(item["label"]))}</text>')
        ly += 16
    if key_lines:
        ly += 6
        for colour, line in key_lines:
            if colour:
                out.append(f'<circle cx="{lx + 4:.1f}" cy="{ly - 3.5:.1f}" r="3.5" fill="{colour}"/>')
            out.append(f'<text class="key" x="{lx + 12:.1f}" y="{ly:.1f}" font-size="10.5" fill="#222">{escape(line)}</text>')
            ly += 13
    if missing:
        notes.append("shade entries not found in the map data: " + ", ".join(missing))
    notes.append("Map outlines: Natural Earth (public domain), simplified. Equirectangular projection; "
                 "routes are schematic lines between named places, not travelled paths.")
    for note in notes:
        note_lines.extend(_wrap(note, max_chars))
    ly += 4
    for line in note_lines:
        out.append(f'<text class="note" x="{lx:.1f}" y="{ly:.1f}" font-size="10" fill="#666">{escape(line)}</text>')
        ly += 12
    height = int(ly + 6)
    out[0] = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
              f'font-family="Helvetica, Arial, sans-serif">')
    out[bg_idx] = f'<rect width="{width}" height="{height}" fill="#ffffff"/>'
    out.append('</svg>')
    if n_drawn == 0:
        raise SpecError("no map outlines fall inside the extent")
    return "\n".join(out)


# ----------------------------------------------------------------------------- pedigree

def _is_living(p: dict) -> bool:
    if p.get("death"):
        return False
    b = str(p.get("birth", ""))
    digits = "".join(ch for ch in b if ch.isdigit())[:4]
    if len(digits) == 4:
        try:
            return int(digits) > datetime.date.today().year - 100
        except ValueError:
            return True
    return True


def render_pedigree(persons: dict, generations: int = 5, redact: bool = False, title: str = "") -> str:
    if not isinstance(persons, dict):
        raise SpecError("pedigree input must be a JSON object keyed by ahnentafel number")
    generations = max(2, min(8, int(generations)))
    box_w, box_h, gap_x = 190, 46, 70
    left, top = 40, 60
    col_count = generations
    rows_last = 2 ** (generations - 1)
    height = top + rows_last * (box_h + 8) + 60
    width = left + col_count * (box_w + gap_x) + 20
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="Helvetica, Arial, sans-serif">',
           f'<rect width="{width}" height="{height}" fill="#fff"/>']
    if title:
        out.append(f'<text x="{left}" y="34" font-size="20" font-weight="bold" fill="#111">{escape(title)}</text>')
    pos = {}
    for g in range(generations):
        count = 2 ** g
        slot = (height - top - 40) / count
        x = left + g * (box_w + gap_x)
        for k in range(count):
            n = count + k
            y = top + slot * k + slot / 2 - box_h / 2
            pos[n] = (x, y)
            p = persons.get(str(n))
            if p is None:
                out.append(f'<rect class="unknown" x="{x}" y="{y:.1f}" width="{box_w}" height="{box_h}" fill="#fafafa" stroke="#aaa" stroke-dasharray="4 3"/>')
                out.append(f'<text x="{x + 8}" y="{y + 20:.1f}" font-size="11" fill="#888">#{n} unknown</text>')
                out.append(f'<text x="{x + 8}" y="{y + 36:.1f}" font-size="10" fill="#aaa">{"father of" if n % 2 == 0 else "mother of"} #{n // 2}</text>')
                continue
            name = str(p.get("name", "")) or "(no name)"
            dates = " - ".join(x for x in (str(p.get("birth", "")), str(p.get("death", ""))) if x) or ""
            place = str(p.get("place", ""))
            if redact and _is_living(p):
                name, dates, place = "living", "", ""   # a birth year plus a place still identifies a living person
            out.append(f'<rect class="person" x="{x}" y="{y:.1f}" width="{box_w}" height="{box_h}" fill="#f4f1ea" stroke="#555"/>')
            out.append(f'<text x="{x + 8}" y="{y + 18:.1f}" font-size="12" font-weight="bold" fill="#111">#{n} {escape(name)}</text>')
            out.append(f'<text x="{x + 8}" y="{y + 32:.1f}" font-size="10" fill="#333">{escape(dates)}</text>')
            if place:
                out.append(f'<text x="{x + 8}" y="{y + 43:.1f}" font-size="9.5" fill="#555">{escape(place[:40])}</text>')
    for n, (x, y) in pos.items():
        for parent in (2 * n, 2 * n + 1):
            if parent in pos:
                px, py = pos[parent]
                out.append(f'<path class="link" d="M{x + box_w},{y + box_h/2:.1f} C{x + box_w + gap_x/2},{y + box_h/2:.1f} {px - gap_x/2},{py + box_h/2:.1f} {px},{py + box_h/2:.1f}" fill="none" stroke="#999" stroke-width="1.2"/>')
    out.append(f'<text x="{left}" y="{height - 14}" font-size="10" fill="#666">Ahnentafel numbering: a person n has father 2n and mother 2n+1. Dashed boxes are unproven or unknown ancestors.</text>')
    out.append('</svg>')
    return "\n".join(out)


# ----------------------------------------------------------------------------- demo + tests

DEMO_MAP = {
    "title": "Deep ancestry routes (synthetic demo)",
    "subtitle": "schematic routes between named places; dates are placeholders",
    "extent": "atlantic",
    "routes": [
        {"label": "paternal line (Y-DNA), demo", "color": "#b5452c",
         "waypoints": [{"lon": 45.0, "lat": 48.0, "label": "Steppe", "when": "demo date A"},
                       {"lon": 12.0, "lat": 49.0, "label": "Central Europe", "when": "demo date B"},
                       {"lon": -8.5, "lat": 52.0, "label": "Ireland", "when": "demo date C"}]},
        {"label": "maternal line (mtDNA), demo", "color": "#2a5d8f", "dash": "6 4",
         "waypoints": [{"lon": 38.0, "lat": 34.0, "label": "Near East", "when": "demo date D"},
                       {"lon": 23.0, "lat": 40.0, "label": "Aegean", "when": "demo date E"},
                       {"lon": -2.0, "lat": 53.0, "label": "Britain", "when": "demo date F"}]},
    ],
    "shade": [{"country": "Ireland", "value": 90}, {"country": "GBR", "value": 60}, {"country": "France", "value": 10}],
    "points": [{"lon": -8.47, "lat": 51.9, "label": "Cork", "sub": "demo b. 18xx", "group": "paternal"},
               {"lon": -73.9, "lat": 40.7, "label": "New York", "sub": "demo arr. 18xx", "group": "paternal"}],
    "notes": ["Demo data only. A real map lists its sources here, one per line."],
}
DEMO_PEDIGREE = {
    "1": {"name": "Demo Person", "birth": "1982", "place": "Demo City"},
    "2": {"name": "Demo Father", "birth": "1950", "place": "Demo Town"},
    "3": {"name": "Demo Mother", "birth": "1952", "death": "2010", "place": "Demo Village"},
    "4": {"name": "Demo Grandfather", "birth": "1920", "death": "1990", "place": "Demo County"},
    "6": {"name": "Demo Maternal Grandfather", "birth": "1918", "death": "1980"},
    "7": {"name": "Demo Maternal Grandmother", "birth": "1922", "death": "2001"},
}


def write_demo(outdir: str) -> list[str]:
    os.makedirs(outdir, exist_ok=True)
    paths = []
    for fn, obj in (("demo_map_spec.json", DEMO_MAP), ("demo_pedigree.json", DEMO_PEDIGREE)):
        p = os.path.join(outdir, fn)
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(obj, fh, indent=2)
        paths.append(p)
    p = os.path.join(outdir, "demo_map.svg")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(render_map(DEMO_MAP))
    paths.append(p)
    p = os.path.join(outdir, "demo_pedigree.svg")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(render_pedigree(DEMO_PEDIGREE, 4, title="Demo pedigree"))
    paths.append(p)
    return paths


def self_test() -> int:
    import xml.etree.ElementTree as ET
    failures: list[str] = []
    total = 0

    def check(name, cond):
        nonlocal total
        total += 1
        if not cond:
            failures.append(name)

    def parse(svg):
        return ET.fromstring(svg)

    NS = "{http://www.w3.org/2000/svg}"

    def count(root, cls):
        return sum(1 for e in root.iter() if e.get("class") == cls)

    # projection
    pr = Projection((-10.0, 50.0, 10.0, 60.0), 1200, 720)
    x1, y1 = pr.xy(-10.0, 60.0)
    x2, y2 = pr.xy(10.0, 50.0)
    check("projection: top-left corner of the extent maps to the map origin", abs(x1 - pr.x0) < 1e-6 and abs(y1 - pr.y0) < 1e-6)
    check("projection: bottom-right corner maps to origin + map size", abs(x2 - (pr.x0 + pr.map_w)) < 1e-6 and abs(y2 - (pr.y0 + pr.map_h)) < 1e-6)
    check("projection: a degree of longitude is cos(midlat) of a degree of latitude", abs((pr.xy(1, 55)[0] - pr.xy(0, 55)[0]) / (pr.xy(0, 55)[1] - pr.xy(0, 56)[1]) - math.cos(math.radians(55))) < 1e-9)
    check("projection: inside() respects the box", pr.inside(0, 55) and not pr.inside(20, 55))
    # shading ramp
    check("shade: 0 -> lightest, 100 -> darkest, six bands finer below 25%", shade_colour(0) == RAMP[0] and shade_colour(100) == RAMP[-1]
          and [RAMP.index(shade_colour(v)) for v in (0, 0.9, 1, 4.9, 5, 9.9, 10, 24.9, 25, 49.9, 50, 100)] == [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    # outlines
    for ext in ("world", "atlantic", "europe", "ireland-britain"):
        svg = render_map({"extent": ext})
        root = parse(svg)
        check(f"map {ext}: well-formed SVG with outlines", count(root, "country") > 0)
    root = parse(render_map({"extent": "ireland-britain"}))
    check("ireland-britain: a handful of countries, not the whole world", 0 < count(root, "country") < 40)
    # full demo
    svg = render_map(DEMO_MAP)
    root = parse(svg)
    check("demo: two routes drawn", count(root, "route") == 2)
    check("demo: six waypoints", count(root, "waypoint") == 6)
    check("demo: two points", count(root, "point") == 2)
    check("demo: route label text present", "paternal line (Y-DNA), demo" in svg)
    check("demo: shaded Ireland uses the top ramp colour", f'fill="{RAMP[-1]}"' in svg)
    check("demo: shaded countries carry a value label", count(root, "value") == 3 and "90%" in svg and "10%" in svg)
    check("demo: numbered waypoint key lists every waypoint", count(root, "key") >= 6 and "1. Steppe" in svg and "6. " in svg)
    check("demo: arrowheads are per-colour markers, not context-stroke", "context-stroke" not in svg and 'id="arrow-b5452c"' in svg)
    check("demo: the shade legend names the bands", "0–1% / 1–5%" in svg)
    edge = render_map({"extent": [-12, 50, 0, 56], "points": [{"lon": -0.5, "lat": 53, "label": "east"}, {"lon": -11.5, "lat": 53, "label": "west"}]})
    check("a point label sits on the side with room: east edge anchors end, west edge anchors start",
          'text-anchor="end" font-size="11.5" fill="#111">east' in edge and 'text-anchor="start" font-size="11.5" fill="#111">west' in edge)
    check("labels use a halo copy, never paint-order", "paint-order" not in svg and count(root, "halo") == count(root, "value") + count(root, "label"))
    bent = render_map(dict(DEMO_MAP, routes=[{"label": "r", "waypoints": [{"lon": 0, "lat": 50, "label": "A"}, {"lon": 5, "lat": 50}, {"lon": 10, "lat": 50, "label": "B"}]}]))
    check("an unlabelled waypoint bends the line but gets no number or key entry",
          count(parse(bent), "waypoint") == 2 and count(parse(bent), "bend") == 1 and ">2. B" in bent and ">3. " not in bent)
    tall = render_map(dict(DEMO_MAP, notes=DEMO_MAP["notes"] + ["x " * 400]))
    check("footer grows with the notes instead of overlapping them",
          int(parse(tall).get("height")) > int(root.get("height")) and count(parse(tall), "note") >= count(root, "note") + 4)
    check("demo: ISO code GBR resolves to a shade", "shade entries not found" not in svg)
    check("demo: attribution footer present", "Natural Earth" in svg)
    pr2 = Projection(EXTENTS["atlantic"], 1200, 640, margin=(64, 40, 12, 40))
    cx, cy = pr2.xy(-8.47, 51.9)
    check("demo: Cork point lands at the projected coordinate", f'cx="{cx:.1f}" cy="{cy:.1f}"' in svg)
    # unknown shade country is reported, not silently dropped
    svg_m = render_map({"extent": "europe", "shade": [{"country": "Atlantis", "value": 50}]})
    check("unknown shade country is named in the footer", "Atlantis" in svg_m)
    # escaping
    svg_e = render_map({"extent": "europe", "points": [{"lon": 0, "lat": 50, "label": "A & B <C>"}]})
    check("labels are XML-escaped", "A &amp; B &lt;C&gt;" in svg_e and parse(svg_e) is not None)
    # custom extent and errors
    check("custom box extent works", count(parse(render_map({"extent": [-12, 50, 0, 56]})), "country") > 0)
    check("a custom box inside Europe uses the finer outlines", len(load_outlines("custom", (-12, 50, 0, 56))) == len(load_outlines("europe"))
          and len(load_outlines("custom", (-120, 10, 60, 72))) == len(load_outlines("world")))
    for bad, why in (({"extent": "mars"}, "unknown extent"), ({"extent": [10, 50, 0, 56]}, "min < max"),
                     ({"routes": [{"waypoints": [{"lon": 0, "lat": 0}]}]}, "at least two waypoints"),
                     ({"shade": [{"value": 5}]}, "needs a country")):
        try:
            render_map(bad)
            check(f"spec error raised for {bad}", False)
        except SpecError as e:
            check(f"spec error raised for {bad}, naming the defect", why in str(e))
    try:
        render_map({"extent": [-40, 30, -35, 35]})
        check("empty extent (no outlines) is an error", False)
    except SpecError:
        check("empty extent (no outlines) is an error", True)
    # pedigree
    svg_p = render_pedigree(DEMO_PEDIGREE, 4, title="T")
    root = parse(svg_p)
    check("pedigree: 15 slots over four generations", count(root, "person") + count(root, "unknown") == 15)
    check("pedigree: known persons drawn solid, missing dashed", count(root, "person") == 6 and count(root, "unknown") == 9)
    check("pedigree: links from each known child to each known parent", count(root, "link") == 15 - 1)
    check("pedigree: names present when not redacted", "Demo Father" in svg_p)
    svg_r = render_pedigree(DEMO_PEDIGREE, 4, redact=True)
    check("pedigree: --redact hides living people and keeps the dead", "Demo Father" not in svg_r and "Demo Mother" in svg_r and "living" in svg_r)
    check("pedigree: --redact also drops a living person's dates and place",
          str(DEMO_PEDIGREE["2"]["birth"]) not in svg_r and str(DEMO_PEDIGREE["2"].get("place", "zz")) not in svg_r
          and str(DEMO_PEDIGREE["2"]["birth"]) in svg_p)
    check("pedigree: living means born within the last hundred years with no death date",
          _is_living({"birth": str(datetime.date.today().year - 30)}) and not _is_living({"birth": "1850"})
          and not _is_living({"birth": str(datetime.date.today().year - 30), "death": "2020"}) and _is_living({}))
    check("pedigree: generations are clamped to 2..8", count(parse(render_pedigree(DEMO_PEDIGREE, 1)), "person") + count(parse(render_pedigree(DEMO_PEDIGREE, 1)), "unknown") == 3)
    # demo writer + CLI
    with tempfile.TemporaryDirectory() as td:
        paths = write_demo(td)
        check("demo writes four files", len(paths) == 4 and all(os.path.getsize(p) > 100 for p in paths))
        import io, contextlib
        def run(argv):
            o, e = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(o), contextlib.redirect_stderr(e):
                rc = main(argv)
            return rc, o.getvalue(), e.getvalue()
        rc, _, _ = run(["map", os.path.join(td, "demo_map_spec.json"), "-o", os.path.join(td, "m.svg")])
        check("CLI map renders, exit 0", rc == 0 and os.path.getsize(os.path.join(td, "m.svg")) > 1000)
        rc, _, _ = run(["pedigree", os.path.join(td, "demo_pedigree.json"), "-o", os.path.join(td, "p.svg"), "--generations", "5"])
        check("CLI pedigree renders, exit 0", rc == 0 and os.path.getsize(os.path.join(td, "p.svg")) > 1000)
        with open(os.path.join(td, "bad.json"), "w") as fh:
            fh.write("{not json")
        rc, _, err = run(["map", os.path.join(td, "bad.json"), "-o", os.path.join(td, "x.svg")])
        check("unreadable spec -> exit 2 with the reason", rc == 2 and "ERROR" in err)
        rc, _, _ = run(["map", os.path.join(td, "missing.json"), "-o", os.path.join(td, "x.svg")])
        check("missing spec -> exit 2", rc == 2)
        check("no arguments -> exit 5", run([])[0] == 5)
    print(f"self-test: {total - len(failures)}/{total} checks passed")
    for f in failures:
        print(f"  FAILED: {f}")
    return 0 if not failures else 1


# ----------------------------------------------------------------------------- main

def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", nargs="?", choices=["map", "pedigree", "demo"])
    ap.add_argument("input", nargs="?", help="spec JSON (map/pedigree)")
    ap.add_argument("-o", "--out", help="output .svg (map/pedigree) or directory (demo)")
    ap.add_argument("--generations", type=int, default=5)
    ap.add_argument("--redact", action="store_true", help="replace living people's names with 'living'")
    ap.add_argument("--title", default="")
    ap.add_argument("--self-test", action="store_true")
    try:
        args = ap.parse_args(argv)
    except SystemExit:
        return 5
    if args.self_test:
        return self_test()
    if not args.mode:
        print("provide a mode: map | pedigree | demo (or --self-test)", file=sys.stderr)
        return 5
    if args.mode == "demo":
        for p in write_demo(args.out or "lineage-demo"):
            print(p)
        return 0
    if not args.input or not args.out:
        print("map/pedigree need an input spec and -o output", file=sys.stderr)
        return 5
    try:
        with open(args.input, encoding="utf-8") as fh:
            spec = json.load(fh)
    except (OSError, ValueError) as e:
        print(f"ERROR: cannot read spec: {e}", file=sys.stderr)
        return 2
    try:
        svg = render_map(spec) if args.mode == "map" else render_pedigree(spec, args.generations, args.redact, args.title)
    except SpecError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        sys.exit(130)
