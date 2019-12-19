import argparse


class CSCArgumentParser(argparse.ArgumentParser):
    pass


def main():
    parser = CSCArgumentParser(description='Change case style.')
    parser.parse_args()
