import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

# exact pattern: style="font-size:14px;color:var(--text-2);margin:0 0 8px;"
pat = re.compile(r'style="font-size:14px;color:var\(--text-2\);margin:0 0 8px;"')
cnt = 0
for f in files:
    s = open(f, encoding='utf-8', errors='replace').read()
    cnt += len(pat.findall(s))
print('exact matches:', cnt)
