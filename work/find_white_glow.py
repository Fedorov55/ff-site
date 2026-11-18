import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/style.css',encoding='utf-8').read()
for m in re.finditer(r'box-shadow:[^;]*', s):
    v=m.group(0)
    if '255, 255, 255' in v or '255,255,255' in v or 'rgba(255' in v:
        print(v[:120])
print('---done---')
# also search for text-shadow white
for m in re.finditer(r'text-shadow:[^;]*', s):
    v=m.group(0)
    if '255' in v:
        print('text-shadow:', v[:120])
