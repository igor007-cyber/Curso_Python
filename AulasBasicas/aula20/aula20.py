#!/usr/bin/python3
'''
For / Else em python
'''
variavel = ['igor', 'sara', 'gabi']

for valor in variavel:
    print(valor)

comeca_com_j = False

print()

for valor in variavel:
    print(valor)
    if valor.lower().startswith('J'):
        comeca_com_j = True
else:
    print('nao começa com j')

# startswith -> vai mostrar se ela começa com uma determinada letra
# lower -> como colocar pra minusculo a letra
