#!/usr/bin/python3
# ----------------------meu-----------------------
cpf = '05167178398'
x = '051671783'
i = 0
j = 10
soma = 0

while i < 9:
    a = int(x[i])
    print(f'{a} * {j} = {a * j}')
    mult = a * j
    soma += mult
    i += 1
    j -= 1
print()
print('A soma desses numeros vai dar:', soma)
resutado = 11 - (soma % 11)
print(f'11 - {soma} % 11 = {resutado}')
ok = int(cpf[9])
if resutado == ok:
    resutado = str(resutado)
    x = x + resutado
    i = 0
    j = 11
    soma = 0
    print(x)
else:
    resutado = 1
    resutado = str(resutado)
    x = x + resutado
    i = 0
    j = 11
    soma = 0
    print(x)

print()

while i <= 9:
    a = int(x[i])
    print(f'{a} * {j} = {a * j}')
    mult = a * j
    soma += mult
    i += 1
    j -= 1
print()
print('A soma desses numeros vai dar:', soma)
resutado = 11 - (soma % 11)
print(f'11 - {soma} % 11 = {resutado}')
ok = int(cpf[10])
if resutado == ok:
    resutado = str(resutado)
    x = x + resutado
    i = 0
    j = 10
    soma = 0
    print(x)
else:
    resutado = 1
    resutado = str(resutado)
    x = x + resutado
    i = 0
    j = 10
    soma = 0
    print(x)

if x == cpf:
    print('cpf valido')
else:
    print('invalido')
# ----------------------------------professor----------------------------

cpf1 = '05167178398'
novo_cpf = cpf1[:-2]
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9
    total = int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)
print(novo_cpf)
if cpf1 == novo_cpf:
    print('valido')
else:
    print('invalido')
