import re

from .case_style import HyphenSeparated
from .case_style import NoSeparated
from .case_style import SpaceSeparated
from .case_style import UnderscoreSeparated
from .case_style import UppercaseSeparated


class TextSplitter(object):
    def __init__(self, case):
        if case == SpaceSeparated:
            self.split = self.space_separated
        elif case == UnderscoreSeparated:
            self.split = self.underscore_separated
        elif case == HyphenSeparated:
            self.split = self.hyphen_separated
        elif case == UppercaseSeparated:
            self.split = self.uppercase_separated
        elif case == NoSeparated:
            self.split = self.no_separated
        else:
            raise Exception('invalid case')

    def space_separated(self, text):
        return text.split(' ')

    def underscore_separated(self, text):
        return text.split('_')

    def hyphen_separated(self, text):
        return text.split('-')

    def uppercase_separated(self, text):
        first_words = [''] + re.findall('[A-Z]', text)
        remaining_words = re.split('[A-Z]', text)

        words = []
        for first_word, remaining_word in zip(first_words, remaining_words):
            word = first_word + remaining_word
            if word != '':
                words.append(word.lower())

        return words

    def no_separated(self, text):
        return [text]
