'''
Dicionario em Python - Estrutura de dado e um valor
'''
import copy
d1 = {'chave1': 'valor da chave'}
d1['Nova chave'] = 'outra chave'  # adicionar uma nova chave

print(d1)
print(d1['chave1'])

# Outra forma de fazer uma chave
d2 = dict(chav1='valor da chave', chav2='valor da outra chave')
d2['chav3'] = 'ultima chave'
print(d2)

d3 = {
    'str': 'valor',
    123: 'outra valor',
    (1, 2, 3): 'tupla',
}

d3.update({'nova_chave': 'novo valor'})  # outro metodo de atualizar a chave

if d3.get('nova_chave') is not None:
    print(d3.get('nova_chave'))

print('str' in d3)  # vai checar se tem esse valor
print('str' in d3.keys())
print('str' in d3.values())
print(len(d3))  # vai contar, quantos pares tem
print('----------------')
for x in d3:  # aqui vai mostrar as chaves
    print(x)
print('----------------')
for x in d3.values():  # aqui vai mostra só os valores.
    print(x)
print('----------------')
for x, v in d3.items():  # Aqui vai acessar tudo
    print(x, v)
print('----------------')
del d3['str']  # vai deletar a chave
print(d3)

print('----------------')
clientes = {
    'cliente1': {
        'nome': 'igor',
        'sobrenome': 'ramalho',
    },
    'cliente2': {
        'nome': 'ian',
        'sobrenome': 'ramalho',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

# CUIDADO...ELE VAI MODIFICAR OS DOIS. É TIPO UM PONTEIRO, SE MODIFICA UM, VAI MODIFICAR O OUTRO
d4 = {1: 'a', 2: 'b', 3: 'c'}
v = d4
v[1] = 'luiz'
print(v)
print(d4)
# Correto
g = d4.copy()
g[1] = 'felipe'
print(g)
print(d4)

# CUIDADO...ele nao vai conseguir copiar a lista que está dentro do dicionario. com isso, ele repete nos dois
# porem colocando a biblioteca copy e colocando a sua funçao, ai sim, consegue copiar sem repetir.
d5 = {1: 'a', 2: 'b', 3: ['igor', 'ian']}
#i = d5.copy()
i = copy.deepcopy(d5)  # copia profunda
i[1] = 'luiz'
i[3][0] = 'iguinho'

print(d5)
print(i)

# d5.pop(1)  # vai deletar qualquer valor do meu dicionario
print('----------')
d6 = {1: 2, 2: 3, 4: 5, }
d7 = {'a': 'b', 'c': 'd', }
d6.update(d7)  # concatenar
print(d6)
