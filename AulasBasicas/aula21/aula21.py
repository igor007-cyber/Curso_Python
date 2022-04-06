#!/usr/bin/python3
"""
Split, join, Enumerate em python
* Split - Dividir uma string #str
* join - juntar uma lista #str
* Enumerate - Enumerar elementos da lista #list / iteraveis
* count -> ele vai contar quantos tem

"""
variavel = "O brasil e o pais do futebol, o brasile penta."
lista_1 = variavel.split(' ')
lista_2 = variavel.split(',')
palavra = ''
contagem = 0

print(lista_1)
print(lista_2)

print()

for valor in lista_1:
    print(f'A palavra "{valor}" apareceu {lista_1.count(valor)}x na frase')

print()

for valors in lista_1:
    qtd_vezes = lista_1.count(valors)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valors
print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')
print()

for valores in lista_2:
    # strip -> ele remove o espaço tanto no final com no inicio
    print(valores.strip().capitalize())

print()

string = "igor é lindo"
string3 = ['igor', 'joao', 'maria']
lista_0 = string.split(' ')
# Aqui ele está adicionando uma vircula e tirando os espaços
string2 = ','.join(lista_0)
print(string)
print(lista_0)
print(string2)

print()

for indice, valo in enumerate(lista_0):
    print(indice, valo)

print()

lista = [
    [1, 2],
    [3, 4],
    [5, 6],
]

for v in lista:
    print(v[0], v[1])

print()
n1, n2, n3 = string3
print(n1)
