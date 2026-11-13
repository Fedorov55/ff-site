# Мониторинг fedorov55.github.io/ff-site

## 1. Uptime (UptimeRobot / Uptime Kuma / Pingdom)
Настрой проверки каждые 5 минут на:
- https://fedorov55.github.io/ff-site/ (главная)
- https://fedorov55.github.io/ff-site/support.html (абонентка)
- https://fedorov55.github.io/ff-site/servers.html (серверы)
- https://fedorov55.github.io/ff-site/contacts.html (контакты)

Алерт: email + Telegram при downtime > 2 мин.

## 2. Core Web Vitals (LCP / INP / CLS)
- **Раз в 1–2 недели**: повторный PSI (PageSpeed Insights) + полевые данные в Search Console / Яндекс.Вебмастере.
- Следить за **75-м перцентилем** (именно его смотрит Google для CWV-статуса).
- Цели: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1.
- Если метрика «Needs improvement» или «Poor» — возвращаться к соответствующему разделу чек-листа (LCP/INP/CLS).
- Инструменты: PSI (labs + field), CrUX Dashboard, Search Console → Core Web Vitals report.

## 3. Проверка sitemap и robots.txt
- Раз в неделю: `curl -I https://fedorov55.github.io/ff-site/sitemap.xml` → 200
- Раз в неделю: `curl -I https://fedorov55.github.io/ff-site/robots.txt` → 200
- Проверять, что sitemap не содержит 404-страниц и служебных URL
- После добавления новых страниц — регенерировать sitemap

## 4. Отслеживание 404
- Яндекс.Вебмастер → Индексирование → Ошибки → 404
- Google Search Console → Coverage → Excluded → Not found (404)
- Раз в неделю проверять новые 404
- Настроить 301-редиректы для старых URL

## 5. Lighthouse CI (опционально)
- Запускать Lighthouse при каждом деплое
- Цели: Performance ≥ 90, A11y ≥ 95, SEO 100
- Алерт при падении ниже порога

## 6. Формы и заявки
- Тестовая отправка формы раз в неделю
- Проверка, что заявки доходят (Formspree / Telegram)
- Мониторинг конверсии через Яндекс.Метрику (цели)

## 7. SSL и домен
- Проверка SSL-сертификата (срок действия)
- Автопродление Let's Encrypt
- Проверка HSTS и security headers после переезда

## 8. Контент
- Проверка уникальности title/description при добавлении новых страниц
- Проверка битых ссылок при каждом обновлении
- Обновление lastmod в sitemap при изменениях
"