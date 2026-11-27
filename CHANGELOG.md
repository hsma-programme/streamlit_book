# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Dates formatted as YYYY-MM-DD as per [ISO standard](https://www.iso.org/iso-8601-date-and-time-format.html).

## v1.1.0 - 2026-11-25

Book content remains unchanged - but repository has been reorganised.

### Added

* Add GitHub action to automate build and deployment to GitHub pages.
* Add `CHANGELOG.md`, `README.md` and `CITATION.cff`.

### Changed

* All content for creating book moved into `book/`, to make it easier to navigate key files (`README.md, `requirements.txt`, etc.) in the repository root.
* Pinned packages in `requirements.txt`.
* Organised `assets/` into e.g., `images/`, `gif/`, etc.
* Moved fonts, logos, geojson, geopkg, bib and css into `assets/`.
* Moved csv files into `datasets/`.

### Removed

* Removed `docs/` and `_freeze/` folders plus some quarto render files for exercise 3 and 4 (as we now build from GitHub action, so don't need them, which in turn makes repository simpler/less stuff).
* Removed R webexercises as not used.
* Removed `test/`.

## v1.0.0 - 2025-05-13

Final version of book for HSMA-6.