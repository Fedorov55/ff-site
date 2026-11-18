import os, json, re
from collections import Counter

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

type_counter = Counter()
errors = []
warnings = []
pages_with_duplicate_type = []

for f in files:
    s = open(f, encoding='utf-8').read()
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    types_on_page = []
    for sch in schemas:
        try:
            data = json.loads(sch)
        except Exception as e:
            errors.append(f'{os.path.relpath(f,root)}: invalid JSON - {str(e)[:60]}')
            continue
        # handle @graph
        items = data.get('@graph', [data]) if isinstance(data, dict) else [data]
        for item in items:
            if not isinstance(item, dict):
                continue
            t = item.get('@type')
            if isinstance(t, list):
                t = t[0] if t else None
            if t:
                type_counter[t] += 1
                types_on_page.append(t)
            # validation per type
            if t == 'FAQPage':
                if not item.get('mainEntity'):
                    errors.append(f'{os.path.relpath(f,root)}: FAQPage missing mainEntity')
                else:
                    for q in item['mainEntity']:
                        if not q.get('name') or not q.get('acceptedAnswer', {}).get('text'):
                            warnings.append(f'{os.path.relpath(f,root)}: FAQPage question missing name/text')
            elif t == 'Organization':
                if not item.get('name') or not item.get('url'):
                    warnings.append(f'{os.path.relpath(f,root)}: Organization missing name/url')
            elif t == 'BreadcrumbList':
                if not item.get('itemListElement'):
                    warnings.append(f'{os.path.relpath(f,root)}: BreadcrumbList missing itemListElement')
            elif t == 'Service':
                if not item.get('name') and not item.get('serviceType'):
                    warnings.append(f'{os.path.relpath(f,root)}: Service missing name/serviceType')
            elif t == 'Article':
                if not item.get('headline'):
                    warnings.append(f'{os.path.relpath(f,root)}: Article missing headline')
    # check duplicate types on same page
    from collections import Counter as C
    tc = C(types_on_page)
    for t, c in tc.items():
        if c > 1 and t in ('FAQPage', 'Organization', 'BreadcrumbList'):
            pages_with_duplicate_type.append((os.path.relpath(f, root), t, c))

print('=== Schema type counts ===')
for t, c in type_counter.most_common():
    print(f'  {t}: {c}')

print()
print('=== Errors ===')
print(f'  Total: {len(errors)}')
for e in errors[:20]:
    print('  ', e)

print()
print('=== Warnings ===')
print(f'  Total: {len(warnings)}')
for w in warnings[:20]:
    print('  ', w)

print()
print('=== Duplicate types on same page ===')
print(f'  Total: {len(pages_with_duplicate_type)}')
for p, t, c in pages_with_duplicate_type[:10]:
    print(f'  {p}: {t} x{c}')

print()
print('Total pages:', len(files))
print('Total schema blocks:', sum(type_counter.values()))
