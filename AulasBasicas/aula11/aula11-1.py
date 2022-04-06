#!/usr/bin/python3

import re


def is_float(val):
    if isinstance(val, float):
        return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val):
        return True

    return False


def is_int(val):
    if isinstance(val, int):
        return True
    if re.search(r'^\-{,1}[0-9]+$', val):
        return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)

# codigo que o professor fez pra da certo


num1 = input('digite um numero: ')
num2 = input('digite um numero: ')

if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
else:
    print('error')
