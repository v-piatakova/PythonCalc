# !/usr/bin/env python
# coding: utf-8
import argparse
import setuptools

from parse import parse_module
from OPZ import OPZ_module
from calculation import calculation_module

formula_string = input("Enter string of numbers")
parsed_formula = []
a = []
string = []
operations = []
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

calculation_module.calculation(OPZ_module.OPZ(parse_module.parse(formula_string)))