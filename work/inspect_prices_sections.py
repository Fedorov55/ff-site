import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html',encoding='utf-8').read()
secs=re.findall(r'<section[^>]*>(.*?)</section>', s, re.S)
for i,sec in enumerate(secs):
    h=re.search(r'<h[123][^>]*>(.*?)</h[123]>', sec, re.S)
    t=re.sub(r'<[^>]+>','',h.group(1)).strip() if h else 'NO HEADING'
    if t in ('Бесплатный IT-аудит', 'NO HEADING', 'Полезные статьи', 'VPN и удалённый доступ', 'Полезные статьи кластера'):
        print(f'--- Section {i+1}: {t} (len={len(sec)}) ---')
        print(sec[:300].replace('\n',' '))
        print()
print('Total sections:', len(secs))
