# Чек-лист проверки Schema.org — F&F Site

## 1. Инструменты
- **Google Rich Results Test:** https://search.google.com/test/rich-results
- **Schema Markup Validator:** https://validator.schema.org/
- **Яндекс Вебмастер:** Вебмастер → Диагностика → Микроразметка
- **Google Search Console:** Enhancements → FAQ, Breadcrumb, Organization, Review

## 2. Что проверять в первую очередь
1. **Organization / ProfessionalService** — name, url, logo, telephone, email, address, taxID, description, areaServed.
2. **Service** — name, description, provider, areaServed, offers (price, currency, availability).
3. **FAQPage** — вопросы и ответы должны точно совпадать с видимым текстом.
4. **BreadcrumbList** — корректная иерархия, абсолютные URL.
5. **Review / AggregateRating** — только реальные отзывы, правильная привязка к Service/Organization.
6. **HowTo** — шаги должны соответствовать тексту на странице.

## 3. Типичные ошибки
- ❌ Дублирование schema (несколько одинаковых блоков).
- ❌ Несовпадение FAQ schema с видимым текстом.
- ❌ Отсутствие `@id` для связи сущностей.
- ❌ Неверные URL (относительные вместо абсолютных).
- ❌ Отсутствие обязательных полей (name, url, provider).
- ❌ Использование AggregateRating без реальных отзывов.
- ❌ Невалидный JSON (лишние запятые, незакрытые скобки).

## 4. Как часто перепроверять
- **После каждого изменения** структуры или контента.
- **Раз в месяц** — полный аудит всех страниц.
- **После добавления новых страниц** — проверить schema на них.
- **После обновления контента** — убедиться, что schema соответствует тексту.

## 5. Чек-лист перед публикацией
- [ ] Все schema валидны (Schema Markup Validator).
- [ ] Rich Results Test показывает без ошибок.
- [ ] Яндекс Вебмастер не выдаёт предупреждений.
- [ ] FAQPage совпадает с видимым текстом.
- [ ] BreadcrumbList соответствует навигации.
- [ ] Нет дублей schema.
- [ ] Все URL абсолютные.

---
*Чек-лист составлен: 2026-11-20*
PY