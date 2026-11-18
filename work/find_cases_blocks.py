import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
target_pages = [
    'for-owner.html', 'compare.html', 'support.html', 'geo/server-kazan.html',
    'hub-servers.html', 'it-autsorsing-kazan.html', 'services.html',
    'blog/refurbished.html', 'blog/server-1c-saturday-plan.html',
]

for rel in target_pages:
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        print(f'MISSING: {rel}')
        continue
    s = open(path, encoding='utf-8').read()
    parts = re.split(r'(<script[^>]*>.*?</script>)', s, flags=re.S)
    for part in parts:
        if part.startswith('<script'):
            continue
        # find paragraphs/divs containing case-related keywords
        for m in re.finditer(r'<(p|div|li|span|td)[^>]*>(.*?)</\1>', part, re.S):
            tag = m.group(1)
            content = m.group(2)
            plain = re.sub(r'<[^>]+>', ' ', content)
            plain = ' '.join(plain.split())
            if ('кейс' in plain.lower() or 'Кейс' in plain or 'результат' in plain.lower() or 'Экономия' in plain or 'экономия' in plain.lower()) and len(plain) > 40:
                print(f'{rel} [{tag}]: {plain[:250]}')
                print()
