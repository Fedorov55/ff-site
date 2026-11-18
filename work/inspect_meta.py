s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/blog/it-outsourcing-cost-kazan-2026.html',encoding='utf-8').read()
i=s.find('description" content=')
print(repr(s[i-20:i+260]))
print('---')
# find the meta tag
import re
m=re.search(r'<meta name="description" content="[^"]*"', s)
print('match:', m.group(0)[:200] if m else 'NONE')
