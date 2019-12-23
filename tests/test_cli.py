import pytest

from case_style_changer.cli import change_case_style
from case_style_changer.cli import parse_args


@pytest.mark.parametrize(
    'args, expected',
    [(['camel_case'], {
        'case_name': 'camel_case',
        'text': None
    }),
     (['camel_case', '--text', 'case style changer'], {
         'case_name': 'camel_case',
         'text': 'case style changer'
     })])
def test_parser(args, expected):
    args = parse_args(args)

    assert args.case_name == expected['case_name']
    assert args.text == expected['text']


@pytest.mark.parametrize(
    'text, case_name, expected',
    [('case', 'camel', 'case'),
     ('case style changer', 'camel_case', 'caseStyleChanger'),
     ('case style\nchanger', 'lcc', 'caseStyle\nchanger')])
def test_change_case_style(text, case_name, expected):
    result = change_case_style(text, case_name)

    assert result == expected
