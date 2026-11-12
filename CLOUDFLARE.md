# Инструкция по подключению Cloudflare

## 1. Подключение домена
1. Зарегистрируйте домен fedorov55.github.io/ff-site (если ещё не сделано).
2. В Cloudflare: Add Site → fedorov55.github.io/ff-site → выберите Free план.
3. Обновите NS-записи у регистратора на те, что выдаст Cloudflare.
4. Дождитесь распространения DNS (до 24 часов).

## 2. Настройка хостинга
- **Вариант A (Cloudflare Pages):** подключите репозиторий GitHub → Pages → ff-site → branch main. Build command: none (static). Output dir: /.
- **Вариант B (свой сервер):** загрузите файлы на сервер (nginx/Apache). Настройте SSL через Let's Encrypt.

## 3. Файл _headers
Файл `_headers` в корне репозитория автоматически применяется Cloudflare Pages:
- CSS/JS/Fonts/Images: Cache-Control 1 год, immutable
- HTML: Cache-Control 1 час, must-revalidate
- Security headers: X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy

Для своего сервера настройте аналогичные заголовки в nginx/Apache.

## 4. После подключения
1. Заменить `` в `script.js` на реальный Formspree ID.
2. Подключить Яндекс.Метрику (реальный ID) — раскомментировать скрипт.
3. Заменить `PLACEHOLDER_YANDEX` / `PLACEHOLDER_GOOGLE`.
4. Снять `noindex` с `privacy.html` (если нужна индексация).
5. Обновить canonical/og/sitemap на `https://fedorov55.github.io/ff-site/` (уже сделано).
6. Отправить sitemap в Яндекс.Вебмастер и Google Search Console.
7. Настроить 301-редиректы со старых URL.
8. Проверить Lighthouse на продакшене.

## 5. Проверка
- Lighthouse: Performance ≥ 90, A11y ≥ 95, BP 100, SEO 100
- Console: 0 ошибок
- Формы: тестовая отправка
- Schema: Rich Results Test
"