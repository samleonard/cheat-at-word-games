def create_spelling_bee_file():
    with open('sowpods.txt') as infile:
        lines = infile.readlines()
    with open('sowpods-spelling-bee.txt', 'w') as outfile:
        for line in lines:
            if len(line.strip()) >= 4:
                outfile.write(line)


def create_crossroads_file():
    with open('sowpods.txt') as infile:
        lines = infile.readlines()
    lines = [line for line in lines if len(line.strip()) >= 3]

    def crossroads_filter(line):
        if len(line.strip()) < 3:
            return False

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                return False

        return True
    lines = filter(no_double_letters, lines)

    with open('sowpods-crossroads.txt', 'w') as outfile:
        outfile.writelines(lines)


if __name__ == '__main__':
    create_crossroads_file()
