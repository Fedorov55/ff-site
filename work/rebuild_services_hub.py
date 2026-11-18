import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
template = open(os.path.join(root, 'backup-checklist.html'), encoding='utf-8').read()

problems = [
    ('pain-1c-slow.html', '1С тормозит', 'Отчёт 10 минут, документ 30 секунд. Перенос на сервер: ускорение в 5 раз.'),
    ('pain-server-down.html', 'Сервер упал в субботу', 'Диск вышел из строя, база не открывается. Восстановление из бэкапа за 2 часа.'),
    ('pain-admin-left.html', 'Сисадмин уволился', 'Пароли не передал, документации нет. Восстановление доступов от 1 дня.'),
    ('pain-no-backup.html', 'Бэкап не работает', 'Бэкап есть, но при восстановлении — ошибка. Проверяем целостность.'),
    ('pain-no-internet.html', 'Нет интернета', 'Нет интернета или почты в офисе — что делать прямо сейчас.'),
    ('pain-new-employee.html', 'Новый сотрудник без места', 'Новый сотрудник, а рабочего места нет.'),
    ('pain-astra.html', 'Переход на Astra Linux', 'Переход офиса на Astra Linux или РЕД ОС.'),
]

problems_cards = ''
for href, title, desc in problems:
    problems_cards += f'''<a href="{href}" class="service-card fade-up" style="text-decoration:none;">
<h3 class="service-card__title">{title}</h3>
<p class="service-card__text">{desc}</p>
</a>
'''

services = [
    ('support.html', 'Абонентское обслуживание', 'Фиксированная сумма, реакция 15 минут, мониторинг 24/7.'),
    ('servers.html', 'Серверы под ключ', 'Подбор, монтаж, настройка, бэкапы.'),
    ('infrastructure.html', 'Инфраструктура и сети', 'СКС, Wi-Fi, VPN, телефония.'),
    ('security.html', 'Безопасность', 'ЭЦП, КриптоПро, 152-ФЗ, шифрование.'),
    ('audit.html', 'IT-аудит', 'Экспресс-аудит за 15 минут. Полный аудит с отчётом.'),
    ('visit.html', 'Разовый выезд', 'Вызов сисадмина в Казани.'),
    ('vpn.html', 'VPN и удалённый доступ', 'WireGuard, туннели между офисами.'),
    ('pbx.html', 'Телефония', 'IP-АТС, запись звонков.'),
    ('printers.html', 'Принтеры и оргтехника', 'Настройка, заправка, ремонт.'),
    ('mail.html', 'Почта', 'Корпоративная почта на своём сервере.'),
    ('services/crypto-gos.html', 'КриптоПро и ЭЦП', 'Установка, настройка, клонирование.'),
    ('services/import.html', 'Импортозамещение ПО', 'Astra Linux, РЕД ОС, МойОфис.'),
    ('services/server-1c.html', 'Сервер для 1С', 'Клиент-серверный режим, PostgreSQL/MS SQL.'),
    ('services/vipnet-veracrypt.html', 'ViPNet и VeraCrypt', 'Защищённые каналы, шифрование.'),
    ('services/it-support.html', 'IT-обслуживание офиса', 'Абонентский сисадмин, мониторинг, бэкапы.'),
    ('sks.html', 'Монтаж СКС', 'Структурированная кабельная система.'),
    ('wifi-setup.html', 'Настройка Wi-Fi', 'Корпоративный Wi-Fi, бесшовный роуминг.'),
    ('cctv.html', 'Видеонаблюдение', 'IP-камеры, NVR, удалённый доступ.'),
]

services_cards = ''
for href, title, desc in services:
    services_cards += f'''<a href="{href}" class="service-card fade-up" style="text-decoration:none;">
<h3 class="service-card__title">{title}</h3>
<p class="service-card__text">{desc}</p>
</a>
'''

main_start = template.find('<main id="main"')
main_end = template.find('</main>', main_start) + len('</main>')
new_main = '''<main id="main" class="site-main">
<section class="page-intro">
<div class="container page-intro__inner">
<div class="page-intro__copy">
<span class="section__label reveal">F&F · IT для бизнеса</span>
<h1 class="page-intro__title">Услуги IT-аутсорсинга в Казани</h1>
<p class="page-intro__lead">Все услуги с описанием. Выберите то, что ближе к задаче. Цены и калькуляторы — на странице цен.</p>
<div class="page-intro__actions">
<a class="btn btn--primary" href="prices.html">Цены и калькуляторы</a>
<a class="btn btn--ghost" href="contacts.html">Получить смету</a>
</div>
</div>
</div>
</div>
</section>

<section class="section reveal">
<div class="container">
<div class="section__head fade-up reveal">
<span class="section__label reveal">Проблемы</span>
<h2 class="section__title reveal">Что ломается и как решаем</h2>
</div>
<div class="services__grid fade-up">
''' + problems_cards + '''</div>
</div>
</section>

<section class="section reveal">
<div class="container">
<div class="section__head fade-up reveal">
<span class="section__label reveal">Услуги</span>
<h2 class="section__title reveal">Все услуги</h2>
<p class="section__subtitle reveal">Каждое направление — со своим составом работ, ценами и ограничениями.</p>
</div>
<div class="services__grid fade-up">
''' + services_cards + '''</div>
</div>
</section>

<section class="section reveal u-pt-0" aria-label="Смотрите также">
<div class="container">
<div class="u-max-760">
<h3 class="u-title-16">Смотрите также</h3>
<div class="u-flex">
<a href="support.html" class="btn btn--ghost btn--sm">Абонентка</a>
<a href="servers.html" class="btn btn--ghost btn--sm">Серверы</a>
<a href="prices.html" class="btn btn--ghost btn--sm">Цены</a>
<a href="contacts.html" class="btn btn--ghost btn--sm">Контакты</a>
</div>
</div>
</div>
</section>
'''

s = template[:main_start] + new_main + template[main_end:]

# Update title
s = s.replace('<title>7 признаков, что ваши бэкапы не работают — Казань | F&F</title>', '<title>Услуги IT-аутсорсинга в Казани | F&F</title>')
# Update description
s = s.replace('<meta name="description" content="7 признаков, что ваши бэкапы не работают. F&F — IT-аутсорсинг для бизнеса в Казани. Звоните +7 (901) 265-52-52.">', '<meta name="description" content="Все услуги IT-аутсорсинга в Казани: абонентское обслуживание, серверы, инфраструктура, безопасность, аудит. F&F.">')
# Update canonical
s = s.replace('<link rel="canonical" href="https://fedorov55.github.io/ff-site/backup-checklist.html">', '<link rel="canonical" href="https://fedorov55.github.io/ff-site/services.html">')
# Update og:url
s = re.sub(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="https://fedorov55.github.io/ff-site/services.html">', s)
# Update og:title
s = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Услуги IT-аутсорсинга в Казани | F&F">', s)
# Update breadcrumb
s = re.sub(r'<span class="u-text">.*?</span>', '<span class="u-text">Услуги</span>', s, count=1)

out_path = os.path.join(root, 'services.html')
open(out_path, 'w', encoding='utf-8').write(s)
print('Rewrote services.html as services hub (problems + services, no prices)')
print('Done')
