# Полная документация: MCP-серверы, скиллы и инструменты F&F

> Единый справочник для всех сессий OpenCode в проекте F&F.
> Обновлено: 2026-11-24. Конфиг: `opencode.jsonc` (корень проекта). Всего: 38 MCP-сервер, 38 скиллов.

---

## 1. Архитектура

- **OpenCode** работает в режиме Code Mode: инструменты MCP доступны через `tools.<server>.<tool>(...)` внутри `execute`.
- **Скиллы** (`.agents/skills/<id>/SKILL.md`) загружаются по запросу через `skill({ id })`.
- **Конфиг** `opencode.jsonc` содержит 31 MCP-сервер, все бесплатные (некоторые требуют входа/аккаунта).
- **Правило:** выбирайте минимальный набор инструментов под задачу. Не вызывайте все подряд — это расходует контекст.
- **Auto-Routing:** AGENTS.md содержит таблицу «запрос → скиллы → MCP». Агент автоматически выбирает по смыслу запроса.

---

## 2. Инвентарь MCP-серверов (38)

### Поиск и исследования

| Сервер | Инструменты | Когда использовать |
|--------|-------------|-------------------|
| **exa** | `web_search_exa`, `web_fetch_exa` | Семантический поиск, people/company lookup, чтение полного контента |
| **web-search** | `search_web`, `fetch_url` | Точный ключевой поиск (DDG/Bing/SearXNG), универсальный fetch (HTML/PDF/text/JSON/XML/CSV/media) |
| **computefirst** | `search`, `describe`, `execute`, `activity` | Точный math, CSV/JSON transforms, date math, хеши |

### Документация и код

| Сервер | Инструменты | Когда использовать |
|--------|-------------|-------------------|
| **context7** | `resolve-library-id`, `query-docs` | Актуальная документация и примеры кода для библиотек/фреймворков/API |
| **serena** | `initial_instructions`, `activate_project`, `serena_repl` | Семантическая навигация по коду (символы, референсы) |
| **codebase-memory** | 17 инструментов (search_graph, trace_path, detect_changes, get_architecture, …) | Граф знаний по коду, анализ зависимостей, влияние изменений |
| **repomix** | `pack_codebase`, `grep_repomix_output`, `read_repomix_output`, `generate_skill` | Упаковка репозитория для анализа |

### Браузер и аудит

| Сервер | Инструменты | Когда использовать |
|--------|-------------|-------------------|
| **playwright** | 25 инструментов (navigate, click, screenshot, console, network, evaluate, …) | Автоматизация браузера, e2e-тесты, скриншоты |
| **frontend-checklist** | 11 инструментов (audit_url, check_rule, fix_rule, explain_rule, search_rules, …) | Аудит фронтенда по 385 правилам (HTML/CSS/JS/a11y/perf/SEO/security/images) |
| **desktop-commander** | 25 инструментов (файлы, процессы, поиск, чтение/запись) | Локальная автоматизация: терминал, файлы, процессы |
| **accesslumens** | `check_accessibility`, `check_pdf`, `create_report` | WCAG 2.0/2.1/2.2 скан (axe-core + keyboard/focus/reflow). Бесплатно, без ключа |
| **lighthouse-audit** | `run_lighthouse` | Lighthouse (perf, a11y, best-practices, SEO, CWV). Remote, без ключа |

### Конвертация и скрейпинг

| Сервер | Инструменты | Когда использовать |
|--------|-------------|-------------------|
| **markitdown** | `convert_to_markdown` | Конвертация PDF/DOCX/XLSX/PPTX/HTML/изображений → Markdown. Требует `protocol: "auto"` |
| **scrapling** | 17 инструментов (fetch, browser sessions, stealth scraping) | Стелс-скрейпинг, браузерные сессии. Заменяет Firecrawl scrape |
| **crawl4ai** | 4 инструмента (crawl, scrape, get_artifact, close_session) | JS-рендеринг, глубокий краулинг. Требует `protocol: "auto"` |

### Безопасность

| Сервер | Инструменты | Когда использовать |
|--------|-------------|-------------------|
| **cve-intelligence** | 6 инструментов (cve_search, cve_get, cve_history, cve_changes) | Поиск CVE, CISA KEV, EPSS, затронутое ПО |

### SEO

| Сервер | Инструменты | Когда использовать |
|--------|-------------|-------------------|
| **seo** (iannuttall) | 16 инструментов (seo_report, seo_page, seo_crawl, seo_lint, seo_index, seo_research, …) | Реальные данные GSC/Bing/Analytics. Требует `seo auth login` |
| **openseo** | 85 инструментов (whoami, list_projects, create_project, seo_audit, keyword_research, …) | Платформа OpenSEO. Требует входа через `/mcps` (OAuth) |

### Дизайн и стили

| Сервер | Инструменты | Когда использовать |
|--------|-------------|-------------------|
| **inspo** | `recommend`, `search_screens`, `find_components`, `find_by_color`, `compare`, `get_screen` | Поиск вдохновения, референсов, палитр, компонентов (2320 страниц, 832 сайта) |
| **standby-design** | `generate_color_palette`, `generate_type_scale`, `generate_space_tokens`, `generate_shape_tokens`, `generate_motion_tokens`, `export_design_system`, `get_design_rules` | Генерация дизайн-системы (цвета, типографика, отступы, форма, motion). Shareable URL |
| **motion-fab** | `search_techniques`, `get_technique`, `search_recipes`, `get_recipe` | Поиск анимаций, переходов, эффектов, kinetic typography (266 техник с кодом GSAP) |
| **css-creme** | `search_themes`, `list_themes`, `get_design_md`, `get_theme_tokens`, `get_install_command`, `get_agent_rules`, `decode_url`, `decode_site`, `css_feature`, `verify_design_md`, `how_to_use` | Поиск тем, извлечение токенов из сайтов, проверка CSS-фич (Baseline), правила для AGENTS.md |

### UX и дизайн-системы

| Сервер | Инструменты | Когда использовать |
|--------|-------------|-------------------|
| **ux-mcp** | 23 инструмента (analyze_accessibility, review_usability, check_contrast, check_responsive, analyze_performance, check_seo, suggest_pattern, generate_component_example, audit_design_system, suggest_microcopy, recommend_form_pattern, suggest_data_visualization, generate_accessibility_report, analyze_information_architecture, detect_dark_patterns, calculate_ux_metrics, generate_wireframe, suggest_microinteraction) | WCAG, эвристики Нильсена, паттерны, формы, метрики, IA, тёмные паттерны. 28 ресурсов знаний |
| **designmind** | 20 инструментов (get_principles, get_pattern, get_checklist, evaluate_design, get_design_system, compose_system, get_content_pattern, get_research_method, get_metrics_framework, get_d4d_framework, get_business_strategy) | Принципы дизайна, паттерны, чеклисты, оценка дизайна, метрики, стратегия. Локальный каталог |
| **web-stylebook** | 14 инструментов (recommend_design_direction, get_design_improvement_plan, audit_page_structure, validate_design_audit_result, get_design_principle_plan, get_ux_principle_plan, get_ui_state_plan, compose_design_tokens, search_design_references, get_design_reference) | Улучшение существующего UI, аудит структуры, дизайн-направления, состояния. Офлайн |

### Визуальная регрессия

| Сервер | Инструменты | Когда использовать |
|--------|-------------|-------------------|
| **visual-parity** | `compare_pages` | Сравнение reference vs candidate: pixel diff, computed style diff, root-cause clusters, suggested fixes |

### Копирайтинг и конверсия

| Сервер | Инструменты | Когда использовать |
|--------|-------------|-------------------|
| **persuasion-taxonomy** | 9 инструментов (plan_marketing_copy, diagnose_marketing_copy, check_headlines, check_marketing_claims, find_persuasion_techniques, get_persuasion_technique, explain_why_not_converting, plan_ab_test, read_ab_test_result) | Планирование и проверка копирайта, заголовков, A/B-тестов, техники убеждения (767 техник). Без ключа |
| **writing-editor** | `revise_writing`, `review_revision` | Редактирование текста с сохранением терминов, проверка изменений |

### CRM (FF-IT CRM)

| Сервер | Инструменты | Когда использовать | Примечания |
|--------|-------------|-------------------|------------|
| **CRM (REST+MCP)** | 20 инструментов (list_contacts, create_contact, list_leads, create_lead, list_deals, create_deal, list_companies, create_company, list_tasks, create_task, list_finance, finance_summary, get_stats, search) | Управление клиентами, лидами, сделками, задачами, финансами | Custom CRM FF-IT v3.50.0, self-hosted. API key в env CRM_API_KEY. |

### Сеть, DNS, SSL и мониторинг (MCP)

| Сервер | Инструменты | Когда использовать | Примечания |
|--------|-------------|-------------------|------------|
| **tpc-free-tools** | 28 инструментов (DNS, email, SSL, headers, TTFB, HTTP/3, redirect, whois, robots.txt, sitemap, URL status, ASN, IP lookup, cron, chmod, CSR decoder) | Проверка DNS, SSL, email-доставляемости, заголовков, TTFB, HTTP/3, robots.txt, sitemap, whois | Бесплатно, без ключа. 28 read-only инструментов. Сервер в Германии. |
| **dns-beautiful** | 9 инструментов (dns_lookup, caa_check, dns_security_scan, nameserver_health, dns_infrastructure, dns_trace, verify_record, global_probe, traceroute) | Глубокий DNS-аудит, DNSSEC, CAA, делегирование, провайдеры | Бесплатно, без ключа. 38 резолверов. |
| **network-mcp** | 17 инструментов (dns_lookup, dns_propagation, dnsbl, email_deliverability, email_test, geolocation, http_check, ipv6_check, mx_check, my_ip, network_audit, reverse_dns, security_headers, bgp) | Комплексный сетевой аудит, BGP, геолокация, заголовки безопасности | Бесплатно, без ключа. network_audit для broad-анализа. |
| **internetvitals** | 5 инструментов (get_internet_health, list_services, get_service_status, get_recent_incidents, get_vitals_history) | Мониторинг 41 облачного сервиса (AWS, Cloudflare, GitHub, OpenAI и др.) | Бесплатно, без ключа. |
| **nuqti** | 10 инструментов (domain_overview, backlinks_summary, domain_history, keyword_overview, keyword_ideas, referring_domains, list_seo_tools, run_seo_tool, fetch, search) | SEO-данные: authority, трафик, ключи, бэклинки, 40 технических SEO-инструментов | Бесплатно, без ключа. Fair-use: 30 req/min, 10 fresh lookups/day. Иногда недоступен. |

### Маркетинг и поиск (MCP)

| Сервер | Инструменты | Когда использовать | Примечания |
|--------|-------------|-------------------|------------|
| **marketing-playbooks** | `search_growth_playbooks`, `consult_seo_and_content_architecture`, `consult_conversion_funnels_and_lead_magnets`, `consult_heuristic_cro_and_growth_experiments`, `consult_authority_and_search_flywheels`, `consult_category_positioning_and_permission_marketing`, `consult_omnichannel_storytelling_and_distribution`, `consult_growth_council_roundtable`, `get_playbook`, `list_disciplines_and_playbooks` | RAG по 19 895 growth-плейбукам: SEO, воронки, CRO, authority, distribution, позиционирование | Бесплатно, без ключа. 20 запросов/день. |
| **parallel-search** | `web_search`, `web_fetch`, `send_feedback` | Параллельный поиск и чтение URL — альтернатива Exa/web-search | Бесплатно, без ключа. |

### Утилиты

| Сервер | Инструменты | Когда использовать |
|--------|-------------|-------------------|
| **time** | `get-current-time`, `get-time-in-timezone`, `list-timezones` | Точное время и часовые пояса |
| **memory** | 9 инструментов (create_entities, create_relations, add_observations, search_nodes, …) | Граф знаний — долгосрочная память между сессиями |

---

## 3. Инвентарь скиллов (38)

### F&F-специфичные

| Скилл | Когда использовать |
|-------|-------------------|
| `crm-usage` | Как пользоваться CRM: API, endpoints, MCP tools, контакты, лиды, сделки, задачи, финансы |
| `ff-services` | Полная база знаний F&F: услуги, цены, процессы, гарантии, контакты |
| `audit` (ScaleBrick) | Анализ: жизнеспособен ли TikTok/Instagram search как канал роста |
| `competitors` (ScaleBrick) | Аудит конкурентов по 3-поверхностному фреймворку |
| `keywords` (ScaleBrick) | Исследование high-intent ключей для TikTok/Instagram |
| `strategy` (ScaleBrick) | Полная маркетинговая стратегия |

### OpenSEO (SEO-воркфлоу)

| Скилл | Когда использовать |
|-------|-------------------|
| `seo-coach` | Режим коуча: объяснение воркфлоу, рекомендации |
| `seo-audit` | Аудит сайта, поиск возможностей роста трафика |
| `seo-project-setup` | Настройка контекста проекта |
| `keyword-research` | Поиск ключевых слов, оценка метрик и SERP |
| `keyword-clustering` | Кластеризация ключей по интенту, маппинг на страницы |
| `competitor-analysis` | Анализ одного конкурента |
| `competitive-landscape` | Карта лидеров рынка |
| `link-prospecting` | Поиск доноров ссылок, аутрич |
| `local-seo` | Аудит Google Business Profile, локальные конкуренты |
| `ai-prompt-research` | Вопросы людей к AI, цитирование сайтов |
| `ai-visibility-audit` | Аудит видимости бренда в AI-ответах (GEO/AEO) |
| `seo-report` | Генерация HTML-отчёта |

### MCP-справочники (как пользоваться MCP)

| Скилл | Когда использовать |
|-------|-------------------|
| `mcp-toolkit` | Полный справочник всех MCP и скиллов |
| `mcp-search` | Поиск и исследования (Exa, web-search, ComputeFirst) |
| `mcp-browser` | Браузер и аудит (Playwright, Desktop Commander, Frontend Checklist) |
| `mcp-docs` | Документация и код (Context7, Serena, Codebase Memory, Repomix) |
| `mcp-scraping` | Скрейпинг и конвертация (MarkItDown, Scrapling, Crawl4AI) |
| `mcp-security` | Безопасность (CVE Intelligence) |
| `mcp-seo` | SEO (iannuttall, OpenSEO) |
| `mcp-utils` | Утилиты (Time, Memory, sequential-thinking) |
| `mcp-design` | Дизайн, стили, вдохновение, дизайн-системы, палитры, типографика |
| `mcp-motion` | Анимации, переходы, эффекты, kinetic typography, particles |
| `mcp-copy` | Копирайт, заголовки, лендинги, реклама, конверсия, A/B-тесты |
| `mcp-css` | CSS, стили, токены, дизайн-системы, написание хорошего CSS |
| `mcp-ux` | UX/UI дизайн, доступность, юзабилити, паттерны, метрики |
| `mcp-visual` | Визуальная регрессия, CSS-дифф, сравнение страниц, layout shift |
| `mcp-network` | Сеть, DNS, SSL, email, мониторинг, SEO-данные (TPC, DNS Beautiful, Network MCP, InternetVitals, Nuqti) |
| `mcp-audit` | Аудит и тестирование: Lighthouse, WCAG, a11y, performance, SEO, security headers |

### Дизайн и фронтенд

| Скилл | Когда использовать |
|-------|-------------------|
| `frontend-design` | Создание UI-компонентов и страниц |
| `frontend-no-slop` | Критика UI, планы страниц, спеки компонентов |
| `ui-ux-design-pro` | Дизайн-системы, аудит UI, поиск паттернов |
| `forge-motion` | Продвинутая анимация (GSAP, Three.js, scroll-storytelling) |
| `web-search` | Мастер-поиск в интернете: Exa + web-search + Context7 + sequential-thinking + memory |

### Служебные

| Скилл | Когда использовать |
|-------|-------------------|
| `find-skills` | Поиск и установка новых скиллов |
| `opencode` | Вопросы по OpenCode (config, plugins, MCP, SDK) |
| `report` | Сообщение о баге OpenCode |
| `review-team` | Code review флотом специализированных агентов |
| `site-specification` | Извлечение спецификации сайта из описания |
| `browser` | Инструкции по браузерным инструментам |

---

## 4. Матрица выбора: задача → инструменты

| Задача | Основные инструменты | Скилл |
|--------|---------------------|-------|
| Исследование конкурентов | Exa + web-search + scrapling | `competitors` / `competitor-analysis` |
| Поиск ключей | Exa + web-search + OpenSEO | `keywords` / `keyword-research` |
| SEO-аудит сайта | OpenSEO, SEO (iannuttall), Frontend Checklist | `seo-audit` |
| Безопасность | CVE Intelligence | `mcp-security` |
| Чтение документации | Context7 (предпочтительно) → Exa/web-search | `mcp-docs` |
| Анализ кода/зависимостей | Codebase Memory, Serena, Repomix | `mcp-docs` |
| Конвертация документов | MarkItDown | `mcp-scraping` |
| Краулинг сайтов | Crawl4AI (JS-рендеринг), Scrapling (стелс) | `mcp-scraping` |
| Браузерная автоматизация | Playwright, Desktop Commander | `mcp-browser` / `browser` |
| Проверка времени/дат | Time | `mcp-utils` |
| Вычисления/трансформации | ComputeFirst | `mcp-utils` |
| Долгосрочная память | Memory (граф знаний) | `mcp-utils` |
| Структурированное мышление | sequential-thinking | `mcp-utils` |
| Дизайн/вдохновение | Inspo, standby.design | `mcp-design` |
| Анимации/эффекты | Motion Fab | `mcp-motion` / `forge-motion` |
| CSS/стили | CSS Crème, standby.design | `mcp-css` / `mcp-design` |
| UX/UI аудит | ux-mcp, designmind, web-stylebook | `mcp-ux` |
| Визуальная регрессия | Visual Parity | `mcp-visual` |
| Копирайт/конверсия | Persuasion Taxonomy, Writing Editor | `mcp-copy` |
| Аудит/тестирование | Lighthouse Audit, AccessLumens, Frontend Checklist | `mcp-audit` |
| Услуги/цены F&F | Memory (F&F_Pricing, F&F_Services) | `ff-services` |
| CRM / клиенты / финансы | CRM REST API (crm.ff-it.ru) | `crm-usage` |

---

## 5. Лучшие практики (из исследований)

### 5.1 Итеративный поиск
1. Сформулируйте вопрос одним предложением.
2. Определите критерии успеха.
3. Запустите 2–4 параллельных поиска (разные углы).
4. Прочитайте 2–4 источника полностью (не доверяйте сниппетам).
5. Уточните запросы по пробелам/противоречиям.
6. Перепроверьте ключевые утверждения на независимых источниках.
7. Синтезируйте ответ с цитатами (URL + дата + confidence).

### 5.2 Выбор инструмента поиска
- **Exa**: описывайте идеальную страницу (не ключевые слова). `category:company` / `category:people`.
- **web-search**: точные ключи, `lang: "ru"`, `provider: "duckduckgo"`.
- **Context7**: всегда предпочтительнее web search для доков библиотек.
- **Firecrawl/Scrapling/Crawl4AI**: для скрейпинга конкретных страниц.

### 5.3 Протоколы MCP
- Серверы на 2026-07-28 (markitdown, crawl4ai) требуют `"protocol": "auto"`.
- CSS Crème требует `"protocol": "legacy"`.
- Остальные работают на legacy (по умолчанию).
- Remote-серверы используют OAuth по умолчанию; при 401 — `/mcps` → войти.

### 5.4 Безопасность
- Никогда не коммитьте ключи — используйте `{env:...}`.
- Начинайте с read-only режимов.
- Соблюдайте robots.txt и rate limits.
- Не скрейпьте за логинами/пейволами.

### 5.5 Эффективность контекста
- Code Mode группирует инструменты по серверу: `tools.exa.web_search_exa(...)`.
- Не вызывайте все инструменты подряд — выбирайте минимальный набор.
- Для больших результатов используйте `maxCharacters` / `max_length`.

### 5.6 Верификация
- Утверждение = «проверено» только если 2+ независимых источника согласны.
- Помечайте confidence: 🟢 проверено / 🟡 вероятно / 🔴 непроверено / ⚪ неизвестно.
- Никогда не выдумывайте числа.

---

## 6. Устранение неполадок

| Проблема | Решение |
|----------|---------|
| Сервер не подключается | Проверить лог: `~/.local/share/opencode/log/opencode.log` |
| 401 Unauthorized | `/mcps` → войти (OAuth) |
| Protocol error (2026-07-28) | Добавить `"protocol": "auto"` в конфиг сервера |
| CSS Crème protocol error | Добавить `"protocol": "legacy"` |
| Timeout при старте | Увеличить `timeout.startup` (мс) |
| Инструмент не найден | Проверить namespace: `search({ namespace: "server-name" })` |
| npx-сервер медленный | Увеличить startup timeout или установить пакет глобально |
| AccessLumens первый запуск | Скачивает Chromium ~150 MB — подождать |

---

## 7. Быстрый старт (для новых сессий)

1. Прочитать этот файл или загрузить скилл `mcp-toolkit`.
2. Проверить `opencode.jsonc` — список серверов.
3. При задаче — выбрать скилл из раздела 3 и инструменты из раздела 4.
4. При поиске — следовать разделу 5.1.
5. При коде — использовать Context7 для доков.
6. При аудите — использовать Frontend Checklist + AccessLumens + Lighthouse Audit.
7. При SEO — проверить OpenSEO (`whoami`) и SEO (`seo_sites`).
8. При услугах/ценах — обращаться к `ff-services` и Memory.

---

## 8. Файлы проекта

| Файл | Назначение |
|------|-----------|
| `opencode.jsonc` | Конфиг MCP-серверов (31 сервер) |
| `.agents/skills/<id>/SKILL.md` | Скиллы (36 шт.) |
| `docs/MCP_AND_SKILLS_GUIDE.md` | Полная документация |
| `docs/MCP_QUICKSTART_RU.md` | Краткое руководство (русский) |
| `docs/WEB_SEARCH_MCP.md` | Документация по поиску и MCP |
| `AGENTS.md` | Правила проекта F&F + Auto-Routing |

---

*Документация обновляется при добавлении/удалении серверов или скиллов. Последнее обновление: 2026-11-24.*

---

## 9. Плагины (6)

| Плагин | Зачем | Скиллы |
|--------|-------|--------|
| `@upstash/context7-opencode` | Официальный Context7: MCP + скилл документации | context7-mcp |
| `opencode-mem` | Персистентная память между сессиями (local Turso/libSQL) | — |
| `@dietrichgebert/ponytail` | Ленивый senior dev mode: минимальные изменения, простые ответы | ponytail, ponytail-audit, ponytail-debt, ponytail-gain, ponytail-help, ponytail-review |
| `cc-safety-net` | Блокировка деструктивных команд и доступа к секретам | — |
| `superpowers` (git) | Полная методология разработки (brainstorm → plan → build) | brainstorming, writing-plans, executing-plans, subagent-driven-development, test-driven-development, systematic-debugging, verification-before-completion, using-git-worktrees, dispatching-parallel-agents, finishing-a-development-branch, requesting-code-review, receiving-code-review, writing-skills, diagnosing-superpowers, using-superpowers |
| `oh-my-opencode` | Полная оркестрация агентов, multi-model, LSP/AST | — |

DCP (`@tarquinen/opencode-dcp`) удалён — сокращал контекст.

Конфиг: `plugins` в `opencode.jsonc`.
