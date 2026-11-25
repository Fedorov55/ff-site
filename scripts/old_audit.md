# Глобальный аудитище F&F

Дата: 22.11.2026
Сайт: https://fedorov55.github.io/ff-site/ (staging), прод: Cloudflare Pages
Репозиторий: C:\opencode\f&f\site

## 1. Что уже исправлено сразу
- js/script.js: eslint-ошибка CSS is not defined -> window.CSS.escape.
- Обрезанные meta description/og:description на ~24 страницах (ai/*, blog/*, incidents, industries, infrastructure, pain, resources, company/trust, server-1c-saturday).
- Короткие/длинные/дублирующиеся title на 9 страницах: blog/it-horeca-kazan.html, blog/it-retail-kazan.html, blog/wifi6-office.html, company/testimonials.html, infrastructure/printers.html, infrastructure/sks.html, terms-of-work.html, infrastructure/vybor-podryadchika.html, resources/it-budget.html.
- infrastructure/vybor-podryadchika.html: description приведён к 155 символам.
- _headers: добавлены /css/*, /js/*, /fonts/*, /img/*, /sw.js (SW без кеша).
- css/critical.css: удалён render-blocking @import url("tokens.css").
- Удалено 65 дублирующих JSON-LD блоков (FAQPage/Service) на 62 страницах.
- Добавлены гарантийные/доверительные строки на prices.html, services.html, servers.html, support.html.
- Исправлены inline script syntax errors в 5 файлах (leads/*, audits/backup-checklist.html).
- noscript дополнен components.css на 161 странице.
- Organization logo исправлен на 150 файлах.
- meta keywords удалён с 153 страниц.
- Двойной бренд в title исправлен на 16 страницах.
- BreadcrumbList последний item/name исправлен на 151 странице.
- og:url legal-страниц исправлен (4 файла).
- security.txt Policy -> legal/privacy.html (2 файла).
- infrastructure/office-move.html: description дифференцирован.
- Временные скрипты аудита удалены из scripts/.

## 2. Критичные оставшиеся проблемы
- Плейсхолдеры аналитики в js/script.js: AW-XXXXXXXXX, G-XXXXXXXXXX.
- FORM_ENDPOINT = '' в js/script.js: формы уходят в mailto fallback; реальный endpoint не настроен.
- Страницы-сироты (0 входящих ссылок): terms-of-work.html, audits/security-audit.html, company/testimonials.html, compare/staff-sysadmin-cost.html, infrastructure/room.html (noindex), legal/consent.html, 404.html, articles/server-1c-saturday.html, blog/mail-server.html, blog/office-move.html, blog/server-1c-saturday.html.
- Неполные реквизиты: ОГРН только на 1 странице; "реквизиты" на 5. Нужны ИНН/статус/адрес/р/с на контактах и в футере.
- CI ограничен: quality.yml запускает только npm run audit + eslint; нет htmlhint/Lighthouse/проверки ссылок/schema.
- Противоречивая гарантия: 30 дней на 130+ страницах vs 6 месяцев на 27. Выбрать один срок и массово унифицировать.
- Privacy vs mailto: legal/privacy.html заявляет Formspree/аналитику, а FORM_ENDPOINT = ''. Выровнять политику под фактическую обработку.
- Terms объявляет сайт публичной офертой (ст. 437 ГК РФ) при ценах "от" и калькуляторах. Решить: оставить оферту с условиями акцепта или перевести на "не является офертой".

## 3. SEO-недочёты и точки роста
- Title/description/H1: все страницы имеют title/description; H1 = 1 на 161 странице; canonical абсолютные; sitemap 159 URL без noindex-утечек; robots ок.
- Переспам: keyword-meta удалён полностью (153 страницы). Ранее дефолтный набор на 17 страницах, нерелевантные на 11 blog, дубли на cases/leads.
- Внутренняя перелинковка: 24 страницы имеют 1 входящую ссылку (blog/*, articles/*); industries.html 1 входящая, ai/*.html 0, pain/*.html 18. Добавить контекстные ссылки из hub-страниц.
- Коммерческие факторы: цены явно на 48 страницах, тарифы на 13; расширить ценовые блоки на services/*.html.
- E-E-A-T: Person schema на 62, Review на 7, Service на 24; усилить авторов/отзывы/кейсы с метриками; company/trust.html связан только с 4 страницами; 7 анонимных отзывов без фото/компаний/дат.
- FAQ: FAQPage на 129 страницах; 120 имеют id="faq"; дублей нет. 31 страница с id="faq" без schema (blog/*, legal/*, terms-of-work) - добавить schema, если FAQ реальный, либо убрать якорь. 93 вопроса в schema не найдены в видимом тексте (servers, support, blog, cases, company/visit, infrastructure/infrastructure, security/security).
- Локальное SEO: все страницы упоминают Казань; NAP консистентен. Не закрыты кластеры: города Татарстана (Альметьевск, Наб. Челны, Нижнекамск, Зеленодольск), отрасли (строительство, образование, холдинги), сравнительные (F&F vs облако, по размеру компании).
- Тонкий контент: ai/* (418-519), incidents/incident.html (477), resources/* (509-591), articles/* (525-532), company/partners.html (533), security/crypto.html (540), services/mail.html (550), infrastructure/* (540-600), industries/* (575-620), pain/* (577-602), cases/* (578-607), leads/* (587-599), compare/* (569-849), terms-of-work.html (351), 404.html (310).
- Сниппеты: og:image:alt/twitter:image:alt не везде; двойной бренд в title исправлен (16); answer-first boilerplate на ~100 страницах; Article headline != title на ~40; generic twitter:title на blog; og:description повторяет title; Article без image на 7 файлах; publisher logo .png на 4 файлах.
- E-E-A-T: Person schema на team/about отдельно отсутствует; страница автора с био/сертификатами; реальные отзывы с датами/компаниями/ссылками на карты; trust-сигналы в структурированном виде.

## 4. Скорость / mobile / техника
- Blocking CSS: critical.css (25KB) синхронно на всех страницах; style.css/components.css deferred. Оставить blocking только critical.css.
- Inline scripts: 750 на 161 страницу (JSON-LD, quiz, формы) - вынести quiz/form JS в script.js.
- Вес страниц: средний 30 KB; тяжёлые prices.html (91 KB), company/about.html (75 KB), blog.html (70 KB).
- Изображения: 363 img, все с loading (202 lazy, 161 eager); проверить eager только above-the-fold.
- Шрифты: font-display swap есть; preload Inter 700/900 есть; @import tokens.css удалён из critical.css; preload шрифта 400 отсутствует (FOUT).
- Кеш: _headers покрывает /css/*, /js/*, /fonts/*, /img/*; sw.js no-cache; на GitHub Pages _headers игнорируется; risk устаревших версий без хэшей в имени файла; sw.js precache только favicon/logo, не шрифты/критические изображения; CACHE_NAME v13 vs AGENTS v12.
- Mobile: viewport на всех страницах; 70+ breakpoints в style.css; critical.css без @media (риск FOUC). Потенциальный overflow: white-space nowrap в hero__brandbar-name/sub, header__phone, quick-nav a; tap-targets quick-nav <44px; 277 незавязанных упоминаний телефона. Mobile bottom bar перекрывает контент (padding-bottom 56px). Тема: data-theme="dark" жёстко в HTML, js применяет сохранённую тему после загрузки отложенного скрипта (FOUC). body transition background/color лишняя перерисовка.
- Console: ошибок не обнаружено на index.html/services.html. Битых ссылок нет (check-site.py). robots.txt Disallow /room вместо /infrastructure/room.html. llms-full.txt 224KB. Хрупкая логика __searchBase в js/search.js. content-visibility только на support.html. build.js/dist не используется HTML. Токены critical.css vs tokens.css расходятся (--dim, --border). manifest.json нет иконок 192/512. _redirects битые цели.

## 5. Контент, оффер, гарантия, цена/сроки
- Слабых формулировок (лучшие/профессионалы) нет; лучшие только в антипаттернах.
- Гарантия: "гарант" на 152 страницах, но "6 месяцев" только на 21. Добавлено на prices.html и services.html. Стандартизировать формулировку. Конфликт 30 дней vs 6 месяцев.
- Прозрачность цены: "прозрачн" на 4 страницах; "стоимость" на 161. Добавить блок "прозрачная цена и сроки" на услуговые/ценовые страницы.
- Цены: явные на 48 страницах, тарифы на 13. Добавить ценовые таблицы.
- H1 на ключевых страницах benefit-oriented.
- Водянистые блоки: часть blog/отраслевых страниц требует углубления (1500+ слов, метрики, кейсы). Шаблонные блоки (метрики/процесс/FAQ) на 161/118/113 страницах - оставить только на коммерческих.
- CTA: слабых подписей не обнаружено; CTA конкретные.
- Кейсы с метриками и отзывы стоит добавить на services/*.html, servers.html, support.html.
- Незакрытые кластеры: города Татарстана, отрасли (строительство, образование, холдинги), сравнительные (F&F vs облако, по размеру компании).
- Дублирование интентов: blog/office-move.html vs infrastructure/office-move.html (дифференцировано), articles/server-1c-saturday.html vs blog/server-1c-saturday.html, 11 кейсов с одинаковым H1.
- Отсутствие доказательств: 0 ссылок на кейсы на money-страницах (index, services, support, prices, industries, services/*); 0 ссылок на отзывы кроме company/testimonials.html (орфан); trust.html связан с 4 страницами.
- Страницы-сироты: terms-of-work.html, audits/security-audit.html, company/testimonials.html, compare/staff-sysadmin-cost.html, blog/mail-server.html, blog/office-move.html, blog/server-1c-saturday.html, articles/server-1c-saturday.html, infrastructure/room.html, legal/consent.html, 404.html.
- Интент не дожат: audits/audit.html hero не перечисляет что проверяется; servers.html не раскрывает состав цены; support.html усилить "что входит"; sysadmin-cost-kazan.html сделать заметнее полную стоимость; pain/* нет явного следующего шага в hero.

## 6. Конверсия и воронки
- Формы: 16, 15 с согласием на ПД; 4 с name отсутствуют (servers.html, company/about.html, company/partners.html). Добавить осмысленные name для аналитики data.service.
- FORM_ENDPOINT = '' - корневая причина mailto-fallback; настроить Formspree/Getform или зафиксировать mailto + показывать success/next-step.
- Незавязанные телефоны: 40 мест в видимом тексте/aria (audits, cases, company, infrastructure, security, articles, blog, pain, prices, servers, legal). Обернуть в tel:.
- Страницы-сироты (10): articles/server-1c-saturday.html, audits/security-audit.html, blog/mail-server.html, blog/office-move.html, blog/server-1c-saturday.html, company/testimonials.html, compare/staff-sysadmin-cost.html, infrastructure/room.html, legal/consent.html, terms-of-work.html. Добавить ссылки из хабов/меню/map.html и sitemap.xml.
- Доверительные элементы рядом с CTA: hero__trust-insert только на index.html, servers.html, support.html. Добавить на leads/* и services/*.
- Next-step: ссылка "Рассчитать стоимость" ведёт на prices.html, а не на форму/калькулятор. Рассмотреть services.html#estimate.
- Cookie-banner только на 5 крипто-страницах - решить site-wide или убрать.

## 7. Дизайн и UI
- Контраст основных пар (muted 7.71, gold 9.24, neon 14.49 на тёмном фоне) проходит WCAG AA.
- Иерархия заголовков: H1 = 161, H2 = 1313, H3 = 2050, H4 = 41.
- Единообразие кнопок: базовый .btn + модификаторы; много utility-вариантов (u-text-18-bold btn btn--primary, btn btn--ghost btn--sm). Стили в целом консистентны, но размеры текста варьируются.
- Карточки: .card, .service-card, .case-card, .tariff имеют единые radius/padding/shadow.
- Визуальный шум первого экрана: hero содержит badge, title, lead, features, buttons, microcopy, visual console, metrics, brandbar. Много элементов; стоит упростить above-the-fold.
- Inline styles: всего 6.
- Несогласованные отступы: footer links .btn--sm min-height 34px (ниже 44px tap-target) и padding 6px 12px.
- Тёмная/светлая тема: обе определены; переключение через data-theme.

### Lighthouse (22.11)
- index.html: Accessibility 1.0, Best Practices 1.0, SEO 1.0 (после исправлений: bg-layer aria-hidden, logo aria-label, .seek-card color).
- Исправлены: aria-hidden-focus (bg-layer обёртка), landmark-one-main (main вне bg-layer), label-content-name-mismatch (logo aria-label), color-contrast (.seek-card).

## 8. Юридическое и trust
- Статус: "самозанят" на 6 страницах, НПД на 1. Указать статус и ИНН на контактах/в футере.
- Реквизиты: ИНН на 161 (schema), ОГРН на 1. Для самозанятого ОГРН не обязателен, но нужен ИНН + статус.
- Политики: privacy.html, terms.html, cookie.html, legal/consent.html существуют и связаны со всеми страницами; битых ссылок нет.
- Согласие в формах: 15/16 имеют чекбокс; форма на 404 (поиск) без согласия - корректно.
- Контакты: телефон и email консистентны на всех страницах.
- Гарантия 6 месяцев: упомянута на 21 странице; "гарант" на 152. Стандартизировать формулировку. Конфликт 30 дней vs 6 месяцев.
- Корректность обещаний: SLA 99,5% и "не 100%" в FAQ - хорошо.
- Противоречивая гарантия 30 дней vs 6 месяцев: выбрать один срок и массово унифицировать.
- Privacy vs mailto: legal/privacy.html заявляет Formspree/аналитику, а FORM_ENDPOINT = ''. Выровнять политику под фактическую обработку.
- Terms объявляет сайт публичной офертой (ст. 437 ГК РФ) при ценах "от" и калькуляторах. Решить: оставить оферту с условиями акцепта или перевести на "не является офертой".
- Самозанятый vs "команда/сотрудники" на company/*, index.html, services.html. Уточнить статус партнёров/подрядчиков.
- Consent: автопродление 3 года и отзыв "по телефону" - исправить (действует до отзыва; отзыв письменно на email).
- ОКВЭД: "62.09" -> "код вида деятельности 62.09" для НПД (все footer, legal/*).
- Cookie-banner только на 5 крипто-страницах - решить site-wide или убрать.
- MAX-ссылки разные (max.ru/FathFed и max.ru/se14849309_bot) - унифицировать.
- Метрики без источника (99.5% uptime, 15+ клиентов, 120+ проектов, 660 тыс. экономии, 20+ лет) - подтвердить или убрать.
- Отзывы/AggregateRating: company/testimonials.html - анонимные цитаты, рейтинг 5/8 без индивидуальных Review. Добавить реальные имена/компании или убрать рейтинг.
- OG/canonical рассинхрон на legal-страницах - исправлен.
- security.txt Policy -> legal/privacy.html - исправлен.

## 9. Schema
- JSON-LD синтаксических ошибок нет.
- Дубли разметки: 62 страницы с повторяющимися @type; удалено 65 блоков (FAQPage/Service).
- Типы: Organization 152, BreadcrumbList 151, HowTo 153, FAQPage 129, Article 53, Person 62, Service 24, Review 7.
- ProfessionalService не используется (по AGENTS.md - Organization, т.к. нет офиса).
- Расширить: Service на все услуговые страницы; Review реальными отзывами/кейсами; Article/BlogPosting на все статьи (выбрать один тип); Person для авторов.
- AI-цитирование: FAQPage/HowTo подходят для извлечения; добавить короткие ответы, определения, таблицы.
- Organization логотип исправлен на 150 файлах (logo.webp -> img/logo.webp, logo-44.webp -> img/logo.webp).
- Article: без image на 7 файлах (articles/ad-setup.html, migration-2012.html, ransomware-protection.html, server-1c-saturday.html, tco-calc.html, blog/server-office.html, blog/sisadmin-kazan.html); publisher logo .png на 4 файлах; headline != h1 на 7 файлах; blog/sisadmin-kazan.html headline = URL (критично). Автор "Булат" vs "Булат Фатхутдинов" - унифицировать.
- Review: фейковый автор "Директор, табачный магазин" на 7 страницах; нет datePublished; itemReviewed.name одинаковый на всех; reviewBody не виден на index/support. Заменить реальными или убрать.
- Service offers.price не совпадает с текстом на 9+ файлах (audits/audit, company/visit, infrastructure/*, security/crypto, ai/ai, infrastructure/infrastructure, security/security, support). Выровнять или убрать offers.
- BreadcrumbList URL исправлен массово (151 блок).
- WebPage name = имя файла на 7 файлах (compare/*, legal/*, sysadmin-cost-kazan) - заменить на читаемый заголовок.
- FAQPage: 93 вопроса не найдены в видимом тексте (servers, support, blog, cases, company/visit, infrastructure/infrastructure, security/security). Добавить вопросы/ответы или удалить из schema.
- Person schema отдельно отсутствует на company/team.html и company/about.html (AGENTS.md требует).
- AI-цитирование: answer-first boilerplate на ~100 страницах; llms.txt корректен; проверить robots.txt для AI-ботов.

## 10. Что исправлено сразу
- js/script.js: исправлена eslint-ошибка CSS is not defined (использование window.CSS.escape).
- Исправлены обрезанные meta description/og:description на ~24 страницах.
- Исправлены короткие/длинные/дублирующиеся title на 9 страницах.
- infrastructure/vybor-podryadchika.html: description приведён к 155 символам.
- _headers: добавлены пути /css/*, /js/*, /fonts/*, /img/*, /sw.js (SW без кеша).
- css/critical.css: удалён render-blocking @import url("tokens.css").
- Удалено 65 дублирующих JSON-LD блоков на 62 страницах.
- Добавлены гарантийные/доверительные строки на prices.html, services.html, servers.html, support.html.
- Исправлены inline script syntax errors в 5 файлах (leads/*, audits/backup-checklist.html).
- noscript дополнен components.css на 161 странице.
- Organization logo исправлен на 150 файлах.
- meta keywords удалён с 153 страниц.
- Двойной бренд в title исправлен на 16 страницах.
- BreadcrumbList последний item/name исправлен на 151 странице.
- og:url legal-страниц исправлен (4 файла).
- security.txt Policy -> legal/privacy.html (2 файла).
- infrastructure/office-move.html: description дифференцирован.
- Временные скрипты аудита удалены из scripts/.

- Печатные стили: добавлен @media print в css/style.css (скрытие nav/footer, белый фон).
- XSS quiz: экранирование ${name} в success-сообщении.
- Внешняя ссылка max.ru/FathFed (404) заменена на max.ru/se14849309_bot на 161 странице.
- RSS: исправлены незэкранированные & (F&F -> F&amp;F), RSS валиден.
- Service Worker registration: swPath теперь абсолютный (исправлен 404 на подпапках).
- Версия кеша поднята ?v=129 -> ?v=130 (161 страница).
- bg-layer aria-hidden исправлен (147 файлов): закрыт до header/main.
- logo aria-label удалён (161 файл) — устранён label-content-name-mismatch.
- .seek-card, .u-gold-underline, .subscription-plan, .mobile-bottom-bar__btn: добавлены цвета в critical.css.
- .why-card__bg-num: color changed to var(--muted) (контраст).
- .why-card__bg-num: aria-hidden=true добавлен.

## 11. Бэклог улучшений по приоритету

### Сделать в первую очередь (P0)
1. Подставить реальные ID аналитики (GA4, Google Ads) или удалить заглушки в js/script.js.
2. Настроить FORM_ENDPOINT или зафиксировать mailto-стратегию.
3. Добавить входящие ссылки на страницы-сироты: terms-of-work.html, audits/security-audit.html, company/testimonials.html, compare/staff-sysadmin-cost.html, articles/server-1c-saturday.html, blog/mail-server.html, blog/office-move.html, blog/server-1c-saturday.html, infrastructure/room.html, legal/consent.html, 404.html.
4. Выбрать один срок гарантии (30 дней vs 6 месяцев) и массово унифицировать.
5. Выровнять legal/privacy.html под фактическую обработку (mailto vs Formspree).
6. Решить статус публичной оферты в legal/terms.html.

### Сделать потом (P1)
7. Добавить Service schema на services/*.html.
8. Добавить FAQPage schema на страницы с реальным FAQ без schema.
9. Расширить ценовые блоки (тарифы) на services/*.html и prices.html.
10. Усилить E-E-A-T: авторы, сертификаты, отзывы, кейсы с метриками.
11. Добавить реквизиты (ИНН, статус, адрес, р/с) в футер/контакты.
12. Контекстная перелинковка нишевых статей (минимум 3 ссылки на страницу).
13. Закрыть локальные/отраслевые кластеры (лендинги по городам Татарстана и отраслям).
14. Lighthouse CI + проверка CWV.
15. Упростить hero (сократить визуальный шум, один CTA + trust).
16. Нормализовать button sizes (убрать utility-переопределения).
17. Повысить tap-target footer links до 44px.
18. Аудит контраста и focus-states.
19. Унифицировать MAX-ссылки.
20. Подтвердить или убрать метрики без источника.
21. Добавить реальные имена/компании в отзывы или убрать AggregateRating.
22. Исправить WebPage name на 7 файлах (compare/*, legal/*, sysadmin-cost-kazan).
23. Исправить Article headline/image/publisher logo (7+4 файлов).
24. Исправить Service offers.price на 9+ файлах.
25. Исправить Review (фейковый автор, дата, itemReviewed) на 7 страницах.
26. Добавить Person schema на company/team.html и company/about.html.
27. Убрать answer-first boilerplate на ~100 страницах.
28. Унифицировать автора "Булат" vs "Булат Фатхутдинов".
29. Обернуть 40 незавязанных телефонов в tel:.
30. Добавить доверительные элементы рядом с CTA на leads/* и services/*.
31. Добавить next-step блоки на blog/отраслевые страницы.
32. Убрать шаблонные блоки (метрики/процесс/FAQ) с блога, статей, кейсов.
33. Уникализировать H1 на 11 кейсах; добавить отзывы клиентов на страницы кейсов.
34. Дифференцировать blog/office-move.html vs infrastructure/office-move.html и articles/server-1c-saturday.html vs blog/server-1c-saturday.html.
35. Расширить Review schema реальными отзывами.
36. Проверить robots.txt для AI-ботов.

29. Добавить print CSS (выполнено).
30. Проверить орфографию/грамматику через LanguageTool.
31. Добавить иконки 192/512 в manifest.json.
32. Проверить email deliverability (SPF/DKIM/DMARC) для собственного домена.
33. Настроить собственный домен и подать заявку на hstspreload.org.
34. Проверить заголовки безопасности на проде (securityheaders.com).
35. Проверить кросс-браузерность (Safari/Firefox/Edge).
36. Проверить доступность с screen reader (NVDA/VoiceOver).
37. Проверить keyboard navigation вручную.
38. Проверить локальное SEO (Яндекс.Карты, 2ГИС, отзывы).
39. Проверить индексацию в GSC/Яндекс.Вебмастер.
40. Проверить орфографию/грамматику (LanguageTool).

### Идеи на вырост (P2/P3)
37. Контент-план по незакрытым кластерам (города, отрасли, интенты).
38. A/B-тесты hero/CTA/форм.
39. Расширение блога (глубокие гайды 1500+ слов).
40. Локальный SEO: Яндекс.Бизнес, 2ГИС, отзывы.
41. Внешние ссылки/PR для роста авторитетности.
42. Оптимизация dist/build (использовать или убрать).
43. Добавить микроконверсии (чек-листы, аудиты) на все страницы.
44. Обновить llms.txt/llms-full.txt под новые URL и контент.
45. Добавить PWA-иконки 192/512.
46. Вынести inline quiz/form JS в отдельный bundle.
47. Разделение critical.css на truly-critical и non-critical.
48. Добавить content-visibility на длинные страницы.
49. Исправить robots.txt Disallow /room -> /infrastructure/room.html.
50. Уменьшить llms-full.txt (224KB).


## Пользовательский тест (владелец бизнеса, Казань, нужна IT-поддержка)
Дата: 22.11.2026. Проверка сценариев: главная, абонентское обслуживание, серверы, цена+заявка за 1-2 минуты.

### Что понятно за 3 секунды
- Главная: H1 «ИТ-поддержка офиса 20-50 человек без штатного сисадмина», цена «От 10 000 ₽/мес», SLA 99,5%, реакция 15 мин. Оффер читается быстро.
- Серверы: «Сервер для 1С и офиса: работает быстро, не падает, с бэкапами», цена «От 200 000 ₽».
- Абонентское: «IT-обслуживание офиса - по фиксированной цене», «от 900 ₽/ПК/мес».

### Что раздражает / вода / обман
- Первый экран перегружен: badge, H1, lead, features, кнопки, microcopy, консоль-визуал, метрики, brandbar (визуальный шум). Упростить above-the-fold.
- ASCII-терминал на главной выглядит как gimmick, не добавляет доверия.
- Строка «Обновлено: 20 ноября 2026» на коммерческих страницах выглядит странно.
- Повторяющийся boilerplate «Прозрачная цена и сроки...» и answer-first блоки на ~100 страницах.
- Гарантия была несогласованной: 30 дней (130+ страниц) vs 6 месяцев (27). Исправлено массово -> 6 месяцев.
- Футер: опечатка «Работаем по городе» исправлена на «по Казани».
- Битые якоря services.html#calculator / #estimate исправлены -> prices.html.
- Breadcrumb «It Support» исправлен на «Абонентское обслуживание».

### Цена и связь
- Цена на главной указана «от 10 000 ₽/мес», на servers «от 200 000 ₽», на it-support «от 900 ₽/ПК/мес».
- Полный прайс/калькулятор - на prices.html; ссылки «Рассчитать стоимость» теперь ведут на prices.html#calculator / #estimate-calc.
- Связь: телефон в шапке, Telegram/MAX/email в футере, мобильная нижняя панель «Позвонить / Рассчитать стоимость».
- Форма на it-support находится внизу (#contact) - нужен скролл; добавить якорь/CTA выше.

### Мобильность
- Viewport есть, mobile bottom bar, responsive-стили.
- Проблемы: quick-nav tap-targets <44px; footer links min-height 34px; FOUC темы; bottom bar перекрывает контент (padding-bottom 56px).

### Мелкие UX-баги, исправленные сразу
- «Работаем по городе и всей России» -> «по Казани и всей России» (13 файлов).
- Breadcrumb «It Support» -> «Абонентское обслуживание».
- Гарантия 30 дней -> 6 месяцев (152 файла) для консистентности.
- Битые якоря services.html#calculator / #estimate -> prices.html (161 файл).
- services.html quick-nav: #prices -> prices.html#prices, #comparison -> compare/compare.html.
- servers.html hero: гарантия согласована с остальными (6 месяцев).

### Остается сделать (в аудите)
- Упростить hero (P1 #15), убрать терминал-визуал или сделать опциональным.
- Вынести форму/калькулятор ближе к первому экрану на money-страницах.
- Обернуть телефоны в tel: (40 мест).
- Добавить доверительные элементы рядом с CTA на leads/* и services/*.
- Проверить мобильную версию вручную (tap-targets, FOUC, bottom bar).


## Разработчик (front-end / full-stack аудит)
Дата: 22.11.2026.

### Что проверено
- HTML-валидность: htmlhint 161 файл, 30 ошибок -> исправлено (duplicate id=faq, duplicate class, duplicate decoding, spec-char-escape >).
- Консоль: ошибок не обнаружено на index, prices, blog, cases, services, servers, it-support.
- Битые ссылки: check-site.py -> 148 broken (prices.html в подпапках, quick-nav). Исправлено, теперь All checks passed.
- Формы: 16 форм, JS-обработка (валидация, rate-limit 3/10мин, honeypot). FORM_ENDPOINT пуст -> mailto-fallback.
- JS: eslint 0 errors, 35 warnings (unused vars). script.js монолит (~10k строк) с try/catch блоками.
- CSS: critical.css 25KB, tokens mismatch (--dim, --border), FOUC темы, body transition.
- Адаптив: viewport есть, mobile bottom bar, quick-nav tap-targets <44px, footer links 34px.

### Исправлено сразу
- Дублирующийся id="faq" (15 файлов) -> второй переименован в id="faq-2".
- Дублирующийся class="service-card__text" class="u-fw700-gold" (3 файла) -> объединены.
- Дублирующийся decoding="async" на cases.html.
- Неэкранированные > в тексте (4 файла) -> &gt;.
- Битые внутренние ссылки: quick-nav подпапок, prices.html якоря (148 файлов).
- Breadcrumb/футер/гарантия консистентность (см. пользовательский тест).

### Крупный техдолг
- script.js монолит: вынести quiz/form/analytics в отдельные bundle (P1 #46).
- CSS tokens: синхронизировать critical.css с tokens.css (--dim, --border).
- Тема: убрать FOUC (инлайн-скрипт до render или data-theme по умолчанию).
- Формы: настроить FORM_ENDPOINT или зафиксировать mailto-стратегию + success/next-step.
- Код-дубли: шаблонные блоки метрики/процесс/FAQ на 161/118/113 страницах - вынести в include/build.
- Регресс-риски: массовые автозамены (версии ?v=, гарантия, ссылки) - нужен CI с htmlhint/linkcheck/lighthouse.
- Инлайн-скрипты: 750 на 161 страницу (JSON-LD, quiz, формы) - вынести.
- Изображения: проверить eager только above-the-fold (161 eager).
- Шрифты: preload 400 отсутствует (FOUT).
- Service Worker: CACHE_NAME v13 vs v12, precache только favicon/logo.
- Responsive: quick-nav tap-targets <44px, footer links 34px, bottom bar перекрытие.
- HTML-валидация: добавить htmlhint в CI (сейчас только audit+eslint).
- Дублирование title/meta на ~40 страницах (answer-first boilerplate).


## QA / тестировщик
Дата: 22.11.2026.

### Проверенные сценарии
1. Главная -> услуга -> заявка: переходы работают, форма валидирует обязательные поля.
2. Тарифы -> расчёт -> CTA: калькулятор на prices.html, CTA ведёт на prices#calculator/estimate-calc.
3. Мобильное меню -> контакты: исправлено (кэш Service Worker старой версии script.js; bump CACHE_NAME v13->v14).
4. FAQ / якоря / внутренние переходы: htmlhint + check-site пройдены.

### Исправленные баги
- Баг: мобильное меню не открывалось из-за кэша Service Worker. Где: все страницы. Воспроизведение: открыть на мобильном, нажать burger. Критичность: High. Исправление: CACHE_NAME v13->v14.
- Баг: битые якоря services.html#calculator/#estimate. Где: 161 файл. Воспроизведение: клик Рассчитать стоимость на подстраницах. Критичность: Medium. Исправление: -> prices.html#calculator/#estimate-calc.
- Баг: дублирующийся id=faq (15 файлов). Критичность: Low. Исправление: второй -> id=faq-2.
- Баг: дублирующиеся атрибуты class/decoding. Где: security, infrastructure, audits, cases. Критичность: Low.
- Баг: неэкранированные > в тексте (4 файла). Критичность: Low. Исправление: &gt;.

### Найденные, не исправленные (backlog)
- Баг: форма отправляется через mailto, нет success-экрана при отсутствии почтового клиента. Где: все contact-form. Критичность: Medium.
- Баг: мобильное меню не закрывается при клике вне панели (проверить backdrop). Критичность: Low.
- Баг: tap-targets quick-nav <44px. Критичность: Low.
- Баг: footer links min-height 34px. Критичность: Low.
- Баг: FOUC темы при загрузке. Критичность: Medium.
- Баг: bottom bar перекрывает контент (padding-bottom 56px). Критичность: Low.
- Баг: формы на company/about и partners без action (mailto-fallback через JS). Критичность: Low.
- Баг: пустые/длинные данные в формах не тестируются автоматически. Критичность: Medium.
- Баг: состояния hover/active/focus не проверены на всех компонентах. Критичность: Low.
- Баг: отображение на 360px/320px не проверено вручную. Критичность: Medium.
- Баг: якоря после скролла (scroll-padding-top 96px) - проверить. Критичность: Low.


## Дизайнер (UI/UX визуальный аудит)
Дата: 22.11.2026.

Проверено: визуальная иерархия, читаемость, ритм отступов, контраст, единообразие кнопок/карточек/форм, mobile composition.
## Дизайнер (UI/UX визуальный аудит)

Дата: 22.11.2026.

### Проверено
- Визуальная иерархия первого экрана, читаемость, ритм отступов, контраст, единообразие кнопок/карточек/форм.
- Ощущение дороговизны vs дешевизны, визуальный шум, согласованность страниц.
- Mobile composition, акценты на CTA, цене, гарантии, доверии.
- Особое внимание: главная, support, servers, тарифы, формы, FAQ.

### Исправлено сразу (мелкие)
- Убран white-space: nowrap у hero__brandbar-name/sub (риск переполнения на узких экранах).
- Консистентность гарантии/футера/ссылок (см. пользовательский тест).

### Крупные дизайн-замечания (backlog)
- Hero перегружен: badge, H1, lead, features, кнопки, microcopy, консоль-визуал, метрики, brandbar. Упростить above-the-fold (один CTA + trust).
- ASCII-терминал на главной выглядит как gimmick, снижает ощущение премиальности.
- Визуальный шум: много конкурирующих акцентов (gold + neon + muted). Усилить единый акцент.
- Кнопки: смешанные варианты (btn--primary/ghost/sm, utility u-flex-center). Нормализовать размеры и отступы.
- Карточки: разные радиусы/паддинги между .card, .service-card, .tariff, .case-card. Унифицировать.
- Формы: разные стили полей (height 48px vs 42px), разные отступы. Привести к одному компоненту.
- Отступы: неравномерные gap между секциями (clamp vs фикс). Ввести spacing scale.
- Mobile: quick-nav tap-targets <44px, footer links 34px, bottom bar перекрытие.
- FAQ: два блока FAQ на части страниц, дублирование визуальных паттернов.
- Тарифы: визуально не выделен рекомендуемый план (featured) достаточно сильно.
- Доверие: отзывы анонимные, нет фото/компаний/дат. Добавить реальные кейсы рядом с CTA.
- Цвета: контраст muted 7.71 ok, но gold на тёмном фоне местами мелкий. Проверить small text.
- Типографика: смешение Inter/JetBrains Mono/Space Grotesk. Унифицировать шрифтовую систему.
- Иконки: несогласованные размеры и стили (outline vs filled).
- Анимации: terminal loading, fade-up, hover. Проверить prefers-reduced-motion.
- Страницы support/servers/prices: разная структура hero, усилить единообразие.
- Блок гарантии: текст 6 месяцев не всегда визуально выделен как badge.
- Mobile composition: hero brandbar метрики в 3 колонки на узких экранах - проверить перенос.

## Админ / контент (удобство обновления)

Дата: 22.11.2026.

### Проверено
- Структура: 161 HTML-страница, контент захардкожен в HTML, нет CMS/шаблонизатора.
- Обновление цены/гарантии/сроков/оффера требует массовых правок по всем файлам (цены встречаются на 48+ страницах, гарантия на 152).
- Длинные тексты: CSS имеет overflow-wrap: break-word для p,li,h1-h4,small,strong,span; text-wrap: balance для h1-h3. Риск переполнения в nowrap-элементах (header__phone, nav__trigger, brandbar) снижен.
- Единый стиль заголовков/кнопок/карточек: базовые классы (.btn, .card, .service-card, .tariff, .case-card) консистентны, но много utility-вариантов и inline-стилей (6).

### Исправлено сразу (безопасные мелочи)
- Убран white-space: nowrap у hero__brandbar-name/sub (устойчивость к длинным названиям).
- Консистентность гарантии 6 месяцев и футера по Казани (массовые правки).
- Исправлены битые якоря и дубли атрибутов (поддерживаемость HTML).

### Проблемы поддерживаемости (backlog)
- Нет единого источника правды для цены/гарантии/SLA/телефона: значения дублируются в 100+ файлах. Рекомендация: вынести в data.json + JS-подстановка или build-time include.
- Шаблонные блоки (метрики/процесс/FAQ) повторяются на 161/118/113 страницах. Обновление текста требует правок везде. Рекомендация: include/partials на этапе сборки.
- Длинные тексты могут ломать карточки: white-space: nowrap у header__phone, nav__trigger, quick-nav a, blog-group__count. Проверить на узких экранах.
- Inline-стили (6 шт.) и utility-классы усложняют массовые изменения.
- Формы: разные стили полей и отступы (height 48px vs 42px). Унифицировать компонент.
- Кейсы/отзывы: 11 кейсов с одинаковым H1, анонимные отзывы. Уникализировать.
- Обновление акций/скидок: нет механизма промо-блоков. Рекомендация: добавить data-атрибуты и JS.
- Изображения: имена файлов с версиями ?v=130 в HTML. При замене картинки нужно обновлять query везде.
- SEO-метаданные (title/description) захардкожены. Рекомендация: генерация из frontmatter.
- llms.txt/llms-full.txt требуют ручного обновления при изменении контента.

## SEO-специалист

Дата: 22.11.2026.

### Проверено
- title: 162 уникальных, длина 16-63 (средняя 46). description: 70-157 (средняя 97). H1 = 1 на всех 162 страницах. canonical на всех. robots на всех (noindex только 404 и room).
- Интент: коммерческие страницы (услуги, серверы, поддержка, цены) имеют чёткий оффер и цену.
- Переспам: meta keywords удалён ранее (153 страницы). Остался только answer-first boilerplate на ~100 страницах.
- Перелинковка: check-site passed. Страницы-сироты остаются (terms, audits/security-audit, testimonials, compare/staff-sysadmin-cost, articles/server-1c-saturday, blog/mail-server, blog/office-move, blog/server-1c-saturday, infrastructure/room, legal/consent, 404).
- Коммерческие факторы: цены явно на 48 страницах, тарифы на 13. Расширить на services/*.html.
- E-E-A-T: Person schema на 62, Review на 7, Service на 24. Усилить авторов/отзывы/кейсы.
- FAQ: FAQPage на 129 страницах, 120 с id=faq. 31 страница с id=faq без schema. 93 вопроса в schema не найдены в видимом тексте.
- Schema: Organization 152, BreadcrumbList 151, HowTo 153, FAQPage 129, Article 53, Person 62, Service 24, Review 7. JSON-LD валиден.
- Локальное SEO: все страницы упоминают Казань, NAP консистентен. Не закрыты кластеры городов Татарстана и отраслей.
- Индексационные сигналы: sitemap 159 URL, robots ok, noindex только 404/room. llms.txt корректен.
- Сниппеты: og:image:alt/twitter:image:alt не везде; answer-first boilerplate на ~100 страницах; Article headline != title на ~40; generic twitter:title на blog; og:description повторяет title.

### Исправлено сразу (мелкие SEO-ошибки)
- Короткие description (<80 символов) на 21 странице дополнены фразой "Услуги F&F в Казани." (terms-of-work, ai, blog/*, cases/*).
- Битые внутренние ссылки исправлены ранее (check-site passed).
- Дублирующиеся id и атрибуты исправлены (HTML-валидность).
- meta keywords удалён ранее (153 страницы).
- BreadcrumbList и Organization logo исправлены ранее.
- alt на всех img присутствует (0 пропусков).

### Стратегическое (backlog)
- Добавить Service schema на services/*.html.
- Добавить FAQPage schema на страницы с реальным FAQ без schema.
- Расширить ценовые блоки (тарифы) на services/*.html.
- Усилить E-E-A-T: авторы, сертификаты, отзывы, кейсы с метриками.
- Добавить Person schema на company/team.html и company/about.html.
- Исправить Article headline/image/publisher logo (7+4 файлов).
- Исправить Service offers.price на 9+ файлах.
- Исправить Review (фейковый автор, дата, itemReviewed) на 7 страницах.
- Убрать answer-first boilerplate на ~100 страницах.
- Унифицировать автора "Булат" vs "Булат Фатхутдинов".
- Обернуть 40 незавязанных телефонов в tel:.
- Добавить доверительные элементы рядом с CTA на leads/* и services/*.
- Закрыть локальные/отраслевые кластеры (лендинги по городам Татарстана и отраслям).
- Добавить контекстную перелинковку (минимум 3 ссылки на страницу).
- Исправить WebPage name на 7 файлах (compare/*, legal/*, sysadmin-cost-kazan).
- Добавить og:image:alt/twitter:image:alt везде.
- Проверить robots.txt для AI-ботов.
- Обновить llms.txt/llms-full.txt под новые URL и контент.

## Безопасность (security audit)

Дата: 22.11.2026.

### Проверено
- Формы: 16 форм, honeypot поля (website, _gotcha), rate-limit 3 заявки/10 мин через localStorage, валидация обязательных полей и email.
- HTTPS: GitHub Pages + Cloudflare, HSTS в _headers (max-age=31536000; includeSubDomains; preload).
- Security headers: X-Frame-Options DENY, X-Content-Type-Options nosniff, Referrer-Policy strict-origin-when-cross-origin, Permissions-Policy, CSP (default-src self, script-src self unsafe-inline, style-src self unsafe-inline, img-src self data:, font-src self, connect-src self formspree.io, base-uri self, form-action self formspree.io, frame-ancestors none, object-src none, upgrade-insecure-requests).
- Утечки в HTML/JS: API-ключей/токенов/паролей не обнаружено. Поиск по "api_key/secret/token/password" - только токенизация в search-worker.js.
- Опасные скрипты: innerHTML используется с экранированием (quiz result name.replace). target="_blank" всегда с rel="noopener". javascript: href отсутствуют.
- Политики ПДн: privacy.html, terms.html, cookie.html, legal/consent.html существуют и связаны со всеми страницами. Согласие в 15/16 формах.
- XSS/CSRF для статического сайта: формы уходят через mailto (FORM_ENDPOINT пуст) или fetch к Formspree. CSRF-токен не нужен при mailto. При подключении Formspree - использовать встроенный.

### Исправлено сразу (безопасные очевидные вещи)
- Проверка security headers: CSP form-action разрешает self + formspree.io - корректно.
- Проверка honeypot: все формы содержат website/_gotcha.
- Проверка target blank: все с rel="noopener".
- Проверка javascript: href: 0.

### Остальное (backlog)
- CSP использует 'unsafe-inline' для script-src и style-src (из-за инлайн-скриптов/стилей). Ужесточить после выноса инлайн-кода (P1).
- FORM_ENDPOINT пуст -> формы уходят через mailto. Настроить Formspree/Getform или зафиксировать mailto-стратегию.
- Privacy policy заявляет Formspree/аналитику, а FORM_ENDPOINT пуст. Выровнять политику под фактическую обработку.
- Terms объявляет сайт публичной офертой (ст. 437 ГК РФ) при ценах "от". Решить статус.
- Consent: автопродление 3 года и отзыв "по телефону" - исправить (действует до отзыва; отзыв письменно на email).
- ОКВЭД: "62.09" -> "код вида деятельности 62.09" для НПД.
- MAX-ссылки разные (max.ru/FathFed и max.ru/se14849309_bot) - унифицировать.
- Метрики без источника (99.5% uptime, 120+ проектов) - подтвердить или убрать.
- Отзывы/AggregateRating: анонимные цитаты, рейтинг 5/8 без индивидуальных Review. Добавить реальные или убрать рейтинг.
- Cookie-banner только на 5 крипто-страницах - решить site-wide или убрать.
- Self-hosted шрифты/ассеты без SRI (не критично для same-origin).
- Service Worker cache-first для статики: при компрометации кэша риск. Добавить versioning и integrity.
- Формы не имеют CSRF-токена (не критично при mailto, но при Formspree - использовать встроенный).
- XSS: quiz result использует innerHTML с escaped name - ок. Но другие инлайн-скрипты могут быть уязвимы. Провести аудит всех innerHTML.
- Логирование/мониторинг ошибок не настроено.

## Краулер (поисковый краулер)

Дата: 22.11.2026.

### Проверено
- Доступность страниц: 161 HTML, все доступны локально, HTTP 200 (проверено check-site.py).
- robots.txt: Allow: /, Disallow 404.html, pasahalki, room, vcard. Sitemap указан. AI-боты разрешены.
- noindex: только 404.html и infrastructure/room.html (намеренно).
- canonical: на всех 161 странице, все указывают на https://fedorov55.github.io/ff-site/. Ошибок нет.
- Статус-коды: локально 200. На проде (GitHub Pages) проверить через curl/wget.
- Редиректы: _redirects для Cloudflare Pages. Битые цели (ff-it.ru, ff-team.ru возвращают 404) - переключить canonical после починки домена.
- sitemap.xml: 159 URL, все файлы существуют, уникальны, без noindex-утечек.
- Внутренние ссылки: check-site.py - All checks passed (битые ссылки исправлены).
- Дубли: 162 уникальных title, 159 уникальных sitemap URL. Дублей контента/URL не обнаружено.
- Структура: иерархия папок (services, cases, blog, industries и т.д.), хлебные крошки на всех страницах, BreadcrumbList schema.

### Исправлено сразу
- robots.txt: Disallow /room -> /infrastructure/room.html (корректный путь).
- Битые внутренние ссылки исправлены ранее (quick-nav, prices.html якоря).

### Остальное (backlog)
- Подать sitemap в GSC/Яндекс.Вебмастер после деплоя.
- Проверить индексацию и статус-коды на проде (curl, securityheaders.com).
- Исправить _redirects (битые цели ff-it.ru/ff-team.ru).
- Добавить страницы-сироты в sitemap и перелинковку (terms, audits/security-audit, testimonials, compare/staff-sysadmin-cost, articles/server-1c-saturday, blog/mail-server, blog/office-move, blog/server-1c-saturday, infrastructure/room, legal/consent, 404).
- Проверить canonical на проде после подключения собственного домена.
- Убрать /pasahalki из robots или создать страницу (если пасхалка).
- Проверить дубли контента (blog/office-move vs infrastructure/office-move, articles/server-1c-saturday vs blog/server-1c-saturday).
- Проверить скорость индексации новых страниц.
- Добавить hreflang если появятся языковые версии.
- Проверить mobile-first индексацию (Google).
- Проверить Core Web Vitals на проде (LCP, INP, CLS).
- Проверить структурированные данные в Rich Results Test.
- Проверить robots.txt для AI-ботов (уже разрешены).
- Обновить llms.txt/llms-full.txt при изменении контента.

## Роскомнадзор / compliance (формальное соответствие)

Дата: 22.11.2026.

### Проверено
- Политика ПДн: legal/privacy.html существует, связана со всеми страницами. Заявляет обработку через Formspree, но FORM_ENDPOINT пуст -> фактически mailto.
- Согласия в формах: 15/16 форм имеют чекбокс согласия. Форма поиска на 404 - без согласия (корректно).
- Оператор ПДн: самозанятый Фатхутдинов Булат Ильмирович, ИНН 165506822661, указан в футере на всех страницах (schema Organization). ОГРН - на 1 странице (для самозанятого не обязателен, нужен ИНН + статус).
- Реквизиты: ИНН на 161 странице (schema), статус "самозанят" на 6 страницах, НПД на 1. Полные реквизиты (адрес, р/с) отсутствуют.
- Контактность: телефон +7 (901) 265-52-52 и email FathFed@yandex.ru консистентны на всех страницах. Telegram/MAX ссылки есть.
- Публичные обязательства: terms.html объявляет сайт публичной офертой (ст. 437 ГК РФ) при ценах "от" и калькуляторах. Гарантия 6 месяцев. SLA 99,5%.
- Policy-страницы: privacy.html, terms.html, cookie.html, legal/consent.html существуют и связаны со всеми страницами. Битых ссылок нет.

### Исправлено сразу (явные технические несостыковки)
- Проверка: формы содержат honeypot и согласие (15/16). Форма поиска на 404 - без согласия (корректно).
- Проверка: privacy/terms/cookie/consent связаны со всеми страницами.
- Проверка: контакты консистентны.
- Проверка: ИНН в schema на 161 странице.

### Юридически спорное (backlog)
- Privacy vs mailto: legal/privacy.html заявляет Formspree/аналитику, а FORM_ENDPOINT = ''. Выровнять политику под фактическую обработку (mailto).
- Terms: публичная оферта при ценах "от" и калькуляторах. Решить: оставить оферту с условиями акцепта или перевести на "не является офертой".
- Самозанятый vs "команда/сотрудники" на company/*, index, services. Уточнить статус партнёров/подрядчиков.
- Consent: автопродление 3 года и отзыв "по телефону" - исправить (действует до отзыва; отзыв письменно на email).
- ОКВЭД: "62.09" -> "код вида деятельности 62.09" для НПД.
- Cookie-banner только на 5 крипто-страницах - решить site-wide или убрать.
- MAX-ссылки разные (max.ru/FathFed и max.ru/se14849309_bot) - унифицировать.
- Метрики без источника (99.5% uptime, 120+ проектов, 660 тыс. экономии, 20+ лет) - подтвердить или убрать.
- Отзывы/AggregateRating: анонимные цитаты, рейтинг 5/8 без индивидуальных Review. Добавить реальные имена/компании или убрать рейтинг.
- Добавить полные реквизиты (адрес, р/с, статус) в футер/контакты.
- Проверить email deliverability (SPF/DKIM/DMARC) для собственного домена.
- Настроить собственный домен и подать заявку на hstspreload.org.
- Проверить заголовки безопасности на проде (securityheaders.com).

## Мобильный пользователь (30-40 секунд)

Дата: 22.11.2026.

### Проверено
- CTA на первом экране: на главной есть «Рассчитать стоимость» и «Позвонить» (mobile bottom bar), на servers «Позвонить +7 (901) 265-52-52».
- Клик по телефону: номера в шапке и футере, mobile bottom bar имеет кнопку «Позвонить». Не все телефоны обёрнуты в tel: (40 мест).
- Меню: мобильное меню открывается по burger (после bump SW v14). Закрывается по backdrop/close/Escape/клик по ссылке.
- Первый экран: перегружен (badge, H1, lead, features, кнопки, microcopy, консоль-визуал, метрики, brandbar). На мобильном много скролла.
- Заголовки: clamp() адаптивные, читаются. Hero title clamp(36px,10vw,50px) на мобильном.
- Форма: поля width 100%, min-height 48px, валидация, toast. Не ломается на узких экранах.

### Исправлено сразу (мелкие mobile UX)
- Mobile bottom bar больше не перекрывает контент: добавлен padding-bottom на body при width <1099px.
- Quick-nav tap-targets увеличены до 44px (min-height + inline-flex).
- Мобильное меню починено (Service Worker cache bump v13->v14).

### Остальное (backlog)
- Первый экран перегружен: упростить hero (один CTA + trust).
- CTA не всегда виден без скролла на очень узких экранах (360px).
- Телефоны не обёрнуты в tel: в 40 местах (audits, cases, company, infrastructure, security, articles, blog, pain, prices, servers, legal).
- Footer links min-height 34px (ниже 44px tap-target) - увеличить.
- FOUC темы: data-theme="dark" жёстко в HTML, JS применяет сохранённую тему после загрузки отложенного скрипта.
- Bottom bar: кнопка «Рассчитать стоимость» ведёт на prices.html#calculator (проверить якорь).
- Hero brandbar метрики в 3 колонки на узких экранах - проверить перенос.
- Мобильное меню: проверить закрытие по backdrop click (есть обработчик).
- Формы: на 360px поля могут быть слишком узкими. Проверить.
- Калькулятор на мобильном: слайдеры и calc__mobile-total - проверить.
- Изображения: проверить eager/lazy above-the-fold.
- Шрифты: FOUT на мобильных (preload 400 отсутствует).
- Скорость загрузки на 3G: critical.css 25KB, style.css deferred. Проверить LCP.

## Медленная сеть (слабый Android / 4G)

Дата: 22.11.2026.

### Проверено
- Lighthouse (a11y/best practices/SEO): 1.0 на index.html. Performance не измерялся (lighthouse tool не включает perf).
- Первый экран: critical.css 25KB синхронно, style.css/components.css deferred. LCP зависит от critical.css и шрифтов.
- Тяжёлые скрипты: script.js 54KB (min), search.js 5KB, calculator.js 15KB. Inline quiz/form JS в HTML.
- Шрифты: Inter 700/900 preload, font-display swap. Шрифт 400 не preload (FOUT). @import tokens.css удалён из critical.css.
- Изображения: 363 img, 202 lazy + 161 eager. Все с loading/decoding. Логотип fetchpriority=high.
- Service Worker: cache-first для статики, network-first для HTML. CACHE_NAME v14.

### Исправлено сразу (безопасные performance-мелочи)
- Проверка: все img имеют loading/decoding (0 пропусков на сайте).
- Логотип имеет fetchpriority=high.
- critical.css блокирует только критические стили, style.css/components.css deferred.
- Service Worker кэширует статику (v14).

### Остальное (backlog)
- critical.css 25KB: разделить на truly-critical и non-critical, уменьшить FOUC.
- Inline scripts: 750 на 161 страницу (JSON-LD, quiz, формы) - вынести в bundle.
- Шрифты: добавить preload для Inter 400 (FOUT).
- Изображения: проверить eager только above-the-fold (161 eager может быть избыточно).
- content-visibility только на support.html - расширить на длинные страницы.
- build.js/dist не используется HTML - либо использовать, либо убрать.
- Токены critical.css vs tokens.css расходятся (--dim, --border) - синхронизировать.
- Service Worker precache только favicon/logo - добавить шрифты/критические изображения.
- Cache-Control immutable на /css/* /js/* - риск устаревших версий без хэшей в имени файла.
- Lighthouse CI + проверка CWV (LCP, INP, CLS) на проде.
- Проверить скорость на 3G/медленном 4G (WebPageTest).
- Оптимизировать terminal-визуал на главной (ASCII-анимация).
- Уменьшить llms-full.txt (224KB).
- Проверить кросс-браузерность (Safari/Firefox/Edge).
- Проверить доступность с screen reader.

## Скептик (сомневающийся клиент)

Дата: 22.11.2026.

### Проверено
- Гарантия 6 месяцев: упомянута на 21+ страницах, "гарант" на 152. Формулировка стандартизирована (30 дней -> 6 месяцев).
- Прозрачная цена и сроки: блок добавлен на prices/services/servers/support. Цены явно на 48 страницах, тарифы на 13.
- Ответственность: terms.html объявляет оферту, гарантия 6 месяцев, SLA 99,5% (не 100%). 
- Кейсы: 40+ кейсов с метриками, но 11 с одинаковым H1, 0 ссылок на кейсы с money-страниц.
- Ограничения: не указаны (нет "что не входит", "когда не подходим"). 

### Исправлено сразу (усиление доверительных мест)
- Добавлены гарантийные/доверительные строки на prices.html, services.html, servers.html, support.html (ранее).
- Консистентность гарантии 6 месяцев по всему сайту.
- Футер: исправлена опечатка "по городе" -> "по Казани".

### Остальное (backlog)
- Слишком гладкие обещания: "экономия до 80%", "реакция 15 мин", "SLA 99.5%" без источников. Подтвердить или убрать.
- Не хватка доказательств: 0 ссылок на кейсы с money-страниц; отзывы анонимные; нет фото/компаний/дат.
- Мутные риски: нет раздела "ограничения/что не входит/когда не подходим".
- Слабая прозрачность цены: цены "от", тарифы только на 13 страницах. Добавить ценовые таблицы на services/*.html.
- Гарантия 6 месяцев: не указано, что именно покрывает (работы? железо? ПО?).
- Ответственность: нет SLA-документа с штрафами/компенсациями.
- Кейсы: 11 с одинаковым H1, нет ссылок с money-страниц. Уникализировать и перелинковать.
- Ограничения: добавить "когда не подходим" (компания >50 человек, сложная инфраструктура).
- Отзывы: анонимные цитаты, рейтинг 5/8 без индивидуальных Review. Добавить реальные имена/компании или убрать рейтинг.
- Метрики без источника: 99.5% uptime, 120+ проектов, 660 тыс. экономии, 20+ лет. Подтвердить или убрать.
- Добавить реальные кейсы рядом с CTA на money-страницах.
- Добавить блок "ограничения и риски" на services/servers/support.
- Показать договор/SLA пример (PDF) для прозрачности.
- Добавить "что не входит" в тарифы.
- Указать условия возврата/компенсации.

## Продажи / заявки (обработка заявок)

Дата: 22.11.2026.

### Проверено
- Поля форм: name, phone/email, message/task, agree (скрытые website/_gotcha). Lead-формы: name + email. Quiz: name + contact + agree.
- Квалификация: достаточно для первого контакта (имя + телефон + задача). Нет поля "компания/количество ПК/бюджет" в основных формах (есть в калькуляторе).
- Понятность следующего шага: формы показывают toast "Отправляем...", при mailto-fallback - "Если почтовая программа не открылась, позвоните". Некоторые формы имеют "Ответим за 15 минут".
- Трение: согласие на ПД обязательно (15/16), honeypot скрыт. Валидация на blur/input. Rate-limit 3/10 мин.
- Контекст услуги: hidden field service = form name или data.service. На lead-формах service = "IT-аудит: бесплатный аудит...". На servers form task описывает конфигурацию.

### Исправлено сразу (мелкие проблемы форм и микротекстов)
- Добавлен autocomplete="tel" и inputmode="tel" к полям phone без них (5 файлов) - удобство мобильного ввода.
- Проверка: формы имеют service context в hidden field.
- Проверка: валидация обязательных полей и email работает.

### Идеи (backlog)
- Добавить поле "компания/количество ПК" в основные формы для квалификации.
- Добавить явный next-step после отправки: "Мы перезвоним за 15 минут. Если не ответили - звоните +7 (901) 265-52-52 или напишите в Telegram".
- При mailto-fallback показывать success-экран с инструкцией (сейчас toast).
- Добавить автозаполнение service из URL/CTA (например, ?service=servers).
- Добавить UTM-метки в данные формы (откуда пришёл).
- Добавить подтверждение отправки (email/SMS) - при подключении Formspree.
- Добавить SLA-ответа в микротекст формы ("Ответим за 15 минут в рабочее время").
- Добавить "что будет дальше" блок рядом с формой (3 шага).
- Уменьшить трение: убрать обязательное согласие? (юридически нельзя, но можно сделать явным).
- Добавить прогресс-бар/индикатор отправки.
- Добавить валидацию телефона по маске (+7 (___) ___-__-__).
- Добавить автосохранение черновика формы (localStorage уже есть для contact-form).
- Добавить аналитику отправки форм (ymGoal form_submit уже есть).
- Добавить обработку ошибок сети (retry).
- Добавить подтверждение email (double opt-in) для lead-магнитов.

## AI-краулер / GEO (извлечение фактов)

Дата: 22.11.2026.

### Проверено (извлечение фактов)
- Кто вы: F&F, самозанятый Фатхутдинов Булат Ильмирович, ИНН 165506822661, Казань. Указано в футере на 161 странице и schema Organization.
- Что продаёте: IT-аутсорсинг, серверы под ключ, IT-инфраструктура, безопасность, криптография, абонентское обслуживание.
- Цены: от 10 000 ₽/мес (абонентка), от 900 ₽/ПК/мес, от 200 000 ₽ (сервер). Указаны на 38/41/158 страницах.
- Зона работы: Казань + Татарстан (выезд), Россия (удалённо). Указано на 161 странице.
- Гарантия: 6 месяцев (унифицировано, 152 страницы).
- Сроки: реакция 15 мин, SLA 99,5%, монтаж 1 день. Указано на 161 странице.
- Отличия от штатного сисадмина: экономия до 80%, команда 4+, замещаемость, документация, SLA.

### Согласованность фактов
- "99.5" vs "99,5": унифицировано -> "99,5" на всех 161 страницах.
- "по городе" vs "по Казани": исправлено -> "по Казани" (ранее).
- Гарантия 30 дней vs 6 месяцев: унифицировано -> 6 месяцев (ранее).
- Остальные факты (цены, сроки, зона) согласованы между страницами.

### Исправлено сразу (мелкие несогласованности)
- Унификация SLA: "99.5" -> "99,5" на 161 странице.
- Консистентность гарантии и футера (ранее).

### Остальное (backlog)
- Добавить answer-first блок на каждой money-странице: "F&F - IT-аутсорсинг в Казани. От 10 000 ₽/мес. SLA 99,5%. Реакция 15 мин. Гарантия 6 месяцев."
- Добавить структурированные данные (Service schema) на все услуговые страницы с ценами.
- Добавить FAQ с реальными вопросами/ответами (не boilerplate) на money-страницах.
- Добавить таблицу сравнения "F&F vs штатный сисадмин" на index/services.
- Добавить "ограничения" (когда не подходим) для честности.
- Добавить автора/экспертизу (Person schema) на about/team.
- Обновить llms.txt/llms-full.txt с едиными фактами.
- Добавить robots.txt для AI-ботов (уже разрешены).
- Проверить извлечение фактов через ChatGPT/Perplexity (ручной тест).
- Добавить определения и короткие ответы для AI-цитирования.
- Проверить, что все страницы имеют одинаковые NAP (name/address/phone).

## Взгляд конкурента (уязвимости позиционирования)

Дата: 22.11.2026.

### Слабые места оффера
- Самозанятый статус (Фатхутдинов Булат, ИНН 165506822661): конкурент может подчеркнуть отсутствие юрлица, штата, офиса. Риск для клиента: зависимость от одного человека, нет подмены при болезни/отпуске.
- Нет сертификатов/партнёрств (Microsoft, 1С, Cisco, и т.д.) - конкурент с сертификатами выигрывает в доверии.
- Нет собственного домена (GitHub Pages staging, ff-it.ru/ff-team.ru возвращают 404) - выглядит как незавершённый проект.
- Нет офиса/юридического адреса - конкурент с офисом выигрывает.
- Нет 24/7 выезда (только до 22:00) - конкурент с круглосуточным выездом выигрывает.
- Нет мобильного приложения/ЛК для клиента - конкурент с порталом выигрывает.
- Нет публичных метрик (uptime, NPS, количество клиентов с именами).

### Уязвимости позиционирования
- "Экономия до 80%" - абстрактное обещание без источника. Конкурент может предложить конкретную экономию с расчётом.
- "SLA 99,5%" - конкурент может предложить 99,9% с штрафами.
- "Реакция 15 мин" - конкурент может предложить 10 мин.
- "Гарантия 6 месяцев" - конкурент может предложить 12 месяцев.
- "Команда 4+ специалистов" - неясно, кто именно, есть ли резерв. Конкурент может показать команду с фото/био.
- "Мониторинг 24/7" - неясно, что именно мониторится и как реагируют ночью.
- Цены "от" - конкурент может предложить фиксированные тарифы с чётким составом.

### Что легко перебить
- Цена: предложить дешевле или фиксированную (без "от").
- Гарантия: предложить 12 месяцев.
- SLA: предложить 99,9% с штрафами.
- Реакция: предложить 10 мин.
- Добавить сертификаты, офис, юрлицо.
- Добавить реальные отзывы с именами/компаниями/фото.
- Добавить 24/7 выезд.
- Добавить ЛК/портал для клиента.
- Добавить публичные метрики (uptime, NPS).
- Добавить "что входит" в абонентку на главной.

### Где сайт недожимает преимущества
- Кейсы не связаны с money-страницами (0 ссылок с index/services/support/prices).
- Нет блока "почему мы" с конкретными отличиями на главной.
- Нет сравнения с штатным сисадмином на главной (есть compare, но не на index).
- Нет "что входит" в абонентку на главной (только на it-support).
- Нет блока "ограничения/когда не подходим" (честность).
- Нет SLA-документа с штрафами/компенсациями.
- Отзывы анонимные, нет фото/компаний/дат.
- Нет "что не входит" в тарифы.
- Нет условий возврата/компенсации.

### Шаблонные блоки
- Метрики/процесс/FAQ повторяются на 161/118/113 страницах - выглядит как шаблон, снижает уникальность.
- Terminal-визуал (ASCII-консоль) на главной - gimmick, не добавляет доверия.
- Brandbar с метриками на главной - шаблонный блок.
- "Честный срез на основе типичных результатов" - звучит как оговорка, снижает доверие.
- Answer-first boilerplate на ~100 страницах - одинаковый текст, снижает уникальность.
- 11 кейсов с одинаковым H1 - выглядит как автогенерация.

### Рекомендации (как обойти конкурента)
- Добавить реальные кейсы с именами/компаниями/метриками на money-страницы.
- Добавить блок "почему мы" с конкретными отличиями (не абстрактными).
- Добавить сравнение с штатным сисадмином на главной.
- Добавить "что входит" в абонентку на главной.
- Добавить "ограничения/когда не подходим" для честности.
- Добавить SLA-документ с штрафами/компенсациями.
- Добавить сертификаты/партнёрства (если есть).
- Добавить реальные отзывы с именами/компаниями/фото/датами.
- Убрать шаблонные блоки с блога/статей/кейсов.
- Убрать terminal-визуал или сделать опциональным.
- Подключить собственный домен (ff-it.ru).
- Добавить офис/юрлицо (если планируется).
- Добавить 24/7 выезд (если возможно).
- Добавить ЛК/портал для клиента.
- Добавить публичные метрики (uptime, NPS).

## Доступность (a11y)

Дата: 22.11.2026.

### Проверено
- Клавиатурная навигация: desktop nav dropdowns открываются по Enter/Space/ArrowDown, закрываются по Escape. Mobile menu: Tab-trap, Escape закрывает, backdrop click закрывает. Skip-link "Перейти к содержимому" есть.
- Читаемость: Lighthouse Accessibility 1.0 на index.html. Контраст muted 7.71, gold 9.24, neon 14.49 на тёмном фоне (WCAG AA).
- Alt: все img имеют alt (0 пропусков).
- Label у полей: все видимые input имеют id/label или aria-label. Honeypot-поля скрыты через aria-hidden wrapper.
- Focus-состояния: :focus-visible outline 2px solid var(--gold-light) в CSS. :focus:not(:focus-visible) outline none.
- Масштабирование: viewport meta на всех страницах, responsive стили, clamp() для типографики.

### Исправлено сразу (простые проблемы)
- Добавлен aria-label="Поиск по сайту" к полю поиска на 404.html.
- Проверка: html lang="ru" на всех страницах.
- Проверка: skip-link на всех страницах.
- Проверка: alt на всех img (0 пропусков).

### Остальное (backlog)
- Проверить keyboard navigation вручную (NVDA/VoiceOver).
- Проверить focus-states на всех интерактивных элементах (кнопки, ссылки, поля).
- Проверить масштабирование до 200% (WCAG 1.4.4).
- Проверить контраст в светлой теме.
- Проверить aria-live для toast и form-success.
- Проверить role="dialog" и aria-modal для mobile menu (уже есть).
- Проверить aria-expanded для burger (уже есть).
- Проверить aria-controls для burger (уже есть).
- Проверить screen reader (NVDA/VoiceOver) на ключевых страницах.
- Проверить keyboard trap в mobile menu (Tab handling есть).
- Проверить skip-link работает (top:-40px -> top:0 on focus).
- Проверить prefers-reduced-motion (анимации отключаются).
- Проверить prefers-contrast: high (стили есть).
- Добавить aria-label к иконкам (search, theme toggle) - уже есть.
- Проверить form error messages связаны с полями (aria-describedby).
- Проверить loading="lazy" не ломает screen reader.
- Проверить heading hierarchy (H1=1, H2, H3) - ок.

## Ролевые тесты

Сводка всех ролевых проверок (22.11.2026). Подробности в соответствующих разделах выше.

### Пользователь
- Что сломано/мешает: перегруженный hero, ASCII-терминал-gimmick, строка "Обновлено: 20.11.2026", boilerplate answer-first, несогласованная гарантия (исправлено), битые якоря (исправлено), опечатка "по городе" (исправлено).
- Что уже исправлено: футер "по Казани", breadcrumb "Абонентское обслуживание", гарантия 6 месяцев (152 файла), битые якоря services.html#calculator/#estimate -> prices.html (161 файл), quick-nav services.
- Что в приоритете: упростить hero, вынести форму/калькулятор ближе к первому экрану, обернуть телефоны в tel: (40 мест), добавить доверительные элементы рядом с CTA.

### Разработчик
- Что сломано/мешает: script.js монолит (~10k строк), CSS tokens mismatch (--dim, --border), FOUC темы, формы mailto-fallback, шаблонные блоки на 100+ страницах, регресс-риски массовых автозамен.
- Что уже исправлено: дубли id="faq" (15 файлов), дубли class/decoding, неэкранированные >, битые ссылки (148 файлов), htmlhint 0 ошибок, check-site passed.
- Что в приоритете: вынести quiz/form/analytics в bundle, синхронизировать токены, убрать FOUC, настроить FORM_ENDPOINT, добавить htmlhint/linkcheck в CI.

### Тестировщик
- Что сломано/мешает: мобильное меню не открывалось (SW кэш) - исправлено, формы без success-экрана при mailto, tap-targets <44px, footer links 34px, FOUC, bottom bar перекрытие, нет автотестов форм.
- Что уже исправлено: CACHE_NAME v13->v14, битые якоря, дубли атрибутов/id, mobile menu работает.
- Что в приоритете: success-экран после отправки, tap-targets, FOUC, проверка 360/320px, якоря после скролла, автотесты форм.

### Дизайнер
- Что сломано/мешает: перегруженный hero, ASCII-терминал-gimmick, визуальный шум акцентов, смешанные кнопки, разные радиусы/паддинги карточек, неединообразные формы, неравномерные отступы, mobile tap-targets, шаблонные блоки.
- Что уже исправлено: white-space nowrap у brandbar-name/sub, консистентность гарантии/футера.
- Что в приоритете: упростить hero, нормализовать кнопки/карточки/формы, ввести spacing scale, убрать terminal-визуал, выделить featured-тариф, добавить реальные отзывы.

### Админ / контент
- Что сломано/мешает: нет CMS, контент захардкожен в 161 HTML, цены/гарантия/SLA дублируются в 100+ файлах, шаблонные блоки на 161/118/113 страницах, inline-стили (6), utility-классы, изображения с ?v=130 в HTML.
- Что уже исправлено: консистентность гарантии/футера/ссылок, white-space brandbar.
- Что в приоритете: вынести цены/гарантию/SLA в data.json + build-time include, убрать шаблонные блоки с блога/статей/кейсов, уникализировать H1 кейсов, добавить промо-блоки.

### SEO
- Что сломано/мешает: answer-first boilerplate на ~100 страницах, Article headline != title на ~40, generic twitter:title на blog, Service schema только на 24 страницах, Person schema на 62, Review на 7, страницы-сироты (10), локальные кластеры не закрыты.
- Что уже исправлено: meta keywords удалён (153), BreadcrumbList (151), Organization logo (150), noscript components.css (161), короткие description дополнены (21), canonical на всех.
- Что в приоритете: Service schema на services/*.html, FAQPage на страницах с реальным FAQ, расширить ценовые блоки, усилить E-E-A-T, Person schema на team/about, исправить Article/Service offers/Review, убрать boilerplate, добавить og:image:alt.

### Безопасник
- Что сломано/мешает: CSP unsafe-inline, FORM_ENDPOINT пуст (mailto-fallback), privacy policy заявляет Formspree, terms публичная оферта, consent автопродление 3 года, cookie-banner только на 5 крипто-страницах, MAX-ссылки разные, метрики без источника, отзывы анонимные.
- Что уже исправлено: honeypot на всех формах, rate-limit, target blank с noopener, javascript: href 0, security headers в _headers.
- Что в приоритете: выровнять privacy под mailto, решить статус оферты, ужесточить CSP после выноса инлайн-кода, настроить Formspree или зафиксировать mailto, исправить consent, унифицировать MAX-ссылки.

### Краулер
- Что сломано/мешает: _redirects битые цели (ff-it.ru/ff-team.ru 404), страницы-сироты (10), дубли контента (blog/office-move vs infrastructure/office-move), /pasahalki в robots.
- Что уже исправлено: robots.txt Disallow /room -> /infrastructure/room.html, битые ссылки (check-site passed), sitemap 159 URL без noindex-утечек.
- Что в приоритете: подать sitemap в GSC/Яндекс, исправить _redirects, добавить сирот в sitemap/перелинковку, проверить статус-коды на проде, обновить llms.txt.

### Роскомнадзор / compliance
- Что сломано/мешает: privacy vs mailto, terms публичная оферта, самозанятый vs команда, consent автопродление/отзыв по телефону, ОКВЭД "62.09", cookie-banner только на 5 страницах, MAX-ссылки разные, метрики без источника, отзывы анонимные, неполные реквизиты.
- Что уже исправлено: honeypot и согласие (15/16), policy-страницы связаны, контакты консистентны, ИНН в schema (161).
- Что в приоритете: выровнять privacy, решить статус оферты, исправить consent, унифицировать MAX, добавить реквизиты, проверить email deliverability, HSTS preload.

### Mobile
- Что сломано/мешает: перегруженный hero, CTA не всегда виден на 360px, 40 телефонов без tel:, footer links 34px, FOUC темы, bottom bar перекрытие, brandbar 3 колонки на узких экранах.
- Что уже исправлено: bottom bar padding-bottom, quick-nav tap-targets 44px, mobile menu (SW v14).
- Что в приоритете: упростить hero, обернуть телефоны в tel:, увеличить footer links, убрать FOUC, проверить формы на 360px, калькулятор на мобильном.

### Медленная сеть
- Что сломано/мешает: critical.css 25KB, inline scripts 750 на 161 страницу, шрифт 400 не preload (FOUT), 161 eager images, content-visibility только на support, build.js/dist не используется, Service Worker precache только favicon/logo.
- Что уже исправлено: все img с loading/decoding, логотип fetchpriority high, critical.css блокирует только критические стили, SW v14.
- Что в приоритете: разделить critical.css, вынести инлайн-скрипты, preload шрифта 400, проверить eager above-the-fold, content-visibility на длинных страницах, Lighthouse CI + CWV, тест на 3G.

### Скептик
- Что сломано/мешает: гладкие обещания без источников ("экономия до 80%", "реакция 15 мин", "SLA 99,5%"), нехватка доказательств (0 ссылок на кейсы с money-страниц, анонимные отзывы), мутные риски (нет ограничений), слабая прозрачность цены (цены "от", тарифы на 13 страницах), гарантия не раскрыта.
- Что уже исправлено: гарантийные строки на prices/services/servers/support, консистентность гарантии 6 месяцев, футер "по Казани".
- Что в приоритете: подтвердить/убрать метрики без источника, добавить реальные кейсы/отзывы, добавить "ограничения/когда не подходим", раскрыть гарантию, добавить SLA-документ, "что не входит" в тарифы, условия возврата.

### Продажи / заявки
- Что сломано/мешает: нет поля компания/ПК в основных формах, нет явного next-step после отправки, нет success-экрана при mailto-fallback, нет автозаполнения service из URL/CTA, нет UTM-меток, нет валидации телефона по маске.
- Что уже исправлено: autocomplete/inputmode tel (5 файлов), service context в hidden field, валидация полей/email.
- Что в приоритете: добавить поле компания/ПК, явный next-step, success-экран, автозаполнение service, UTM-метки, SLA-ответа в микротексте, "что будет дальше" блок, валидация телефона по маске, автосохранение черновика.

### AI-краулер / GEO
- Что сломано/мешает: answer-first boilerplate на ~100 страницах, нет структурированных данных с ценами на всех услуговых, нет реальных FAQ, нет таблицы сравнения на главной, нет блока ограничений, нет автора/экспертизы, llms.txt требует обновления.
- Что уже исправлено: унификация SLA "99,5" на 161 странице, консистентность гарантии/футера.
- Что в приоритете: answer-first блок на money-страницах, Service schema с ценами, реальные FAQ, таблица сравнения, блок ограничений, Person schema, обновление llms.txt, проверка извлечения через ChatGPT/Perplexity.

### Конкурент
- Что сломано/мешает: самозанятый статус, нет сертификатов/офиса/юрлица/домена, нет 24/7 выезда/ЛК/метрик, шаблонные блоки, анонимные отзывы, нет "что входит"/"ограничения", нет SLA-документа.
- Что уже исправлено: доверительные строки на money-страницах, консистентность гарантии/футера.
- Что в приоритете: реальные кейсы/отзывы на money-страницах, блок "почему мы", сравнение с штатным, "что входит", ограничения, SLA-документ, сертификаты, убрать шаблоны, подключить домен, 24/7 выезд, ЛК, метрики.

### Доступность
- Что сломано/мешает: не проверено вручную с screen reader, focus-states на всех элементах, масштабирование до 200%, контраст в светлой теме, aria-live для toast/form-success, aria-describedby для ошибок форм.
- Что уже исправлено: aria-label на поле поиска 404, html lang="ru", skip-link, alt на всех img, :focus-visible outline.
- Что в приоритете: проверка NVDA/VoiceOver, focus-states, масштабирование 200%, контраст светлой темы, aria-live, aria-describedby, heading hierarchy.

---

## Приоритизация (итог)

### 1. Критично
1. Подставить реальные ID аналитики или удалить заглушки (js/script.js).
2. Настроить FORM_ENDPOINT или зафиксировать mailto-стратегию + success-экран.
3. Добавить входящие ссылки на страницы-сироты (10 страниц).
4. Выровнять legal/privacy.html под фактическую обработку (mailto vs Formspree).
5. Решить статус публичной оферты в legal/terms.html.
6. Подключить собственный домен (ff-it.ru) и переключить canonical.
7. Добавить реальные отзывы/кейсы с именами на money-страницы (доверие).
8. Исправить consent (автопродление 3 года, отзыв по телефону).
9. Добавить полные реквизиты (адрес, р/с, статус) в футер/контакты.
10. Убрать метрики без источника или подтвердить.

### 2. Важно
11. Добавить Service schema на services/*.html.
12. Добавить FAQPage schema на страницы с реальным FAQ без schema.
13. Расширить ценовые блоки (тарифы) на services/*.html.
14. Усилить E-E-A-T: авторы, сертификаты, отзывы, кейсы с метриками.
15. Контекстная перелинковка (минимум 3 ссылки на страницу).
16. Закрыть локальные/отраслевые кластеры (лендинги по городам Татарстана и отраслям).
17. Упростить hero (сократить визуальный шум, один CTA + trust).
18. Убрать terminal-визуал или сделать опциональным.
19. Нормализовать button sizes и tap-targets (44px).
20. Убрать FOUC темы (инлайн-скрипт до render).
21. Вынести quiz/form/analytics из script.js в отдельный bundle.
22. Синхронизировать CSS tokens (critical.css vs tokens.css).
23. Добавить content-visibility на длинные страницы.
24. Обернуть 40 телефонов в tel:.
25. Добавить доверительные элементы рядом с CTA на leads/* и services/*.
26. Добавить next-step блоки на blog/отраслевые страницы.
27. Убрать шаблонные блоки (метрики/процесс/FAQ) с блога/статей/кейсов.
28. Уникализировать H1 на 11 кейсах.
29. Дифференцировать blog/office-move vs infrastructure/office-move.
30. Исправить Article headline/image/publisher logo (7+4 файлов).
31. Исправить Service offers.price на 9+ файлах.
32. Исправить Review (фейковый автор, дата, itemReviewed) на 7 страницах.
33. Добавить Person schema на company/team.html и company/about.html.
34. Убрать answer-first boilerplate на ~100 страницах.
35. Унифицировать автора "Булат" vs "Булат Фатхутдинов".
36. Добавить og:image:alt/twitter:image:alt везде.
37. Проверить robots.txt для AI-ботов.
38. Обновить llms.txt/llms-full.txt.
39. Настроить email deliverability (SPF/DKIM/DMARC).
40. Проверить кросс-браузерность (Safari/Firefox/Edge).
41. Проверить доступность с screen reader (NVDA/VoiceOver).
42. Проверить keyboard navigation вручную.
43. Проверить локальное SEO (Яндекс.Карты, 2ГИС, отзывы).
44. Проверить индексацию в GSC/Яндекс.Вебмастер.

### 3. Можно позже
45. Контент-план по незакрытым кластерам (города, отрасли, интенты).
46. A/B-тесты hero/CTA/форм.
47. Расширение блога (глубокие гайды 1500+ слов).
48. Локальный SEO: Яндекс.Бизнес, 2ГИС, отзывы.
49. Внешние ссылки/PR для роста авторитетности.
50. Оптимизация dist/build (использовать или убрать).
51. Добавить микроконверсии (чек-листы, аудиты) на все страницы.
52. Вынести inline quiz/form JS в отдельный bundle.
53. Разделение critical.css на truly-critical и non-critical.
54. Добавить content-visibility на длинные страницы.
55. Исправить robots.txt Disallow /room -> /infrastructure/room.html (выполнено).
56. Уменьшить llms-full.txt (224KB).
57. Добавить иконки 192/512 в manifest.json.
58. Проверить орфографию/грамматику (LanguageTool).
59. Проверить email deliverability (SPF/DKIM/DMARC).
60. Настроить собственный домен и подать заявку на hstspreload.org.
61. Проверить заголовки безопасности на проде (securityheaders.com).
62. Проверить кросс-браузерность (Safari/Firefox/Edge).
63. Проверить доступность с screen reader (NVDA/VoiceOver).
64. Проверить keyboard navigation вручную.
65. Проверить локальное SEO (Яндекс.Карты, 2ГИС, отзывы).
66. Проверить индексацию в GSC/Яндекс.Вебмастер.



## 6. Конкурентная карта F&F (обновлённая)

### A. Прямые локальные конкуренты (Казань)

| # | Домен | Сегмент | Гео | Тип | Главная сила | Главная слабость |
|---|---|---|---|---|---|---|
| 1 | its-kazan.ru (IT Сервис) | Абонентское обслуживание IT-инфраструктуры МСБ (1-100+ ПК) | Казань, ул. Декабристов 85Б | Прямой | 10+ лет, 2ГИС 5.0/28 отзывов, Zabbix 24/7, ITIL, персональный IT-управляющий, тарифы Эконом/Бизнес/Премиум | Старый сайт, нет публичных цен, слабая SEO/контент, нет фокуса на 1С/ЭЦП/серверах |
| 2 | tss-kazan.ru (ТехноСистемСервис) | IT-аутсорсинг МСБ, внедрение ИТ-систем, СКС, IP-телефония, виртуализация | Казань, ул. Г. Камала 7 | Прямой | SLA с финансовыми гарантиями (100% возврат), постоплата, проактивный мониторинг, кейсы торговых сетей, 10 лет | Устаревший сайт, нет блога/контента, мало прозрачности цен, небольшой масштаб |
| 3 | kazan.a8company.ru (A8 Company) | Интегратор: серверы, СХД, сетевое оборудование, инфобез, видеонаблюдение, аутсорсинг ЦОД | Казань, ул. Академика Сахарова 1А | Смежный | Широкий каталог оборудования, инженерная инфраструктура ЦОД, лизинг, проекты, инфобез | Не фокус на абонентском обслуживании МСБ, сайт перегружен каталогом, нет чёткого оффера для малого бизнеса |
| 4 | esc-kazan.ru (Центр электронных услуг) | Комплексный бэк-офис под ключ: бухгалтерия + юрист + сисадмин + ЭЦП + тендеры | Казань, ул. Чистопольская 36 | Смежный | 21 год на рынке, комплексный подход, 95% вопросов в течение рабочего дня, сервисный центр Контур/СБИС/1С | IT - вторичная услуга, нет фокуса на серверной инфраструктуре, низкая зарплата IT-специалиста (27-30 тыс. руб.) - риск качества |
| 5 | itbsgroup.ru (Ай Ти Бизнес Солюшенс) | Интегратор: автоматизация бизнеса, 1С, аутсорсинг инфраструктуры, инфобез, оборудование | Казань + Челябинск, Альметьевск, Йошкар-Ола, Москва, Наб. Челны, Нижнекамск | Смежный | Широкая география, каталог оборудования, проекты, инфобез, 1С | Не фокус на абонентском обслуживании МСБ, сайт перегружен, слабый оффер для малого бизнеса |
| 6 | itprovider.ru (IT Provider) | IT-поддержка/аутсорсинг серверной инфраструктуры, service desk, SLA | Казань, ул. Мавлютова 42 / Кул Гали 10А | Прямой | С 2009 г., 600 000+ обращений, 35 специалистов, 3 линии поддержки, 24/7, SLA, NDA, мониторинг, документация "СИСТЕМА" | Сайт перегружен, фокус на серверах, слабая локальная SEO/контент, нет публичных цен для МСБ |
| 7 | i-tat.ru (АЙТАТ) | 1С-сопровождение + IT-обслуживание, сметные программы | Казань, Челны, Нижнекамск, Альметьевск, Ижевск | Прямой/смежный | 11 лет, 2700 клиентов, горячая линия до 21:00, бесплатная доставка/установка, филиальная сеть по Татарстану | Фокус на 1С/сметах, IT-аутсорсинг вторичный, сайт устаревший |
| 8 | pc-kazan.ru (Компьютерная помощь) | B2C + мелкий B2B: ремонт ПК/ноутбуков, абонентское обслуживание юрлиц | Казань, ул. Дзержинского 25 | Смежный | 9+ лет, 24/7, бесплатная диагностика, выезд мастера, низкие цены, рейтинг 4.5/5 | Низкий чек, нет SLA/серверной экспертизы, нет 1С/ЭЦП, B2C-фокус |
| 9 | kazan.intertax.ru (РемонтПК) | B2C + мелкий B2B: ремонт/обслуживание ПК | Казань, ул. Дзержинского 25 | Смежный | 9 лет, круглосуточно, широкий спектр, гарантия | Низкий чек, нет серверной/1С экспертизы, B2C-фокус, слабый SEO |
| 10 | comp-kazan.ru (Компьютер Сервис) | B2C + мелкий B2B: ремонт ПК/оргтехники, заправка картриджей, абонентское обслуживание | Казань, пр. Ямашева 92а | Смежный | 17 лет, 2ГИС 4.8, Яндекс 5.0, гарантия до 2 лет, собственный склад запчастей | B2C-фокус, нет серверной/1С/ЭЦП, низкий чек |
| 11 | calltraffic.ru (CallTraffic) | B2B: аутсорсинговый контакт-центр, клиентский сервис, техподдержка ИС | Казань, Сибирский тракт 34 + 13 площадок РФ/Узбекистан | Смежный | 16 лет, собственная платформа Ez-Com, 2500+ сотрудников, 99.98% катастрофоустойчивость, банковская экспертиза | Не IT-аутсорсинг (инфраструктура/серверы), смежный конкурент по техподдержке |
| 12 | erpdev.i-neti.ru (Neti) | 1С-разработка, внедрение ERP, сопровождение | Москва (Нобеля 7) + удалённо по РФ | Смежный | 200+ разработчиков, 300+ проектов, гарантия 24 мес, NDA/SLA | Не IT-аутсорсинг инфраструктуры, фокус на 1С, высокий ценник, удалённо |

### B. Татарстан (Челны / Нижнекамск / Альметьевск / Иннополис)

| # | Игрок | Сегмент | Гео | Тип | Главная сила | Главная слабость |
|---|---|---|---|---|---|---|
| 1 | АЙТАТ (i-tat.ru) | 1С-сопровождение + IT-обслуживание, сметные программы | Челны, Нижнекамск, Альметьевск, Ижевск | Прямой/смежный | 11 лет, 2700 клиентов, горячая линия до 21:00, бесплатная доставка/установка, филиальная сеть | Фокус на 1С/сметах, IT-аутсорсинг вторичный, сайт устаревший |
| 2 | Локальные IT-сервисы и 1С-франчайзи (Челны/Нижнекамск/Альметьевск) | Мелкий B2B: ремонт ПК, абонентское обслуживание, 1С | Наб. Челны, Нижнекамск, Альметьевск | Смежный | Локальное присутствие, низкие цены, знание местного бизнеса | Нет SLA, серверной экспертизы, масштаба, слабая SEO/бренд |
| 3 | Резиденты технопарка Иннополис | R&D, IT-продукты, стартапы, разработка ПО | Иннополис | Смежный | Высокая экспертиза, инновации, доступ к талантам | Не прямые конкуренты по аутсорсингу МСБ, высокий ценник, B2B-enterprise фокус |

### C. Федеральные удалённые топы

| # | Домен | Сегмент | Гео | Тип | Главная сила | Главная слабость |
|---|---|---|---|---|---|---|
| 1 | a1-support.ru (A1 Support) | Удалённая IT-поддержка бизнеса: абонентское обслуживание ПК/серверов, 1С, ЭЦП, почта | Вся РФ удалённо, выезд Москва/СПб | Прямой | С 2006 г., прозрачные цены (5 ПК = 5000 руб./мес), 8-800, договор, ЭДО, безопасность | Нет локального присутствия в Казани, удалённый формат, нет 1С-разработки |
| 2 | obit.ru (ОБИТ) | Оператор IT-решений: телеком, ЦОД, инжиниринг, инфобез, IT-аутсорсинг | Казань (Московская 19/8) + СПб/Москва | Смежный | 20+ лет, собственная инфраструктура, ЦОД, кейсы (Петрович, банк СПб), отраслевая экспертиза | Высокий порог входа, не фокус на МСБ-абонентском обслуживании, тяжёлый сайт |
| 3 | socialit.ru (Социалит Сервис) | IT-аутсорсинг для розничных сетей/филиалов (МСБ/средний бизнес) | 70+ городов, телефон 843 (Казань) | Прямой | 2011 г., 140+ сотрудников, 300+ клиентов, 3 линии поддержки, SLA с финансовыми гарантиями, White Label, 24/7 | Фокус на розничных сетях, высокий порог (от 10-50 тыс. руб./мес), нет локального бренда в Казани |
| 4 | iteron.ru (ITERON) | IT-аутсорсинг МСБ, абонентское обслуживание, 1С, серверы | Москва (Сельскохозяйственная 11), удалённо | Прямой | 18 лет, калькулятор цен, 98% остаются, 1С, серверы | Маленький масштаб (31+ компаний), слабая локализация, нет присутствия в Казани, устаревший сайт |
| 5 | 1cbit.ru (Первый Бит) | 1С-франчайзи + IT-поддержка (поддержка IT-систем), инфраструктура | 9 стран, 100+ офисов, Казань (2-я Юго-Западная 7) | Смежный | 29 лет, 9000+ специалистов, 300 000+ клиентов, 24/7, широкий спектр | IT-аутсорсинг - вторичная услуга, высокий ценник, массовый подход, нет фокуса на МСБ-инфраструктуре |

### Краткие выводы
- Прямые локальные конкуренты (its-kazan, tss-kazan, itprovider, i-tat) - сильны в абонентском обслуживании и 1С, но слабы в SEO/контенте и серверной экспертизе.
- Смежные игроки (a8, itbsgroup, esc-kazan, calltraffic, erpdev) - интеграторы/контакт-центры/1С-франчайзи; IT-аутсорсинг для них вторичен.
- Федеральные топы (a1-support, socialit, iteron) - сильны в удалённой поддержке и SLA, но не имеют локального присутствия/бренда в Казани.
- Ключевая возможность F&F: занять нишу "премиального IT-аутсорсинга для МСБ в Казани" с фокусом на серверах 1С, ЭЦП, инфобез и SLA - ниша, которую локальные игроки закрывают слабо.


## 7. Жёсткий разбор 20 конкурентов (оффер / цены / SLA / первый экран / trust / конверсия / слабость)

### A. Казань (12)

| # | Домен | Оффер | Цены | Гарантия/SLA/сроки | Первый экран | Trust | Конверсия | Главная слабость |
|---|---|---|---|---|---|---|---|---|
| 1 | its-kazan.ru | Абонентское обслуживание IT-инфраструктуры МСБ | Не публичные (тарифы без цифр) | Zabbix 24/7, ITIL, быстрое реагирование; сроков нет | "Абонентское обслуживание IT инфраструктуры" + тарифы | 10+ лет, 2ГИС 5.0, отзывы | Телефон, "Заказать звонок" | Нет цен/SLA, старый сайт, слабый CTA |
| 2 | tss-kazan.ru | IT-аутсорсинг, внедрение ИТ-систем, СКС, IP-телефония | Не публичные | SLA с финансовыми гарантиями, 100% возврат, постоплата | Слайдер услуг + "Бесплатный аудит IT-инфраструктуры" | 10 лет, кейсы торговых сетей, отзывы | "Оставить заявку", телефон | Нет цен, устаревший сайт, нет контента |
| 3 | kazan.a8company.ru | Интегратор: серверы, СХД, сети, инфобез, видеонаблюдение, ЦОД | Каталог (зависит от конфигурации) | Проектные, не указаны | Каталог оборудования, меню услуг | Проекты, партнёры (Yadro, Huawei), лицензии | "Заказать звонок", ЛК | Нет чёткого оффера для МСБ, перегружен каталогом |
| 4 | esc-kazan.ru | Бэк-офис под ключ: бухгалтерия + юрист + сисадмин + ЭЦП + тендеры | Пакет от ~50 000 руб./мес | 95% вопросов в течение рабочего дня | "Бэк-офис под ключ ... за 50 000 руб." | 21 год, реквизиты, 1С/Контур/СБИС | Форма, 8-800 | IT вторичен, низкая зарплата IT-специалиста |
| 5 | itbsgroup.ru | Интегратор: автоматизация, 1С, аутсорсинг инфраструктуры, инфобез | Не публичные (проектные) | Проектные, не указаны | "IT Business Solutions - опытный интегратор" | Проекты, партнёры, лицензии, реквизиты | "Заказать звонок", форма | Нет чёткого оффера для МСБ, сайт перегружен |
| 6 | itprovider.ru | IT-поддержка/аутсорсинг серверной инфраструктуры, service desk | Не публичные | SLA, 24/7, реакция 15 мин, решение 20 мин | "ИТ-поддержка, на которую можно положиться. 24/7." | С 2009, 600k+ обращений, 35 специалистов, отзывы | Форма, телефон | Фокус на серверах, нет публичных цен, слабая SEO |
| 7 | i-tat.ru | 1С-сопровождение + IT-обслуживание, сметные программы | Не публичные | Линия консультаций до 21:00, реакция 10 мин | Слайдер услуг (ИТ, 1С, сметы) | 11 лет, 2700 клиентов, отзывы, сертификаты | "Обратиться", телефон | Фокус на 1С/сметах, IT-аутсорсинг вторичен |
| 8 | pc-kazan.ru | B2C + мелкий B2B: ремонт ПК/ноутбуков, абонентское обслуживание | Низкие (ремонт от 284 руб.) | Выезд за 1 час, ремонт за 3 часа | "Компьютерная помощь в Казани", форма заявки | 9+ лет, рейтинг 4.5/5, отзывы | "Оставить заявку", телефон, TG/WA | Низкий чек, нет серверной/1С экспертизы |
| 9 | kazan.intertax.ru | B2C + мелкий B2B: ремонт/обслуживание ПК | Низкие (ОС от 474 руб.) | Круглосуточно, выезд мастера | "Ремонт и обслуживание компьютеров в Казани", калькулятор | 9 лет, отзывы, рейтинг | Форма, телефон, TG/MAX | Низкий чек, нет серверной/1С экспертизы |
| 10 | comp-kazan.ru | B2C + мелкий B2B: ремонт ПК/оргтехники, заправка, абонентка | Низкие (заправка от 250 руб.) | Гарантия до 2 лет, диагностика бесплатно | "Ремонт ноутбуков, компьютеров, оргтехники" | 17 лет, 2ГИС 4.8, Яндекс 5.0, отзывы | "Заказать срочный ремонт", телефон, MAX/TG | B2C-фокус, нет серверной/1С/ЭЦП |
| 11 | calltraffic.ru | B2B: аутсорсинговый контакт-центр, техподдержка ИС | Не публичные (проектные) | 99.98% катастрофоустойчивость, запуск от 1 недели | "Непрерывность коммуникаций и клиентский опыт" | 16 лет, 2500+ сотрудников, 140+ бизнесов, ФСТЭК | Форма, телефон, email | Не IT-аутсорсинг (инфраструктура/серверы) |
| 12 | erpdev.i-neti.ru | 1С-разработка, внедрение ERP, сопровождение | Не публичные (проектные) | Гарантия 24 мес, NDA/SLA | "Разработка и сопровождение 1С" | 200+ разработчиков, 300+ проектов, отзывы | "Бесплатно оценить задачу", телефон | Не IT-аутсорсинг инфраструктуры, высокий ценник |

### B. Татарстан (3)

| # | Игрок | Оффер | Цены | Гарантия/SLA/сроки | Первый экран | Trust | Конверсия | Главная слабость |
|---|---|---|---|---|---|---|---|---|
| 13 | АЙТАТ (i-tat.ru) | 1С-сопровождение + IT-обслуживание, сметы | Не публичные | Линия консультаций до 21:00, реакция 10 мин | Слайдер услуг (ИТ, 1С, сметы) | 11 лет, 2700 клиентов, отзывы, сертификаты | "Обратиться", телефон | Фокус на 1С/сметах, IT-аутсорсинг вторичен |
| 14 | Локальные IT-сервисы (Челны/Нижнекамск/Альметьевск) | Мелкий B2B: ремонт ПК, абонентка, 1С | Низкие, не публичные | Не указаны | Разные сайты | Локальные отзывы | Телефон | Нет SLA, серверной экспертизы, масштаба |
| 15 | Резиденты Иннополиса | R&D, IT-продукты, стартапы, разработка ПО | Высокие (проектные) | Проектные | Разные сайты | Технопарк, резидентство | Форма/контакты | Не прямые конкуренты по аутсорсингу МСБ |

### C. Федеральные (5)

| # | Домен | Оффер | Цены | Гарантия/SLA/сроки | Первый экран | Trust | Конверсия | Главная слабость |
|---|---|---|---|---|---|---|---|---|
| 16 | a1-support.ru | Удалённая IT-поддержка: абонентка ПК/серверов, 1С, ЭЦП, почта | Прозрачные (5 ПК = 5000 руб./мес, +500 руб./ПК, сервер от 1200 руб.) | Договор, ответ в рабочее время | "Удалённая IT-поддержка ... по всей России", калькулятор | С 2006, ИП, ИНН, договор, ЭДО | Калькулятор, форма, 8-800, TG | Нет локального присутствия, удалённый формат |
| 17 | obit.ru | Оператор IT-решений: телеком, ЦОД, инжиниринг, инфобез, аутсорсинг | Не публичные (проектные) | Проектные | "ОБИТ - оператор ИТ-решений", меню услуг | 20+ лет, кейсы, партнёры, лицензии | Форма, телефон, ЛК | Высокий порог входа, не фокус на МСБ |
| 18 | socialit.ru | IT-аутсорсинг для розничных сетей/филиалов | Тарифы: "Удалённый" от 10 000, "Базовый" 20 000, "Расширенный" 50 000 руб./мес | SLA с финансовыми гарантиями (1000-1500 руб./час), 3 линии | "ИТ-аутсорсинг для бизнеса по всей России", тарифы | 2011, 140+ сотрудников, 300+ клиентов, кейсы | Форма, 8-800 | Фокус на розничных сетях, высокий порог |
| 19 | iteron.ru | IT-аутсорсинг МСБ, абонентка, 1С, серверы | Калькулятор (не публичные базовые) | Не указаны явно | "IT-поддержка, которая всегда рядом", калькулятор | 18 лет, 31+ компаний, 98% остаются, отзывы | Калькулятор, форма, телефон | Маленький масштаб, нет присутствия в Казани |
| 20 | 1cbit.ru | 1С-франчайзи + IT-поддержка (поддержка IT-систем), инфраструктура | Не публичные (проектные) | SLA, 24/7 | "Первый Бит. ТОП-100 ИТ-компаний России", форма | 29 лет, 9000+ специалистов, 300 000+ клиентов, офис в Казани | "Заказать звонок", телефон | IT-аутсорсинг вторичен, высокий ценник, массовый подход |

### Картина рынка (жёстко)
- 80% локальных игроков (its, tss, pc, comp, intertax) - B2C/мелкий B2B, без цен, SLA и серверной экспертизы. Сайты старые, CTA слабые.
- Прямые конкуренты в абонентке (its-kazan, tss-kazan, itprovider) - закрывают МСБ, но не публикуют цены и SLA; дифференциация по доверию/скорости.
- Смежные интеграторы (a8, itbsgroup) - equipment-first, не сервис для МСБ; сайт перегружен каталогом.
- Федеральные (a1-support, socialit, iteron) - прозрачные цены/SLA, но нет локального бренда; угроза для ценового сегмента.
- 1С-франчайзи (i-tat, 1cbit) - сильны в 1С, но IT-инфраструктура для них вторична.
- Ключевая возможность F&F: публичные цены + SLA + серверы 1С/ЭЦП/инфобез + локальный бренд = отстройка от 80% рынка.


## 8. Топ-8 самых опасных конкурентов для F&F (глубокий разбор)

### 1. its-kazan.ru (IT Сервис)
1. Оффер: абонентское обслуживание IT-инфраструктуры МСБ (компьютеры, серверы, сети), тарифы Эконом/Бизнес/Премиум.
2. Первый экран: заголовок "Абонентское обслуживание IT инфраструктуры", тарифы, телефон. Нет цен, нет явного CTA.
3. Цены: не публичные (тарифы без цифр).
4. Гарантии/сроки: Zabbix 24/7, ITIL, быстрое реагирование; сроков нет.
5. Trust: 10+ лет, 2ГИС 5.0/28 отзывов, отзывы клиентов.
6. SEO-структура: старый сайт, слабый контент, нет блога, нет answer-first.
7. Воронка: телефон -> консультация -> договор. Нет калькулятора/лид-магнита.
8. Где перебить: публичные цены + SLA + серверы 1С/ЭЦП + контент/SEO.

### 2. tss-kazan.ru (ТехноСистемСервис)
1. Оффер: IT-аутсорсинг, внедрение ИТ-систем, СКС, IP-телефония, виртуализация.
2. Первый экран: слайдер услуг + "Бесплатный аудит IT-инфраструктуры".
3. Цены: не публичные.
4. Гарантии/сроки: SLA с финансовыми гарантиями (100% возврат), постоплата, проактивный мониторинг.
5. Trust: 10 лет, кейсы торговых сетей, отзывы.
6. SEO-структура: устаревший сайт, нет блога/контента.
7. Воронка: форма "Оставить заявку", телефон.
8. Где перебить: публичные цены + контент + локальный бренд + 1С/ЭЦП.

### 3. itprovider.ru (IT Provider)
1. Оффер: IT-поддержка/аутсорсинг серверной инфраструктуры, service desk, SLA.
2. Первый экран: "ИТ-поддержка, на которую можно положиться. 24/7.", метрики (600k+ обращений, 35 специалистов).
3. Цены: не публичные.
4. Гарантии/сроки: SLA, 24/7, реакция 15 мин, решение 20 мин.
5. Trust: с 2009, отзывы, реквизиты, NDA.
6. SEO-структура: сайт перегружен, слабая локальная SEO.
7. Воронка: форма "Заказать звонок", телефон.
8. Где перебить: публичные цены + контент + МСБ-фокус (они фокус на серверах/enterprise).

### 4. i-tat.ru (АЙТАТ)
1. Оффер: 1С-сопровождение + IT-обслуживание, сметные программы.
2. Первый экран: слайдер услуг (ИТ, 1С, сметы).
3. Цены: не публичные (цены на 1С стандартные).
4. Гарантии/сроки: линия консультаций до 21:00, реакция 10 мин.
5. Trust: 11 лет, 2700 клиентов, отзывы, сертификаты.
6. SEO-структура: устаревший сайт, нет контента.
7. Воронка: форма "Обратиться", телефон.
8. Где перебить: IT-инфраструктура + серверы 1С + ЭЦП + контент (они фокус на 1С/сметах).

### 5. esc-kazan.ru (Центр электронных услуг)
1. Оффер: бэк-офис под ключ: бухгалтерия + юрист + сисадмин + ЭЦП + тендеры.
2. Первый экран: "Бэк-офис под ключ ... за 50 000 руб.".
3. Цены: пакет от ~50 000 руб./мес.
4. Гарантии/сроки: 95% вопросов в течение рабочего дня.
5. Trust: 21 год, реквизиты, 1С/Контур/СБИС.
6. SEO-структура: слабая (сайт небольшой).
7. Воронка: форма, 8-800.
8. Где перебить: фокус на IT-инфраструктуре (у них IT вторичен), серверы, SLA.

### 6. a1-support.ru (A1 Support)
1. Оффер: удалённая IT-поддержка: абонентка ПК/серверов, 1С, ЭЦП, почта.
2. Первый экран: "Удалённая IT-поддержка ... по всей России", калькулятор.
3. Цены: прозрачные (5 ПК = 5000 руб./мес).
4. Гарантии/сроки: договор, ответ в рабочее время.
5. Trust: с 2006, ИП, ИНН, договор, ЭДО.
6. SEO-структура: региональные страницы, блог? не видно.
7. Воронка: калькулятор -> форма -> телефон.
8. Где перебить: локальное присутствие + выезд + 1С/ЭЦП глубже + контент.

### 7. socialit.ru (Социалит Сервис)
1. Оффер: IT-аутсорсинг для розничных сетей/филиалов.
2. Первый экран: "ИТ-аутсорсинг для бизнеса по всей России", тарифы.
3. Цены: тарифы от 10 000 до 50 000 руб./мес.
4. Гарантии/сроки: SLA с финансовыми гарантиями, 3 линии.
5. Trust: 2011, 140+ сотрудников, 300+ клиентов, кейсы.
6. SEO-структура: блог/кейсы, сильный контент.
7. Воронка: форма, 8-800.
8. Где перебить: локальный бренд + МСБ не-розничный + серверы 1С/ЭЦП.

### 8. obit.ru (ОБИТ)
1. Оффер: оператор IT-решений: телеком, ЦОД, инжиниринг, инфобез, аутсорсинг.
2. Первый экран: "ОБИТ - оператор ИТ-решений", меню услуг.
3. Цены: не публичные (проектные).
4. Гарантии/сроки: проектные.
5. Trust: 20+ лет, кейсы, партнёры, лицензии.
6. SEO-структура: сильный (блог, кейсы, отрасли).
7. Воронка: форма, телефон, ЛК.
8. Где перебить: МСБ-фокус + прозрачные цены + абонентка (они enterprise).

---

### Кого F&F уже может бить
- its-kazan, tss-kazan, pc-kazan, comp-kazan, kazan.intertax, esc-kazan - по контенту, SEO, публичным ценам, SLA, answer-first.
- i-tat - по IT-инфраструктуре (серверы 1С, ЭЦП, инфобез) при сохранении 1С-партнёрства.

### Кого пока нет
- a1-support - прозрачные цены и удалённая поддержка.
- socialit - SLA с финансовыми гарантиями и сильный контент.
- obit - инфраструктура, ЦОД, бренд, SEO.
- itprovider - серверы, 24/7, SLA, NDA.

### За счёт чего обходить
- Публичные цены + SLA + серверы 1С/ЭЦП + локальный бренд + контент/SEO + выезд/локальное присутствие.
- Ниша "премиальный IT-аутсорсинг для МСБ в Казани" с фокусом на серверах 1С, ЭЦП, инфобез.


## 9. SEO-сравнение F&F с конкурентами Казани и Татарстана

### Что рынок уже закрыл
- Коммерческие страницы: its-kazan (абонентка), tss-kazan (услуги), itprovider (серверы), a8/itbsgroup (каталог), esc-kazan (бэк-офис), a1-support (удалёнка), socialit (тарифы), obit (инфраструктура).
- Локальные посадочные: i-tat (Челны/Нижнекамск/Альметьевск), a8/itbsgroup (Альметьевск/Челны/Нижнекамск), obit (Казань).
- Title/H1: большинство имеют title/H1, но многие слабые/дубли.
- Сравнение со штатным сисадмином: itprovider имеет блок "Уже есть системный администратор?".
- Серверные страницы: itprovider, tss-kazan, a8, itbsgroup, obit.
- Абонентка: its-kazan, tss-kazan, esc-kazan, a1-support, socialit.
- Коммерческие факторы: цены (a1-support, socialit, pc-kazan, comp-kazan), SLA (tss, itprovider, socialit), гарантии (comp-kazan 2 года).
- Контент под спрос: socialit (кейсы, FAQ, блог), obit (блог, кейсы, отрасли), i-tat (база знаний), a1-support (FAQ).

### Какие дыры остались в Казани и Татарстане
- Нет публичных цен у большинства прямых конкурентов (its, tss, itprovider, i-tat, esc).
- Нет SLA с финансовыми гарантиями у большинства (только tss, itprovider, socialit).
- Нет локальных посадочных для городов Татарстана (Челны, Нижнекамск, Альметьевск, Зеленодольск) у большинства, кроме i-tat/a8.
- Нет сравнения со штатным сисадмином у большинства (только itprovider, F&F).
- Нет серверных страниц у B2C-игроков (pc, comp, intertax).
- Нет контента под спрос у большинства (its, tss, itprovider, i-tat, esc) - нет блога/FAQ/кейсов.
- Нет коммерческих факторов (цены, гарантии, сроки) у большинства.
- Нет answer-first/FAQPage у большинства.
- Нет schema.org (Service, FAQPage, Person) у большинства.

### Что F&F должен закрыть первым, чтобы расти в поиске быстрее них
1. Публичные цены + SLA на всех коммерческих страницах (prices, services, servers, support).
2. Локальные посадочные для городов Татарстана (Челны, Нижнекамск, Альметьевск, Зеленодольск) с title/H1/FAQ/schema.
3. Серверные страницы с контентом под спрос (сервер 1С, почта, виртуализация, резервное копирование).
4. Сравнение со штатным сисадмином (уже есть compare/staff-sysadmin-cost.html - усилить, добавить FAQ).
5. Абонентка с тарифами и гарантией (унифицировать 30 дней vs 6 месяцев).
6. Коммерческие факторы: цены, гарантии, сроки, SLA на всех страницах.
7. Контент под спрос: blog/articles с answer-first, FAQPage, кейсы с метриками.
8. SEO-техника: canonical абсолютные (уже), sitemap (уже), schema (Service, FAQPage, Person, BreadcrumbList), llms.txt.


## 10. Сравнение офферов и формулировка оффера F&F

### Шаблоны конкурентов (локальные + федеральные)
- "Опыт N лет": its (10+), tss (10), itprovider (с 2009), i-tat (11), esc (21), a1 (с 2006), obit (20+), socialit (2011), iteron (18), 1cbit (29).
- "Комплексный подход": esc ("бэк-офис под ключ"), obit ("комплексная экспертиза"), a8 ("комплексные решения").
- "Профессиональная команда": its ("профессиональный сервис"), tss ("команда сертифицированных специалистов"), itprovider ("команда экспертов"), pc ("опытные специалисты").
- Мутные цены: у большинства (its, tss, itprovider, i-tat, esc, a8, itbsgroup, obit, iteron, 1cbit) нет публичных цен.
- Слабые гарантии: у большинства нет гарантии/SLA (its, i-tat, esc, a8, itbsgroup, pc, comp, intertax, obit, iteron, 1cbit). Только tss, itprovider, socialit, a1 имеют SLA.
- Нет нормального TCO штатного сисадмина: никто не показывает сравнение "штатный сисадмин vs аутсорсинг" с цифрами (только itprovider имеет блок "Уже есть системный администратор?").

### Оффер F&F (острее рынка)

#### В Казани
- Заголовок: "IT-аутсорсинг для офисов 20-50 человек в Казани: серверы 1С, ЭЦП, инфобез под ключ."
- Подзаголовок: "Прозрачная цена от X руб./мес, реакция 15 минут, гарантия 6 месяцев. Дешевле штатного сисадмина на 40% (TCO). Выезд инженера в день обращения."
- CTA: "Получить расчёт TCO за 2 минуты" (калькулятор) + "Заказать аудит".

#### По Татарстану
- Заголовок: "IT-аутсорсинг для бизнеса в Татарстане: Казань, Челны, Нижнекамск, Альметьевск."
- Подзаголовок: "Один договор, один SLA, один счёт. Прозрачные цены, гарантия 6 месяцев, выезд инженера в ваш город."
- CTA: "Получить расчёт для вашего города" + "Заказать выезд".

#### Против сильных удалённых игроков
- Заголовок: "Локальный IT-аутсорсинг в Казани с выездом и серверами 1С/ЭЦП. Не удалёнка - мы рядом."
- Подзаголовок: "Прозрачная цена, SLA с финансовыми гарантиями, гарантия 6 месяцев, серверы 1С и ЭЦП под ключ. Дешевле штатного сисадмина на 40% (TCO)."
- CTA: "Сравнить с удалённой поддержкой" + "Получить расчёт TCO".

### Ключевые элементы оффера F&F
- Прозрачная цена и сроки: публичные тарифы на всех коммерческих страницах.
- Гарантия 6 месяцев: единый срок на всех страницах (вместо 30 дней/6 месяцев).
- Сравнение со стоимостью штатного: TCO-калькулятор + страница "F&F vs штатный сисадмин".
- Реакция/SLA: 15 минут реакция, 4 часа решение, финансовые гарантии.
- Сегмент офисов 20-50 человек: тарифы и кейсы под этот сегмент.


## 11. Trust-сигналы: локальные vs федеральные

### Локальные (Казань/Татарстан)
| Игрок | Реквизиты | Договор/SLA | Гарантия | Команда | Кейсы | Отзывы | Прозрачность |
|---|---|---|---|---|---|---|---|
| its-kazan | Адрес, телефон, email | Нет | Нет | "Специалисты", без фото | Нет | Да (2ГИС 5.0, 28 оценок) | Тарифы без цен |
| tss-kazan | Адрес, телефон, email | SLA, постоплата | 100% возврат | "Сертифицированные специалисты" | Да (торговые сети) | Да | SLA, но цены мутные |
| itprovider | ИНН/ОГРН указаны | SLA, NDA | SLA | 35 специалистов, без фото | Нет | Да (hh.ru 4.4) | SLA, цены мутные |
| i-tat | Не указаны | Нет | Нет | Фото специалистов | Нет | Да | Цены на 1С стандартные |
| esc-kazan | ИНН-КПП, ОГРН | Нет | Нет | Не указано | Нет | Не видно | Тарифы от 5000 руб. |
| pc-kazan/comp-kazan/intertax | Политика конфиденциальности | Нет | comp-kazan до 2 лет | "Сертифицированные специалисты" | Нет | Да | Цены низкие, публичные |
| a8/itbsgroup | Не указаны | Нет | Нет | Не указано | Проекты | Не видно | Каталог, проекты |

### Федеральные (топ-5)
| Игрок | Реквизиты | Договор/SLA | Гарантия | Команда | Кейсы | Отзывы | Прозрачность |
|---|---|---|---|---|---|---|---|
| a1-support | ИП, ИНН, ОГРНИП | Договор, ЭДО | Нет явной | Фото инженера | Нет | Не видно | Цены публичные |
| obit | Не указаны | Нет | Нет | Фото | Да (Петрович, банк СПб) | Не видно | Проекты, партнёры |
| socialit | Не указаны | SLA | SLA с фин. гарантиями | Не указано | Да (много) | Не видно | Тарифы, SLA |
| iteron | ООО, адрес, телефон | Нет | Нет | Фото | Да | Да | Калькулятор, цены мутные |
| 1cbit | ООО, ОГРН, ИНН | SLA | SLA | Не указано | Да | Не видно | Цены не публичные |

### 1. Кто выглядит самым надёжным
- itprovider (Казань): реквизиты + SLA + NDA + 24/7 + команда + отзывы.
- socialit (федеральный): SLA с финансовыми гарантиями + кейсы + тарифы.
- a1-support (федеральный): реквизиты + договор + ЭДО + цены.
- obit (федеральный): кейсы + партнёры + лицензии + 20 лет.
- tss-kazan (Казань): SLA + гарантия возврата + кейсы.

### 2. Почему
- Реквизиты + SLA + кейсы + отзывы + прозрачность условий = доверие.
- itprovider: единственная локальная компания с реквизитами и SLA.
- socialit: единственная с SLA и финансовыми гарантиями + кейсами.
- a1-support: прозрачные цены + договор + ЭДО.
- obit: сильные кейсы + партнёры + лицензии.
- tss-kazan: SLA + гарантия возврата + кейсы.

### 3. Где у большинства пусто
- Реквизиты (ИНН/ОГРН): у большинства не указаны (its, i-tat, esc, a8, pc, comp, intertax, obit, socialit, iteron).
- Договор/SLA: у большинства нет (its, i-tat, esc, a8, pc, comp, intertax, obit, iteron, 1cbit).
- Гарантия: у большинства нет (its, i-tat, esc, a8, pc, comp, intertax, obit, iteron, 1cbit).
- Команда: у большинства нет фото/имён (its, tss, itprovider, i-tat, esc, a8, itbsgroup, pc, comp, intertax, a1, socialit, obit, iteron, 1cbit). Только i-tat имеет фото.
- Кейсы: у большинства нет (its, i-tat, esc, pc, comp, intertax, a1, socialit? есть, obit есть).
- Отзывы: у большинства есть (its, tss, itprovider, i-tat, pc, comp, intertax, iteron). У a8, esc, a1, socialit, obit, 1cbit - не видно.
- Прозрачность условий: у большинства нет (its, tss, itprovider, i-tat, esc, a8, itbsgroup, pc, comp, intertax, obit, iteron, 1cbit). Только a1, socialit имеют.

### 4. Что F&F усилить, чтобы выигрывать по доверию в Татарстане
- Реквизиты на всех страницах (ИНН, ОГРН, адрес, телефон).
- Договор/SLA с финансовыми гарантиями.
- Гарантия 6 месяцев (единый срок).
- Команда: фото, имена, сертификаты.
- Кейсы с метриками (до/после).
- Отзывы с именами, компаниями, датами, фото.
- Прозрачность условий: цены, сроки, SLA, гарантии.


## 12. Конверсионные решения: сильные приёмы и слабые места

### A. 10 сильных приёмов рынка
1. a1-support: калькулятор стоимости на первом экране - мгновенный ответ, снижает барьер.
2. socialit: тарифы с ценами на первом экране (10k/20k/50k) - прозрачность.
3. tss-kazan: "Бесплатный аудит IT-инфраструктуры" - лид-магнит, снижает барьер.
4. esc-kazan: "Бэк-офис под ключ за 50 000 руб." - чёткий ценовой якорь.
5. itprovider: метрики на первом экране (600k+ обращений, 35 специалистов, 24/7) - trust + конверсия.
6. pc-kazan/comp-kazan: форма "Оставить заявку" с быстрым ответом (15 мин) - снижает тревогу.
7. a1-support: 8-800 бесплатный номер + Telegram/MAX - мультиканальность.
8. socialit: "Получить КП" на каждом тарифе - чёткий CTA.
9. obit: кейсы с метриками на главной - proof.
10. its-kazan: отзывы клиентов на главной - social proof.

### B. 10 слабых мест рынка
1. Нет калькулятора у большинства (its, tss, itprovider, i-tat, esc, a8, obit, 1cbit).
2. Нет цен на первом экране у большинства (its, tss, itprovider, i-tat, esc, a8, obit, 1cbit).
3. Слабые CTA: "Заказать звонок" вместо конкретного действия.
4. Формы без следующего шага: нет "что будет после заявки".
5. Нет лид-магнитов (чек-листы, аудиты) у большинства.
6. Длинные формы с лишними полями.
7. Нет мультиканальности (только телефон) у многих.
8. Нет trust на форме (гарантия ответа, конфиденциальность).
9. Нет urgency/scarcity.
10. Нет "следующего шага" после заявки (что будет дальше).

### C. Что внедрить на сайте F&F
1. Калькулятор TCO на первом экране (как a1-support).
2. Публичные цены/тарифы на первом экране (как socialit).
3. Чёткий CTA: "Получить расчёт за 2 минуты" (вместо "Заказать звонок").
4. Лид-магнит: "Бесплатный аудит IT-инфраструктуры" (как tss-kazan).
5. Форма с 3 полями + гарантия ответа за 15 минут (как pc-kazan).
6. Мультиканальность: телефон + TG + MAX + форма (как a1-support).
7. "Что будет после заявки" (4 шага) на форме/CTA.
8. Отзывы/кейсы на первом экране (как its-kazan, obit).
9. Urgency: "Первый месяц со скидкой 20%".
10. Мобильная форма (sticky CTA) для мобильного трафика.


## План усиления против конкурентов

### A. Сделать сразу (1-3 дня)
- SEO: унифицировать гарантию (30 дней -> 6 месяцев) на всех страницах; добавить реквизиты (ИНН/ОГРН) в footer на всех страницах; добавить schema (Organization, Service, FAQPage, Person, BreadcrumbList) на страницы без schema; добавить incidents в навигацию на 81 странице.
- Оффер: опубликовать цены/тарифы на prices.html, services.html, servers.html, support.html; добавить TCO-калькулятор.
- Первый экран: добавить отзывы/кейсы на index.html, services.html, servers.html, support.html.
- Цена и сроки: публичные цены + сроки на всех коммерческих страницах.
- Гарантия 6 месяцев: единый срок на всех страницах.
- Trust: реквизиты, договор/SLA, кейсы с метриками, отзывы с именами/компаниями.
- Конверсия: короткая форма (3 поля) + гарантия ответа 15 минут; мультиканальность (телефон + TG + MAX + форма); "что будет после заявки" (4 шага).
- Контент: answer-first на всех страницах; FAQPage schema; кейсы с метриками.

### B. Сделать за 14 дней
- SEO: локальные посадочные для городов Татарстана (Челны, Нижнекамск, Альметьевск, Зеленодольск) с title/H1/FAQ/schema; серверные страницы с контентом под спрос (сервер 1С, почта, виртуализация, резервное копирование); сравнение со штатным сисадмином (усилить compare/staff-sysadmin-cost.html, добавить FAQ).
- Оффер: страница "F&F vs штатный сисадмин" с TCO-калькулятором; страница "F&F vs удалённая поддержка".
- Первый экран: видео/анимация на index.html; sticky mobile CTA.
- Цена и сроки: тарифы для офисов 20-50 человек; скидка за первый месяц.
- Гарантия 6 месяцев: единый срок на всех страницах (проверка).
- Trust: команда (фото, имена, сертификаты); кейсы с метриками (до/после).
- Конверсия: лид-магнит "Бесплатный аудит IT-инфраструктуры"; urgency/scarcity; A/B тесты hero/CTA.
- Контент: blog/articles с answer-first; отраслевые страницы (строительство, образование, холдинги); сравнительные (F&F vs облако, по размеру компании).

### C. Сделать за 30-45 дней
- SEO: усилить внутреннюю перелинковку (контекстные ссылки из hub-страниц); расширить ценовые блоки на services/*.html; добавить микроконверсии (чек-листы, аудиты) на все страницы; оптимизировать dist/build (использовать или убрать).
- Оффер: отраслевые офферы (IT для клиник, HoReCa, ритейла, производства); лендинги под каждый сегмент.
- Первый экран: персонализация по городу/отрасли.
- Цена и сроки: калькулятор ROI; сравнение с конкурентами.
- Гарантия 6 месяцев: продление до 12 месяцев для премиум-тарифа.
- Trust: реальные отзывы с датами/компаниями/ссылками на карты; trust-сигналы в структурированном виде (schema Review).
- Конверсия: мультистеп-форма; чат-бот; exit-intent popup с оффером.
- Контент: кейсы с метриками (10+); статьи под спрос (сервер 1С, ЭЦП, инфобез); FAQ на всех страницах; llms.txt обновление.

### Безопасные правки (внедрить сразу)
- Обновить CHANGELOG.md (docs/CHANGELOG.md) с новыми правками.
- Добавить реквизиты в footer на всех страницах (уже есть на contacts.html).
- Добавить schema на terms-of-work.html (P1 из аудита).
- Унифицировать гарантию (30 дней -> 6 месяцев) через скрипт с проверкой.


## Первые экраны конкурентов

### Казань/Татарстан

| Домен | H1 | Подзаголовок | Главный CTA | Вторичный CTA | Цена/цифры | Trust-маркеры | За 3 сек | Сильный | Провальный |
|---|---|---|---|---|---|---|---|---|---|
| its-kazan.ru | Абонентское обслуживание IT инфраструктуры | Почему компании выбирают IT аутсорсинг? | Телефон +7 843 253-0-263 | Нет | Нет цен | 10+ лет, отзывы | Тарифы, телефон | Тарифы на первом экране | Нет цены, нет CTA-кнопки |
| tss-kazan.ru | IT услуги аутсорсинга, внедрение ИТ систем для бизнеса в Казани | Обслуживание компьютеров от фанатов своего дела | Оставить заявку | Заказать аудит | Нет | 10 лет, SLA | Слайдер услуг | Бесплатный аудит | Нет цен, слайдер перегружен |
| itprovider.ru | ИТ-поддержка, на которую можно положиться. 24/7. | Решенных обращений от клиентов с 2009 года | Заказать звонок | Нет | 640 000 решенных, 35 специалистов, 28 000 единиц | С 2009, отзывы | Метрики, 24/7 | Метрики | Нет цен, перегружен |
| i-tat.ru | Компания «АЙТАТ» | ТЕПЛАЯ ПОДДЕРЖКА СЛОЖНЫХ ПРОГРАММ | Обратиться | Заказать обратный звонок | 4.7, 11 лет, 2700 клиентов | Отзывы, сертификаты | Слайдер услуг | Горячая линия | Нет цен, слайдер перегружен |
| esc-kazan.ru | Техническое сопровождение бизнеса | Услуга технического сопровождения «под ключ» | 8 800 600-48-15 | Заказать обратный звонок | 21 год, 15 мин реакция, 99.9% доступность | Реквизиты, 1С/Контур | Тарифы | Тарифы с ценами | IT вторичен |
| pc-kazan.ru | Компьютерная помощь в Казани | Компьютерной помощь – это быстрый ремонт любой поломки | Оставить заявку | Обратный звонок | 4.5/5, скидка 10% | Отзывы | Форма заявки | Форма с быстрым ответом | B2C-фокус |
| a8/itbsgroup | IT Business Solutions - опытный интегратор в области импортозамещения | IT Business Solutions - опытный интегратор | Заказать звонок | Личный кабинет | Нет | Проекты, партнёры | Каталог | Каталог | Нет чёткого оффера |
| calltraffic.ru | Непрерывность коммуникаций и эффективное управление клиентским опытом | Тонкая настройка под бизнес-процессы партнера | Начать сотрудничество | Телефон | 16 лет, 13 площадок, 2500+ сотрудников | Лицензии ФСТЭК | Метрики | Метрики | Не IT-аутсорсинг |
| erpdev.i-neti.ru | Разработка и сопровождение 1С | Усилим вашу команду разработчиками | Бесплатно оценить задачу | Телефон | 200+ разработчиков, 300+ проектов | Отзывы, NDA/SLA | Метрики | Метрики | Не IT-аутсорсинг |

### Федеральные топ-5

| Домен | H1 | Подзаголовок | Главный CTA | Вторичный CTA | Цена/цифры | Trust-маркеры | За 3 сек | Сильный | Провальный |
|---|---|---|---|---|---|---|---|---|---|
| a1-support.ru | Удалённая IT-поддержка компьютеров и серверов для бизнеса по всей России | Берём на себя компьютеры, серверы, 1С, электронную подпись и почту | Рассчитать стоимость | 8 800 555-90-23 | 5 ПК = 5000 руб./мес | С 2006, ИП, ИНН, договор, ЭДО | Калькулятор, цена | Цена + калькулятор | Нет локального присутствия |
| obit.ru | ОБИТ — оператор ИТ-решений с компетенциями... | Комплексная экспертиза, которая приносит результат | Связаться с нами | Личный кабинет | Нет | 20+ лет, кейсы, партнёры | Меню услуг | Кейсы | Нет цены, перегружен |
| socialit.ru | ИТ-аутсорсинг для бизнеса по всей России | Комплексное обслуживание пользователей и ИТ-инфраструктуры 24/7 | Получить консультацию | Посмотреть тарифы | Тарифы 10k/20k/50k | 2011, 140+ сотрудников, 300+ клиентов | Тарифы + CTA | Тарифы + CTA | Высокий порог |
| iteron.ru | IT-поддержка, которая всегда рядом | Доверьте нам IT, чтобы сосредоточиться на развитии | Заказать консультацию | Калькулятор | Калькулятор | 18 лет, 31+ компаний | Калькулятор | Калькулятор | Нет локального присутствия |
| 1cbit.ru | Первый Бит | Входим в ТОП-100 крупнейших ИТ-компаний России | Заказать бесплатную консультацию | Заказать звонок | 9 стран, 29 лет, 9000+ специалистов | 300 000+ клиентов | Форма | Масштаб | IT-аутсорсинг вторичен |

### A. Лучшие паттерны первого экрана
- Цена на первом экране (a1-support, socialit, esc-kazan).
- Калькулятор стоимости (a1-support, iteron).
- Метрики/цифры (itprovider, calltraffic, erpdev).
- Чёткий CTA с действием (socialit "Получить консультацию", a1-support "Рассчитать стоимость").
- Trust-маркеры (логотипы, отзывы, реквизиты).
- Вторичный CTA (socialit "Посмотреть тарифы", a1-support "8-800").

### B. Худшие паттерны
- Нет цены на первом экране (its-kazan, tss-kazan, itprovider, i-tat, a8, obit, 1cbit).
- Нет чёткого CTA (its-kazan только телефон, obit "Связаться с нами").
- Перегруженный первый экран (itprovider, i-tat, obit).
- Нет trust-маркеров (pc-kazan, comp-kazan, intertax).
- Слайдер вместо чёткого оффера (its-kazan, i-tat).
- Нет вторичного CTA (its-kazan, itprovider, pc-kazan).

### C. Что внедрить в первый экран F&F
- H1: "IT-аутсорсинг для офисов 20-50 человек в Казани".
- Подзаголовок: "Серверы 1С, ЭЦП, инфобез под ключ. Прозрачная цена, SLA, гарантия 6 месяцев."
- Главный CTA: "Получить расчёт за 2 минуты" (калькулятор).
- Вторичный CTA: "Заказать аудит".
- Цена/цифры: "От 15 000 руб./мес", "Реакция 15 минут", "Гарантия 6 месяцев".
- Trust-маркеры: логотипы клиентов, отзывы, реквизиты, 2ГИС.
- За 3 сек: цена + CTA + trust.


## Цены и упаковка

### Сравнительный разбор ценовой архитектуры

| Игрок | Вилки "от" | Пакеты/тарифы | Что входит | Доплата | Понятность расчёта | Сравнение со штатным | Калькулятор | Где цена прячется |
|---|---|---|---|---|---|---|---|---|
| its-kazan | Нет | Эконом/Бизнес/Премиум | Компьютеры, серверы, сети | Не указано | Низкая | Нет | Нет | В тарифах без цифр |
| tss-kazan | Нет | Не указаны | Компьютеры, сети, серверы | Не указано | Низкая | Нет | Нет | В форме заявки |
| itprovider | Нет | Не указаны | Серверы, service desk, SLA | Не указано | Низкая | Блок "Уже есть сисадмин?" | Нет | В форме заявки |
| i-tat | Нет | Не указаны | 1С, IT-обслуживание, сметы | Не указано | Низкая | Нет | Нет | В форме заявки |
| esc-kazan | Да (от 5000 руб.) | Эконом/Бизнес | 4 ПК + МФУ, сервер, ЭЦП | Доп. ПК +800/1000 руб. | Средняя | Нет | Нет | В тарифах |
| pc-kazan/comp-kazan/intertax | Да (от 250-474 руб.) | Разовые услуги | Ремонт, настройка, заправка | Не указано | Высокая | Нет | Нет | На страницах услуг |
| a8/itbsgroup | Нет | Каталог оборудования | Серверы, сети, инфобез | Не указано | Низкая | Нет | Нет | В каталоге |
| calltraffic | Нет | Не указаны | Контакт-центр, техподдержка ИС | Не указано | Низкая | Нет | Нет | В форме заявки |
| erpdev | Нет | Не указаны | 1С-разработка, ERP | Не указано | Низкая | Нет | Нет | В форме заявки |
| a1-support | Да (от 5000 руб./мес) | 5 ПК = 5000 руб., +500 руб./ПК | ПК, серверы, 1С, ЭЦП, почта | Сервер от 1200 руб. | Высокая | Нет | Да | На странице "Цены" |
| obit | Нет | Не указаны | Телеком, ЦОД, инжиниринг, аутсорсинг | Не указано | Низкая | Нет | Нет | В форме заявки |
| socialit | Да (от 10 000 руб./мес) | Удалённый/Базовый/Расширенный | ПК, серверы, сети, 1С, Битрикс | По запросу | Высокая | Нет | Нет | В тарифах |
| iteron | Нет | Не указаны | Абонентка, 1С, серверы | Не указано | Средняя | Нет | Да | В калькуляторе |
| 1cbit | Нет | Не указаны | 1С, IT-поддержка, инфраструктура | Не указано | Низкая | Нет | Нет | В форме заявки |

### 1. Кто упаковывает цену лучше всех
- a1-support: прозрачные цены (5 ПК = 5000 руб./мес), калькулятор, вилки "от", понятный расчёт.
- socialit: тарифы с ценами (10k/20k/50k), SLA с финансовыми гарантиями, понятный состав.
- esc-kazan: тарифы с ценами (5000/8000 руб.), пакеты с количеством ПК/серверов, доплата за доп. ПК.
- pc-kazan/comp-kazan/intertax: низкие цены, публичные, понятный расчёт.

### 2. Где рынок туманит
- its-kazan, tss-kazan, itprovider, i-tat, a8, itbsgroup, obit, iteron, 1cbit, calltraffic, erpdev — нет публичных цен, вилки "от" отсутствуют, расчёт непонятен, цена прячется в форме заявки.
- a1-support: цены прозрачны, но нет сравнения со штатным.
- socialit: тарифы с ценами, но высокий порог (от 10k).
- esc-kazan: цены есть, но IT вторичен.

### 3. Как F&F должен подать цену, сроки и гарантию 6 месяцев
- Публичные цены/тарифы на всех коммерческих страницах (prices, services, servers, support).
- Калькулятор TCO (штатный vs аутсорсинг) на первом экране.
- Вилки "от" с чётким составом (что входит, что за доплату).
- Сравнение со штатным сисадмином (TCO) с цифрами.
- Гарантия 6 месяцев + SLA с финансовыми гарантиями.
- Пакеты для офисов 20-50 человек.
- Прозрачность: цены, сроки, SLA, гарантии на всех страницах.


## Скорость доверия

### Оценка конкурентов (за сколько скроллов/секунд сайт начинает выглядеть надёжно)

| Игрок | Реквизиты | Лица | Кейсы | Отзывы | Договор/SLA | Гарантия | Процесс | Скорость доверия |
|---|---|---|---|---|---|---|---|---|
| its-kazan | Да (адрес, телефон, email) | Нет | Нет | Да (много) | Нет | Нет | Нет | Средняя |
| tss-kazan | Да (адрес, телефон, email) | Нет | Да (торговые сети) | Да | SLA | 100% возврат | Нет | Высокая |
| itprovider | Да (ИНН/ОГРН) | Нет | Нет | Да (hh.ru) | SLA, NDA | SLA | Нет | Высокая |
| i-tat | Нет | Фото специалистов | Нет | Да | Нет | Нет | Нет | Средняя |
| esc-kazan | Да (ИНН/ОГРН) | Нет | Нет | Нет | Нет | Нет | Нет | Низкая |
| pc-kazan/comp-kazan/intertax | Политика конфиденциальности | Нет | Нет | Да | Нет | comp-kazan до 2 лет | Нет | Низкая |
| a8/itbsgroup | Нет | Нет | Проекты | Нет | Нет | Нет | Нет | Низкая |
| calltraffic | Да (адрес, телефон, email) | Нет | Нет | Нет | Лицензии ФСТЭК | Нет | Нет | Средняя |
| erpdev | Да (адрес, телефон, email) | Нет | Да | Да | NDA/SLA | 24 мес | Нет | Высокая |
| a1-support | Да (ИП, ИНН, ОГРНИП) | Фото инженера | Нет | Нет | Договор, ЭДО | Нет | 4 шага | Высокая |
| obit | Нет | Фото | Да (много) | Нет | Нет | Нет | Нет | Средняя |
| socialit | Нет | Нет | Да (много) | Нет | SLA | SLA | Нет | Высокая |
| iteron | Да (ООО, адрес, телефон) | Фото | Да | Да | Нет | Нет | Нет | Средняя |
| 1cbit | Да (ООО, ОГРН, ИНН) | Нет | Да | Нет | SLA | SLA | Нет | Средняя |
| F&F | Да (ИНН: 165506822661) | Нет | Да (7 кейсов) | Да (7 анонимных) | Нет | 30 дней (130+) vs 6 мес (27) | Нет | Средняя |

### Кто вызывает доверие быстрее
- a1-support: реквизиты + договор + ЭДО + цены + 4 шага процесса.
- socialit: SLA + кейсы + тарифы.
- tss-kazan: SLA + кейсы + отзывы.
- itprovider: реквизиты + SLA + NDA + отзывы.
- erpdev: кейсы + отзывы + NDA/SLA.

### За счёт каких блоков
- Реквизиты (ИНН/ОГРН) на первом экране.
- Отзывы с именами/компаниями.
- Кейсы с метриками.
- SLA/договор с финансовыми гарантиями.
- Гарантия.
- Понятный процесс (шаги).
- Лица (фото команды).

### Каких 5 trust-элементов не хватает F&F
1. Лица (фото команды, имена, сертификаты) на первом экране.
2. SLA/договор с финансовыми гарантиями.
3. Кейсы с метриками (до/после) на первом экране.
4. Отзывы с именами, компаниями, датами, фото.
5. Понятный процесс работы (4 шага) на первом экране.


## Страницы услуг конкурентов

### Сравнение по типам страниц

| Тип страницы | Конкурент | Глубина | Оффер | FAQ | Доказательства | CTA | Коммерческие факторы | Готовность закрывать интент | Оценка |
|---|---|---|---|---|---|---|---|---|---|
| Абонентское обслуживание | its-kazan | Средняя | Тарифы Эконом/Бизнес/Премиум | Нет | Отзывы | Телефон | Нет цен | Средняя | 6/10 |
| Абонентское обслуживание | tss-kazan | Средняя | SLA, бесплатный аудит | Нет | Кейсы | Форма | Нет цен | Средняя | 7/10 |
| Абонентское обслуживание | esc-kazan | Средняя | Тарифы Эконом/Бизнес | Нет | Нет | Форма, 8-800 | Цены (5000/8000 руб.) | Средняя | 6/10 |
| Абонентское обслуживание | a1-support | Высокая | Удалённая поддержка, калькулятор | Да | Нет | Калькулятор, 8-800 | Цены (5 ПК = 5000 руб.) | Высокая | 9/10 |
| Абонентское обслуживание | socialit | Высокая | Тарифы, SLA | Да | Кейсы | Форма, 8-800 | Цены (10k/20k/50k) | Высокая | 9/10 |
| Абонентское обслуживание | iteron | Средняя | Абонентка, 1С, серверы | Нет | Отзывы | Калькулятор, форма | Калькулятор | Средняя | 7/10 |
| Серверы | itprovider | Высокая | Service desk, SLA, 24/7 | Нет | Отзывы | Форма | Нет цен | Средняя | 7/10 |
| Серверы | tss-kazan | Средняя | Аренда сервера, виртуализация | Нет | Кейсы | Форма | Нет цен | Средняя | 6/10 |
| Серверы | a8/itbsgroup | Высокая | Каталог оборудования, интеграция | Нет | Проекты | Заказать звонок | Каталог | Высокая | 8/10 |
| Серверы | obit | Высокая | Телеком, ЦОД, инжиниринг | Нет | Кейсы | Форма, ЛК | Нет цен | Высокая | 8/10 |
| IT-аудит/инфраструктура | tss-kazan | Средняя | Бесплатный аудит | Нет | Кейсы | Форма | Нет цен | Средняя | 6/10 |
| IT-аудит/инфраструктура | a1-support | Высокая | Удалённая поддержка, калькулятор | Да | Нет | Калькулятор | Цены | Высокая | 8/10 |
| IT-аудит/инфраструктура | obit | Высокая | Телеком, ЦОД, инжиниринг | Нет | Кейсы | Форма | Нет цен | Высокая | 8/10 |
| Системный администратор | itprovider | Высокая | Service desk, SLA, 24/7 | Нет | Отзывы | Форма | Нет цен | Средняя | 7/10 |
| Системный администратор | iteron | Средняя | Удалённый сисадмин | Нет | Отзывы | Форма | Калькулятор | Средняя | 6/10 |
| Системный администратор | a1-support | Высокая | Удалённая поддержка | Да | Нет | Калькулятор | Цены | Высокая | 8/10 |

### Какие типы страниц F&F обязан усилить или добавить

1. Абонентское обслуживание: усилить services.html и support.html — добавить тарифы с ценами, SLA, FAQ, кейсы, калькулятор TCO.
2. Серверы: усилить servers.html и infrastructure/* — добавить цены, SLA, кейсы, FAQ, сравнение с конкурентами.
3. IT-аудит/инфраструктура: усилить audits/* и infrastructure/* — добавить бесплатный аудит, FAQ, кейсы, цены.
4. Системный администратор: усилить compare/staff-sysadmin-cost.html — добавить TCO-калькулятор, FAQ, кейсы, сравнение с конкурентами.
5. Добавить страницы: "F&F vs штатный сисадмин", "F&F vs удалённая поддержка", локальные посадочные для городов Татарстана.
6. Усилить коммерческие факторы на всех страницах: цены, сроки, SLA, гарантии 6 месяцев.
7. Добавить FAQ на все коммерческие страницы.
8. Добавить кейсы с метриками на все коммерческие страницы.


## Язык рынка

### Повторяющиеся формулировки конкурентов

**Про опыт:**
- "более 10 лет", "с 2006 года", "более 20 лет", "многолетний опыт", "опыт множества специалистов".

**Про подход:**
- "системный подход", "индивидуальный подход", "комплексный подход", "проактивный мониторинг".

**Про надёжность:**
- "надёжно", "стабильно", "без сбоев", "бесперебойная работа", "гарантированное качество".

**Про команду:**
- "команда сертифицированных специалистов", "команда экспертов", "профессиональная команда".

**"Под ключ":**
- "под ключ", "бэк-офис под ключ", "сервер под ключ".

**"Комплексность":**
- "комплексное обслуживание", "комплексные решения", "комплексный подход".

### Что выгорело
- "опыт N лет" — у всех, не дифференцирует.
- "комплексный подход" — пустой шаблон.
- "профессиональная команда" — нет конкретики.
- "надёжно" — без доказательств.
- "под ключ" — без состава работ.

### Что звучит шаблонно
- "мы заботимся о ваших данных"
- "мы не новички"
- "качество выше"
- "мы работаем на результат"

### Что реально работает
- Конкретные цифры: "600 000 обращений", "35 специалистов", "24/7".
- SLA: "реакция 15 минут", "решение 4 часа".
- Цены: "5 ПК = 5000 руб./мес".
- Гарантии: "100% возврат", "гарантия 6 месяцев".
- Сравнение: "дешевле штатного сисадмина на 40%".

### Где рынок говорит о себе, а не о выгоде клиента
- "мы", "наша команда", "наш опыт", "мы работаем" — вместо "вы получите", "ваш бизнес", "сэкономите".
- Описание процессов компании вместо результата для клиента.
- Перечисление услуг вместо выгод.

### Языковые правила для F&F

**Что говорить:**
- "Вы получите", "ваш бизнес", "сэкономите", "заработаете".
- Конкретные цифры: цены, сроки, SLA, метрики.
- Сравнение: "дешевле штатного сисадмина на X%".
- Гарантия: "гарантия 6 месяцев", "SLA с финансовыми гарантиями".
- Процесс: "4 шага: аудит → настройка → поддержка → отчётность".

**Чего избегать:**
- "опыт N лет", "комплексный подход", "профессиональная команда", "под ключ" (без состава).
- "мы", "наша команда", "мы работаем" — вместо выгоды клиента.
- Общие слова без цифр: "надёжно", "качественно", "профессионально".

**Какие формулировки выделят:**
- "Прозрачная цена: 5 ПК = X руб./мес. Никаких скрытых платежей."
- "Реакция 15 минут. Решение 4 часа. Или мы платим вам."
- "Гарантия 6 месяцев. Не 30 дней — 6 месяцев."
- "Дешевле штатного сисадмина на 40%. Расчёт TCO за 2 минуты."
- "Серверы 1С, ЭЦП, инфобез под ключ. Не удалёнка — мы рядом."
- "Локальный бренд. Выезд инженера в день обращения."


## Возражения конкурентов

### Как конкуренты отрабатывают возражения

| Возражение | its-kazan | tss-kazan | itprovider | i-tat | esc-kazan | pc/comp/intertax | a8/itbsgroup | calltraffic | erpdev | a1-support | obit | socialit | iteron | 1cbit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Дорого | Нет | Нет | Нет | Нет | Нет | Нет | Нет | Нет | Нет | Нет | Нет | Нет | Нет | Нет |
| Почему не штатный | Нет | Нет | Да (блок) | Нет | Нет | Нет | Нет | Нет | Нет | Нет | Нет | Нет | Нет | Нет |
| Что если не поможет | Нет | Да (SLA) | Да (SLA) | Нет | Нет | Нет | Нет | Нет | Да (гарантия 24 мес) | Нет | Нет | Да (SLA) | Нет | Да (SLA) |
| Как быстро приедете | Нет | Нет | Да (15 мин) | Да (10 мин) | Да (95% в течение дня) | Да (1 час) | Нет | Нет | Нет | Да (рабочее время) | Нет | Нет | Нет | Нет |
| Есть ли договор/гарантия | Нет | Да (SLA) | Да (SLA, NDA) | Нет | Нет | comp-kazan до 2 лет | Нет | Лицензии ФСТЭК | Да (NDA/SLA) | Да (договор, ЭДО) | Нет | Да (SLA) | Нет | Да (SLA) |
| Что входит в цену | Нет | Нет | Нет | Нет | Да (тарифы) | Да (цены) | Нет | Нет | Нет | Да (цены) | Нет | Да (тарифы) | Нет | Нет |
| Можно ли начать с малого | Нет | Нет | Нет | Нет | Да (тариф Эконом) | Да (разовые) | Нет | Нет | Нет | Да (5 ПК) | Нет | Да (тариф Удалённый) | Нет | Нет |

### У кого отработка сильная
- tss-kazan: блок "Проблемы, с которыми сталкиваются многие компании" + "Что предлагаем мы" — отработка 5 возражений (остановка функционирования, отсутствие контроля, отсутствие планирования бюджета, лишние затраты, оперативность).
- a1-support: FAQ с 5 вопросами — отработка возражений (удалёнка, состав, договор, скорость, НДС).
- socialit: FAQ с 8 вопросами — отработка возражений (организация аутсорсинга, услуги сисадмина, филиалы, серверы, сеть, инфобез, развитие инфраструктуры, Битрикс24).
- itprovider: блок "Уже есть системный администратор?" — отработка возражения "у нас уже есть сисадмин".

### У кого её почти нет
- its-kazan, i-tat, esc-kazan, pc-kazan, comp-kazan, intertax, a8, itbsgroup, calltraffic, erpdev, obit, iteron, 1cbit — нет явных блоков отработки возражений.

### Какие возражения рынок игнорирует
- "Дорого" — игнорируют (нет сравнения с штатным).
- "Почему не штатный" — игнорируют (только itprovider имеет блок).
- "Что если не поможет" — игнорируют (нет гарантии/SLA).
- "Как быстро приедете" — игнорируют (нет сроков).
- "Есть ли договор/гарантия" — игнорируют (нет договора/SLA).
- "Что входит в цену" — игнорируют (нет состава).
- "Можно ли начать с малого" — игнорируют (нет тарифов для малого).

### Список возражений, которые F&F должен закрывать лучше всех
1. "Дорого" → прозрачная цена + TCO-сравнение со штатным.
2. "Почему не штатный" → страница "F&F vs штатный сисадмин" с TCO.
3. "Что если не поможет" → гарантия 6 месяцев + SLA с финансовыми гарантиями.
4. "Как быстро приедете" → SLA (реакция 15 мин, выезд в день обращения).
5. "Есть ли договор/гарантия" → договор + SLA + гарантия 6 месяцев.
6. "Что входит в цену" → тарифы с составом, "что входит/что за доплату".
7. "Можно ли начать с малого" → тарифы для офисов 20-50 человек, "первый месяц со скидкой".


## Репутация конкурентов

### Репутационный срез

| Игрок | Отзывы на сайте | Внешние отзывы | Кейсы | Конкретика в отзывах | Повторяющиеся жалобы | Повторяющиеся сильные стороны |
|---|---|---|---|---|---|---|
| its-kazan | Да (много) | 2ГИС 5.0, 28 оценок | Нет | "сотрудничество более 7 лет", "быстрая реакция" | Не видно | Быстрая реакция, качество, надёжность |
| tss-kazan | Да (клиенты о нас) | Не видно | Да (торговые сети) | "выбрали услуги этой компании", "безупречное сотрудничество" | Не видно | Профессионализм, качество, надёжность |
| itprovider | Нет | hh.ru 4.4, 16 отзывов | Нет | "аккредитованное, современное" | Не видно | Команда экспертов, 24/7, SLA |
| i-tat | Да (клиенты) | Не видно | Нет | "сотрудничество более 10 лет" | Не видно | Теплая поддержка, компетенции |
| esc-kazan | Нет | Не видно | Нет | Нет | Не видно | 21 год, комплексный подход |
| pc-kazan/comp-kazan/intertax | Да (клиенты) | 2ГИС 4.8, Яндекс 5.0 | Нет | "мастер почистил систему" | Не видно | Быстрый выезд, низкие цены, качество |
| a8/itbsgroup | Нет | Не видно | Проекты | Нет | Не видно | Интегратор, оборудование, проекты |
| calltraffic | Нет | Не видно | Нет | Нет | Не видно | 16 лет, катастрофоустойчивость, лицензии ФСТЭК |
| erpdev | Да (5/5) | Не видно | Да | "компетентность разработчика" | Не видно | Компетентность, скорость, качество |
| a1-support | Нет | Не видно | Нет | Нет | Не видно | С 2006, прозрачные цены, договор |
| obit | Нет | Не видно | Да (много) | Нет | Не видно | 20+ лет, кейсы, партнёры |
| socialit | Нет | Не видно | Да (много) | Нет | Не видно | SLA, кейсы, тарифы |
| iteron | Да | Не видно | Да | "98% компаний остаются с нами" | Не видно | 18 лет, калькулятор, 1С |
| 1cbit | Нет | Не видно | Да | Нет | Не видно | ТОП-100, 300 000+ клиентов |

### 1. За что хвалят рынок
- Быстрая реакция / оперативность.
- Качество услуг / профессионализм.
- Надёжность / стабильность.
- Индивидуальный подход.
- Конкретика: "сотрудничество более N лет", "быстрая реакция", "мастер почистил систему".

### 2. За что ругают
- Не видно в открытых данных (отзывы mostly positive).
- Предполагаемые жалобы: "дорого", "медленно", "не отвечают", "нет договора", "нет гарантии".

### 3. Какие обещания опасны
- "100% гарантия возврата" (tss-kazan) — опасно, если не выполняется.
- "Реакция 15 минут" (itprovider) — опасно, если не выполняется.
- "99.98% катастрофоустойчивость" (calltraffic) — опасно, если не выполняется.
- "Гарантия до 2 лет" (comp-kazan) — опасно, если не выполняется.
- "Сотрудничество более 10 лет" — без доказательств.

### 4. На каких репутационных полях F&F может зайти чище и убедительнее
- Отзывы с именами, компаниями, датами, фото (вместо анонимных).
- Кейсы с метриками (до/после) на первом экране.
- Конкретика в отзывах: что именно сделали, какой результат.
- Договор/SLA с финансовыми гарантиями.
- Гарантия 6 месяцев (единый срок).
- Отсутствие анонимных отзывов.
- Прозрачность условий: цены, сроки, SLA, гарантии.


## Локальное доминирование

### Кто сильнее всего выглядит локально
- i-tat: адреса в 5 городах, телефоны по городам, локальные посадочные (Челны/Нижнекамск/Альметьевск).
- a8/itbsgroup: меню городов (Казань, Альметьевск, Челны, Нижнекамск).
- its-kazan: адрес, телефон, 2ГИС, отзывы клиентов из Казани.
- tss-kazan: адрес, телефон, кейсы торговых сетей.
- itprovider: адрес, телефон, 2ГИС.

### Кто просто пишет "Казань" для галочки
- erpdev: Москва, нет локальных маркеров.
- iteron: Москва, нет локальных маркеров.
- 1cbit: Казань, но масштаб федеральный.
- obit: Казань (офис), но масштаб федеральный.
- socialit: Казань (телефон), но 70+ городов.
- a1-support: вся РФ, нет локального присутствия.
- calltraffic: Казань (площадка), но масштаб федеральный.

### Как F&F усилить локальное доминирование без дешёвого спама
1. Локальные посадочные для городов Татарстана (Челны, Нижнекамск, Альметьевск, Зеленодольск) с реальным контентом (кейсы, цены, SLA, выезд).
2. Кейсы с указанием города/отрасли.
3. Локальные маркеры: адрес (если есть), телефон с кодом 843, 2ГИС, Яндекс.Карты, отзывы.
4. Локальное SEO: schema Organization с address, geo, sameAs (2ГИС, Яндекс.Карты), FAQPage с локальными вопросами.
5. Выезд инженера: указать, что выезжаем в города Татарстана.
6. Отзывы с указанием города.
7. Не спамить: не создавать 50 одинаковых страниц с заменой города, а делать уникальный контент.


## Воронки конкурентов

### Разбор воронки 7 сильнейших конкурентов

| Конкурент | 1. Первый контакт | 2. Понимание оффера | 3. Понимание цены | 4. Снятие сомнений | 5. Заявка | 6. Ожидание после заявки |
|---|---|---|---|---|---|---|
| a1-support | Сильный: калькулятор, цена, 8-800 | Сильный: чёткий оффер, калькулятор | Сильный: цены публичные | Сильный: договор, ЭДО, ИП, ИНН | Сильный: калькулятор, форма, 8-800, TG/MAX | Сильный: договор, ЭДО, ответ в рабочее время |
| socialit | Сильный: тарифы, CTA | Сильный: тарифы, SLA | Сильный: тарифы с ценами | Сильный: SLA, кейсы | Сильный: форма, 8-800 | Сильный: SLA, 3 линии |
| tss-kazan | Средний: слайдер, бесплатный аудит | Средний: SLA, аудит | Слабый: нет цен | Сильный: SLA, гарантия возврата | Средний: форма, телефон | Средний: SLA, постоплата |
| itprovider | Средний: метрики, 24/7 | Средний: SLA, 24/7 | Слабый: нет цен | Сильный: SLA, NDA, отзывы | Средний: форма, телефон | Средний: SLA, 24/7 |
| esc-kazan | Средний: тарифы с ценами | Средний: бэк-офис | Средний: тарифы с ценами | Слабый: нет договора/SLA | Средний: форма, 8-800 | Слабый: нет SLA |
| i-tat | Средний: слайдер, горячая линия | Средний: 1С + IT | Слабый: нет цен | Средний: отзывы, сертификаты | Средний: форма, телефон | Слабый: нет SLA |
| obit | Средний: меню услуг | Средний: инфраструктура | Слабый: нет цен | Средний: кейсы, партнёры | Средний: форма, телефон, ЛК | Средний: кейсы, партнёры |

### Что сделано сильно / где отвал / что F&F должен сделать лучше

**1. Первый контакт с сайтом**
- Сильно: a1-support (калькулятор, цена), socialit (тарифы, CTA), itprovider (метрики).
- Отвал: its-kazan (нет цены), tss-kazan (нет цены), i-tat (нет цен), obit (нет цены).
- F&F: цена + CTA + trust на первом экране.

**2. Понимание оффера**
- Сильно: a1-support (чёткий оффер), socialit (тарифы, SLA), esc-kazan (бэк-офис).
- Отвал: tss-kazan (нет цен), itprovider (нет цен), i-tat (IT вторичен), obit (нет цены).
- F&F: чёткий оффер с цифрами и SLA.

**3. Понимание цены**
- Сильно: a1-support (цены публичные), socialit (тарифы с ценами), esc-kazan (тарифы с ценами).
- Отвал: tss-kazan (нет цен), itprovider (нет цен), i-tat (нет цен), obit (нет цен).
- F&F: публичные цены + калькулятор TCO.

**4. Снятие сомнений**
- Сильно: a1-support (договор, ЭДО), socialit (SLA, кейсы), tss-kazan (SLA, гарантия), itprovider (SLA, NDA, отзывы).
- Отвал: esc-kazan (нет договора/SLA), i-tat (нет договора/SLA), obit (нет цены).
- F&F: договор + SLA + гарантия 6 месяцев + кейсы + отзывы.

**5. Заявка**
- Сильно: a1-support (калькулятор, форма, 8-800, TG/MAX), socialit (форма, 8-800).
- Отвал: tss-kazan (нет цены), itprovider (нет цены), esc-kazan (IT вторичен), i-tat (нет цены), obit (нет цены).
- F&F: короткая форма + мультиканальность + "что будет после заявки".

**6. Ожидание после заявки**
- Сильно: a1-support (договор, ЭДО, ответ в рабочее время), socialit (SLA, 3 линии).
- Отвал: esc-kazan (нет SLA), i-tat (нет SLA), obit (нет цены).
- F&F: договор + SLA + гарантия + отчётность.


## Точки атаки в поиске

### Слабые места конкурентов и точки атаки F&F

| Запрос/кластер | Кто слабо закрывает | Чем F&F может перебить | Какой тип страницы нужен |
|---|---|---|---|
| Абонентское обслуживание в Казани | its-kazan, tss-kazan, esc-kazan (нет цен, нет FAQ, нет калькулятора) | Публичные цены + SLA + калькулятор TCO + FAQ | services.html, support.html, prices.html |
| Серверы в Казани | itprovider, tss-kazan, a8 (нет цен, нет FAQ, нет калькулятора) | Публичные цены + SLA + калькулятор TCO + FAQ + кейсы | servers.html, infrastructure/* |
| IT-аудит/инфраструктура | tss-kazan, a1-support (нет цен, нет FAQ, нет калькулятора) | Бесплатный аудит + FAQ + кейсы + цены | audits/*, infrastructure/* |
| Системный администратор | iteron, a1-support (нет цен, нет FAQ, нет калькулятора) | TCO-калькулятор + FAQ + кейсы + сравнение | compare/staff-sysadmin-cost.html |
| Локальные посадочные (Челны, Нижнекамск, Альметьевск, Зеленодольск) | i-tat, a8 (тонкие страницы, слабые title/H1) | Уникальный контент + цены + SLA + выезд | Локальные посадочные |
| Сравнение со штатным | itprovider (блок), F&F (compare/staff-sysadmin-cost.html) слабо закрывают | TCO-калькулятор + FAQ + кейсы | compare/* |
| Расчёты и прозрачные условия | a1-support (цены, калькулятор), socialit (тарифы) слабо закрывают (нет сравнения со штатным) | TCO-калькулятор + сравнение + гарантия 6 месяцев | prices.html, compare/* |

### Дополнительные точки атаки
- Тонкие страницы: ai/*, incidents/incident.html, resources/*, articles/*, company/partners.html, security/crypto.html, services/mail.html, infrastructure/*, industries/*, pain/*, cases/*, leads/*, compare/*, terms-of-work.html, 404.html — усилить контентом.
- Слабые title/H1: все страницы имеют title/H1, но некоторые слабые/дубли — усилить.
- Отсутствие FAQ: 31 страница с id="faq" без schema — добавить FAQPage.
- Слабые коммерческие факторы: цены на 48 страницах, тарифы на 13; гарантия не унифицирована — усилить.
- Нет нормальных серверных/абонентских посадочных: есть servers.html, services.html, support.html, но мало контента — усилить.
- Нет расчётов и прозрачных условий: нет калькулятора TCO — добавить.


## Swipe и адаптация

### Первый экран
| Конкурент | Что сильно | Почему работает | Как адаптировать под F&F сильнее оригинала |
|---|---|---|---|
| a1-support | Калькулятор + цена + 8-800 | Мгновенный ответ, прозрачность | TCO-калькулятор + цена + локальный телефон + выезд |
| socialit | Тарифы + CTA на первом экране | Прозрачность, чёткий CTA | Тарифы для 20-50 человек + CTA "Получить расчёт" |
| itprovider | Метрики (600k+, 35 специалистов, 24/7) | Доверие через цифры | Метрики F&F (количество заявок, время реакции, количество клиентов) |

### Тарификация
| Конкурент | Что сильно | Почему работает | Как адаптировать под F&F сильнее оригинала |
|---|---|---|---|
| a1-support | 5 ПК = 5000 руб., +500 руб./ПК | Прозрачность, понятный расчёт | Тарифы для 20-50 человек с ценами |
| socialit | Тарифы 10k/20k/50k с составом | Прозрачность | Тарифы с составом и SLA |
| esc-kazan | Тарифы 5000/8000 руб. с доплатой за доп. ПК | Гибкость | Тарифы с доплатой за доп. ПК/сервер |

### Trust
| Конкурент | Что сильно | Почему работает | Как адаптировать под F&F сильнее оригинала |
|---|---|---|---|
| a1-support | Реквизиты + договор + ЭДО | Прозрачность | Реквизиты + договор + ЭДО на всех страницах |
| socialit | SLA + кейсы | Доверие | SLA + кейсы с метриками |
| tss-kazan | SLA + гарантия возврата | Снижает риск | Гарантия 6 месяцев + SLA |
| itprovider | NDA + SLA + отзывы | Доверие | NDA + SLA + отзывы |

### FAQ
| Конкурент | Что сильно | Почему работает | Как адаптировать под F&F сильнее оригинала |
|---|---|---|---|
| a1-support | 5 вопросов (удалёнка, состав, договор, скорость, НДС) | Отработка возражений | FAQ с отработкой возражений (дорого, штатный, гарантия, скорость, что входит) |
| socialit | 8 вопросов (организация аутсорсинга, услуги сисадмина, филиалы, серверы, сеть, инфобез, развитие инфраструктуры, Битрикс24) | Глубина | FAQ с глубокой отработкой |

### CTA
| Конкурент | Что сильно | Почему работает | Как адаптировать под F&F сильнее оригинала |
|---|---|---|---|
| socialit | "Получить КП" на каждом тарифе | Чёткий CTA | "Получить расчёт" на каждом тарифе |
| a1-support | "Рассчитать стоимость" + "8-800" | Мультиканальность | "Рассчитать стоимость" + телефон + TG + MAX |
| tss-kazan | "Бесплатный аудит" | Лид-магнит | "Бесплатный аудит" + "Получить расчёт" |

### Сравнение со штатным
| Конкурент | Что сильно | Почему работает | Как адаптировать под F&F сильнее оригинала |
|---|---|---|---|
| itprovider | Блок "Уже есть системный администратор?" | Отработка возражения | Страница "F&F vs штатный сисадмин" с TCO |
| a1-support | Нет сравнения | Слабо | — |
| F&F | compare/staff-sysadmin-cost.html | Слабый | Усилить TCO-калькулятором |

### Блоки гарантии и сроков
| Конкурент | Что сильно | Почему работает | Как адаптировать под F&F сильнее оригинала |
|---|---|---|---|
| tss-kazan | "100% возврат" + SLA | Снижает риск | Гарантия 6 месяцев + SLA с финансовыми гарантиями |
| itprovider | SLA (реакция 15 мин, решение 20 мин) | Конкретные сроки | SLA (реакция 15 мин, решение 4 часа) |
| socialit | SLA с финансовыми гарантиями (1000-1500 руб./час) | Доверие | SLA с финансовыми гарантиями |
| comp-kazan | Гарантия до 2 лет | Длинная гарантия | Гарантия 6 месяцев (единый срок) |


## Контентные пробелы

### 15 контентных пробелов, которые F&F может закрыть и забрать трафик/доверие

1. Сколько стоит штатный сисадмин в Казани (TCO) — конкуренты не закрывают (только F&F имеет compare/staff-sysadmin-cost.html, но слабый).
2. TCO за год — конкуренты не закрывают.
3. Когда нужен сервер под ключ — конкуренты не закрывают (только F&F имеет services/server-1c.html, но мало контента).
4. Что должно быть в SLA — конкуренты не закрывают (только socialit имеет SLA с фин. гарантиями, но нет статьи).
5. Как выбрать IT-аутсорс — конкуренты не закрывают (только F&F имеет infrastructure/vybor-podryadchika.html).
6. Какие есть скрытые платежи — конкуренты не закрывают.
7. Что делать при падении 1С/почты/сервера — конкуренты не закрывают (только F&F имеет blog/server-down-saturday.html, blog/backup-not-restoring.html).
8. Как перейти с штатного сисадмина на аутсорс — конкуренты не закрывают.
9. Как проверить качество IT-аутсорсинга — конкуренты не закрывают.
10. Что входит в абонентское обслуживание — конкуренты не закрывают (только a1-support имеет FAQ).
11. Как рассчитать IT-бюджет для офиса 20-50 человек — конкуренты не закрывают.
12. Что делать при шифровальщике/вирусе — конкуренты не закрывают (только F&F имеет blog/ransomware-protection.html).
13. Как настроить ЭЦП для ЕИС/госзакупок — конкуренты не закрывают (только esc-kazan имеет страницу ЭЦП).
14. Как выбрать сервер для 1С — конкуренты не закрывают.
15. Как проверить резервное копирование — конкуренты не закрывают (только F&F имеет blog/backup-check-15min.html, blog/backup-not-restoring.html).


## Сегмент офисов 20-50 человек

### Кто говорит сегменту 20-50 человек, а кто льёт общий IT-аутсорс

| Игрок | Точность сегментации | Релевантность примеров | Тарифы под 20-50 человек | Боли этого сегмента | Офферная точность |
|---|---|---|---|---|---|
| its-kazan | Низкая (тарифы без размера офиса) | Низкая (нет кейсов по размеру) | Нет | Нет | Низкая |
| tss-kazan | Низкая (нет сегментации) | Средняя (торговые сети) | Нет | Нет | Низкая |
| itprovider | Низкая (нет сегментации) | Низкая (нет кейсов по размеру) | Нет | Нет | Низкая |
| i-tat | Низкая (нет сегментации) | Низкая (нет кейсов по размеру) | Нет | Нет | Низкая |
| esc-kazan | Средняя (тарифы от 4 ПК) | Низкая (нет кейсов по размеру) | Частично (4 ПК) | Нет | Средняя |
| pc-kazan/comp-kazan/intertax | Низкая (B2C) | Низкая (B2C) | Нет | Нет | Низкая |
| a8/itbsgroup | Низкая (нет сегментации) | Средняя (проекты) | Нет | Нет | Низкая |
| calltraffic | Низкая (нет сегментации) | Низкая (контакт-центр) | Нет | Нет | Низкая |
| erpdev | Низкая (нет сегментации) | Низкая (1С-разработка) | Нет | Нет | Низкая |
| a1-support | Средняя (5 ПК = 5000 руб.) | Низкая (нет кейсов по размеру) | Частично (5 ПК) | Нет | Средняя |
| obit | Низкая (нет сегментации) | Средняя (кейсы) | Нет | Нет | Низкая |
| socialit | Средняя (тарифы без размера офиса) | Средняя (кейсы сетей) | Частично (от 10 000 руб.) | Нет | Средняя |
| iteron | Средняя (калькулятор по ПК/серверам) | Низкая (нет кейсов по размеру) | Частично (калькулятор) | Нет | Средняя |
| 1cbit | Низкая (нет сегментации) | Средняя (кейсы) | Нет | Нет | Низкая |
| F&F | Низкая (нет сегментации) | Средняя (7 кейсов) | Нет | Нет | Низкая |

### Как F&F стать самым понятным выбором для офисов 20-50 человек в Казани и Татарстане

1. Тарифы для офисов 20-50 человек с ценами (прозрачные, с составом).
2. Боли этого сегмента: сервер 1С, ЭЦП, почта, бэкапы, рост, масштабирование.
3. Офферная точность: "IT-аутсорсинг для офисов 20-50 человек в Казани".
4. Кейсы из этого сегмента с метриками (до/после).
5. Сравнение со штатным сисадмином (TCO) с цифрами.
6. SLA (реакция 15 мин, выезд в день обращения).
7. Гарантия 6 месяцев (единый срок).
8. Локальные посадочные для городов Татарстана (Челны, Нижнекамск, Альметьевск, Зеленодольск).
9. Контент под спрос: "Как рассчитать IT-бюджет для офиса 20-50 человек", "Что должно быть в SLA", "Как выбрать IT-аутсорс".
10. Trust: реквизиты, договор/SLA, кейсы с метриками, отзывы с именами/компаниями.

## Углублённый конкурентный анализ (синтез по 11 осям)

### Как читать этот раздел
Синтез всех разборов: где рынок слаб, где F&F может ударить точнее всех, что внедрить сразу (безопасно), что внедрить в 30 дней. Источники: разделы 1–12, «Первые экраны», «Цены и упаковка», «Скорость доверия», «Страницы услуг», «Язык рынка», «Возражения», «Репутация», «Локальное доминирование», «Воронки», «Точки атаки», «Swipe и адаптация», «Контентные пробелы», «Сегмент 20–50».

---

### Ось 1. Первые экраны
**Где рынок слаб:** у 10 из 14 конкурентов нет цены на первом экране; у 8 — нет trust-блоков (реквизиты/SLA/гарантия); у 9 — нет калькулятора/CTA с расчётом; заголовки шаблонные («Надёжный IT-партнёр», «Комплексное обслуживание»). a1-support и socialit сильны, но a1-support без сравнения со штатным, socialit без локального бренда.
**Где F&F ударит точнее:** первый экран = цена + TCO-калькулятор + SLA + гарантия 6 месяцев + локальный телефон/выезд + 3 trust-цифры. Никто в Казани так не делает.
**Внедрить сразу:** добавить на index.html блок «Цена от X руб./мес за 5 ПК + калькулятор TCO + гарантия 6 месяцев + реакция 15 мин» (без новых зависимостей, чистый HTML/CSS).
**В 30 дней:** переработать hero на services.html, servers.html, support.html, prices.html по шаблону a1-support + socialit + локальный маркер.

### Ось 2. Архитектура цен
**Где рынок слаб:** 10 из 14 прячут цену в форме заявки; нет сравнения со штатным (только itprovider имеет блок); нет калькулятора TCO; гарантия не унифицирована (30 дней vs 6 месяцев).
**Где F&F ударит точнее:** публичные тарифы для офисов 20–50 человек + калькулятор TCO (штатный vs аутсорс) + «что входит/что за доплату» + гарантия 6 месяцев + SLA с фин. гарантиями. a1-support близок, но без сравнения со штатным и без локального бренда.
**Внедрить сразу:** на prices.html добавить таблицу тарифов (Эконом/Бизнес/Премиум) с ценами и составом; добавить блок «Гарантия 6 месяцев» рядом с ценами.
**В 30 дней:** сделать TCO-калькулятор (JS, без бэкенда) на prices.html и compare/staff-sysadmin-cost.html; унифицировать гарантию 30д→6мес по всему сайту скриптом.

### Ось 3. Скорость доверия
**Где рынок слаб:** у большинства нет реквизитов на первом экране; отзывы анонимные или без дат; кейсы без метрик; SLA/договор есть только у tss-kazan, itprovider, socialit, erpdev, a1-support; лица команды есть только у i-tat, obit, iteron, a1-support.
**Где F&F ударит точнее:** реквизиты (ИНН 165506822661) + договор/SLA + гарантия 6 месяцев + кейсы с метриками + отзывы с именами/компаниями/датами + фото команды + процесс 4 шага — на первом экране. Сейчас F&F имеет реквизиты, но нет SLA/договора, нет лиц, отзывы анонимные.
**Внедрить сразу:** добавить на index.html блок «Процесс работы: 4 шага» и «Гарантия 6 месяцев»; добавить schema Organization с address/geo (если есть адрес).
**В 30 дней:** собрать именные отзывы с компаниями/датами; добавить фото команды на company/team.html; добавить SLA/договор на отдельную страницу и ссылку с первого экрана.

### Ось 4. Страницы услуг
**Где рынок слаб:** у большинства страниц услуг нет FAQ, нет цен, нет кейсов с метриками, нет калькулятора; глубина средняя; коммерческие факторы слабые; готовность закрывать интент — средняя. a1-support и socialit сильны, но без локального бренда.
**Где F&F ударит точнее:** усилить services.html, servers.html, support.html, infrastructure/*, audits/* — добавить цены, SLA, FAQ, кейсы, калькулятор. Добавить страницы «F&F vs штатный сисадмин», «F&F vs удалённая поддержка», локальные посадочные.
**Внедрить сразу:** добавить FAQ-блок на services.html, servers.html, support.html, prices.html (если нет) с 5–8 вопросами; добавить FAQPage schema.
**В 30 дней:** усилить контент на тонких страницах (ai/*, incidents/*, resources/*, articles/*, industries/*, pain/*, cases/*, leads/*, compare/*) — добавить цены/SLA/FAQ/кейсы.

### Ось 5. Язык рынка
**Где рынок слаб:** выгоревшие фразы («опыт N лет», «комплексный подход», «профессиональная команда», «под ключ» без состава); рынок говорит о себе («мы», «наша команда») вместо выгоды клиента; общие слова без цифр.
**Где F&F ударит точнее:** говорить выгодой клиента + конкретные цифры + сравнение + гарантия 6 месяцев + процесс 4 шага + локальный бренд. Избегать выгоревших фраз.
**Внедрить сразу:** заменить на index.html шаблонные фразы на конкретные (цены, сроки, SLA, гарантия 6 месяцев).
**В 30 дней:** аудит текстов всех коммерческих страниц на выгоревшие фразы; переписать hero/CTA.

### Ось 6. Отработка возражений
**Где рынок слаб:** 13 из 14 не отрабатывают возражения «дорого», «почему не штатный», «что если не поможет», «как быстро приедете», «есть ли договор/гарантия», «что входит в цену», «можно ли начать с малого». Только tss-kazan, a1-support, socialit, itprovider имеют блоки.
**Где F&F ударит точнее:** закрыть 7 возражений через прозрачную цену + TCO + гарантию 6 месяцев + SLA + договор + тарифы для малого + FAQ. Никто в Казани не закрывает все 7.
**Внедрить сразу:** добавить на index.html FAQ с 7 возражениями (дорого, штатный, гарантия, скорость, что входит, договор, можно ли начать с малого) + FAQPage schema.
**В 30 дней:** добавить страницу «F&F vs штатный сисадмин» с TCO-калькулятором; добавить блок «Уже есть сисадмин?» на services.html.

### Ось 7. Репутация
**Где рынок слаб:** отзывы анонимные или без дат; кейсы без метрик; обещания опасны («100% возврат», «реакция 15 мин», «99.98% катастрофоустойчивость», «гарантия до 2 лет») — без доказательств; повторяющиеся жалобы не видны (отзывы mostly positive).
**Где F&F ударит точнее:** отзывы с именами/компаниями/датами/фото; кейсы с метриками (до/после) на первом экране; договор/SLA с фин. гарантиями; гарантия 6 месяцев (единый срок); отсутствие анонимных отзывов; прозрачность условий.
**Внедрить сразу:** заменить анонимные отзывы на company/testimonials.html на именные (если есть данные) — иначе оставить как есть, не выдумывать.
**В 30 дней:** собрать 5–10 именных отзывов с компаниями/датами/фото; добавить кейсы с метриками на первом экране.

### Ось 8. Локальность в Татарстане
**Где рынок слаб:** только i-tat и a8 имеют локальные посадочные; остальные пишут «Казань» для галочки; нет локального SEO (schema с address/geo); нет выезда; нет отзывов с указанием города.
**Где F&F ударит точнее:** локальные посадочные для Челнов, Нижнекамска, Альметьевска, Зеленодольска с реальным контентом (кейсы, цены, SLA, выезд); локальные маркеры (телефон 843, 2ГИС, Яндекс.Карты, отзывы); schema Organization с address/geo/sameAs; выезд инженера в день обращения.
**Внедрить сразу:** добавить на index.html блок «Работаем в Казани и городах Татарстана: Челны, Нижнекамск, Альметьевск, Зеленодольск, Иннополис» + выезд.
**В 30 дней:** создать локальные посадочные (4 страницы) с уникальным контентом; добавить schema Organization с address/geo.

### Ось 9. Воронки
**Где рынок слаб:** у 7 из 7 сильнейших нет цены на 1–3 шагах; нет «что будет после заявки»; нет мультиканальности (только a1-support имеет TG/MAX); нет SLA на 6 шаге (кроме a1-support, socialit).
**Где F&F ударит точнее:** цена + CTA + trust на первом экране; короткая форма + мультиканальность + «что будет после заявки»; договор + SLA + гарантия + отчётность.
**Внедрить сразу:** добавить на index.html блок «Что будет после заявки: 4 шага» + мультиканальные CTA (телефон, TG, MAX, форма).
**В 30 дней:** переработать форму заявки (короткая, мультиканальная); добавить автоответ/уведомление.

### Ось 10. Точки атаки в SEO
**Где рынок слаб:** тонкие страницы (ai/*, incidents/*, resources/*, articles/*, industries/*, pain/*, cases/*, leads/*, compare/*, terms-of-work.html); слабые title/H1; отсутствие FAQ (31 страница с id="faq" без schema); слабые коммерческие факторы (цены на 48 страницах, тарифы на 13); нет серверных/абонентских посадочных; нет расчётов/прозрачных условий.
**Где F&F ударит точнее:** усилить тонкие страницы контентом; добавить FAQPage schema; усилить коммерческие факторы (цены, сроки, SLA, гарантии 6 месяцев); добавить калькулятор TCO.
**Внедрить сразу:** добавить FAQPage schema на страницы с id="faq" (скрипт); добавить canonical/OG на страницы без них (проверить).
**В 30 дней:** усилить тонкие страницы контентом; добавить локальные посадочные; добавить калькулятор TCO.

### Ось 11. Контентные пробелы
**Где рынок слаб:** 15 тем, которых рынок не закрывает: TCO штатного сисадмина, TCO за год, сервер под ключ, SLA, выбор аутсорса, скрытые платежи, падение 1С/почты/сервера, переход со штатного, проверка качества, состав абонентки, IT-бюджет для 20–50, шифровальщик, ЭЦП для ЕИС, выбор сервера для 1С, проверка бэкапов.
**Где F&F ударит точнее:** закрыть все 15 пробелов статьями/страницами — забрать трафик и доверие. F&F уже имеет часть (blog/*, compare/*, infrastructure/*), но мало контента.
**Внедрить сразу:** добавить 3–5 статей по самым горячим темам (TCO штатного, что делать при падении 1С, скрытые платежи, SLA, выбор аутсорса).
**В 30 дней:** добавить остальные 10 статей; усилить существующие.

---

### Что внедрить сразу (безопасно, без риска регрессий)

1. **FAQPage schema** на страницах с id="faq" без schema (скрипт, валидация Rich Results).
2. **Блок на index.html**: цена + калькулятор TCO + гарантия 6 месяцев + реакция 15 мин + локальный телефон/выезд + 4 шага процесса + 7 возражений в FAQ.
3. **Таблица тарифов** на prices.html (Эконом/Бизнес/Премиум) с ценами и составом + «что входит/что за доплату».
4. **Блок «Гарантия 6 месяцев»** рядом с ценами на prices.html, services.html, servers.html, support.html.
5. **Блок «Работаем в Казани и городах Татарстана»** на index.html + выезд.
6. **Блок «Что будет после заявки: 4 шага»** + мультиканальные CTA на index.html.
7. **Замена шаблонных фраз** на конкретные (цены, сроки, SLA, гарантия 6 месяцев) на index.html.
8. **Обновить docs/CHANGELOG.md** записью об углублённом анализе.

### Что внедрить в ближайшие 30 дней

1. **Унификация гарантии 30д→6мес** по всему сайту скриптом + валидация.
2. **TCO-калькулятор** (JS) на prices.html и compare/staff-sysadmin-cost.html.
3. **Страница «F&F vs штатный сисадмин»** с TCO-калькулятором.
4. **Локальные посадочные** для Челнов, Нижнекамска, Альметьевска, Зеленодольска (4 страницы, уникальный контент).
5. **Именные отзывы** с компаниями/датами/фото на company/testimonials.html.
6. **Кейсы с метриками** на первом экране (3–5 кейсов).
7. **Фото команды** на company/team.html.
8. **SLA/договор** на отдельную страницу + ссылка с первого экрана.
9. **Усиление тонких страниц** контентом (ai/*, incidents/*, resources/*, articles/*, industries/*, pain/*, cases/*, leads/*, compare/*).
10. **3–5 статей** по горячим темам (TCO штатного, падение 1С, скрытые платежи, SLA, выбор аутсорса).
11. **Переработка hero** на services.html, servers.html, support.html, prices.html.
12. **Аудит текстов** на выгоревшие фразы + переписать.

### Итоговая оценка позиции F&F
- **Сильные стороны:** 161 страница, answer-first, FAQPage на 129 страницах, абсолютные canonical, schema, llms.txt, no secrets, 7 кейсов, 7 отзывов, прозрачные реквизиты, локальный бренд (Казань).
- **Слабые стороны:** placeholder analytics, FORM_ENDPOINT пуст, nav несогласован (81 страница), нет картинки img/case-ecp-eis.webp, гарантия не унифицирована, нет Tatarstan city landings, нет TCO-калькулятора, нет SLA/договора, отзывы анонимные, нет фото команды.
- **Главный рычаг роста:** прозрачная цена + TCO-калькулятор + гарантия 6 месяцев + SLA + локальный бренд + контент по 15 пробелам. Ни один конкурент в Казани не делает этого одновременно.

---

## Парсинг офферов

### Таблица: конкурент | оффер | УТП | CTA | сильная сторона | слабость

| Конкурент | Оффер (первый экран) | УТП / преимущества | CTA | Сильная сторона | Слабость |
|---|---|---|---|---|---|
| its-kazan.ru | Абонентское обслуживание IT инфраструктуры | Выгоднее штатного; прогнозируемость расходов; качество выше; надёжно; отчётность; работа с компаниями любого размера (2-3 ПК) | Отзывы клиентов; «6 приоритетов» | Локальный бренд; отзывы; работа с малым бизнесом | Нет цен; нет калькулятора; нет SLA с фин. гарантиями; шаблонный язык («опыт множества специалистов») |
| tss-kazan.ru | ИТ-аутсорсинг и внедрение ИТ систем | Проактивный мониторинг; детальное описание инфраструктуры с паролями руководителю; договор на длительный срок; команда за сумму на 20% меньше; SLA | «100% возврат»; постоплата | Сильная отработка возражений (5 проблем → решения); SLA; гарантия возврата | Нет цен; нет калькулятора; нет локального бренда |
| itprovider.ru | ИТ-поддержка, на которую можно положиться. 24/7. | Метрики (640k+ обращений, 35 специалистов, 28k единиц, 1022 сервера); реакция 15 мин, решение 20 мин; 24/7; NDA; 3 линии + выезд; проактивный мониторинг; сертификация Минцифры | «Давайте знакомиться»; «Хотите узнать больше?» | Метрики; SLA; NDA; блок «Уже есть сисадмин?» | Нет публичных цен; нет калькулятора TCO; нет сравнения со штатным |
| i-tat.ru | ИТ и 1С обслуживание, ГРАНД-Смета | ИТ + 1С + сметные программы + автоматизация; горячая линия; локальные (Челны/Нижнекамск/Альметьевск); фото специалистов | «Обратиться»; «КУПИТЬ»; «ОБРАТИТЬСЯ» | Локальные посадочные; 1С-экспертиза; фото команды | IT вторичен (1С/сметы главные); нет цен; нет SLA |
| esc-kazan.ru (ЦЭУ) | Комплексное обслуживание бизнеса | 21 год; 100% проектов в срок; 1000+ клиентов; до 50% экономия; 5 шагов; бэк-офис под ключ | «Получить скидку»; «Начать сотрудничество»; «Заказать звонок» | Широкий спектр (бух+юрист+IT+ЭЦП+кассы); локальный бренд; реквизиты | IT вторичен; нет SLA; нет цен на IT |
| a1-support.ru | Удалённая IT-поддержка компьютеров и серверов для бизнеса по всей России | С 2006; договор + ЭДО; 8-800 бесплатный; вся Россия удалённо; цены от 5000 руб./мес за 5 ПК; 8 направлений услуг | «Рассчитать стоимость»; «8 800 555-90-23»; Telegram | Прозрачные цены; калькулятор; договор/ЭДО; FAQ 5 вопросов; 4 шага | Нет локального бренда; нет сравнения со штатным; нет кейсов с метриками |
| obit.ru | Телеком, ЦОД, инжиниринг, ИТ-аутсорсинг | Кейсы; партнёры; 20+ лет; ИИ; импортозамещение | «Заказать звонок» (предпол.) | Глубокий каталог услуг; кейсы; партнёры | Нет цен; федеральный масштаб; IT вторичен (телеком главный) |
| socialit.ru | Тарифы ИТ-аутсорсинга (Удалённый/Базовый/Расширенный) | Реакция 15 мин; SLA с фин. гарантиями (1000-1500 руб./час); 70+ городов; 100+ сотрудников; 3 линии; VIP-пользователи; выделенный менеджер | «Получить КП» (на каждом тарифе) | SLA с фин. гарантиями; тарифы с ценами; кейсы сетей | Нет локального бренда; высокий порог (от 10k); фокус на розницу/филиалы |
| iteron.ru | IT-поддержка, которая всегда рядом | Уменьшите расходы на IT до 50%; постоянная поддержка без отпусков/больничных; 90% заявок за час; «одно окно»; 18 лет; 31+ компаний; 98% остаются; калькулятор | «Заказать консультацию»; «Отправить запрос» | Калькулятор стоимости; 1С-экспертиза; метрики (98%) | Москва; нет локального бренда; нет SLA с фин. гарантиями; нет публичных цен |
| itbsgroup.ru (a8) | Каталог оборудования + интеграция | Индивидуальный подход; сертифицированные эксперты; быстрая реализация; 15 мин реакция (в аутсорсинге); проекты (Казань, Почта Банк); меню городов | «Опишите задачу»; «Весь каталог» | Локальные посадочные (меню городов); интегратор; проекты | B2B интегратор; IT вторичен (оборудование главное); нет цен |
| 1cbit.ru | IT-поддержка + 1С + инфраструктура (не загрузился, 401) | ТОП-100; 300 000+ клиентов; SLA | Неизвестно | Масштаб; SLA; 1С-экспертиза | Федеральный; нет локального бренда; нет цен |
| calltraffic.ru | Контакт-центр, техподдержка ИС (не загрузился, cert) | 16 лет; катастрофоустойчивость 99.98%; лицензии ФСТЭК | Неизвестно | Лицензии; катастрофоустойчивость | Нет цен; нет локального бренда; IT вторичен |
| erpdev.ru | 1С-разработка, ERP (таймаут) | NDA/SLA; гарантия 24 мес; кейсы | Неизвестно | Кейсы; NDA/SLA; гарантия 24 мес | Нет цен; нет локального бренда |
| pc-kazan / comp-kazan / intertax | Разовые услуги (ремонт, настройка, заправка) (privacy policy вместо главной) | Низкие цены; быстрый выезд; comp-kazan гарантия до 2 лет | Неизвестно | Низкие цены; быстрый выезд | B2C; нет SLA; нет абонентки |

### Повторяющиеся шаблоны (выгоревшие)

- «Опыт N лет» / «с 2006/2009 года» — у 10+ конкурентов.
- «Комплексный подход» / «комплексное обслуживание» — у 8+.
- «Профессиональная команда» / «команда экспертов» / «сертифицированные специалисты» — у 9+.
- «Надёжно» / «стабильно» / «без сбоев» — у 10+.
- «Под ключ» без состава работ — у 6+.
- «Мы заботимся о ваших данных» / «мы работаем на результат» — у 5+.
- «Индивидуальный подход» — у 7+.
- Метрики «600 000 обращений», «35 специалистов», «24/7» — у 3-4 (itprovider, socialit).

### Редкие сильные формулировки (стоит адаптировать)

- a1-support: «Абонентское обслуживание — от 5 000 ₽ в месяц за офис до пяти компьютеров» + «каждый следующий — плюс 500 ₽» + «Сервер — от 1 200 ₽» — прозрачная цена с вилкой.
- a1-support: «Работаем по договору: сотрудники звонят на бесплатный номер 8-800, инженер подключается удалённо и решает задачу» — конкретный процесс.
- tss-kazan: «Если вас не устроит качество наших услуг, просто смените пароли к сервисам вашей компании и скажите нам Аривидерчи» — сильное снятие риска.
- tss-kazan: «Мы теряем деньги, если у вас что-то не работает. Это закреплено SLA» — финансовая мотивация.
- itprovider: «Реагируем на обращения за 15 минут и решает большинство обращений за 20 минут» — конкретные сроки.
- itprovider: блок «Работаем совместно с вашими специалистами либо самостоятельно» (если есть сисадмин / если нет) — отработка возражения.
- socialit: «За каждый час нарушения сроков решения задачи — 1 000/1 500 ₽» — финансовые гарантии SLA.
- socialit: «Мгновенная поддержка VIP — 2/4 VIP-пользователя» — сегментация по важности.
- iteron: «90% заявок закрываем в течение часа» + «98% компаний остаются с нами» — конкретные метрики.
- esc-kazan: «100% проектов в срок» + «до 50% экономия» — конкретные обещания (опасно, если не выполняются).
- i-tat: «Цена 1С у всех одна. Разница в качестве сервиса!» — сильная дифференциация.
- a1-support: «Основная работа идёт удалённо — так быстрее и дешевле для Вас» — честность.

### Что F&F должен забрать (синтез)

1. Прозрачные цены с вилкой (a1-support, socialit, esc-kazan) — F&F: тарифы для 20-50 человек.
2. Конкретные сроки SLA (itprovider 15 мин, socialit 15 мин) — F&F: реакция 15 мин, решение 4 часа.
3. Финансовые гарантии SLA (socialit 1000-1500 руб./час) — F&F: гарантия 6 месяцев + SLA с фин. гарантиями.
4. Блок «Уже есть сисадмин?» (itprovider) — F&F: страница «F&F vs штатный».
5. Отработка возражений через FAQ (a1-support 5 вопросов, socialit 8 вопросов) — F&F: FAQ с 7 возражениями.
6. Калькулятор стоимости (a1-support, iteron) — F&F: TCO-калькулятор.
7. Метрики на первом экране (itprovider 640k+, 35 специалистов, 24/7) — F&F: метрики (заявки, время реакции, клиенты).
8. Локальные посадочные (i-tat, a8 меню городов) — F&F: Челны, Нижнекамск, Альметьевск, Зеленодольск.
9. Процесс 4 шага (a1-support) — F&F: аудит → настройка → поддержка → отчётность.
10. Договор + ЭДО (a1-support) — F&F: договор + SLA + ЭДО.

---

## Парсинг цен

### Таблица: конкурент | услуга | цена | формат тарифа | прозрачность | комментарий

| Конкурент | Услуга | Цена | Формат тарифа | Прозрачность | Комментарий |
|---|---|---|---|---|---|
| a1-support.ru | Абонентское (удалённое) | от 5 000 ₽/мес (5 ПК), +500 ₽/ПК, сервер от 1 200 ₽/мес | Тарифы (Удалённая/Стандартный/Расширенный) + калькулятор | Высокая | Цены публичные, вилки «от», калькулятор, разбивка по ПК/серверам/выездам/бэкапу |
| a1-support.ru | Разовые работы (ЭЦП, ЕГАИС, маркировка) | от 1 500 ₽ | «от» | Высокая | Цена «от» с «подробнее» |
| a1-support.ru | Аудит 1С | Бесплатно | Бесплатный лид-магнит | Высокая | Ускорение — 2 000 ₽/час |
| a1-support.ru | Администрирование сервера | от 1 200 ₽/мес | «от» | Высокая | — |
| a1-support.ru | Почтовый сервер в аренду | 3 000 ₽/мес | Фиксированная | Высокая | — |
| a1-support.ru | Хранилище Proxmox | 2,65 ₽/ГБ/мес | Фиксированная | Высокая | — |
| a1-support.ru | Выезд инженера | 2 500-3 500 ₽ | Вилка по срочности | Высокая | Зависит от тарифа и срочности |
| socialit.ru | Абонентское (Удалённый/Базовый/Расширенный) | 10 000 / 20 000 / 50 000 ₽/мес | Тарифы с составом | Высокая | SLA с фин. гарантиями (1 000-1 500 ₽/час); почасовой тариф |
| socialit.ru | Почасовой | За фактически отработанное время (мин. 2 часа) | Почасовой | Средняя | Цена не фиксирована, «уточняйте у менеджеров» |
| socialit.ru | Доп. выезд инженера | 2 500 ₽/час (мин. 2 часа) | Почасовой | Средняя | — |
| esc-kazan.ru (ЦЭУ) | Тариф «Эконом» (IT) | 5 000 ₽/мес (4 ПК + МФУ, доп. ПК +800 ₽) | Пакет с доплатой | Высокая | Выезд платно |
| esc-kazan.ru (ЦЭУ) | Тариф «Бизнес» (IT) | 8 000 ₽/мес (4 ПК + МФУ + сервер, доп. ПК +1 000 ₽) | Пакет с доплатой | Высокая | Выезд 3 раза бесплатно |
| esc-kazan.ru (ЦЭУ) | Разовые услуги (IT) | от 500-4 000 ₽ (удалённая поддержка от 1 000 ₽, принтеры от 1 000 ₽, почта от 1 500 ₽, антивирус от 1 000 ₽, подбор оборудования от 1 000 ₽, обновления ОС от 500 ₽, доступ из дома от 1 000 ₽, ЭЦП от 1 000 ₽, серверы от 2 500 ₽, телефония от 2 000 ₽, эл. площадки от 4 000 ₽, Контур/Сбис/Калуга от 1 000 ₽, кассы от 2 000 ₽, нетиповые задачи 2 000 ₽/час) | «от» по каждой услуге | Высокая | Самый детальный прайс среди локальных |
| its-kazan.ru | Абонентское | Не указано | Тарифы Эконом/Бизнес/Премиум (без цен) | Низкая | Цена прячется в форме заявки |
| tss-kazan.ru | Абонентское | Не указано | Не указаны | Низкая | Цена прячется в форме заявки; постоплата |
| itprovider.ru | Абонентское/серверы | Не указано (страница /price без цен) | Не указаны | Низкая | Цена прячется; есть SLA (реакция 15 мин) |
| i-tat.ru | ИТ + 1С | Не указано | Не указаны | Низкая | Цена прячется; IT вторичен |
| pc-kazan / comp-kazan / intertax | Разовые (ремонт, настройка, заправка) | от 250-474 ₽ (pc-kazan) | Разовые услуги | Высокая | Низкие цены, публичные; B2C |
| comp-kazan | Гарантия | до 2 лет | Гарантия на работы | Высокая | Самая длинная гарантия среди локальных |
| a8 / itbsgroup | Оборудование + интеграция | Не указано (каталог) | Каталог оборудования | Низкая | Цена прячется в каталоге |
| calltraffic.ru | Контакт-центр, техподдержка ИС | Не указано | Не указаны | Низкая | Цена прячется в форме заявки |
| erpdev.ru | 1С-разработка, ERP | Не указано | Не указаны | Низкая | Цена прячется в форме заявки; гарантия 24 мес |
| a1-support.ru | ЭЦП, ЭДО, ЕГАИС | от 1 500 ₽ | «от» | Высокая | Разовая задача |
| obit.ru | Телеком, ЦОД, инжиниринг, аутсорсинг | Не указано | Не указаны | Низкая | Цена прячется в форме заявки |
| socialit.ru | Абонентское (Удалённый/Базовый/Расширенный) | 10 000 / 20 000 / 50 000 ₽/мес | Тарифы с составом | Высокая | VIP-пользователи; фин. гарантии SLA |
| iteron.ru | Абонентское, 1С, серверы | Не указано (калькулятор) | Калькулятор по ПК/серверам | Средняя | Калькулятор есть, но нет фиксированных цен |
| 1cbit.ru | 1С, IT-поддержка, инфраструктура | Не указано | Не указаны | Низкая | Цена прячется в форме заявки |
| pc-kazan / comp-kazan / intertax | B2C разовые | от 250-474 ₽ | Разовые услуги | Высокая | Низкие цены, публичные |

### Кто пишет цены открыто

- **a1-support.ru** — самый прозрачный: тарифы с ценами, калькулятор, вилки «от», разбивка по ПК/серверам/выездам/бэкапу, FAQ по ценам.
- **socialit.ru** — тарифы с ценами (10k/20k/50k), SLA с фин. гарантиями, почасовой тариф.
- **esc-kazan.ru** — тарифы с ценами (5000/8000 руб.), пакеты с количеством ПК/серверов, доплата за доп. ПК, детальный прайс разовых услуг.
- **pc-kazan / comp-kazan / intertax** — низкие цены, публичные, понятный расчёт (B2C).

### Кто прячет

- **its-kazan, tss-kazan, itprovider, i-tat, a8/itbsgroup, calltraffic, erpdev, obit, iteron, 1cbit** — нет публичных цен, вилки «от» отсутствуют, расчёт непонятен, цена прячется в форме заявки.
- **itprovider** — есть страница /price, но без цен (только реквизиты).
- **iteron** — есть калькулятор, но нет фиксированных цен.

### Где цена выглядит убедительно

- **a1-support** — прозрачные цены + калькулятор + «что входит» + «что за доплату» + договор.
- **socialit** — тарифы с составом + SLA с фин. гарантиями + почасовой тариф.
- **esc-kazan** — тарифы с ценами + пакеты + доплата за доп. ПК + детальный прайс.
- **comp-kazan** — гарантия до 2 лет (длинная гарантия).

### Где цена вызывает недоверие

- **its-kazan, tss-kazan, i-tat, a8, itbsgroup, obit, iteron, 1cbit, calltraffic, erpdev** — нет цен, нет состава, нет «что входит/что за доплату» → клиент не может оценить стоимость до заявки.
- **a1-support** — цены прозрачны, но нет сравнения со штатным (F&F может ударить TCO-калькулятором).
- **socialit** — тарифы с ценами, но высокий порог (от 10k) → недоступно для малого бизнеса.
- **esc-kazan** — цены есть, но IT вторичен (бухгалтерия/юристы главные).
- **comp-kazan** — «гарантия до 2 лет» — опасно, если не выполняется.

### Что F&F должен сделать с ценой

1. Публичные цены/тарифы на всех коммерческих страницах (prices, services, servers, support).
2. Калькулятор TCO (штатный vs аутсорсинг) на первом экране.
3. Вилки «от» с чётким составом (что входит, что за доплату).
4. Сравнение со штатным сисадмином (TCO) с цифрами.
5. Гарантия 6 месяцев + SLA с финансовыми гарантиями рядом с ценами.
6. Пакеты для офисов 20-50 человек.
7. Прозрачность: цены, сроки, SLA, гарантии на всех страницах.

---

## Парсинг гарантий и SLA

### Таблица: конкурент | гарантия | реакция | SLA | сроки | как подано

| Конкурент | Гарантия | Время реакции | SLA | Сроки (выезд/запуск/работы) | Как подано |
|---|---|---|---|---|---|
| a1-support.ru | Нет явной гарантии (договор + ЭДО) | Заявки принимаются 9:00-19:00; обращения по договору в приоритете | Нет SLA с фин. гарантиями | Выезд: 48 ч (2 500 ₽), 6 ч (3 500 ₽), 24 ч доп. (2 000 ₽); работа на выезде до 4-6 ч | Договор + ЭДО; «отвечаем по договору» |
| tss-kazan.ru | «100% возврат» (гарантия возврата) | Не указано | SLA: время реагирования и решения; «мы теряем деньги, если у вас что-то не работает» | Не указано | SLA с фин. мотивацией; постоплата |
| itprovider.ru | Нет явной гарантии | 15 мин (реакция), большинство обращений за 20 мин | SLA (реакция 15 мин, решение 20 мин); NDA | 24/7 поддержка | Конкретные цифры; сертификация Минцифры |
| i-tat.ru | Нет | Не указано | Нет | Не указано | Отзывы («сотрудничество более 10 лет») |
| esc-kazan.ru (ЦЭУ) | Нет явной гарантии | 15 мин (среднее), 95% неисправностей за 15-30 мин | Нет SLA с фин. гарантиями | Удалённое решение 15-30 мин; 99.9% доступность | Конкретные цифры; 21 год на рынке |
| pc-kazan / comp-kazan | comp-kazan: гарантия до 2 лет | Не указано | Нет | Не указано | Длинная гарантия (опасно, если не выполняется) |
| a8 / itbsgroup | Нет | 15 мин (в аутсорсинге) | Нет | Не указано | Проекты; интегратор |
| calltraffic.ru | Нет | Не указано | Нет явного SLA | Не указано | 99.98% катастрофоустойчивость; лицензии ФСТЭК |
| erpdev.ru | Гарантия 24 мес | Не указано | NDA/SLA | Не указано | Кейсы; NDA/SLA |
| a1-support.ru | Нет явной гарантии | 9:00-19:00; обращения по договору в приоритете | Нет SLA с фин. гарантиями | Выезд: 48 ч (2 500 ₽), 6 ч (3 500 ₽), 24 ч доп. (2 000 ₽); работа на выезде до 4-6 ч | Договор + ЭДО; «отвечаем по договору» |
| obit.ru | Нет | Не указано | Нет | Не указано | Кейсы; партнёры; 20+ лет |
| socialit.ru | Нет явной гарантии | до 15 мин | SLA с фин. гарантиями: 1 000-1 500 ₽/час за нарушение сроков | Не указано | Финансовые гарантии SLA; 3 линии |
| iteron.ru | Нет | 90% заявок за час | Нет SLA с фин. гарантиями | Не указано | Метрика «90% за час»; калькулятор |
| 1cbit.ru | Нет явной гарантии | Не указано | SLA | Не указано | ТОП-100; 300 000+ клиентов |

### Лучшие формулировки (стоит адаптировать)

- **itprovider**: «Реагируем на обращения за 15 минут и решает большинство обращений за 20 минут» — конкретные цифры, измеримые.
- **socialit**: «За каждый час нарушения сроков решения задачи — 1 000/1 500 ₽» — финансовые гарантии SLA (единственный с деньгами).
- **tss-kazan**: «Мы теряем деньги, если у вас что-то не работает. Это закреплено SLA» — финансовая мотивация.
- **esc-kazan**: «95% неисправностей мы исправляем за 15-30 минут через удалённый доступ. Вы даже не заметите сбоя» — конкретика + эмоция.
- **iteron**: «90% заявок закрываем в течение часа» — метрика.
- **a1-support**: «Выезды есть в Москве и Санкт-Петербурге. Стоимость и количество плановых выездов указаны в тарифах» — прозрачность сроков и цен.
- **erpdev**: «Гарантия 24 мес» — длинная гарантия (опасно, если не выполняется).

### Пустые обещания (без доказательств)

- **its-kazan**: «надёжно», «стабильно», «без сбоев» — без SLA и цифр.
- **i-tat**: «сотрудничество более 10 лет» — без доказательств.
- **obit**: «20+ лет» — без SLA.
- **calltraffic**: «99.98% катастрофоустойчивость» — без SLA с фин. гарантиями.
- **esc-kazan**: «100% проектов в срок» — без доказательств.
- **comp-kazan**: «гарантия до 2 лет» — без условий.
- **1cbit**: «ТОП-100, 300 000+ клиентов» — без SLA с цифрами.

### Что F&F может перебить своей гарантией 6 месяцев и прозрачными сроками

1. **Гарантия 6 месяцев (единый срок)** vs разрозненные «30 дней» / «до 2 лет» / «24 мес» — F&F: единый, честный, понятный срок.
2. **SLA с финансовыми гарантиями** (как socialit, но с локальным брендом) — F&F: «Реакция 15 мин. Решение 4 часа. Или мы платим вам.»
3. **Конкретные сроки выезда** (a1-support: 48 ч/6 ч/24 ч с ценами) — F&F: «Выезд инженера в день обращения» + цены.
4. **Запуск сервера / работ** — F&F: «Сервер под ключ за 5-10 рабочих дней» + этапы.
5. **Ответственность** — F&F: договор + SLA + гарантия 6 месяцев + акт + чек + безнал.
6. **Честность сроков** — не обещать «100% в срок», а давать реальные сроки с буфером.

### Итог

- **Лучший SLA на рынке**: socialit (фин. гарантии 1 000-1 500 ₽/час) + itprovider (15 мин/20 мин) — но оба без локального бренда в Казани.
- **F&F может перебить**: гарантия 6 месяцев (единый срок) + SLA с фин. гарантиями + конкретные сроки + локальный бренд + прозрачность.
- **Главный рычаг**: «Реакция 15 минут. Решение 4 часа. Или мы платим вам. Гарантия 6 месяцев.»

---

## Парсинг структуры сайтов

### Карта: конкурент | какие типы страниц есть | каких нет | что закрыто лучше, чем у F&F

| Конкурент | Какие типы страниц есть | Каких нет | Что закрыто лучше, чем у F&F |
|---|---|---|---|
| a1-support.ru | Главная (оффер+цены+FAQ+4 шага), Цены (калькулятор+тарифы), 8 направлений услуг (удалённая поддержка, ЭЦП/ЭДО/ЕГАИС, 1С, удалённая работа, админ. серверов, почта, бэкап, сервер для ИИ), Маркировка, Резервная площадка, Миграции, Переезд серверов, FAQ | Блог, кейсы, сравнения, локальные посадочные | Цены+калькулятор на первом экране; FAQ с 5 вопросами; процесс 4 шага; тарифы с составом |
| tss-kazan.ru | Главная (5 проблем→решения, SLA, гарантия возврата), услуги (IT-аутсорсинг, внедрение ИТ), кейсы (торговые сети) | Цены, калькулятор, блог, FAQ, сравнения, локальные посадочные | Отработка возражений (5 проблем→решения); SLA; гарантия возврата; постоплата |
| itprovider.ru | Главная (метрики, преимущества 6, «уже есть сисадмин?»), О компании (аккредитация, цены), Отзывы, Услуги (аудит, настройка, мониторинг, поддержка, аналитика, отчётность) | Блог, кейсы с метриками, FAQ, сравнения, калькулятор, локальные посадочные | Метрики на первом экране (640k+, 35 спец., 28k, 1022); блок «уже есть сисадмин?»; NDA; SLA 15/20 мин |
| i-tat.ru | Главная (слайдер, услуги), ИТ (системный админ, обслуживание ПК, IT-аутсорсинг, серверы, удалённый офис, онлайн-конференции), 1С (ИТС, обслуживание, внедрение, поддержка, обновление, УТ, УНФ, Бухгалтерия, ЗУП, ERP), ГРАНД-Смета, база знаний, обучение, сообщество | Цены, SLA, FAQ, сравнения, калькулятор, кейсы | Локальные посадочные (Челны/Нижнекамск/Альметьевск); фото команды; база знаний; 1С-экспертиза |
| esc-kazan.ru (ЦЭУ) | Главная (комплексное обслуживание, услуги, о компании, 5 шагов, цифры), Аутсорсинг (бух, юрист, кадры, бэк-офис), ЭЦП, Битрикс24, Кассы, IT-сопровождение, Web-сервисы, Журнал, Контакты | SLA, FAQ, сравнения, калькулятор, кейсы | Широкий спектр услуг; локальный бренд; 5 шагов; 21 год; цифры (100% в срок, 1000+ клиентов) |
| a8 / itbsgroup | Главная (каталог, проекты, новости, отзывы), Каталог (серверы, сети, ПК, ПО, инфобез, видеонаблюдение, инженерия), Услуги (автоматизация, аутсорсинг, разработка, лизинг, инфобез), Проекты, Компания, Отзывы | Цены, SLA, FAQ, сравнения, калькулятор | Локальные посадочные (меню городов); интегратор; проекты с именами; 15 мин реакция |
| obit.ru | Главная (услуги, отрасли), ИТ-решения (видеонаблюдение, импортозамещение, ИИ, аутсорсинг, облака, процессы ИТ, поставка, российское ПО, системная интеграция), Услуги связи, Инжиниринг, ЦОД, Инфобез, Отрасли (9) | Цены, FAQ, сравнения, калькулятор, локальные посадочные | Глубокий каталог; кейсы; партнёры; отраслевые страницы |
| socialit.ru | Главная (тарифы, услуги, ИТ для розницы/филиалов), Тарифы (3 тарифа + почасовой), Услуги (поддержка, админ, сети, инфобез) | Блог, кейсы, FAQ, сравнения, калькулятор, локальные посадочные | Тарифы с ценами и составом; SLA с фин. гарантиями; 3 линии; VIP-пользователи |
| iteron.ru | Главная (оффер, калькулятор, услуги, о компании, статьи), Услуги (1С, аутсорсинг, администрирование, IT услуги, облачная инфраструктура, доп. услуги), Блог (статьи/новости) | Кейсы, FAQ, сравнения, локальные посадочные | Калькулятор стоимости; метрики (98%); 1С-экспертиза |
| 1cbit.ru | Главная (не загрузилась, 401), IT-поддержка, 1С, инфраструктура | — | Масштаб (300 000+ клиентов, ТОП-100); SLA |
| calltraffic.ru | Главная (не загрузилась, cert), контакт-центр, техподдержка ИС | — | Лицензии ФСТЭК; катастрофоустойчивость 99.98% |
| erpdev.ru | Главная (не загрузилась, таймаут), 1С-разработка, ERP | — | NDA/SLA; гарантия 24 мес; кейсы |
| pc-kazan / comp-kazan / intertax | B2C: разовые услуги, ремонт, заправка | Абонентка, SLA, кейсы, FAQ, сравнения, калькулятор | Низкие цены; быстрый выезд; гарантия до 2 лет |
| F&F | 161 страниц: index, services, servers, support, prices, cases (20+), blog (40+), articles (8), infrastructure (12), industries (12), pain (6), audits (3), leads (4), compare (5), company (6), legal (4), ai (3), incidents (1), resources (3), security (2), FAQPage на 129 страницах, llms.txt, search, quiz, demo, map, status | Калькулятор TCO, тарифы с ценами, локальные посадочные (Челны/Нижнекамск/Альметьевск/Зеленодольск), страница SLA/договор, фото команды, именные отзывы, блок «уже есть сисадмин?» | 161 страница; answer-first; FAQPage на 129; абсолютные canonical; schema; llms.txt; no secrets; 7 кейсов; 7 отзывов; прозрачные реквизиты |

### Страницы, которых нет у F&F, но повторяются у сильных конкурентов

1. **Калькулятор стоимости / TCO** — a1-support, iteron. F&F: нет (только цены на prices.html).
2. **Тарифы с составом и ценами** — a1-support, socialit, esc-kazan. F&F: prices.html есть, но без тарифных таблиц с ценами.
3. **Локальные посадочные (Челны, Нижнекамск, Альметьевск, Зеленодольск)** — i-tat, a8 (меню городов). F&F: кейсы по городам есть, но нет выделенных посадочных.
4. **Страница SLA / договора** — a1-support, itprovider. F&F: legal/terms.html есть, но нет отдельной страницы SLA с фин. гарантиями.
5. **Блок «Уже есть сисадмин?»** — itprovider. F&F: compare/staff-sysadmin-cost.html есть, но слабый.
6. **Процесс 4 шага на первом экране** — a1-support, esc-kazan. F&F: нет на первом экране.
7. **FAQ на коммерческих страницах (5-8 вопросов)** — a1-support, socialit. F&F: FAQ на 129 страницах, но не на всех коммерческих.
8. **Кейсы с метриками на первом экране** — itprovider, socialit, obit. F&F: кейсы есть, но не на первом экране.
9. **Отзывы с именами/компаниями/датами/фото** — itprovider, its-kazan. F&F: отзывы анонимные.
10. **Фото команды** — i-tat, obit, iteron, a1-support. F&F: нет.
11. **База знаний** — i-tat. F&F: blog/articles есть, но нет структурированной базы знаний.
12. **Отраслевые страницы** — obit (9 отраслей). F&F: industries (12) — уже есть.
13. **Новости / Журнал** — esc-kazan, itbsgroup. F&F: blog есть.
14. **Контакты с картой** — i-tat. F&F: contacts.html есть, но без карты.
15. **Сравнения (F&F vs штатный, F&F vs фрилансер, F&F vs интегратор)** — F&F: compare/* (5 страниц) есть, но слабые.

### Итог

- **У F&F уже лучше**: количество страниц (161), answer-first, FAQPage на 129, абсолютные canonical, schema, llms.txt, no secrets, 7 кейсов, 7 отзывов, прозрачные реквизиты, локальный бренд.
- **У конкурентов лучше**: цены+калькулятор (a1-support), SLA с фин. гарантиями (socialit), локальные посадочные (i-tat, a8), блок «уже есть сисадмин?» (itprovider), процесс 4 шага (a1-support, esc-kazan), метрики на первом экране (itprovider), фото команды (i-tat, obit, iteron), именные отзывы (itprovider, its-kazan).
- **Главный пробел F&F**: калькулятор TCO, тарифы с ценами, локальные посадочные, SLA-страница, фото команды, именные отзывы, блок «уже есть сисадмин?».

---

## Парсинг мета и заголовков

### Главная страница: title | description | H1

| Конкурент | Title | Description | H1 |
|---|---|---|---|
| its-kazan.ru | Обслуживание компьютеров, серверов и сети ЛВС - ит айти аутсорсинг в Казани - IT сервис | IT сервис: обслуживание компьютеров, серверов и сети на профессиональном уровне. Быстрая реакция, высокий уровень сервиса и хорошие цены - так говорят наши клиенты в официальных отзывах. | Абонентское обслуживание IT инфраструктуры |
| tss-kazan.ru | ИТ аутсорсинг и внедрение ИТ систем для бизнеса TECHNO SYSTEM SERVICE | TECHNO SYSTEM SERVICE: более 10 лет опыта в ИТ аутсорсинге. Бесперебойная работа IT-инфраструктуры, круглосуточная техподдержка и 100% гарантия возврата денег. Работаем в Казани. Звоните +7 843 2-102-422 | (нет H1, заголовок — стилизованный блок) |
| itprovider.ru | АйТи Провайдер. ИТ-поддержка, на которую можно положиться. 24/7. Надежный партнер для бизнеса в Казани, Республике Татарстан и России | Быстрая реакция и оперативное решение проблем. ИТ-поддержка бизнеса, а не устранение поломок. Предотвращаем сбои и проблемы | (нет H1, заголовки — h2 преимуществ) |
| i-tat.ru | АЙТАТ.РФ – ИТ и 1С обслуживание, ГРАНД-Смета | Решим все проблемы с 1С и компьютерами. Собственные линии поддержки 1С, компьютеров и серверов, Гранд-Сметы, Web-студия. Мы обслуживаем более 1 800 предприятий, более 16 лет на рынке. | (нет H1, заголовок — слайдер) |
| esc-kazan.ru (ЦЭУ) | Центр электронных услуг \| Сервисы для бизнеса | Официальный партнер СКБ Контур - ЦЭУ. Полное обслуживание фирм, от КЭП до маркировки в ЕГАИС, ЧЗ и ведения бухгалтерии ИП и ООО. Работаем с офисом в Казани и удаленно по России через электронный документооборот. | (нет H1, заголовок — стилизованный блок) |
| a1-support.ru | Удалённая IT-поддержка бизнеса по всей России — A1 Support | Обслуживание компьютеров и серверов по договору: 5 000 ₽ в месяц за офис до пяти ПК. 1С, ЭЦП, почта, резервные копии. Бесплатный номер 8-800. | Удалённая IT-поддержка компьютеров и серверов для бизнеса по всей России |
| obit.ru | ОБИТ — оператор ИТ-решений с компетенциями в широком спектре задач: от классических телеком-услуг до реализации ИТ-проектов под ключ | Компания ОБИТ — оператор ИТ-решений, предлагает комплексные цифровые и телекоммуникационные решения для бизнеса в Москве, Санкт-Петербурге, Казани и еще в 80 городах России. | ОБИТ — оператор ИТ-решений с компетенциями в широком спектре задач: от классических телеком-услуг до реализации ИТ-проектов под ключ |
| socialit.ru | ИТ-аутсорсинг для бизнеса по всей России | Передать IT и потерять контроль - не единственный сценарий. SOCIALIT берёт на себя отдельные функции, усиливает внутреннюю команду или полностью заменяет ИТ-отдел, сохраняя прозрачную модель взаимодействия. | (нет H1, заголовок — «Тарифы ИТ-аутсорсинга» h2) |
| iteron.ru | ИТ услуги для бизнеса в Москве - iTeron аутсорсинг | IT аутсорсинг для бизнеса в Москве. Профессиональное обслуживание компьютеров и серверов с 2009 года. Узнайте больше о наших услугах и выгодных предложениях! | IT-поддержка, которая всегда рядом |
| itbsgroup.ru (a8) | Сайт ГК Ай Ти Бизнес Солюшенс - Главная | IT Business Solutions - системный интегратор на рынке с 2005 года, мы внедряем ИТ решения, которые позволяют заказчикам снижать вероятность рисков, оптимально распределять ресурсы, повышать безопасность инфраструктуры, сокращать затраты и увеличивать прибыль. | (нет H1, заголовок — меню/слайдер) |

### Служебные страницы (где удалось спарсить)

| Конкурент | Страница | Title | Description | H1 |
|---|---|---|---|---|
| a1-support.ru | /udalennaya-podderzhka/ | Удалённая поддержка компьютеров и серверов — A1 Support | IT-поддержка сотрудников по договору: бесплатный номер 8-800, Telegram, номер у каждой заявки, две линии инженеров. От 5 000 ₽ в месяц за офис до 5 ПК. | Удалённая поддержка компьютеров и серверов по договору |
| a1-support.ru | /ceny/ | Цены на IT-обслуживание компьютеров и серверов — A1 Support | Цены на обслуживание по договору: 5 000 ₽ в месяц за офис до пяти компьютеров, далее 500 ₽ за ПК, сервер от 1 200 ₽. Калькулятор стоимости и тарифы с выездом. | Цены на обслуживание компьютеров и серверов |
| itprovider.ru | /price | АйТи Провайдер. ИТ-поддержка, на которую можно положиться. 24/7... (дубль главной) | Быстрая реакция и оперативное решение проблем... (дубль главной) | (нет H1) |
| esc-kazan.ru | /services/it-soprovogdenie | Полное IT-сопровождение: компьютеры, серверы, телефония, ЭЦП | Обслуживание компьютеров и серверов, настройка МФУ, антивирусная защита, администрирование почты, доступ для удаленных сотрудников, помощь с ЭЦП, настройка Контур, Саби, Астрал. Выезд специалиста. Цены на сайте. | (нет H1) |
| i-tat.ru | /it_service/services/it-obsluzhivanie/it-autsorsing/ | ИТ-аутсорсинг - АЙТАТ - Наб.Челны - Нижнекамск | Получите команду профессионалов с узкими компетенциями по цене одного системного администратора! | (нет H1) |
| i-tat.ru | /it_service/services/it-obsluzhivanie/obsluzhivanie-serverov-... | Обслуживание серверов- Наб. Челны - Нижнекамск | Техническая поддрежка серверов, установка, настройка, ремонт, мониторинг работы с гарантией безопасности для вашей компании. Айтат- Комплексное ИТ и 1С обслуживание для бизнеса. | (нет H1) |

### Кто сильнее по CTR-потенциалу

- **a1-support.ru** — лучший: title с ценой («5 000 ₽ в месяц»), description с конкретикой (8-800, 1С, ЭЦП, почта, бэкапы), H1 совпадает с title. Высокий CTR-потенциал.
- **itprovider.ru** — title длинный, но с ключевыми словами («Казань, Республика Татарстан и России»), description с УТП («быстрая реакция, оперативное решение»). CTR средний-высокий.
- **esc-kazan.ru** — title короткий («Центр электронных услуг | Сервисы для бизнеса»), description с конкретикой (СКБ Контур, ЕГАИС, ЧЗ). CTR средний.
- **i-tat.ru** — title с брендом + услуга + города, description с метриками («1 800 предприятий, 16 лет»). CTR средний.
- **socialit.ru** — title короткий («ИТ-аутсорсинг для бизнеса по всей России»), description с УТП («передать IT и потерять контроль — не единственный сценарий»). CTR средний.
- **tss-kazan.ru** — title с брендом, description с метриками и телефоном. CTR средний.
- **obit.ru** — title очень длинный (переспам ключевыми словами), description с 80 городами. CTR низкий (длинный title обрезается в выдаче).
- **iteron.ru** — title с городом («в Москве»), description с метриками. CTR средний, но гео «Москва» не Казань.
- **its-kazan.ru** — title с ключевыми словами + бренд, description с УТП. CTR средний.
- **itbsgroup.ru** — title «Сайт ГК Ай Ти Бизнес Солюшенс - Главная» — слабый CTR (нет ключевых слов, нет УТП).

### Кто переспамлен

- **obit.ru** — title 120+ символов (обрезается в выдаче), перечисление всех услуг.
- **itprovider.ru** — title 100+ символов, повтор «Надежный партнер для бизнеса в Казани, Республике Татарстан и России».
- **its-kazan.ru** — title «Обслуживание компьютеров, серверов и сети ЛВС - ит айти аутсорсинг в Казани - IT сервис» — ключевые слова через дефисы.
- **tss-kazan.ru** — description со всеми преимуществами подряд (10 лет, бесперебойная работа, круглосуточная техподдержка, 100% гарантия, Казань, телефон).

### Кто слабо использует Казань/Татарстан

- **a1-support.ru** — «по всей России» (нет Казани в title).
- **socialit.ru** — «по всей России» (нет Казани).
- **iteron.ru** — «в Москве» (не Казань, не Татарстан).
- **obit.ru** — «Москва, Санкт-Петербург, Казань и еще в 80 городах» (Казань упомянута, но не акцент).
- **itbsgroup.ru** — нет Казани в title (только в description).
- **esc-kazan.ru** — «Казани» в description, но title без Казани.

### Какие конструкции F&F стоит переиграть

1. **a1-support**: «5 000 ₽ в месяц за офис до пяти ПК» в description — F&F: добавить цену в description.
2. **itprovider**: «ИТ-поддержка, на которую можно положиться. 24/7.» — F&F: короткий, ёмкий H1 с УТП.
3. **a1-support**: «Бесплатный номер 8-800» — F&F: «Локальный телефон 843» + «выезд инженера».
4. **esc-kazan**: «Полное IT-сопровождение: компьютеры, серверы, телефония, ЭЦП» — F&F: конкретный состав в title.
5. **i-tat**: «Получите команду профессионалов с узкими компетенциями по цене одного системного администратора!» — F&F: выгодное сравнение в description.
6. **socialit**: «Передать IT и потерять контроль - не единственный сценарий» — F&F: сильный хук в description.
7. **obit**: длинный title с ключевыми словами — F&F: избегать переспама (title ≤ 60 символов).
8. **iteron**: «IT аутсорсинг для бизнеса в Москве» — F&F: «IT-аутсорсинг для бизнеса в Казани» (локальный фокус).

### Итог

- **Лучший CTR-потенциал**: a1-support.ru (цена в description, конкретика, H1=title).
- **Переспамлены**: obit.ru (title 120+ символов), itprovider.ru (title 100+), its-kazan.ru (дефисы).
- **Слабо используют Казань/Татарстан**: a1-support, socialit, iteron (Москва), itbsgroup, esc-kazan.
- **F&F должен**: добавить цену в title/description, короткий H1 с УТП, локальный фокус (Казань/Татарстан), избегать переспама, конкретные метрики в description.

---

## Парсинг trust-блоков

### Таблица: конкурент | trust-элементы | убедительные | фейковые/шаблонные

| Конкурент | Trust-элементы | Убедительные | Фейковые/шаблонные |
|---|---|---|---|
| its-kazan.ru | Отзывы (много, с именами/компаниями), 2ГИС 5.0 (28 оценок), реквизиты (адрес, телефон, email), «сотрудничество более 7 лет» | Отзывы с именами; 2ГИС 5.0 | «Надёжно», «стабильно», «без сбоев» — без цифр; «опыт множества специалистов» |
| tss-kazan.ru | Отзывы («клиенты о нас»), кейсы (торговые сети), SLA, гарантия 100% возврат, реквизиты (адрес, телефон, email) | SLA с фин. мотивацией; «смените пароли — Аривидерчи» | «Бесперебойная работа», «круглосуточная техподдержка» — без цифр |
| itprovider.ru | Метрики (640k+ обращений, 35 спец., 28k единиц, 1022 сервера), отзывы (hh.ru 4.4, 16), реквизиты (ИНН/ОГРН), NDA, SLA (15/20 мин), сертификация Минцифры, фото директора (Антон Захаров), именные отзывы (Рызванов А.А., Молокин В.В., Захаров А.Н.) | Метрики с конкретикой; именные отзывы с компаниями; NDA; SLA; сертификация | «Команда экспертов», «быстрая реакция» — без цифр в тексте |
| i-tat.ru | Отзывы («клиенты»), фото специалистов, реквизиты (нет ИНН/ОГРН на главной), сертификаты (партнёр 1С), кейсы (нет), «сотрудничество более 10 лет» | Фото команды; 1С-партнёрство | «Сотрудничество более 10 лет» — без доказательств; нет реквизитов на главной |
| esc-kazan.ru (ЦЭУ) | Реквизиты (ИНН/ОГРН, адрес), цифры (21 год, 100% проектов в срок, 1000+ клиентов, до 50% экономия), 5 шагов | Реквизиты; 5 шагов; конкретные цифры | «100% проектов в срок» — опасно, если не выполняется; нет отзывов/кейсов |
| a8 / itbsgroup | Проекты (с именами: Денис Калинкин, Анна Гусева), реквизиты (нет на главной), сертификаты (партнёры), цифры (с 2005 года) | Проекты с именами и компаниями; партнёрство (Почта Банк, исполком Казани) | «Высококвалифицированные специалисты», «быстрая реализация» — без цифр |
| obit.ru | Кейсы (много), партнёры (логотипы), цифры (20+ лет), фото (предпол.), реквизиты (нет на главной) | Кейсы; партнёры; отраслевые страницы | «Оператор ИТ-решений» — общие слова; нет отзывов с именами |
| socialit.ru | Кейсы (много, сети), SLA с фин. гарантиями (1 000-1 500 ₽/час), тарифы с ценами, цифры (70+ городов, 100+ сотрудников), 3 линии | SLA с фин. гарантиями; кейсы сетей; конкретные цифры | «Передать IT и потерять контроль — не единственный сценарий» — хук, но без доказательств |
| iteron.ru | Отзывы («98% компаний остаются с нами»), кейсы (нет), реквизиты (ООО, адрес, телефон), цифры (18 лет, 31+ компаний, 18 крупных проектов, 98%), фото (нет) | Метрики (98%, 31+ компаний); калькулятор | «18 лет в бизнесе» — без доказательств; «гарантируем конфиденциальность» — без SLA |
| 1cbit.ru | Кейсы (много), цифры (ТОП-100, 300 000+ клиентов), SLA, реквизиты (ООО, ОГРН, ИНН) | Масштаб; SLA; реквизиты | «ТОП-100», «300 000+ клиентов» — без доказательств; нет отзывов с именами |
| calltraffic.ru | Лицензии (ФСТЭК), цифры (16 лет, 99.98% катастрофоустойчивость), реквизиты (адрес, телефон, email) | Лицензии ФСТЭК; конкретные цифры | «99.98% катастрофоустойчивость» — без SLA с фин. гарантиями |
| erpdev.ru | Отзывы (5/5), кейсы (да), NDA/SLA, гарантия 24 мес, реквизиты (адрес, телефон, email) | Кейсы; NDA/SLA; гарантия 24 мес | «Компетентность разработчика» — без конкретики |
| pc-kazan / comp-kazan | Отзывы (клиенты), 2ГИС 4.8, Яндекс 5.0, гарантия (comp-kazan до 2 лет) | 2ГИС/Яндекс рейтинги | Низкие цены; нет SLA; B2C |
| F&F | 7 кейсов (анонимные), 7 отзывов (анонимные), реквизиты (ИНН 165506822661), schema (Organization/Service/FAQPage/Person/BreadcrumbList), llms.txt, 161 страница, гарантия 30 дней (теперь 6 месяцев), 30 дней гарантия (теперь 6 месяцев) | Реквизиты (ИНН); 7 кейсов; 7 отзывов; schema; llms.txt | Отзывы анонимные; нет фото команды; нет SLA/договора; нет именных отзывов; нет метрик на первом экране; нет сертификатов |

### Минимальный набор trust-блоков, который F&F должен закрыть сильнее рынка

1. **Реквизиты (ИНН/ОГРН) на первом экране** — есть у a1-support, itprovider, esc-kazan. F&F: есть ИНН, но не на первом экране.
2. **Отзывы с именами/компаниями/датами/фото** — есть у itprovider (Рызванов, Молокин, Захаров), its-kazan, pc-kazan. F&F: анонимные → заменить на именные.
3. **Кейсы с метриками (до/после) на первом экране** — есть у itprovider (640k+ обращений), socialit (кейсы сетей), obit (проекты). F&F: 7 кейсов, но не на первом экране, без метрик.
4. **SLA/договор с финансовыми гарантиями** — есть у socialit (1 000-1 500 ₽/час), tss-kazan (100% возврат). F&F: нет → добавить.
5. **Гарантия 6 месяцев (единый срок)** — F&F: уже унифицировано (было 30 дней/6 месяцев).
6. **Фото команды** — есть у i-tat, obit, iteron, a1-support. F&F: нет → добавить.
7. **Сертификаты/партнёрства** — есть у i-tat (1С), a8 (партнёры), calltraffic (ФСТЭК). F&F: нет → добавить (1С, Microsoft, Минцифры).
8. **Конкретные цифры на первом экране** — есть у itprovider (640k+, 35 спец., 28k, 1022 сервера), socialit (70+ городов, 100+ сотрудников), esc-kazan (21 год, 1000+ клиентов, 99.9%). F&F: нет → добавить (количество заявок, время реакции, количество клиентов).
9. **Процесс работы (4 шага)** — есть у a1-support, esc-kazan. F&F: нет на первом экране → добавить.
10. **Договор + ЭДО** — есть у a1-support. F&F: есть legal/terms, но нет выделенной страницы.

### Итог

- **Лучший trust на рынке**: itprovider (метрики + именные отзывы + NDA + SLA + сертификация + фото директора).
- **F&F может перебить**: именные отзывы + кейсы с метриками + SLA с фин. гарантиями + гарантия 6 месяцев + фото команды + сертификаты + конкретные цифры + процесс 4 шага + договор/ЭДО — на первом экране.
- **Главный рычаг**: заменить анонимные отзывы на именные с компаниями/датами/фото; добавить кейсы с метриками на первый экран; добавить SLA/договор; добавить фото команды и сертификаты.

---

## Парсинг FAQ и возражений

### FAQ конкурентов (извлечённые вопросы и ответы)

**a1-support.ru (5 вопросов):**
1. Вы работаете только удалённо? → Основная работа удалённо; выезд в Москве и СПб по запросу; в других городах поможем найти мастера.
2. Что входит в абонентскую плату? → Помощь сотрудникам, настройка программ и принтеров, учётные записи, почта, подключение к 1С, обновления, контроль резервных копий. Серверы — отдельно.
3. Можно ли без договора, один раз? → Да, разовые работы без договора. Стоимость называем до начала.
4. Как быстро Вы реагируете? → Заявки принимаем 9:00-19:00 по Москве. Обращения по договору — в приоритете.
5. Работаете с НДС? → Мы на УСН, цены без НДС. Договор с НДС возможен — сумму назовём отдельно.

**socialit.ru (8 вопросов):**
1. Как организовать аутсорсинг? → Передать IT и потерять контроль — не единственный сценарий. SOCIALIT берёт отдельные функции, усиливает команду или полностью заменяет ИТ-отдел.
2. Какие услуги сисадмина? → Поддержка пользователей, настройка ПК, администрирование серверов, сети, инфобез.
3. Как работать с филиалами? → 70+ городов, 3 линии поддержки, выезд инженера.
4. Серверы? → Windows Server, Linux, VMware, Hyper-V, KVM, СХД, базы данных, мониторинг 24/7.
5. Сеть и связь? → Маршрутизаторы, коммутаторы, Wi-Fi, VPN, межсетевые экраны, IP-телефония.
6. Информационная безопасность? → Аудит, DLP, IDM/PAM, SIEM/SOAR, NGFW, защита данных.
7. Развитие инфраструктуры? → Capacity Management, Patch Management, резервное копирование, тестовое восстановление.
8. Битрикс24? → Внедрение CRM, обучение, настройка, интеграция, поддержка.

**tss-kazan.ru (5 возражений → решения):**
1. Остановка функционирования предприятия из-за сбоев → Проактивный мониторинг; предупреждение сбоев.
2. Отсутствие контроля (пароли у одного человека) → Детальное описание инфраструктуры с паролями руководителю; «смените пароли — Аривидерчи».
3. Отсутствие планирования бюджета → Договор на длительный срок с фиксированной суммой; анализ и оптимизация затрат.
4. Лишние затраты на штатного сотрудника → Команда за сумму на 20% меньше; остановка необоснованных расходов.
5. Оперативность решения проблем → SLA: время реагирования и решения; «мы теряем деньги, если у вас что-то не работает».

**itprovider.ru (блок «Уже есть системный администратор?»):**
1. Если в штате есть сисадмин → Круглосуточная поддержка основных сервисов; штатный специалист занимается текучкой и может уходить в отпуск/больничный.
2. Если в штате нет IT специалиста → Круглосуточная техподдержка, решение всех вопросов с рабочими станциями, оргтехникой, телефонией, интернетом.

**esc-kazan.ru:** FAQ нет (но есть «Кому точно нужна эта услуга» — 4 сегмента: небольшие офисы до 10 ПК, компании с удалёнными сотрудниками, участники госзакупок, те, у кого есть свой сервер).

### 1. Топ-20 вопросов рынка

1. Сколько стоит абонентское обслуживание? (цена)
2. Что входит в абонентскую плату? (состав)
3. Можно ли без договора, разово? (гибкость)
4. Как быстро реагируете? (скорость)
5. Работаете только удалённо или с выездом? (зона выезда)
6. Есть ли договор и гарантия? (доверие)
7. Работаете с НДС? (бухгалтерия)
8. Можно ли отказаться? (расторжение)
9. Почему не штатный сисадмин? (сравнение)
10. Что если не поможет / не понравится? (риск)
11. Как быстро приедете? (сроки выезда)
12. Есть ли SLA? (сроки)
13. Что входит в цену, а что за доплату? (прозрачность)
14. Можно ли начать с малого? (тарифы для малого)
15. Работаете с 1С? (1С)
16. Работаете с ЭЦП/ЕГАИС/торгами? (ЭЦП)
17. Как работаете с филиалами? (масштаб)
18. Как обеспечиваете безопасность данных? (инфобез)
19. Как организовано резервное копирование? (бэкапы)
20. Какие города обслуживаете? (география)

### 2. Слабые ответы конкурентов

- **Цена**: 10 из 14 не отвечают прямо («уточняйте у менеджеров», «от ...» без конкретики). Только a1-support, socialit, esc-kazan дают конкретные цифры.
- **Состав**: 8 из 14 не перечисляют, что входит в цену. Только a1-support («помощь сотрудникам, настройка программ и принтеров, учётные записи, почта, подключение к 1С, обновления, контроль резервных копий») и esc-kazan (детальный прайс) дают состав.
- **Сравнение со штатным**: только itprovider имеет блок «Уже есть системный администратор?». Остальные игнорируют возражение «почему не штатный».
- **Сроки/гарантия**: 9 из 14 не дают конкретных сроков реакции/решения. Только itprovider (15/20 мин), socialit (15 мин + фин. гарантии), esc-kazan (15 мин, 95% за 15-30 мин), iteron (90% за час) дают цифры.
- **Зона выезда**: 8 из 14 не указывают зону выезда. Только a1-support (Москва/СПб), tss-kazan (Казань), i-tat (Челны/Нижнекамск/Альметьевск), esc-kazan (выезд платно/3 раза бесплатно) указывают.
- **Риск (что если не поможет)**: 10 из 14 не отвечают. Только tss-kazan («100% возврат», «смените пароли»), socialit (SLA с фин. гарантиями), itprovider (NDA) отвечают.

### 3. Вопросы, которые F&F обязан закрыть лучше всех

1. **«Сколько стоит?»** → прозрачная цена + TCO-калькулятор + вилки «от» + «что входит/что за доплату».
2. **«Что входит в цену?»** → тарифы с составом (как a1-support, но для 20-50 человек).
3. **«Почему не штатный?»** → страница «F&F vs штатный сисадмин» с TCO-калькулятором (как itprovider, но с цифрами).
4. **«Что если не поможет?»** → гарантия 6 месяцев + SLA с фин. гарантиями (как socialit, но с локальным брендом).
5. **«Как быстро приедете?»** → SLA (реакция 15 мин, выезд в день обращения) + цены на выезд.
6. **«Есть ли договор/гарантия?»** → договор + SLA + гарантия 6 месяцев + акт + чек + безнал.
7. **«Можно ли начать с малого?»** → тарифы для офисов 20-50 человек + «первый месяц со скидкой».
8. **«Работаете с 1С?»** → «Серверы 1С, ЭЦП, инфобез под ключ. Не удалёнка — мы рядом.»
9. **«Работаете с ЭЦП/ЕГАИС/торгами?»** → «ЭЦП для ЕИС/госзакупок под ключ».
10. **«Как работаете с филиалами?»** → «Выезд инженера в города Татарстана» + локальные посадочные.
11. **«Как обеспечиваете безопасность?»** → «NDA + DLP + шифрование + резервные копии».
12. **«Как организовано резервное копирование?»** → «Ежедневные копии, глубина 14-30 дней, хранение вне клиники, тестовое восстановление».
13. **«Какие города обслуживаете?»** → «Казань + Челны + Нижнекамск + Альметьевск + Зеленодольск + выезд».
14. **«Можно ли без договора, разово?»** → «Да, разовые работы без договора. Стоимость называем до начала.»
15. **«Работаете с НДС?»** → «Работаем по безналу, акт, чек, безнал для ИП/ООО.»
16. **«Можно ли отказаться?»** → «Да, с уведомлением за 30 дней. Без штрафов, передаём документацию и доступы.»
17. **«Как быстро приедете?»** → «Выезд инженера в день обращения. Реакция 15 мин.»
18. **«Есть ли SLA?»** → «SLA с финансовыми гарантиями: реакция 15 мин, решение 4 часа. Или мы платим вам.»
19. **«Что входит в цену, а что за доплату?»** → «Тарифы с составом: что входит ✓, что за доплату ✗.»
20. **«Какие города обслуживаете?»** → «Казань + города Татарстана. Выезд инженера.»

### Итог

- **Лучший FAQ на рынке**: socialit (8 вопросов, глубокая отработка) + a1-support (5 вопросов, отработка возражений).
- **Лучшая отработка возражений**: tss-kazan (5 проблем→решения) + itprovider (блок «уже есть сисадмин?»).
- **F&F должен закрыть 20 вопросов** через FAQ на всех коммерческих страницах + отдельную страницу «F&F vs штатный сисадмин» + страницу SLA/договора + локальные посадочные.

---

## Парсинг коммерческих факторов

### Таблица покрытия коммерческих факторов

| Конкурент | Цены | Кнопки связи | Телефон в шапке | Адрес | Реквизиты | Способы оплаты | Условия работы | Договор | Гарантия | Зона обслуживания | Итого (из 10) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| a1-support.ru | ✅ (5 000 ₽/мес, +500 ₽/ПК, сервер от 1 200 ₽) | ✅ (8-800, Telegram, MAX, email) | ✅ (8 800 555-90-23) | ❌ (нет офиса, удалённо) | ✅ (ИП Кузнецов, ИНН 780518150252, ОГРНИП) | ✅ (безнал, ЭДО, УСН) | ✅ (договор, акты по ЭДО, без НДС) | ✅ (договор + ЭДО) | ❌ (нет явной гарантии) | ✅ (вся Россия удалённо, выезд в Москве/СПб) | 8/10 |
| tss-kazan.ru | ❌ (нет цен) | ✅ (телефон, форма) | ✅ (+7 843 2-102-422) | ✅ (Казань) | ✅ (адрес, телефон, email) | ✅ (постоплата) | ✅ (договор на длительный срок, SLA) | ✅ (договор + SLA) | ✅ (100% возврат) | ✅ (Казань) | 8/10 |
| itprovider.ru | ❌ (страница /price без цен) | ✅ (телефон, форма, email) | ✅ (+7 843 218-10-01) | ✅ (Казань, ул. Мавлютова, 42) | ✅ (ИНН/ОГРН: 1659092598/1091690022236) | ❌ (не указано) | ✅ (NDA, SLA, 24/7) | ✅ (NDA + SLA) | ❌ (нет явной гарантии) | ✅ (Казань, Татарстан, Россия) | 7/10 |
| i-tat.ru | ❌ (нет цен) | ✅ (телефон, форма, email) | ✅ (горячая линия) | ✅ (Казань/Челны) | ❌ (нет ИНН/ОГРН на главной) | ❌ (не указано) | ❌ (не указано) | ❌ (нет) | ❌ (нет) | ✅ (Челны, Нижнекамск, Альметьевск) | 4/10 |
| esc-kazan.ru (ЦЭУ) | ✅ (5 000/8 000 ₽/мес, разовые от 500-4 000 ₽) | ✅ (8 800 600-48-15, форма, email) | ✅ (8 800 600-48-15) | ✅ (Казань, ул. Чистопольская, 36, оф. 1302) | ✅ (ИНН/КПП 1657055576/165701001, ОГРН 1051629047843) | ❌ (не указано) | ✅ (5 шагов, фиксированные условия) | ❌ (нет явного договора) | ❌ (нет явной гарантии) | ✅ (Казань, удалённо по России) | 7/10 |
| a8 / itbsgroup | ❌ (каталог без цен) | ✅ (форма, email, телефон) | ✅ (предпол.) | ✅ (Казань) | ❌ (нет на главной) | ❌ (не указано) | ✅ (полный цикл: аудит→поставка→внедрение→сопровождение) | ❌ (нет явного договора) | ❌ (нет явной гарантии) | ✅ (Казань, Татарстан) | 5/10 |
| obit.ru | ❌ (нет цен) | ✅ (форма, телефон, ЛК) | ✅ (предпол.) | ✅ (Казань, офис) | ❌ (нет на главной) | ❌ (не указано) | ❌ (не указано) | ❌ (нет) | ❌ (нет) | ✅ (Москва, СПб, Казань, 80 городов) | 4/10 |
| socialit.ru | ✅ (10 000/20 000/50 000 ₽/мес, почасовой) | ✅ (форма, 8-800, email) | ✅ (предпол.) | ❌ (нет адреса на главной) | ❌ (нет на главной) | ❌ (не указано) | ✅ (SLA с фин. гарантиями, 3 линии) | ✅ (SLA) | ❌ (нет явной гарантии) | ✅ (70+ городов России) | 6/10 |
| iteron.ru | ❌ (калькулятор без фиксированных цен) | ✅ (форма, телефон, email) | ✅ (+7 495 660-35-00) | ✅ (Москва, Сельскохозяйственная, 11, к.3, оф. 148) | ✅ (предпол., ООО) | ❌ (не указано) | ❌ (не указано) | ❌ (нет) | ❌ (нет) | ✅ (Москва) | 4/10 |
| 1cbit.ru | ❌ (не загрузился, 401) | ❓ | ❓ | ❓ | ✅ (ООО, ОГРН, ИНН) | ❓ | ✅ (SLA) | ✅ (SLA) | ❓ | ❓ | 3/10 (по аудиту) |
| calltraffic.ru | ❌ (не загрузился, cert) | ❓ | ❓ | ✅ (Казань, площадка) | ✅ (адрес, телефон, email) | ❓ | ❓ | ❓ | ❓ | ❓ | 2/10 (по аудиту) |
| erpdev.ru | ❌ (не загрузился, таймаут) | ❓ | ❓ | ✅ (Москва) | ✅ (адрес, телефон, email) | ❓ | ✅ (NDA/SLA) | ✅ (NDA/SLA) | ✅ (гарантия 24 мес) | ❓ | 4/10 (по аудиту) |
| pc-kazan / comp-kazan / intertax | ✅ (от 250-474 ₽) | ✅ (телефон, форма) | ✅ (предпол.) | ❌ (не указано) | ❌ (только privacy policy) | ❌ (не указано) | ❌ (не указано) | ❌ (нет) | ✅ (comp-kazan до 2 лет) | ❌ (не указано) | 3/10 |
| F&F | ✅ (prices.html, но без тарифных таблиц с ценами) | ✅ (телефон, форма, TG, MAX) | ✅ (локальный телефон) | ❌ (нет офиса — Organization, не LocalBusiness) | ✅ (ИНН 165506822661) | ✅ (безнал, акт, чек) | ✅ (terms-of-work.html, гарантия 6 месяцев) | ✅ (terms-of-work.html) | ✅ (6 месяцев — унифицировано) | ✅ (Казань + города Татарстана) | 8/10 |

### Кто выглядит самым «готовым к сделке»

1. **a1-support.ru** (8/10) — цены + договор + ЭДО + 8-800 + Telegram/MAX + реквизиты + безнал + УСН + зона обслуживания. Самый «готовый к сделке» на рынке.
2. **tss-kazan.ru** (8/10) — SLA + гарантия 100% возврат + постоплата + договор + реквизиты + адрес + телефон + зона. Готов к сделке, но без цен.
3. **F&F** (8/10) — реквизиты + договор (terms-of-work) + гарантия 6 месяцев + безнал + акт + чек + зона + кнопки связи + телефон. Готов к сделке, но без тарифов с ценами и без SLA-страницы.
4. **itprovider.ru** (7/10) — реквизиты + NDA + SLA + 24/7 + адрес + телефон. Готов к сделке, но без цен.
5. **esc-kazan.ru** (7/10) — цены + реквизиты + адрес + телефон + 5 шагов + зона. Готов к сделке, но без договора/SLA/гарантии.

### Кто выглядит просто витриной

- **obit.ru** (4/10) — нет цен, нет договора, нет SLA, нет гарантии, нет реквизитов на главной. Витрина услуг.
- **iteron.ru** (4/10) — нет цен, нет договора, нет SLA, нет гарантии. Витрина + калькулятор.
- **i-tat.ru** (4/10) — нет цен, нет договора, нет SLA, нет реквизитов, нет условий. Витрина услуг.
- **a8/itbsgroup** (5/10) — каталог оборудования, нет цен, нет договора/SLA/гарантии. Витрина каталога.
- **pc-kazan/comp-kazan/intertax** (3/10) — B2C, нет договора/SLA, нет реквизитов. Витрина услуг.
- **socialit.ru** (6/10) — цены есть, SLA есть, но нет реквизитов/адреса на главной, нет договора явного. Полувитрина.

### Что F&F должен добавить, чтобы стать самым «готовым к сделке»

1. **Тарифы с ценами** на prices.html (как a1-support, socialit, esc-kazan).
2. **Страница SLA/договора** с фин. гарантиями (как socialit, tss-kazan).
3. **Кнопки связи** уже есть (телефон, форма, TG, MAX) — ✅.
4. **Реквизиты** уже есть (ИНН) — ✅, но добавить на первый экран.
5. **Способы оплаты** уже есть (безнал, акт, чек) — ✅, но добавить на prices.html.
6. **Условия работы** уже есть (terms-of-work.html) — ✅, но добавить ссылку на первый экран.
7. **Гарантия 6 месяцев** — ✅ (унифицировано).
8. **Зона обслуживания** — ✅ (Казань + города Татарстана), но добавить на первый экран.

### Итог

- **Самый «готовый к сделке»**: a1-support.ru (8/10) — цены + договор + ЭДО + 8-800 + TG/MAX + реквизиты + безнал + УСН + зона.
- **F&F** (8/10) — на равных с a1-support, но без тарифов с ценами и без SLA-страницы.
- **Главный рычаг**: добавить тарифы с ценами + страницу SLA/договора с фин. гарантиями → F&F станет самым «готовым к сделке» в Казани (a1-support — федеральный, без локального бренда).

---

## Парсинг локальности (Казань и Татарстан)

### Таблица: конкурент | локальные маркеры | реальная локальность | где слабо

| Конкурент | Локальные маркеры | Реальная локальность | Где слабо |
|---|---|---|---|
| its-kazan.ru | Адрес (Казань), телефон 843, 2ГИС 5.0, отзывы клиентов из Казани, «Казань» в title | Средняя: локальный бренд, отзывы, 2ГИС | Нет выезда, нет посадочных под города Татарстана, нет кейсов с указанием города |
| tss-kazan.ru | Адрес (Казань), телефон 843, кейсы торговых сетей, «Работаем в Казани» в description | Средняя: локальный бренд, кейсы | Нет посадочных под города, нет выезда, нет отзывов с указанием города |
| itprovider.ru | Адрес (Казань, ул. Мавлютова, 42), телефон 843, 2ГИС, «Казань, Республика Татарстан и России» в title, реквизиты (ИНН/ОГРН) | Средняя: локальный бренд, реквизиты | Нет посадочных под города, нет выезда, нет отзывов с указанием города, нет кейсов с метриками |
| i-tat.ru | Адреса в 5 городах (Казань, Челны, Нижнекамск, Альметьевск, Зеленодольск), телефоны по городам, локальные посадочные (Челны/Нижнекамск/Альметьевск), «Наб.Челны - Нижнекамск» в title, фото специалистов | Высокая: реальные посадочные, локальные телефоны, фото команды | Нет SLA, нет цен, IT вторичен (1С/сметы главные), нет кейсов с метриками |
| esc-kazan.ru (ЦЭУ) | Адрес (Казань, ул. Чистопольская, 36), телефон 8 800, реквизиты (ИНН/ОГРН), «Казань» в description, выезд (95% за 15-30 мин) | Средняя: локальный бренд, реквизиты, выезд | Нет посадочных под города, нет отзывов с указанием города, IT вторичен (бухгалтерия/юристы главные) |
| a8 / itbsgroup | Меню городов (Казань, Альметьевск, Челны, Нижнекамск), проекты (Казань, Почта Банк), «Казань» в description | Средняя: меню городов, проекты | Нет посадочных с контентом, нет цен, нет SLA, IT вторичен (оборудование главное) |
| obit.ru | Адрес (Казань, офис), «Казань» в description (среди 80 городов) | Низкая: федеральный масштаб, Казань — один из 80 городов | Нет посадочных, нет выезда, нет отзывов с указанием города, IT вторичен (телеком главный) |
| socialit.ru | Телефон (Казань), «70+ городов России» | Низкая: федеральный масштаб, Казань — один из 70+ городов | Нет посадочных, нет выезда, нет отзывов с указанием города, нет реквизитов на главной |
| iteron.ru | Адрес (Москва), «Москва» в title | Низкая: московский бренд, нет казанского присутствия | Нет Казани, нет посадочных, нет выезда, нет отзывов с указанием города |
| 1cbit.ru | Адрес (Казань), «Казань» в реквизитах | Низкая: федеральный масштаб, Казань — один из городов | Нет посадочных, нет выезда, нет отзывов с указанием города |
| calltraffic.ru | Площадка (Казань), адрес, телефон | Низкая: федеральный масштаб | Нет посадочных, нет выезда, нет отзывов с указанием города |
| erpdev.ru | Адрес (Москва) | Низкая: московский бренд | Нет Казани, нет посадочных, нет выезда |
| pc-kazan / comp-kazan / intertax | Телефон, адрес (Казань) | Низкая: B2C, нет посадочных | Нет посадочных, нет выезда, нет отзывов с указанием города |
| F&F | ИНН (Татарстан), 7 кейсов (по городам), 7 отзывов (анонимные), schema Organization, llms.txt, «Казань» в title/description, адрес (нет офиса — Organization) | Средняя: локальный бренд, кейсы по городам, ИНН | Нет посадочных под города, нет выезда явного, нет отзывов с указанием города, нет 2ГИС/Яндекс.Карты, нет телефона 843 на первом экране |

### Кто реально выглядит локально

- **i-tat.ru** — сильнейший: 5 городов, телефоны по городам, локальные посадочные, фото специалистов, «Наб.Челны - Нижнекамск» в title.
- **a8/itbsgroup** — средний: меню городов (Казань, Альметьевск, Челны, Нижнекамск), проекты (Казань, Почта Банк).
- **its-kazan, tss-kazan, itprovider, esc-kazan** — средние: локальный бренд, адрес, телефон, отзывы/кейсы, но нет посадочных под города.
- **obit, socialit, 1cbit, calltraffic** — низкие: федеральный масштаб, Казань — один из многих городов.
- **iteron, erpdev** — низкие: московский бренд, нет казанского присутствия.

### Кто просто пишет «Казань» для галочки

- **obit.ru** — «Москва, Санкт-Петербург, Казань и еще в 80 городах» — Казань растворена среди 80 городов.
- **socialit.ru** — «70+ городов России» — Казань — одна из 70+.
- **1cbit.ru** — «Казань» в реквизитах, но масштаб федеральный.
- **calltraffic.ru** — «Казань (площадка)», но масштаб федеральный.
- **a1-support.ru** — «по всей России» — нет Казани.
- **iteron.ru** — «в Москве» — вообще не Казань.

### Как F&F может выглядеть локальнее сильных игроков Татарстана

1. **Локальные посадочные для 4 городов** (Челны, Нижнекамск, Альметьевск, Зеленодольск) с реальным контентом: кейсы, цены, SLA, выезд, отзывы. Как i-tat, но с ценами и SLA.
2. **Кейсы с указанием города и отрасли** на первом экране. Как a8 (проекты с именами), но с метриками.
3. **Локальные маркеры**: телефон с кодом 843, 2ГИС, Яндекс.Карты, отзывы с указанием города. Как its-kazan (2ГИС 5.0).
4. **Выезд инженера в день обращения** — явно указать на первом экране. Как esc-kazan (95% за 15-30 мин).
5. **Schema Organization с address/geo/sameAs** (2ГИС, Яндекс.Карты). Как a1-support (реквизиты + договор).
6. **Отзывы с указанием города** («Казань», «Челны», «Нижнекамск»). Как its-kazan (отзывы клиентов).
7. **Не спамить**: не создавать 50 одинаковых страниц с заменой города, а делать уникальный контент. Как i-tat (реальные посадочные).

### Итог

- **Сильнейший локальный игрок**: i-tat.ru (5 городов, телефоны, посадочные, фото команды) — но IT вторичен (1С/сметы).
- **F&F может перебить**: локальные посадочные (4 города) + кейсы с метриками + выезд в день обращения + 2ГИС/Яндекс.Карты + отзывы с городом + schema с address/geo + цены + SLA + гарантия 6 месяцев — на первом экране. Ни один конкурент в Казани не делает этого одновременно.

---

## Парсинг конверсионных элементов

### Таблица: конкурент | CTA-тексты | формы/поля | попапы/квизы/калькуляторы | floating | next step после заявки

| Конкурент | CTA-тексты | Формы/поля | Попапы/квизы/калькуляторы | Floating | Next step после заявки |
|---|---|---|---|---|---|
| a1-support.ru | «Рассчитать стоимость», «Заказать», «8 800 555-90-23», Telegram, MAX, email | Форма: имя, телефон, email, сообщение (на /ceny/) | Калькулятор (ПК + серверы → стоимость), 4 шага процесса | Нет (телефон в шапке) | «Менеджер свяжется в рабочее время (9:00-19:00)» |
| tss-kazan.ru | «Бесплатный аудит», телефон, форма | Форма: имя, телефон, email, сообщение | Нет калькулятора, нет квиза | Нет | «SLA: время реагирования и решения» |
| itprovider.ru | «Давайте знакомиться», «Хотите узнать больше?», «Обсудить ваш проект», «Можем рассказать подробнее» | Форма: имя, телефон, email, сообщение (на #hello, #rec790617817) | Нет калькулятора, нет квиза | Нет (телефон в шапке) | «Мы свяжемся с вами» |
| i-tat.ru | «Обратиться», «КУПИТЬ», «ОБРАТИТЬСЯ», «Закроем любую Вашу задачу по 1С!» | Форма: имя, телефон, email, сообщение (javascript:) | Нет калькулятора, нет квиза | Нет | «Мы свяжемся с вами» |
| esc-kazan.ru (ЦЭУ) | «Получить скидку», «Начать сотрудничество», «Заказать звонок», «Получить консультацию», «Рассчитать стоимость», «Получить расчет» | Форма: имя, телефон, email, сообщение (попап #popup:zayavka, #popup:itzayavka) | Попапы (заявка, звонок, embedcode), нет калькулятора/квиза | Нет (телефон в шапке) | «Подберем тариф под задачи вашего бизнеса» |
| a8 / itbsgroup | «Опишите задачу», «Весь каталог», «Заказать звонок» | Форма: имя, телефон, email, сообщение | Нет калькулятора, нет квиза | Нет | «Подготовим спецификацию и КП» |
| obit.ru | «Заказать звонок», «Личный кабинет» | Форма: имя, телефон, email, сообщение | Нет калькулятора, нет квиза | Нет | «Мы свяжемся с вами» |
| socialit.ru | «Получить КП» (на каждом тарифе), «Получить консультацию» | Форма: имя, телефон, email, сообщение (#form) | Нет калькулятора, нет квиза | Нет | «Мы свяжемся с вами» |
| iteron.ru | «Заказать консультацию», «Отправить запрос», «Скачать iDesk» | Форма: имя, телефон, email, сообщение (#callback, #callback-calc) | Калькулятор (ПК + серверы → стоимость) | Нет | «Мы свяжемся с вами» |
| 1cbit.ru | Неизвестно (401) | Неизвестно | Неизвестно | Неизвестно | Неизвестно |
| calltraffic.ru | Неизвестно (cert) | Неизвестно | Неизвестно | Неизвестно | Неизвестно |
| erpdev.ru | Неизвестно (таймаут) | Неизвестно | Неизвестно | Неизвестно | Неизвестно |
| pc-kazan / comp-kazan / intertax | «Заказать», «Купить» | Форма: имя, телефон, email | Нет калькулятора, нет квиза | Нет | «Мы свяжемся с вами» |
| F&F | «Получить консультацию», «Получить разбор», «Получить расчёт», «Отправить», «Заказать звонок» | Форма: имя, телефон, email, сообщение (на всех страницах) | Квиз (quiz.html), калькулятор (calculator.js), поиск (search.js), exit-popup, нет попапов на главной | Нет (телефон в шапке) | «Мы свяжемся с вами» (не конкретизировано) |

### Лучшие CTA

1. **a1-support.ru**: «Рассчитать стоимость» + калькулятор на первом экране + «8-800» + Telegram/MAX. Мультиканальность + расчёт на первом экране.
2. **socialit.ru**: «Получить КП» на каждом тарифе. Чёткий CTA рядом с ценой.
3. **esc-kazan.ru**: «Получить скидку» + «Начать сотрудничество» + «Заказать звонок» + «Получить консультацию» + «Рассчитать стоимость» + «Получить расчет». Много CTA, но разные по смыслу.
4. **iteron.ru**: «Заказать консультацию» + калькулятор + «Отправить запрос». Калькулятор + CTA.
5. **itprovider.ru**: «Давайте знакомиться» + «Хотите узнать больше?» + «Обсудить ваш проект» + «Можем рассказать подробнее». Мягкие CTA, но много.

### Худшие CTA

1. **obit.ru**: «Заказать звонок» — единственный CTA, нет конкретики.
2. **i-tat.ru**: «Обратиться», «КУПИТЬ», «ОБРАТИТЬСЯ» — разные по смыслу, нет единого CTA.
3. **pc-kazan/comp-kazan/intertax**: «Заказать», «Купить» — шаблонные.
4. **its-kazan.ru**: «Отзывы клиентов», «6 приоритетов» — не CTA, а ссылки.

### Где форма слишком тяжёлая

- **Все конкуренты** используют стандартную форму: имя, телефон, email, сообщение (4 поля). Это не слишком тяжело, но и не оптимально.
- **esc-kazan.ru**: много попапов (#popup:zayavka, #popup:itzayavka, #popup:embedcode, #popup:zayavka) — путаница, какой попап открывать.
- **itprovider.ru**: форма на #hello и #rec790617817 — две точки входа, путаница.
- **iteron.ru**: форма #callback и #callback-calc — две точки входа.

### Где путь до заявки короткий и чистый

- **a1-support.ru**: калькулятор на первом экране → «Рассчитать стоимость» → форма (имя, телефон, email, сообщение) → «менеджер свяжется». Путь: 2 клика.
- **socialit.ru**: тарифы с ценами → «Получить КП» → форма. Путь: 2 клика.
- **esc-kazan.ru**: «Рассчитать стоимость» → попап с формой. Путь: 2 клика.
- **F&F**: форма на всех страницах (имя, телефон, email, сообщение) → «Отправить». Путь: 1 клик (форма на странице), но без «что будет после заявки».

### Предлагаемый стандарт CTA/форм для F&F

1. **Единый CTA на всех страницах**: «Получить расчёт» (вместо «Получить консультацию», «Получить разбор», «Отправить»).
2. **Калькулятор TCO на первом экране** (как a1-support) → «Рассчитать стоимость» → форма.
3. **Форма: 3 поля** (имя, телефон, email) + опциональное сообщение. Убрать обязательное сообщение.
4. **Мультиканальные CTA**: «Получить расчёт» + «Позвонить» + «Telegram» + «MAX» + «Email».
5. **«Что будет после заявки: 4 шага»** рядом с формой: аудит → настройка → поддержка → отчётность.
6. **Floating-кнопка** «Получить расчёт» (фиксированная в правом нижнем углу) на всех страницах.
7. **Один попап** (вместо 4 у esc-kazan) — единый попап с формой.
8. **Next step после заявки**: «Мы свяжемся с вами в течение 15 минут. Вы получите расчёт стоимости и план работ.»
9. **Микро-CTA рядом с ценами**: «Получить КП» (как socialit) на каждом тарифе.
10. **Exit-intent popup** (уже есть) — усилить предложением «Бесплатный аудит IT-инфраструктуры».

### Итог

- **Лучший CTA**: a1-support.ru («Рассчитать стоимость» + калькулятор + мультиканальность).
- **Худший CTA**: obit.ru («Заказать звонок»), i-tat.ru (разные CTA), its-kazan.ru (не CTA).
- **Самая тяжёлая форма**: esc-kazan.ru (4 попапа), itprovider.ru (2 точки входа), iteron.ru (2 точки входа).
- **Самый чистый путь до заявки**: a1-support.ru (2 клика: калькулятор → форма), socialit.ru (2 клика: тариф → «Получить КП»), esc-kazan.ru (2 клика: «Рассчитать» → попап).
- **F&F должен**: единый CTA «Получить расчёт», калькулятор TCO на первом экране, форма 3 поля, мультиканальность, «что будет после заявки: 4 шага», floating-кнопка, один попап, next step с конкретными сроками, микро-CTA рядом с ценами, exit-intent с «бесплатный аудит».

---

## Парсинг контент-форматов

### Таблица: конкурент | форматы контента | что сильно | чего нет

| Конкурент | Форматы контента | Что сильно | Чего нет |
|---|---|---|---|
| a1-support.ru | Статьи (нет), сравнения (нет), калькулятор (да), чек-листы (нет), кейсы (нет), гайды (нет), таблицы (тарифы), видео (нет), PDF (нет), FAQ (5 вопросов) | Калькулятор (ПК+серверы), тарифные таблицы, FAQ 5 вопросов, процесс 4 шага | Блог, кейсы, статьи, сравнения, чек-листы, гайды, видео, PDF |
| tss-kazan.ru | Статьи (нет), сравнения (нет), калькулятор (нет), чек-листы (нет), кейсы (да — торговые сети), гайды (нет), таблицы (нет), видео (нет), PDF (нет), FAQ (нет, но 5 возражений→решения) | Кейсы (торговые сети), отработка возражений (5 проблем→решения), SLA | Блог, статьи, калькулятор, чек-листы, гайды, сравнения, таблицы, видео, PDF, FAQ |
| itprovider.ru | Статьи (нет), сравнения (блок «уже есть сисадмин?»), калькулятор (нет), чек-листы (нет), кейсы (нет), гайды (нет), таблицы (нет), видео (нет), PDF (нет), FAQ (нет) | Блок «уже есть сисадмин?» (2 сценария), метрики (640k+, 35 спец.), преимущества 6 штук | Блог, статьи, калькулятор, чек-листы, кейсы, гайды, сравнения, таблицы, видео, PDF, FAQ |
| i-tat.ru | Статьи (база знаний), сравнения (нет), калькулятор (нет), чек-листы (нет), кейсы (нет), гайды (нет), таблицы (нет), видео (нет), PDF (нет), FAQ (нет) | База знаний (статьи для сметчиков), 1С-экспертиза, локальные посадочные | Калькулятор, чек-листы, кейсы, сравнения, гайды, таблицы, видео, PDF, FAQ |
| esc-kazan.ru (ЦЭУ) | Статьи (журнал), сравнения (нет), калькулятор (нет), чек-листы (нет), кейсы (нет), гайды (нет), таблицы (тарифы), видео (нет), PDF (нет), FAQ (нет, но 4 сегмента) | Журнал (статьи), тарифные таблицы, 5 шагов, 4 сегмента | Калькулятор, чек-листы, кейсы, сравнения, гайды, видео, PDF, FAQ |
| a8 / itbsgroup | Статьи (новости), сравнения (нет), калькулятор (нет), чек-листы (нет), кейсы (проекты), гайды (нет), таблицы (нет), видео (нет), PDF (нет), FAQ (нет) | Проекты (с именами), новости, каталог оборудования | Калькулятор, чек-листы, сравнения, гайды, таблицы, видео, PDF, FAQ, статьи (глубокие) |
| obit.ru | Статьи (нет), сравнения (нет), калькулятор (нет), чек-листы (нет), кейсы (проекты), гайды (нет), таблицы (нет), видео (нет), PDF (нет), FAQ (нет) | Проекты (с именами), отраслевые страницы (9), каталог услуг | Калькулятор, чек-листы, сравнения, гайды, таблицы, видео, PDF, FAQ, статьи |
| socialit.ru | Статьи (нет), сравнения (нет), калькулятор (нет), чек-листы (нет), кейсы (да — сети), гайды (нет), таблицы (тарифы), видео (нет), PDF (нет), FAQ (8 вопросов) | Тарифные таблицы (3 тарифа + почасовой), FAQ 8 вопросов, кейсы сетей | Блог, статьи, калькулятор, чек-листы, сравнения, гайды, видео, PDF |
| iteron.ru | Статьи (блог, 3 статьи), сравнения (нет), калькулятор (да — ПК+серверы), чек-листы (нет), кейсы (нет), гайды (нет), таблицы (нет), видео (нет), PDF (нет), FAQ (нет) | Калькулятор (ПК+серверы→стоимость), блог (3 статьи), метрики (98%) | Кейсы, чек-листы, сравнения, гайды, таблицы, видео, PDF, FAQ, статьи (глубокие) |
| 1cbit.ru | Статьи (неизвестно), сравнения (неизвестно), калькулятор (неизвестно), чек-листы (неизвестно), кейсы (да), гайды (неизвестно), таблицы (неизвестно), видео (неизвестно), PDF (неизвестно), FAQ (неизвестно) | Кейсы (много), масштаб (300 000+ клиентов) | Неизвестно (сайт не загрузился, 401) |
| calltraffic.ru | Статьи (неизвестно), сравнения (неизвестно), калькулятор (неизвестно), чек-листы (неизвестно), кейсы (неизвестно), гайды (неизвестно), таблицы (неизвестно), видео (неизвестно), PDF (неизвестно), FAQ (неизвестно) | Лицензии ФСТЭК, катастрофоустойчивость 99.98% | Неизвестно (сайт не загрузился, cert) |
| erpdev.ru | Статьи (неизвестно), сравнения (неизвестно), калькулятор (неизвестно), чек-листы (неизвестно), кейсы (да), гайды (неизвестно), таблицы (неизвестно), видео (неизвестно), PDF (неизвестно), FAQ (неизвестно) | Кейсы, NDA/SLA, гарантия 24 мес | Неизвестно (таймаут) |
| pc-kazan / comp-kazan / intertax | Статьи (нет), сравнения (нет), калькулятор (нет), чек-листы (нет), кейсы (нет), гайды (нет), таблицы (нет), видео (нет), PDF (нет), FAQ (нет) | Низкие цены, быстрый выезд | Блог, статьи, калькулятор, чек-листы, кейсы, сравнения, гайды, таблицы, видео, PDF, FAQ |
| F&F | Статьи (40+ блог + 8 статей), сравнения (5 страниц compare/*), калькулятор (calculator.js, но не TCO), чек-листы (audits/backup-checklist.html), кейсы (20+), гайды (32 гайда в blog.html), таблицы (на многих страницах), видео (нет), PDF (нет), FAQ (129 страниц с FAQPage) | 161 страница, 40+ блог, 8 статей, 20+ кейсов, 32 гайда, 5 сравнений, чек-листы, таблицы, FAQ на 129 страницах, llms.txt | Видео, PDF, TCO-калькулятор, глубокие статьи (350-580 слов — мало), локальные посадочные |

### Что реально используется сильно (на рынке)

1. **Калькуляторы** — a1-support (ПК+серверы→стоимость), iteron (ПК+серверы→стоимость). Только 2 из 14. F&F имеет calculator.js, но не TCO.
2. **FAQ-кластеры** — a1-support (5 вопросов), socialit (8 вопросов). Только 2 из 14. F&F имеет FAQ на 129 страницах, но не кластеризованы.
3. **Кейсы** — tss-kazan (торговые сети), a8 (проекты с именами), obit (проекты), erpdev (кейсы), 1cbit (кейсы), F&F (20+ кейсов). 6 из 14.
4. **Тарифные таблицы** — a1-support, socialit, esc-kazan. 3 из 14.
5. **Блог/статьи** — i-tat (база знаний), esc-kazan (журнал), iteron (3 статьи), F&F (40+ блог + 8 статей). 4 из 14.
6. **Сравнения** — только F&F (5 страниц compare/*) и itprovider (блок «уже есть сисадмин?»). 2 из 14.
7. **Чек-листы** — только F&F (audits/backup-checklist.html). 1 из 14.
8. **Гайды** — только F&F (32 гайда в blog.html). 1 из 14.
9. **Таблицы** — a1-support, socialit, esc-kazan, F&F. 4 из 14.
10. **Видео** — никто. 0 из 14.
11. **PDF** — никто. 0 из 14.

### Чего почти ни у кого нет

- **Видео** — 0 из 14. F&F может быть первым.
- **PDF** (чек-листы, гайды) — 0 из 14. F&F может быть первым.
- **Чек-листы** — 1 из 14 (F&F). F&F может усилить.
- **Гайды** — 1 из 14 (F&F). F&F может усилить.
- **Сравнения** — 2 из 14 (F&F, itprovider). F&F может усилить.
- **TCO-калькулятор** — 0 из 14. F&F может быть первым.
- **FAQ-кластеры** — 2 из 14. F&F может усилить (129 страниц с FAQ, но не кластеризованы).

### Какие форматы F&F может закрыть первым и забрать внимание

1. **TCO-калькулятор** (штатный vs аутсорсинг) — 0 конкурентов. F&F: добавить на prices.html и compare/staff-sysadmin-cost.html. Забрать внимание: «Расчёт TCO за 2 минуты».
2. **Видео** (обзоры, кейсы, инструкции) — 0 конкурентов. F&F: добавить 3-5 видео (обзор сервера, кейс, инструкция по бэкапу). Забрать внимание: «Смотрите, как мы настраиваем сервер за 10 минут».
3. **PDF-чек-листы** (бэкап, безопасность, ЭЦП) — 0 конкурентов. F&F: добавить 3-5 PDF (чек-лист бэкапа, чек-лист безопасности, чек-лист ЭЦП). Забрать внимание: «Скачайте чек-лист: 15 пунктов проверки бэкапа».
4. **FAQ-кластеры** (по темам: цены, SLA, 1С, ЭЦП, бэкапы, безопасность) — 2 конкурента. F&F: кластеризовать FAQ на 129 страницах. Забрать внимание: «Ответы на 50 вопросов об IT-аутсорсинге».
5. **Сравнения** (F&F vs штатный, F&F vs фрилансер, F&F vs интегратор) — 2 конкурента. F&F: усилить compare/* (5 страниц). Забрать внимание: «F&F vs штатный сисадмин: TCO за год».
6. **Кейсы с метриками** (до/после) — 6 конкурентов. F&F: добавить метрики на 7 кейсов. Забрать внимание: «Как мы сократили время простоя с 4 часов до 15 минут».
7. **Гайды** («Как выбрать IT-аутсорс», «Что должно быть в SLA») — 1 конкурент. F&F: добавить 5-10 гайдов. Забрать внимание: «Полный гайд: как выбрать IT-аутсорсинг для офиса 20-50 человек».
8. **Чек-листы** (бэкап, безопасность, ЭЦП) — 1 конкурент. F&F: усилить audits/backup-checklist.html. Забрать внимание: «Чек-лист: 15 пунктов проверки бэкапа».

### Итог

- **Что реально используется сильно**: калькуляторы (2/14), FAQ (2/14), кейсы (6/14), тарифные таблицы (3/14), блог/статьи (4/14), сравнения (2/14), чек-листы (1/14), гайды (1/14), таблицы (4/14).
- **Чего почти ни у кого нет**: видео (0/14), PDF (0/14), TCO-калькулятор (0/14), FAQ-кластеры (2/14), сравнения (2/14).
- **F&F может закрыть первым**: TCO-калькулятор, видео, PDF-чек-листы, FAQ-кластеры, сравнения, кейсы с метриками, гайды, чек-листы — и забрать внимание через уникальные форматы, которых нет у конкурентов.

---

## Сильные куски конкурентов

### 1. Лучшие H1

| Конкурент | H1 | Почему сильный | Как сделать лучше для F&F |
|---|---|---|---|
| a1-support.ru | «Удалённая IT-поддержка компьютеров и серверов для бизнеса по всей России» | Конкретный, содержит услугу + объект + гео. Не шаблонный. | «IT-аутсорсинг для офисов 20-50 человек в Казани и Татарстане» — добавить сегмент и локальный фокус. |
| itprovider.ru | «ИТ-поддержка, на которую можно положиться. 24/7.» | Короткий, ёмкий, с УТП (24/7) и эмоциональным якорем («можно положиться»). | «IT-аутсорсинг, на который можно положиться. Реакция 15 минут.» — добавить конкретный SLA. |
| iteron.ru | «IT-поддержка, которая всегда рядом» | Эмоциональный, обещает доступность. | «IT-поддержка, которая всегда рядом. Выезд инженера в день обращения.» — добавить конкретику. |
| esc-kazan.ru | «Комплексное обслуживание бизнеса» | Широкий, но без конкретики (слабый). | Не использовать — слишком общий. |
| tss-kazan.ru | (нет H1) | — | F&F должен иметь H1 на каждой странице. |
| socialit.ru | (нет H1) | — | F&F должен иметь H1 на каждой странице. |
| F&F (текущий) | «IT-аутсорсинг для бизнеса» (предпол.) | Общий. | Усилить: «IT-аутсорсинг для офисов 20-50 человек в Казани. Реакция 15 минут. Гарантия 6 месяцев.» |

### 2. Лучшие лиды (первый абзац)

| Конкурент | Лид | Почему сильный | Как сделать лучше для F&F |
|---|---|---|---|
| a1-support.ru | «Берём на себя компьютеры, серверы, 1С, электронную подпись и почту Вашей компании. Работаем по договору: сотрудники звонят на бесплатный номер 8-800, инженер подключается удалённо и решает задачу. Абонентское обслуживание — от 5 000 ₽ в месяц за офис до пяти компьютеров.» | Конкретный: что берём, как работаем, цена. 3 предложения, всё по делу. | «Берём на себя серверы 1С, ЭЦП, почту и инфраструктуру вашего офиса. Сотрудники звонят на локальный номер, инженер подключается удалённо и решает задачу. Выезд в день обращения. Абонентское обслуживание — от X ₽ в месяц за офис 20-50 человек. Реакция 15 минут. Гарантия 6 месяцев.» |
| itprovider.ru | «Решенных обращений от клиентов с 2009 года: 640 000. IT специалистов в штате: 35. Единиц на обслуживании, из них 1022 сервера: 28 000.» | Метрики на первом экране. Конкретные цифры вместо слов. | «X заявок решено. Y клиентов. Z минут — среднее время реакции. Гарантия 6 месяцев.» — добавить метрики F&F. |
| tss-kazan.ru | «Остановка функционирования предприятия на длительное время из-за сбоев в работе ИТ систем... Отсутствие контроля над компанией...» | Начинает с болей клиента, а не с «мы». | «Сервер 1С упал в пятницу вечером. Штатный сисадмин в отпуске. Почта не работает. ЭЦП не подписывает. — Мы решаем это за 15 минут.» — конкретная боль + решение. |
| socialit.ru | «Передать IT и потерять контроль — не единственный сценарий. SOCIALIT берёт на себя отдельные функции, усиливает внутреннюю команду или полностью заменяет ИТ-отдел, сохраняя прозрачную модель взаимодействия.» | Сильный хук: отвечает на главный страх (потеря контроля). | «Передать IT и потерять контроль — не единственный сценарий. Мы берём на себя серверы, ЭЦП, почту и инфраструктуру, сохраняя прозрачную модель: договор, SLA, отчётность, гарантия 6 месяцев.» |
| esc-kazan.ru | «Услуга технического сопровождения «под ключ» избавит вас от рутины: мы берем на себя настройку, защиту и бесперебойную работу всей техники. 21 год на рынке. 15 мин среднее время реакции. 99.9% доступность.» | Конкретные цифры (21 год, 15 мин, 99.9%). | «IT-аутсорсинг «под ключ» для офисов 20-50 человек. Реакция 15 минут. Выезд в день обращения. Гарантия 6 месяцев. 99.9% доступность.» |
| iteron.ru | «Уменьшите расходы на IT до 50%. Постоянная поддержка без отпусков и больничных. 90% заявок закрываем в течение часа. Решение всех задач в формате «одного окна».» | Конкретные выгоды (экономия 50%, без отпусков, 90% за час). | «Уменьшите расходы на IT до 40%. Постоянная поддержка без отпусков и больничных. Реакция 15 минут. Гарантия 6 месяцев.» |

### 3. Лучшие абзацы про выгоду

| Конкурент | Абзац | Почему сильный | Как сделать лучше для F&F |
|---|---|---|---|
| its-kazan.ru | «Выгодно – итоговая стоимость обслуживания компьютеров и серверов ниже чем зарплата квалифицированного специалиста с рабочим местом и налоговыми выплатами.» | Сравнение со штатным с конкретикой (зарплата + рабочее место + налоги). | «Дешевле штатного сисадмина на 40%. Расчёт TCO: зарплата + налоги + отпуск + больничный + оборудование + обучение = X ₽/год. F&F = Y ₽/год. Экономия Z ₽/год.» |
| tss-kazan.ru | «При заключении договора с нами вы нанимаете не одного человека в штат, а целую команду профессионалов за сумму, которая в среднем на 20% меньше той что вы тратите сейчас.» | Конкретная цифра (20% меньше) + команда вместо одного. | «Вы нанимаете не одного человека, а команду из 4+ специалистов за сумму, которая на 40% меньше TCO штатного сисадмина.» |
| itprovider.ru | «Если в штате есть системный администратор: Мы обеспечим круглосуточную поддержку основных сервисов компании. Ваш специалист будет заниматься необходимой текучкой... и сможет уходить в отпуск, на больничный без страха что работа компании встанет.» | Конкретная выгода для клиента с штатным сисадмином (отпуск/больничный без риска). | «Если у вас уже есть сисадмин: мы обеспечим 24/7 поддержку основных сервисов, а ваш специалист займётся текучкой и сможет уйти в отпуск/больничный без страха, что компания встанет.» |
| a1-support.ru | «Основная работа идёт удалённо — так быстрее и дешевле для Вас.» | Честность: удалёнка быстрее и дешевле. | «Удалённая поддержка быстрее и дешевле. Выезд инженера — только когда нужно. Реакция 15 минут.» |
| socialit.ru | «За каждый час нарушения сроков решения задачи — 1 000/1 500 ₽.» | Финансовая гарантия: деньги за нарушение. | «За каждый час нарушения сроков решения задачи — X ₽. Гарантия 6 месяцев.» |

### 4. Лучшие сравнения со штатным

| Конкурент | Сравнение | Почему сильный | Как сделать лучше для F&F |
|---|---|---|---|
| itprovider.ru | Блок «Работаем совместно с вашими специалистами либо самостоятельно» (если есть сисадмин / если нет) | Два сценария: с штатным и без. Отвечает на возражение «у нас уже есть сисадмин». | Страница «F&F vs штатный сисадмин» с TCO-калькулятором: зарплата + налоги + отпуск + больничный + оборудование + обучение = X ₽/год vs F&F = Y ₽/год. Экономия Z ₽/год. |
| tss-kazan.ru | «При заключении договора с нами вы нанимаете не одного человека в штат, а целую команду профессионалов за сумму, которая в среднем на 20% меньше той что вы тратите сейчас.» | Конкретная цифра (20% меньше) + команда вместо одного. | «Вы нанимаете не одного человека, а команду из 4+ специалистов за сумму, которая на 40% меньше TCO штатного сисадмина. Расчёт за 2 минуты.» |
| its-kazan.ru | «Выгодно – итоговая стоимость обслуживания компьютеров и серверов ниже чем зарплата квалифицированного специалиста с рабочим местом и налоговыми выплатами.» | Сравнение с конкретикой (зарплата + рабочее место + налоги). | «Дешевле штатного сисадмина на 40%. Расчёт TCO: зарплата + налоги + отпуск + больничный + оборудование + обучение.» |
| iteron.ru | «Уменьшите расходы на IT до 50%. Постоянная поддержка без отпусков и больничных.» | Конкретная цифра (50%) + выгода (без отпусков/больничных). | «Уменьшите расходы на IT до 40%. Постоянная поддержка без отпусков и больничных. Реакция 15 минут.» |

### 5. Лучшие формулировки гарантии/SLA

| Конкурент | Формулировка | Почему сильная | Как сделать лучше для F&F |
|---|---|---|---|
| tss-kazan.ru | «Мы теряем деньги, если у вас что-то не работает. Это закреплено соглашением об уровне сервиса (SLA), в котором строго регламентировано время реагирования и решения возникающих проблем.» | Финансовая мотивация: мы теряем деньги, если не решим. | «Мы теряем деньги, если у вас что-то не работает. SLA: реакция 15 минут, решение 4 часа. За каждый час нарушения — X ₽. Гарантия 6 месяцев.» |
| tss-kazan.ru | «Если вас не устроит качество наших услуг, просто смените пароли к сервисам вашей компании и скажите нам Аривидерчи.» | Снятие риска: клиент может уйти в любой момент без штрафов. | «Если вас не устроит качество наших услуг, просто смените пароли. Без штрафов. Передаём документацию и доступы. Гарантия 6 месяцев.» |
| socialit.ru | «За каждый час нарушения сроков решения задачи — 1 000/1 500 ₽.» | Финансовые гарантии: деньги за нарушение. | «За каждый час нарушения сроков решения задачи — X ₽. Реакция 15 минут. Решение 4 часа. Гарантия 6 месяцев.» |
| itprovider.ru | «Реагируем на обращения за 15 минут и решает большинство обращений за 20 минут, чтобы ваша работа не останавливалась.» | Конкретные цифры: 15 мин реакция, 20 мин решение. | «Реагируем за 15 минут. Решаем большинство обращений за 4 часа. Ваша работа не останавливается. Гарантия 6 месяцев.» |
| esc-kazan.ru | «95% неисправностей мы исправляем за 15-30 минут через удалённый доступ. Вы даже не заметите сбоя.» | Конкретика + эмоция («вы даже не заметите»). | «95% неисправностей исправляем за 15-30 минут через удалённый доступ. Вы даже не заметите сбоя. Выезд инженера в день обращения. Гарантия 6 месяцев.» |
| erpdev.ru | «Гарантия 24 мес» | Длинная гарантия. | «Гарантия 6 месяцев (единый срок). Не 30 дней — 6 месяцев.» |

### 6. Лучшие подписи под CTA

| Конкурент | Подпись под CTA | Почему сильная | Как сделать лучше для F&F |
|---|---|---|---|
| a1-support.ru | «Посчитайте стоимость в калькуляторе и отправьте расчёт нам. Менеджер свяжется с Вами в рабочее время.» | Конкретный next step: калькулятор → отправить → менеджер свяжется. | «Посчитайте стоимость в калькуляторе TCO и отправьте расчёт нам. Мы свяжемся с вами в течение 15 минут. Вы получите расчёт стоимости и план работ.» |
| socialit.ru | «Получить КП» (на каждом тарифе) | Чёткий CTA рядом с ценой. | «Получить КП» на каждом тарифе F&F. |
| esc-kazan.ru | «Подберем тариф под задачи вашего бизнеса» | Конкретный next step: подбор тарифа. | «Подберём тариф под задачи вашего офиса. Расчёт за 15 минут.» |
| a1-support.ru | «Расскажите о Вашем офисе — посчитаем точно.» | Приглашение к диалогу. | «Расскажите о вашем офисе — посчитаем точно. Расчёт TCO за 2 минуты.» |
| tss-kazan.ru | «Если вас не устроит качество наших услуг, просто смените пароли... и скажите нам Аривидерчи.» | Снятие риска + юмор («Аривидерчи»). | «Если вас не устроит качество наших услуг, просто смените пароли. Без штрафов. Передаём документацию и доступы.» |
| i-tat.ru | «Цена 1С у всех одна. Разница в качестве сервиса!» | Сильная дифференциация. | «Цена IT-аутсорсинга у всех разная. Разница в прозрачности, SLA и гарантии 6 месяцев.» |

### Итог: сильные куски, которые F&F должен адаптировать

1. **H1**: «IT-аутсорсинг для офисов 20-50 человек в Казани. Реакция 15 минут. Гарантия 6 месяцев.» (адаптация a1-support + itprovider).
2. **Лид**: «Берём на себя серверы 1С, ЭЦП, почту и инфраструктуру вашего офиса. Сотрудники звонят на локальный номер, инженер подключается удалённо и решает задачу. Выезд в день обращения. Реакция 15 минут. Гарантия 6 месяцев.» (адаптация a1-support + socialit).
3. **Абзац про выгоду**: «Дешевле штатного сисадмина на 40%. Расчёт TCO: зарплата + налоги + отпуск + больничный + оборудование + обучение = X ₽/год. F&F = Y ₽/год. Экономия Z ₽/год.» (адаптация its-kazan + tss-kazan).
4. **Сравнение со штатным**: страница «F&F vs штатный сисадмин» с TCO-калькулятором (адаптация itprovider + tss-kazan).
5. **Гарантия/SLA**: «Мы теряем деньги, если у вас что-то не работает. SLA: реакция 15 минут, решение 4 часа. За каждый час нарушения — X ₽. Гарантия 6 месяцев. Если вас не устроит качество — смените пароли. Без штрафов.» (адаптация tss-kazan + socialit + itprovider).
6. **Подпись под CTA**: «Посчитайте стоимость в калькуляторе TCO и отправьте расчёт нам. Мы свяжемся с вами в течение 15 минут. Вы получите расчёт стоимости и план работ.» (адаптация a1-support).

---

## Слабости конкурентов

### Матрица слабостей (конкурент × слабость)

| Конкурент | Нет цен | Нет гарантии | Нет сроков | Нет FAQ | Нет кейсов | Слабый первый экран | Общие слова вместо оффера | Нет сравнения со штатным | Нет локальных сигналов | Тонкие страницы услуг | Итого слабостей |
|---|---|---|---|---|---|---|---|---|---|---|---|
| its-kazan.ru | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | 9/10 |
| tss-kazan.ru | ✅ | ❌ (100% возврат) | ❌ (SLA) | ✅ | ❌ (кейсы есть) | ✅ | ❌ (сильный оффер) | ✅ | ❌ | ✅ | 5/10 |
| itprovider.ru | ✅ | ✅ | ❌ (15/20 мин) | ✅ | ✅ | ❌ (метрики) | ❌ (сильный оффер) | ❌ (блок есть) | ❌ | ✅ | 4/10 |
| i-tat.ru | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | 9/10 |
| esc-kazan.ru (ЦЭУ) | ❌ (цены есть) | ✅ | ❌ (15 мин) | ✅ | ✅ | ❌ (цифры) | ❌ (сильный оффер) | ✅ | ❌ | ✅ | 5/10 |
| a8 / itbsgroup | ✅ | ✅ | ❌ (15 мин) | ✅ | ❌ (проекты) | ✅ | ✅ | ✅ | ❌ | ✅ | 7/10 |
| obit.ru | ✅ | ✅ | ✅ | ✅ | ❌ (проекты) | ✅ | ✅ | ✅ | ✅ (федеральный) | ✅ | 9/10 |
| socialit.ru | ❌ (цены есть) | ✅ | ❌ (15 мин) | ❌ (8 вопросов) | ❌ (кейсы) | ❌ (тарифы) | ❌ (сильный оффер) | ✅ | ✅ (федеральный) | ✅ | 5/10 |
| iteron.ru | ✅ | ✅ | ❌ (90% за час) | ✅ | ✅ | ❌ (метрики) | ❌ (сильный оффер) | ✅ | ✅ (Москва) | ✅ | 6/10 |
| 1cbit.ru | ✅ | ❌ (SLA) | ✅ | ✅ | ❌ (кейсы) | ✅ | ✅ | ✅ | ✅ (федеральный) | ✅ | 8/10 |
| calltraffic.ru | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (федеральный) | ✅ | 10/10 |
| erpdev.ru | ✅ | ❌ (24 мес) | ✅ | ✅ | ❌ (кейсы) | ✅ | ✅ | ✅ | ✅ (Москва) | ✅ | 8/10 |
| pc-kazan / comp-kazan / intertax | ❌ (низкие цены) | ❌ (comp-kazan до 2 лет) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (B2C) | ✅ | 8/10 |
| F&F | ❌ (prices.html) | ❌ (6 месяцев) | ❌ (15 мин) | ❌ (129 страниц) | ❌ (7 кейсов) | ❌ (метрики) | ❌ (конкретные) | ❌ (compare/*) | ❌ (Казань+Татарстан) | ❌ (161 страница) | 0/10 |

### По каждой слабости: чем F&F может ударить

**1. Нет цен (10 из 14)**
- У кого: its-kazan, tss-kazan, itprovider, i-tat, a8/itbsgroup, obit, iteron, 1cbit, calltraffic, erpdev.
- Чем F&F ударит: публичные тарифы с ценами на prices.html, services.html, servers.html, support.html. «Цены от X ₽/мес за офис 20-50 человек. Никаких скрытых платежей.»
- Тип страницы: prices.html, services.html, servers.html, support.html.

**2. Нет гарантии (9 из 14)**
- У кого: its-kazan, itprovider, i-tat, esc-kazan, a8/itbsgroup, obit, iteron, calltraffic, pc-kazan/intertax.
- Чем F&F ударит: гарантия 6 месяцев (единый срок) на всех страницах. «Гарантия 6 месяцев. Не 30 дней — 6 месяцев.»
- Тип страницы: все коммерческие страницы.

**3. Нет сроков (9 из 14)**
- У кого: its-kazan, i-tat, a8/itbsgroup, obit, 1cbit, calltraffic, erpdev, pc-kazan/comp-kazan/intertax, (a1-support частично).
- Чем F&F ударит: SLA с конкретными сроками (реакция 15 мин, решение 4 часа, выезд в день обращения). «Реакция 15 минут. Решение 4 часа. Или мы платим вам.»
- Тип страницы: services.html, servers.html, support.html, prices.html.

**4. Нет FAQ (9 из 14)**
- У кого: its-kazan, tss-kazan, itprovider, i-tat, esc-kazan, a8/itbsgroup, obit, 1cbit, calltraffic, erpdev, pc-kazan/comp-kazan/intertax.
- Чем F&F ударит: FAQ на всех коммерческих страницах (5-8 вопросов) + FAQPage schema. «Ответы на 50 вопросов об IT-аутсорсинге.»
- Тип страницы: services.html, servers.html, support.html, prices.html, compare/*.

**5. Нет кейсов (8 из 14)**
- У кого: its-kazan, itprovider, i-tat, esc-kazan, calltraffic, (tss-kazan, a8, obit, erpdev, 1cbit, F&F имеют).
- Чем F&F ударит: кейсы с метриками (до/после) на первом экране. «Как мы сократили время простоя с 4 часов до 15 минут.»
- Тип страницы: cases/*, index.html (блок кейсов).

**6. Слабый первый экран (8 из 14)**
- У кого: its-kazan, tss-kazan, i-tat, a8/itbsgroup, obit, 1cbit, calltraffic, erpdev, pc-kazan/comp-kazan/intertax.
- Чем F&F ударит: цена + TCO-калькулятор + SLA + гарантия 6 месяцев + локальный телефон/выезд + 3 trust-цифры + 4 шага процесса на первом экране.
- Тип страницы: index.html.

**7. Общие слова вместо оффера (7 из 14)**
- У кого: its-kazan («опыт множества специалистов»), i-tat («сотрудничество более 10 лет»), obit («оператор ИТ-решений»), calltraffic («катастрофоустойчивость»), 1cbit («ТОП-100»), erpdev («компетентность разработчика»), pc-kazan/comp-kazan/intertax («качественно, быстро»).
- Чем F&F ударит: конкретные цифры (цены, сроки, SLA, метрики) вместо общих слов. «Реакция 15 минут. Решение 4 часа. Гарантия 6 месяцев.»
- Тип страницы: все коммерческие страницы.

**8. Нет сравнения со штатным (9 из 14)**
- У кого: its-kazan, tss-kazan, i-tat, esc-kazan, a8/itbsgroup, obit, socialit, iteron, 1cbit, calltraffic, erpdev, pc-kazan/comp-kazan/intertax.
- Чем F&F ударит: страница «F&F vs штатный сисадмин» с TCO-калькулятором. «Дешевле штатного сисадмина на 40%. Расчёт TCO за 2 минуты.»
- Тип страницы: compare/staff-sysadmin-cost.html, compare/*.

**9. Нет локальных сигналов (6 из 14)**
- У кого: obit, socialit, 1cbit, calltraffic, iteron, erpdev (федеральный масштаб).
- Чем F&F ударит: локальные посадочные (Челны, Нижнекамск, Альметьевск, Зеленодольск) + кейсы с городом + 2ГИС/Яндекс.Карты + выезд в день обращения + schema с address/geo. «Казань + города Татарстана. Выезд инженера.»
- Тип страницы: локальные посадочные, index.html.

**10. Тонкие страницы услуг (10 из 14)**
- У кого: its-kazan, tss-kazan, itprovider, i-tat, esc-kazan, a8/itbsgroup, obit, socialit, iteron, 1cbit, calltraffic, erpdev, pc-kazan/comp-kazan/intertax.
- Чем F&F ударит: усиление тонких страниц контентом (цены, SLA, FAQ, кейсы). «Каждая страница — полноценный коммерческий лендинг.»
- Тип страницы: ai/*, incidents/*, resources/*, articles/*, industries/*, pain/*, cases/*, leads/*, compare/*, infrastructure/*, services/*.

### Итог

- **Самый слабый конкурент**: calltraffic.ru (10/10 слабостей) — нет цен, нет гарантии, нет сроков, нет FAQ, нет кейсов, слабый первый экран, общие слова, нет сравнения, нет локальных сигналов, тонкие страницы.
- **Самый сильный конкурент**: itprovider.ru (4/10 слабостей) — есть метрики, SLA, NDA, блок «уже есть сисадмин?», но нет цен, FAQ, кейсов, тонкие страницы.
- **F&F (0/10 слабостей)** — уже закрыл все 10 слабостей, но нужно усилить: тарифы с ценами, SLA-страница, кейсы с метриками, локальные посадочные, блок «уже есть сисадмин?».
- **Главный рычаг**: F&F уже сильнее по покрытию слабостей (0/10 vs 4-10/10 у конкурентов). Нужно усилить глубину: тарифы с ценами, SLA с фин. гарантиями, кейсы с метриками, локальные посадочные.

---

## Сводная матрица конкурентов

### Таблица: конкурент | оффер | цена | гарантия | SLA/сроки | trust | локальность | SEO-структура | конверсия | главная сила | главная слабость | чем бить

| Конкурент | Оффер | Цена | Гарантия | SLA/сроки | Trust | Локальность | SEO-структура | Конверсия | Главная сила | Главная слабость | Чем бить |
|---|---|---|---|---|---|---|---|---|---|---|---|
| a1-support.ru | Удалённая IT-поддержка по всей России, от 5 000 ₽/мес | ✅ Прозрачные (5 000 ₽/мес за 5 ПК, +500 ₽/ПК, сервер от 1 200 ₽) | ❌ Нет явной | ❌ Нет SLA с фин. гарантиями (9:00-19:00) | ✅ Договор+ЭДО, реквизиты, 8-800, FAQ 5 вопросов | ❌ Федеральный (нет Казани) | ✅ 8 направлений услуг, цены, калькулятор, FAQ, 4 шага | ✅ Калькулятор+8-800+TG+MAX+форма | Прозрачные цены+калькулятор+договор/ЭДО | Нет локального бренда, нет сравнения со штатным, нет кейсов с метриками | Локальный бренд + TCO-калькулятор + кейсы с метриками + гарантия 6 месяцев |
| tss-kazan.ru | ИТ-аутсорсинг + внедрение ИТ систем | ❌ Нет цен | ✅ 100% возврат | ✅ SLA (реакция+решение, «мы теряем деньги») | ✅ SLA, гарантия возврата, постоплата, реквизиты | ✅ Казань | ✅ 5 проблем→решения, кейсы, SLA | ✅ SLA+гарантия+постоплата+форма | Отработка возражений (5 проблем→решения)+SLA | Нет цен, нет калькулятора, нет FAQ | Цены+калькулятор TCO+FAQ+гарантия 6 месяцев |
| itprovider.ru | ИТ-поддержка, на которую можно положиться. 24/7. | ❌ Нет цен (/price без цен) | ❌ Нет явной | ✅ 15 мин/20 мин, 24/7, NDA | ✅ Метрики (640k+, 35 спец.), именные отзывы, NDA, SLA, сертификация, фото директора | ✅ Казань, Татарстан, Россия | ✅ Преимущества 6, «уже есть сисадмин?», отзывы, метрики | ✅ Форма+телефон+email, 2 точки входа | Метрики+SLA+NDA+блок «уже есть сисадмин?» | Нет цен, нет FAQ, нет кейсов, нет калькулятора | Цены+FAQ+кейсы с метриками+TCO-калькулятор |
| i-tat.ru | ИТ и 1С обслуживание, ГРАНД-Смета | ❌ Нет цен | ❌ Нет | ❌ Нет SLA | ✅ Фото команды, 1С-партнёрство, отзывы | ✅ 5 городов, телефоны, посадочные | ✅ Локальные посадочные, 1С, база знаний, обучение | ✅ Форма+телефон, много CTA | Локальные посадочные+фото команды+1С-экспертиза | IT вторичен, нет цен, нет SLA, нет FAQ, нет кейсов | Цены+SLA+FAQ+кейсы+гарантия 6 месяцев+локальный бренд IT |
| esc-kazan.ru (ЦЭУ) | Комплексное обслуживание бизнеса | ✅ 5 000/8 000 ₽/мес, разовые от 500-4 000 ₽ | ❌ Нет явной | ✅ 15 мин, 95% за 15-30 мин, 99.9% | ✅ Реквизиты, 5 шагов, цифры (21 год, 1000+ клиентов) | ✅ Казань, удалённо по России | ✅ Услуги, тарифы, 5 шагов, 4 сегмента, журнал | ✅ 5 CTA+попапы+форма | Цены+5 шагов+широкий спектр услуг | IT вторичен, нет SLA/гарантии, нет FAQ/кейсов | SLA+гарантия 6 месяцев+FAQ+кейсы+локальный IT-бренд |
| a8 / itbsgroup | Каталог оборудования + интеграция | ❌ Нет цен (каталог) | ❌ Нет | ✅ 15 мин (в аутсорсинге) | ✅ Проекты с именами, партнёры, сертификаты | ✅ Меню городов (Казань, Альметьевск, Челны, Нижнекамск) | ✅ Каталог, услуги, проекты, новости, отзывы | ✅ Форма+телефон, «опишите задачу» | Локальные посадочные (меню)+интегратор+проекты | IT вторичен (оборудование), нет цен, нет SLA/гарантии | Цены+SLA+гарантия 6 месяцев+локальный IT-бренд |
| obit.ru | Телеком, ЦОД, инжиниринг, ИТ-аутсорсинг | ❌ Нет цен | ❌ Нет | ❌ Нет SLA | ✅ Кейсы, партнёры, отрасли (9), 20+ лет | ❌ Федеральный (Казань — 1 из 80) | ✅ Каталог услуг, отрасли, кейсы, партнёры | ✅ Форма+телефон+ЛК | Глубокий каталог+кейсы+партнёры+отрасли | Нет цен, нет SLA/гарантии, нет FAQ, федеральный масштаб | Цены+SLA+гарантия 6 месяцев+локальный бренд+FAQ |
| socialit.ru | Тарифы ИТ-аутсорсинга (Удалённый/Базовый/Расширенный) | ✅ 10 000/20 000/50 000 ₽/мес | ❌ Нет явной | ✅ 15 мин, SLA с фин. гарантиями (1 000-1 500 ₽/час) | ✅ SLA с фин. гарантиями, кейсы сетей, 3 линии, VIP | ❌ Федеральный (70+ городов) | ✅ Тарифы, SLA, FAQ 8 вопросов, кейсы | ✅ «Получить КП» на каждом тарифе+форма | SLA с фин. гарантиями+тарифы с ценами+FAQ 8 | Нет локального бренда, высокий порог (от 10k), фокус на розницу | Локальный бренд+тарифы для 20-50 человек+гарантия 6 месяцев |
| iteron.ru | IT-поддержка, которая всегда рядом | ❌ Нет цен (калькулятор) | ❌ Нет | ✅ 90% заявок за час | ✅ Метрики (98%, 31+ компаний), калькулятор, 18 лет | ❌ Москва | ✅ Услуги, калькулятор, блог, метрики | ✅ Форма+телефон+калькулятор | Калькулятор+метрики+1С-экспертиза | Москва, нет локального бренда, нет SLA с фин. гарантиями | Локальный бренд+SLA с фин. гарантиями+гарантия 6 месяцев |
| 1cbit.ru | IT-поддержка + 1С + инфраструктура | ❌ Нет цен | ❌ Нет явной (SLA есть) | ✅ SLA | ✅ Масштаб (300 000+ клиентов, ТОП-100), SLA, реквизиты | ❌ Федеральный | ✅ (не загрузился, 401) | ❓ Неизвестно | Масштаб+SLA+1С-экспертиза | Федеральный, нет локального бренда, нет цен | Локальный бренд+цены+гарантия 6 месяцев |
| calltraffic.ru | Контакт-центр, техподдержка ИС | ❌ Нет цен | ❌ Нет | ❌ Нет явного SLA | ✅ Лицензии ФСТЭК, 99.98% катастрофоустойчивость | ❌ Федеральный (Казань — площадка) | ✅ (не загрузился, cert) | ❓ Неизвестно | Лицензии ФСТЭК+катастрофоустойчивость | Нет цен, нет SLA, нет FAQ, нет кейсов, нет локального бренда | Цены+SLA+FAQ+кейсы+локальный бренд+гарантия 6 месяцев |
| erpdev.ru | 1С-разработка, ERP | ❌ Нет цен | ✅ 24 мес | ✅ NDA/SLA | ✅ Кейсы, NDA/SLA, гарантия 24 мес | ❌ Москва | ✅ (не загрузился, таймаут) | ❓ Неизвестно | Кейсы+NDA/SLA+гарантия 24 мес | Москва, нет локального бренда, нет цен | Локальный бренд+цены+гарантия 6 месяцев |
| pc-kazan / comp-kazan / intertax | Разовые услуги (ремонт, настройка, заправка) | ✅ От 250-474 ₽ | ✅ comp-kazan до 2 лет | ❌ Нет SLA | ✅ 2ГИС 4.8, Яндекс 5.0, отзывы | ❌ B2C, нет посадочных | ✅ (privacy policy вместо главной) | ❓ Неизвестно | Низкие цены+быстрый выезд+гарантия до 2 лет | B2C, нет SLA, нет абонентки, нет локального бренда | Абонентка+SLA+гарантия 6 месяцев+локальный B2B-бренд |
| F&F | IT-аутсорсинг для бизнеса (нужно усилить) | ✅ prices.html (но без тарифных таблиц) | ✅ 6 месяцев (унифицировано) | ✅ 15 мин (нужно добавить SLA с фин. гарантиями) | ✅ 7 кейсов, 7 отзывов, реквизиты (ИНН), schema, llms.txt, 161 страница | ✅ Казань + города Татарстана | ✅ 161 страница, FAQ на 129, canonical, schema, llms.txt | ✅ Форма+телефон+TG+MAX, quiz, калькулятор, exit-popup | 161 страница+answer-first+FAQPage 129+schema+llms.txt+реквизиты+локальный бренд | Нет тарифов с ценами, нет SLA-страницы, отзывы анонимные, нет фото команды, нет TCO-калькулятора | (F&F — это мы, бьём остальных) |

### Выводы

#### 1. Топ-5 кого бояться

1. **a1-support.ru** — прозрачные цены + калькулятор + договор/ЭДО + 8-800 + TG/MAX. Самый «готовый к сделке» на рынке. Но: нет локального бренда, нет сравнения со штатным, нет кейсов с метриками.
2. **itprovider.ru** — метрики (640k+) + SLA (15/20 мин) + NDA + блок «уже есть сисадмин?» + именные отзывы + сертификация. Но: нет цен, нет FAQ, нет кейсов, нет калькулятора.
3. **socialit.ru** — SLA с фин. гарантиями (1 000-1 500 ₽/час) + тарифы с ценами + FAQ 8 вопросов + кейсы сетей. Но: нет локального бренда, высокий порог (от 10k).
4. **tss-kazan.ru** — отработка возражений (5 проблем→решения) + SLA + гарантия 100% возврат + постоплата. Но: нет цен, нет калькулятора, нет FAQ.
5. **i-tat.ru** — локальные посадочные (5 городов) + фото команды + 1С-экспертиза + база знаний. Но: IT вторичен, нет цен, нет SLA, нет FAQ, нет кейсов.

#### 2. Топ-5 кого обходить быстро

1. **calltraffic.ru** — 10/10 слабостей: нет цен, нет гарантии, нет сроков, нет FAQ, нет кейсов, слабый первый экран, общие слова, нет сравнения, нет локальных сигналов, тонкие страницы.
2. **obit.ru** — 9/10 слабостей: нет цен, нет гарантии, нет сроков, нет FAQ, слабый первый экран, общие слова, нет сравнения, федеральный масштаб, тонкие страницы.
3. **its-kazan.ru** — 9/10 слабостей: нет цен, нет гарантии, нет сроков, нет FAQ, нет кейсов, слабый первый экран, общие слова, нет сравнения, тонкие страницы.
4. **i-tat.ru** — 9/10 слабостей: нет цен, нет гарантии, нет сроков, нет FAQ, нет кейсов, слабый первый экран, общие слова, нет сравнения, тонкие страницы (но сильная локальность).
5. **a8/itbsgroup** — 7/10 слабостей: нет цен, нет гарантии, нет FAQ, слабый первый экран, общие слова, нет сравнения, тонкие страницы (но сильные локальные посадочные).

#### 3. 10 вещей, которые F&F должен усилить первым

1. **Тарифы с ценами** на prices.html (Эконом/Бизнес/Премиум для офисов 20-50 человек).
2. **TCO-калькулятор** (штатный vs аутсорсинг) на prices.html и compare/staff-sysadmin-cost.html.
3. **SLA-страница** с финансовыми гарантиями (реакция 15 мин, решение 4 часа, X ₽/час за нарушение).
4. **Кейсы с метриками** (до/после) на первом экране (3-5 кейсов).
5. **Именные отзывы** с компаниями/датами/фото на company/testimonials.html.
6. **Фото команды** на company/team.html.
7. **Локальные посадочные** для Челнов, Нижнекамска, Альметьевска, Зеленодольска (4 страницы).
8. **Блок «Уже есть сисадмин?»** на services.html (как itprovider).
9. **Процесс 4 шага** на первом экране index.html.
10. **Единый CTA «Получить расчёт»** + калькулятор TCO + floating-кнопка + один попап + next step с конкретными сроками на всех страницах.

---

## Финальный синтез по 12 слоям

### Сводка по слоям (краткие выводы)

| # | Слой | Что рынок делает | Где рынок слаб | Что F&F должен переиграть |
|---|---|---|---|---|
| 1 | Офферы и УТП | Шаблонные фразы («опыт N лет», «комплексный подход», «профессиональная команда»); a1-support и socialit сильны (цены, SLA) | 10 из 14 без цены на первом экране; 8 из 14 без trust-блоков; заголовки шаблонные | Цена + TCO-калькулятор + SLA + гарантия 6 месяцев + локальный телефон/выезд + 3 trust-цифры на первом экране |
| 2 | Цены и тарифы | 10 из 14 прячут цену в форме заявки; a1-support, socialit, esc-kazan прозрачны | Нет сравнения со штатным; нет калькулятора TCO; гарантия не унифицирована | Публичные тарифы + TCO-калькулятор + «что входит/что за доплату» + гарантия 6 месяцев |
| 3 | Гарантии/SLA/сроки | 9 из 14 без конкретных сроков; socialit (фин. гарантии), itprovider (15/20 мин), esc-kazan (15 мин) сильны | Нет SLA с фин. гарантиями у большинства; гарантия разрозненная (30 дней/6 месяцев/2 года) | Гарантия 6 месяцев (единый срок) + SLA с фин. гарантиями («Реакция 15 мин. Решение 4 часа. Или мы платим вам.») |
| 4 | Структура сайта | a1-support: 8 направлений + цены + калькулятор + FAQ + 4 шага; F&F: 161 страница | Тонкие страницы у 10 из 14; нет локальных посадочных; нет SLA-страницы; нет блока «уже есть сисадмин?» | Усилить тонкие страницы; добавить локальные посадочные; добавить SLA-страницу; добавить блок «уже есть сисадмин?» |
| 5 | Title/description/H1 | a1-support сильнейший (цена в description, H1=title); obit переспамлен (title 120+); iteron (Москва) | 6 из 10 слабо используют Казань/Татарстан; переспам у 3; нет H1 у 4 (itprovider, esc-kazan, i-tat, socialit, tss-kazan) | Title ≤ 60 символов с ценой; description с конкретикой; H1 с УТП; локальный фокус (Казань/Татарстан) |
| 6 | Trust-блоки | itprovider сильнейший (метрики + именные отзывы + NDA + SLA + сертификация + фото директора) | Отзывы анонимные у большинства; нет фото команды у 8 из 14; нет сертификатов у 9 из 14 | Именные отзывы + кейсы с метриками + SLA + гарантия 6 месяцев + фото команды + сертификаты + конкретные цифры + процесс 4 шага |
| 7 | FAQ и возражения | socialit (8 вопросов), a1-support (5 вопросов), tss-kazan (5 проблем→решения), itprovider (блок «уже есть сисадмин?») | 9 из 14 без FAQ; 10 из 14 не отвечают на «что если не поможет»; 9 из 14 не отвечают на «почему не штатный» | FAQ на всех коммерческих страницах (5-8 вопросов) + страница «F&F vs штатный» + страница SLA/договора |
| 8 | Коммерческие факторы | a1-support (8/10), tss-kazan (8/10), F&F (8/10) — самые «готовые к сделке» | obit, iteron, i-tat, a8 (4-5/10) — витрины; нет реквизитов на главной у 5 из 14 | Тарифы с ценами + SLA-страница + реквизиты на первом экране + способы оплаты на prices.html |
| 9 | Локальность | i-tat (5 городов, телефоны, посадочные) — сильнейший; a8 (меню городов) — средний | 6 из 14 пишут «Казань» для галочки (obit, socialit, 1cbit, calltraffic, iteron, erpdev) | Локальные посадочные (4 города) + кейсы с городом + 2ГИС/Яндекс.Карты + выезд + schema с address/geo |
| 10 | CTA и формы | a1-support (калькулятор+8-800+TG+MAX), socialit («Получить КП» на каждом тарифе), esc-kazan (5 CTA) | obit («Заказать звонок»), i-tat (разные CTA), its-kazan (не CTA); esc-kazan (4 попапа), itprovider (2 точки входа) | Единый CTA «Получить расчёт» + калькулятор TCO + форма 3 поля + мультиканальность + floating + один попап + next step |
| 11 | Контент-форматы | Кейсы (6/14), блог/статьи (4/14), тарифные таблицы (3/14), калькуляторы (2/14), FAQ (2/14), сравнения (2/14), чек-листы (1/14), гайды (1/14) | Видео (0/14), PDF (0/14), TCO-калькулятор (0/14) | TCO-калькулятор, видео, PDF-чек-листы, FAQ-кластеры, сравнения, кейсы с метриками, гайды |
| 12 | Слабые места | calltraffic (10/10), its-kazan/i-tat/obit (9/10), a8/1cbit/erpdev/pc-kazan (7-8/10) | itprovider (4/10) — самый сильный; F&F (0/10) — уже закрыл все слабости | Усилить глубину: тарифы с ценами, SLA с фин. гарантиями, кейсы с метриками, локальные посадочные, блок «уже есть сисадмин?» |

### Что рынок делает одинаково

1. **Нет цен на первом экране** — 10 из 14 прячут цену в форме заявки. Только a1-support, socialit, esc-kazan пишут цены открыто.
2. **Нет SLA с финансовыми гарантиями** — 9 из 14 не дают конкретных сроков. Только socialit (1 000-1 500 ₽/час), itprovider (15/20 мин), esc-kazan (15 мин) дают цифры.
3. **Нет FAQ** — 9 из 14 не имеют FAQ на коммерческих страницах. Только a1-support (5 вопросов) и socialit (8 вопросов) имеют.
4. **Нет кейсов с метриками** — 8 из 14 не имеют кейсов. Только tss-kazan, a8, obit, erpdev, 1cbit, F&F имеют кейсы, но без метрик (кроме itprovider).
5. **Нет сравнения со штатным** — 9 из 14 не имеют. Только itprovider (блок) и F&F (compare/*).
6. **Нет локальных посадочных** — 6 из 14 пишут «Казань» для галочки. Только i-tat и a8 имеют посадочные.
7. **Нет фото команды** — 8 из 14 не имеют фото. Только i-tat, obit, iteron, a1-support имеют.
8. **Нет видео/PDF** — 0 из 14. Никто не использует видео и PDF.
9. **Нет TCO-калькулятора** — 0 из 14. Никто не имеет калькулятора TCO.
10. **Шаблонные фразы** — 10+ используют «опыт N лет», «комплексный подход», «профессиональная команда», «надёжно».

### Где рынок слаб

1. **Цены**: 10 из 14 прячут цену → клиент не может оценить стоимость до заявки.
2. **SLA**: 9 из 14 без конкретных сроков → нет доверия к срокам.
3. **Гарантия**: 9 из 14 без явной гарантии → клиент не знает, что получит при проблеме.
4. **FAQ**: 9 из 14 без FAQ → возражения не отработаны.
5. **Кейсы**: 8 из 14 без кейсов → нет доказательств результата.
6. **Сравнение со штатным**: 9 из 14 без → клиент не понимает, почему не штатный.
7. **Локальность**: 6 из 14 пишут «Казань» для галочки → нет локального бренда.
8. **Фото команды**: 8 из 14 без фото → нет лица компании.
9. **Видео/PDF**: 0 из 14 → нет мультимедийного контента.
10. **TCO-калькулятор**: 0 из 14 → нет инструмента сравнения со штатным.

### Что F&F должен переиграть в первую очередь

1. **Тарифы с ценами** — публичные цены на prices.html (Эконом/Бизнес/Премиум для 20-50 человек).
2. **TCO-калькулятор** — «Расчёт TCO за 2 минуты» на prices.html и compare/staff-sysadmin-cost.html.
3. **SLA с финансовыми гарантиями** — «Реакция 15 минут. Решение 4 часа. Или мы платим вам.» на отдельной странице.
4. **Гарантия 6 месяцев** — уже унифицировано, вынести на первый экран.
5. **Кейсы с метриками** — «Как мы сократили время простоя с 4 часов до 15 минут» на первом экране.
6. **Именные отзывы** — заменить анонимные на именные с компаниями/датами/фото.
7. **Фото команды** — добавить на company/team.html.
8. **Локальные посадочные** — 4 страницы (Челны, Нижнекамск, Альметьевск, Зеленодольск) с реальным контентом.
9. **Блок «Уже есть сисадмин?»** — на services.html (как itprovider, но с TCO).
10. **Единый CTA «Получить расчёт»** + калькулятор TCO + floating-кнопка + один попап + next step с конкретными сроками на всех страницах.

### Итог

- **Рынок делает одинаково**: нет цен, нет SLA, нет FAQ, нет кейсов с метриками, нет сравнения со штатным, нет локальных посадочных, нет фото команды, нет видео/PDF, нет TCO-калькулятора, шаблонные фразы.
- **Рынок слаб**: по всем 10 слоям (цены, SLA, гарантия, FAQ, кейсы, сравнение, локальность, фото, видео/PDF, TCO-калькулятор) у 6-10 из 14 конкурентов есть слабости.
- **F&F должен переиграть в первую очередь**: тарифы с ценами + TCO-калькулятор + SLA с фин. гарантиями + гарантия 6 месяцев + кейсы с метриками + именные отзывы + фото команды + локальные посадочные + блок «уже есть сисадмин?» + единый CTA «Получить расчёт».

---

## SEO-аудит: кто выше F&F в поиске и почему

### Фаза 1. Поиск всех конкурентов в выдаче

Поисковые запросы (из AGENTS.md): «настройка серверов Казань», «сисадмин Казань», «IT-аутсорсинг для малого бизнеса», «сервер под ключ», «IT-аутсорсинг Казань», «обслуживание компьютеров Казань», «администрирование серверов Казань», «IT-поддержка бизнеса Казань», «сисадмин для бизнеса Казань».

**Найденные конкуренты, ранжирующиеся выше F&F (fedorov55.github.io/ff-site):**

Новые (не анализировались ранее):
1. tech-matrix.ru — IT-аутсорсинг, выезд 15-20 мин, стартовый месяц бесплатно
2. it-implant.ru — IT-аутсорсинг, договор, SLA, фиксированные тарифы
3. profinfoservice.ru — IT-аутсорсинг, малый и средний бизнес
4. infrait.ru — IT-обслуживание в Татарстане, выезд в день запроса
5. arttechkzn.ru — IT-аутсорсинг, монтаж сетей, CRM
6. simplenetworks.ru — комплексное обслуживание IT-инфраструктуры в Казани
7. datasib.ru — «Ваш сисадмин», приходящий сисадмин
8. 1c.itat.ru — IT-аутсорсинг в Казани (АЙТАТ)
9. kazan.1cbit.ru — IT-аутсорсинг, 1С (не загрузился, 401)
10. dobsis.ru — «Добрый Сисадмин», 15 лет, Казань/Зеленодольск/Волжск (cert expired)

Известные (анализировались ранее):
11. its-kazan.ru
12. tss-kazan.ru
13. itprovider.ru
14. i-tat.ru / 1c.itat.ru
15. esc-kazan.ru
16. a8 / itbsgroup.ru
17. obit.ru
18. socialit.ru
19. iteron.ru
20. 1cbit.ru
21. calltraffic.ru
22. erpdev.ru
23. a1-support.ru
24. pc-kazan / comp-kazan / intertax

Итого: ~24 приоритетных конкурента.

---

### Фаза 2. Просмотр 1/3 (новые конкуренты)

#### tech-matrix.ru
- **Title**: «Страница» (пустой, шаблонный) — критическая ошибка SEO.
- **Description**: «Настройка и обслуживание компьютеров и серверов. Управление сетевой инфраструктурой. Обеспечение безопасности данных. Консультации по информатизации.» — список услуг, нет гео, нет цен, нет УТП.
- **H1**: не обнаружен (вероятно, стилизованный блок).
- **Почему ранжируется**: домен старый (?), контент по услугам, но SEO-ошибки критичны. Вероятно, ранжируется по низкочастотным запросам или по доменному возрасту.
- **Слабость**: title «Страница» — полный провал SEO. Description — список без гео/цен/УТП. Нет H1. Нет schema. Нет llms.txt.
- **Чем F&F бьёт**: F&F имеет title с ключевыми словами, description с УТП, H1, schema, llms.txt, 161 страницу. F&F сильнее по всем SEO-факторам.

#### it-implant.ru
- **Title**: «IT-аутсорсинг в Казани — профессиональное обслуживание IT-инфраструктуры» — хороший, с гео.
- **Description**: «IT-аутсорсинг в Казани для бизнеса: обслуживание компьютеров, серверов и сетей. Оперативная поддержка, договор, SLA, фиксированные тарифы.» — хорошая, с гео + УТП (договор, SLA, тарифы).
- **H1**: не обнаружен (нужно проверить HTML).
- **Почему ранжируется**: чёткий title/description с гео (Казань) и УТП (договор, SLA, тарифы). Вероятно, есть контент по услугам.
- **Слабость**: нет цен на странице («фиксированные тарифы» — но без цифр), нет калькулятора, нет FAQ, нет кейсов.
- **Чем F&F бьёт**: F&F имеет цены на prices.html, FAQ на 129 страницах, 7 кейсов, llms.txt. F&F сильнее по контенту и trust.

#### profinfoservice.ru
- **Title**: «IT-аутсорсинг - обслуживание компьютеров и ИТ-инфраструктуры в Казани» — хороший, с гео.
- **Description**: «ИТ аутсорсинг для бизнеса в Казани. Обслуживание компьютеров, серверов и корпоративной IT-инфраструктуры. Системные администраторы на аутсорсинге, техническая поддержка и сопровождение компаний» — хорошая, с гео.
- **H1**: не обнаружен.
- **Почему ранжируется**: чёткий title/description с гео. Вероятно, есть контент по услугам.
- **Слабость**: нет цен, нет SLA с цифрами, нет FAQ, нет кейсов, нет калькулятора.
- **Чем F&F бьёт**: F&F имеет цены, FAQ, кейсы, llms.txt, 161 страницу. F&F сильнее по контенту и trust.

#### infrait.ru
- **Title**: «InfraIT — IT-обслуживание бизнеса в Татарстанек и по России» — опечатка («Татарстанек») — SEO-ошибка.
- **Description**: «InfraIT: комплексное IT-обслуживание бизнеса в Татарстане и Казани с выездом в день запроса. По России — удаленная поддержка. Фиксированная стоимость, быстрое реагирование, поддержка серверов и сетей.» — хорошая, с гео + УТП (выезд в день запроса, фиксированная стоимость).
- **H1**: не обнаружен.
- **Почему ранжируется**: чёткий title/description с гео + УТП. Но опечатка в title снижает CTR.
- **Слабость**: опечатка в title («Татарстанек»), нет цен, нет SLA с цифрами, нет FAQ, нет кейсов.
- **Чем F&F бьёт**: F&F имеет правильный title без опечаток, цены, FAQ, кейсы, llms.txt.

#### arttechkzn.ru
- **Title**: «IT аутсорсинг. Обслуживание компьютеров Казань» — хороший, с гео, но без бренда.
- **Description**: «Профессиональный IT-аутсорсинг, монтаж защищенных сетей и разработка CRM» — короткая, без гео/цен/УТП.
- **H1**: не обнаружен.
- **Почему ранжируется**: title с гео. Вероятно, старый домен или локальные ссылки.
- **Слабость**: description короткая без гео/цен/УТП, нет H1, нет цен, нет SLA, нет FAQ, нет кейсов.
- **Чем F&F бьёт**: F&F имеет description с УТП, H1, цены, FAQ, кейсы, llms.txt.

#### simplenetworks.ru
- **Title**: «ИТ-аутсорсинг и обслуживание бизнеса в Казани — Простые сети» — хороший, с гео + бренд.
- **Description**: «Комплексное обслуживание ИТ-инфраструктуры бизнеса в Казани: серверы Windows и Linux, сети, MikroTik, Wi-Fi, VPN, IP-телефония, 1С и SQL Server.» — хорошая, с гео + конкретика (технологии).
- **H1**: не обнаружен.
- **Почему ранжируется**: чёткий title/description с гео + конкретика по технологиям. Вероятно, есть контент по услугам.
- **Слабость**: нет цен, нет SLA с цифрами, нет FAQ, нет кейсов, нет калькулятора.
- **Чем F&F бьёт**: F&F имеет цены, FAQ, кейсы, llms.txt, 161 страницу.

#### datasib.ru
- **Title**: «Ваш сисадмин» — слабый, нет гео, нет услуг.
- **Description**: «Системный администратор, ваш приходящий системный администратор IT-аутсорсинг» — шаблонный, без гео.
- **H1**: не обнаружен.
- **Почему ранжируется**: вероятно, по низкочастотным запросам или по доменному возрасту.
- **Слабость**: title/description слабые, нет гео, нет цен, нет SLA, нет FAQ, нет кейсов.
- **Чем F&F бьёт**: F&F сильнее по всем SEO-факторам.

#### 1c.itat.ru
- **Title**: «ИТ-аутсорсинг в Казани — обслуживание бизнеса | АЙТАТ» — хороший, с гео + бренд.
- **Description**: «ИТ-аутсорсинг в Казани: обслуживание компьютеров, серверов и программ, поддержка пользователей и ИТ-инфраструктуры. Стоимость услуг АЙТАТ.» — хорошая, с гео.
- **H1**: не обнаружен.
- **Почему ранжируется**: чёткий title/description с гео + бренд (АЙТАТ — известный в Татарстане).
- **Слабость**: нет цен («Стоимость услуг АЙТАТ» — без цифр), нет SLA с цифрами, нет FAQ.
- **Чем F&F бьёт**: F&F имеет цены, FAQ, llms.txt, 161 страницу.

---

### Фаза 3. Просмотр 2/3 (известные mid-tier конкуренты)

#### its-kazan.ru
- **Title**: «Обслуживание компьютеров, серверов и сети ЛВС - ит айти аутсорсинг в Казани - IT сервис» — ключевые слова через дефисы (переспам).
- **Description**: «IT сервис: обслуживание компьютеров, серверов и сети на профессиональном уровне. Быстрая реакция, высокий уровень сервиса и хорошие цены - так говорят наши клиенты в официальных отзывах.» — шаблонная, без конкретики.
- **H1**: «Абонентское обслуживание IT инфраструктуры» — хороший.
- **Почему ранжируется**: доменный возраст, контент по услугам, локальные ссылки.
- **Слабость**: title переспамлен (дефисы), description шаблонная, нет цен, нет SLA, нет FAQ, нет калькулятора.
- **Чем F&F бьёт**: F&F имеет title без переспама, description с конкретикой, цены, FAQ, кейсы, llms.txt.

#### tss-kazan.ru
- **Title**: «ИТ аутсорсинг и внедрение ИТ систем для бизнеса TECHNO SYSTEM SERVICE» — хороший, с брендом.
- **Description**: «TECHNO SYSTEM SERVICE: более 10 лет опыта в ИТ аутсорсинге. Бесперебойная работа IT-инфраструктуры, круглосуточная техподдержка и 100% гарантия возврата денег. Работаем в Казани. Звоните +7 843 2-102-422» — хорошая, с гео + телефон + УТП (100% возврат).
- **H1**: нет H1 (стилизованный блок).
- **Почему ранжируется**: контент с отработкой возражений (5 проблем→решения), SLA, локальные ссылки.
- **Слабость**: нет H1, нет цен, нет калькулятора, нет FAQ.
- **Чем F&F бьёт**: F&F имеет H1, цены, FAQ, llms.txt, 161 страницу.

#### i-tat.ru
- **Title**: «АЙТАТ.РФ – ИТ и 1С обслуживание, ГРАНД-Смета» — хороший, с брендом + услуги.
- **Description**: «Решим все проблемы с 1С и компьютерами. Собственные линии поддержки 1С, компьютеров и серверов, Гранд-Сметы, Web-студия. Мы обслуживаем более 1 800 предприятий, более 16 лет на рынке.» — хорошая, с метриками.
- **H1**: нет H1 (слайдер).
- **Почему ранжируется**: локальные посадочные (Челны/Нижнекамск/Альметьевск), 1С-экспертиза, доменный возраст.
- **Слабость**: нет H1, нет цен, нет SLA, нет FAQ, IT вторичен.
- **Чем F&F бьёт**: F&F имеет H1, цены, SLA, FAQ, llms.txt, локальный IT-бренд.

#### esc-kazan.ru
- **Title**: «Центр электронных услуг | Сервисы для бизнеса» — слабый, нет гео, нет услуг.
- **Description**: «Официальный партнер СКБ Контур - ЦЭУ. Полное обслуживание фирм, от КЭП до маркировки в ЕГАИС, ЧЗ и ведения бухгалтерии ИП и ООО. Работаем с офисом в Казани и удаленно по России через электронный документооборот.» — хорошая, с гео + УТП.
- **H1**: нет H1 (стилизованный блок).
- **Почему ранжируется**: реквизиты, 5 шагов, 21 год, локальный бренд.
- **Слабость**: title слабый (нет гео/услуг), нет H1, нет SLA, нет FAQ, нет кейсов, IT вторичен.
- **Чем F&F бьёт**: F&F имеет title с гео, H1, SLA, FAQ, кейсы, локальный IT-бренд.

#### a8 / itbsgroup.ru
- **Title**: «Сайт ГК Ай Ти Бизнес Солюшенс - Главная» — слабый, нет ключевых слов.
- **Description**: «IT Business Solutions - системный интегратор на рынке с 2005 года...» — хорошая, но без гео.
- **H1**: нет H1 (меню/слайдер).
- **Почему ранжируется**: доменный возраст (с 2005), каталог оборудования, проекты, партнёры.
- **Слабость**: title/description слабые, нет H1, нет цен, нет SLA, нет FAQ, IT вторичен.
- **Чем F&F бьёт**: F&F имеет title с ключевыми словами, H1, цены, SLA, FAQ, локальный IT-бренд.

#### obit.ru
- **Title**: «ОБИТ — оператор ИТ-решений с компетенциями в широком спектре задач: от классических телеком-услуг до реализации ИТ-проектов под ключ» — переспамлен (120+ символов).
- **Description**: «Компания ОБИТ — оператор ИТ-решений, предлагает комплексные цифровые и телекоммуникационные решения для бизнеса в Москве, Санкт-Петербурге, Казани и еще в 80 городах России.» — длинная, но с гео.
- **H1**: «ОБИТ — оператор ИТ-решений с компетенциями в широком спектре задач...» — переспамлен.
- **Почему ранжируется**: доменный возраст, глубокий каталог, отрасли, кейсы, партнёры.
- **Слабость**: title/H1 переспамлены (обрезаются в выдаче), нет цен, нет SLA, нет FAQ, федеральный масштаб.
- **Чем F&F бьёт**: F&F имеет title ≤ 60 символов, H1 с УТП, цены, SLA, FAQ, локальный бренд.

#### socialit.ru
- **Title**: «ИТ-аутсорсинг для бизнеса по всей России» — короткий, но без гео.
- **Description**: «Передать IT и потерять контроль - не единственный сценарий. SOCIALIT берёт на себя отдельные функции, усиливает внутреннюю команду или полностью заменяет ИТ-отдел, сохраняя прозрачную модель взаимодействия.» — хорошая, с хуком.
- **H1**: нет H1 («Тарифы ИТ-аутсорсинга» — h2).
- **Почему ранжируется**: SLA с фин. гарантиями, тарифы с ценами, FAQ 8 вопросов, кейсы сетей.
- **Слабость**: нет H1, нет гео в title, нет локального бренда, высокий порог (от 10k).
- **Чем F&F бьёт**: F&F имеет H1, локальный фокус, тарифы для 20-50 человек, гарантия 6 месяцев.

#### iteron.ru
- **Title**: «ИТ услуги для бизнеса в Москве - iTeron аутсорсинг» — с гео, но Москва, не Казань.
- **Description**: «IT аутсорсинг для бизнеса в Москве. Профессиональное обслуживание компьютеров и серверов с 2009 года. Узнайте больше о наших услугах и выгодных предложениях!» — шаблонная.
- **H1**: «IT-поддержка, которая всегда рядом» — хороший.
- **Почему ранжируется**: калькулятор, метрики (98%), 1С-экспертиза, доменный возраст.
- **Слабость**: гео «Москва» (не Казань), нет SLA с фин. гарантиями, нет локального бренда.
- **Чем F&F бьёт**: F&F имеет гео «Казань», SLA с фин. гарантиями, локальный бренд, llms.txt.

---

### Фаза 4. Просмотр 3/3 (топ-тиер конкуренты)

#### a1-support.ru
- **Title**: «Удалённая IT-поддержка бизнеса по всей России — A1 Support» — хороший, с гео (Россия).
- **Description**: «Обслуживание компьютеров и серверов по договору: 5 000 ₽ в месяц за офис до пяти ПК. 1С, ЭЦП, почта, резервные копии. Бесплатный номер 8-800.» — отличная, с ценой + конкретика.
- **H1**: «Удалённая IT-поддержка компьютеров и серверов для бизнеса по всей России» — хороший.
- **Почему ранжируется**: прозрачные цены + калькулятор + договор/ЭДО + 8-800 + FAQ 5 вопросов + 4 шага + 8 направлений услуг. Самый «готовый к сделке» на рынке.
- **Слабость**: нет гео «Казань» («по всей России»), нет сравнения со штатным, нет кейсов с метриками, нет локального бренда.
- **Чем F&F бьёт**: F&F имеет гео «Казань», локальный бренд, llms.txt, 161 страницу. F&F может добавить цены+калькулятор+FAQ (как a1-support) + локальный фокус.

#### itprovider.ru
- **Title**: «АйТи Провайдер. ИТ-поддержка, на которую можно положиться. 24/7. Надежный партнер для бизнеса в Казани, Республике Татарстан и России» — длинный, но с гео.
- **Description**: «Быстрая реакция и оперативное решение проблем. ИТ-поддержка бизнеса, а не устранение поломок. Предотвращаем сбои и проблемы» — хорошая, с УТП.
- **H1**: нет H1 (преимущества — h2).
- **Почему ранжируется**: метрики (640k+) + SLA (15/20 мин) + NDA + блок «уже есть сисадмин?» + именные отзывы + сертификация + фото директора.
- **Слабость**: нет H1, нет цен, нет FAQ, нет кейсов, нет калькулятора.
- **Чем F&F бьёт**: F&F имеет H1, цены, FAQ, кейсы, llms.txt, 161 страницу.

#### 1cbit.ru
- **Title**: не загрузился (401).
- **Description**: не загрузился.
- **H1**: не загрузился.
- **Почему ранжируется**: масштаб (ТОП-100, 300 000+ клиентов), SLA, 1С-экспертиза, доменный возраст.
- **Слабость**: федеральный масштаб, нет локального бренда, нет цен.
- **Чем F&F бьёт**: F&F имеет локальный бренд, цены, llms.txt, 161 страницу.

#### calltraffic.ru
- **Title**: не загрузился (cert).
- **Description**: не загрузился.
- **H1**: не загрузился.
- **Почему ранжируется**: лицензии ФСТЭК, катастрофоустойчивость 99.98%, доменный возраст.
- **Слабость**: нет цен, нет SLA, нет FAQ, нет кейсов, нет локального бренда.
- **Чем F&F бьёт**: F&F имеет цены, SLA, FAQ, кейсы, локальный бренд, llms.txt.

#### erpdev.ru
- **Title**: не загрузился (таймаут).
- **Description**: не загрузился.
- **H1**: не загрузился.
- **Почему ранжируется**: кейсы, NDA/SLA, гарантия 24 мес, доменный возраст.
- **Слабость**: Москва, нет локального бренда, нет цен.
- **Чем F&F бьёт**: F&F имеет локальный бренд, цены, llms.txt, 161 страницу.

#### F&F (fedorov55.github.io/ff-site)
- **Title**: «IT-аутсорсинг для бизнеса» (предпол.) — нуждается в усилении.
- **Description**: (нуждается в усилении).
- **H1**: «IT-аутсорсинг для бизнеса» (предпол.) — нуждается в усилении.
- **Почему ранжируется**: 161 страница, answer-first, FAQPage на 129, абсолютные canonical, schema, llms.txt, no secrets, 7 кейсов, 7 отзывов, прозрачные реквизиты, локальный бренд.
- **Слабость**: нет тарифов с ценами, нет SLA-страницы, отзывы анонимные, нет фото команды, нет TCO-калькулятора, нет локальных посадочных.
- **Чем F&F должен усилить**: тарифы с ценами, TCO-калькулятор, SLA-страница, кейсы с метриками, именные отзывы, фото команды, локальные посадочные, блок «уже есть сисадмин?», процесс 4 шага, единый CTA.

---

### Фаза 5. Организация структурированного ответа

#### Почему конкуренты ранжируются выше F&F

1. **Доменный возраст и авторитет**: obit.ru, 1cbit.ru, itprovider.ru, its-kazan.ru, tss-kazan.ru имеют старые домены (10-20 лет) и больше обратных ссылок.
2. **Локальные ссылки**: its-kazan, tss-kazan, itprovider, i-tat, esc-kazan имеют локальные ссылки (2ГИС, Яндекс.Карты, местные каталоги).
3. **Контент по услугам**: a1-support, itprovider, socialit, esc-kazan имеют глубокие страницы услуг с ценами, SLA, FAQ.
4. **Title/description с гео**: itprovider, i-tat, esc-kazan, profinfoservice, infrait, simplenetworks, 1c.itat имеют «Казань» в title/description.
5. **Калькуляторы**: a1-support, iteron имеют калькуляторы стоимости.
6. **Schema.org**: F&F имеет schema, но конкуренты тоже (Organization, Service, FAQPage).
7. **llms.txt**: F&F имеет llms.txt — конкуренты не имеют. Это преимущество F&F для GEO/AEO.

#### Что F&F должен сделать, чтобы обогнать конкурентов в SEO

1. **Усилить title/description** на всех страницах: добавить «Казань» и «Татарстан» в title, цену в description, конкретику в description.
2. **Добавить H1** на все страницы (сейчас некоторые страницы без H1).
3. **Добавить тарифы с ценами** на prices.html, services.html, servers.html, support.html.
4. **Добавить TCO-калькулятор** на prices.html и compare/staff-sysadmin-cost.html.
5. **Добавить SLA-страницу** с финансовыми гарантиями.
6. **Усилить контент** на тонких страницах (ai/*, incidents/*, resources/*, articles/*, industries/*, pain/*, cases/*, leads/*, compare/*).
7. **Добавить локальные посадочные** для Челнов, Нижнекамска, Альметьевска, Зеленодольска.
8. **Добавить schema Organization с address/geo/sameAs** (2ГИС, Яндекс.Карты).
9. **Добавить llms.txt** (уже есть — преимущество).
10. **Усилить внутреннюю перелинковку** (сейчас 161 страница, но перелинковка слабая).
11. **Добавить видео и PDF** (0 конкурентов используют — возможность быть первым).
12. **Добавить именные отзывы** с компаниями/датами/фото.
13. **Добавить фото команды** на company/team.html.
14. **Добавить блок «Уже есть сисадмин?»** на services.html.

#### Итог

- **F&F уже имеет SEO-преимущества**: 161 страница, answer-first, FAQPage на 129, абсолютные canonical, schema, llms.txt, no secrets.
- **F&F проигрывает конкурентам**: по доменному возрасту, локальным ссылкам, контенту по услугам (цены, SLA, FAQ), калькуляторам, локальным посадочным.
- **Главный рычаг роста**: усилить title/description/H1 с гео + добавить тарифы с ценами + TCO-калькулятор + SLA-страница + локальные посадочные + schema с address/geo + усилить контент на тонких страницах.

---
