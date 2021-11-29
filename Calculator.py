# !/usr/bin/env python
# coding: utf-8
import os

OPERATORS = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y),
             '*': (lambda x, y: x * y), '/': (lambda x, y: x / y),
             '%': (lambda x, y: x % y)}

PRIORITY = {
    '/': 4,
    '*': 4,
    '%': 4,
    '+': 3,
    '-': 3,
    '(': 2,
    ')': 2,
}

operations = []
string = []
parsed_formula = []
formula_string = input("Enter string of numbers")


def parse(formula_string):
    number = ''
    for s in formula_string:
        if s in '1234567890.':
            number += s
        elif number:
            parsed_formula.append(number)
            number = ''
        if s in OPERATORS or s in "()":
            parsed_formula.append(s)
    if number:
        parsed_formula.append(number)


a = []


def OPZ(a):
    count = 0
    for s in parsed_formula:
        if s.isdigit():
            string.append(s)
        elif s == "(":
            operations.append(s)
            count += 1
        elif s == "(":
            count -= 1
        if count < 0:
            print('error')
            break
        elif s in OPERATORS or s == ")":
            if s == ")":
                count -= 1
            if len(operations) > 0:
                prev = operations[-1]
                prevPriority = PRIORITY[prev]
                currentPriority = PRIORITY[s]

                if currentPriority <= prevPriority:
                    while operations and currentPriority <= PRIORITY[operations[-1]]:
                        last = operations.pop()

                        if last == "(":
                            break
                        else:
                            string.append(last)

                    if currentPriority > 1:
                        operations.append(s)
                else:
                    operations.append(s)
            else:
                operations.append(s)
    while operations:
        string.append(operations[-1])
        operations.pop()
    print(string)


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

    print(string[0])


calculation(OPZ(parse(formula_string)))
