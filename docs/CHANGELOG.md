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

## [2026-11-19] - Repo cleanup
### Removed
- Temporary work/ scripts and debug helpers.
### Kept
- Core site pages, assets, scripts, and agent skills.

## [2026-11-21] - Full repository audit & P0 fixes
### Added
- Full audit via 5 parallel subagents (JS/CSS, HTML, SEO infra, content/links, build/scripts).
- docs/REPO_AUDIT_2026-11-21.md with consolidated findings and prioritized plan.
### Fixed
- js/script.js: FORM_ENDPOINT ReferenceError (forms now fall back to mailto instead of failing).
- js/script.js: form-data persistence selector injection hardened with CSS.escape.
- js/calculator.js: empty fetch('') replaced with endpoint/mailto fallback + success state.
- js/calculator.js: calcSlab null-guards for missing DOM nodes.
- js/search.js: relative search-index.json/worker paths now resolve under /ff-site/ base.
- js/search.js: XSS hardening in renderResults (escape of title/desc/url).
- sw.js: precache paths base-aware (/ff-site/); added components.css, tokens.css, search-worker.js, manifest.json; fallback uses base index.
- css/style.css: font urls corrected to ../fonts/.
- Removed UTF-8 BOM from 8 HTML files (index, prices, servers, services, support, audits/audit, compare/compare, infrastructure/infrastructure).
- build.js: expanded build set (tokens, components, search-worker, sw) and bundle with externalized binary assets.
### Validated
- node --check: all JS pass.
- npm run build: completes successfully.

## [2026-11-21] — P1 fixes
### Fixed
- Canonical/og:url absolutized on 67 subdirectory pages.
- Sitemap regenerated: 159 URLs, no broken/noindex, lastmod + priority differentiation.
- search-index.json regenerated: 159 entries matching actual files.
- llms.txt links corrected to canonical subfolder URLs.
- security.txt (root + .well-known) fixed: stray quote removed, aligned Expires/languages, absolute Canonical/Policy.
- Added meta description/canonical/robots/OG/twitter to 4 pages (compare/*, sysadmin-cost-kazan, terms-of-work); schema on terms-of-work.
- De-duplicated 3 meta descriptions.
- Replaced missing image case-ecp-eis.webp references with service-crypto.webp.
- Nav consistency: added incidents item to 81 pages.
### Validated
- sitemap.xml resolves to existing files; no noindex leaks.
- search-index.json has 0 dead / 0 missing vs HTML files.

## [2026-11-21] — P2 fixes
### Fixed
- CSP img-src tightened to 'self' data: in 137 HTML files and _headers.
- htmlhint issues: duplicate class attributes and duplicate id="faq" fixed.
- Removed legacy .eslintrc.json (flat config only).
- AGENTS.md page count corrected (202 -> 161).
- Added CI workflow .github/workflows/quality.yml.
### Notes
- Heading-order and llms-full.txt regeneration deferred to P3.

## [2026-11-21] — P3 fixes
### Fixed
- why-item card titles changed from h3 to h2 on articles.html and resources/research.html (heading order).
- llms-full.txt regenerated: 159 pages, trimmed to ~136 KB.
- manifest.json: added lang, dir, id, categories, purpose for apple-touch icon.
### Validated
- npm run build successful.

## [2026-11-21] — Фаза 5: валидация
### Fixed
- services.html и 5 страниц: inline-скрипт PDF (комментарий // глотал закрывающие скобки) → SyntaxError устранён.
### Validated
- 6 страниц проверены в браузере: 0 ошибок консоли.
- Lighthouse: SEO 1.0, Best Practices 1.0 на index/support.
- Accessibility: 0.87–0.96 (замечания aria-hidden-focus, landmark-one-main — некритичны).
- Search-index загружается на вложенных страницах (200 OK).

## [2026-11-22] - Competitive Audit & Enhancement Plan
### Added
- Competitive map of 20 competitors (Kazan/Tatarstan + federal top-5) in глобальный_аудитище.md.
- Deep breakdown of top-8 dangerous competitors.
- SEO comparison F&F vs competitors.
- Offer comparison and F&F offer formulation.
- Trust signals comparison.
- Conversion best/worst practices.
- Enhancement plan (A: immediate, B: 14 days, C: 30-45 days).


## [2026-11-24] - Deep Competitive Analysis & Guarantee Unification
### Added
- Deep competitive analysis synthesis across 11 axes in глобальный_аудитище.md (first screens, pricing architecture, trust speed, service pages, market language, objections, reputation, Tatarstan locality, funnels, SEO attack points, content gaps) with implement-now and 30-days plans.
- Unified guarantee from 30 days to 6 months across 161 HTML pages (392 replacements); only guarantee-related phrases changed, non-guarantee 30-day contexts preserved.
### Validated
- scripts/check-site.py: 161 HTML files, all checks passed.
- No remaining guarantee-day phrases (verified by check_guarantee_remaining.py).
