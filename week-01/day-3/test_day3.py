"""Week 1, Day 3 - the requirements.

Run me:  pytest week-01/day-3 -v
"""

import re

from doccheck import count_items, finished, section, words


def requirements(text):
    body = section(text, "Requirements")
    return [r for r in re.split(r"\n### ", "\n" + body)[1:] if r.strip()]


class TestRequirements:
    def test_finished(self, doc):
        finished(doc("REQUIREMENTS.md"), "REQUIREMENTS.md")

    def test_users(self, doc):
        assert words(section(doc("REQUIREMENTS.md"), "Users")) >= 10, "Say who uses it, by role."

    def test_six(self, doc):
        n = len(requirements(doc("REQUIREMENTS.md")))
        assert n >= 6, f"{n} requirements. At least six."

    def test_each_is_numbered(self, doc):
        finished(doc("REQUIREMENTS.md"), "REQUIREMENTS.md")
        for r in requirements(doc("REQUIREMENTS.md")):
            assert re.match(r"R\d+\b", r), f"'### {r.splitlines()[0]}' needs an ID like R1."

    def test_each_has_priority_and_test(self, doc):
        for r in requirements(doc("REQUIREMENTS.md")):
            name = r.splitlines()[0]
            assert re.search(r"Priority:\s*(Must|Should|Could)\b", r), f"{name} has no Must/Should/Could priority."
            m = re.search(r"Accepted when:\s*(.+)", r)
            assert m and len(m.group(1).split()) >= 5, f"{name} has no 'Accepted when:' check worth the name."

    def test_not_everything_is_a_must(self, doc):
        finished(doc("REQUIREMENTS.md"), "REQUIREMENTS.md")
        reqs = requirements(doc("REQUIREMENTS.md"))
        musts = sum(1 for r in reqs if re.search(r"Priority:\s*Must\b", r))
        assert musts <= 0.6 * len(reqs), f"{musts} of {len(reqs)} are Must. Decide what can slip."

    def test_constraints(self, doc):
        assert count_items(section(doc("REQUIREMENTS.md"), "Constraints")) >= 3, "At least three constraints."

    def test_out_of_scope(self, doc):
        assert count_items(section(doc("REQUIREMENTS.md"), "Out of scope")) >= 3, "At least three things out of scope."

    def test_open_questions_have_owners(self, doc):
        body = section(doc("REQUIREMENTS.md"), "Open questions")
        assert count_items(body) >= 2, "At least two open questions."
        assert body.count("Owner:") >= 2, "Every open question needs an 'Owner:'."
