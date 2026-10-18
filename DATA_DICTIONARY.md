# Data dictionary — Thai Government Lottery results 2553–2569 (2010–2026)

All prize numbers are stored as **text** (strings) so leading zeros are kept (e.g. `045998`, `07`).
When loading with pandas use `dtype=str`; in spreadsheets import the columns as Text.

## thai-lottery-results.csv (one row per draw, 397 rows)

| Column | Type | Description |
|---|---|---|
| `draw_date` | date, ISO 8601 `YYYY-MM-DD` (Gregorian) | Official draw date. Primary key, unique. |
| `draw_date_be` | text `YYYY-MM-DD` (Thai Buddhist Era) | Same date with the Buddhist Era year (Gregorian year + 543). |
| `draw_date_th` | text | Thai long date, e.g. `16 ตุลาคม 2569`. |
| `year_be` | integer | Buddhist Era year of the draw (2553–2569). |
| `first_prize` | text, 6 digits | First prize number (1 number). |
| `near_first_prize` | text, 6 digits × 2, `;`-separated | Numbers adjacent to the first prize (first prize −1 and +1). |
| `second_prize` | text, 6 digits × 5, `;`-separated | Second prize numbers. |
| `third_prize` | text, 6 digits × 10, `;`-separated | Third prize numbers. |
| `fourth_prize` | text, 6 digits × 50, `;`-separated | Fourth prize numbers. |
| `fifth_prize` | text, 6 digits × 100, `;`-separated | Fifth prize numbers. |
| `front_three_digits` | text, 3 digits × 2, `;`-separated, may be empty | Front three-digit prize. **Empty for draws up to 2015-08-16**: this prize did not exist yet (first appears 2015-09-01). |
| `last_three_digits` | text, 3 digits, `;`-separated | Last three-digit prize. **4 numbers per draw up to 2015-08-16**, 2 numbers from 2015-09-01. |
| `last_two_digits` | text, 2 digits | Last two-digit prize (1 number). |
| `glo_result_pdf` | URL | Link to the official result sheet (PDF) published by the Government Lottery Office for that draw. |

Within each cell, numbers are sorted ascending.

**Known quirk (kept as published):** in the official result sheet for the 2019-08-01 (2562-08-01) draw, the fifth-prize number `354809` is printed twice, so that cell lists it twice and the long file has two identical rows for it.

## thai-lottery-results-long.csv (one row per winning number, 68,681 rows)

| Column | Type | Description |
|---|---|---|
| `draw_date` | date ISO `YYYY-MM-DD` | Draw date (Gregorian). |
| `draw_date_be` | text `YYYY-MM-DD` | Draw date (Buddhist Era). |
| `prize` | text | One of the prize column names above (`first_prize` … `last_two_digits`). |
| `number` | text | One winning number. |

## thai-lottery-results.json

Object with metadata (`name`, `source`, `compiled_by`, `citation`, `license`, `draw_count`, `first_draw`, `last_draw`, `generated`)
and `draws`: an array of 397 objects with the same fields as the wide CSV, where every prize field is an **array of strings**.

## Not included (on purpose)

- **Prize amounts (baht).** The official data feed returns the *current* prize table for old draws, not the amount that applied at the time, so amounts are left out rather than risk wrong values.
- Predictions, "lucky numbers", or any derived guesses. This is a record of published results only.
- Any personal data. The dataset contains dates, numbers and official URLs only.
