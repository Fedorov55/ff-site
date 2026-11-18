import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'

def adjust_href(href, rel):
    if href.startswith(('http', 'mailto', 'tel', '#', '../', './')):
        return href
    d = os.path.dirname(rel)
    if d == '' or d == '.':
        return href
    if href.startswith(d + '/'):
        return href[len(d)+1:]
    return '../' + href

def links_for(rel):
    # rel: relative path with /
    base = os.path.basename(rel)
    # Commercial
    if rel == 'support.html':
        return [('services.html#calculator','Рассчитать стоимость'),('compare.html','Сравнение с штатным'),('cases.html','Все кейсы'),('security.html','ЭЦП и КриптоПро'),('servers.html','Серверы под ключ'),('visit.html','Разовый выезд')]
    if rel == 'servers.html':
        return [('services.html#estimate','Рассчитать стоимость'),('blog/pochemu-1c-tormozit.html','Почему тормозит 1С'),('blog/backup-check-15min.html','Проверка бэкапов'),('support.html','Абонентка'),('cases/server-turnkey.html','Кейс сервер'),('services.html#calculator','Конструктор услуг')]
    if rel == 'infrastructure.html':
        return [('services.html#estimate','Добавить в смету'),('vpn.html','VPN и удалённый доступ'),('office-move.html','Переезд офиса'),('visit.html','Разовый выезд'),('support.html','Абонентка'),('servers.html','Серверы под ключ')]
    if rel == 'security.html':
        return [('services.html#estimate','Проверить контур'),('152fz-prep.html','Подготовка к 152-ФЗ'),('blog/ecp-guide.html','Гайд по ЭЦП'),('audit.html','IT-аудит'),('vybor-podryadchika.html','Как выбрать подрядчика'),('backup-checklist.html','Скачать чек-лист'),('support.html','Абонентка'),('servers.html','Серверы под ключ')]
    if rel == 'audit.html':
        return [('contacts.html','Записаться на аудит'),('quiz.html','Короткая проверка'),('office-move.html','Переезд офиса'),('hub-office.html','Офис под ключ'),('blog/how-to-choose.html','Как выбрать IT-аутсорсера'),('blog/tco-calc.html','Расчёт TCO'),('lead-audit.html','Скачать чек-лист'),('support.html','Абонентка'),('servers.html','Серверы под ключ')]
    if rel == 'visit.html':
        return [('tel:+79012655252','Позвонить'),('contacts.html','Оставить заявку'),('servers.html','Серверы и 1С'),('support.html','Абонентка')]
    if rel == 'vpn.html':
        return [('services.html#estimate','Добавить в смету'),('tel:+79012655252','Позвонить'),('security.html','Безопасность'),('infrastructure.html','Инфраструктура'),('support.html','Абонентка')]
    if rel == 'services.html':
        return [('services.html#estimate','Получить смету'),('support.html','Абонентка'),('servers.html','Серверы'),('infrastructure.html','Инфраструктура'),('security.html','Безопасность'),('audit.html','IT-аудит'),('visit.html','Разовый выезд')]
    if rel == 'contacts.html':
        return [('services.html#calculator','Рассчитать стоимость'),('support.html','Абонентка'),('servers.html','Серверы')]
    # Comparative
    if rel == 'compare.html':
        return [('contacts.html','Рассчитать экономию'),('contacts.html','Получить смету'),('support.html','Абонентка'),('cases.html','Все кейсы'),('methodology.html','Как мы работаем')]
    if rel == 'vybor-podryadchika.html':
        return [('contacts.html?source=audit-access','Запросить аудит'),('compare.html','Сравнение'),('support.html','Абонентка'),('trust.html','Доверие и SLA'),('methodology.html','Как мы работаем')]
    if rel in ('compare-freelance.html','compare-integrator.html'):
        return [('contacts.html','Рассчитать стоимость'),('support.html','Абонентка'),('cases.html','Все кейсы')]
    # Audience
    if rel == 'for-owner.html':
        return [('support.html','Абонентка'),('servers.html','Серверы'),('audit.html','IT-аудит'),('compare.html','Сравнение'),('contacts.html','Рассчитать стоимость')]
    if rel == 'for-it-director.html':
        return [('infrastructure.html','Инфраструктура'),('security.html','Безопасность'),('audit.html','IT-аудит'),('support.html','Абонентка')]
    if rel == 'for-accountant.html':
        return [('security.html','ЭЦП'),('servers.html','Серверы'),('support.html','Абонентка')]
    if rel.startswith('industry-'):
        return [('support.html','Абонентка'),('servers.html','Серверы'),('audit.html','IT-аудит'),('contacts.html','Контакты')]
    if rel.startswith('hub-'):
        return [('support.html','Абонентка'),('servers.html','Серверы'),('infrastructure.html','Инфраструктура'),('security.html','Безопасность'),('audit.html','IT-аудит'),('contacts.html','Рассчитать стоимость')]
    if rel == 'office-move.html':
        return [('infrastructure.html','Инфраструктура'),('audit.html','IT-аудит'),('support.html','Абонентка'),('contacts.html','Рассчитать стоимость')]
    # Pain
    if rel == 'pain-1c-slow.html':
        return [('servers.html','Серверы и 1С'),('blog/pochemu-1c-tormozit.html','Почему тормозит 1С'),('contacts.html','Рассчитать стоимость')]
    if rel == 'pain-admin-left.html':
        return [('support.html','Абонентка'),('compare.html','Сравнение'),('contacts.html','Рассчитать стоимость')]
    if rel == 'pain-no-backup.html':
        return [('servers.html','Серверы и бэкапы'),('backup-checklist.html','Скачать чек-лист'),('support.html','Абонентка')]
    if rel == 'pain-new-employee.html':
        return [('support.html','Абонентка'),('infrastructure.html','Инфраструктура')]
    if rel == 'pain-astra.html':
        return [('security.html','Безопасность'),('audit.html','IT-аудит')]
    if rel.startswith('pain-'):
        return [('support.html','Абонентка'),('servers.html','Серверы'),('contacts.html','Контакты')]
    # Lead magnets
    if rel == 'lead-audit.html':
        return [('audit.html','IT-аудит'),('support.html','Абонентка')]
    if rel == 'lead-ecp.html':
        return [('security.html','Настройка ЭЦП'),('support.html','Абонентка')]
    if rel == 'lead-network-move.html':
        return [('infrastructure.html','Инфраструктура'),('office-move.html','Переезд офиса')]
    if rel == 'lead-server-1c.html':
        return [('servers.html','Серверы'),('support.html','Абонентка')]
    if rel == 'lead-it-director-checklist.html':
        return [('for-it-director.html','Для IT-директора'),('infrastructure.html','Инфраструктура'),('security.html','Безопасность'),('audit.html','IT-аудит')]
    if rel == '152fz-template.html':
        return [('152fz-prep.html','Подготовка к 152-ФЗ'),('security.html','Безопасность'),('security-audit.html','Аудит ИБ'),('audit.html','IT-аудит')]
    if rel == 'sla-template.html':
        return [('trust.html','Доверие и SLA'),('support.html','Абонентка'),('methodology.html','Как мы работаем'),('contacts.html','Контакты')]
    if rel == 'server-move-checklist.html':
        return [('office-move.html','Переезд офиса'),('servers.html','Серверы'),('infrastructure.html','Инфраструктура'),('audit.html','IT-аудит')]
    if rel == 'backup-checklist.html':
        return [('servers.html','Серверы и бэкапы'),('support.html','Абонентка'),('audit.html','IT-аудит')]
    # Cases
    if rel.startswith('cases/'):
        if 'office-support' in rel:
            return [('support.html','Абонентка'),('cases.html','Все кейсы'),('contacts.html','Рассчитать стоимость')]
        if 'server-turnkey' in rel:
            return [('servers.html','Серверы'),('cases.html','Все кейсы')]
        return [('security.html','Безопасность'),('support.html','Абонентка'),('cases.html','Все кейсы')]
    if rel == 'cases.html':
        return [('support.html','Абонентка'),('servers.html','Серверы'),('security.html','Безопасность'),('audit.html','IT-аудит')]
    # Geo
    if rel.startswith('geo/support-'):
        return [('support.html','Абонентка'),('contacts.html','Рассчитать стоимость')]
    if rel.startswith('geo/servers-') or rel == 'geo/server-kazan.html':
        return [('servers.html','Серверы'),('contacts.html','Рассчитать стоимость')]
    if rel.startswith('geo/security-'):
        return [('security.html','Безопасность'),('contacts.html','Рассчитать стоимость')]
    # Hubs
    if rel.startswith('hub-'):
        return [('support.html','Абонентка'),('servers.html','Серверы'),('infrastructure.html','Инфраструктура'),('security.html','Безопасность'),('audit.html','IT-аудит'),('contacts.html','Рассчитать стоимость')]
    # Blog
    if rel == 'blog/pochemu-1c-tormozit.html':
        return [('servers.html','Серверы и 1С'),('support.html','Абонентка'),('blog/backup-check-15min.html','Проверка бэкапов')]
    if rel in ('blog/backup-check-15min.html','blog/backup-strategy.html','blog/backup-3-2-1.html'):
        return [('backup-checklist.html','Скачать чек-лист'),('servers.html','Серверы и бэкапы'),('support.html','Абонентка')]
    if rel in ('blog/ecp-guide.html','blog/cryptopro-vipnet.html','blog/ecp-lost.html'):
        return [('security.html','Настройка ЭЦП'),('lead-ecp.html','Скачать чек-лист'),('support.html','Абонентка')]
    if rel in ('blog/sisadmin-cost.html','blog/sisadmin-cost-2026.html','blog/sisadmin-vs-abonent.html'):
        return [('compare.html','Сравнение'),('support.html','Абонентка'),('contacts.html','Рассчитать экономию')]
    if rel == 'blog/how-to-choose.html':
        return [('contacts.html?source=audit-access','Запросить аудит'),('compare.html','Сравнение'),('support.html','Абонентка')]
    if rel in ('blog/transition-to-abonent.html','blog/admin-quit.html','blog/sisadmin-uvolilsya.html'):
        return [('support.html','Абонентка'),('visit.html','Разовый выезд'),('compare.html','Сравнение')]
    if rel == 'blog/server-1c.html' or rel == 'blog/server-1c-saturday.html' or rel == 'blog/server-office.html':
        return [('servers.html','Серверы'),('support.html','Абонентка')]
    if rel in ('blog/wifi6-office.html','blog/sks-ports.html','blog/skud-office.html','blog/cctv-poe.html'):
        return [('infrastructure.html','Инфраструктура'),('support.html','Абонентка')]
    if rel == 'blog/office-move.html':
        return [('office-move.html','Переезд офиса'),('infrastructure.html','Инфраструктура')]
    if rel in ('blog/abonentka-chto-vhodit.html','blog/what-included.html'):
        return [('support.html','Абонентка'),('services.html#calculator','Калькулятор')]
    if rel in ('blog/it-outsourcing-cost-kazan-2026.html','blog/tco-calc.html','blog/3-year-tco-comparison.html'):
        return [('compare.html','Сравнение'),('contacts.html','Рассчитать экономию'),('support.html','Абонентка')]
    if rel.startswith('blog/'):
        return [('support.html','Абонентка'),('servers.html','Серверы'),('contacts.html','Контакты')]
    # Articles
    if rel.startswith('articles/'):
        return [('support.html','Абонентка'),('servers.html','Серверы'),('contacts.html','Контакты')]
    # Default: contextual fallback based on page path
    low = rel.lower()
    if 'security' in low or 'ecp' in low or 'crypto' in low or '152fz' in low:
        return [('security.html','Безопасность'),('support.html','Абонентка'),('lead-ecp.html','Скачать чек-лист'),('audit.html','IT-аудит')]
    if 'server' in low or '1c' in low or 'backup' in low:
        return [('servers.html','Серверы'),('support.html','Абонентка'),('backup-checklist.html','Скачать чек-лист'),('audit.html','IT-аудит')]
    if 'vpn' in low or 'network' in low or 'wifi' in low or 'sks' in low or 'cctv' in low or 'infra' in low:
        return [('infrastructure.html','Инфраструктура'),('support.html','Абонентка'),('vpn.html','VPN'),('audit.html','IT-аудит')]
    if 'office' in low or 'move' in low:
        return [('office-move.html','Переезд офиса'),('infrastructure.html','Инфраструктура'),('support.html','Абонентка'),('audit.html','IT-аудит')]
    if 'audit' in low:
        return [('audit.html','IT-аудит'),('support.html','Абонентка'),('lead-audit.html','Скачать чек-лист'),('servers.html','Серверы')]
    return [('support.html','Абонентка'),('servers.html','Серверы'),('services.html','Услуги'),('contacts.html','Контакты')]

see_also_re = re.compile(r'<section[^>]*>\s*<div class="container">\s*<div class="u-max-760">\s*<h3 class="u-title-16">Смотрите также</h3>.*?</section>', re.S)

updated = 0
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r or 'work' in r:
        continue
    for f in fs:
        if not f.endswith('.html'):
            continue
        path = os.path.join(r, f)
        rel = os.path.relpath(path, root).replace('\\', '/')
        links = links_for(rel)
        links = [(adjust_href(h, rel), a) for h, a in links]
        # build block
        link_html = '\n'.join(f'<a href="{h}" class="btn btn--ghost btn--sm">{a}</a>' for h, a in links)
        new_block = f'''<section class="section reveal u-pt-0" aria-label="Смотрите также">
<div class="container">
<div class="u-max-760">
<h3 class="u-title-16">Смотрите также</h3>
<div class="u-flex">
{link_html}
</div>
</div>
</div>
</section>'''
        s = open(path, encoding='utf-8').read()
        original = s
        if see_also_re.search(s):
            s = see_also_re.sub(new_block, s, count=1)
        else:
            # insert before </main>
            if '</main>' in s:
                s = s.replace('</main>', new_block + '\n</main>', 1)
        if s != original:
            open(path, 'w', encoding='utf-8').write(s)
            updated += 1

print(f'Updated {updated} pages')
print('Done')
