import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/index.html',encoding='utf-8').read()
pat=re.compile(r'<div class="mobile-nav__inner" aria-label="Основная навигация">.*?</nav>', re.S)
m=pat.search(s)
print('match:', bool(m))
if m:
    print(m.group(0)[:80])
