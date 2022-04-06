#!/usr/bin/python3

# Tabuada dos numeros

num = float(input('Digite um numero: '))

print('\n---------------------------')

for x in range(0, 11):
    print(f'{num} x {x} = {num*x}')
print('---------------------------')
