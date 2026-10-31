# INTERACTIVE_AUDIT.md — F&F Interactive Features

Дата: 2026-10-31

## Реализовано

| Фича | Статус | Файл |
|---|---|---|
| Терминал в Hero | ✅ | index.html + script.js (heroTerminal) |
| Квиз «Проверка на прочность» (5 вопросов) | ✅ | quiz.html + script.js |
| Прогресс-бар квиза | ✅ | quiz.html |
| ROI-калькулятор (потери за инцидент) | ✅ | script.js (showQuizResult) |
| Кнопка «Скачать PDF» (window.print) | ✅ | script.js + print CSS |
| Конфигуратор «Соберите свой контур» | ✅ | services.html + script.js |
| Exit-intent попап | ✅ | все страницы + script.js |
| Cookie-баннер | ✅ | все страницы + script.js |
| Тёмная тема + переключатель | ✅ | script.js (themeToggle) |
| Live-метрики (data.json) | ✅ | index.html + data.json + script.js |
| Анимация fade-up (Intersection Observer) | ✅ | script.js |
| Микродоказательства у CTA | ✅ | index.html |
| Таблица «Что будет, если» (8 сценариев) | ✅ | index.html |
| Статус-страница | ✅ | status.html |
| Демо-панель (Chart.js) | ✅ | demo.html |
| Telegram/MAX deep links | ✅ | 35/34 страниц |

## Не реализовано / частично

| Фича | Статус | Примечание |
|---|---|---|
| noscript fallback | ⚠️ Отсутствует | Добавить на index, contacts, quiz |
| State object (централизованный) | ⚠️ Частично | Логика в script.js, не вынесена в отдельный state.js |
| Модульность (quiz.js, roi.js и т.д.) | ⚠️ Частично | Всё в одном script.js (~37k символов) |
| PDF через jsPDF | ⚠️ Заменено на window.print() | Достаточно для статического сайта |
| Отправка результата квиза в Telegram (deep link) | ⚠️ Не реализовано | Кнопка есть, но deep link не генерируется |
| Переключатель периода 24ч/7д/30д в демо | ⚠️ Не проверено | Нужно проверить demo.html |

## Рекомендации
1. Добавить `<noscript>` fallback на ключевых страницах.
2. Рассмотреть вынос JS в модули (state.js, quiz.js и т.д.) — но для статического сайта текущая архитектура работает.
3. Добавить deep link для отправки результата квиза в Telegram.
4. Проверить переключатель периода в demo.html.
