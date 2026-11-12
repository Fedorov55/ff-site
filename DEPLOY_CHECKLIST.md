# Чек-лист деплоя на fedorov55.github.io/ff-site

## 1. Что заливать
- Весь репозиторий (159 HTML + CSS + JS + img + files/ + fonts/)
- `robots.txt`, `sitemap.xml`, `llms.txt`, `_headers`
- `CLOUDFLARE.md`, `MONITORING.md`, `AB_TESTS.md`

## 2. Файлы обновить в первую очередь
1. **`robots.txt`** — Sitemap и Host на `https://fedorov55.github.io/ff-site`
2. **`sitemap.xml`** — все URL на `https://fedorov55.github.io/ff-site/...`, актуальный lastmod
3. **`canonical`** — на всех страницах `https://fedorov55.github.io/ff-site/...`
4. **`og:url`** — на всех страницах `https://fedorov55.github.io/ff-site/...`
5. **Schema.org** — все `url` в JSON-LD на `https://fedorov55.github.io/ff-site/`

## 3. Плейсхолдеры заменить
- `` в `script.js` → реальный Formspree ID
- `00000000` → реальный ID Яндекс.Метрики (или удалить скрипт)
- `PLACEHOLDER_YANDEX` / `PLACEHOLDER_GOOGLE` → коды верификации
- (удалено: Calendly не используется)

## 4. 301-редиректы (настроить на сервере / .htaccess / nginx)
```
# Старые URL GitHub Pages → новый домен
https://fedorov55.github.io/ff-site/* → https://fedorov55.github.io/ff-site/* (301)

# Слэш в конце
https://fedorov55.github.io/ff-site/index.html → https://fedorov55.github.io/ff-site/ (301)

# Старые названия страниц (если были)
/compare.html → /compare-staff.html (301)
/compare-freelance.html → /compare-freelancer.html (301)
```

## 5. Порядок проверки после деплоя
1. Открыть `https://fedorov55.github.io/ff-site/` — главная загружается
2. Проверить `https://fedorov55.github.io/ff-site/robots.txt` и `https://fedorov55.github.io/ff-site/sitemap.xml`
3. Проверить canonical на 5 ключевых страницах (index, support, servers, services, cases)
4. Запустить Lighthouse (мобильный): Perf ≥ 90, A11y ≥ 95, BP 100, SEO 100
5. Проверить консоль: 0 красных ошибок
6. Отправить тестовую заявку через форму
7. Проверить Schema через Rich Results Test
8. Отправить sitemap в Яндекс.Вебмастер и Google Search Console
9. Проверить индексацию: `site:fedorov55.github.io/ff-site`

## 6. Закрытие старой версии (GitHub Pages)
- Вариант A: Оставить как staging (добавить `noindex` на все страницы зеркала)
- Вариант B: Настроить 301-редирект со всех URL GitHub Pages на fedorov55.github.io/ff-site
- Вариант C: Удалить репозиторий (не рекомендуется)

## 7. DNS и HTTPS
- A-запись: `fedorov55.github.io/ff-site` → IP сервера
- CNAME: `www.fedorov55.github.io/ff-site` → `fedorov55.github.io/ff-site`
- SSL-сертификат (Let's Encrypt)
- HSTS включён на сервере

## 8. После успешного переезда
- Проверить `site:fedorov55.github.io/ff-site` в Google и Яндекс
- Мониторить индексацию раз в неделю
- Добавить реальные отзывы + фото команды
- Создать карточки Яндекс.Бизнес / 2GIS
- Разместить гостевые посты
"