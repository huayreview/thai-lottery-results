"""Validate the release files. Exit 1 on any failure."""
import csv, json, re, sys, os, datetime
H = os.path.dirname(os.path.abspath(__file__)); fails = []
def chk(c, msg):
    if not c: fails.append(msg)
W = list(csv.DictReader(open(os.path.join(H, 'thai-lottery-results.csv'), encoding='utf-8')))
J = json.load(open(os.path.join(H, 'thai-lottery-results.json'), encoding='utf-8'))
L = list(csv.DictReader(open(os.path.join(H, 'thai-lottery-results-long.csv'), encoding='utf-8')))
TH = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
chk(len(W) == 398, f'wide rows {len(W)} != 398'); chk(J['draw_count'] == len(J['draws']) == len(W), 'json count mismatch')
dates = [r['draw_date'] for r in W]
chk(len(set(dates)) == len(dates), 'duplicate draw_date'); chk(dates == sorted(dates), 'not sorted')
chk(len({tuple(r.values()) for r in W}) == len(W), 'duplicate rows')
# Known official quirk: the GLO result sheet for 2019-08-01 prints fifth prize 354809 twice (kept as published).
KNOWN_DUP = {('2019-08-01', '2562-08-01', 'fifth_prize', '354809')}
import collections
dup_long = {k for k, v in collections.Counter(tuple(r.values()) for r in L).items() if v > 1}
chk(dup_long <= KNOWN_DUP, f'unexpected duplicate long rows {sorted(dup_long - KNOWN_DUP)}')
print('known official duplicates present:', sorted(dup_long))
SPEC = {'first_prize': (1, 6), 'near_first_prize': (2, 6), 'second_prize': (5, 6), 'third_prize': (10, 6), 'fourth_prize': (50, 6), 'fifth_prize': (100, 6), 'last_two_digits': (1, 2)}
total = 0
for r, j in zip(W, J['draws']):
    d = r['draw_date']
    try: dt = datetime.date.fromisoformat(d)
    except Exception: fails.append(f'{d} bad ISO date'); continue
    chk(re.fullmatch(r'\d{4}-\d{2}-\d{2}', d) is not None, f'{d} not ISO')
    chk(r['draw_date_be'] == f'{dt.year+543}-{dt.month:02d}-{dt.day:02d}', f'{d} BE date')
    chk(r['draw_date_th'] == f'{dt.day} {TH[dt.month-1]} {dt.year+543}', f'{d} Thai date')
    chk(int(r['year_be']) == dt.year + 543 and 2553 <= int(r['year_be']) <= 2569, f'{d} year_be')
    for col, (n, w) in SPEC.items():
        v = r[col].split(';'); chk(len(v) == n and all(re.fullmatch(r'\d{%d}' % w, x) for x in v), f'{d} {col}')
    f3 = [x for x in r['front_three_digits'].split(';') if x]; b3 = r['last_three_digits'].split(';')
    if d <= '2015-08-16': chk(not f3 and len(b3) == 4, f'{d} old 3-digit format')
    else: chk(len(f3) == 2 and len(b3) == 2, f'{d} new 3-digit format')
    chk(all(re.fullmatch(r'\d{3}', x) for x in f3 + b3), f'{d} 3-digit width')
    fp = int(r['first_prize']); chk(sorted(r['near_first_prize'].split(';')) == sorted(f'{(fp+k) % 1000000:06d}' for k in (-1, 1)), f'{d} near1 != first±1')
    chk(r['glo_result_pdf'].startswith('https://api.glo.or.th/'), f'{d} pdf url')
    for col in list(SPEC) + ['front_three_digits', 'last_three_digits']:
        chk(';'.join(j[col]) == r[col], f'{d} json/csv mismatch {col}')
    total += sum(len([x for x in r[c].split(';') if x]) for c in list(SPEC) + ['front_three_digits', 'last_three_digits'])
chk(total == len(L), f'long rows {len(L)} != {total}')
print(f'wide rows={len(W)} unique_dates={len(set(dates))} first={dates[0]} last={dates[-1]} long_rows={len(L)} json_draws={len(J["draws"])}')
print('VALIDATION:', 'PASS' if not fails else 'FAIL'); [print(' -', x) for x in fails[:50]]
sys.exit(1 if fails else 0)
