# Case Style Changer

[![PyPi](https://img.shields.io/pypi/v/case-style-changer)](https://pypi.org/project/case-style-changer) [![Python Version](https://img.shields.io/pypi/pyversions/case-style-changer)](https://pypi.org/project/case-style-changer) [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/xkumiyu/case-style-changer/Python%20package)](https://github.com/xkumiyu/case-style-changer/actions) [![codecov](https://img.shields.io/codecov/c/github/xkumiyu/case-style-changer)](https://codecov.io/gh/xkumiyu/case-style-changer) [![Code Climate](https://img.shields.io/codeclimate/maintainability/xkumiyu/case-style-changer)](https://codeclimate.com/github/xkumiyu/case-style-changer) [![License](https://img.shields.io/github/license/xkumiyu/case-style-changer)](LICENSE)

Case Style Changer is a CLI tool that guesses the case of the input string and converts it to another case.

## Installation

``` sh
pip install case-style-changer
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

| Case Name | `CASE_NAME` | Example |
|:--|:--|:--|
| Camel Case | `camel`, `camel_case`, `lower_camel_case`, `lcc` | caseStyleChanger |
| Pascal Case | `pascal`, `pascal_case`, `upper_camel_case`, `ucc` | CaseStyleChanger |
| Snake Case | `snake`, `snake_case`, `lower_snake_case`, `lsc` | case_style_changer |
| Constant Case | `constant`, `constant_case`, `screaming`, `screaming_snake_case`, `upper_snake_case`, `upper_case`, `usc`, `ssc` | CASE_STYLE_CHANGER |
| Kebab Case | `kebab`, `kebab_case`, `chain`, `chain_case` | case-style-changer |
