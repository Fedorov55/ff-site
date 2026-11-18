import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
for rel in ['blog.html', 'services.html']:
    path = os.path.join(root, rel)
    s = open(path, encoding='utf-8').read()
    s = s.replace('blog/server-1c-saturday-plan.html', 'blog/server-upal-subbotu-plan.html')
    open(path, 'w', encoding='utf-8').write(s)
    print('Updated', rel)
print('Done')
