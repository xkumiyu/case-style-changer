import pytest

from case_style_changer.case_changer import CaseChanger
from case_style_changer.case_style import CamelCase


def test_camel_case():
    words = ['case', 'style', 'changer']
    case = CamelCase

    changer = CaseChanger(case)
    text = changer.change(words)

    assert text == 'caseStyleChanger'


def test_case_error():
    case = None

    with pytest.raises(Exception):
        CaseChanger(case)
