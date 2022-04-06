#!/usr/bin/python3
'''
while / else

contadores e acumuladores
'''

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador += contador
    contador += 1
else:  # se a expressao for falsa do while, ele execulta o else
    print('cheguei no else')
