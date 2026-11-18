import re
path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/articles.html'
s = open(path, encoding='utf-8').read()
original = s

# Remove research card
s = s.replace('''<a href="research-msb.html" class="why-item fade-up" style="text-decoration:none;color:inherit">
<h3 class="why-item__title">Исследование: сколько казанский МСБ платит за IT</h3>
<p class="why-item__text">Исследование 2026: расходы малого бизнеса на IT в Казани.</p>
</a>
''', '')

# Update title/h1
s = re.sub(r'<title>.*?</title>', '<title>Статьи F&F — гайды по IT для бизнеса | F&F</title>', s)
s = re.sub(r'<h1 class="page-intro__title">.*?</h1>', '<h1 class="page-intro__title">Статьи</h1>', s)
s = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Статьи F&F | F&F">', s)

open(path, 'w', encoding='utf-8').write(s)
print('Updated articles.html')
print('Done')
