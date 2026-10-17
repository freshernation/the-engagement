"""Checks shared by every test: is the document finished?

    from doccheck import section, words, count_items, has_number, finished
"""

import re


def section(text, heading):
    """The body of one '## heading' section, or '' if it is missing."""
    marker = f"## {heading}"
    if marker not in text:
        return ""
    return text.split(marker, 1)[1].split("\n## ")[0]


def words(text):
    return len(re.sub(r"<!--.*?-->", "", text, flags=re.S).split())


def count_items(text):
    """Bullet or numbered list items."""
    return len(re.findall(r"^\s*(?:[-*]|\d+\.)\s+\S", text, flags=re.M))


def has_number(text):
    return re.search(r"\d", text) is not None


def finished(text, name):
    assert "<!--" not in text, f"Delete the instructions comment in {name}."
    assert "TODO" not in text, f"{name} still has a TODO in it."
