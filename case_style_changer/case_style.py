class Case(object):
    @staticmethod
    def from_string(case_name):
        if case_name == 'camel_case':
            return CamelCase
        elif case_name == 'pascal_case':
            return PascalCase
        elif case_name == 'snake_case':
            return SnakeCase
        elif case_name == 'constant_case':
            return ConstantCase
        elif case_name == 'kebab_case':
            return KebabCase
        else:
            raise Exception('invalid case name')

    @staticmethod
    def available_list():
        return [
            'camel_case', 'pascal_case', 'snake_case', 'constant_case',
            'kebab_case'
        ]


class SpaceSeparated(object):
    pass


class UnderscoreSeparated(object):
    pass


class HyphenSeparated(object):
    pass


class UppercaseSeparated(object):
    pass


class CapitalCase(SpaceSeparated):
    """ capital case
    Example:
        Case style changer
    """
    pass


class CamelCase(UppercaseSeparated):
    """ camel case
    Example:
        caseStyleChanger
    """
    pass


class PascalCase(UppercaseSeparated):
    """ pascal case
    Example:
        CaseStyleChanger
    """


class SnakeCase(UnderscoreSeparated):
    """ snake case
    Example:
        case_style_changer
    """


class ConstantCase(UnderscoreSeparated):
    """ constant case
    Example:
        CASE_STYLE_CHANGER
    """


class KebabCase(HyphenSeparated):
    """ kebab case
    Example:
        case-style-changer
    """
