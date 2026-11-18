import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/index.html',encoding='utf-8').read()
import re
m=re.search(r'<div class="nav__item"><button[^>]*>Услуги<svg.*?</div>\s*</div>', s, re.S)
if m:
    print(m.group(0)[:300])
else:
    print('NOT FOUND')
# mobile
i=s.find('mobile-nav__inner')
j=s.find('mobile-nav__footer', i)
mobile=s[i:j]
m2=re.search(r'<details class="mobile-nav__group">\s*<summary>Услуги</summary>.*?</details>', mobile, re.S)
if m2:
    print('MOBILE:', m2.group(0)[:200])
else:
    print('MOBILE NOT FOUND')
