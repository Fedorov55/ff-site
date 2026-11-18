import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html',encoding='utf-8').read()
moji = set('╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀■□▪▫▬▲►◄↕‼¶§▬ ')
# find all sections
for i,m in enumerate(re.finditer(r'<section[^>]*>(.*?)</section>', s, re.S)):
    text = m.group(1)
    if any(c in text for c in moji):
        h = re.search(r'<h[123][^>]*>(.*?)</h[123]>', text, re.S)
        title = re.sub(r'<[^>]+>','',h.group(1)).strip() if h else 'NO HEADING'
        print(f'Section {i}: {title[:60]} | len={len(m.group(0))} | moji_count={sum(1 for c in text if c in moji)}')
print('Total sections:', len(re.findall(r'<section', s)))
