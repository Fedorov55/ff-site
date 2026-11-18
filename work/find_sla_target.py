import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
target_pages = [
    'for-owner.html', 'for-it-director.html', 'for-accountant.html', 'index.html',
    'services.html', 'vybor-podryadchika.html', 'nastroyka-serverov-tatarstan.html',
    'about.html', 'methodology.html',
]

for rel in target_pages:
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        continue
    s = open(path, encoding='utf-8').read()
    # split by script
    parts = re.split(r'(<script[^>]*>.*?</script>)', s, flags=re.S)
    for part in parts:
        if part.startswith('<script'):
            continue
        for m in re.finditer(r'<(p|div|li|span|td)[^>]*>(.*?)</\1>', part, re.S):
            tag = m.group(1)
            content = m.group(2)
            plain = re.sub(r'<[^>]+>', ' ', content)
            plain = ' '.join(plain.split())
            if ('99,5' in plain or '99.5' in plain or 'SLA' in plain) and len(plain) > 30:
                print(f'{rel} [{tag}]: {plain}')
                print()
