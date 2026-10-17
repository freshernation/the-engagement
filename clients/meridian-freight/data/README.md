# What Priya sent over

> "Here is last night's export from the TMS and the dispatchers' WhatsApp location
> pins for the same trucks. Hope it helps. P"

| File | What it is |
|---|---|
| `tms_export.csv` | The nightly TMS export, taken at 23:30 on 12 October 2026. One row per shipment |
| `whatsapp_pins.csv` | Every location pin drivers sent their dispatchers, copied out of WhatsApp by hand at 09:30 on 13 October |
| `calls.md` | Eight customer calls one dispatcher wrote down on a single morning |

## Columns

**`tms_export.csv`**: `shipment_id`, `customer`, `origin`, `destination`, `truck`,
`driver_phone`, `dispatched_at`, `planned_eta`, `tms_status`.

**`whatsapp_pins.csv`**: `shipment_id`, `sent_at`, `lat`, `lon`, `note` (whatever the
driver typed, often nothing).

All times are IST. All companies, trucks and phone numbers are invented.

## Before you build anything

Compare a few shipments' `planned_eta` and `tms_status` with their last pin. Then decide
which of the two sources a customer's question should be answered from.
