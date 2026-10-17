# Day zero

Thirty minutes. Do it before week 1.

---

## 1. Python 3.10 or newer, and your own copy

Make your own copy of this repository on GitHub (**Use this template**), then:

```bash
git clone https://github.com/YOUR-USERNAME/the-engagement.git
cd the-engagement
python3 -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
```

Every test fails. That is correct: there are no documents yet.

## 2. Choose your client

Read the three `BRIEF.md` files in `clients/`. Pick the one you know least about. The
point is to learn a business you have never worked in, which is what the job is.

Write it at the top of `logs/signal-log.md`:

```
Client: meridian-freight
```

Do **not** open that client's `CUSTOMER.md`.

## 3. Set up the customer

Open a fresh chat with any capable model. Paste `ai/customer.md`, then, without
reading it, paste your client's `CUSTOMER.md` where it asks. Say hello and stop.
You will interview them on Monday.

If you are taking the live version, your instructor plays the customer and you skip
this step.

## 4. Your week-2 code

Week 2 builds a first slice in `week-02/build/`. Use your own code from the earlier
courses: your agent, your retrieval pipeline, your service. Copy what you need in on
Monday of week 2, not before.

You will need a model key in week 2. Nothing in week 1 needs one, except the AI
customer and stakeholder, which run in an ordinary chat.
