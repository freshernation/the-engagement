"""Week 2, Day 2 - the status update.

Run me:  pytest week-02/day-2 -v
"""

import re

from doccheck import count_items, finished, section, words

DATE = re.compile(r"\b(\d{1,2}\s+[A-Z][a-z]{2,8}|\d{4}-\d{2}-\d{2}|[A-Z][a-z]{2,8}\s+\d{1,2})\b")


class TestStatus:
    def test_finished(self, doc):
        finished(doc("STATUS.md"), "STATUS.md")

    def test_summary_leads_with_a_colour(self, doc):
        body = section(doc("STATUS.md"), "Summary").strip()
        assert re.match(r"\**\s*(Green|Amber|Red)\b", body), "Start the summary with Green, Amber or Red."
        assert words(body) <= 60, f"Summary is {words(body)} words. Under 60."

    def test_number_against_target(self, doc):
        body = section(doc("STATUS.md"), "Against the target")
        assert len(re.findall(r"\d+", body)) >= 2, "The current number and the target."
        assert "target" in body.lower(), "Name the target."

    def test_done_and_next(self, doc):
        text = doc("STATUS.md")
        assert count_items(section(text, "Done")) >= 1, "What was done?"
        assert count_items(section(text, "Next")) >= 1, "What is next?"

    def test_risks(self, doc):
        assert count_items(section(doc("STATUS.md"), "Risks")) >= 2, "At least two risks. There are always two."

    def test_decisions_have_dates(self, doc):
        body = section(doc("STATUS.md"), "Decisions needed")
        items = [l for l in body.splitlines() if re.match(r"^\s*(?:[-*]|\d+\.)\s+\S", l)]
        assert items, "At least one decision the customer owes you."
        for item in items:
            assert DATE.search(item), f"No date on: {item.strip()}"
