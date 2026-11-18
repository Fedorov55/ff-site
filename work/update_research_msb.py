import re
path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/research-msb.html'
s = open(path, encoding='utf-8').read()
s = re.sub(r'<title>.*?</title>', '<title>Исследование: сколько казанский МСБ платит за IT | F&F</title>', s)
s = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://fedorov55.github.io/ff-site/research-msb.html">', s)
s = re.sub(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="https://fedorov55.github.io/ff-site/research-msb.html">', s)
s = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Исследование: сколько казанский МСБ платит за IT | F&F">', s)
open(path, 'w', encoding='utf-8').write(s)
print('Updated research-msb.html')
print('Done')
