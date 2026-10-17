# Day 4: The design and the estimate

> **By the end of today** you have chosen between two ways to build it, on paper, for
> reasons the customer would accept, and you can say what it will cost as a range you
> would defend.

---

## Read first

- [ ] Malte Ubl, [*Design Docs at Google*](https://www.industrialempathy.com/posts/design-docs-at-google/) · 20 min
- [ ] Steve McConnell, *Software Estimation*, chapter 1 · 30 min
- [ ] Your `REQUIREMENTS.md`

---

## What you need to know

### Two options, always

One option is not a design, it is a preference. Write at least two real ones, and make
one of them **the cheapest thing that could possibly work**: often no model at all, or a
model doing one narrow step inside ordinary code. If the cheap option meets the Musts,
it wins, and saying so is the most credible sentence in your proposal.

### The picture

Every part, every store, every outside service, and where the customer's data goes. A
customer who has a data constraint will look at the arrows before anything else.

### The evaluation plan

How you will know, in week 2, whether it works: how many test cases, built from what
data, scored how, against what baseline. You did this in every earlier course. The
difference now is that the cases come from the customer, and the customer must agree
they are real.

### An estimate is a range

McConnell's point: an estimate is a prediction, a target is a wish, a commitment is a
promise. A single number is read as all three. Give a range, in days and in money per
month, and say what would move it to either end.

### Risks

What could make this fail, how likely, what it would cost, and what you will do about
it. "The data is worse than the sample" is on almost every list. Write the specific
version.

---

## Exercises

Write `DESIGN.md`. Then the editor, and then **red-team it**: give it to the stakeholder
role with the first paragraph only, and see what they ask.

```bash
pytest week-01/day-4 -v
```
