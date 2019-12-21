from .case_style import (CamelCase, ConstantCase, KebabCase, PascalCase,
                         SnakeCase)


class CaseChanger(object):
    def __init__(self, case):
        to_change = {
            CamelCase: self.camel_case,
            PascalCase: self.pascal_case,
            SnakeCase: self.snake_case,
            ConstantCase: self.constant_case,
            KebabCase: self.kebab_case
        }
        try:
            self.change = to_change[case]
        except KeyError:
            raise Exception('invalid case')

    def camel_case(self, words):
        """ convert text to camel case
        """
        words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
        return ''.join(words)

    def pascal_case(self, words):
        """ convert text to pascal case
        """
        words = [word.capitalize() for word in words]
        return ''.join(words)

    def snake_case(self, words):
        """ convert text to snake case
        """
        words = [word.lower() for word in words]
        return '_'.join(words)

    def constant_case(self, words):
        """ convert text to constant case
        """
        words = [word.upper() for word in words]
        return '_'.join(words)

    def kebab_case(self, words):
        """ convert text to kebab case
        """
        words = [word.lower() for word in words]
        return '-'.join(words)
