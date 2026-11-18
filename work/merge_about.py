import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
about_path = os.path.join(root, 'about.html')
s = open(about_path, encoding='utf-8').read()

# Extract <main> content from each page
pages_to_merge = ['team.html', 'methodology.html', 'trust.html', 'partners.html']
merged_content = ''
for pg in pages_to_merge:
    p = os.path.join(root, pg)
    if not os.path.exists(p):
        print(f'MISSING: {pg}')
        continue
    ps = open(p, encoding='utf-8').read()
    m = re.search(r'<main[^>]*>(.*?)</main>', ps, re.S)
    if m:
        content = m.group(1).strip()
        merged_content += f'\n<!-- {pg} -->\n{content}\n'
        print(f'Extracted main from {pg}')
    else:
        print(f'No <main> in {pg}')

# Insert before </main> in about.html
if '</main>' in s:
    s = s.replace('</main>', merged_content + '</main>', 1)
    open(about_path, 'w', encoding='utf-8').write(s)
    print('Merged into about.html')
else:
    print('No </main> in about.html')
print('Done')
