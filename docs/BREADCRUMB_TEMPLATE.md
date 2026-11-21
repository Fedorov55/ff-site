# Шаблон и стандартизация BreadcrumbList — F&F Site

## Шаблон BreadcrumbList
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Главная", "item": "https://fedorov55.github.io/ff-site/"},
    {"@type": "ListItem", "position": 2, "name": "[Раздел]", "item": "https://fedorov55.github.io/ff-site/[раздел].html"},
    {"@type": "ListItem", "position": 3, "name": "[Страница]", "item": "https://fedorov55.github.io/ff-site/[путь]/[страница].html"}
  ]
}
```

## Примеры для основных разделов

### Услуги (services.html)
```json
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://fedorov55.github.io/ff-site/"},{"@type":"ListItem","position":2,"name":"Услуги","item":"https://fedorov55.github.io/ff-site/services.html"}]}
```

### Серверы (servers.html)
```json
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://fedorov55.github.io/ff-site/"},{"@type":"ListItem","position":2,"name":"Серверы","item":"https://fedorov55.github.io/ff-site/servers.html"}]}
```

### Поддержка (support.html)
```json
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://fedorov55.github.io/ff-site/"},{"@type":"ListItem","position":2,"name":"Поддержка","item":"https://fedorov55.github.io/ff-site/support.html"}]}
```

### Кейсы (cases.html)
```json
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://fedorov55.github.io/ff-site/"},{"@type":"ListItem","position":2,"name":"Кейсы","item":"https://fedorov55.github.io/ff-site/cases.html"}]}
```

### Инфраструктура (infrastructure/infrastructure.html)
```json
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://fedorov55.github.io/ff-site/"},{"@type":"ListItem","position":2,"name":"Инфраструктура","item":"https://fedorov55.github.io/ff-site/infrastructure/infrastructure.html"}]}
```

### Безопасность (security/security.html)
```json
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://fedorov55.github.io/ff-site/"},{"@type":"ListItem","position":2,"name":"Безопасность","item":"https://fedorov55.github.io/ff-site/security/security.html"}]}
```

### Аудит (audits/audit.html)
```json
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://fedorov55.github.io/ff-site/"},{"@type":"ListItem","position":2,"name":"Аудит","item":"https://fedorov55.github.io/ff-site/audits/audit.html"}]}
```

## Правила
- Каждая внутренняя страница должна иметь BreadcrumbList.
- Иерархия: Главная → Раздел → Страница (максимум 3 уровня).
- Названия должны совпадать с навигацией сайта.
- URL должны быть абсолютными.

---
*Стандарт установлен: 2026-11-20*
PY