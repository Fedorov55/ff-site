# DEPLOY.md — Развёртывание F&F site

## Архитектура
- Репозиторий: https://github.com/Fedorov55/ff-site.git (ветка main)
- Продакшен: GitHub Pages — https://fedorov55.github.io/ff-site/
- Тестовый сервер: 92.255.199.90:8080 (nginx, root /var/www/test-site)

## Правила работы (ОБЯЗАТЕЛЬНО для всех сессий)

1. **Все изменения — в локальной папке** `C:\opencode\f&f\site`. Никаких правок на сервере напрямую.
2. **После каждой задачи/фазы:**
   - Запустить `npm run audit` (node --check) и htmlhint.
   - Обновить `docs/CHANGELOG.md`.
   - Задеплоить на тестовый сервер: `python scripts/deploy-test.py`
   - Закоммитить и запушить в репозиторий: `git add -A && git commit -m "..." && git push origin main`
3. **Не оставлять заглушек/TODO** в коде.
4. **Валидировать** каждое изменение: Lighthouse, Rich Results Test, консоль браузера.

## Деплой на тестовый сервер

```bash
python scripts/deploy-test.py
```

Параметры подключения:
- Хост: 92.255.199.90
- Порт SFTP: 2222
- Логин: ftpuser
- Пароль: !1assert!!
- Удалённый путь: /var/www/test-site
- Проверка: http://92.255.199.90:8080

Альтернатива (FTP, порт 21) — не рекомендуется (пароль в открытом виде).

Управление сервером (SSH, порт 2222, логин odmin):
- Перезапуск nginx: `echo "!1assert!!" | sudo -S systemctl reload nginx`
- Просмотр логов: `sudo tail -f /var/log/nginx/access.log`

## Деплой в репозиторий

```bash
git add -A
git commit -m "feat: описание изменений"
git push origin main
```

GitHub Pages автоматически обновляется после push в main.

## Сборка

```bash
npm install
npm run build        # esbuild CSS+JS -> dist/
npm run lint:js      # eslint
npm run lint:html    # htmlhint
npm run audit        # node --check
```

## Локальный запуск

```bash
python -m http.server 8000
# или
npx serve .
```

## Проверка качества

- htmlhint: `node node_modules/htmlhint/bin/htmlhint "**/*.html"`
- Lighthouse: через MCP lighthouse-audit или https://pagespeed.web.dev/
- Rich Results Test: https://search.google.com/test/rich-results
- Sitemap: `python scripts/generate-sitemap.py` (автодискавери HTML)

## Структура проекта

- Корневые страницы: index, articles, blog, cases, contacts, industries, prices, servers, services, support, sysadmin-cost-kazan, terms-of-work, 404
- Подкаталоги: ai, articles, audits, blog, cases, company, compare, incidents, industries, infrastructure, leads, legal, pain, resources, security, services
- legal/: privacy.html, terms.html, cookie.html, consent.html
- css/: style.css, critical.css, components.css, tokens.css
- js/: script.js, calculator.js, search.js, search-worker.js
- img/: WebP-изображения + srcset-варианты
- fonts/: woff2 (subset cyrillic_latin)
- scripts/: deploy-test.py, generate-sitemap.py, check-site.py, и др.
- docs/: аудиты, планы, CHANGELOG.md, MCP_AND_SKILLS_GUIDE.md
- AGENTS.md: правила агента, SEO, auto-routing скиллов/MCP
"