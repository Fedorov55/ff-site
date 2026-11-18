import re
path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html'
s = open(path, encoding='utf-8').read()
# Find the second h1 (hero__title) and change to h2
matches = list(re.finditer(r'<h1[^>]*>(.*?)</h1>', s, re.S))
if len(matches) > 1:
    m = matches[1]
    s = s[:m.start()] + m.group(0).replace('<h1', '<h2', 1).replace('</h1>', '</h2>', 1) + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s)
    print('Fixed second H1 -> H2')
else:
    print('Only one H1 found')
print('Done')
