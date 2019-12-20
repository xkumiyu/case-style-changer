from .case_style import SpaceSeparated


class TextSplitter(object):
    def __init__(self, case):
        if case == SpaceSeparated:
            self.split = self.space_separated
        else:
            raise

    def space_separated(self, text):
        return text.split(' ')
