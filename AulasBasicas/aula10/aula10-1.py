#!/usr/bin/python3

usuario = input('digite algo: ')
usuario1 = input('digite algo: ')

print(len(usuario))
# pode ser assim ou...
print(usuario1.__len__())

print(
    f'A soma de carecteres dessas palavras é: {len(usuario) + len(usuario1)}')
