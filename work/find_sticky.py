import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

pat = re.compile(r'style="[^"]*position:\s*sticky[^"]*bottom:\s*0[^"]*"')
cnt = 0
examples = []
for f in files:
    s = open(f, encoding='utf-8', errors='replace').read()
    for m in pat.finditer(s):
        cnt += 1
        if len(examples) < 10:
            examples.append(m.group(0))
print('matches:', cnt)
for e in examples:
    print(e)
    print()
