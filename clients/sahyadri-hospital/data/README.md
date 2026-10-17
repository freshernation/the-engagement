# What Dr Joshi sent over

> "Five de-identified case files from last week, the pharmacy record for the same
> patients, and our discharge summary format. IT has approved these five for the
> engagement only. MJ"

| File | What it is |
|---|---|
| `cases/case-01.md` … `case-05.md` | Typed progress notes, as exported from the hospital system. Patients are identified by a case number only |
| `pharmacy.csv` | Every medicine dispensed and returned for those five patients |
| `SUMMARY_FORMAT.md` | The discharge summary layout. Fixed by the hospital's accreditation; do not change it |

Every patient, doctor and record here is invented. Nothing is real clinical advice.

## Before you build anything

Write, by hand, the "medications at discharge" section for all five cases from the notes
alone. Then check each against `pharmacy.csv`. Count how many you would have got wrong.
