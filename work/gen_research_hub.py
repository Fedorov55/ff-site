import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
template_path = os.path.join(root, 'articles.html')
template = open(template_path, encoding='utf-8').read()

s = template
# Replace title
s = re.sub(r'<title>.*?</title>', '<title>Исследования F&F — IT для бизнеса в Казани | F&F</title>', s)
# Replace h1
s = re.sub(r'<h1 class="page-intro__title">.*?</h1>', '<h1 class="page-intro__title">Исследования</h1>', s)
# Replace lead
s = re.sub(r'<p class="page-intro__lead">.*?</p>', '<p class="page-intro__lead">Исследования, аналитика и шаблоны для планирования IT-бюджета.</p>', s)
# Replace canonical
s = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://fedorov55.github.io/ff-site/research.html">', s)
# Replace og:url
s = re.sub(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="https://fedorov55.github.io/ff-site/research.html">', s)
# Replace og:title
s = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Исследования F&F | F&F">', s)
# Replace section label
s = re.sub(r'<span class="section__label reveal">[^<]*</span>', '<span class="section__label reveal">Исследования</span>', s, count=1)
# Replace section title
s = re.sub(r'<h2 class="section__title reveal">[^<]*</h2>', '<h2 class="section__title reveal">Все исследования</h2>', s, count=1)
# Replace subtitle
s = re.sub(r'<p class="section__subtitle reveal">[^<]*</p>', '<p class="section__subtitle reveal">Исследования и аналитика</p>', s, count=1)

# Replace the why__grid content with research cards
research_cards = [
    ('research-msb.html', 'Сколько казанский МСБ платит за IT', 'Исследование 2026: расходы малого бизнеса на IT в Казани.'),
    ('it-budget.html', 'IT-бюджет 2026-2027: исследование и шаблон', 'Реальные расходы на IT и шаблон для планирования.'),
]
cards = ''
for href, title, desc in research_cards:
    cards += f'''<a href="{href}" class="why-item fade-up" style="text-decoration:none;color:inherit">
<h3 class="why-item__title">{title}</h3>
<p class="why-item__text">{desc}</p>
</a>
'''
s = re.sub(r'<div class="why__grid">.*?</div>\s*</div>\s*</section>', f'<div class="why__grid">\n{cards}</div>\n</div>\n</section>', s, count=1, flags=re.S)

out_path = os.path.join(root, 'research.html')
open(out_path, 'w', encoding='utf-8').write(s)
print('Rewrote research.html as hub')
print('Done')
