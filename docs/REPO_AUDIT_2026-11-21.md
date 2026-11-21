# Full Repository Audit — 2026-11-21

Scope: entire site repo (excluding node_modules, .agents). 161 HTML pages, 4 CSS, 5 JS, SW, build, scripts, SEO infra.

## 1. Summary

- Production forms/search were effectively broken (P0): `FORM_ENDPOINT` ReferenceError, calculator `fetch('')`, search paths wrong on subpages, XSS in search results, SW precache using domain-root paths under `/ff-site/`.
- HTML: 4 pages missing meta/OG/canonical/robots; 3 duplicate descriptions; 67 pages with relative canonical; 8 files with BOM; heading order issues.
- SEO infra: sitemap has 4 broken URLs + noindex leak + 3 missing pages; `_redirects` has 17 broken targets; search-index stale (39 dead + 41 missing); llms.txt/llms-full.txt inaccurate; security.txt errors; SW precache incomplete.
- Content: nav inconsistency (81 pages missing incidents item); 1 missing image; placeholder analytics IDs; 3 near-duplicate title clusters.
- Build: dist unused by HTML; build omits several assets; fonts path bug fixed.
- No secrets found; images optimized; no CI workflows.

## 2. P0 — Critical (fixed this pass)

1. `js/script.js` — `FORM_ENDPOINT` undefined → ReferenceError in forms. Fixed with `typeof` guard (mailto fallback).
2. `js/script.js` — form-data persistence selector injection. Hardened with `CSS.escape`.
3. `js/calculator.js` — `fetch('')`. Replaced with endpoint/mailto fallback + success state.
4. `js/calculator.js` — `calcSlab()` null deref. Guarded.
5. `js/search.js` — relative `search-index.json`/worker paths break on subpages. Base path `/ff-site/` (or `/`).
6. `js/search.js` — XSS in `renderResults`. Escaped title/desc/url.
7. `sw.js` — precache domain-root paths under `/ff-site/`. Base-aware; added missing assets; fallback uses base index.
8. `css/style.css` — font urls `fonts/` → `../fonts/`.
9. 8 HTML files — removed UTF-8 BOM before doctype.
10. `build.js` — expanded build set; bundle with externalized binaries.

## 3. P1 — High (recommended next)

- Regenerate `sitemap.xml`: remove 4 broken URLs, remove `infrastructure/room.html`, add 3 missing pages, add `lastmod`, differentiate priority.
- Fix `_redirects` 17 targets to real subfolder paths (or migrate to Cloudflare Pages).
- Regenerate `search-index.json` from actual HTML; exclude 404/noindex/redirect sources.
- Fix `llms.txt` links to canonical subfolder URLs; regenerate `llms-full.txt` (trim, exclude noindex).
- Fix root `security.txt` (remove stray `"`, align fields, absolute Canonical/Policy).
- Make canonical URLs absolute on 67 subdirectory pages.
- Add missing meta description/canonical/robots/OG/twitter to 4 pages (compare/*, sysadmin-cost-kazan, terms-of-work).
- Add schema to terms-of-work.html.
- Fix nav inconsistency: add incidents item to 81 pages.
- Replace placeholder analytics IDs in `js/script.js` (`AW-XXXXXXXXX`, `G-XXXXXXXXXX`).
- Add missing image `img/case-ecp-eis.webp` or remove reference.
- De-duplicate 3 meta descriptions.
- Fix heading order: articles.html, resources/research.html (H3 before H2); security/security.html (H1 late).

## 4. P2 — Medium/Low

- Tighten CSP `img-src`; add PWA icons 192/512 to manifest.
- SW precache version alignment docs (v13 vs v12).
- CSS token mismatch critical.css vs tokens.css (`--dim`, `--border`).
- Breakpoint scale consolidation; reduce `!important` in critical.css.
- Remove legacy `.eslintrc.json` (use flat config only); fix htmlhint duplicate class/id.
- Add CI workflows (none present).
- AGENTS.md page count (202 vs actual 161) update.
- Remove unused tokens; clean dead code (window.sanitize unused until now).
- llms-full.txt size (438 KB) trim.

## 5. Validation done

- node --check: all JS pass.
- npm run build: completes successfully.
- No secrets found.
- Images optimized (WebP + responsive variants).

## 6. Not changed (intentionally)

- Did not migrate hosting or apply `_headers`/`_redirects` (GitHub Pages ignores them).
- Did not regenerate sitemap/search-index/llms (requires script; queued as P1).
- Did not mass-edit 161 HTML pages for canonical/nav (queued as P1 to avoid risky bulk edits without review).