from .case_style import (CamelCase, ConstantCase, KebabCase, PascalCase,
                         SnakeCase)


class CaseChanger(object):
    def __init__(self, case):
        if case == CamelCase:
            self.change = self.camel_case
        elif case == PascalCase:
            self.change = self.pascal_case
        elif case == SnakeCase:
            self.change = self.snake_case
        elif case == ConstantCase:
            self.change = self.constant_case
        elif case == KebabCase:
            self.change = self.kebab_case
        else:
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
