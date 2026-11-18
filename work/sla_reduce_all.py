import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
target_pages = [
    'for-owner.html', 'for-it-director.html', 'for-accountant.html', 'index.html',
    'services.html', 'vybor-podryadchika.html', 'nastroyka-serverov-tatarstan.html',
    'about.html', 'methodology.html',
]
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html') and (r.endswith('blog') or r.endswith('geo')):
            rel = os.path.relpath(os.path.join(r, f), root).replace('\\', '/')
            target_pages.append(rel)
target_pages = list(set(target_pages))

compact = 'Реакция от 15 минут, 99,5% в договоре. <a href="trust.html" class="u-gold">Доверие и SLA →</a>'

total_replaced = 0
for rel in sorted(target_pages):
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        continue
    s = open(path, encoding='utf-8').read()
    original = s

    parts = re.split(r'(<script[^>]*>.*?</script>)', s, flags=re.S)
    new_parts = []
    replaced_this = [0]
    for part in parts:
        if part.startswith('<script'):
            new_parts.append(part)
            continue
        def repl_p(m):
            tag = m.group(1)
            attrs = m.group(2)
            content = m.group(3)
            if '99,5' in content or '99.5' in content or 'SLA' in content:
                replaced_this[0] += 1
                return f'<{tag}{attrs}>{compact}</{tag}>'
            return m.group(0)
        part = re.sub(r'<(p)([^>]*)>(.*?)</\1>', repl_p, part, flags=re.S)
        new_parts.append(part)
    s = ''.join(new_parts)

    if s != original:
        open(path, 'w', encoding='utf-8').write(s)
        total_replaced += replaced_this[0]
        print(f'Updated {rel}: {replaced_this[0]} paragraphs')

print(f'Total paragraphs replaced: {total_replaced}')
print('Done')
