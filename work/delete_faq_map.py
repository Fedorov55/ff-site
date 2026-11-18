import os
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
for f in ['faq.html','map.html']:
    p=os.path.join(root,f)
    if os.path.exists(p):
        os.remove(p)
        print('deleted', f)
print('Done')
