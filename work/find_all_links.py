import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html',encoding='utf-8').read()
for m in re.finditer(r'<a\b([^>]*)>(.*?)</a>', s, re.S):
    attrs = m.group(1)
    content = m.group(2)
    text = re.sub(r'<[^>]+>', '', content).strip()
    has_aria = 'aria-label' in attrs
    if not text and not has_aria:
        print('NO NAME LINK:', m.group(0)[:200])
        print()
print('Done')
