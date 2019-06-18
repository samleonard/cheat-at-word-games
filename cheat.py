import argparse
import os
import sys

import cheat_letter_boxed
import cheat_spelling_bee


def solve_spelling_bee(args):
    cheat_spelling_bee.solve(args.letters, args.center)


def solve_letter_boxed(args):
    cheat_letter_boxed.solve(args.side)


def main():
    os.chdir(sys.path[0])

    parser = argparse.ArgumentParser(description='Cheat at word games')
    subparsers = parser.add_subparsers(dest='command', required=True)

    spelling_bee = subparsers.add_parser('sb', description='cheat at Spelling Bee')
    spelling_bee.add_argument('letters')
    spelling_bee.add_argument('center')
    spelling_bee.set_defaults(func=solve_spelling_bee)

    letter_boxed = subparsers.add_parser('lb', description='cheat at Letter Boxed')
    letter_boxed.add_argument('side', nargs=4)
    letter_boxed.set_defaults(func=solve_letter_boxed)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
