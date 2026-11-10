#!/usr/bin/env python3
"""Rebuild the self-hosted web fonts in assets/fonts/.

The site ships subsets instead of the full families: Crimson Pro (upright and
italic variable fonts, Latin) and Ubuntu Mono (ASCII, it only sets the e-mail
lines), with every OpenType feature kept.

Usage:
    pip install fonttools brotli
    python tools/subset_fonts.py --crimson <dir with CrimsonPro[wght].ttf> \
                                 --ubuntu-mono <UbuntuMono-Regular.ttf>

Sources:
    https://github.com/google/fonts/tree/main/ofl/crimsonpro    (SIL OFL 1.1)
    https://github.com/google/fonts/tree/main/ufl/ubuntumono    (Ubuntu Font Licence 1.0)
"""
import argparse
import pathlib

from fontTools import subset
from fontTools.ttLib import TTFont

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "fonts"

# Basic Latin, Latin-1, Latin Extended-A (author names), and the handful of
# typographic marks the page uses (dashes, quotes, ellipsis, thin spaces, arrows).
LATIN = (
    "U+0020-007E,U+00A0-00FF,U+0100-017F,U+2009-200A,U+2010-2015,U+2018-201F,"
    "U+2020-2022,U+2026,U+202F,U+2032-2033,U+2039-203A,U+2190-2193,U+2197,U+2212"
)
ASCII = "U+0020-007E"

CRIMSON = {
    "CrimsonPro[wght].ttf": "crimson-pro.woff2",
    "CrimsonPro-Italic[wght].ttf": "crimson-pro-italic.woff2",
}


def run_subset(src, dst, unicodes):
    options = subset.Options()
    options.flavor = "woff2"
    options.layout_features = ["*"]
    options.name_IDs = [0, 1, 2, 3, 4, 5, 6, 13, 14]
    options.notdef_outline = True
    font = TTFont(src)
    subsetter = subset.Subsetter(options)
    subsetter.populate(unicodes=subset.parse_unicodes(unicodes))
    subsetter.subset(font)
    font.flavor = "woff2"
    font.save(dst)
    print(f"  {dst.name:28s} {dst.stat().st_size / 1024:6.1f} KB")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--crimson", type=pathlib.Path, help="directory containing CrimsonPro[wght].ttf and CrimsonPro-Italic[wght].ttf")
    ap.add_argument("--ubuntu-mono", type=pathlib.Path, help="path to UbuntuMono-Regular.ttf")
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    if args.crimson:
        print("Crimson Pro")
        for src, dst in CRIMSON.items():
            run_subset(args.crimson / src, OUT / dst, LATIN)

    if args.ubuntu_mono:
        print("Ubuntu Mono")
        run_subset(args.ubuntu_mono, OUT / "ubuntu-mono.woff2", ASCII)


if __name__ == "__main__":
    main()
