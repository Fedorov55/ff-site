import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
for f in ['cases.html', 'services.html']:
    path = os.path.join(root, f)
    s = open(path, encoding='utf-8').read()
    s = s.replace('"@type":"LocalBusiness"', '"@type":"Organization"')
    s = s.replace('"@type":"Product"', '"@type":"Service"')
    open(path, 'w', encoding='utf-8').write(s)
    print('Updated', f)
print('Done')
