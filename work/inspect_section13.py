import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html',encoding='utf-8').read()
sections = list(re.finditer(r'<section[^>]*>(.*?)</section>', s, re.S))
m = sections[13]
print(m.group(0)[:500])
print('...')
print(m.group(0)[-200:])
