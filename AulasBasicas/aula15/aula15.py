#!/usr/bin/python3
'''
while em python

ultilizado para realizar açoes enquanto 
uma condiçao  for verdadeira

requisito: Entender condiçoes e operadores

'''
num = 0
while num < 10:
    if num == 3:
        num += 1
        # break -> ele termina o laço de repetiçao
        continue  # ele pula para o proximo laço de repetiçao
    print(num)
    num += 1
print('acabou')
