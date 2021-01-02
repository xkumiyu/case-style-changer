import pytest

from case_style_changer.case_changer import CaseChanger
from case_style_changer.case_style import CamelCase
from case_style_changer.case_style import CapitalCase
from case_style_changer.case_style import ConstantCase
from case_style_changer.case_style import KebabCase
from case_style_changer.case_style import PascalCase
from case_style_changer.case_style import SentenceCase
from case_style_changer.case_style import SnakeCase


@pytest.mark.parametrize(
    "case, expected",
    [
        (CamelCase, "caseStyleChanger"),
        (PascalCase, "CaseStyleChanger"),
        (SnakeCase, "case_style_changer"),
        (ConstantCase, "CASE_STYLE_CHANGER"),
        (KebabCase, "case-style-changer"),
        (SentenceCase, "Case style changer"),
        (CapitalCase, "Case Style Changer"),
    ],
)
def test_case_changer(case, expected):
    words = ["case", "style", "changer"]

    changer = CaseChanger(case)
    text = changer.change(words)

    assert text == expected


def test_case_error():
    case = None

    with pytest.raises(Exception):
        CaseChanger(case)
