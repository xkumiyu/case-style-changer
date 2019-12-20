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
            raise

    @staticmethod
    def available_list():
        return [
            'camel_case', 'pascal_case', 'snake_case', 'constant_case',
            'kebab_case'
        ]


class SpaceSeparated(object):
    """ space separated
    Example:
        case style changer
    """
    pass


class CapitalCase(object):
    """ capital case
    Example:
        Case style changer
    """
    pass


class CamelCase(object):
    """ camel case
    Example:
        caseStyleChanger
    """
    pass


class PascalCase(object):
    """ pascal case
    Example:
        CaseStyleChanger
    """


class SnakeCase(object):
    """ snake case
    Example:
        case_style_changer
    """


class ConstantCase(object):
    """ constant case
    Example:
        CASE_STYLE_CHANGER
    """


class KebabCase(object):
    """ kebab case
    Example:
        case-style-changer
    """
