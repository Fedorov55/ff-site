import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/index.html',encoding='utf-8').read()
for m in re.finditer(r'<section[^>]*>(.*?)</section>', s, re.S):
    h=re.search(r'<h[123][^>]*>(.*?)</h[123]>', m.group(1), re.S)
    title = re.sub(r'<[^>]+>','',h.group(1)).strip() if h else ''
    label = re.search(r'class="section__label[^>]*>(.*?)</', m.group(1), re.S)
    label = re.sub(r'<[^>]+>','',label.group(1)).strip() if label else ''
    print(f'{label:25s} | {title[:60]}')
print('Total sections:', len(re.findall(r'<section', s)))
