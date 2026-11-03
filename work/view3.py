import json
recs=json.load(open('C:/Users/Eblan/Downloads/records_classified.json',encoding='utf-8'))
debits=[r for r in recs if r['is_debit']]
for r in debits:
    cn=r['corr_name'].lower()
    if ('баланс' in cn or 'тавиат' in cn or 'асборн' in cn or 'ростелеком' in cn or 'заслон' in cn or 'управля' in cn or 'пжкх' in cn):
        print(r['date'], '|', r['corr_name'], '|', r['content'], '|', r['amount'])
