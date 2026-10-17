"""Week 1, Day 1 - the discovery interview.

Run me:  pytest week-01/day-1 -v

The tests check that your questions avoid the obvious traps and that your notes
are sorted. Whether you found the real problem is Friday's question.
"""

import re

from doccheck import count_items, finished, section

FUTURE = re.compile(
    r"\b(would you|do you think|would it|could you see|if we built|how much would you pay|"
    r"would that|will you|are you interested)\b",
    re.I,
)
PAST = re.compile(r"\b(last|yesterday|this week|most recent|previous|ago)\b", re.I)


def questions(text):
    return [l for l in text.splitlines() if re.match(r"^\s*(?:[-*]|\d+\.)\s+.*\?\s*$", l)]


class TestQuestions:
    def test_finished(self, doc):
        finished(doc("QUESTIONS.md"), "QUESTIONS.md")

    def test_twelve(self, doc):
        n = len(questions(doc("QUESTIONS.md")))
        assert n >= 12, f"{n} questions. Bring at least twelve; you will not use them all."

    def test_none_ask_for_a_prediction(self, doc):
        finished(doc("QUESTIONS.md"), "QUESTIONS.md")
        bad = [q.strip() for q in questions(doc("QUESTIONS.md")) if FUTURE.search(q)]
        assert not bad, "These ask the customer to predict or rate, and will get a polite yes:\n" + "\n".join(bad)

    def test_five_about_the_past(self, doc):
        past = [q for q in questions(doc("QUESTIONS.md")) if PAST.search(q)]
        assert len(past) >= 5, f"{len(past)} questions about a specific past event. Ask about the last time."


class TestNotes:
    def test_finished(self, doc):
        finished(doc("NOTES.md"), "NOTES.md")

    def test_facts(self, doc):
        n = count_items(section(doc("NOTES.md"), "Facts"))
        assert n >= 8, f"{n} facts. Forty minutes should give you at least eight."

    def test_quotes_are_verbatim(self, doc):
        quotes = re.findall(r"^\s*>\s*\S", section(doc("NOTES.md"), "Quotes"), flags=re.M)
        assert len(quotes) >= 5, f"{len(quotes)} quotes. Write down at least five things exactly as said, as '> ' lines."

    def test_numbers_have_digits(self, doc):
        body = section(doc("NOTES.md"), "Numbers")
        items = [l for l in body.splitlines() if re.match(r"^\s*(?:[-*]|\d+\.)\s+\S", l)]
        with_digits = [l for l in items if re.search(r"\d", re.sub(r"^\s*\d+\.", "", l))]
        assert len(with_digits) >= 5, f"{len(with_digits)} numbers. A number has digits in it."

    def test_constraints(self, doc):
        assert count_items(section(doc("NOTES.md"), "Constraints")) >= 2, "Name at least two constraints."

    def test_opinions_kept_apart(self, doc):
        assert count_items(section(doc("NOTES.md"), "Opinions")) >= 1, (
            "No opinions recorded. Every customer gives some; put them here, not under Facts."
        )

    def test_unknowns(self, doc):
        assert count_items(section(doc("NOTES.md"), "Unknowns")) >= 3, "List at least three things you still need to find out."
