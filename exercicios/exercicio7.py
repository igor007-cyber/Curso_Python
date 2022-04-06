#!/usr/bin/python3

altura = int(input('DIGITE UM NUMERO: '))
num = 1

while num <= altura:
    num1 = num
    print("*")
    if num == altura:
        break
    num += 1
    while num1 >= 0:
        print('*', end='')
        num1 -= 1
    print()
