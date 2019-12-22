import pytest

from case_style_changer.case_style import CamelCase
from case_style_changer.case_style import CapitalCase
from case_style_changer.case_style import Case
from case_style_changer.case_style import ConstantCase
from case_style_changer.case_style import KebabCase
from case_style_changer.case_style import PascalCase
from case_style_changer.case_style import SentenceCase
from case_style_changer.case_style import SnakeCase


@pytest.mark.parametrize('string, expected', [('camel', CamelCase),
                                              ('pascal', PascalCase),
                                              ('snake', SnakeCase),
                                              ('constant', ConstantCase),
                                              ('kebab', KebabCase),
                                              ('sentence', SentenceCase),
                                              ('capital', CapitalCase)])
def test_from_string(string, expected):
    case = Case.from_string(string)

    assert case == expected


def test_from_string_gives_error():
    with pytest.raises(Exception):
        Case.from_string('')


def test_no_duplicates_in_the_available_list():
    available_list = Case.available_list()

    expected_length = len(available_list)
    length = len(set(available_list))

    assert length == expected_length
