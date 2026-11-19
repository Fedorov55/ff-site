import re
for f in ['prices.html']:
    s=open(f,encoding='utf-8').read()
    # find <a> tags with no text content
    for m in re.finditer(r'<a\b[^>]*>(.*?)</a>', s, re.S):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        if not text:
            print('EMPTY LINK:', m.group(0)[:200])
            print()
    print('Done')
