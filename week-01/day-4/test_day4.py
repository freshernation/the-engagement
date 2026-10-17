"""Week 1, Day 4 - the design and the estimate.

Run me:  pytest week-01/day-4 -v
"""

import re

import pytest

from doccheck import finished, has_number, section, words

HEADINGS = ["Context and scope", "Goals and non-goals", "Options", "Decision", "The design",
            "Evaluation plan", "Risks", "Cost and estimate"]


class TestDesign:
    def test_finished(self, doc):
        finished(doc("DESIGN.md"), "DESIGN.md")

    @pytest.mark.parametrize("heading", HEADINGS)
    def test_sections(self, doc, heading):
        assert words(section(doc("DESIGN.md"), heading)) >= 15, f"'{heading}' is missing or thin."

    def test_two_options(self, doc):
        finished(doc("DESIGN.md"), "DESIGN.md")
        n = section(doc("DESIGN.md"), "Options").count("\n### ")
        assert n >= 2, f"{n} options. One option is a preference, not a design."

    def test_decision_names_an_option(self, doc):
        text = doc("DESIGN.md")
        names = re.findall(r"^### (.+)$", section(text, "Options"), flags=re.M)
        decision = section(text, "Decision").lower()
        assert any(n.strip().lower() in decision for n in names), "Decision does not name one of your options."

    def test_a_picture(self, doc):
        assert "```" in section(doc("DESIGN.md"), "The design"), "The design needs a picture in a code block."

    def test_eval_plan_has_numbers(self, doc):
        body = section(doc("DESIGN.md"), "Evaluation plan").lower()
        assert has_number(body), "How many cases? Write it as a number."
        assert "baseline" in body, "Against what baseline?"

    def test_three_risks(self, doc):
        rows = [l for l in section(doc("DESIGN.md"), "Risks").splitlines()
                if l.startswith("|") and "---" not in l and "Likelihood" not in l]
        assert len(rows) >= 3, f"{len(rows)} risks in the table. At least three."

    def test_estimate_is_a_range(self, doc):
        body = section(doc("DESIGN.md"), "Cost and estimate")
        assert re.search(r"\d+\s*(?:-|–|to)\s*\d+", body), "Give the estimate as a range, like '6 to 9 days'."
        assert re.search(r"(₹|rs\.?|inr|\$).*month|month.*(₹|rs\.?|inr|\$)", body, re.I | re.S), (
            "Say what it costs per month to run, in money."
        )
