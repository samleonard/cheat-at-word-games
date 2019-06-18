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

    parser = argparse.ArgumentParser(description='cheat at word games', formatter_class=argparse.RawTextHelpFormatter)
    subparsers = parser.add_subparsers(dest='game', required=True,
                                       help='sb: Spelling Bee\n'
                                            'lb: Letter Boxed')

    spelling_bee = subparsers.add_parser('sb', description='cheat at Spelling Bee')
    spelling_bee.add_argument('letters', help='the letters in the puzzle, with or without the center letter')
    spelling_bee.add_argument('center', help='the center letter')
    spelling_bee.set_defaults(func=solve_spelling_bee)

    letter_boxed = subparsers.add_parser('lb', description='cheat at Letter Boxed')
    letter_boxed.add_argument('side', nargs=4, help='one side of the box')
    letter_boxed.set_defaults(func=solve_letter_boxed)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
