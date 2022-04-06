#!/usr/bin/python3

num1 = input('digite um numero: ')
num2 = input('digite um numero: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
    print('error')
"""
o try -> ele vai tentar compilar o seu codigo, porem se nao der certo ele vai
compilar no que está no except;

"""
