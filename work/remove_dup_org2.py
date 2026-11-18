import re, os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
path = os.path.join(root, 'cases.html')
s = open(path, encoding='utf-8').read()
original = s

# Find all script blocks containing Organization with aggregateRating
pat = re.compile(r'<script type="application/ld\+json">\{[^}]*"@type":"Organization"[^}]*aggregateRating.*?</script>', re.S)
matches = pat.findall(s)
print('Matches:', len(matches))
if matches:
    s = pat.sub('', s, count=1)
    open(path, 'w', encoding='utf-8').write(s)
    print('Removed duplicate Organization (aggregateRating) block')
else:
    print('No match')
print('Done')
