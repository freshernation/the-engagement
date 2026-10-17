# The Engagement

Two weeks from "the customer asked for a chatbot" to a working system, a signed-off
scope, a handover, and a case study you can show anyone.

Every other course on the route teaches you to build. This one teaches the half of a
forward deployed engineer's job that happens before the build, during it, and after it:
finding the real problem, writing down what will and will not be built, saying no to a
scope change without losing the customer, and handing the thing over so it survives
without you.

There is very little code. There is a lot of writing, and every document is attacked.

---

## Who this is for

You have finished the core route (Agent From Zero, Retrieval Under Test, Agent In
Production), or you have built and deployed an AI system you can explain line by line.
Week 2 asks you to build a first slice in four days with whatever you already know.
It does not teach you anything technical.

---

## The rules

**1. The twenty-minute rule.** Stuck for twenty minutes: open the tutor. Still stuck:
bring it to the live hour. Log it in `logs/stuck-log.md`.

**2. Do not read a client's `CUSTOMER.md`.** It is the sheet the AI customer plays from,
and it holds what the customer will only tell you if you ask well. Reading it first is
reading the answers: your tests will pass and your Friday defence will not.

**3. Facts beat opinions.** Anything a customer says about the future ("we would use
it", "it would save time") is an opinion. Anything they say about last week is a fact.
Every document in this course is built from facts.

**4. Nothing counts until the tests pass and it is pushed.**

---

## The two weeks

| Week | | Milestone |
|---|---|---|
| 1 | Before the build | **Project 1**: a proposal the customer's decision maker can say yes to |
| 2 | The engagement | **Project 2**: a working slice, a scope change handled, a handover, and a case study |

### Week 1: Before the build

| Day | | You produce |
|---|---|---|
| Mon | The discovery interview | `QUESTIONS.md`, then `NOTES.md` from a 40-minute interview |
| Tue | The real problem | `PROBLEM.md`: the ask, the problem, the number, the non-goals |
| Wed | The requirements | `REQUIREMENTS.md`: numbered, prioritised, each with its acceptance test |
| Thu | The design and the estimate | `DESIGN.md`: two options, one chosen, the eval plan, the cost |
| Fri | **The proposal** | `PROPOSAL.md`, defended in front of a sceptical decision maker |

### Week 2: The engagement

| Day | | You produce |
|---|---|---|
| Mon | The first slice | An eval set from the customer's data, a baseline, a first build |
| Tue | The status update | `STATUS.md`: the number, the risks, the decision you need from them |
| Wed | The scope change | `CHANGE.md`: the impact, the options, and the reply you send |
| Thu | The handover | `HANDOVER.md`: how it runs, how you know it broke, what is not done |
| Fri | **The case study** | `CASE_STUDY.md` and a live demo to the customer |

Week 1 Monday is the keystone. Every document after it is only as good as the facts
you came out of that interview with.

---

## The clients

Three companies, invented, each with a problem that looks like an AI problem and is
only partly one. You pick one on day zero and keep it for both weeks.

| Client | What they ask for |
|---|---|
| `clients/meridian-freight/` | "An AI chatbot for our drivers" |
| `clients/sahyadri-hospital/` | "Use AI to summarise patient records" |
| `clients/kaveri-finance/` | "An AI agent that approves loans" |

Each folder has a `BRIEF.md` (read it), a `data/` folder (use it in week 2) and a
`CUSTOMER.md` (do not read it; see rule 2). The customer is played by an AI with
`ai/customer.md`, or by your instructor in the live version.

---

## How to work

```bash
source .venv/bin/activate
pytest week-01/day-1 -v        # one day
pytest week-01 -v              # one week
```

The tests check that a document is finished: the sections exist, the numbers are
there, the non-goals are listed, the word limit is kept. They cannot check that it is
any good. That is what the editor, the stakeholder and Friday are for.

| | Checks | Can it be faked |
|---|---|---|
| `pytest` | the document is complete | yes, easily |
| The editor (`ai/editor.md`) | the document is clear and honest | partly |
| **The Friday defence** | whether it survives the person paying for it | no |

---

## Map

| Path | What it is |
|---|---|
| `SETUP.md` | Day zero |
| `week-01/`, `week-02/` | Four days, a milestone, a fence, a defence |
| `clients/` | The three clients: brief, data, and the sheet you do not read |
| `ai/` | The customer, the stakeholder, the tutor, the editor, the defence |
| `logs/` | Your stuck log and your signal log |
| `SOURCES.md` | What to read, and why |
| `CUT_LIST.md` | What this course deliberately does not teach |

---

## The one thing you keep

`CASE_STUDY.md`. One page: the situation, the real problem, what you built and what
you refused to, the measured result, and what you would do differently. It is the
document an FDE interviewer, a freelance client and a hiring manager all ask for in
different words. Write it so a stranger believes it.
