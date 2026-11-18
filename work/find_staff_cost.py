import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
target_pages = [
    'for-owner.html', 'index.html', 'services.html', 'support.html', 'hub-support.html',
]
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.startswith('industry-') and f.endswith('.html'):
            rel = os.path.relpath(os.path.join(r, f), root).replace('\\', '/')
            target_pages.append(rel)

compact = 'Штатный сисадмин обходится в 1,4 млн ₽/год. <a href="compare.html" class="u-gold">Сравнить с штатным →</a>'

for rel in sorted(set(target_pages)):
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        continue
    s = open(path, encoding='utf-8').read()
    parts = re.split(r'(<script[^>]*>.*?</script>)', s, flags=re.S)
    for part in parts:
        if part.startswith('<script'):
            continue
        for m in re.finditer(r'<(p|div|li|span|td)[^>]*>(.*?)</\1>', part, re.S):
            tag = m.group(1)
            content = m.group(2)
            plain = re.sub(r'<[^>]+>', ' ', content)
            plain = ' '.join(plain.split())
            if ('штатный' in plain.lower() or 'сисадмин' in plain.lower()) and ('млн' in plain or 'стоит' in plain.lower() or 'стоимость' in plain.lower() or 'оклад' in plain.lower()) and len(plain) > 50:
                print(f'{rel} [{tag}]: {plain[:250]}')
                print()
