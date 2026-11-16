# 7-Phase Plan for F&F Site Semantic Optimization

Based on SEMANTIC_MAP.md analysis of 174 HTML pages.

## Phase 1: Critical Deduplication (1-2 weeks)
**Goal:** Remove duplicate content, consolidate 14 pairs of pages
**Tasks:**
1. Add 301 redirects for 14 duplicate page pairs in `_redirects`
2. Merge blog/sisadmin-cost.html + blog/sisadmin-cost-2026.html → sisadmin-cost.html
3. Merge blog/backup-3-2-1.html + articles/backup-3-2-1.html → articles/backup-3-2-1.html
4. Merge blog/server-1c-saturday.html + blog/server-1c-saturday-plan.html → server-1c-saturday.html
5. Merge 152fz-prep.html + articles/152fz-prep.html + blog/152fz-prep.html → 152fz-prep.html
6. Merge vpn.html + blog/vpn-udalenny-dostup.html → vpn.html
7. Merge audit.html + services/audit-services.html → audit.html
8. Update sitemap.xml (remove merged pages)
9. Update internal links across all pages

## Phase 2: Intent Separation — Core Service Pages (2-3 weeks)
**Goal:** Split mixed-intent pages into focused landing pages
**Tasks:**
1. support.html → support.html (main) + support-prices.html (tariffs) + support-onboarding.html (how to connect)
2. servers.html → servers.html (main) + servers-cases.html (case studies)
3. security.html → security.html (overview) + crypto.html (CryptoPro/ECP) + security-audit.html (security audit)
4. infrastructure.html → infrastructure.html (overview) + wifi-setup.html + sks.html + cctv.html

## Phase 3: High-Priority New Pages (2-3 weeks)
**Goal:** Create 8 high-priority transactional pages
**Tasks:**
1. support-prices.html — tariff calculator for IT outsourcing
2. servers-tco.html — TCO calculator for servers
3. security-audit.html — security audit service page
4. wifi-setup.html — corporate Wi-Fi setup
5. sks.html — structured cabling system installation
6. cctv.html — video surveillance for offices
7. crypto.html — CryptoPro and ECP dedicated page
8. Improve pain-server-down.html (problem page)

## Phase 4: Medium-Priority Pages (3-4 weeks)
**Goal:** Create 7 medium-priority pages
**Tasks:**
1. support-onboarding.html — how to connect IT outsourcing
2. servers-cases.html — server case studies
3. audit-free.html — free IT audit landing
4. backup-restore-test.html — backup restoration test guide
5. ecp-lost-token.html — lost ECP token recovery
6. mail-server.html — corporate email on own server
7. print-management.html — print management

## Phase 5: Internal Linking & Schema (2 weeks)
**Goal:** Implement internal linking map and add Schema.org
**Tasks:**
1. Implement INTERNAL_LINKING_MAP.md links across all pages
2. Add Service schema to all service pages
3. Add BreadcrumbList to all pages
4. Add FAQPage to all pages with FAQ sections
5. Verify canonical URLs and OG tags

## Phase 6: Low-Priority Pages & Optimization (2-3 weeks)
**Goal:** Create remaining pages and optimize
**Tasks:**
1. glossary.html — IT terms glossary
2. faq.html — general FAQ page
3. comparison-matrix.html — comparison matrix
4. case-studies.html — detailed case studies
5. testimonials.html — client testimonials with photos/video
6. Optimize images (WebP, dimensions, lazy loading)
7. Performance audit (Lighthouse, Core Web Vitals)

## Phase 7: Content Marketing & Monitoring (ongoing)
**Goal:** Continuous content and SEO monitoring
**Tasks:**
1. Publish 2-4 blog articles per month
2. Update existing articles (dateModified)
3. Add new case studies
4. Monitor rankings and adjust semantics
5. A/B test CTAs and landing pages
6. Track conversion rates

---
**Current status:** Phase 1 done (redirects + sitemap cleanup). Phase 2 in progress (support-prices.html, crypto.html created).