# AGENTS.md — F&F SEO Project

## Project
- Site: F&F (fedorov55.github.io/ff-site), static HTML/CSS/JS, GitHub Pages.
- Stack: Vanilla JS, no backend. Forms → Formspree/Getform.
- Style: dark theme (#0A0D14), gold accent (#D4AF37), JetBrains Mono for accents, Inter for body.
- Tone: business, status, light self-irony. No «100%», no «cheap», no «best in the world».

## SEO Rules
- Target region: Kazan + Tatarstan (on-site), Russia (remote).
- Primary keywords: «настройка серверов Казань», «сисадмин Казань», «IT-аутсорсинг для малого бизнеса», «сервер под ключ».
- Schema.org: Organization (not LocalBusiness — no office), Service, FAQPage, Person, BreadcrumbList.
- AEO/GEO: answer-first paragraphs, FAQPage, llms.txt.
- Core Web Vitals: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1.

## Execution Discipline
1. Не оставляй заглушек и «TODO» в коде.
2. Каждое изменение валидируй: Lighthouse, Rich Results Test, консоль браузера.
3. После каждой фазы обновляй CHANGELOG.md.
4. Если сомневаешься — предложи два варианта с плюсами и минусами, но продолжай работу.

## Pages
- 101 HTML pages (index, services, servers, infrastructure, security, cases, blog 32 + articles 8, geo 10, services 6, cases 6, hubs, industries, etc.)
- blog.html — blog index (40 cards)
- map.html — sitemap (99 links)
- status.html, quiz.html, demo.html, compare*.html, etc.

## Key Files
- style.css (base), style-overrides.css (final layer)
- script.js (nav, calculators, quiz, forms, terminal, exit-popup, metrics)
- data.json (live metrics)
- sitemap.xml, robots.txt, llms.txt
- privacy.html (152-ФЗ policy)
