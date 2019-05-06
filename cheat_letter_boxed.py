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

    lines = [line.strip() for line in lines if check_word(sides, line)]

    index = {}

    for line in lines:
        index.setdefault(line[0], []).append(line)

    letters = ''.join(sides)

    for line in lines:
        unseen = [letter for letter in letters if letter not in line]
        for word in index[line[-1]]:
            valid = True
            for letter in unseen:
                if letter not in word:
                    valid = False
            if valid:
                print(line, word)


if __name__ == '__main__':
    main()
