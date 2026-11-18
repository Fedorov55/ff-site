import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

total_removed = 0
for f in files:
    s = open(f, encoding='utf-8').read()
    original = s
    parts = re.split(r'(<script[^>]*>.*?</script>)', s, flags=re.S)
    new_parts = []
    removed_count = [0]
    for part in parts:
        if part.startswith('<script'):
            new_parts.append(part)
            continue
        seen = set()
        def repl_p(m):
            tag = m.group(1)
            attrs = m.group(2)
            content = m.group(3)
            plain = re.sub(r'<[^>]+>', '', content).strip()
            plain_norm = ' '.join(plain.split())
            if plain_norm in seen and len(plain_norm) > 30:
                removed_count[0] += 1
                return ''
            seen.add(plain_norm)
            return m.group(0)
        part = re.sub(r'<(p)([^>]*)>(.*?)</\1>', repl_p, part, flags=re.S)
        new_parts.append(part)
    s = ''.join(new_parts)
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        total_removed += removed_count[0]
        if removed_count[0] > 0:
            print(f'{os.path.relpath(f, root)}: removed {removed_count[0]} duplicate paragraphs')

print(f'Total duplicate paragraphs removed: {total_removed}')
print('Done')
