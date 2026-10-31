# PERFORMANCE_AUDIT.md — F&F Performance Audit

Дата: 2026-10-31

## Lighthouse (главная, мобильный)

| Метрика | Значение | Цель | Статус |
|---|---|---|---|
| LCP | 1.3s | ≤ 2.5s | ✅ |
| INP | 10ms | ≤ 200ms | ✅ |
| CLS | 0.004 | ≤ 0.1 | ✅ |
| TBT | 10ms | ≤ 200ms | ✅ |
| FCP | 1.3s | ≤ 1.8s | ✅ |
| Performance | 100 | ≥ 90 | ✅ |
| Accessibility | 100 | ≥ 95 | ✅ |
| Best Practices | 100 | — | ✅ |
| SEO | 100 | ≥ 100 | ✅ |

## Проверки

| Проверка | Результат |
|---|---|
| Горизонтальный скролл на 320px | Нет |
| Изображения без width/height | 0 (было 7, исправлено) |
| Ленивая загрузка | 217/217 img с loading="lazy" (кроме LCP) |
| Шрифты | Variable, font-display: swap, локальные |
| Внешние ресурсы | 0 (Google Fonts и Chart.js удалены) |
| content-visibility | Включено для off-screen секций |
| contain | Включено для карточек и компонентов |
| CSP | На всех 101 страницах |
| Ошибки в консоли | 0 |

## Известные ограничения
- Нет CrUX-данных (требуется реальный трафик и Search Console).
- PageSpeed Insights не проверялся (требует публичный URL — есть, но данные накапливаются).
- Размер страницы: главная ~75KB HTML, CSS ~118KB (style.css 67KB + overrides 51KB).
