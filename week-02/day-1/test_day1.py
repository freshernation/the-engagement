"""Week 2, Day 1 - the first slice.

Run me:  pytest week-02/day-1 -v
"""

import json
from pathlib import Path

from doccheck import count_items, finished, has_number, section, words

HERE = Path(__file__).parent


def cases():
    lines = [l for l in (HERE / "evals.jsonl").read_text().splitlines() if l.strip()]
    out = []
    for n, line in enumerate(lines, 1):
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError as e:
            raise AssertionError(f"evals.jsonl line {n} is not valid JSON: {e}")
    return out


class TestCases:
    def test_twenty(self):
        n = len(cases())
        assert n >= 20, f"{n} cases. At least twenty, from the customer's data."

    def test_fields(self):
        assert cases(), "evals.jsonl is empty."
        for c in cases():
            for field in ("id", "input", "expected", "source"):
                assert str(c.get(field, "")).strip(), f"Case {c.get('id', '?')} has no '{field}'."

    def test_unique_ids(self):
        assert cases(), "evals.jsonl is empty."
        ids = [c["id"] for c in cases()]
        assert len(ids) == len(set(ids)), "Two cases share an id."

    def test_sources_are_spread(self):
        records = {str(c["source"]).strip() for c in cases()}
        assert len(records) >= 10, f"Only {len(records)} distinct sources. Twenty cases from three records is three cases."


class TestEvals:
    def test_finished(self, doc):
        finished(doc("EVALS.md"), "EVALS.md")

    def test_measured(self, doc):
        assert words(section(doc("EVALS.md"), "What is measured")) >= 30, "Say what a case is and how it is scored."

    def test_baseline_and_slice_have_numbers(self, doc):
        text = doc("EVALS.md")
        assert has_number(section(text, "Baseline")), "The baseline needs a number, or a stated reason it cannot have one."
        assert has_number(section(text, "First slice")), "Today's score needs a number."

    def test_failures_named(self, doc):
        assert count_items(section(doc("EVALS.md"), "What fails")) >= 3, "Name at least three failing cases and why."

    def test_customer_told(self, doc):
        assert words(section(doc("EVALS.md"), "Sent to the customer")) >= 20, "Tell the customer tonight. Paste what you sent."
