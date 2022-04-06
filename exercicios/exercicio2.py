#!/usr/bin/python3

num1 = input('digite um numero: ')

if num1.isdigit():
    num1 = int(num1)
    if num1 % 2 == 0:
        print('Esse numero é par')
    else:
        print('Esse numero é impar')
else:
    print('Error')
