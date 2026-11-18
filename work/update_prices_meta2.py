import re
path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html'
s = open(path, encoding='utf-8').read()
s = re.sub(r'<title>.*?</title>', '<title>Цены на IT-услуги в Казани — калькулятор, тарифы, сравнение | F&F</title>', s)
s = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Цены на IT-услуги в Казани: абонентское обслуживание, серверы, инфраструктура, безопасность. Калькулятор, тарифы, сравнение.">', s)
s = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Цены на IT-услуги в Казани | F&F">', s)
s = re.sub(r'<h1 class="page-intro__title">.*?</h1>', '<h1 class="page-intro__title">Цены на IT-услуги в Казани</h1>', s)
s = re.sub(r'<p class="page-intro__lead">.*?</p>', '<p class="page-intro__lead">Соберите IT-поддержку под свой офис: обслуживание, настройка серверов, криптография и аудит. Предварительная смета — в калькуляторах ниже.</p>', s)
s = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://fedorov55.github.io/ff-site/prices.html">', s)
s = re.sub(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="https://fedorov55.github.io/ff-site/prices.html">', s)
open(path, 'w', encoding='utf-8').write(s)
print('Updated prices.html meta')
print('Done')
