import os, re, json

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

for f in files:
    s = open(f, encoding='utf-8').read()
    original = s

    # Remove duplicate FAQPage scripts (keep first)
    faq_scripts = [m for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
                   if '"FAQPage"' in m.group(1)]
    if len(faq_scripts) > 1:
        # remove from last to first (keep first)
        for m in reversed(faq_scripts[1:]):
            s = s[:m.start()] + s[m.end():]

    # Fix LocalBusiness -> Organization
    s = s.replace('"@type": "LocalBusiness"', '"@type": "Organization"')
    # Fix Product -> Service (only in schema context)
    s = s.replace('"@type": "Product"', '"@type": "Service"')

    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        print('Updated', os.path.relpath(f, root))
print('Done')
