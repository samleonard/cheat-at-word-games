def create_spelling_bee_file():
    def spelling_bee_filter(line):
        if len(line.strip()) < 4:
            return False
        return True

    with open('sowpods.txt') as infile:
        lines = infile.readlines()
    with open('sowpods-spelling-bee.txt', 'w') as outfile:
        outfile.writelines(filter(spelling_bee_filter, lines))


def create_letter_boxed_file():
    def letter_boxed_filter(line):
        if len(line.strip()) < 3:
            return False

        for i in range(1, len(line)):
            if line[i] == line[i-1]:
                return False

        return True

    with open('sowpods.txt') as infile:
        lines = infile.readlines()
    with open('sowpods-letter-boxed.txt', 'w') as outfile:
        outfile.writelines(filter(letter_boxed_filter, lines))


if __name__ == '__main__':
    create_letter_boxed_file()
