#!/usr/bin/python3

#isnumeric, isdigit, isdecimal

num1 = input('digite um numero: ')
num2 = input('digite um numero: ')

print(num1.isnumeric())
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
else:
    print('error')
