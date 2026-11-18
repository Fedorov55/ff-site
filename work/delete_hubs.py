import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
hub_files = ['hub-office.html', 'hub-servers.html', 'hub-security.html', 'hub-support.html']

# Update references in all HTML files
all_files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            all_files.append(os.path.join(r, f))

for f in all_files:
    s = open(f, encoding='utf-8').read()
    original = s
    for hf in hub_files:
        s = s.replace(hf, 'hub.html')
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)

# Update _redirects
redirects_path = os.path.join(root, '_redirects')
s = open(redirects_path, encoding='utf-8').read()
for hf in hub_files:
    line = f'/{hf} /hub.html 301\n'
    if line not in s:
        s += line
open(redirects_path, 'w', encoding='utf-8').write(s)
print('Updated _redirects')

# Delete hub files
for hf in hub_files:
    p = os.path.join(root, hf)
    if os.path.exists(p):
        os.remove(p)
        print('Deleted', hf)
print('Done')
