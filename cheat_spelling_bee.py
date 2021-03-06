def check_line(line, letters, center):
    """check whether word is valid with these letters"""
    if center not in line:
        return False
    for letter in line:
        if letter not in letters:
            return False
    return True


def check_bingo(line, letters):
    for letter in letters:
        if letter not in line:
            return False
    return True


def solve(letters, center):
    letters = letters.upper()
    center = center.upper()
    if center not in letters:
        letters += center

    with open('sowpods-spelling-bee.txt') as infile:
        lines = infile.readlines()

    bingos = []
    for line in lines:
        line = line.strip()
        if check_line(line, letters, center):
            print(line)
            if check_bingo(line, letters):
                bingos.append(line)
    print("bingos:", bingos)
