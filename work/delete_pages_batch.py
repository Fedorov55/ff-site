import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'

deletions = {
    'ecp-lost-token.html': 'services/crypto-gos.html',
    'crypto-error.html': 'services/crypto-gos.html',
    'it-autsorsing-kazan.html': 'support.html',
    'nastroyka-serverov-tatarstan.html': 'servers.html',
    'server-move-checklist.html': 'office-move.html',
    'server-pod-klyuch-kazan.html': 'servers.html',
    'servers-cases.html': 'cases.html',
    'sla-template.html': 'trust.html',
    'support-onboarding.html': 'support.html',
    'pasahalki.html': 'index.html',
    'vcard.html': 'contacts.html',
    'backup-restore-test.html': 'backup-checklist.html',
    'lead-it-director-checklist.html': 'services.html',
    'case-studies.html': 'cases.html',
    '152fz-template.html': 'services/152fz.html',
}

# Update references in all HTML
all_files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            all_files.append(os.path.join(r, f))

for f in all_files:
    s = open(f, encoding='utf-8').read()
    original = s
    for old, new in deletions.items():
        s = s.replace(old, new)
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)

# Update _redirects
redirects_path = os.path.join(root, '_redirects')
s = open(redirects_path, encoding='utf-8').read()
for old, new in deletions.items():
    line = f'/{old} /{new} 301\n'
    if line not in s:
        s += line
open(redirects_path, 'w', encoding='utf-8').write(s)
print('Updated _redirects')

# Delete files
for old in deletions:
    p = os.path.join(root, old)
    if os.path.exists(p):
        os.remove(p)
        print('Deleted', old)
print('Done')
