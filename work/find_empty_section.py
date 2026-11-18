import os, re
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files=[]
for r,ds,fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r: continue
    for f in fs:
        if f.endswith('.html'): files.append(os.path.join(r,f))
for f in files:
    s=open(f,encoding='utf-8').read()
    for m in re.finditer(r'<section[^>]*>(.*?)</section>', s, re.S):
        text=re.sub(r'<[^>]+>','',m.group(1)).strip()
        text=' '.join(text.split())
        if len(text)<20:
            print('EMPTY SECTION in', os.path.relpath(f,root))
            print('  ', m.group(0)[:200])
            print()
print('Done')
