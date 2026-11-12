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
- GitHub Pages: https://ff-it.ru/
- README.md with run/deploy instructions.


## [2026-10-31] — Security Audit & Hardening
### Added
- SECURITY.md — security policy, vulnerability reporting, developer checklist.
- SECURITY_AUDIT.md — full audit table with findings and fixes.
- .well-known/security.txt (RFC 9116).
- CSP meta tag on all 101 pages.
- Referrer-Policy meta tag on all pages.
- Honeypot field in all forms (101 pages).
- Consent checkbox on contact form and quiz.

### Fixed
- Removed external Google Fonts (14 pages) — now uses local fonts.
- Removed Chart.js CDN from demo.html.
- Removed CSP/X-Frame-Options meta that caused console errors.
- Removed low-contrast decorative numbers (accessibility).

### Documented
- GitHub Pages limitation: no custom HTTP headers.
- Recommended headers for migration to Cloudflare Pages/Netlify.

### Validated
- Lighthouse: Performance 100, Accessibility 100, Best Practices 100, SEO 100.
- 0 console errors.
- 0 secrets in repository.
- 0 dangerous patterns (eval, document.write, Function()).

## [2026-10-31] — Performance & Responsiveness
### Added
- design-system.css: tokens, reveals, grain, micro-interactions, contain, content-visibility.
- PERFORMANCE_AUDIT.md with Lighthouse results.
- width/height on all 217 images (was 7 missing).
- noscript fallbacks on key pages.

### Fixed
- Color contrast: terminal text and decorative numbers.
- External fonts/CDN removed (local fonts only).

### Validated
- Lighthouse: Performance 100, Accessibility 100, Best Practices 100, SEO 100.
- LCP 1.3s, INP 10ms, CLS 0.004, TBT 10ms.
- No horizontal scroll at 320px.
- 0 console errors.

## [2026-10-31] — Code Quality & Production Readiness
### Added
- .eslintrc.json + eslint.config.mjs (ESLint flat config).
- .htmlhintrc (HTMLHint config).
- .github/workflows/quality.yml (CI: ESLint + HTMLHint + node --check).
- CODE_AUDIT.md — full code audit results.
- .nojekyll for dotfile serving.

### Fixed
- Duplicate aria-live on cookie banner (14 pages).
- ESLint errors: contactForm not defined, location not defined (added to globals).
- HTMLHint: 0 errors on 101 pages.

### Validated
- ESLint: 0 errors, 25 warnings (unused catch variables).
- HTMLHint: 0 errors on 101 files.
- node --check: 0 errors.
- Lighthouse: Performance 100, Accessibility 100, Best Practices 100, SEO 100.
- 0 console errors, 0 broken links.


## [2026-11-09] — Deep audit & fixes
### Fixed
- script.js: removed ReferenceError sources (tgBtn, runSaturdayScenario, updateMbar).
- script.js: ym calls guarded via window.ym.
- Schema: converted LocalBusiness/ProfessionalService to Organization (no office per AGENTS.md); removed PostalAddress, openingHours, priceRange.
- Fixed aggregateRating reviewCount to match actual reviews (3).
- Meta: added og:title/twitter:card to consent, cookie, privacy, terms, map.
- map.html: fixed garbage meta description.
- style.css: changed font-display from block to optional (reduce CLS).
- All JS passes eslint (0 errors) and node --check.
### Validated
- 164 HTML pages: 0 broken internal links, 0 missing required meta, 0 invalid schema (518 blocks).
- 0 images missing alt/dimensions.
- noindex only on 404 + service/legal pages.
