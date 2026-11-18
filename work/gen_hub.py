import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
template_path = os.path.join(root, 'hub-servers.html')
template = open(template_path, encoding='utf-8').read()

s = template
# Replace title
s = re.sub(r'<title>.*?</title>', '<title>Хаб ресурсов F&F — гайды, кейсы, статьи, исследования | F&F</title>', s)
# Replace h1
s = re.sub(r'<h1 class="page-intro__title">.*?</h1>', '<h1 class="page-intro__title">Хаб ресурсов</h1>', s)
# Replace lead
s = re.sub(r'<p class="page-intro__lead">.*?</p>', '<p class="page-intro__lead">Все гайды, кейсы, статьи, исследования и инструменты в одном месте.</p>', s)
# Replace canonical
s = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://fedorov55.github.io/ff-site/hub.html">', s)
# Replace og:url
s = re.sub(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="https://fedorov55.github.io/ff-site/hub.html">', s)
# Replace og:title
s = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Хаб ресурсов F&F | F&F">', s)
# Replace section label
s = re.sub(r'<span class="section__label reveal">Серверы — гайды</span>', '<span class="section__label reveal">Ресурсы</span>', s)
# Replace section title
s = re.sub(r'<h2 class="section__title reveal">Если вы первый раз выбираете сервер</h2>', '<h2 class="section__title reveal">Все ресурсы</h2>', s)
# Replace subtitle
s = re.sub(r'<p class="section__subtitle reveal">8 статей хаба</p>', '<p class="section__subtitle reveal">Гайды, кейсы, статьи, исследования и инструменты</p>', s)

# Replace the why__grid content with resource links
resources = [
    ('blog.html', 'Блог', 'Все статьи о серверах, безопасности, поддержке'),
    ('articles.html', 'Статьи и исследования', 'Гайды, исследования, калькуляторы'),
    ('cases.html', 'Кейсы', 'Реальные результаты с метриками'),
    ('research.html', 'Исследование 2026', 'Сколько казанский МСБ платит за IT'),
    ('services.html', 'Услуги и цены', 'Все услуги с ценами и калькуляторами'),
    ('glossary.html', 'Глоссарий', 'IT-термины простым языком'),
    ('status.html', 'Статус', 'Uptime и инциденты'),
    ('demo.html', 'Интерактивное демо', 'Демо панели мониторинга'),
    ('quiz.html', 'Квиз', 'Проверка инфраструктуры за 5 вопросов'),
    ('course.html', 'Мини-курс', 'Как выбрать IT-подрядчика'),
    ('it-budget.html', 'IT-бюджет 2026', 'Шаблон для планирования'),
    ('support-prices.html', 'Тарифы', 'Тарифы IT-обслуживания'),
    ('servers-tco.html', 'TCO сервера', 'Калькулятор TCO'),
    ('audit-free.html', 'Бесплатный аудит', 'Экспресс-аудит за 15 минут'),
]
cards = ''
for href, title, desc in resources:
    cards += f'''<a href="{href}" class="why-item fade-up" style="text-decoration:none;color:inherit">
<h3 class="why-item__title">{title}</h3>
<p class="why-item__text">{desc}</p>
</a>
'''
s = re.sub(r'<div class="why__grid">.*?</div>\s*</div>\s*</section>', f'<div class="why__grid">\n{cards}</div>\n</div>\n</section>', s, count=1, flags=re.S)

out_path = os.path.join(root, 'hub.html')
open(out_path, 'w', encoding='utf-8').write(s)
print('Created hub.html')
print('Done')
