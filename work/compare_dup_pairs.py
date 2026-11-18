import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'

pairs = [
    ('compare-freelancer.html', 'compare-freelance.html'),
    ('compare-staff.html', 'compare.html'),
    ('lead-audit.html', 'backup-checklist.html'),
    ('lead-ecp.html', 'backup-checklist.html'),
    ('lead-magnet-backup.html', 'backup-checklist.html'),
    ('lead-network-move.html', 'backup-checklist.html'),
    ('lead-server-1c.html', 'backup-checklist.html'),
    ('lead-magnet-audit.html', 'lead-audit.html'),
    ('lead-magnet-network.html', 'lead-network-move.html'),
    ('lead-magnet-server-1c.html', 'lead-server-1c.html'),
    ('lead-magnet-ecp.html', 'lead-ecp.html'),
    ('blog/sisadmin-cost-2026.html', 'blog/sisadmin-cost.html'),
    ('blog/backup-3-2-1.html', 'articles/backup-3-2-1.html'),
    ('blog/server-1c-saturday-plan.html', 'blog/server-1c-saturday.html'),
    ('blog/server-upal-subbotu-plan.html', 'blog/server-1c-saturday.html'),
    ('articles/152fz-prep.html', '152fz-prep.html'),
    ('blog/152fz-prep.html', '152fz-prep.html'),
    ('blog/vpn-udalenny-dostup.html', 'vpn.html'),
    ('services/audit-services.html', 'audit.html'),
]

for a, b in pairs:
    pa = os.path.join(root, a)
    pb = os.path.join(root, b)
    if not os.path.exists(pa) or not os.path.exists(pb):
        print(f'MISSING: {a} or {b}')
        continue
    sa = open(pa, encoding='utf-8').read()
    sb = open(pb, encoding='utf-8').read()
    wa = len(sa.split())
    wb = len(sb.split())
    # h1
    import re
    ha = re.search(r'<h1[^>]*>(.*?)</h1>', sa, re.S)
    hb = re.search(r'<h1[^>]*>(.*?)</h1>', sb, re.S)
    ha = ha.group(1).strip()[:60] if ha else ''
    hb = hb.group(1).strip()[:60] if hb else ''
    print(f'{a:40s} {wa:6d} words | H1: {ha}')
    print(f'{b:40s} {wb:6d} words | H1: {hb}')
    print(f'  -> KEEP: {a if wa > wb else b} (more words)')
    print()
