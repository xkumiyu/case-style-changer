# Case Style Changer

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/xkumiyu/case-style-changer/Python%20package)](https://github.com/xkumiyu/case-style-changer/actions) [![codecov](https://img.shields.io/codecov/c/github/xkumiyu/case-style-changer)](https://codecov.io/gh/xkumiyu/case-style-changer) [![Code Climate](https://img.shields.io/codeclimate/maintainability/xkumiyu/case-style-changer)](https://codeclimate.com/github/xkumiyu/case-style-changer) [![License](https://img.shields.io/github/license/xkumiyu/case-style-changer)](LICENSE)

## Installation

``` sh
pip install case-style-changer
```

## Usage

``` sh
$ echo "case style changer" | csc camel_case
caseStyleChanger
```

``` sh
$ csc snake_case --text "case style changer"
case_style_changer
```

### Available case style

| Case Name | Example |
|:--:|:--:|
| `camel_case` | caseStyleChanger |
| `pascal_case` | CaseStyleChanger |
| `snake_case` | case_style_changer |
| `constant_case` | CASE_STYLE_CHANGER |
| `kebab_case` | case-style-changer |
