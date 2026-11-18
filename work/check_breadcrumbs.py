import re
for f in ['services.html', 'demo.html', 'quiz.html']:
    s=open(f,encoding='utf-8').read()
    # find breadcrumb section
    for m in re.finditer(r'<nav class="u-breadcrumb breadcrumbs".*?</nav>', s, re.S):
        print(f, '->', m.group(0)[:200])
        print()
    # also search for Services/Demo/Quiz in breadcrumbs
    for kw in ['Services','Demo','Quiz']:
        if kw in s:
            print(f, 'contains', kw)
print('Done')
