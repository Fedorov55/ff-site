import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
geo_to_case = {
    'geo/server-kazan.html': 'cases/case-server-kazan.html',
    'geo/support-kazan.html': 'cases/case-support-kazan.html',
    'geo/servers-nabchelny.html': 'cases/case-servers-nabchelny.html',
    'geo/security-nabchelny.html': 'cases/case-security-nabchelny.html',
    'geo/servers-almetyevsk.html': 'cases/case-servers-almetyevsk.html',
    'geo/support-almetyevsk.html': 'cases/case-support-almetyevsk.html',
    'geo/security-nizhnekamsk.html': 'cases/case-security-nizhnekamsk.html',
    'geo/support-nizhnekamsk.html': 'cases/case-support-nizhnekamsk.html',
    'geo/support-zelendolsk.html': 'cases/case-support-zelendolsk.html',
    'geo/servers-innopolis.html': 'cases/case-servers-innopolis.html',
}

# Update _redirects
redirects_path = os.path.join(root, '_redirects')
s = open(redirects_path, encoding='utf-8').read()
for geo, case in geo_to_case.items():
    line = f'/{geo} /{case} 301\n'
    if line not in s:
        s += line
open(redirects_path, 'w', encoding='utf-8').write(s)
print('Updated _redirects')

# Delete geo pages
for geo in geo_to_case:
    p = os.path.join(root, geo)
    if os.path.exists(p):
        os.remove(p)
        print('Deleted', geo)
print('Done')
