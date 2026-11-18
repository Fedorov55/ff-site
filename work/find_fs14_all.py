import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

cnt = 0
examples = []
for f in files:
    s = open(f, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'style="[^"]*"', s):
        val = m.group(0)
        if 'font-size:14px' in val and 'color:var(--text-2)' in val:
            cnt += 1
            if len(examples) < 5:
                examples.append(val)
print('inline styles with font-size:14px + color:var(--text-2):', cnt)
for e in examples:
    print(e)
    print()
