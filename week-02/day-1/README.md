# Day 1: The first slice

> **By the end of today** you have at least twenty cases built from the customer's own
> data, a baseline number on them, and a first slice of the system you can run.

---

## Read first

- [ ] Your client's `data/README.md`, and every file it lists, by eye
- [ ] Your `DESIGN.md`: the evaluation plan and the Musts
- [ ] `EVALS.md` from Retrieval Under Test, or the evals week of whichever agent course
      you took · 10 min

---

## What you need to know

### Cases before code

The same rule as Retrieval Under Test week 1, now with a customer. Every case is one
real question or one real record from `data/`, with the answer the customer would accept
and where in the data that answer comes from. Twenty is the floor, not the target.

Include the ugly ones: the record with the missing field, the shipment with no recent
pin, the statement that does not add up. Every client's data has a trap in it,
and at least one case should step on it.

### The baseline is what they do today

Not "the model with no retrieval". What the customer's people do now: the dispatcher's
answer, the resident's summary, the credit officer's spreadsheet. Score that on your
cases where you can, from the data, or say exactly why you cannot.

### The first slice

The thinnest version that meets one Must end to end, on real data. Not every Must. Not
a demo with hard-coded answers. One path, honest, measured.

---

## Exercises

1. `evals.jsonl`: one JSON object per line: `id`, `input`, `expected`, `source` (the file
   and the record or line the answer comes from).
2. `EVALS.md`: what is measured and how, the baseline, the first slice's score, and which
   cases fail and why.
3. The slice itself, in `../build/`.

```bash
pytest week-02/day-1 -v
```

---

## Before you close the laptop

Tell the customer. One message: what you built today, the number, and the first case it
gets wrong. Put the message in `EVALS.md` under "Sent to the customer".
