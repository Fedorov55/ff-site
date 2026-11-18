import re, os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
path = os.path.join(root, 'cases.html')
s = open(path, encoding='utf-8').read()
original = s

# Find all Organization script blocks
matches = list(re.finditer(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "Organization".*?</script>', s, re.S))
print('Organization blocks found:', len(matches))
if len(matches) > 1:
    # remove the last one
    m = matches[-1]
    s = s[:m.start()] + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s)
    print('Removed duplicate Organization block')
else:
    print('No duplicate')
print('Done')
