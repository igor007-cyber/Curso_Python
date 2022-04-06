#!/usr/bin/python3
l1 = [0, 1, 2]
l2 = [3, 4, 5]
l1.extend(l2)  # ela extendi
l3 = l1 + l2
l2.append('a')  # ela adiciona
l2.insert(0, 'oi')  # ela vai inserir em qualquer lugar
l4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l1)
print(l2)
print(l3)
print('')

l2.pop()  # ela exclui a ultima
print(l2)
print('')

del(l3[3:5])  # ela exclui a quantidade que voce quiser
print(l3)
print('')

print(max(l4))
print(min(l4))  # ele mostra o maximo e o minimo valor
print('')

soma = 0
l5 = list(range(1, 5))
for valor in l5:
    soma += valor
print(soma)

l6 = [-10, 10, 1.3, 'ola', True]
for classe in l6:
    print(f'O tipo é {type(classe)} e seu valor é "{classe}"')
