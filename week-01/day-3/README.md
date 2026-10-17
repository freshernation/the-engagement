# Day 3: The requirements

> **By the end of today** the customer could sign a list of what will be built, and an
> engineer could test every line of it.

---

## Read first

- [ ] Your `PROBLEM.md` and `NOTES.md`
- [ ] Your own week-1 milestone tests from any earlier course · 10 min. You have read
      acceptance tests all along. Today you write them in English.

---

## What you need to know

### A requirement is a promise with a test

"The system should be fast" is a wish. "A dispatcher gets a shipment's latest position
within ten seconds of asking, for any shipment dispatched in the last 72 hours" is a
requirement, because you can check it and the customer can see you checked it.

Each requirement gets:

- an **ID** (`R1`, `R2`…) so it can be argued about by name,
- a **priority**: **Must** (without it, the target is missed), **Should** (important,
  can slip a week), **Could** (if there is time),
- an **"Accepted when"** line: the check that proves it is done.

### Not everything is a Must

If every requirement is a Must, none of them is. A list with more than about half Musts
is a list nobody prioritised, and in week 2 something will slip without anyone having
decided which.

### Constraints are not requirements

Where the data may live, who must approve what, what the customer will not install.
They limit every design. List them separately, each with where it came from.

### Open questions

What you still do not know, who will answer it, and by when. An open question with an
owner is a plan. Without one it is a risk.

---

## Exercises

Write `REQUIREMENTS.md`. Then the editor.

```bash
pytest week-01/day-3 -v
```
