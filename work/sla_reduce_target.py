import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
target_pages = [
    'for-it-director.html', 'for-accountant.html', 'index.html', 'services.html',
    'vybor-podryadchika.html', 'nastroyka-serverov-tatarstan.html', 'about.html',
    'methodology.html',
]
compact = 'Реакция от 15 минут, 99,5% в договоре. <a href="trust.html" class="u-gold">Доверие и SLA →</a>'

protected_re = re.compile(r'(<script[^>]*>.*?</script>|<nav[^>]*>.*?</nav>|<header[^>]*>.*?</header>|<footer[^>]*>.*?</footer>|<details[^>]*>.*?</details>)', re.S)

total = 0
for rel in target_pages:
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        print(f'MISSING: {rel}')
        continue
    s = open(path, encoding='utf-8').read()
    original = s

    parts = protected_re.split(s)
    new_parts = []
    replaced_count = [0]
    for part in parts:
        if part.startswith(('<script', '<nav', '<header', '<footer', '<details')):
            new_parts.append(part)
            continue
        def repl_p(m):
            tag = m.group(1)
            attrs = m.group(2)
            content = m.group(3)
            plain = re.sub(r'<[^>]+>', ' ', content)
            plain = ' '.join(plain.split())
            if ('SLA' in plain or '99,5' in plain or '99.5' in plain) and len(plain) > 80:
                replaced_count[0] += 1
                return f'<{tag}{attrs}>{compact}</{tag}>'
            return m.group(0)
        part = re.sub(r'<(p)([^>]*)>(.*?)</\1>', repl_p, part, flags=re.S)
        new_parts.append(part)
    s = ''.join(new_parts)

    if s != original:
        open(path, 'w', encoding='utf-8').write(s)
        print(f'Updated {rel}: {replaced_count[0]} paragraphs')
        total += replaced_count[0]
    else:
        print(f'No changes {rel}')

print(f'Total paragraphs replaced: {total}')
print('Done')
