import sys


# might not work if there are duplicate letters
def check_word(sides, line):
    prev = -1
    for letter in line.strip():
        valid = False
        for i in range(len(sides)):
            # can't reuse side consecutively
            if i == prev:
                continue
            if letter in sides[i]:
                prev = i
                valid = True
                break
        if not valid:
            return False
    return True


def main():
    sides = ['PDS', 'LEI', 'CMO', 'RTU']
    if len(sys.argv) == 5:
        sides = sys.argv[1:]

    with open('sowpods-letter-boxed.txt') as infile:
        lines = infile.readlines()

    # make a list of valid words
    lines = [line.strip() for line in lines if check_word(sides, line)]

    index = {}

    # index all words by first letter
    for line in lines:
        index.setdefault(line[0], []).append(line)

    letters = ''.join(sides)

    # find all 1 word solutions
    singles = set()
    for line in lines:
        if all(letter in line for letter in letters):
            singles.add(line)

    # find all 2 word solutions
    answers = []
    for line in lines:
        if line in singles:
            continue

        unseen = [letter for letter in letters if letter not in line]

        for word in index[line[-1]]:
            if word in singles:
                continue

            if all(letter in word for letter in unseen):
                answers.append((line, word))

    shortest = min(len(''.join(answer)) for answer in answers)
    shorties = []
    for answer in answers:
        if len(''.join(answer)) == shortest:
            shorties.append(answer)

    for answer in answers:
        print(answer)
    print('\n\n\n************TERSEST************')
    for answer in shorties:
        print(answer)
    print('\n\n\n************SINGLES************')
    for answer in singles:
        print(answer)


if __name__ == '__main__':
    main()
