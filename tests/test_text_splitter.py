import pytest

from case_style_changer.case_style import SpaceSeparated
from case_style_changer.text_splitter import TextSplitter


def test_split_text():
    text = 'case style changer'
    case = SpaceSeparated

    splitter = TextSplitter(case)
    words = splitter.split(text)

    assert words == ['case', 'style', 'changer']


def test_split_text_error():
    case = None

    with pytest.raises(Exception):
        TextSplitter(case)
