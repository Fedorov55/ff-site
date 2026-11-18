import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'

# Fix articles.html canonical/og:url
path = os.path.join(root, 'articles.html')
s = open(path, encoding='utf-8').read()
s = s.replace('https://fedorov55.github.io/ff-site/hub.html', 'https://fedorov55.github.io/ff-site/articles.html')
open(path, 'w', encoding='utf-8').write(s)
print('Fixed articles.html')

# Fix "Решения" block on service pages: hub.html -> services.html
service_pages = ['audit.html','infrastructure.html','security.html','servers.html','services.html','support.html','visit.html','vpn.html']
for rel in service_pages:
    path = os.path.join(root, rel)
    s = open(path, encoding='utf-8').read()
    s = s.replace('href="hub.html"', 'href="services.html"')
    s = s.replace('href="../hub.html"', 'href="../services.html"')
    open(path, 'w', encoding='utf-8').write(s)
    print('Fixed', rel)

print('Done')
