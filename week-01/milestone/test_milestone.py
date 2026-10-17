"""Week 1 Milestone - the proposal.

Run me:  pytest week-01/milestone -v
"""

import re

import pytest

from doccheck import count_items, finished, has_number, section, words

HEADINGS = ["Summary", "The problem", "What we will build", "What we will not build",
            "How we will know it worked", "Timeline and cost", "What we need from you", "Risks"]

# Names a decision maker should not have to know. Extend it for your client.
JARGON = ["llm", "gpt", "claude", "openai", "langgraph", "langchain", "rag", "embedding",
          "vector", "fastapi", "docker", "kubernetes", "api", "pipeline", "agentic", "prompt"]


class TestProposal:
    def test_finished(self, doc):
        finished(doc("PROPOSAL.md"), "PROPOSAL.md")

    @pytest.mark.parametrize("heading", HEADINGS)
    def test_sections(self, doc, heading):
        assert words(section(doc("PROPOSAL.md"), heading)) >= 10, f"'{heading}' is missing or thin."

    def test_summary_comes_first(self, doc):
        finished(doc("PROPOSAL.md"), "PROPOSAL.md")
        first = re.search(r"^## (.+)$", doc("PROPOSAL.md"), flags=re.M)
        assert first and first.group(1).strip() == "Summary", "The summary is the first section."

    def test_summary_is_short_and_has_a_number(self, doc):
        body = section(doc("PROPOSAL.md"), "Summary")
        assert words(body) <= 100, f"Summary is {words(body)} words. Under 100."
        assert has_number(body), "The summary needs a number: the cost, the target, or both."

    def test_one_page(self, doc):
        finished(doc("PROPOSAL.md"), "PROPOSAL.md")
        n = words(doc("PROPOSAL.md"))
        assert n <= 800, f"{n} words. Under 800: the decision maker reads one page."

    def test_no_jargon(self, doc):
        finished(doc("PROPOSAL.md"), "PROPOSAL.md")
        text = doc("PROPOSAL.md").lower()
        found = [j for j in JARGON if re.search(rf"\b{j}\b", text)]
        assert not found, f"Words the decision maker should not need: {found}"

    def test_non_goals(self, doc):
        assert count_items(section(doc("PROPOSAL.md"), "What we will not build")) >= 3, "At least three non-goals."

    def test_what_we_need(self, doc):
        assert count_items(section(doc("PROPOSAL.md"), "What we need from you")) >= 3, "At least three things you need."

    def test_cost_is_a_range_per_month(self, doc):
        body = section(doc("PROPOSAL.md"), "Timeline and cost")
        assert re.search(r"\d+\s*(?:-|–|to)\s*\d+", body), "Timeline and cost as a range."
        assert re.search(r"month", body, re.I), "Say what it costs per month to run."
