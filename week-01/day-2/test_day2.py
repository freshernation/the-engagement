"""Week 1, Day 2 - the real problem.

Run me:  pytest week-01/day-2 -v
"""

import re

import pytest

from doccheck import count_items, finished, has_number, section, words

HEADINGS = ["The ask", "The problem", "Who has it", "What it costs today", "How we will know", "Non-goals", "Why now"]


class TestProblem:
    def test_finished(self, doc):
        finished(doc("PROBLEM.md"), "PROBLEM.md")

    @pytest.mark.parametrize("heading", HEADINGS)
    def test_sections(self, doc, heading):
        body = section(doc("PROBLEM.md"), heading)
        assert words(body) >= 5, f"'{heading}' is missing or empty."

    def test_problem_is_short(self, doc):
        finished(doc("PROBLEM.md"), "PROBLEM.md")
        n = words(section(doc("PROBLEM.md"), "The problem"))
        assert n <= 60, f"The problem is {n} words. If it takes more than sixty, you have not found it yet."

    def test_problem_is_not_the_ask(self, doc):
        text = doc("PROBLEM.md")
        ask = " ".join(section(text, "The ask").lower().split())
        problem = " ".join(section(text, "The problem").lower().split())
        assert ask != problem, "The problem is the ask, restated. What is the ask a guess at fixing?"

    def test_cost_has_a_number(self, doc):
        assert has_number(section(doc("PROBLEM.md"), "What it costs today")), "What it costs today has no number."

    def test_baseline_and_target(self, doc):
        body = section(doc("PROBLEM.md"), "How we will know").lower()
        assert "baseline" in body and "target" in body, "Name the baseline and the target."
        assert len(re.findall(r"\d+", body)) >= 2, "The baseline and the target each need a number."

    def test_three_non_goals(self, doc):
        n = count_items(section(doc("PROBLEM.md"), "Non-goals"))
        assert n >= 3, f"{n} non-goals. Write at least three; each is an argument you will not have later."
