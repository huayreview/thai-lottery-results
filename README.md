# Thai Government Lottery Results 2553–2569 (2010–2026) · ผลสลากกินแบ่งรัฐบาลย้อนหลัง

**397 draws · 1 March 2010 (2553) – 16 October 2026 (2569) · every prize tier · CSV + JSON · CC BY 4.0**

Source: [huayreview.net](https://huayreview.net/stats/ten-year-data/) · underlying results published by the
Government Lottery Office of Thailand ([glo.or.th](https://www.glo.or.th/)).

[English](#english) · [ภาษาไทย](#ภาษาไทย)

---

## English

### What this is
A clean, machine-readable record of every Thai Government Lottery draw result from the first draw available in
the Government Lottery Office's public results (1 March 2010 / 2553) to the latest draw (16 October 2026 / 2569).
Every prize tier is included: first prize, near-first prizes, 2nd–5th prizes, front three digits, last three digits
and last two digits.

### Files
| File | Rows | Description |
|---|---|---|
| `thai-lottery-results.csv` | 397 | One row per draw (wide format). |
| `thai-lottery-results-long.csv` | 68,681 | One row per winning number (long / tidy format). |
| `thai-lottery-results.json` | 397 draws | Same data, prize fields as arrays, plus metadata. |
| `DATA_DICTIONARY.md` | – | Full column descriptions. |
| `CHECKSUMS.sha1` | – | SHA-1 of each data file. |

Draws per Buddhist Era year: 2553: 21 (results start 1 Mar 2010) · 2554–2562: 24 each · 2563: 21 (no draws
16 Apr–16 May 2020) · 2564–2566: 24 each · 2567: 23 · 2568: 24 · 2569: 20 (to 16 Oct 2026).

### Columns (wide CSV)
`draw_date` (ISO `YYYY-MM-DD`), `draw_date_be` (Buddhist Era `YYYY-MM-DD`), `draw_date_th` (Thai long date),
`year_be`, `first_prize`, `near_first_prize`, `second_prize`, `third_prize`, `fourth_prize`, `fifth_prize`,
`front_three_digits`, `last_three_digits`, `last_two_digits`, `glo_result_pdf`.
Multiple numbers in one cell are separated by `;`. **Read all number columns as text** to keep leading zeros
(`pd.read_csv(path, dtype=str)`). See [DATA_DICTIONARY.md](DATA_DICTIONARY.md).

Format notes: the front-three-digit prize starts on 1 Sep 2015, so `front_three_digits` is empty before that;
up to 16 Aug 2015 there were four last-three-digit numbers per draw (two afterwards). Prize amounts are not
included because the official feed only returns today's prize table for older draws. One quirk is kept as
published: the official 2019-08-01 result sheet lists fifth prize `354809` twice.

### Source and verification
- **Source:** results published by the Government Lottery Office of Thailand (glo.or.th), taken from its public
  results service; each row links to the official result sheet PDF (`glo_result_pdf`).
- **Verification:** every one of the 397 draws was cross-checked against a second, independent public results
  source. The first prize, front three digits, last three digits and last two digits matched for **397/397 draws**.
  The data also passed automated checks: unique dates, correct count of numbers per prize tier, correct digit length,
  near-first prizes equal to first prize ±1.
- Always confirm against the official GLO result sheet before claiming a prize.

### Update cadence
Thai Government Lottery draws are normally held twice a month (around the 1st and 16th; dates move for holidays).
This dataset is refreshed after new draws are published; the most current results are always on
[huayreview.net](https://huayreview.net/stats/ten-year-data/).

### What is NOT in this dataset
No predictions, no "lucky numbers", no tips — only results as officially published. No personal data.

### Quick start
```python
import pandas as pd
df = pd.read_csv("thai-lottery-results.csv", dtype=str, parse_dates=["draw_date"])
print(len(df), df["draw_date"].min().date(), df["draw_date"].max().date())
```

### License and citation
The compilation (structure, cleaning, verification, documentation) is released under
**[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**. The underlying draw results are public facts
published by the Government Lottery Office.

Please credit:

> Source: huayreview.net — https://huayreview.net/stats/ten-year-data/

BibTeX:
```bibtex
@misc{huayreview_thai_lottery_2026,
  title  = {Thai Government Lottery Results 2553--2569 (2010--2026)},
  author = {{huayreview.net}},
  year   = {2026},
  url    = {https://huayreview.net/stats/ten-year-data/},
  note   = {Underlying results: Government Lottery Office of Thailand (glo.or.th). License: CC BY 4.0}
}
```

---

## ภาษาไทย

### ชุดข้อมูลนี้คืออะไร
ผลสลากกินแบ่งรัฐบาลครบทุกงวด ตั้งแต่งวดแรกที่มีในระบบผลรางวัลสาธารณะของสำนักงานสลากกินแบ่งรัฐบาล
(1 มีนาคม 2553) จนถึงงวดล่าสุด (16 ตุลาคม 2569) รวม **397 งวด** ครบทุกรางวัล ได้แก่ รางวัลที่ 1
รางวัลข้างเคียงรางวัลที่ 1 รางวัลที่ 2–5 เลขหน้า 3 ตัว เลขท้าย 3 ตัว และเลขท้าย 2 ตัว
ในรูปแบบ CSV และ JSON ที่นำไปใช้กับโปรแกรมได้ทันที

### ไฟล์
- `thai-lottery-results.csv` — 1 แถวต่อ 1 งวด (397 แถว)
- `thai-lottery-results-long.csv` — 1 แถวต่อ 1 เลขที่ถูกรางวัล (68,681 แถว)
- `thai-lottery-results.json` — ข้อมูลชุดเดียวกัน แบบ JSON พร้อมข้อมูลกำกับ
- `DATA_DICTIONARY.md` — คำอธิบายคอลัมน์ทั้งหมด

### คอลัมน์
`draw_date` วันที่ออกรางวัลแบบ ค.ศ. (YYYY-MM-DD) · `draw_date_be` วันที่แบบ พ.ศ. · `draw_date_th` วันที่ภาษาไทย ·
`year_be` ปี พ.ศ. · `first_prize` รางวัลที่ 1 · `near_first_prize` รางวัลข้างเคียงรางวัลที่ 1 ·
`second_prize`–`fifth_prize` รางวัลที่ 2–5 · `front_three_digits` เลขหน้า 3 ตัว · `last_three_digits` เลขท้าย 3 ตัว ·
`last_two_digits` เลขท้าย 2 ตัว · `glo_result_pdf` ลิงก์ใบตรวจผลทางการ (PDF)
เลขหลายตัวในช่องเดียวคั่นด้วย `;` ควรอ่านทุกคอลัมน์เป็นข้อความ เพื่อไม่ให้เลข 0 นำหน้าหาย

ข้อสังเกต: เลขหน้า 3 ตัวเริ่มมีตั้งแต่งวด 1 ก.ย. 2558 งวดก่อนหน้านั้นช่องนี้จึงว่าง และถึงงวด 16 ส.ค. 2558
เลขท้าย 3 ตัวมี 4 รางวัลต่องวด · ไม่ได้ใส่จำนวนเงินรางวัล เพราะระบบทางการให้ตารางเงินรางวัลปัจจุบัน
ไม่ใช่อัตราที่ใช้ในงวดนั้นจริง · งวด 1 ส.ค. 2562 ใบตรวจผลทางการพิมพ์รางวัลที่ 5 เลข `354809` ซ้ำ 2 ครั้ง ชุดข้อมูลนี้คงไว้ตามประกาศ

### ที่มาและวิธีตรวจสอบ
- **ที่มา:** ผลรางวัลที่สำนักงานสลากกินแบ่งรัฐบาลประกาศ (glo.or.th) ทุกงวดมีลิงก์ใบตรวจผลทางการแนบไว้
- **การตรวจสอบ:** ทุกงวดตรวจเทียบกับแหล่งผลรางวัลสาธารณะแหล่งที่สอง รางวัลที่ 1 เลขหน้า 3 ตัว
  เลขท้าย 3 ตัว และเลขท้าย 2 ตัว ตรงกัน **397 จาก 397 งวด** และผ่านการตรวจอัตโนมัติ
  (วันที่ไม่ซ้ำ จำนวนเลขแต่ละรางวัลถูกต้อง จำนวนหลักถูกต้อง รางวัลข้างเคียง = รางวัลที่ 1 ±1)
- ก่อนขึ้นเงินรางวัล ให้ตรวจกับใบตรวจผลทางการของสำนักงานสลากฯ อีกครั้งเสมอ

### การอัปเดต
สลากกินแบ่งรัฐบาลออกรางวัลเดือนละ 2 ครั้ง (ราววันที่ 1 และ 16 ของเดือน เลื่อนได้ตามวันหยุด)
ชุดข้อมูลนี้อัปเดตหลังมีผลงวดใหม่ ผลล่าสุดดูได้ที่ [huayreview.net](https://huayreview.net/stats/ten-year-data/)

### สิ่งที่ไม่มีในชุดข้อมูลนี้
ไม่มีการทำนาย ไม่มีเลขเด็ด ไม่มีการใบ้หวย มีเฉพาะผลที่ประกาศอย่างเป็นทางการ และไม่มีข้อมูลส่วนบุคคล

### สัญญาอนุญาตและการอ้างอิง
การรวบรวมข้อมูลชุดนี้เผยแพร่ภายใต้ **CC BY 4.0** ส่วนผลรางวัลเป็นข้อเท็จจริงที่สำนักงานสลากฯ ประกาศต่อสาธารณะ
เมื่อนำไปใช้ กรุณาอ้างอิง:

> Source: huayreview.net — https://huayreview.net/stats/ten-year-data/
