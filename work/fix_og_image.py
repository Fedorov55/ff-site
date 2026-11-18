import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
targets = ['cases/server-turnkey.html', 'cases/tatar-septic.html', 'cases/tobacco.html']

for rel in targets:
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        print(f'MISSING: {rel}')
        continue
    s = open(path, encoding='utf-8').read()
    original = s
    # Find og:image with relative path
    s = re.sub(
        r'<meta property="og:image" content="(?!https?://)([^"]+)"',
        lambda m: f'<meta property="og:image" content="https://fedorov55.github.io/ff-site/{m.group(1)}">',
        s
    )
    # Also fix twitter:image
    s = re.sub(
        r'<meta name="twitter:image" content="(?!https?://)([^"]+)"',
        lambda m: f'<meta name="twitter:image" content="https://fedorov55.github.io/ff-site/{m.group(1)}">',
        s
    )
    if s != original:
        open(path, 'w', encoding='utf-8').write(s)
        print(f'Updated {rel}')
    else:
        print(f'No changes {rel}')
print('Done')
