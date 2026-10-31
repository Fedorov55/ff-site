# SECURITY_AUDIT.md — F&F Security Audit

Дата: 2026-10-31

## Таблица проблем

| # | Проблема | Приоритет | Статус | Решение |
|---|---|---|---|---|
| 1 | Нет CSP | High | ✅ Исправлено | CSP через `<meta http-equiv>` на всех 101 страницах |
| 2 | Нет Referrer-Policy | Medium | ✅ Исправлено | `<meta name="referrer">` на всех страницах |
| 3 | Внешние Google Fonts (14 страниц) | Medium | ✅ Исправлено | Удалены, используются локальные шрифты |
| 4 | Chart.js CDN в demo.html без SRI | Low | ✅ Исправлено | Удалён (не используется) |
| 5 | Honeypot только на 1 из 101 страниц | High | ✅ Исправлено | Honeypot добавлен во все формы (exit-popup + contacts) |
| 6 | Чекбокс согласия на ПДн не везде | Medium | ✅ Исправлено | Добавлен в контакты и квиз |
| 7 | innerHTML в script.js (12 мест) | Medium | ✅ Проверено | Все используют статические/внутренние данные, не пользовательский ввод |
| 8 | location.search → textarea value | Low | ✅ Безопасно | Используется `.value`, не innerHTML |
| 9 | Секреты в репозитории | Critical | ✅ Проверено | `git grep` не нашёл токенов/ключей |
| 10 | .gitignore неполный | Low | ✅ Исправлено | Добавлены .env, *.bak, *.tmp, .agents, docs, promo |
| 11 | Нет security.txt | Low | ✅ Исправлено | Создан /.well-known/security.txt |
| 12 | GitHub Pages: нет кастомных заголовков | High | ⚠️ Ограничение платформы | Документировано в SECURITY.md. Рекомендована миграция на Cloudflare Pages/Netlify |
| 13 | HSTS отсутствует | Medium | ⚠️ Ограничение платформы | GitHub Pages не поддерживает. Рекомендована миграция |
| 14 | X-Frame-Options отсутствует | Medium | ⚠️ Ограничение платформы | Заменён на `frame-ancestors 'none'` в CSP |

## Результаты проверок

- **Секреты в репозитории:** 0 (проверено `git grep` по паттернам `ghp_`, `sk-`, `AKIA`, `password`, `secret`, `token`).
- **Опасные паттерны:** `eval()` — 0, `document.write` — 0, `Function()` — 0. `innerHTML` — 12 (все безопасны).
- **Внешние ресурсы без SRI:** 0 (Google Fonts удалены, Chart.js удалён).
- **Формы:** honeypot на 101 странице, consent на 8 страницах с формами.
- **Битые ссылки:** 0.
- **Lighthouse:** Performance 100, Accessibility 100, Best Practices 100, SEO 100.
- **Ошибки в консоли:** 0.

## Валидация

- [x] CSP не ломает сайт (проверено в браузере).
- [x] Формы валидируются на клиенте.
- [x] Honeypot работает (заполненное скрытое поле блокирует отправку).
- [x] Чекбокс согласия обязателен.
- [x] security.txt доступен по /.well-known/security.txt.
- [x] SECURITY.md и SECURITY_AUDIT.md созданы.
- [ ] GitHub Actions для проверки безопасности (не настроены — требует ручной настройки).
