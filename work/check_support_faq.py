import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/support.html',encoding='utf-8').read()
for m in re.finditer(r'<p class="faq__a">(.*?)</p>', s, re.S):
    if 'Штатный один' in m.group(1):
        print('visible FAQ found:', m.group(1)[:80])
print('done')
