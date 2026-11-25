# AGENTS.md — F&F SEO Project

## Project
- Site: F&F (ff-it.ru), static HTML/CSS/JS. Production: ff-it.ru (custom domain). Staging: GitHub Pages (fedorov55.github.io/ff-site).
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

## Deployment Workflow (ОБЯЗАТЕЛЬНО)

Все изменения делаются в локальной папке `C:\opencode\f&f\site`. Никаких правок на сервере напрямую.

После каждой задачи/фазы:
1. Валидация: `npm run audit` + htmlhint.
2. Обновить `docs/CHANGELOG.md`.
3. Деплой на тестовый сервер: `python scripts/deploy-test.py` (SFTP, 92.255.199.90:2222, ftpuser). Проверка: http://92.255.199.90:8080
4. Коммит и пуш: `git add -A && git commit -m "..." && git push origin main`

Полная документация: `docs/DEPLOY.md`.

## Pages
- 161 HTML pages total: root pages (index, articles, blog, cases, contacts, industries, prices, servers, services, support, sysadmin-cost-kazan, terms-of-work, 404) plus subdirectories (ai, articles, audits, blog, cases, company, compare, incidents, industries, infrastructure, leads, legal, pain, resources, security, services).
- blog.html — blog index; articles.html — article index.
- services.html, servers.html, support.html, contacts.html, prices.html — core commercial pages.
- legal/ — privacy.html, terms.html, cookie.html, consent.html (152-ФЗ policy).
- compare/ — compare.html, compare-freelance.html, compare-integrator.html, ff-vs-staff-2026.html, staff-sysadmin-cost.html.
- sitemap.xml (159 URLs), robots.txt, llms.txt / llms-full.txt.

## Auto-Routing (автоматический выбор скиллов и MCP)

Агент ДОЛЖЕН автоматически выбирать скиллы и MCP по смыслу запроса пользователя, не спрашивая «какой скилл использовать». Используй скиллы и MCP при ЛЮБОЙ возможности — не делай вручную то, что можно сделать через инструмент.

### Обязательное правило
- Если запрос совпадает с любой категорией ниже — загрузи скилл и используй соответствующие MCP без дополнительных вопросов.
- Если не уверен — загрузи `mcp-toolkit`.
- Если задача не покрыта — используй встроенные инструменты.
- При любом запросе, связанном с SEO, автоматически проверяй подключение OpenSEO (`whoami`) и SEO (`seo_sites`).

### SEO и маркетинг

| Запрос (примеры) | Скиллы | MCP-инструменты |
|------------------|--------|-----------------|
| сео, SEO, оптимизация, продвижение | `seo-audit`, `mcp-seo` | OpenSEO, SEO (iannuttall), Frontend Checklist |
| аудит, проверь сайт, проверка сайта, тест сайта | `audit`, `seo-audit`, `mcp-audit` | Lighthouse Audit, AccessLumens, Frontend Checklist, Playwright, OpenSEO |
| ключи, ключевые слова, подбор ключей, семантика | `keywords`, `keyword-research`, `keyword-clustering` | Exa, web-search, OpenSEO |
| конкуренты, конкурентный анализ, анализ конкурентов | `competitors`, `competitor-analysis`, `competitive-landscape` | Exa, web-search, scrapling |
| «DNS», «SSL», «сертификат», «заголовки», «почта», «email» | `mcp-network` | TPC, DNS Beautiful, Network MCP |
| «доступность сайта», «сайт упал», «мониторинг», «статус сервисов» | `mcp-network` | InternetVitals, TPC |
| «SEO данные», «authority», «трафик», «бэклинки», «ключевые слова» | `mcp-network`, `mcp-seo` | Nuqti, OpenSEO, SEO |
| стратегия, маркетинг, план, план продвижения | `strategy`, `seo-coach` | Exa, web-search |
| локальное SEO, Google Business Profile, карты | `local-seo`, `mcp-seo` | OpenSEO |
| AI видимость, GEO, AEO, цитирование | `ai-visibility-audit`, `ai-prompt-research` | Exa, OpenSEO |
| ссылки, бэклинки, доноры, линкбилдинг | `link-prospecting`, `mcp-seo` | OpenSEO, SEO |
| отчёт, сводка, report, проверка | `seo-report` | OpenSEO, SEO |
| контент-бриф, ТЗ на статью | `seo-project-setup`, `keyword-clustering` | OpenSEO |
| ранжирование, позиции, трекинг, ранки | `mcp-seo` | OpenSEO, SEO |
| трафик, показы, клики, CTR | `mcp-seo` | SEO (iannuttall) |
| индексация, индекс | `mcp-seo` | SEO (iannuttall) |

### Исследования и поиск

| Запрос (примеры) | Скиллы | MCP-инструменты |
|------------------|--------|-----------------|
| поиск, найди, исследуй, поищи, найти | `web-search`, `mcp-search` | Exa, web-search |
| факт, правда ли, проверь факт, истинность | `web-search`, `mcp-search` | Exa, web-search |
| рынок, индустрия, тренды, тенденции | `web-search`, `mcp-search`, `strategy` | Exa, web-search |
| люди, компания, кто такой, фирма | `web-search`, `mcp-search` | Exa (category:people/company) |
| новости, свежее, что нового, актуальное | `web-search`, `mcp-search` | Exa, web-search |
| «маркетинговые плейбуки», «плейбуки», «growth», «воронки», «CRO» | `mcp-search` | Marketing Playbooks |
| «параллельный поиск», «быстрый поиск», «multi search» | `mcp-search` | Parallel Search |

### Дизайн и фронтенд

| Запрос (примеры) | Скиллы | MCP-инструменты |
|------------------|--------|-----------------|
| переделать дизайн, UI, интерфейс, вёрстка | `frontend-design`, `ui-ux-design-pro` | Playwright, Frontend Checklist |
| анимация, motion, анимировать, движение | `forge-motion` | — |
| эффекты, переходы, glitch, particles, кинетика | `mcp-motion`, `forge-motion` | Motion Fab |
| вдохновение, референсы, примеры дизайна, палитра, цвета, шрифты | `mcp-design` | Inspo, standby.design |
| дизайн-система, токены, типографика, отступы, радиусы | `mcp-design` | CSS Crème, standby.design |
| CSS, стили, токены, дизайн-система | `mcp-css`, `mcp-design` | CSS Crème, standby.design |
| написать CSS, хороший CSS, архитектура CSS | `mcp-css` | CSS Crème |
| UX, юзабилити, usability, удобство | `mcp-ux` | ux-mcp, designmind |
| паттерны, UI-паттерны, формы, навигация | `mcp-ux` | designmind, ux-mcp |
| метрики UX, SUS, NPS, CSAT | `mcp-ux` | ux-mcp |
| улучшить UI, улучшить интерфейс, редизайн | `mcp-ux`, `mcp-design` | web-stylebook, designmind, Inspo |
| аудит фронтенда, проверь вёрстку, a11y, доступность | `frontend-no-slop`, `mcp-browser`, `mcp-audit` | Frontend Checklist, Playwright, ux-mcp |
| визуальная регрессия, CSS поплыл, сравнить страницы, до и после | `mcp-visual` | Visual Parity |
| проверь что ничего не сломалось, визуальная проверка | `mcp-visual`, `mcp-browser` | Visual Parity, Playwright |
| скриншот, как выглядит | `mcp-browser` | Playwright |
| Lighthouse, Core Web Vitals, скорость, производительность | `mcp-audit`, `mcp-browser` | Lighthouse Audit, Playwright |
| консоль, ошибки в браузере, сеть, network | `mcp-browser` | Playwright, Desktop Commander |

### Код и разработка

| Запрос (примеры) | Скиллы | MCP-инструменты |
|------------------|--------|-----------------|
| проверь код, ревью, code review | `review-team`, `mcp-docs` | Codebase Memory, Serena |
| документация, как работает X, API | `mcp-docs` | Context7 |
| анализ кода, зависимости, архитектура | `mcp-docs` | Codebase Memory, Serena, Repomix |
| рефакторинг, переименовать, изменить | `mcp-docs` | Serena, Codebase Memory |
| собрать репо, упаковать код | `mcp-docs` | Repomix |
| гит, коммит, ветка, PR, пулл реквест | — | Desktop Commander |
| билд, сборка, ошибки сборки, компиляция | — | Desktop Commander |

### Скрейпинг и данные

| Запрос (примеры) | Скиллы | MCP-инструменты |
|------------------|--------|-----------------|
| скрейпинг, спарси, спарсить, парсинг | `mcp-scraping` | Scrapling, Crawl4AI, MarkItDown |
| конвертировать PDF, прочитать документ, PDF | `mcp-scraping` | MarkItDown |
| краулинг, обойти сайт, обход | `mcp-scraping` | Crawl4AI, Scrapling |
| извлечь данные, таблицы, структурировать | `mcp-scraping` | Crawl4AI, Scrapling, MarkItDown |

### Безопасность

| Запрос (примеры) | Скиллы | MCP-инструменты |
|------------------|--------|-----------------|
| безопасность, уязвимости, CVE | `mcp-security` | CVE Intelligence |
| аудит безопасности, проверка безопасности | `mcp-security` | CVE Intelligence |
| харденинг, защита, хардн | `mcp-security` | CVE Intelligence |

### Тексты и конверсия

| Запрос (примеры) | Скиллы | MCP-инструменты |
|------------------|--------|-----------------|
| текст, заголовок, конверсия, копирайт, лендинг, реклама | `mcp-copy` | Persuasion Taxonomy |
| проверь текст, проверь заголовок, A/B тест | `mcp-copy` | Persuasion Taxonomy |
| написать текст, написать статью, написать пост | `mcp-copy`, `ff-services` | Persuasion Taxonomy, Exa, web-search |
| переписать, улучшить текст, без воды | `mcp-copy`, `ff-services` | Persuasion Taxonomy, Writing Editor |
| редактировать, правка текста | `mcp-copy` | Writing Editor, Persuasion Taxonomy |

### Услуги и бизнес (F&F)

| Запрос (примеры) | Скиллы | MCP-инструменты |
|------------------|--------|-----------------|
| услуги, цены, стоимость, сколько стоит, тарифы | `ff-services` | — (Memory: F&F_Pricing) |
| «CRM», «клиенты», «контакты», «лиды», «сделки», «задачи» | `crm-usage` | CRM REST API (crm.ff-it.ru) |
| «финансы», «доход», «расход», «прибыль», «транзакции» | `crm-usage`, `ff-services` | CRM REST API |
| процесс, как работаете, гарантия, SLA | `ff-services` | — (Memory: F&F_Process, F&F_Guarantees) |
| что вы делаете, чем занимаетесь, услуги | `ff-services` | — (Memory: F&F_Services) |
| контакт, телефон, email, как связаться | `ff-services` | — (Memory: F&F_Company) |

### Утилиты

| Запрос (примеры) | Скиллы | MCP-инструменты |
|------------------|--------|-----------------|
| время, дата, часовой пояс, сколько времени | `mcp-utils` | Time |
| память, запомни, сохрани факт, помни | `mcp-utils` | Memory |
| посчитай, вычисли, математика, калькулятор | `mcp-utils` | ComputeFirst |
| трансформация, CSV, JSON, преобразовать | `mcp-utils` | ComputeFirst |

### Общие

| Запрос (примеры) | Скиллы | MCP-инструменты |
|------------------|--------|-----------------|
| аудит, проверка сайта, тестирование | `audit`, `seo-audit`, `mcp-audit` | Lighthouse Audit, AccessLumens, Frontend Checklist, Playwright, OpenSEO |
| стратегия, маркетинг, план, план продвижения | `strategy` | Exa, web-search |
| что умеешь, какие инструменты | `mcp-toolkit` | — |
| настрой, конфиг, MCP, серверы | `opencode`, `mcp-toolkit` | — |
| помоги, что делать | `mcp-toolkit`, `seo-coach` | — |

**Правило:** если запрос совпадает с одной из категорий выше — загрузи скилл и используй соответствующие MCP без дополнительных вопросов. Если не уверен — загрузи `mcp-toolkit` для обзора. Если задача не покрыта — используй встроенные инструменты и здравый смысл.

**Дополнительно:** при любом запросе, связанном с SEO, автоматически проверяй подключение OpenSEO (`whoami`) и SEO (`seo_sites`), чтобы убедиться, что данные доступны. При запросах об услугах/ценах — обращайся к `ff-services` и Memory (`F&F_Pricing`, `F&F_Services`).

## MCP & Skills
- Полная документация: `docs/MCP_AND_SKILLS_GUIDE.md`
- Краткое руководство: `docs/MCP_QUICKSTART_RU.md`
- Справочник скилл: `mcp-toolkit`
- Конфиг серверов: `opencode.jsonc`
- 38 MCP-серверов (все бесплатные), 38 скиллов проекта + 7 из плагинов + 14 Superpowers.
- Плагины (6): @upstash/context7-opencode, opencode-mem, @dietrichgebert/ponytail, cc-safety-net, superpowers, oh-my-opencode.
- При новой сессии: загрузить `mcp-toolkit` для обзора инструментов.

## Plugins
- `@upstash/context7-opencode` — официальный плагин Context7: MCP + скилл документации.
- `opencode-mem` — персистентная память между сессиями (local Turso/libSQL vector search).
- `@dietrichgebert/ponytail` — «ленивый senior dev mode»: минимальные изменения, простые ответы. Скиллы: ponytail, ponytail-audit, ponytail-debt, ponytail-gain, ponytail-help, ponytail-review.
- Конфиг: `plugins` в `opencode.jsonc`.
## Key Files
- style.css (base), critical.css (critical layer)
- script.js (nav, calculators, quiz, forms, terminal, exit-popup, metrics)
- calculator.js, search.js, search-worker.js
- data.json (live metrics)
- sitemap.xml, robots.txt, llms.txt
- privacy.html, terms.html, cookie.html (152-ФЗ policy)
- _headers, _redirects (Cloudflare Pages)
- sw.js (Service Worker, ff-cache-v12)
