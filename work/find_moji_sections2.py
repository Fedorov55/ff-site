import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html',encoding='utf-8').read()
moji = set('╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀■□▪▫▬▲►◄↕‼¶§▬ ')
sections = list(re.finditer(r'<section[^>]*>(.*?)</section>', s, re.S))
for i,m in enumerate(sections):
    text = m.group(1)
    if any(c in text for c in moji):
        h = re.search(r'<h[123][^>]*>(.*?)</h[123]>', text, re.S)
        title = re.sub(r'<[^>]+>','',h.group(1)).strip() if h else 'NO HEADING'
        print(f'Section {i+1}: {title[:60]} | len={len(m.group(0))} | moji={sum(1 for c in text if c in moji)}')
print('Total sections:', len(sections))
print('Done')
