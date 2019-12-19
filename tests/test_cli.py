from case_style_changer.cli import (CaseGuesser, camel_case, change_case,
                                    split_text)


def test_camel_case():
    words = ['case', 'style', 'changer']
    text = camel_case(words)

    assert text == 'caseStyleChanger'


def test_split_text():
    text = 'case style changer'
    case = 'space_separated'
    words = split_text(text, case)

    assert words == ['case', 'style', 'changer']


def test_guess():
    text = 'case style changer'
    guesser = CaseGuesser()
    case = guesser.guess(text)

    assert case == 'space_separated'


def test_change_case():
    text = 'case style changer'
    changed_text = change_case(text)

    assert changed_text == 'caseStyleChanger'
