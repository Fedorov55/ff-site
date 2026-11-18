import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
target_pages = [
    'for-it-director.html', 'for-accountant.html', 'index.html',
    'nastroyka-serverov-tatarstan.html',
]

for rel in target_pages:
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        print(f'MISSING: {rel}')
        continue
    s = open(path, encoding='utf-8').read()
    parts = re.split(r'(<script[^>]*>.*?</script>|<nav[^>]*>.*?</nav>|<header[^>]*>.*?</header>|<footer[^>]*>.*?</footer>|<details[^>]*>.*?</details>)', s, flags=re.S)
    for part in parts:
        if part.startswith(('<script', '<nav', '<header', '<footer', '<details')):
            continue
        for m in re.finditer(r'<(p|div|span|li|td)[^>]*>(.*?)</\1>', part, re.S):
            tag = m.group(1)
            content = m.group(2)
            plain = re.sub(r'<[^>]+>', ' ', content)
            plain = ' '.join(plain.split())
            if ('SLA' in plain or '99,5' in plain or '99.5' in plain) and len(plain) > 20:
                print(f'{rel} [{tag}]: {plain[:200]}')
                print()
print('Done')
