import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
target_pages = [
    'for-owner.html', 'for-it-director.html', 'for-accountant.html', 'index.html',
    'services.html', 'vybor-podryadchika.html', 'nastroyka-serverov-tatarstan.html',
    'about.html', 'methodology.html',
]
# also blog/* and geo/*
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html') and (r.endswith('blog') or r.endswith('geo')):
            rel = os.path.relpath(os.path.join(r, f), root).replace('\\', '/')
            target_pages.append(rel)

target_pages = list(set(target_pages))

for rel in sorted(target_pages):
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        continue
    s = open(path, encoding='utf-8').read()
    # find paragraphs/divs containing 99,5 or SLA
    for m in re.finditer(r'<(p|div|li|span)[^>]*>([^<]*99[,.]5[^<]*|[^<]*SLA[^<]*)</\1>', s):
        text = m.group(0)
        plain = re.sub(r'<[^>]+>', ' ', text)
        plain = ' '.join(plain.split())
        if len(plain) > 40:
            print(f'{rel}: {plain[:200]}')
            print()
