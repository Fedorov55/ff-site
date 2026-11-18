import re

TEMPLATE = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/backup-checklist.html'
ROOT = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'

pages = {
    'lead-it-director-checklist.html': {
        'title': 'Чек-лист IT-инфраструктуры для IT-директора — Казань | F&F',
        'desc': 'Чек-лист IT-инфраструктуры для IT-директора: 15 пунктов, которые мы проверяем перед обслуживанием. Скачайте бесплатно. Казань, F&F.',
        'og_title': 'Чек-лист IT-инфраструктуры для IT-директора | F&F',
        'twitter_title': 'Чек-лист IT-инфраструктуры для IT-директора | F&F',
        'h1': 'Чек-лист IT-инфраструктуры для IT-директора',
        'lead': '15 пунктов, которые мы проверяем перед тем, как взять сервер на обслуживание. Скачайте и проверьте за 30 минут.',
        'inside_title': 'Что внутри чек-листа',
        'items': [
            '<li><strong>Инвентаризация оборудования.</strong> Серверы, ПК, сетевое оборудование, оргтехника — актуальный список с серийниками.</li>',
            '<li><strong>Документация.</strong> Схема сети, пароли, доступы, договоры с провайдерами — где хранятся и кто отвечает.</li>',
            '<li><strong>Бэкапы.</strong> Правило 3-2-1, проверка восстановления, глубина хранения, отчётность.</li>',
            '<li><strong>Серверы.</strong> Версия ОС, обновления, мониторинг, RAID, UPS, температура.</li>',
            '<li><strong>1С.</strong> Версия платформы, СУБД, лицензии, производительность, регламентные задания.</li>',
            '<li><strong>Сеть.</strong> Коммутаторы, VLAN, Wi-Fi, интернет-каналы, резервирование.</li>',
            '<li><strong>Безопасность.</strong> Антивирус, обновления, права доступа, ЭЦП, 152-ФЗ.</li>',
            '<li><strong>Удалённый доступ.</strong> VPN, RDP, MFA, политика паролей, журналы.</li>',
            '<li><strong>Мониторинг.</strong> Аптайм, алерты, логи, отчёты, SLA-метрики.</li>',
            '<li><strong>SLA.</strong> Время реакции, время восстановления, доступность, ответственность.</li>',
            '<li><strong>ЭЦП.</strong> Токены, сертификаты, КриптоПро, ViPNet, сроки действия.</li>',
            '<li><strong>152-ФЗ.</strong> Реестр ПДн, согласия, политика, шифрование, аудит.</li>',
            '<li><strong>Оргтехника.</strong> Принтеры, МФУ, сканеры, расходники, очередь печати.</li>',
            '<li><strong>Пользователи.</strong> Учётные записи, права, увольнение, онбординг, MFA.</li>',
            '<li><strong>План развития.</strong> Бюджет, roadmap, риски, приоритеты на квартал.</li>',
        ],
        'service': 'Чек-лист IT-директора',
        'file_slug': 'it-director-checklist',
        'breadcrumb': 'Чек-лист IT-директора',
        'also': [('for-it-director.html','Для IT-директора'),('infrastructure.html','Инфраструктура'),('security.html','Безопасность'),('audit.html','IT-аудит')],
    },
    '152fz-template.html': {
        'title': 'Шаблон политики обработки ПДн по 152-ФЗ — Казань | F&F',
        'desc': 'Готовый шаблон политики обработки персональных данных по 152-ФЗ + чек-лист подготовки. Скачайте и адаптируйте. Казань, F&F.',
        'og_title': 'Шаблон политики обработки ПДн по 152-ФЗ | F&F',
        'twitter_title': 'Шаблон политики обработки ПДн по 152-ФЗ | F&F',
        'h1': 'Шаблон политики обработки ПДн по 152-ФЗ',
        'lead': 'Готовый шаблон политики + чек-лист подготовки к проверке. Скачайте и адаптируйте под свою компанию.',
        'inside_title': 'Что внутри шаблона',
        'items': [
            '<li><strong>Реестр информационных систем.</strong> Список систем, где хранятся и обрабатываются ПДн.</li>',
            '<li><strong>Категории ПДн.</strong> Какие данные собираете: ФИО, телефон, email, паспорт, биометрия.</li>',
            '<li><strong>Согласия субъектов.</strong> Шаблон формы согласия на обработку ПДн.</li>',
            '<li><strong>Политика обработки ПДн.</strong> Готовый текст политики для сайта и внутреннего использования.</li>',
            '<li><strong>Защита ПДн.</strong> Шифрование, доступы, бэкапы, журналы — чек-лист по требованиям.</li>',
            '<li><strong>Ответственный за ПДн.</strong> Назначение, приказ, обязанности.</li>',
            '<li><strong>Уведомление Роскомнадзора.</strong> Форма и порядок подачи.</li>',
            '<li><strong>Аудит и тестирование.</strong> Чек-лист проверки перед инспекцией.</li>',
            '<li><strong>Обучение сотрудников.</strong> Программа и журнал инструктажа.</li>',
            '<li><strong>Журнал инцидентов.</strong> Учёт утечек и нарушений, порядок реагирования.</li>',
        ],
        'service': 'Шаблон 152-ФЗ',
        'file_slug': '152fz-template',
        'breadcrumb': 'Шаблон 152-ФЗ',
        'also': [('152fz-prep.html','Подготовка к 152-ФЗ'),('security.html','Безопасность'),('security-audit.html','Аудит ИБ'),('audit.html','IT-аудит')],
    },
    'sla-template.html': {
        'title': 'Шаблон SLA для договора IT-аутсорсинга — Казань | F&F',
        'desc': 'Готовый шаблон SLA с метриками и сроками реакции для договора IT-аутсорсинга. Скачайте и вставьте. Казань, F&F.',
        'og_title': 'Шаблон SLA для договора IT-аутсорсинга | F&F',
        'twitter_title': 'Шаблон SLA для договора IT-аутсорсинга | F&F',
        'h1': 'Шаблон SLA: метрики и сроки реакции',
        'lead': 'Готовый шаблон SLA с примерами метрик. Скачайте и вставьте в договор с подрядчиком.',
        'inside_title': 'Что внутри шаблона',
        'items': [
            '<li><strong>Время реакции.</strong> Критический инцидент ≤15 мин, высокий ≤1 час, средний ≤4 часа, низкий ≤1 день.</li>',
            '<li><strong>Время восстановления.</strong> Критический ≤4 часа, высокий ≤8 часов, средний ≤1 день.</li>',
            '<li><strong>Доступность (uptime).</strong> 99,5% в месяц, методика расчёта, исключения.</li>',
            '<li><strong>Окно обслуживания.</strong> 24/7 мониторинг, выезд в рабочее время, ночные работы по согласованию.</li>',
            '<li><strong>Эскалация.</strong> Уровни L1/L2/L3, контакты, сроки эскалации.</li>',
            '<li><strong>Отчётность.</strong> Ежемесячный отчёт, метрики, формат и сроки.</li>',
            '<li><strong>Штрафы и компенсации.</strong> За нарушение SLA: скидка, продление, штраф.</li>',
            '<li><strong>Исключения.</strong> Форс-мажор, плановые работы, изменения со стороны клиента.</li>',
        ],
        'service': 'SLA-шаблон',
        'file_slug': 'sla-template',
        'breadcrumb': 'SLA-шаблон',
        'also': [('trust.html','Доверие и SLA'),('support.html','Абонентское обслуживание'),('methodology.html','Как мы работаем'),('contacts.html','Контакты')],
    },
    'server-move-checklist.html': {
        'title': 'Чек-лист перед переездом сервера и офиса — Казань | F&F',
        'desc': 'Чек-лист переезда сервера и офиса: 20 пунктов, чтобы переехать без простоя. Скачайте бесплатно. Казань, F&F.',
        'og_title': 'Чек-лист переезда сервера и офиса | F&F',
        'twitter_title': 'Чек-лист переезда сервера и офиса | F&F',
        'h1': 'Чек-лист: переезд сервера без простоя',
        'lead': '20 пунктов, которые мы проверяем перед переездом. Скачайте и используйте при планировании.',
        'inside_title': 'Что внутри чек-листа',
        'items': [
            '<li><strong>Инвентаризация.</strong> Оборудование, кабели, лицензии — полный список с фото.</li>',
            '<li><strong>Схема сети.</strong> План расстановки, розетки, патч-панели, коммутаторы.</li>',
            '<li><strong>Бэкапы перед переездом.</strong> Полная копия всех данных, проверка восстановления.</li>',
            '<li><strong>Тестирование бэкапов.</strong> Развернуть на тестовом стенде, убедиться, что всё работает.</li>',
            '<li><strong>Отключение и маркировка.</strong> Подписанные кабели, пронумерованные устройства.</li>',
            '<li><strong>Транспортировка.</strong> Антистатическая упаковка, виброизоляция, сопровождение.</li>',
            '<li><strong>Подготовка новой серверной.</strong> Электрика, охлаждение, заземление, стойка.</li>',
            '<li><strong>Монтаж и подключение.</strong> Расстановка, кабели, питание, тестирование.</li>',
            '<li><strong>Настройка сети.</strong> VLAN, Wi-Fi, интернет-каналы, VPN.</li>',
            '<li><strong>Проверка 1С.</strong> Базы, лицензии, производительность, регламентные задания.</li>',
            '<li><strong>Рабочие места.</strong> ПК, мониторы, периферия, права доступа.</li>',
            '<li><strong>Печать и сканирование.</strong> Принтеры, МФУ, драйверы, очередь.</li>',
            '<li><strong>Телефония.</strong> IP-АТС, номера, гарнитуры, запись звонков.</li>',
            '<li><strong>Камеры и СКУД.</strong> Видеонаблюдение, доступы, ключи.</li>',
            '<li><strong>Интернет-каналы.</strong> Провайдеры, резервирование, скорость.</li>',
            '<li><strong>DNS и маршрутизация.</strong> Обновление записей, проверка доступности.</li>',
            '<li><strong>Уведомление пользователей.</strong> Инструкции, контакты, план работ.</li>',
            '<li><strong>План отката.</strong> Rollback-сценарий на случай сбоя.</li>',
            '<li><strong>Пост-переездный аудит.</strong> Проверка всех систем, отчёт.</li>',
            '<li><strong>Документация.</strong> Схемы, пароли, контакты — передача клиенту.</li>',
        ],
        'service': 'Чек-лист переезда сервера',
        'file_slug': 'server-move-checklist',
        'breadcrumb': 'Чек-лист переезда сервера',
        'also': [('office-move.html','Переезд офиса'),('servers.html','Серверы под ключ'),('infrastructure.html','Инфраструктура'),('audit.html','IT-аудит')],
    },
}

template = open(TEMPLATE, encoding='utf-8').read()

for fname, cfg in pages.items():
    s = template
    s = re.sub(r'<title>.*?</title>', f"<title>{cfg['title']}</title>", s)
    s = re.sub(r'<meta name="description" content=".*?">', f"<meta name=\"description\" content=\"{cfg['desc']}\">", s)
    s = re.sub(r'<meta property="og:title" content=".*?">', f"<meta property=\"og:title\" content=\"{cfg['og_title']}\">", s)
    s = re.sub(r'<meta name="twitter:title" content=".*?">', f"<meta name=\"twitter:title\" content=\"{cfg['twitter_title']}\">", s)
    s = re.sub(r'<link rel="canonical" href=".*?">', f"<link rel=\"canonical\" href=\"https://fedorov55.github.io/ff-site/{fname}\">", s)
    s = re.sub(r'<meta property="og:url" content=".*?">', f"<meta property=\"og:url\" content=\"https://fedorov55.github.io/ff-site/{fname}\">", s)
    s = re.sub(r'<h1 class="page-intro__title">.*?</h1>', f"<h1 class=\"page-intro__title\">{cfg['h1']}</h1>", s)
    s = re.sub(r'<p class="page-intro__lead">.*?</p>', f"<p class=\"page-intro__lead\">{cfg['lead']}</p>", s)
    s = re.sub(r'<h2 class="section__title reveal">.*?</h2>', f"<h2 class=\"section__title reveal\">{cfg['inside_title']}</h2>", s)
    ol_content = '\n'.join(cfg['items'])
    s = re.sub(r'<ol style="color:var\(--text-2\);font-size:15px;line-height:1.8;margin-bottom:24px;">.*?</ol>', f"<ol style=\"color:var(--text-2);font-size:15px;line-height:1.8;margin-bottom:24px;\">\n{ol_content}\n</ol>", s, flags=re.S)
    s = re.sub(r'<input type="hidden" name="service" value=".*?">', f"<input type=\"hidden\" name=\"service\" value=\"{cfg['service']}\">", s)
    s = re.sub(r'<a href="files/.*?" class="btn btn--primary" download>.*?</a>', f"<a href=\"files/{cfg['file_slug']}.pdf\" class=\"btn btn--primary\" download>Скачать бесплатно</a>", s)
    # breadcrumb
    s = re.sub(r'<span class="u-text">.*?</span>', f"<span class=\"u-text\">{cfg['breadcrumb']}</span>", s, count=1)
    # BreadcrumbList JSON-LD name/item
    s = re.sub(r'("name": "Чек-лист бэкапов", "item": "https://fedorov55.github.io/ff-site/backup-checklist.html")', f'"name": "{cfg["breadcrumb"]}", "item": "https://fedorov55.github.io/ff-site/{fname}"', s)
    # "Смотрите также" links
    also_html = ''.join(f'<a href="{a}" class="btn btn--ghost btn--sm">{t}</a>' for a,t in cfg['also'])
    # replace the also-links block (4 links)
    s = re.sub(r'<a href="support.html" class="btn btn--ghost btn--sm">Абонентское обслуживание</a>\s*<a href="servers.html" class="btn btn--ghost btn--sm">Серверы под ключ</a>\s*<a href="audit.html" class="btn btn--ghost btn--sm">IT-аудит</a>\s*<a href="contacts.html" class="btn btn--ghost btn--sm">Контакты</a>', also_html, s)
    open(f'{ROOT}/{fname}', 'w', encoding='utf-8').write(s)
    print('Created', fname)

print('Done')
