import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/index.html',encoding='utf-8').read()
m=re.search(r'<div class="dropdown" id="menu-resources">.*?</div>', s, re.S)
print(m.group(0) if m else 'NOT FOUND')
print('---')
# search for research
for kw in ['research.html','research-msb.html']:
    print(kw, '->', s.count(kw))
