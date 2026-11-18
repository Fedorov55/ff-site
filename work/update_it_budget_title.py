import re
path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/it-budget.html'
s = open(path, encoding='utf-8').read()
s = re.sub(r'<title>.*?</title>', '<title>IT-бюджет 2026-2027: исследование и шаблон для планирования | F&F</title>', s)
s = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="IT-бюджет 2026-2027: исследование расходов на IT и шаблон для планирования. Казань, F&F.">', s)
s = re.sub(r'<h1 class="page-intro__title">.*?</h1>', '<h1 class="page-intro__title">IT-бюджет 2026-2027: исследование и шаблон</h1>', s)
open(path, 'w', encoding='utf-8').write(s)
print('Updated it-budget.html')
print('Done')
