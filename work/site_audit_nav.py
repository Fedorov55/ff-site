import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.relpath(os.path.join(r, f), root).replace('\\', '/'))

files.sort()

# Read header/footer/mobile nav from index.html (template)
index = open(os.path.join(root, 'index.html'), encoding='utf-8').read()
# Extract nav links from header
header_links = set(re.findall(r'href="([^"]+)"', index[index.find('<nav class="nav"'):index.find('</nav>')]))
# mobile nav
mobile_start = index.find('mobile-nav__inner')
mobile_end = index.find('mobile-nav__footer', mobile_start)
mobile_links = set(re.findall(r'href="([^"]+)"', index[mobile_start:mobile_end]))
# footer
footer_start = index.find('<footer class="footer">')
footer_end = index.find('</footer>', footer_start)
footer_links = set(re.findall(r'href="([^"]+)"', index[footer_start:footer_end]))

# Normalize links to page names (strip ../ and anchors)
def normalize(href):
    if href.startswith(('http','mailto','tel','#','javascript')): return None
    href = href.split('#')[0].split('?')[0]
    if href.startswith('../'):
        href = href[3:]
    if href == '' or href == 'index.html':
        return 'index.html'
    return href

header_pages = set(normalize(h) for h in header_links if normalize(h))
mobile_pages = set(normalize(h) for h in mobile_links if normalize(h))
footer_pages = set(normalize(h) for h in footer_links if normalize(h))
nav_pages = header_pages | mobile_pages | footer_pages

# Categorize
def cat(rel):
    if rel == 'index.html': return 'Главная'
    if rel.startswith('blog/'): return 'Блог'
    if rel.startswith('articles/'): return 'Статьи'
    if rel.startswith('cases/'): return 'Кейсы'
    if rel.startswith('geo/'): return 'Гео (удалено)'
    if rel.startswith('services/'): return 'Услуги (подстр.)'
    if rel in ('support.html','servers.html','infrastructure.html','security.html','audit.html','visit.html','vpn.html','services.html','contacts.html','about.html','team.html','methodology.html','trust.html','partners.html','cases.html','blog.html','industries.html','map.html','faq.html','comparison-matrix.html','case-studies.html','testimonials.html','glossary.html','status.html','quiz.html','demo.html','course.html','research.html','it-budget.html','it-autsorsing-kazan.html','nastroyka-serverov-tatarstan.html','office-move.html','pbx.html','printers.html','mail.html','mail-server.html','print-management.html','wifi-setup.html','sks.html','cctv.html','crypto.html','security-audit.html','servers-tco.html','support-prices.html','support-onboarding.html','audit-free.html','backup-restore-test.html','ecp-lost-token.html','backup-checklist.html','lead-audit.html','lead-ecp.html','lead-network-move.html','lead-server-1c.html','lead-it-director-checklist.html','152fz-template.html','sla-template.html','server-move-checklist.html','for-owner.html','for-it-director.html','for-accountant.html','hub.html','hub-office.html','hub-servers.html','hub-security.html','hub-support.html'): return 'Коммерческая'
    if rel.startswith('lead-') or rel in ('lead-audit.html','lead-ecp.html','lead-network-move.html','lead-server-1c.html'): return 'Лид-магнит'
    if rel in ('privacy.html','terms.html','cookie.html','consent.html','404.html','spasibo.html','pasahalki.html','room.html','vcard.html'): return 'Служебная'
    return 'Прочее'

# Print summary
from collections import Counter
cat_counts = Counter(cat(r) for r in files)
print('=== Категории ===')
for c, n in sorted(cat_counts.items(), key=lambda x: -x[1]):
    print(f'{c}: {n}')
print(f'Total: {len(files)}')
print()

# Orphan check: not in nav and not referenced by any page
referenced = set()
for f in files:
    s = open(os.path.join(root, f), encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'href="([^"]+)"', s):
        href = m.group(1).split('?')[0].split('#')[0]
        if href.startswith(('http','mailto','tel','javascript','data:','#')) or href == '': continue
        target = href.lstrip('/') if href.startswith('/') else None
        if target:
            referenced.add(target)
        else:
            d = os.path.dirname(f)
            target = os.path.normpath(os.path.join(d, href)).replace('\\','/')
            referenced.add(target)

orphans = []
for rel in files:
    if rel not in referenced and rel not in ('index.html',):
        orphans.append(rel)

print('=== Страницы, недоступные из навигации (не в хедере/футере/мобильном меню) ===')
print(f'Всего: {len(orphans)}')
for o in sorted(orphans):
    c = cat(o)
    in_see_also = 'unknown'
    print(f'  {o:45s} | {c}')
print()

# Also check which are in "Смотрите также" (at least one reference from another page)
in_see_also = set()
for f in files:
    s = open(os.path.join(root, f), encoding='utf-8', errors='replace').read()
    if 'Смотрите также' in s:
        # extract links from that block
        for m in re.finditer(r'Смотрите также.*?</section>', s, re.S):
            for link in re.findall(r'href="([^"]+)"', m.group(0)):
                href = link.split('?')[0].split('#')[0]
                if href.startswith(('http','mailto','tel','javascript','data:','#')): continue
                d = os.path.dirname(f)
                target = os.path.normpath(os.path.join(d, href)).replace('\\','/')
                in_see_also.add(target)

print('=== Страницы, доступные ТОЛЬКО через "Смотрите также" ===')
only_see_also = [o for o in orphans if o in in_see_also]
print(f'Кол-во: {len(only_see_also)}')
for o in sorted(only_see_also):
    print(f'  {o}')
print()

print('=== Страницы, НЕДОСТУПНЫЕ НИГДЕ (ни в навигации, ни в "Смотрите также") ===')
nowhere = [o for o in orphans if o not in in_see_also]
print(f'Кол-во: {len(nowhere)}')
for o in sorted(nowhere):
    print(f'  {o}')
print()

# Save to file
with open(os.path.join(root, 'work', 'site_audit_nav.txt'), 'w', encoding='utf-8') as f:
    f.write('Аудит навигации F&F\n')
    f.write('='*80 + '\n')
    f.write(f'Total pages: {len(files)}\n')
    f.write(f'Pages in nav (header/footer/mobile): {len(nav_pages)}\n')
    f.write(f'Orphan pages: {len(orphans)}\n')
    f.write(f'Only in "Смотрите также": {len(only_see_also)}\n')
    f.write(f'Nowhere: {len(nowhere)}\n\n')
    f.write('=== NOWHERE (no links at all) ===\n')
    for o in sorted(nowhere):
        f.write(f'  {o}\n')
    f.write('\n=== ONLY IN "Смотрите также" ===\n')
    for o in sorted(only_see_also):
        f.write(f'  {o}\n')
print('Saved to work/site_audit_nav.txt')
