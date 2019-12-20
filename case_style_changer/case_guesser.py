from .case_style import SpaceSeparated


class CaseGuesser(object):
    def guess(self, text):
        if self.is_space_separated(text):
            return SpaceSeparated
        else:
            raise Exception('Invalid case')

    def is_space_separated(self, text):
        return ' ' in text
