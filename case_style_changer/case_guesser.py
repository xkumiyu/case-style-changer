import re

from .case_style import (HyphenSeparated, SpaceSeparated, UnderscoreSeparated,
                         UppercaseSeparated)


class CaseGuesser(object):
    def guess(self, text):
        # TODO: for multiple matches
        if self.is_space_separated(text):
            return SpaceSeparated
        elif self.is_underscore_separated(text):
            return UnderscoreSeparated
        elif self.is_hyphen_separated(text):
            return HyphenSeparated
        elif self.is_uppercase_separated(text):
            return UppercaseSeparated
        else:
            raise Exception('invalid case')

    def is_space_separated(self, text):
        return ' ' in text

    def is_underscore_separated(self, text):
        return '_' in text

    def is_hyphen_separated(self, text):
        return '-' in text

    def is_uppercase_separated(self, text):
        result = re.search('[A-Z]', text)
        return bool(result)
