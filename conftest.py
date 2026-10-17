"""Test harness for The Engagement.

Every deliverable in this course is a document. The tests check that a document
is finished - sections present, numbers given, limits kept - and nothing more.
Whether it is good is Friday's question.

    from doccheck import section, count_items

    def test_something(doc):
        text = doc("PROBLEM.md")                 # the file next to the test
        body = section(text, "Non-goals")        # one "## " section
        assert count_items(body) >= 3
"""

from pathlib import Path

import pytest


@pytest.fixture
def doc(request):
    """Read a document that lives next to the test file."""
    here = Path(request.fspath).parent

    def _doc(name):
        path = here / name
        if not path.exists():
            pytest.fail(f"{name} does not exist yet in {here.name}/. Create it, then run the tests again.")
        return path.read_text()

    return _doc
