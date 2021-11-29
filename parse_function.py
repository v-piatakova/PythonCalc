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
    return parsed_formula


