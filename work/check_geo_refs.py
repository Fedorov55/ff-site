import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
geo_files = [
    'geo/server-kazan.html', 'geo/support-kazan.html', 'geo/servers-nabchelny.html',
    'geo/security-nabchelny.html', 'geo/servers-almetyevsk.html', 'geo/support-almetyevsk.html',
    'geo/security-nizhnekamsk.html', 'geo/support-nizhnekamsk.html',
    'geo/support-zelendolsk.html', 'geo/servers-innopolis.html',
]
all_files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            all_files.append(os.path.join(r, f))

for geo in geo_files:
    cnt = 0
    for f in all_files:
        s = open(f, encoding='utf-8').read()
        if geo in s:
            cnt += 1
    print(f'{geo}: referenced in {cnt} files')
print('Done')
