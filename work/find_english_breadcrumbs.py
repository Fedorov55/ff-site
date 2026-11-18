import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

english = ['Services', 'Demo', 'Quiz', 'Cases', 'Blog', 'About', 'Team', 'Contact', 'Home']
found = []
for f in files:
    s = open(f, encoding='utf-8').read()
    for m in re.finditer(r'<nav class="u-breadcrumb breadcrumbs".*?</nav>', s, re.S):
        block = m.group(0)
        for kw in english:
            if kw in block:
                found.append((os.path.relpath(f, root), kw))
                break
if found:
    for f, kw in found:
        print(f, '->', kw)
else:
    print('No English breadcrumbs found')
print('Done')
