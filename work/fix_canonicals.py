import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = ['lead-audit.html', 'lead-ecp.html', 'lead-network-move.html', 'lead-server-1c.html']

for fn in files:
    path = os.path.join(root, fn)
    s = open(path, encoding='utf-8').read()
    # fix canonical
    s = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="https://fedorov55.github.io/ff-site/{fn}">', s)
    # fix og:url
    s = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="https://fedorov55.github.io/ff-site/{fn}">', s)
    open(path, 'w', encoding='utf-8').write(s)
    print('Fixed canonical/og:url for', fn)
print('Done')
