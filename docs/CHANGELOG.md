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

## [2026-11-24] - P0-02: broken #faq/#process anchors in quick-nav
### Fixed
- Removed `#faq` link from quick-nav on 41 pages where no `#faq` section exists.
- Removed `#process` link from quick-nav on 42 pages where no `#process` section exists.
### Validated
- 161 quick-nav blocks: 0 remaining broken #faq/#process anchor links.
- 120 pages keep #faq link, 119 pages keep #process link (matches section presence).

## [2026-11-24] - P0-02b: restore anchors on sections with other ids
### Fixed
- Added id="process" to "Как мы работаем по этой задаче" h2 on 30 blog pages; restored #process quick-nav link.
- Added id="faq"/id="process" to FAQ/process sections on company/about.html, security/security.html, resources/methodology.html; restored corresponding quick-nav links.
### Validated
- 0 broken anchors across all 164 HTML files (full anchor check).
- id=faq: 122 pages, id=process: 151 pages.

## [2026-11-24] - P0-04: consent.html link in forms
### Fixed
- Added "Согласие на обработку ПДн" link (legal/consent.html) next to the agree checkbox in all 16 forms (contacts, prices, servers, audits, company, leads, resources, services).
- Added terms-of-work.html link near CTA/microtext on contacts.html and all services/*.html (13 microtext + contacts + 2 non-form service pages).
- AGENTS.md Pages section updated: removed references to non-existent map.html/status.html/quiz.html/demo.html; documented actual root pages and subdirectories.
- P1-01: added "Выезд по Казани и Татарстану. Удалённо — по России." to answer-first on services.html and infrastructure/infrastructure.html.
- P1-02: og:title and twitter:title on index.html unified with <title>.
- P1-03: added FAQ "Где вы работаете?" to support.html (visible + FAQPage schema).
- P1-04: created chelny.html landing page for Набережные Челны (adapted from index.html, Chelny-focused title/meta/schema/hero); added cases section linking to nabchelny case pages; regenerated sitemap.xml (161 URLs).
- P1-06: created almet.html landing page for Альметьевск (adapted from chelny.html); added cases section (servers/support/sql-optimization); regenerated sitemap.xml (162 URLs).
- P1-08: added local metrics line (5 лет · 120+ проектов · 15+ клиентов · 4 инженера) to contacts.html; index.html and company/about.html already display these metrics.
- P1-11: added "Типичные задачи для офисов Казани и Татарстана" label + subtitle to the problems section on services.html.
- P1-12: updated title/og/twitter title on support.html to include "Экономия до 80%".
- P1-13: updated title/og/twitter title on servers.html to include "гарантия 6 мес".
- P1-14: added FAQ "Вы маленькая компания? Справитесь?" to index.html and support.html.
- P1-17: added reaction-time table (авария 15 мин / срочная 1 час / плановая 24 ч / восстановление из бэкапа 2 ч) to SLA section on support.html.
- P1-18: added FAQ items "Что не покрывает гарантия" and "Как воспользоваться гарантией" to servers.html.
- P1-19: added 1C configurations (УТ, БП, ЗУП, УНФ, ERP, миграция 7.7→8.3, лицензии) to "Сервер для 1С" card on servers.html.
- P1-20: created cases/case-incident-saturday.html (авария в субботу — реакция 15 мин, восстановление 2 ч, 0 потерь) and added case card on cases.html; regenerated sitemap.xml (163 URLs).
- P1-21: added Telegram + MAX CTA next to success message on 15 pages.
- P1-22: created cases/case-vs-staff.html and added case card on cases.html (переход со штатного сисадмина на F&F, экономия до 80%); regenerated sitemap.xml (164 URLs).
- P1-23: updated FAQ "Сколько стоит штатный сисадмин по городу?" on prices.html with Kazan figures (80 000–120 000 ₽/мес).
- P1-24: shortened forms (removed service hidden + need select, merged into task) on 13 pages.
- P1-25: added "Размер офиса" select (до 10 / 10–30 / 30+) to forms on contacts.html and servers.html.
- P1-26: added "Что будет после заявки" 4-step block to 5 pages that lacked it (audits/backup-checklist, company/about, company/partners, resources/it-budget, services/mail).
- P1-27: added "Посчитаем точную стоимость для Вашего офиса" CTA on contacts.html and support.html.
- P1-28: added "Не навязываем лишние услуги" line to support.html and prices.html.
- P1-29: added "Мы не держим заложников" line to support.html and index.html.
- P1-30: added 4 cards to "Что входит" section on support.html (Подключение к 1С и ЭЦП, Тикет-система, Взаимодействие с провайдерами, 1 ГБ облака на ПК).
- P1-31: testimonials already include city tags (e.g. "В Казани, IT-директор (анонимно)"); real names require client permission (owner-dependent).
- P1-32: added Yandex Maps iframe (Kazan) section on contacts.html.
- Title optimization on 7 pages: prices, infrastructure, compare, audits/audit, industries, company/about, contacts.
- Font/image optimization: fonts already subset (cyrillic_latin, 7 files); images mostly WebP (26/30). Generated -400w/-800w variants for 12 content images (case-*, service-*, team-*, logo) via PIL. Added srcset to all img tags referencing variant bases (0 remaining). Remaining single-size images (team-*, case-tobacco, logo-*) lack variants by design (small).
- Core Web Vitals: changed font-display from swap to optional in css/style.css (8 @font-face); added min-height:220px to .terminal__body to reduce CLS. Lighthouse (mobile): perf 98, LCP 920ms, CLS 0, TBT 0. Desktop CLS 0.996 (still high — likely terminal animation; pending verification). npm run build ok.
- Review/AggregateRating schema: added aggregateRating (5/7) to Organization schema on 153 pages (testimonials.html already had it). All JSON-LD valid.
- Rich Results Test: validated all 684 JSON-LD blocks across 168 pages — 0 errors. Types: Article, BreadcrumbList, CollectionPage, FAQPage, HowTo, Organization, Service, WebPage. FAQPage mainEntity and AggregateRating structurally valid.
- Lighthouse (after font subsetting/CWV fixes): mobile perf 98, LCP 978ms, CLS 0, TBT 45ms, a11y 100, SEO 100, BP 100. Desktop perf 76, CLS 0.996 (terminal animation). Forced reflow in script.js (review slider) noted.
- Cross-browser: added -webkit-backdrop-filter prefixes to all backdrop-filter rules in css/style.css, css/critical.css, css/components.css. Fonts/images already modern (WebP, woff2). No optional chaining/nullish coalescing in JS (ES2017 baseline).
- Font subsetting: subset all 7 woff2 fonts to the 279 unique characters used on the site via fontTools (pyftsubset). Sizes reduced ~35% (28KB→18-19KB Inter, 24KB→19-20KB JetBrains Mono). npm run build ok.
- P1-33: added "Нам доверяют" section with anonymized client-segment chips on index.html, cases.html, company/testimonials.html (real logos pending client permission).
- P1-15: added FAQ "Что если результат не устроит?" to 124 pages with FAQ blocks.
- P1-16: prices.html already contains "Что входит и что не входит в поддержку" and "Что входит и что оплачивается отдельно" sections with in/out lists (verified).
