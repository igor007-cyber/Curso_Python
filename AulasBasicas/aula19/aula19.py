#!/usr/bin/python3
'''
Lista de python

Fatiamento:
append -> vai adicionar na ultima fileira;
insert -> vai inserir em qualquer lugar e o valor que desejar;
pop; 
del -> pode deletar um ou mais valores; 
clear; 
extend -> vai estender os numeros; +
min -> vai pegar o menor valor;
max -> vai pegar o maior valor;
range -> ele vai de valor ate o valor que voce colocou para ele seguir e
ainda pode pular as numeros;
'''
#         0   1   2   3
lista = ['i', 'g', 'o', 'r', 'bacana', 10]
# -       4   3   2   1

string = 'igorbacana10'  # é diferente de lista

print(string[4])
print(lista[4])
print(lista[::2])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
l2.insert(0, "a")

print(l1)
print(l2)

# del(l2[0:3])
del(l2[0])
print(l2)

print(max(l1))
print(min(l1))

l3 = list(range(1, 20, 2))
print(l3)
