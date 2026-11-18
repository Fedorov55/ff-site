import os, re
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files=[]
for r,ds,fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r: continue
    for f in fs:
        if f.endswith('.html'): files.append(os.path.join(r,f))
tail='F&F — IT-аутсорсинг для бизнеса в Казани. Звоните +7 (901) 265-52-52.'
cnt=0
for f in files:
    s=open(f,encoding='utf-8').read()
    m=re.search(r'<meta name="description" content="(.*?)">', s)
    if m and m.group(1).endswith(tail):
        cnt+=1
print('pages with generic tail:', cnt, 'of', len(files))
# Show a few descriptions that don't end with tail
print('\nSample descriptions without generic tail:')
shown=0
for f in files:
    s=open(f,encoding='utf-8').read()
    m=re.search(r'<meta name="description" content="(.*?)">', s)
    if m and not m.group(1).endswith(tail):
        print(os.path.relpath(f,root), '->', m.group(1)[:100])
        shown+=1
        if shown>=10: break
print('Done')
