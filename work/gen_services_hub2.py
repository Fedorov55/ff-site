import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
template_path = os.path.join(root, 'cases.html')
template = open(template_path, encoding='utf-8').read()

services = [
    ('support.html', 'Абонентское обслуживание', 'Фиксированная сумма, реакция 15 минут, мониторинг 24/7.', 'от 10 000 ₽/мес'),
    ('servers.html', 'Серверы под ключ', 'Подбор, монтаж, настройка, бэкапы.', 'от 200 000 ₽'),
    ('infrastructure.html', 'Инфраструктура и сети', 'СКС, Wi-Fi, VPN, телефония.', 'от 50 000 ₽'),
    ('security.html', 'Безопасность', 'ЭЦП, КриптоПро, 152-ФЗ, шифрование.', 'от 1 200 ₽'),
    ('audit.html', 'IT-аудит', 'Экспресс-аудит за 15 минут. Полный аудит с отчётом.', 'от 4 000 ₽'),
    ('visit.html', 'Разовый выезд', 'Вызов сисадмина в Казани.', 'от 3 000 ₽'),
    ('vpn.html', 'VPN и удалённый доступ', 'WireGuard, туннели между офисами.', 'от 8 000 ₽'),
    ('pbx.html', 'Телефония', 'IP-АТС, запись звонков.', 'от 25 000 ₽'),
    ('printers.html', 'Принтеры и оргтехника', 'Настройка, заправка, ремонт.', 'от 3 000 ₽'),
    ('mail.html', 'Почта', 'Корпоративная почта на своём сервере.', 'от 12 000 ₽'),
    ('services/crypto-gos.html', 'КриптоПро и ЭЦП', 'Установка, настройка, клонирование.', 'от 1 200 ₽'),
    ('services/import.html', 'Импортозамещение ПО', 'Astra Linux, РЕД ОС, МойОфис.', 'по задаче'),
    ('services/server-1c.html', 'Сервер для 1С', 'Клиент-серверный режим, PostgreSQL/MS SQL.', 'от 4 000 ₽'),
    ('services/vipnet-veracrypt.html', 'ViPNet и VeraCrypt', 'Защищённые каналы, шифрование.', 'от 1 200 ₽'),
    ('services/it-support.html', 'IT-обслуживание офиса', 'Абонентский сисадмин, мониторинг, бэкапы.', 'от 10 000 ₽/мес'),
    ('sks.html', 'Монтаж СКС', 'Структурированная кабельная система.', 'от 50 000 ₽'),
    ('wifi-setup.html', 'Настройка Wi-Fi', 'Корпоративный Wi-Fi, бесшовный роуминг.', 'от 30 000 ₽'),
    ('cctv.html', 'Видеонаблюдение', 'IP-камеры, NVR, удалённый доступ.', 'от 25 000 ₽'),
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
s = re.sub(r'<title>.*?</title>', '<title>Услуги IT-аутсорсинга в Казани | F&F</title>', s)
# Replace h1
s = re.sub(r'<h1 class="page-intro__title">.*?</h1>', '<h1 class="page-intro__title">Услуги IT-аутсорсинга в Казани</h1>', s)
# Replace lead
s = re.sub(r'<p class="page-intro__lead">.*?</p>', '<p class="page-intro__lead">Все услуги с ценами. Выберите то, что ближе к задаче.</p>', s)
# Replace canonical
s = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://fedorov55.github.io/ff-site/services.html">', s)
# Replace og:url
s = re.sub(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="https://fedorov55.github.io/ff-site/services.html">', s)
# Replace og:title
s = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Услуги IT-аутсорсинга в Казани | F&F">', s)
# Replace breadcrumb
s = re.sub(r'<span class="u-text">.*?</span>', '<span class="u-text">Услуги</span>', s, count=1)
# Replace BreadcrumbList
s = re.sub(r'("name": ".*?", "item": "https://fedorov55.github.io/ff-site/services.html")', '"name": "Услуги", "item": "https://fedorov55.github.io/ff-site/services.html"', s)
# Replace the cases__grid section with services__grid
s = re.sub(r'<div class="cases__grid">.*?</div>\s*</div>\s*</section>', f'<div class="services__grid fade-up">\n{cards}</div>\n</div>\n</section>', s, count=1, flags=re.S)
# Replace section label/title/subtitle
s = re.sub(r'<span class="section__label reveal">[^<]*</span>', '<span class="section__label reveal">Услуги</span>', s, count=1)
s = re.sub(r'<h2 class="section__title reveal">[^<]*</h2>', '<h2 class="section__title reveal">Все услуги</h2>', s, count=1)

out_path = os.path.join(root, 'services.html')
open(out_path, 'w', encoding='utf-8').write(s)
print('Rewrote services.html as services hub')
print('Done')
