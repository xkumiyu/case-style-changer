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
    parser.add_argument('case_name', choices=Case.available_list())
    parser.add_argument('--text')
    return parser.parse_args(args)


def change_case_style(text, case_name):
    in_text = get_text(text)
    out_case = Case.from_string(case_name)

    guesser = CaseGuesser()
    in_case = guesser.guess(in_text)

    splitter = TextSplitter(in_case)
    words = splitter.split(in_text)

    changer = CaseChanger(out_case)
    out_text = changer.change(words)

    return out_text


def get_text(text):
    if text is None:
        text = input().strip()
    return text
