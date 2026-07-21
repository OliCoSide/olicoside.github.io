# olicoside.github.io — Olivier Côté's academic website

Personal academic website of **Olivier Côté, ACAS** — Ph.D. candidate in Actuarial Science at Université Laval, working on fairness and discrimination in insurance predictive models.

**Live site:** [https://olicoside.github.io](https://olicoside.github.io)

## What's on the site

- **About** — research overview and recent highlights (homepage)
- **Publications** — papers with links, generated from the files in `_publications/`
- **Talks** — presentations and seminars, generated from `_talks/`
- **Teaching** — courses taught, generated from `_teaching/`
- **CV** — online version at `/cv/` plus a downloadable PDF

## Repository structure

| Path | Purpose |
|------|---------|
| `_config.yml` | Site-wide settings (name, bio, social links, sidebar) |
| `_pages/` | Main pages (`about.md` is the homepage, `cv.md` is the online CV) |
| `_publications/`, `_talks/`, `_teaching/` | One markdown file per item; they populate the corresponding pages |
| `_data/navigation.yml` | Order and content of the top navigation bar |
| `_sass/` | Styling (see `_custom.scss` for the site's custom design layer) |
| `files/` | Downloadable files, most importantly the CV PDF |
| `files/cv-src/` | LaTeX source of the CV (`.tex` + `biblio.bib`) |
| `files/archive/` | Previous CV versions, kept for reference |
| `images/` | Profile picture and other images |

## Updating the CV

The CV lives in three places that should stay in sync:

1. **LaTeX source** — edit `files/cv-src/CV_latex_OC_20210914.tex` (and `biblio.bib` for papers)
2. **Production PDF** — recompile and replace `files/CV_OlivierCote_ENG_prod.pdf` (this is the file linked from the navbar and the CV page; keep the same filename so links never break)
3. **Online CV** — mirror the changes in `_pages/cv.md`

When replacing the production PDF, move the outgoing version into `files/archive/` rather than deleting it.

## Running the site locally

The site is built with [Jekyll](https://jekyllrb.com/) and deployed automatically by GitHub Pages on every push to `master`.

```bash
# with Ruby ≥ 3 installed
bundle install
bundle exec jekyll serve -l -H localhost
# → http://localhost:4000
```

Or with Docker, no Ruby required:

```bash
docker build -t jekyll-site .
docker run -p 4000:4000 --rm -v $(pwd):/usr/src/app jekyll-site
```

## Credits

Built on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) template (a fork of [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) © Michael Rose, MIT License). See `LICENSE` for details.
