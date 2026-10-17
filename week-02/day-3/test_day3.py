"""Week 2, Day 3 - the scope change.

Run me:  pytest week-02/day-3 -v
"""

import re

from doccheck import finished, section, words


class TestChange:
    def test_finished(self, doc):
        finished(doc("CHANGE.md"), "CHANGE.md")

    def test_request_quoted(self, doc):
        assert re.search(r"^\s*>\s*\S", section(doc("CHANGE.md"), "The request"), flags=re.M), (
            "Quote the request exactly, as a '> ' line."
        )

    def test_behind_it(self, doc):
        assert words(section(doc("CHANGE.md"), "What is behind it")) >= 15, "What worry or event caused the request?"

    def test_impact_in_numbers(self, doc):
        body = section(doc("CHANGE.md"), "Impact")
        assert len(re.findall(r"\d+", body)) >= 2, "Give the impact in numbers: days, money, the target."

    def test_three_options_including_defer(self, doc):
        body = section(doc("CHANGE.md"), "Options")
        assert body.count("\n### ") >= 3, "At least three options."
        assert re.search(r"defer|later|after", body, re.I), "One option should be to defer it."

    def test_recommendation_names_an_option(self, doc):
        text = doc("CHANGE.md")
        names = [n.strip().lower() for n in re.findall(r"^### (.+)$", section(text, "Options"), flags=re.M)]
        rec = section(text, "Recommendation").lower()
        assert any(n in rec for n in names), "The recommendation names one of the options by its heading."

    def test_reply_is_short(self, doc):
        n = words(section(doc("CHANGE.md"), "The reply"))
        assert 20 <= n <= 150, f"The reply is {n} words. Between 20 and 150."

    def test_how_they_took_it(self, doc):
        assert words(section(doc("CHANGE.md"), "How they took it")) >= 10, "What did the customer say back?"
