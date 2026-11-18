import os, re
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files=[]
for r,ds,fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r: continue
    for f in fs:
        if f.endswith('.html'): files.append(os.path.join(r,f))
for f in files[:10]:
    s=open(f,encoding='utf-8').read()
    m=re.search(r'<meta name="description" content="(.*?)">', s)
    print(os.path.relpath(f,root), '->', m.group(1)[:120] if m else 'NONE')
print('Total:', len(files))
# check template tail
needle='Реакция от 15 минут, 99,5% по SLA'
cnt=sum(1 for f in files if needle in open(f,encoding='utf-8').read())
print('pages with template tail:', cnt)
