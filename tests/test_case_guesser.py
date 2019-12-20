import pytest

from case_style_changer.case_guesser import CaseGuesser
from case_style_changer.case_style import SpaceSeparated


def test_guess():
    text = 'case style changer'

    guesser = CaseGuesser()
    case = guesser.guess(text)

    assert case == SpaceSeparated


def test_guess_error():
    text = ''

    guesser = CaseGuesser()
    with pytest.raises(Exception):
        guesser.guess(text)
