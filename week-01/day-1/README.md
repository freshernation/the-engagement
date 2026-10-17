# Day 1: The discovery interview

> **By the end of today** you have forty minutes of facts about a business you did not
> understand this morning, and you know which of the things you were told are opinions.

---

## Read first

- [ ] Rob Fitzpatrick, *The Mom Test*, chapters 1 and 2 · 45 min
- [ ] Palantir, [*Dev versus Delta*](https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87) · 10 min: what a forward deployed engineer is judged on
- [ ] Your client's `BRIEF.md`, twice

---

## What you need to know

### Why customers lie to you

Not on purpose. Ask someone whether they would use the thing you are about to build and
they will say yes, because saying no to a person in front of you is rude. Ask how much
it would save and they will guess high, because they want it to be true. Every answer
about the future is a compliment or a guess. Neither can be built on.

### What to ask instead

Three rules, from the reading:

1. **Talk about their work, not your idea.** You have no idea yet. You have an ask.
2. **Ask about specific past events.** "Walk me through the last time this happened."
   "How long did the last one take?" "What did you do when it went wrong last week?"
3. **Listen more than you talk.** If you are explaining, you are not learning.

And two for this job in particular:

4. **Find the number.** How often, how long, how much, how many people. A problem without
   a number cannot be shown to be solved.
5. **Ask why now.** Something changed, or nobody would have called you. Whatever it is
   decides what success means to the person who pays.

### Facts, quotes, opinions

Write down exactly what was said, in quotation marks, as often as you can. Afterwards,
sort every line into a fact (something that happened), a number, a constraint, or an
opinion (anything about the future or anyone's feelings). The opinions are not
useless. They are just not evidence.

---

## Exercises

### 1. `QUESTIONS.md`: before the interview

At least twelve questions. At least five must ask about a specific past event (the
word "last", "yesterday", "this week" or "most recent" is a good sign). None may ask
the customer to predict their own behaviour or rate your idea: no "would you", "do you
think", "how much would you pay".

### 2. The interview: forty minutes

Open your customer chat (`ai/customer.md`). Run the interview. Take notes as you go.
Ask follow-ups you did not plan; the plan is a safety net, not a script. When the
customer says they have to go, ask what happens next, then type **DEBRIEF**.

### 3. `NOTES.md`: the same afternoon

Sort what you heard. The customer's DEBRIEF will tell you what you missed. **Do not
add the missed facts to your notes.** You did not get them. Book a follow-up and get
them properly tomorrow, with a better question.

```bash
pytest week-01/day-1 -v
```

---

## Before you close the laptop

Copy the customer's `SIGNAL` block into `logs/signal-log.md`. Commit, push.
