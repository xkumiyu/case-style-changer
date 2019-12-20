import pytest

from case_style_changer.cli import parse_args, change_case_style


@pytest.mark.parametrize('args, expected',
                         [(['camel_case'], {
                             'case': 'camel_case',
                             'text': None
                         }),
                          (['camel_case', '--text', 'case style changer'], {
                              'case': 'camel_case',
                              'text': 'case style changer'
                          })])
def test_parser(args, expected):
    parser = parse_args(args)

    assert parser.case == expected['case']
    assert parser.text == expected['text']


def test_change_case_style():
    result = change_case_style('case style changer', 'camel_case')

    assert result == 'caseStyleChanger'
