#!/usr/bin/python3
import math

x = float(input('digite um numero: '))
print(f'Em seno o valor vai ser {math.sin(math.radians(x)):.2f}')
print(f'Em cosseno o valor vai ser {math.cos(math.radians(x)):.2f}')
print(f'Em tangente o valor vai ser {math.tan(math.radians(x)):.2f}')
print()
y = float(input('digite um numero: '))
y = y*(3.14/180)
print(f'Em seno o valor vai ser {math.sin(y):.2f}')
print(f'Em seno o valor vai ser {math.cos(y):.2f}')
