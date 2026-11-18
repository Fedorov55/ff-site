import re
path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/it-budget.html'
s = open(path, encoding='utf-8').read()
# Update title/h1/description to be a research page
s = re.sub(r'<title>.*?</title>', '<title>Исследование IT-бюджета 2026-2027: сколько тратит бизнес на IT | F&F</title>', s)
s = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Исследование IT-бюджета 2026-2027: реальные расходы малого и среднего бизнеса на IT. Казань, F&F.">', s)
s = re.sub(r'<h1 class="page-intro__title">.*?</h1>', '<h1 class="page-intro__title">Исследование IT-бюджета 2026-2027</h1>', s)
open(path, 'w', encoding='utf-8').write(s)
print('Updated it-budget.html')
print('Done')
