#!/usr/bin/env python3
"""Build assets/img/verse-chu.svg: the motto set in Chu-script glyphs.

The glyphs are tracings of excavated Chu bamboo-slip and silk-manuscript
characters from https://github.com/zhouyongh/hanzi-glyphs-svg (CC0 1.0). The
picks, their sources and the pinned commit live in tools/verse-chu.json.
Nine characters of the verse are not attested in the Chu corpus; those fall
back to transmitted guwen ("chuanchao") or small seal forms, and get an outline
stroke so their thin lines sit closer in weight to the brush-written ones.

Usage:
    pip install fonttools
    python tools/build_verse_chu.py            # fetches glyphs into tools/.cache
"""
import json
import pathlib
import re
import urllib.request

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.svgLib.path import parse_path

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "assets" / "img" / "verse-chu.svg"
CACHE = HERE / ".cache" / "hanzi-glyphs-svg"

# Geometry, in output units. Columns run right to left.
CELL, PITCH_Y, PITCH_X, PAD = 200, 250, 330, 20
# Outline added to thin-line layers, in source (400-unit) space.
FAT = {"seal": 9, "chuanchao": 7}


def fetch(repo, commit, layer, name):
    local = CACHE / commit[:12] / layer / name
    if not local.exists():
        local.parent.mkdir(parents=True, exist_ok=True)
        url = f"https://raw.githubusercontent.com/{repo}/{commit}/glyphs/{layer}/{name}"
        req = urllib.request.Request(url, headers={"User-Agent": "homepage-build"})
        local.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    return local.read_text(encoding="utf-8")


def contours(svg):
    """Split every path into sub-paths so stray specks can be dropped."""
    result = []
    for d in re.findall(r'\sd="([^"]+)"', svg, flags=re.S):
        rec = RecordingPen()
        parse_path(d, rec)
        current = []
        for op, args in rec.value:
            if op == "moveTo" and current:
                result.append(current)
                current = []
            current.append((op, args))
        if current:
            result.append(current)
    out = []
    for ops in result:
        rec = RecordingPen()
        rec.value = ops
        bounds = BoundsPen(None)
        rec.replay(bounds)
        if bounds.bounds:
            out.append((rec, bounds.bounds))
    return out


def clean(svg):
    """Return the glyph's contours and bounding box, without scanner marks at the canvas edge."""
    cs = contours(svg)
    size = lambda b: max(b[2] - b[0], b[3] - b[1])
    strokes = [b for _, b in cs if size(b) >= 40] or [b for _, b in cs]
    x0, y0 = min(b[0] for b in strokes), min(b[1] for b in strokes)
    x1, y1 = max(b[2] for b in strokes), max(b[3] for b in strokes)
    keep = []
    for rec, b in cs:
        outside = b[2] < x0 - 6 or b[0] > x1 + 6 or b[3] < y0 - 6 or b[1] > y1 + 6
        if size(b) < 24 and outside:
            continue
        keep.append((rec, b))
    x0, y0 = min(b[0] for _, b in keep), min(b[1] for _, b in keep)
    x1, y1 = max(b[2] for _, b in keep), max(b[3] for _, b in keep)
    return [rec for rec, _ in keep], (x0, y0, x1, y1)


def main():
    spec = json.loads((HERE / "verse-chu.json").read_text(encoding="utf-8"))
    columns = spec["columns"]
    width = PAD * 2 + CELL + PITCH_X * (len(columns) - 1)
    height = PAD * 2 + CELL + PITCH_Y * (max(len(c) for c in columns) - 1)
    paths = []
    for ci, column in enumerate(columns):
        cx = width - PAD - CELL / 2 - ci * PITCH_X
        for ri, glyph in enumerate(column):
            recs, (x0, y0, x1, y1) = clean(fetch(spec["repo"], spec["commit"], glyph["layer"], glyph["file"]))
            w, h = x1 - x0, y1 - y0
            scale = CELL * glyph["size"] / max(w, h)
            cy = PAD + CELL / 2 + ri * PITCH_Y
            ox, oy = cx - (x0 + w / 2) * scale, cy - (y0 + h / 2) * scale
            pen = SVGPathPen(None, ntos=lambda v: str(int(round(v))))
            for rec in recs:
                rec.replay(TransformPen(pen, (scale, 0, 0, scale, ox, oy)))
            fat = glyph.get("fat", FAT.get(glyph["layer"], 0)) * scale
            stroke = f' stroke="#000" stroke-width="{fat:.1f}" stroke-linejoin="round"' if fat else ""
            paths.append(f'<path d="{pen.getCommands()}"{stroke}/>')
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">'
        + "".join(paths)
        + "</svg>\n"
    )
    OUT.write_text(svg, encoding="utf-8")
    print(f"{OUT.relative_to(HERE.parent)}: {width}x{height}, {len(svg) / 1024:.0f} KB, {sum(len(c) for c in columns)} glyphs")


if __name__ == "__main__":
    main()
