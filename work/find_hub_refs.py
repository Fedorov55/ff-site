import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

for f in files:
    s = open(f, encoding='utf-8').read()
    if 'hub.html' in s:
        print(os.path.relpath(f, root))
        # show context
        i = s.find('hub.html')
        print('   ', s[max(0,i-40):i+40])
print('Done')
