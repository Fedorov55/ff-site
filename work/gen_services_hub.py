import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
template_path = os.path.join(root, 'hub-servers.html')
template = open(template_path, encoding='utf-8').read()

services = [
    ('support.html', 'Абонентское обслуживание', 'Фиксированная сумма, реакция 15 минут, мониторинг 24/7. От 10 000 ₽/мес.', 'от 10 000 ₽/мес'),
    ('servers.html', 'Серверы под ключ', 'Подбор, монтаж, настройка, бэкапы. От 200 000 ₽.', 'от 200 000 ₽'),
    ('infrastructure.html', 'Инфраструктура и сети', 'СКС, Wi-Fi, VPN, телефония. От 50 000 ₽.', 'от 50 000 ₽'),
    ('security.html', 'Безопасность', 'ЭЦП, КриптоПро, 152-ФЗ, шифрование. От 1 200 ₽.', 'от 1 200 ₽'),
    ('audit.html', 'IT-аудит', 'Экспресс-аудит за 15 минут. Полный аудит с отчётом. От 4 000 ₽.', 'от 4 000 ₽'),
    ('visit.html', 'Разовый выезд', 'Вызов сисадмина в Казани. От 3 000 ₽.', 'от 3 000 ₽'),
    ('vpn.html', 'VPN и удалённый доступ', 'WireGuard, туннели между офисами. От 8 000 ₽.', 'от 8 000 ₽'),
    ('pbx.html', 'Телефония', 'IP-АТС, запись звонков. От 25 000 ₽.', 'от 25 000 ₽'),
    ('printers.html', 'Принтеры и оргтехника', 'Настройка, заправка, ремонт. От 3 000 ₽.', 'от 3 000 ₽'),
    ('mail.html', 'Почта', 'Корпоративная почта на своём сервере. От 12 000 ₽.', 'от 12 000 ₽'),
    ('services/crypto-gos.html', 'КриптоПро и ЭЦП', 'Установка, настройка, клонирование. От 1 200 ₽.', 'от 1 200 ₽'),
    ('services/import.html', 'Импортозамещение ПО', 'Astra Linux, РЕД ОС, МойОфис. По задаче.', 'по задаче'),
    ('services/server-1c.html', 'Сервер для 1С', 'Клиент-серверный режим, PostgreSQL/MS SQL. От 4 000 ₽.', 'от 4 000 ₽'),
    ('services/vipnet-veracrypt.html', 'ViPNet и VeraCrypt', 'Защищённые каналы, шифрование. От 1 200 ₽.', 'от 1 200 ₽'),
    ('services/it-support.html', 'IT-обслуживание офиса', 'Абонентский сисадмин, мониторинг, бэкапы. От 10 000 ₽/мес.', 'от 10 000 ₽/мес'),
    ('sks.html', 'Монтаж СКС', 'Структурированная кабельная система. От 50 000 ₽.', 'от 50 000 ₽'),
    ('wifi-setup.html', 'Настройка Wi-Fi', 'Корпоративный Wi-Fi, бесшовный роуминг. От 30 000 ₽.', 'от 30 000 ₽'),
    ('cctv.html', 'Видеонаблюдение', 'IP-камеры, NVR, удалённый доступ. От 25 000 ₽.', 'от 25 000 ₽'),
]

cards = ''
for href, title, desc, price in services:
    cards += f'''<a href="{href}" class="service-card fade-up" style="text-decoration:none;">
<h3 class="service-card__title">{title}</h3>
<p class="service-card__text">{desc}</p>
<div class="service-card__price">{price}</div>
</a>
'''

s = template
# Replace title
s = re.sub(r'<title>.*?</title>', '<title>Услуги и цены IT-аутсорсинга в Казани | F&F</title>', s)
# Replace h1
s = re.sub(r'<h1 class="page-intro__title">.*?</h1>', '<h1 class="page-intro__title">Услуги IT-аутсорсинга в Казани</h1>', s)
# Replace lead
s = re.sub(r'<p class="page-intro__lead">.*?</p>', '<p class="page-intro__lead">Соберите IT-поддержку под свой офис: обслуживание, настройка серверов, криптография и аудит. Предварительная смета — в калькуляторах ниже.</p>', s)
# Replace canonical
s = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://fedorov55.github.io/ff-site/services.html">', s)
# Replace og:url
s = re.sub(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="https://fedorov55.github.io/ff-site/services.html">', s)
# Replace og:title
s = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Услуги IT-аутсорсинга в Казани | F&F">', s)
# Replace section label
s = re.sub(r'<span class="section__label reveal">[^<]*</span>', '<span class="section__label reveal">Услуги</span>', s, count=1)
# Replace section title
s = re.sub(r'<h2 class="section__title reveal">[^<]*</h2>', '<h2 class="section__title reveal">Все услуги</h2>', s, count=1)
# Replace subtitle
s = re.sub(r'<p class="section__subtitle reveal">[^<]*</p>', '<p class="section__subtitle reveal">Каждое направление — со своим составом работ, ценами и ограничениями.</p>', s, count=1)
# Replace why__grid content
s = re.sub(r'<div class="why__grid">.*?</div>\s*</div>\s*</section>', f'<div class="services__grid fade-up">\n{cards}</div>\n</div>\n</section>', s, count=1, flags=re.S)

out_path = os.path.join(root, 'services.html')
open(out_path, 'w', encoding='utf-8').write(s)
print('Rewrote services.html as services hub')
print('Done')
