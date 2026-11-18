import re
p='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/work/implement_linking.py'
s=open(p,encoding='utf-8').read()
s=s.replace("links = links_for(rel)\nlinks = [(adjust_href(h, rel), a) for h, a in links]",
            "links = links_for(rel)\nlinks = [(adjust_href(h, rel), a) for h, a in links]")
# ensure indentation
s=s.replace("        links = links_for(rel)\nlinks = [(adjust_href(h, rel), a) for h, a in links]",
            "        links = links_for(rel)\n        links = [(adjust_href(h, rel), a) for h, a in links]")
open(p,'w',encoding='utf-8').write(s)
print('done')
