#!/usr/bin/env python3
"""Check that the three CV sources stay in sync.

Sources checked, all from the repo root:
  1. _publications/*.md front matter (title, venue, venue_prefix, paperurl)
  2. files/cv-src/biblio.bib (title, journal, year, doi, note)
  3. files/cv-src/CV_latex_OC_20210914.tex (\\bibentry{key} in Research Papers)

Rules:
  - Every published publication must have a matching BibTeX entry
    (normalised title) and vice versa.
  - A DOI in one source must match the DOI in the other, when present.
  - An "In press" BibTeX note must match an "In press at" venue_prefix
    on the publication page.
  - Every \\bibentry key used in the LaTeX CV must exist in biblio.bib.

This script uses only the standard library so the CI workflow can run
it with plain `python3`. It does not check the compiled PDF itself:
recompiling the PDF is a manual step (see files/cv-src/README.md).
Exit code 0 on success, 1 with a list of mismatches otherwise.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def norm(title):
    title = title.lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def parse_front_matter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fields = {}
    for line in text[3:end].splitlines():
        if ":" in line and not line.startswith(" ") and not line.startswith("\t"):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip("'\"")
    return fields


def parse_bib(text):
    entries = {}
    # Split on @type{key, ...} blocks; bib entries here are simple.
    for match in re.finditer(
        r"@\w+\{([^,]+),(.*?)\n\}", text, re.DOTALL
    ):
        key = match.group(1).strip()
        body = match.group(2)
        fields = {}
        for field in re.finditer(
            r"(\w+)\s*=\s*\{([^{}]*)\}", body
        ):
            fields[field.group(1).lower()] = field.group(2).strip()
        # Titles in biblio.bib sometimes contain LaTeX accents; keep raw.
        entries[key] = fields
    return entries


def doi_suffix(value):
    if not value:
        return ""
    match = re.search(r"10\.\d{4,}/[^\s\"'}]+", value)
    return match.group(0).rstrip(".,") if match else ""


def main():
    errors = []

    pubs = {}
    for path in sorted((ROOT / "_publications").glob("*.md")):
        fields = parse_front_matter(path.read_text(encoding="utf-8"))
        if fields.get("published", "").lower() == "false":
            continue
        if "title" in fields:
            pubs[norm(fields["title"])] = (path.name, fields)

    bib_text = (ROOT / "files" / "cv-src" / "biblio.bib").read_text(
        encoding="utf-8"
    )
    bib = parse_bib(bib_text)
    bib_by_title = {}
    for key, fields in bib.items():
        if "title" in fields:
            bib_by_title[norm(fields["title"])] = (key, fields)

    for title, (name, fields) in pubs.items():
        if title not in bib_by_title:
            errors.append(
                f"{name}: no matching BibTeX entry for "
                f"'{fields.get('title')}'"
            )
            continue
        key, bfields = bib_by_title[title]
        pub_doi = doi_suffix(fields.get("paperurl", ""))
        bib_doi = doi_suffix(
            bfields.get("doi", "") + " " + bfields.get("note", "")
        )
        if pub_doi and bib_doi and pub_doi != bib_doi:
            errors.append(
                f"{name}: DOI mismatch, publication {pub_doi} vs "
                f"bib {key} {bib_doi}"
            )
        if "in press" in bfields.get("note", "").lower():
            if fields.get("venue_prefix", "") != "In press at":
                errors.append(
                    f"{name}: bib note says In press but "
                    f"venue_prefix is '{fields.get('venue_prefix', '')}'"
                )

    for title, (key, fields) in bib_by_title.items():
        if title not in pubs:
            errors.append(
                f"bib {key}: no published publication page for "
                f"'{fields.get('title')}'"
            )

    tex = (ROOT / "files" / "cv-src" / "CV_latex_OC_20210914.tex").read_text(
        encoding="utf-8"
    )
    used_keys = re.findall(r"\\bibentry\{([^}]+)\}", tex)
    for key in used_keys:
        if key not in bib:
            errors.append(f"LaTeX CV uses \\bibentry{{{key}}} missing from biblio.bib")
    for key in bib:
        if key not in used_keys:
            errors.append(
                f"bib {key} is not used by any \\bibentry in the LaTeX CV"
            )

    if errors:
        print("CV sync check FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        f"CV sync check passed: {len(pubs)} publications, "
        f"{len(bib)} BibTeX entries, {len(used_keys)} bibentry keys."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
