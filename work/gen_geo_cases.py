import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
template_path = os.path.join(root, 'cases', 'server-turnkey.html')
template = open(template_path, encoding='utf-8').read()

geo_to_case = {
    'geo/server-kazan.html': ('cases/case-server-kazan.html', 'Сервер под ключ в Казани: кейс', 'Сервер под ключ для офиса на 25 человек в Казани', 'Казань', 'Сервер для офиса на 25 человек: подбор, монтаж, настройка. От 240 000 ₽. 6 месяцев — ноль простоев.'),
    'geo/support-kazan.html': ('cases/case-support-kazan.html', 'Абонентское обслуживание в Казани: кейс', 'Абонентка для офиса на 20 ПК в Казани', 'Казань', 'Абонентское обслуживание офиса на 20 ПК: мониторинг 24/7, бэкапы, реакция от 15 минут. 0 простоев за 2 года.'),
    'geo/servers-nabchelny.html': ('cases/case-servers-nabchelny.html', 'Сервер под ключ в Набережных Челнах: кейс', 'Сервер для производства в Набережных Челнах', 'Набережные Челны', 'Сервер для производства: 1С, бэкапы, мониторинг. От 200 000 ₽. Стабильная работа без простоев.'),
    'geo/security-nabchelny.html': ('cases/case-security-nabchelny.html', 'ЭЦП и криптография в Набережных Челнах: кейс', 'Настройка ЭЦП для тендеров в Набережных Челнах', 'Набережные Челны', 'Настройка ЭЦП и КриптоПро для тендерного отдела. 5 рабочих мест за 1 день.'),
    'geo/servers-almetyevsk.html': ('cases/case-servers-almetyevsk.html', 'Сервер под ключ в Альметьевске: кейс', 'Сервер для нефтяной компании в Альметьевске', 'Альметьевск', 'Сервер под ключ для нефтяной компании: 1С, бэкапы, мониторинг. От 200 000 ₽.'),
    'geo/support-almetyevsk.html': ('cases/case-support-almetyevsk.html', 'Абонентское обслуживание в Альметьевске: кейс', 'IT-аутсорсинг для офиса в Альметьевске', 'Альметьевск', 'Абонентское обслуживание офиса: мониторинг 24/7, бэкапы, реакция от 15 минут.'),
    'geo/security-nizhnekamsk.html': ('cases/case-security-nizhnekamsk.html', 'ЭЦП и криптография в Нижнекамске: кейс', 'Защита ПДн и ЭЦП для завода в Нижнекамске', 'Нижнекамск', 'Защита персональных данных и ЭЦП для завода. Аудит ИБ, шифрование, 152-ФЗ.'),
    'geo/support-nizhnekamsk.html': ('cases/case-support-nizhnekamsk.html', 'Абонентское обслуживание в Нижнекамске: кейс', 'IT-аутсорсинг для промышленного офиса в Нижнекамске', 'Нижнекамск', 'Абонентское обслуживание промышленного офиса: мониторинг, бэкапы, реакция от 15 минут.'),
    'geo/support-zelendolsk.html': ('cases/case-support-zelendolsk.html', 'Абонентское обслуживание в Зеленодольске: кейс', 'IT-аутсорсинг для офиса в Зеленодольске', 'Зеленодольск', 'Абонентское обслуживание офиса: мониторинг 24/7, бэкапы, реакция от 15 минут.'),
    'geo/servers-innopolis.html': ('cases/case-servers-innopolis.html', 'Сервер под ключ в Иннополисе: кейс', 'Сервер для IT-компании в Иннополисе', 'Иннополис', 'Сервер под ключ для IT-компании: 1С, виртуализация, бэкапы. От 200 000 ₽.'),
}

for geo, (case_path, title, h1, city, lead) in geo_to_case.items():
    s = template
    # Replace title
    s = re.sub(r'<title>.*?</title>', f'<title>{title} | F&F</title>', s)
    # Replace description
    s = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{lead}">', s)
    # Replace og:title
    s = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title} | F&F">', s)
    # Replace h1
    s = re.sub(r'<h1 class="page-intro__title">.*?</h1>', f'<h1 class="page-intro__title">{h1}</h1>', s)
    # Replace lead
    s = re.sub(r'<p class="page-intro__lead">.*?</p>', f'<p class="page-intro__lead">{lead}</p>', s)
    # Replace canonical
    s = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://fedorov55.github.io/ff-site/{case_path}">', s)
    # Replace og:url
    s = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="https://fedorov55.github.io/ff-site/{case_path}">', s)
    # Replace breadcrumb span
    s = re.sub(r'<span class="u-text">.*?</span>', f'<span class="u-text">Кейс: {city}</span>', s, count=1)
    # Replace BreadcrumbList JSON-LD
    s = re.sub(r'("name": "Кейс .*?", "item": "https://fedorov55.github.io/ff-site/cases/server-turnkey.html")', f'"name": "Кейс: {city}", "item": "https://fedorov55.github.io/ff-site/{case_path}"', s)
    # Write file
    out_path = os.path.join(root, case_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, 'w', encoding='utf-8').write(s)
    print(f'Created {case_path}')

print('Done: 10 case pages created')
