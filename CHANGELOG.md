# CHANGELOG.md — F&F SEO Project

## [2026-10-31] — Phase 0: SEO Audit
### Added
- AUDIT.md with full technical and content audit results.
- AGENTS.md with project rules and SEO guidelines.

### Validated
- Lighthouse: Performance 100, Accessibility 100, Best Practices 100, SEO 100.
- 0 broken links, 0 missing assets, 0 orphans across 101 pages.

## [2026-10-31] — Phase 1: Technical SEO
### Added
- robots.txt with sitemap link and AI crawler allowances.
- sitemap.xml with 97 URLs.
- Canonical tags on all 101 pages.
- Schema.org: Organization, Service (13), FAQPage (40), Person (1), BreadcrumbList (100), Article (40).
- llms.txt for AEO/GEO.
- data.json for live metrics.

### Fixed
- Redirect chains: none (static hosting).
- LCP: hero image lazy/eager, fetchpriority.
- INP: deferred JS, no blocking scripts.
- CLS: width/height on images.

## [2026-10-31] — Phase 2: On-Page SEO & Content
### Added
- Unique Title/Description on all pages with local keywords.
- H1 on every page matching intent.
- 40 blog cards (8 articles + 32 guides) in blog.html.
- 32 enriched blog posts (350–580 words each).
- 8 long-form articles in articles/.
- Comparison pages (3) with "where competitor is stronger" block.
- JTBD pages: office-move, 152fz-prep, server-1c-saturday.
- Local geo pages (10 cities in Tatarstan).
- Service subpages (6), case pages (6).

### Fixed
- Duplicate titles (152fz-prep, server-1c-saturday).
- Removed invented statistics (70%/52% in backup article).

## [2026-10-31] — Phase 3: UX/UI & Conversion
### Added
- Terminal hero animation (./ff-it --status).
- Exit-intent popup (60s / 50% scroll / mouseleave).
- Footer signature ($ cat about-site.txt).
- Live metrics block (12 мин / 47 заявок / 0 инцидентов).
- Cookie banner with consent.
- privacy.html (152-ФЗ policy).
- Quiz with PDF download button.
- map.html (site map, 99 links).

### Fixed
- Color contrast (removed low-contrast decorative numbers).
- Heading order (h4→h3 in why-items, team cards, footer, timeline).
- CSP/X-Frame-Options meta removed (console errors).
- Lazy loading on all 217 images.

## [2026-10-31] — Phase 4: Deployment
### Added
- GitHub repository: https://github.com/Fedorov55/ff-site
- GitHub Pages: https://fedorov55.github.io/ff-site/
- README.md with run/deploy instructions.
