import pytest

from case_style_changer.case_guesser import CaseGuesser
from case_style_changer.case_style import HyphenSeparated
from case_style_changer.case_style import NoSeparated
from case_style_changer.case_style import SpaceSeparated
from case_style_changer.case_style import UnderscoreSeparated
from case_style_changer.case_style import UppercaseSeparated


@pytest.mark.parametrize(
    "text, expected",
    [
        ("", NoSeparated),
        ("case", NoSeparated),
        ("Case", NoSeparated),
        ("case style changer", SpaceSeparated),
        ("case_style_changer", UnderscoreSeparated),
        ("case-style-changer", HyphenSeparated),
        ("caseStyleChanger", UppercaseSeparated),
        ("CaseStyleChanger", UppercaseSeparated),
    ],
)
def test_guess(text, expected):
    guesser = CaseGuesser()
    case = guesser.guess(text)

    assert case == expected
