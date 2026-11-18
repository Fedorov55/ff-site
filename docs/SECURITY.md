# SECURITY.md — F&F

## Политика безопасности

F&F серьёзно относится к безопасности. Этот документ описывает, как сообщить об уязвимости и какие меры приняты для защиты сайта и данных пользователей.

## Как сообщить об уязвимости

Если вы обнаружили уязвимость, отправьте описание на **FathFed@yandex.ru** с темой «Security: [краткое описание]». Мы ответим в течение 48 часов и, если подтвердим проблему, исправим её в ближайшем релизе. Публичное раскрытие — только после исправления.

## Ограничения платформы (GitHub Pages)

GitHub Pages **не поддерживает** кастомные HTTP-заголовки ответа. Это значит, что следующие заголовки **не могут** быть установлены через сервер:
- `Strict-Transport-Security` (HSTS)
- `X-Frame-Options`
- `X-Content-Type-Options`
- `Referrer-Policy`
- `Permissions-Policy`

**Что сделано:**
- CSP реализован через `<meta http-equiv="Content-Security-Policy">` на всех страницах.
- Referrer-Policy реализован через `<meta name="referrer">`.
- `frame-ancestors 'none'` в CSP заменяет X-Frame-Options (работает в современных браузерах).

**Рекомендация:** при миграции на Cloudflare Pages или Netlify добавить `_headers` / `netlify.toml` со всеми заголовками из раздела «Рекомендуемые заголовки».

## Чек-лист для разработчиков

**Запрещено:**
- Использовать `innerHTML` с пользовательским вводом. Используйте `textContent` или `createElement`.
- Использовать `eval()`, `Function()`, `document.write()`.
- Хардкодить секреты, токены, пароли в коде.
- Использовать внешние скрипты без SRI (`integrity` + `crossorigin`).
- Оставлять `console.log` с чувствительными данными.

**Обязательно:**
- Валидация на клиенте: `required`, `type="email"`, `pattern`, `maxlength`.
- Honeypot-поле в формах.
- Обязательный чекбокс согласия на обработку ПДн.
- Локальные шрифты (без Google Fonts).
- `loading="lazy"` для изображений.

## Рекомендуемые заголовки (для миграции)

```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self'; connect-src 'self' https://formspree.io; frame-ancestors 'none'; base-uri 'self'; form-action 'self' https://formspree.io;
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

## Контакт
- Email: FathFed@yandex.ru
- Telegram: @FathFed
- Телефон: +7 (901) 265-52-52
