from .case_style import CamelCase


class CaseChanger(object):
    def __init__(self, case):
        if case == CamelCase:
            self.change = self.camel_case
        else:
            raise

    def camel_case(self, words):
        """ convert text to camel case
        """
        words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
        return ''.join(words)
