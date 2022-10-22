'''
Funções - def em Python - *args **kwargs - (parte 3)
'''

# quando isso acontece, dai por diante tem que fazer desse jeito;


def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)


func(1, 2, 3, 4, 5, "igor", 6)
#######################################################


def fun(*args):  # O args, vai pegar todos as variaveis dentro da tupla
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    args = list(args)  # aqui transformou de tupla pra lista
    args[0] = 20
    print(args)


fun(1, 2, 3, 4, 5)
#####################################


def funcao(*args):
    print(args)


lista = [11, 12, 13, 14, 15]
# Aqui vou desenpacotar a minha lista, ela vai fica assim: 11 12 13 14 15. Porque vai ficar dentro da tupla
funcao(*lista)
#########################################


def funca(*args, **kwargs):  # no kwargs, ele pega só os argumentos nomeados. Com isso, ele coloca eles dentro de chaves
    print(args)
    print(kwargs)
    print()
    # O get, se dentro dele tiver resultado, ele vai mandar o resultado. Se nao, ele vai mandar None
    nome = kwargs.get('nome')
    print(nome)


l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

funca(*l1, *l2, nome="igor", sobre="barbosa")
