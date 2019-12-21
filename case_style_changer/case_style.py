class Case(object):
    @staticmethod
    def from_string(case_name):
        cases = [CamelCase, PascalCase, SnakeCase, ConstantCase, KebabCase]

        to_case = {}
        for case in cases:
            to_case.update({flag: case for flag in case.flags()})

        try:
            return to_case[case_name]
        except KeyError:
            raise Exception('invalid case name')

    @staticmethod
    def available_list():
        return CamelCase.flags() + PascalCase.flags() + SnakeCase.flags(
        ) + ConstantCase.flags() + KebabCase.flags()


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
    @staticmethod
    def flags():
        return ['camel', 'camel_case', 'lower_camel_case', 'lcc']


class PascalCase(UppercaseSeparated):
    """ pascal case
    Example:
        CaseStyleChanger
    """
    @staticmethod
    def flags():
        return ['pascal', 'pascal_case', 'upper_camel_case', 'ucc']


class SnakeCase(UnderscoreSeparated):
    """ snake case
    Example:
        case_style_changer
    """
    @staticmethod
    def flags():
        return ['snake', 'snake_case', 'lower_snake_case', 'lsc']


class ConstantCase(UnderscoreSeparated):
    """ constant case
    Example:
        CASE_STYLE_CHANGER
    """
    @staticmethod
    def flags():
        return [
            'constant', 'constant_case', 'screaming', 'screaming_snake_case',
            'upper_snake_case', 'upper_case', 'usc', 'ssc'
        ]


class KebabCase(HyphenSeparated):
    """ kebab case
    Example:
        case-style-changer
    """
    @staticmethod
    def flags():
        return ['kebab', 'kebab_case', 'chain', 'chain_case']
