#!/usr/bin/python3
'''
For in em python
Iterando strings com for
Funçao range(start = 0, stop, step = 1)
'''
texto = 'pyhton'
nova_string = ''

for letra in texto:
    print(letra)

print()

for n, letra in enumerate(texto):
    print(n, letra)

print()

for n in range(10):
    print(n)

print()

for n in range(20, 10, -1):
    print(n)

print()

for n in range(0, 10, 1):
    print(n)

print()

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
