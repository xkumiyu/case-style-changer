# Case Style Changer

[![PyPi][pypi-version]][pypi] [![Python Version][python-version]][pypi] [![GitHub Workflow Status][actions-status]][actions] [![codecov][codecov-status]][codecov] [![Code Climate][codeclimate-status]][codeclimate] [![License][license]][license-file]

Case Style Changer is a CLI tool that guesses the case of the input string and converts it to another case.

## Installation

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

``` sh
pip install case-style-changer
```

For macOS user, you can install and update using [brew](https://brew.sh/):

``` sh
brew tap xkumiyu/homebrew-case-style-changer
brew install case-style-changer
```

## Usage

``` sh
$ csc [--text TEXT] CASE_NAME
```

`CASE_NAME` is the name of the case you want to convert.

### Examples

You can use standard input or arguments.

``` sh
$ echo "case-style-changer" | csc camel
caseStyleChanger
```

``` sh
$ csc snake --text "caseStyleChanger"
case_style_changer
```

### Available case style

The available case styles are:

| Case Name | Case Name Alias | Example |
|:--|:--|:--|
| `camel_case` | `camel`, `lower_camel_case`, `lcc` | caseStyleChanger |
| `pascal_case` | `pascal`, `pascal_case`, `upper_camel_case`, `ucc` | CaseStyleChanger |
| `snake_case` | `snake`, `lower_snake_case`, `lsc` | case_style_changer |
| `constant_case` | `constant`, `constant_case`, `screaming`, `screaming_snake_case`, `upper_snake_case`, `upper_case`, `usc`, `ssc` | CASE_STYLE_CHANGER |
| `kebab_case` | `kebab`, `kebab_case`, `chain`, `chain_case` | case-style-changer |
| `sentence_case` | `sentence` | Case style changer |
| `capital_case` | `capital`,`train`, `train_case` | Case Style Changer |

## Change Log

See [Change Log](CHANGELOG.md).

## Licence

MIT: [LICENCE](LICENSE)

[pypi]: https://pypi.org/project/case-style-changer
[pypi-version]: https://img.shields.io/pypi/v/case-style-changer
[python-version]: https://img.shields.io/pypi/pyversions/case-style-changer
[actions]: https://github.com/xkumiyu/case-style-changer/actions
[actions-status]: https://img.shields.io/github/workflow/status/xkumiyu/case-style-changer/Python%20package
[codecov]: https://codecov.io/gh/xkumiyu/case-style-changer
[codecov-status]: https://img.shields.io/codecov/c/github/xkumiyu/case-style-changer
[codeclimate]: https://img.shields.io/codeclimate/maintainability/xkumiyu/case-style-changer
[codeclimate-status]: https://img.shields.io/codeclimate/maintainability/xkumiyu/case-style-changer
[license]: https://img.shields.io/github/license/xkumiyu/case-style-changer
[license-file]: https://github.com/xkumiyu/case-style-changer/blob/master/LICENSE
