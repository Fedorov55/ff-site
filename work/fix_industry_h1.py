import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'

mapping = {
    'industry-accounting.html': 'IT-поддержка для бухгалтерии и учёта в Казани',
    'industry-bc.html': 'IT-поддержка для бизнес-центров в Казани',
    'industry-clinics.html': 'IT-поддержка для клиник и медицинских центров в Казани',
    'industry-cowork.html': 'IT-поддержка для коворкингов в Казани',
    'industry-franchise.html': 'IT-поддержка для франшиз в Казани',
    'industry-horeca-dealers.html': 'IT-поддержка для HoReCa и поставщиков в Казани',
    'industry-horeca.html': 'IT-поддержка для ресторанов и HoReCa в Казани',
    'industry-itpark.html': 'IT-поддержка для ИТ-парка в Казани',
    'industry-logistics.html': 'IT-поддержка для логистики в Казани',
    'industry-manufacturing.html': 'IT-поддержка для производства в Казани',
    'industry-realty.html': 'IT-поддержка для недвижимости в Казани',
    'industry-retail.html': 'IT-поддержка для розницы и магазинов в Казани',
    'industry-web.html': 'IT-поддержка для веб-студий в Казани',
}

for filename, h1 in mapping.items():
    path = os.path.join(root, filename)
    if not os.path.exists(path):
        print(f'MISSING: {filename}')
        continue
    s = open(path, encoding='utf-8').read()
    original = s
    # Fix H1
    s = re.sub(r'<h1[^>]*>.*?</h1>', f'<h1 class="page-intro__title">{h1}</h1>', s, count=1, flags=re.S)
    # Fix title: remove double Kazan
    s = re.sub(r'<title>.*?</title>', f'<title>{h1} | F&F</title>', s, count=1)
    # Fix og:title
    s = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{h1} | F&F">', s)
    if s != original:
        open(path, 'w', encoding='utf-8').write(s)
        print(f'Updated {filename}')
    else:
        print(f'No changes {filename}')
print('Done')
