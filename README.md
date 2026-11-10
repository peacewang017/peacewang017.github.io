# cyrusluo.site

Source of Zhengyang Luo's homepage, <https://cyrusluo.site>. A single Jekyll page
served by GitHub Pages; no JavaScript and no third-party requests.

## Editing

| What | Where |
|------|-------|
| Name, position, e-mail, profile links | `_config.yml` |
| About, research interests, experience, education | `index.md` |
| Papers | `_data/publications.yml` (optional `arxiv`, `pdf`, `code`, `page`, `bibtex` links) |
| Look of the page | `assets/css/ink.css`, `_layouts/homepage.html` |

## Preview

```sh
bundle install
bundle exec jekyll serve      # http://127.0.0.1:4000 — restart after editing _config.yml
```

## Generated assets

- `assets/fonts/` — Latin subsets built by `tools/subset_fonts.py`.
- `assets/img/verse-chu.svg` — the motto in Chu-script glyphs, built by
  `tools/build_verse_chu.py` from the picks in `tools/verse-chu.json`.

## Credits

- Type: [Crimson Pro](https://github.com/Fonthausen/CrimsonPro) (SIL OFL 1.1) and
  [Ubuntu Mono](https://design.ubuntu.com/font) (Ubuntu Font Licence 1.0); licence
  texts are in `assets/fonts/`.
- Chu-script, guwen and seal glyphs: [hanzi-glyphs-svg](https://github.com/zhouyongh/hanzi-glyphs-svg) (CC0 1.0).
- Seal characters: Shuowen small-seal forms from Wikimedia Commons (public domain).
- Icons: [Font Awesome Free](https://fontawesome.com/license/free) (CC BY 4.0); the
  arXiv icon is from [Academicons](https://jpswalsh.github.io/academicons/) (SIL OFL 1.1).
- The first version of this site was built on the
  [minimal-light](https://github.com/yaoyao-liu/minimal-light) theme.
