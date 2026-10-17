"""Week 2, Day 4 - the handover.

Run me:  pytest week-02/day-4 -v
"""

import re

import pytest

from doccheck import count_items, finished, section, words

HEADINGS = ["What it does", "How to run it", "How you know it is broken", "What to do when it breaks",
            "What is not done", "Result against the target", "Who to call"]


class TestHandover:
    def test_finished(self, doc):
        finished(doc("HANDOVER.md"), "HANDOVER.md")

    @pytest.mark.parametrize("heading", HEADINGS)
    def test_sections(self, doc, heading):
        assert words(section(doc("HANDOVER.md"), heading)) >= 5, f"'{heading}' is missing or empty."

    def test_commands(self, doc):
        assert "```" in section(doc("HANDOVER.md"), "How to run it"), "Put the commands in a code block."

    def test_three_signals(self, doc):
        assert count_items(section(doc("HANDOVER.md"), "How you know it is broken")) >= 3, "At least three signals."

    def test_not_done(self, doc):
        assert count_items(section(doc("HANDOVER.md"), "What is not done")) >= 3, "At least three things not done."

    def test_result(self, doc):
        body = section(doc("HANDOVER.md"), "Result against the target")
        assert len(re.findall(r"\d+", body)) >= 2, "The latest number and the target."
