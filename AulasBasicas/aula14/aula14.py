#!/usr/bin/python3
'''
Manipulando strings:

* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funçoes built-in len, abs, type, print, etc...

Essas funçoes podem ser usadas diretamente em cada tipo.

'''
# positivo [0123456789]
texto = 'igor ramal'
# negativo[-10,987654321]
novo_str = texto
url = 'www.google.com.br/'

print(url[:-1:2])
print(texto[0])
print(texto[-10])
print('')
print(novo_str[:5])
print(novo_str[1:7])
print(novo_str[-9:-3])
print(novo_str[::2])
