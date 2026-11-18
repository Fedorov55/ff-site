import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

# pattern: style attr containing font-size:14px; color:var(--text-2); margin:0 0 8px (in any order, with spaces)
pat = re.compile(r'style="[^"]*font-size:\s*14px[^"]*color:\s*var\(--text-2\)[^"]*margin:\s*0 0 8px[^"]*"')
cnt = 0
examples = []
for f in files:
    s = open(f, encoding='utf-8', errors='replace').read()
    for m in pat.finditer(s):
        cnt += 1
        if len(examples) < 3:
            examples.append(m.group(0))
print('matches (strict order):', cnt)
for e in examples:
    print(e)
    print()

# broader: any style attr with all three keywords
pat2 = re.compile(r'style="[^"]*"')
cnt2 = 0
for f in files:
    s = open(f, encoding='utf-8', errors='replace').read()
    for m in pat2.finditer(s):
        val = m.group(0)
        if 'font-size:14px' in val or 'font-size: 14px' in val:
            if 'color:var(--text-2)' in val or 'color: var(--text-2)' in val:
                if 'margin:0 0 8px' in val or 'margin: 0 0 8px' in val:
                    cnt2 += 1
print('matches (broad):', cnt2)
