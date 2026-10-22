# CV sync procedure

The CV lives in three places. Keep them in sync, in this order:

1. **LaTeX source**: `CV_latex_OC_20210914.tex` and `biblio.bib` in this
   folder. Add or update a paper as a `\bibentry{key}` in the
   Research Papers section and as a matching entry in `biblio.bib`
   (title, journal, year, DOI when available, `In press` note when
   applicable).
2. **Production PDF**: recompile and replace
   `../CV_OlivierCote_ENG_prod.pdf`, keeping that exact filename so the
   navbar and page links never break. Move the outgoing PDF into
   `../archive/` rather than deleting it.
3. **Online CV**: `_pages/cv.md` lists publications automatically from
   `_publications/`, so do not hand-edit that list. Instead, add or
   update the matching `_publications/*.md` file (title, `venue`,
   `venue_prefix` for status, `paperurl` for the DOI, `bibtex` block)
   and check that the homepage (`_pages/about.md`) still describes the
   status correctly.

## Automated check

Run this from the repo root before opening a PR that touches the CV:

```sh
python3 scripts/check_cv_sync.py
```

It checks, with no extra dependencies, that every published publication
has a matching BibTeX entry (and vice versa), that DOIs match when
present, that an "In press" BibTeX note matches an "In press at"
`venue_prefix`, and that every `\bibentry` key used in the LaTeX CV
exists in `biblio.bib`. The same check runs in CI
(`.github/workflows/site-check.yml`).

The check does **not** read the compiled PDF itself. After recompiling,
spot-check the PDF text (for example with `pdftotext`) for the new or
changed paper title, status, and DOI before merging.
