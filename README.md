# F&F IT — статический сайт

Премиальный IT-аутсорсинг сайт (Казань). Чистый HTML/CSS/JS, без сборщиков.

## Запуск локально

```bash
# Python
python -m http.server 8000

# или Node
npx serve .
```

Открыть http://localhost:8000

## Публикация в интернет (чтобы другая ИИ могла открыть)

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

Загрузить папку через дашборд Cloudflare Pages.

## Структура

- `index.html` — главная
- `blog.html` — индекс блога (40 статей)
- `blog/` — 32 гайда
- `articles/` — 8 больших разборов
- `services/`, `cases/`, `geo/` — подстраницы
- `map.html` — карта сайта
- `style.css`, `style-overrides.css`, `script.js`

## Важно

Сайт статический: никакой сборки не требуется. Все ссылки относительные, работает с любого хостинга.
