import pytest

from case_style_changer.case_style import HyphenSeparated
from case_style_changer.case_style import NoSeparated
from case_style_changer.case_style import SpaceSeparated
from case_style_changer.case_style import UnderscoreSeparated
from case_style_changer.case_style import UppercaseSeparated
from case_style_changer.text_splitter import TextSplitter


@pytest.mark.parametrize(
    "case, text",
    [
        (SpaceSeparated, "case style changer"),
        (UnderscoreSeparated, "case_style_changer"),
        (HyphenSeparated, "case-style-changer"),
        (UppercaseSeparated, "caseStyleChanger"),
        (UppercaseSeparated, "CaseStyleChanger"),
    ],
)
def test_text_splitter(case, text):
    splitter = TextSplitter(case)
    words = splitter.split(text)

    assert words == ["case", "style", "changer"]


@pytest.mark.parametrize(
    "text, expected", [("", ""), ("case", "case"), ("Case", "Case")]
)
def test_no_split(text, expected):
    case = NoSeparated

    splitter = TextSplitter(case)
    words = splitter.split(text)

    assert words == [expected]


def test_split_text_error():
    case = None

    with pytest.raises(Exception):
        TextSplitter(case)
