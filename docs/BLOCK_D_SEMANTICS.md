# Блок D — Семантика и структура (2026-11-25)

## Ядро (core queries)
| Запрос | Посадочная | Статус |
|--------|-----------|--------|
| абонентское IT-обслуживание Казань | support.html, services/it-support.html | ✅ |
| сервер под ключ Казань | servers.html, services/server-1c.html | ✅ |
| системный администратор Казань | sysadmin-cost-kazan.html, sistemnyy-administrator-kazan.html | ✅ |
| обслуживание 1С-сервера Казань | services/server-1c.html | ✅ |
| выезд сисадмина Казань | company/visit.html, services.html | ✅ |
| обслуживание компьютеров Казань | obsluzhivanie-kompyuterov-kazan.html | ✅ (новая) |
| удалённый сисадмин Казань | udalennyy-sisadmin-kazan.html | ✅ (новая) |
| обслуживание серверов Казань | obsluzhivanie-serverov-kazan.html | ✅ (новая) |
| IT-поддержка Казань | it-podderzhka-kazan.html | ✅ (новая) |
| мониторинг серверов Казань | monitoring-serverov-kazan.html | ✅ (новая) |
| резервное копирование Казань | rezervnoe-kopirovanie-kazan.html | ✅ (новая) |
| восстановление данных Казань | vosstanovlenie-dannykh-kazan.html | ✅ (новая) |
| компьютерная помощь Казань | kompyuternaya-pomoshch-kazan.html | ✅ (новая) |
| настройка сети офиса Казань | nastroyka-seti-ofisa-kazan.html | ✅ (новая) |
| IT-аутсорсинг для малого бизнеса | it-autsorsing-malyy-biznes.html | ✅ (новая) |

## Кластеры → посадочные (интенты разделены)
- **Покупка (commercial):** services.html, servers.html, support.html, prices.html, contacts.html
- **Стоимость (cost):** sysadmin-cost-kazan.html, staff-sysadmin-cost.html, compare/*
- **Как выбрать (guide):** infrastructure/vybor-podryadchika.html, blog/how-to-choose.html
- **Проблема (pain):** pain/* (7 страниц)
- **Статья (informational):** blog/* (46 статей), articles/* (6)
- **Кейс (case):** cases/* (26 страниц)
- **Отрасль (industry):** industries/* (13 страниц)
- **Город (geo):** chelny.html, almet.html, nizhnekamsk.html, zelendolsk.html

## Инвентаризация (181 URL)
- Всего: 181 HTML-страница
- Тонких страниц (<300 слов): 0
- Дубликатов H1: 0 (исправлено)
- Дубликатов title: 0 (исправлено)
- Дубликатов meta description: 0 (исправлено)
- Дубликатов FAQ-вопросов между секциями: 0 (исправлено)

## Дубли FAQ на одной странице
- index.html: 2 секции → 1 (13 вопросов)
- support.html: 3 секции → 3 (убраны 3 перекрывающихся вопроса)
- servers.html: 3 секции → 3 (убран 1 перекрывающийся вопрос)
- prices.html: 4 секции, 0 дубликатов

## Внутренняя перелинковка
- Коммерция ↔ TCO: compare/*, sysadmin-cost-kazan.html
- Коммерция ↔ Кейсы: cases.html, case-* (ссылки на страницах услуг)
- Коммерция ↔ FAQ: FAQ-блоки на всех коммерческих страницах
- Новые посадочные ↔ главная: блок «Полезные страницы» на index.html
- Новые посадочные ↔ services: блок «Смотрите также» на services.html
- Блог/pain ↔ коммерция: pain-страницы ссылаются на услуги

## Не размазывать вес по тонким pain/blog-дублям
- Все страницы имеют >300 слов контента (тонких нет)
- Self-canonical на всех 181 странице
- Каждая страница имеет уникальный title/H1
- Интенты различаются (problem/guide/commercial/comparison/case)
- Рекомендация: при добавлении новых страниц — проверять уникальность интента

## Городские лендинги
- Созданы: chelny.html, almet.html, nizhnekamsk.html, zelendolsk.html
- Основание: реальные кейсы в этих городах
- Рекомендация: мониторить трафик; если нет спроса — добавить noindex

---
*Создано: 2026-11-25*
"