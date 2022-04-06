#!/usr/bin/python3
'''
Desempacotamento - de lista e python

'''
listas = ['igor', 'gabi', 'ian']
lista = ['igor', 'gabi', 'ian', 3213, 3213, 3213, 322, 31]

n1, n2, n3 = listas

# *outra_lista -> Aqui ele armazena o resto da minha lista e é preciso coloca-lo se voce só quer alguns
# o 'n4' vai pegar lista[0] e assim por diante que vai até ultimo da lista
n4, n5, *outra_lista = lista

*outra_listas, n6, n7 = lista
# Aqui ele vai pegar os ultimos da minha lista e o resto vai ta na 'outra_listas'

print(n1, n2, n3)
print(outra_lista)
print(n6, n7)
print(outra_listas)
