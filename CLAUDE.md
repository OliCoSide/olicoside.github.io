# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Personal academic website of Olivier Côté (Ph.D. candidate in Actuarial Science, Université Laval), live at https://olicoside.github.io. Built with Jekyll on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) template (a fork of Minimal Mistakes). This is a content site — there are no tests or linters.

## Build and deploy

- **Deployment is automatic**: every push to `master` triggers the GitHub Pages "pages build and deployment" workflow. There is no other CI.
- **Local preview** (Ruby ≥ 3): `bundle install`, then `bundle exec jekyll serve -l -H localhost` → http://localhost:4000. Note that `_config.yml` is NOT hot-reloaded; restart the server after changing it.
- **Docker alternative** (no Ruby needed): `docker build -t jekyll-site .` then `docker run -p 4000:4000 --rm -v $(pwd):/usr/src/app jekyll-site`.
- **JavaScript**: `assets/js/main.min.js` is a committed build artifact. Only if you edit `assets/js/_main.js` or the plugins, regenerate it with `npm install && npm run build:js`. Don't edit `main.min.js` directly.
- This file (`CLAUDE.md`) is listed in the `exclude` section of `_config.yml` so it is never published on the live site. Keep it that way.

## Architecture

Content lives in Jekyll **collections**, one markdown file per item, rendered by list pages in `_pages/`:

- `_publications/` → `/publications/` — front matter fields: `title`, `collection: publications`, `category` (e.g. `manuscripts`), `permalink`, `excerpt`, `date`, `venue`, `citation`, and `bibtex` (a literal BibTeX block). The `bibtex` field powers the copyable "BibTeX" pill rendered by `_includes/bibtex.html` on both list cards (`_includes/archive-single.html`) and item pages (`_layouts/single.html`). Every publication should have it.
- `_talks/` → `/talks/` — uses the `talk` layout.
- `_teaching/` → `/teaching/`.

Other key pieces:

- `_pages/about.md` is the homepage; `_pages/cv.md` is the online CV.
- `_data/navigation.yml` controls the top navbar (order and entries). The "CV" navbar entry links directly to the PDF, not to `/cv/`.
- `_config.yml` holds site-wide identity (name, bio, social links → sidebar via `_includes/author-profile.html`).
- `_includes/footer/custom.html` holds the site's custom footer: Sitemap/Stats links, the GoatCounter analytics snippet (privacy-friendly, cookie-free; site code `olicoside`), and the scroll-reveal script for list cards.
- `markdown_generator/` contains optional Jupyter/Python tooling that generates publication/talk markdown files from TSVs — not part of the build.

## Styling

All custom design lives in `_sass/_custom.scss` ("japandi refresh": warm paper palette, muted pine accent, hairline borders, quiet micro-animations). It is loaded last and overrides the theme defaults — make style changes there, not in the upstream theme partials. Animations must stay `prefers-reduced-motion`-safe and no-JS-safe (see the IntersectionObserver pattern in the footer).

## Pending talk→paper links (working papers not yet on the site)

When these working papers get a page in `_publications/`, add the matching talk pills:

- **"Causal decomposition" paper** (*Profiling Actuarial Discrimination via Causal Decomposition*): AFM 2026 poster (`2026-02-02-AFM`), CRDM (`2026-05-15-CRDM`), STATQAM (`2026-05-26-STATQAM`), 29th IME Congress Seoul (`2026-07-02-IME-Seoul`).
- **"Confounding bias" paper**: STATQAM (`2026-05-26-STATQAM`) — that seminar covered both working papers.

Hidden talks (extensionless files in `_talks/`, invisible to Jekyll) still awaiting an explicit assignment: `2022-05-15-jeda`, `2022-08-01-Summerday`, `2023-06-15-IDS`, `2024-01-29-IVADO`, `2024-02-01-WIM`, `2024-10-11-causaux`. `2023-10-25-intact` stays hidden on purpose: private company talks are only tallied anonymously via the `industry_talks` front-matter field on publications (see `_includes/archive-single.html`).

## Updating the CV — keep three places in sync

1. **LaTeX source**: `files/cv-src/CV_latex_OC_20210914.tex` (+ `biblio.bib` for papers).
2. **Production PDF**: recompile and replace `files/CV_OlivierCote_ENG_prod.pdf` — **keep this exact filename** so navbar and page links never break. Move the outgoing PDF into `files/archive/` rather than deleting it.
3. **Online CV**: mirror the changes in `_pages/cv.md`.
