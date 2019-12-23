import argparse
import sys

from .case_changer import CaseChanger
from .case_guesser import CaseGuesser
from .case_style import Case
from .text_splitter import TextSplitter


def main():
    args = parse_args(sys.argv[1:])
    print(change_case_style(args.text, args.case_name))


def parse_args(args):
    parser = argparse.ArgumentParser(description='Change case style.')
    parser.add_argument('case_name',
                        choices=Case.available_list(),
                        help='the name of the case to convert')
    parser.add_argument('-t', '--text', help='the string to convert')
    return parser.parse_args(args)


def change_case_style(text, case_name):
    in_text = get_text(text)
    out_case = Case.from_string(case_name)

    guesser = CaseGuesser()
    result = []
    for in_string in in_text:
        in_case = guesser.guess(in_string)

        splitter = TextSplitter(in_case)
        words = splitter.split(in_string)

        changer = CaseChanger(out_case)
        out_string = changer.change(words)

        result.append(out_string)

    if len(result) == 1:
        out_text = result[0]
    else:
        out_text = '\n'.join(result)

    return out_text


def get_text(text) -> list:
    if text is None:
        text = sys.stdin.readlines()
        text = [line.rstrip() for line in text]
    else:
        text = text.encode('utf-8').decode('unicode-escape')
        text = text.splitlines()
    return text
