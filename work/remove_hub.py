import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
# Remove hub.html
hub_path = os.path.join(root, 'hub.html')
if os.path.exists(hub_path):
    os.remove(hub_path)
    print('Deleted hub.html')

# Update _redirects: add /hub.html -> /index.html
redirects_path = os.path.join(root, '_redirects')
s = open(redirects_path, encoding='utf-8').read()
line = '/hub.html /index.html 301\n'
if line not in s:
    s += line
open(redirects_path, 'w', encoding='utf-8').write(s)
print('Updated _redirects')

# Remove "Хаб" link from all HTML files
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

updated = 0
for f in files:
    s = open(f, encoding='utf-8').read()
    original = s
    # Remove desktop nav link
    s = s.replace('<a href="hub.html" class="nav__direct">Хаб</a>\n', '')
    s = s.replace('<a href="../hub.html" class="nav__direct">Хаб</a>\n', '')
    # Remove mobile nav link
    s = s.replace('<a href="hub.html" class="mobile-nav__link">Хаб</a>\n', '')
    s = s.replace('<a href="../hub.html" class="mobile-nav__link">Хаб</a>\n', '')
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1

print(f'Updated {updated} files')
print('Done')
