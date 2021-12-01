OPERATORS = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y),
             '*': (lambda x, y: x * y), '/': (lambda x, y: x / y),
             '%': (lambda x, y: x % y)}
string = []


def calculation(string):
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
    print(string[0])
    return string[0]


if __name__ == "__main__":
    calculation(['4', '6', '+', '2', '-'])
    print(string[0])