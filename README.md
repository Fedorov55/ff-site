# F&F IT — статический сайт

Премиальный IT-аутсорсинг сайт (Казань). Чистый HTML/CSS/JS, без сборщиков.

## Домены и деплой

**Основной продакшен-домен:** https://fedorov55.github.io/ff-site/
**Статус:** GitHub Pages (staging). Все страницы имеют `noindex, follow`.

Правила:
- Canonical, og:url, sitemap.xml и schema.org указывают на `https://fedorov55.github.io/ff-site/`
- Внутренние ссылки — относительные (`support.html`, `../cases/tobacco.html`)
- ff-it.ru и ff-team.ru НЕ используются (возвращают 404)
- Когда ff-it.ru начнёт отдавать 200 на все пути — переключить canonical в отдельном задании

## Запуск локально

```bash
# Python
python -m http.server 8000

# или Node
npx serve .
```

Открыть http://localhost:8000

## Сборка (минификация)

Проект использует esbuild для минификации CSS/JS.

```bash
# Установка зависимостей
npm install

# Сборка (минификация всех CSS и JS)
npm run build

# Линтинг
npm run lint:js
npm run lint:html

# Проверка синтаксиса JS
npm run audit
```

Результат сборки — папка `dist/` с минифицированными файлами.

## Публикация в интернет

### Вариант 1 — GitHub Pages (бесплатно, постоянный URL)
- Репозиторий: https://github.com/Fedorov55/ff-site
- Автодеплой при push в main
- URL: https://fedorov55.github.io/ff-site/

### Вариант 2 — Cloudflare Pages (рекомендуется)
- Подключить репозиторий к Cloudflare Pages
- Build command: `npm run build` (опционально)
- Output directory: `/` или `dist/`
- Headers: из файла `_headers`
- Автоматический HTTP/2, HTTP/3, Brotli

## Структура проекта

- `index.html` — главная
- `style.css` — основные стили (загружаются async)
- `critical.css` — критические стили (above-the-fold)
- `script.js` — основной JS (defer)
- `search.js` — поиск по сайту (defer)
- `calculator.js` — калькулятор IT-бюджета (defer)
- `search-index.json` — индекс для поиска
- `_headers` — заголовки для Cloudflare Pages
- `sitemap.xml` — карта сайта (157 URL)
- `robots.txt` — правила для краулеров
- `llms.txt` — описание для AI-систем
- `MONITORING.md` — инструкции по мониторингу
- `build.js` — скрипт сборки (esbuild)
- `package.json` — зависимости и скрипты