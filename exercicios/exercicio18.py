#!/usr/bin/python3
import math

x = float(input('digite um numero do cateto oposto: '))
y = float(input('digite um numero do cateto adjacente: '))
h = math.sqrt((x**2) + (y**2))
print('A minha hipotenusa vai ser {:.2f}'.format(h))
print()
# ou
x = float(input('digite um numero do cateto oposto: '))
y = float(input('digite um numero do cateto adjacente: '))
h = math.hypot(x, y)
print('A minha hipotenusa vai ser {:.2f}'.format(h))
