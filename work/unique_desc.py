import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
tail = 'F&F — IT-аутсорсинг для бизнеса в Казани. Звоните +7 (901) 265-52-52.'

files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

updated = 0
for f in files:
    s = open(f, encoding='utf-8').read()
    original = s
    m = re.search(r'<meta name="description" content="(.*?)">', s)
    if not m:
        continue
    desc = m.group(1)
    if not desc.endswith(tail):
        continue
    # get H1
    h1m = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
    h1 = re.sub(r'<[^>]+>', '', h1m.group(1)).strip() if h1m else ''
    # remove tail, keep unique part
    unique_part = desc[:-len(tail)].strip()
    # new desc: unique_part + short CTA
    new_desc = f'{unique_part} F&F — IT-аутсорсинг для бизнеса в Казани.'
    if len(new_desc) > 160:
        new_desc = new_desc[:157] + '...'
    s = s.replace(f'<meta name="description" content="{desc}">', f'<meta name="description" content="{new_desc}">')
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1

print(f'Updated {updated} files')
print('Done')
