from Calculator import OPERATORS

string = []


def calculation(line):
    i = 0
    while i < len(string):
        char = string[i]

        if char in OPERATORS:
            res = OPERATORS[char](int(string[i - 2]), int(string[i - 1]))
            string.pop(i)
            string.pop(i - 1)
            string[i - 2] = str(res)

            i -= 2
        else:
            i += 1

    return string[0]
