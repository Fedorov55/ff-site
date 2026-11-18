import re
for f in ['lead-it-director-checklist.html','152fz-template.html','sla-template.html','server-move-checklist.html']:
    s=open(f,encoding='utf-8').read()
    title=re.search(r'<title>(.*?)</title>',s).group(1)
    h1=re.search(r'<h1 class="page-intro__title">(.*?)</h1>',s).group(1)
    cnt=s.count('<li>')
    print(f, '|', title, '|', h1, '| li:', cnt)
