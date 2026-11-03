import json, re, pdfplumber

# Load records
recs=json.load(open('C:/Users/Eblan/Downloads/records.json',encoding='utf-8'))

# Build cls list
PDF='C:/Users/Eblan/Downloads/Выписка_ИП КОДЫЛЕВ АЛЕКСЕЙ ВЛАДИМИРОВИЧ_40802810500002951090_01.10.2026-31.10.2026.pdf'
cls=[]
with pdfplumber.open(PDF) as pdf:
    for pi,pg in enumerate(pdf.pages):
        words=pg.extract_words()
        lines={}
        for w in words:
            lines.setdefault(round(w['top']),[]).append(w)
        for t in sorted(lines):
            ws=sorted(lines[t], key=lambda w:w['x0'])
            if not ws: continue
            if re.match(r'\d{2}\.\d{2}\.\d{4}', ws[0]['text']) and any(w['text']=='Вид:' for w in ws):
                amt_words=[w for w in ws if w['x0']>590]
                x0=amt_words[0]['x0']
                typ='DEBIT' if x0<650 else 'CREDIT'
                amt=' '.join(w['text'] for w in amt_words)
                cls.append((ws[0]['text'], typ, amt))

print('records', len(recs), 'cls', len(cls))
# align
mismatch=0
for i,(r,c) in enumerate(zip(recs,cls)):
    rnorm=r['amount_str'].replace(' ','')
    cnorm=c[2].replace(' ','')
    if r['date']!=c[0] or rnorm!=cnorm:
        mismatch+=1
        if mismatch<=10:
            print('MISMATCH', i, r['date'], c[0], r['amount_str'], c[2])
print('mismatches', mismatch)

# attach
for r,c in zip(recs,cls):
    r['is_debit'] = (c[1]=='DEBIT')
    r['amount'] = float(r['amount_str'].replace(' ','').replace(',','.'))
    # fix amount_str normalized with spaces? keep original
json.dump(recs, open('C:/Users/Eblan/Downloads/records_classified.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved')
