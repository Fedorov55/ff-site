import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/index.html',encoding='utf-8').read()
for i,m in enumerate(re.finditer(r'<section[^>]*>(.*?)</section>', s, re.S)):
    text = re.sub(r'<[^>]+>', ' ', m.group(1))
    text = ' '.join(text.split())
    print(f'--- Section {i+1} ---')
    print(text[:300])
    print()
print('Total sections:', len(re.findall(r'<section', s)))
