import os
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files=[]
for r,ds,fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r: continue
    for f in fs:
        if f.endswith('.html'): files.append(os.path.join(r,f))
nav=0; div=0
for f in files:
    s=open(f,encoding='utf-8').read()
    if '<nav class="mobile-nav__inner"' in s: nav+=1
    if '<div class="mobile-nav__inner"' in s: div+=1
print('files with nav mobile:', nav)
print('files with div mobile:', div)
