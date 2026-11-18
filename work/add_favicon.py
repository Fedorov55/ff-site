import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = ['cases.html', 'consent.html', 'cookie.html', 'privacy.html', 'spasibo.html', 'terms.html']

for rel in files:
    path = os.path.join(root, rel)
    s = open(path, encoding='utf-8').read()
    if 'favicon.ico' not in s:
        s = s.replace('</head>', '<link rel="icon" href="favicon.ico" sizes="any">\n</head>', 1)
        open(path, 'w', encoding='utf-8').write(s)
        print('Updated', rel)
    else:
        print('Already has', rel)
print('Done')
