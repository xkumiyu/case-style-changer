import argparse


class CaseGuesser(object):
    def guess(self, text):
        if self.is_space_separated(text):
            return 'space_separated'
        else:
            raise Exception('Invalid case')

    def is_space_separated(self, text):
        return ' ' in text


def split_text(text, case):
    """ split text into words
    """

    if case == 'space_separated':
        return text.split(' ')
    else:
        raise


def camel_case(words):
    """ convert text to camel case
    """
    words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    return ''.join(words)


def change_case(text):
    guesser = CaseGuesser()
    case = guesser.guess(text)

    words = split_text(text, case)
    return camel_case(words)


def main():
    parser = argparse.ArgumentParser(description='Change case style.')
    parser.add_argument('text')
    args = parser.parse_args()

    print(change_case(args.text))
