# Day 4: The handover

> **By the end of today** an engineer at the customer who has never met you could run
> the system, tell when it is broken, and know what was left undone.

---

## Read first

- [ ] Your own `ARCHITECTURE.md` and `RUNBOOK.md` from Agent In Production · 15 min
- [ ] `../build/README.md`

---

## What you need to know

### You are leaving

Every forward deployed engagement ends with you moving to the next customer. What you
built either keeps working without you or quietly stops, and the customer remembers which.
The handover is the difference.

### Who reads it

An engineer at the customer, competent, busy, and not an AI specialist. They need: what it
does, how to start it, how to tell it is unhealthy, what to do then, and who to call when
that does not work.

### How you know it is broken

Not "check the logs". Specific signals: the number of cases passing drops below a line;
answers stop citing a source; the nightly data did not arrive. Each one with where to
look.

### What is not done

Every Should and Could you did not build, every known failing case, every shortcut. Writing
it down is not admitting failure. It is the list the customer's next budget is built from,
and the reason they call you back.

---

## Exercises

Write `HANDOVER.md`. Then have a fresh chat with no context follow its "How to run it"
section literally, from a clean clone. Fix every place it got stuck.

```bash
pytest week-02/day-4 -v
```
