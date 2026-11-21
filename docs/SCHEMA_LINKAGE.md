# Связка Schema.org для support.html и servers.html — F&F

## Принцип
Все сущности связаны через `@id` (URL с фрагментом). ИИ и поисковики понимают, что Organization, Service, FAQPage, Review и BreadcrumbList относятся к одной странице и одному бизнесу.

---

## support.html

```json
[
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": "https://fedorov55.github.io/ff-site/#organization",
    "name": "F&F",
    "url": "https://fedorov55.github.io/ff-site/",
    "telephone": "+79012655252",
    "email": "FathFed@yandex.ru",
    "address": {"@type": "PostalAddress", "addressLocality": "Казань", "addressCountry": "RU"},
    "taxID": "165506822661"
  },
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "@id": "https://fedorov55.github.io/ff-site/support.html#service",
    "name": "Абонентское IT-обслуживание",
    "provider": {"@id": "https://fedorov55.github.io/ff-site/#organization"},
    "areaServed": "Казань, Татарстан, Россия",
    "offers": {"@type": "Offer", "price": "10000", "priceCurrency": "RUB", "availability": "https://schema.org/InStock"}
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "@id": "https://fedorov55.github.io/ff-site/support.html#faq",
    "mainEntity": [
      {"@type": "Question", "name": "Сколько стоит абонентское обслуживание?", "acceptedAnswer": {"@type": "Answer", "text": "От 10 000 ₽/мес. Штатный сисадмин — 1.6–1.9 млн ₽/год. Экономия до 80%."}}
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "Review",
    "@id": "https://fedorov55.github.io/ff-site/support.html#review",
    "itemReviewed": {"@id": "https://fedorov55.github.io/ff-site/support.html#service"},
    "author": {"@type": "Person", "name": "Директор, табачный магазин"},
    "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
    "reviewBody": "F&F настроили сервер за один день. Раньше отчёты генерировались 10 минут, теперь 30 секунд."
  },
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "@id": "https://fedorov55.github.io/ff-site/support.html#breadcrumb",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Главная", "item": "https://fedorov55.github.io/ff-site/"},
      {"@type": "ListItem", "position": 2, "name": "Поддержка", "item": "https://fedorov55.github.io/ff-site/support.html"}
    ]
  }
]
```

## servers.html

```json
[
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": "https://fedorov55.github.io/ff-site/#organization",
    "name": "F&F",
    "url": "https://fedorov55.github.io/ff-site/",
    "telephone": "+79012655252",
    "email": "FathFed@yandex.ru",
    "address": {"@type": "PostalAddress", "addressLocality": "Казань", "addressCountry": "RU"},
    "taxID": "165506822661"
  },
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "@id": "https://fedorov55.github.io/ff-site/servers.html#service",
    "name": "Сервер под ключ",
    "provider": {"@id": "https://fedorov55.github.io/ff-site/#organization"},
    "areaServed": "Казань, Татарстан, Россия",
    "offers": {"@type": "Offer", "price": "200000", "priceCurrency": "RUB", "availability": "https://schema.org/InStock"}
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "@id": "https://fedorov55.github.io/ff-site/servers.html#faq",
    "mainEntity": [
      {"@type": "Question", "name": "Сколько стоит сервер под ключ?", "acceptedAnswer": {"@type": "Answer", "text": "От 200 000 ₽. Монтаж за 1 день, гарантия 30 дней."}}
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "Review",
    "@id": "https://fedorov55.github.io/ff-site/servers.html#review",
    "itemReviewed": {"@id": "https://fedorov55.github.io/ff-site/servers.html#service"},
    "author": {"@type": "Person", "name": "Директор, табачный магазин"},
    "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
    "reviewBody": "F&F настроили сервер за один день. Раньше отчёты генерировались 10 минут, теперь 30 секунд."
  },
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "@id": "https://fedorov55.github.io/ff-site/servers.html#breadcrumb",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Главная", "item": "https://fedorov55.github.io/ff-site/"},
      {"@type": "ListItem", "position": 2, "name": "Серверы", "item": "https://fedorov55.github.io/ff-site/servers.html"}
    ]
  }
]
```

## Правила связывания
- `Organization` имеет `@id` = `https://fedorov55.github.io/ff-site/#organization`.
- `Service` ссылается на Organization через `provider: {"@id": ...}`.
- `Review` ссылается на Service через `itemReviewed: {"@id": ...}`.
- `FAQPage` и `BreadcrumbList` имеют собственные `@id` с фрагментом `#faq` и `#breadcrumb`.
- Все сущности находятся в одном массиве JSON-LD на странице.

---
*Разработано: 2026-11-20*
PY