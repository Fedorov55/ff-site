import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/index.html',encoding='utf-8').read()
pat=re.compile(r'<div class="mobile-nav__inner"')
m=pat.search(s)
print('opening match:', bool(m))
pat2=re.compile(r'</nav>')
m2=pat2.search(s, pos=m.end() if m else 0)
print('closing nav after opening:', bool(m2))
if m and m2:
    print('span length:', m2.end() - m.start())
