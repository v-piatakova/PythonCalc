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

a = []
string = []
operations = []


def OPZ(a):
    count = 0
    for s in a:
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
    return string


if __name__ == "__main__":
    OPZ(['4', '+', '6', '-', '2'])
    print(string)