"""Week 2 Milestone - the case study and the demo.

Run me:  pytest week-02/milestone -v
"""

import re

import pytest

from doccheck import count_items, finished, has_number, section, words

HEADINGS = ["Summary", "The ask and the real problem", "What we built", "What we refused to build",
            "The result", "What changed along the way", "What I would do differently", "Evidence"]


class TestCaseStudy:
    def test_finished(self, doc):
        finished(doc("CASE_STUDY.md"), "CASE_STUDY.md")

    @pytest.mark.parametrize("heading", HEADINGS[:-1])  # Evidence is links; test_evidence_links covers it
    def test_sections(self, doc, heading):
        assert words(section(doc("CASE_STUDY.md"), heading)) >= 10, f"'{heading}' is missing or thin."

    def test_summary(self, doc):
        body = section(doc("CASE_STUDY.md"), "Summary")
        assert words(body) <= 80, f"Summary is {words(body)} words. Under 80."
        assert has_number(body), "The summary needs the result, with a number."

    def test_length(self, doc):
        finished(doc("CASE_STUDY.md"), "CASE_STUDY.md")
        n = words(doc("CASE_STUDY.md"))
        assert n <= 1000, f"{n} words. Under 1,000."

    def test_result_is_traceable(self, doc):
        body = section(doc("CASE_STUDY.md"), "The result").lower()
        assert "baseline" in body, "Give the baseline."
        assert len(re.findall(r"\d+", body)) >= 3, "Baseline, result and number of cases, at least."

    def test_two_lessons(self, doc):
        assert count_items(section(doc("CASE_STUDY.md"), "What I would do differently")) >= 2, "At least two."

    def test_evidence_links(self, doc):
        links = re.findall(r"\]\([^)]+\)", section(doc("CASE_STUDY.md"), "Evidence"))
        assert len(links) >= 3, f"{len(links)} links. Link the repository, the evals and the handover."


class TestDemo:
    def test_finished(self, doc):
        finished(doc("DEMO.md"), "DEMO.md")

    def test_six_steps(self, doc):
        n = len(re.findall(r"^\s*\d+\.\s+\S", doc("DEMO.md"), flags=re.M))
        assert n >= 6, f"{n} numbered steps. At least six."

    def test_shows_a_failure(self, doc):
        finished(doc("DEMO.md"), "DEMO.md")
        assert re.search(r"fail|wrong|break", doc("DEMO.md"), re.I), "One step shows a failure on purpose."
