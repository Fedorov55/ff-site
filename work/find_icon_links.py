import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html',encoding='utf-8').read()
# find <a> tags containing only svg/img (no text)
for m in re.finditer(r'<a\b[^>]*>(.*?)</a>', s, re.S):
    content = m.group(1)
    text = re.sub(r'<[^>]+>', '', content).strip()
    if not text and ('<svg' in content or '<img' in content):
        print('ICON LINK:', m.group(0)[:200])
        print()
print('Done')
