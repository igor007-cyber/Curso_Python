'''

Expressoes lambda(funcoes anonimas) em python

'''
a = lambda x, y: x * y


print(a(2, 2))

lista = [
    ['p1', 'igor'],
    ['p2', "alberto"],
    ['p3', 'flavio'],
    ['p4', 'gabi'],
    ['p5', 'lucas']
]

# vai organizar minha lista em seguencia
print(sorted(lista, key=lambda i: i[1], reverse=True))
lista.sort(key=lambda item: item[0], reverse=True)  # ele coloca na seguencia
print(lista)
