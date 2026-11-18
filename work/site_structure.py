import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r or 'work' in r or 'dist' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.relpath(os.path.join(r, f), root).replace('\\', '/'))

files.sort()

# categorize
def cat(rel):
    if rel == 'index.html': return 'Главная'
    if rel.startswith('blog/'): return 'Блог'
    if rel.startswith('articles/'): return 'Статьи'
    if rel.startswith('cases/'): return 'Кейсы'
    if rel.startswith('geo/'): return 'Гео'
    if rel.startswith('services/'): return 'Услуги (подстр.)'
    if rel in ('support.html','servers.html','infrastructure.html','security.html','audit.html','visit.html','vpn.html','services.html','contacts.html','about.html','team.html','methodology.html','trust.html','partners.html','cases.html','blog.html','services.html','industries.html','map.html','faq.html','comparison-matrix.html','case-studies.html','testimonials.html','glossary.html','status.html','quiz.html','demo.html','course.html','research.html','it-budget.html','it-autsorsing-kazan.html','nastroyka-serverov-tatarstan.html','office-move.html','pbx.html','printers.html','mail.html','mail-server.html','print-management.html','vpn.html','wifi-setup.html','sks.html','cctv.html','crypto.html','security-audit.html','servers-tco.html','support-prices.html','support-onboarding.html','audit-free.html','backup-restore-test.html','ecp-lost-token.html','backup-checklist.html','lead-audit.html','lead-ecp.html','lead-network-move.html','lead-server-1c.html','lead-it-director-checklist.html','152fz-template.html','sla-template.html','server-move-checklist.html','for-owner.html','for-it-director.html','for-accountant.html','hub-office.html','hub-servers.html','hub-security.html','hub-support.html','industry-accounting.html'): 
        return 'Коммерческая'
    if rel.startswith('lead-') or rel in ('lead-audit.html','lead-ecp.html','lead-network-move.html','lead-server-1c.html'): return 'Лид-магнит'
    if rel in ('privacy.html','terms.html','cookie.html','consent.html','404.html','spasibo.html','pasahalki.html','room.html','vcard.html'): return 'Служебная'
    return 'Прочее'

out = []
for rel in files:
    path = os.path.join(root, rel)
    s = open(path, encoding='utf-8').read()
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
    h1 = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else ''
    title = re.search(r'<title[^>]*>(.*?)</title>', s, re.S)
    title = title.group(1).strip() if title else ''
    out.append((rel, cat(rel), h1, title))

# Print summary by category
from collections import Counter
cat_counts = Counter(c for _, c, _, _ in out)
print('=== Категории ===')
for c, n in sorted(cat_counts.items(), key=lambda x: -x[1]):
    print(f'{c}: {n}')
print()
print('=== Все страницы ===')
for rel, c, h1, title in out:
    print(f'{rel:45s} | {c:20s} | {h1[:60]}')
print()
print('Total:', len(out))
# Save to file
with open(os.path.join(root, 'work', 'site_structure.txt'), 'w', encoding='utf-8') as f:
    f.write('Структура сайта F&F\n')
    f.write('='*80 + '\n')
    for rel, c, h1, title in out:
        f.write(f'{rel:45s} | {c:20s} | {h1[:60]}\n')
    f.write(f'\nTotal: {len(out)}\n')
print('Saved to work/site_structure.txt')
