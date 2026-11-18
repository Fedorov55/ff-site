import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/services.html',encoding='utf-8').read()
links=re.findall(r'href="(services/[^"]+)"', s)
print('services/* links on services.html:', len(links))
for l in sorted(set(links)):
    print(' ', l)
