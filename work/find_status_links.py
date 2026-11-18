s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/index.html',encoding='utf-8').read()
import re
for m in re.finditer(r'Status|Статус', s):
    print(repr(s[max(0,m.start()-60):m.start()+40]))
print('---')
# search in all files for status link
import os
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
cnt=0
for r,ds,fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r: continue
    for f in fs:
        if f.endswith('.html'):
            ss=open(os.path.join(r,f),encoding='utf-8').read()
            if 'Статус' in ss:
                cnt+=1
print('files with Статус:', cnt)
