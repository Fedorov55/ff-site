import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/about.html',encoding='utf-8').read()
m=re.search(r'<section class="section reveal" aria-label="5 лет на рынке.*?</section>', s, re.S)
if m:
    print(m.group(0)[:500])
print('Done')
