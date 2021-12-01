OPERATORS = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y),
             '*': (lambda x, y: x * y), '/': (lambda x, y: x / y),
             '%': (lambda x, y: x % y)}
parsed_formula = []


def parse(string):
    number = ''
    for s in string:
        if s in '1234567890.':
            number += s
        elif number:
            parsed_formula.append(number)
            number = ''
        if s in OPERATORS or s in "()":
            parsed_formula.append(s)
    if number:
        parsed_formula.append(number)
    print(parsed_formula)
    return parsed_formula


if __name__ == "__main__":
    parse("4+6-2")
    print(parsed_formula)
