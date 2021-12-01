# !/usr/bin/env python
# coding: utf-8
import os
import parse_module
import OPZ_module

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

parsed_formula = []
formula_string = input("Enter string of numbers")
a = []
string = []
operations = []


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


calculation(OPZ_module.OPZ(parse_module.parse(formula_string)))
