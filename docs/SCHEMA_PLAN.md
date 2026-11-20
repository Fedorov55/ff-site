# План усиления structured data (Яндекс CTR)

## 1. FAQPage
- **Где:** все страницы с FAQ-блоком (support, servers, services, index, compare, audits, infrastructure, security, cases, geo-страницы).
- **Что:** JSON-LD `FAQPage` с вопросами и ответами из блока FAQ.
- **Эффект:** rich snippet с вопросами в выдаче → CTR +15–25%.

## 2. HowTo
- **Где:** страницы с пошаговыми процессами (services, support, servers, infrastructure, audits).
- **Что:** JSON-LD `HowTo` с шагами «1. Заявка и диагностика», «2. Договор и сроки», «3. Выполнение», «4. Приёмка и гарантия».
- **Эффект:** rich snippet с шагами → CTR +10–15%.

## 3. Service / Product
- **Где:** services.html, support.html, servers.html, infrastructure/infrastructure.html, security/security.html.
- **Что:** JSON-LD `Service` с названием, описанием, ценой (от 10 000 ₽/мес), поставщиком (F&F).
- **Эффект:** rich snippet с ценой и рейтингом → CTR +20–30%.

## 4. BreadcrumbList
- **Где:** все внутренние страницы (уже на большинстве).
- **Что:** JSON-LD `BreadcrumbList` с цепочкой: Главная → Раздел → Страница.
- **Эффект:** хлебные крошки в сниппете → CTR +5–10%, удобство навигации.

## 5. Review / AggregateRating
- **Где:** index.html, services.html, cases.html, support.html.
- **Что:** JSON-LD `Review` / `AggregateRating` с реальными отзывами (имя, оценка, текст). Только если есть согласие клиентов.
- **Эффект:** звёзды в сниппете → CTR +25–40%.

## Приоритет реализации
1. **Высокий:** FAQPage на всех страницах с FAQ (уже частично есть).
2. **Высокий:** BreadcrumbList на всех внутренних страницах.
3. **Средний:** Service на коммерческих страницах.
4. **Средний:** HowTo на страницах с процессом.
5. **Низкий:** Review/AggregateRating (только с реальными отзывами).

---
*План составлен: 2026-11-20*
PY