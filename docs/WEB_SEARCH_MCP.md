# Web Search MCP — использование в проекте F&F

## Что подключено

В `opencode.jsonc` (корень проекта) настроены семь бесплатных MCP-серверов **без API-ключей**:

| Сервер | Тип | Статус | Назначение |
|--------|-----|--------|------------|
| `exa` | remote | ✅ активен | Семантический поиск + чтение страниц (free tier) |
| `web-search` | local | ✅ активен | Поиск (DuckDuckGo/Bing/SearXNG) + универсальный `fetch_url`, без ключей |
| `context7` | remote | ✅ активен | Актуальная документация и примеры кода для любых библиотек/фреймворков |
| `sequential-thinking` | local | ✅ активен | Структурированное пошаговое мышление, ревизии, ветвление |
| `memory` | local | ✅ активен | Граф знаний — долгосрочная память между сессиями |
| `playwright` | local | ✅ активен | Автоматизация браузера: навигация, клики, скриншоты, консоль, сеть, Lighthouse |
| `time` | local | ✅ активен | Точное текущее время и конвертация часовых поясов |
| `seo` | local | ✅ активен | Google Search Console/Bing/Analytics MCP (требует `seo auth login`) |
| `markitdown` | local | ✅ активен | Конвертация PDF/DOCX/XLSX/PPTX/HTML → Markdown (заменяет платные парсеры) |
| `scrapling` | local | ✅ активен | Стелс-скрейпинг, браузерные сессии (заменяет Firecrawl scrape/crawl) |
| `crawl4ai` | local | ✅ активен | Краулинг/скрейпинг, извлечение, JS-рендеринг (protocol: auto) |
| `serena` | local | ✅ активен | Семантическая навигация по коду (uv + language servers) |
| `codebase-memory` | local | ✅ активен | Граф знаний по коду, trace_path, detect_changes |
| `chrome-devtools` | local | ✅ активен | Глубокая отладка: performance traces, сеть, консоль, скриншоты, Lighthouse |
| `computefirst` | remote | ✅ активен | Точный math, CSV/JSON transforms, date math, хеши (без ключа) |
| `cve-intelligence` | remote | ✅ активен | Поиск CVE, CISA KEV, EPSS, затронутое ПО (без ключа) |

Brave/Firecrawl/Jina/SearXNG (self-hosted) — опциональные апгрейды (см. ниже).

## Быстрый старт (всё уже работает)

Exa и web-search не требуют ключей. Примеры вызовов в Code Mode:

```js
// Exa — семантический поиск
const r = await tools.exa.web_search_exa({
  query: "pricing page of IT outsourcing company in Kazan with monthly tariffs",
  numResults: 8,
  objective: "Find pages with tariff tables; exclude blog posts."
});

// Exa — чтение страниц
const pages = await tools.exa.web_fetch_exa({
  urls: ["https://example.com/prices"],
  maxCharacters: 4000
});

// web-search — ключевой поиск (DuckDuckGo/Bing/SearXNG)
const s = await tools["web-search"].search_web({
  q: "IT-аутсорсинг Казань цены",
  limit: 10,
  lang: "ru",
  provider: "duckduckgo"
});

// web-search — универсальный fetch (HTML/PDF/text/JSON/XML/CSV/media)
const page = await tools["web-search"].fetch_url({
  url: "https://competitor.com/prices",
  format: "markdown",
  max_length: 8000,
  include_links: true
});
```

## Опциональные апгрейды (с ключами)

Если нужны SERP-фичи, полный краулинг или выше лимиты:

| Сервер | Ключ | Зачем |
|--------|------|-------|
| Brave Search | `BRAVE_API_KEY` | Точный поиск, SERP-фичи, новости |
| Firecrawl | `FIRECRAWL_API_KEY` | Полный краулинг сайтов, структурированное извлечение |
| OpenSEO | `https://app.openseo.so/mcp` | SEO-исследования, ключи, SERP, домены (требует аккаунт/API key) | `OPENSEO_API_KEY` |
| changedetection.io | ваш instance `/mcp/v1` | Мониторинг изменений страниц конкурентов (требует свой инстанс + токен) | instance URL + token |
| Jina Reader | `JINA_API_KEY` | Чтение PDF/arXiv, скриншоты, rerank |
| SearXNG (self-hosted) | `SEARXNG_URL` | Высоконагруженный поиск без лимитов |

Подключение: добавьте блок в `opencode.jsonc` и задайте env-переменную. Пример:

```jsonc
"brave-search": {
  "type": "local",
  "command": ["npx", "-y", "@brave/brave-search-mcp-server"],
  "environment": { "BRAVE_API_KEY": "{env:BRAVE_API_KEY}" }
}
```

## Безопасность

- Ключи **не хранятся** в репозитории — используется подстановка `{env:...}`.
- Не коммитьте `opencode.jsonc` с реальными ключами (они и так через env).
- Используйте read-only режимы где возможно.
- Соблюдайте robots.txt и rate limits.

## Скилл

Полная методология исследования — в `.agents/skills/web-search/SKILL.md`.
Вызывается как навык `web-search`.

## Другие полезные MCP-серверы (по запросу)

### Бесплатные / без ключей
| Сервер | Пакет/URL | Зачем |
|--------|-----------|-------|
| Playwright MCP | `@playwright/mcp` | Автоматизация браузера, e2e-тесты, скриншоты |
| Filesystem MCP | `@modelcontextprotocol/server-filesystem` | Чтение/запись файлов вне воркспейса (с ограничением путей) |
| Git MCP | `@modelcontextprotocol/server-git` | Git-операции (log, diff, blame) без shell |
| Time MCP | `@modelcontextprotocol/server-time` | Точное время/часовые пояса |
| Fetch MCP | `@modelcontextprotocol/server-fetch` | Простое чтение URL (уже покрыто web-search fetch_url) |

### С ключами / аккаунтом (по необходимости)
| Сервер | Зачем | Ключ |
|--------|-------|------|
| GitHub MCP | Репозитории, PR, issues, Actions | PAT (`GITHUB_TOKEN`) |
| Cloudflare MCP | Деплой, Workers, DNS, R2 | OAuth/API token |
| Vercel MCP | Деплои, проекты, логи | OAuth |
| Supabase MCP | БД, миграции, edge functions | OAuth |
| Sentry MCP | Ошибки, performance, triage | OAuth |
| Brave Search MCP | SERP-фичи, точный поиск | `BRAVE_API_KEY` |
| Firecrawl MCP | Полный краулинг, структурированное извлечение | `FIRECRAWL_API_KEY` |
| Jina Reader MCP | PDF/arXiv, скриншоты, rerank | `JINA_API_KEY` (чтение бесплатно с лимитом) |

### Как добавить любой сервер
```sh
opencode mcp add <name> --url <remote-url>          # remote
opencode mcp add <name> -- npx -y <package>          # local
opencode mcp list                                     # проверить статус
```
Или руками в `opencode.jsonc` (см. `mcp.servers`). После изменений — `/reload`.
```

