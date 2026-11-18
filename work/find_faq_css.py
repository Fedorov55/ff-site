s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/style.css',encoding='utf-8').read()
import re
for cls in ['.faq', '.faq__q', '.faq__a', '.faq__item', '.faq__list', '.faq__question', '.faq__answer']:
    # find rules where selector contains cls
    for m in re.finditer(r'[^{]*\{[^}]*\}', s):
        if cls in m.group(0).split('{')[0]:
            print(cls, '->', m.group(0)[:150])
            break
    else:
        print(cls, '-> NOT FOUND')
