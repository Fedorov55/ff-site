import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
template_path = os.path.join(root, 'hub-servers.html')
template = open(template_path, encoding='utf-8').read()

# Articles list
articles = [
    ('articles/ad-setup.html', 'Active Directory: зачем он нужен малому бизнесу', 'Зачем AD офису на 15 человек, что даёт, сколько стоит внедрение.'),
    ('articles/migration-2012.html', 'Переезд с Windows Server 2012: как не потерять данные', 'Пошаговый план миграции с устаревшей ОС без потери данных.'),
    ('articles/ransomware-protection.html', 'Как защитить бизнес от вирусов-шифровальщиков', 'Защита от шифровальщиков: бэкапы, права, мониторинг.'),
    ('articles/server-1c-saturday.html', 'Сервер 1С не падает в субботу: бэкапы и мониторинг', 'Как сделать 1С надёжной в выходные.'),
    ('articles/server-vs-cloud.html', 'Локальный сервер или облако: что выгоднее в 2026?', 'Сравнение TCO локального сервера и облака.'),
    ('articles/tco-calc.html', 'TCO-калькулятор IT-инфраструктуры', 'Расчёт полной стоимости владения IT-инфраструктурой.'),
    ('research.html', 'Исследование: сколько казанский МСБ платит за IT', 'Исследование 2026: расходы малого бизнеса на IT в Казани.'),
]

# Build cards
cards = ''
for href, title, desc in articles:
    cards += f'''<a href="{href}" class="why-item fade-up" style="text-decoration:none;color:inherit">
<h3 class="why-item__title">{title}</h3>
<p class="why-item__text">{desc}</p>
</a>
'''

s = template
# Replace title
s = re.sub(r'<title>.*?</title>', '<title>Статьи и исследования F&F — гайды по IT для бизнеса | F&F</title>', s)
# Replace h1
s = re.sub(r'<h1 class="page-intro__title">.*?</h1>', '<h1 class="page-intro__title">Статьи и исследования</h1>', s)
# Replace lead
s = re.sub(r'<p class="page-intro__lead">.*?</p>', '<p class="page-intro__lead">Гайды, исследования и калькуляторы по IT для бизнеса в Казани.</p>', s)
# Replace canonical
s = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://fedorov55.github.io/ff-site/articles.html">', s)
# Replace og:url
s = re.sub(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="https://fedorov55.github.io/ff-site/articles.html">', s)
# Replace og:title
s = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Статьи и исследования F&F | F&F">', s)
# Replace the "8 статей хаба" section content (the why__grid with articles)
# Find the why__grid block and replace its content
s = re.sub(r'<div class="why__grid">.*?</div>\s*</div>\s*</section>', f'<div class="why__grid">\n{cards}</div>\n</div>\n</section>', s, count=1, flags=re.S)
# Replace section label
s = re.sub(r'<span class="section__label reveal">Серверы — гайды</span>', '<span class="section__label reveal">Статьи — гайды</span>', s)
# Replace section title
s = re.sub(r'<h2 class="section__title reveal">Если вы первый раз выбираете сервер</h2>', '<h2 class="section__title reveal">Статьи и исследования</h2>', s)
# Replace subtitle
s = re.sub(r'<p class="section__subtitle reveal">8 статей хаба</p>', '<p class="section__subtitle reveal">Гайды, исследования и калькуляторы</p>', s)

out_path = os.path.join(root, 'articles.html')
open(out_path, 'w', encoding='utf-8').write(s)
print('Created articles.html')
print('Done')
