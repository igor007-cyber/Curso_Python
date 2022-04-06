#!/usr/bin/python3
'''
*Enumarete - Enumerar elementos da lista #list
'''

lista = ['igor', 'ian', 'gabi']

lista1 = [
    #   0       1       2
    ['igor', 'ian', 'gabi'],  # 0
    ['lu', 'rita', 'maria'],  # 1
    ['aline', 'vivi', 'jo'],  # 2
]


for v1, v2 in enumerate(lista1):
    #print(v1, v2)
    nome1, nome2, nome3 = v2
    print(nome1, nome2, nome3)


'''
[
     0          1
    (0,['igor', 'ian', 'gabi']), # 0
           0     1       2
    (1,['lu', 'rita', 'maria']), # 1
    (2,['aline', 'vivi', 'jo']), # 2

]
'''
