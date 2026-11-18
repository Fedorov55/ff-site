import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

replacements = {
    'status.html': 'index.html',
    'demo.html': 'blog.html',
    'course.html': 'vybor-podryadchika.html',
}

for f in files:
    s = open(f, encoding='utf-8').read()
    original = s
    for old, new in replacements.items():
        s = s.replace(old, new)
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)

# Update _redirects
redirects_path = os.path.join(root, '_redirects')
s = open(redirects_path, encoding='utf-8').read()
for old in ['status.html', 'demo.html', 'course.html']:
    new = replacements[old]
    line = f'/{old} /{new} 301\n'
    if line not in s:
        s += line
open(redirects_path, 'w', encoding='utf-8').write(s)
print('Updated _redirects')

# Delete files
for f in ['status.html', 'demo.html', 'course.html']:
    p = os.path.join(root, f)
    if os.path.exists(p):
        os.remove(p)
        print('Deleted', f)
print('Done')
