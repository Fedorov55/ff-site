import os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
old = 'https://fedorov55.github.io/ff-site/'
new = 'https://ff-it.ru/'

files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith(('.html', '.css', '.js', '.xml', '.txt', '.json')):
            files.append(os.path.join(r, f))

count = 0
for f in files:
    s = open(f, encoding='utf-8').read()
    if old in s:
        s = s.replace(old, new)
        open(f, 'w', encoding='utf-8').write(s)
        count += 1
print(f'Updated {count} files')
print('Migration complete. Run check-site.py to verify.')
print('Done')
