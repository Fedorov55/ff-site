import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/services.html',encoding='utf-8').read()
for m in re.finditer(r'<section[^>]*>(.*?)</section>', s, re.S):
    if 'services/' in m.group(1) or 'Услуги — отдельно' in m.group(1) or 'Подстраницы' in m.group(1):
        print(m.group(0)[:800])
        print('---')
print('Total sections:', len(re.findall(r'<section', s)))
