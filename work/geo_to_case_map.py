# Mapping geo pages to new case pages
geo_to_case = {
    'geo/server-kazan.html': ('cases/case-server-kazan.html', 'Сервер под ключ в Казани: кейс', 'Сервер под ключ для офиса на 25 человек в Казани'),
    'geo/support-kazan.html': ('cases/case-support-kazan.html', 'Абонентское обслуживание в Казани: кейс', 'Абонентка для офиса на 20 ПК в Казани'),
    'geo/servers-nabchelny.html': ('cases/case-servers-nabchelny.html', 'Сервер под ключ в Набережных Челнах: кейс', 'Сервер для производства в Набережных Челнах'),
    'geo/security-nabchelny.html': ('cases/case-security-nabchelny.html', 'ЭЦП и криптография в Набережных Челнах: кейс', 'Настройка ЭЦП для тендеров в Набережных Челнах'),
    'geo/servers-almetyevsk.html': ('cases/case-servers-almetyevsk.html', 'Сервер под ключ в Альметьевске: кейс', 'Сервер для нефтяной компании в Альметьевске'),
    'geo/support-almetyevsk.html': ('cases/case-support-almetyevsk.html', 'Абонентское обслуживание в Альметьевске: кейс', 'IT-аутсорсинг для офиса в Альметьевске'),
    'geo/security-nizhnekamsk.html': ('cases/case-security-nizhnekamsk.html', 'ЭЦП и криптография в Нижнекамске: кейс', 'Защита ПДн и ЭЦП для завода в Нижнекамске'),
    'geo/support-nizhnekamsk.html': ('cases/case-support-nizhnekamsk.html', 'Абонентское обслуживание в Нижнекамске: кейс', 'IT-аутсорсинг для промышленного офиса в Нижнекамске'),
    'geo/support-zelendolsk.html': ('cases/case-support-zelendolsk.html', 'Абонентское обслуживание в Зеленодольске: кейс', 'IT-аутсорсинг для офиса в Зеленодольске'),
    'geo/servers-innopolis.html': ('cases/case-servers-innopolis.html', 'Сервер под ключ в Иннополисе: кейс', 'Сервер для IT-компании в Иннополисе'),
}

for geo, (case, title, h1) in geo_to_case.items():
    print(f'{geo} -> {case} | {title} | {h1}')
print('Total:', len(geo_to_case))
