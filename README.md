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

## Публикация в интернет

### Вариант 1 — GitHub Pages (бесплатно, постоянный URL)

1. Создать репозиторий на GitHub (пустой, без README).
2. В папке сайта:
   ```bash
   git remote add origin https://github.com/ВАШ_ЛОГИН/ff-site.git
   git branch -M main
   git push -u origin main
   ```
3. В настройках репозитория: Settings → Pages → Source: Deploy from a branch → Branch: main → /(root) → Save.
4. Через 1–2 минуты сайт будет доступен по `https://ВАШ_ЛОГИН.github.io/ff-site/`.

### Вариант 2 — Netlify / Vercel (drag-and-drop)

- Netlify: https://app.netlify.com/drop — перетащить папку сайта, получить URL.
- Vercel: `npx vercel` в папке сайта.

### Вариант 3 — Cloudflare Pages

Загрузить папку через дашборд Cloudflare Pages. Файл `_headers` содержит CSP и cache-control.

## Структура

- `index.html` — главная
- `blog.html` — индекс блога (40+ статей)
- `blog/` — 32 гайда
- `articles/` — 8 больших разборов
- `services/`, `cases/`, `geo/` — подстраницы
- `map.html` — карта сайта
- `style.css`, `critical.css`, `script.js`, `calculator.js`
- `data/site-config.json` — единый source of truth для цифр
- `scripts/generate-sitemap.py` — генерация sitemap.xml
- `scripts/check-site.py` — CI-проверка
- `privacy.html`, `terms.html`, `cookie.html` — юридические страницы
- `files/dogovor.docx` — типовой договор

## Операционка

### Единый source of truth
- Цифры: `data/site-config.json`
- Политика конфиденциальности: `privacy.html`
- Политика cookie: `cookie.html`
- Типовой договор: `files/dogovor.docx`

### Проверка перед деплоем
См. `DEPLOY-CHECKLIST.md`

### Генерация sitemap
```bash
python scripts/generate-sitemap.py
```

### CI-проверка
```bash
python scripts/check-site.py
```

### Мониторинг битых ссылок
- Перед каждым деплоем — быстрая проверка
- Раз в месяц — полная проверка
- Скрипт: `scripts/check-site.py` (проверяет битые ссылки, пустые секции, placeholders, JS syntax, версии)

## Важно

Сайт статический: никакой сборки не требуется. Все ссылки относительные, работает с любого хостинга. Формы используют mailto fallback (Formspree ID не настроен).