'''
1- Crie uma funçao que exibe uma saudaçao com os paramentros saudação e nome;
'''
print("#############")
print("QUESTAO 1")
print("#############")


def funcao(saudacao, nome):
    print(f"{saudacao} {nome}")


x = 'Seja bem vindo'
y = input('Digite o seu nome: ')

funcao(x, y)

'''
2- Crie uma funçao que receba 3 numeros como parametros e exiba a soma deles.
'''
print()
print("#############")
print("QUESTAO 2")
print("#############")


def soma(x, y, z):
    print(x+y+z)


# uma dica: nao coloca letra, porque vai dar problema. Por causa que eu tava com preguiça o correto. Mas fica o desafio pra voces tentarem fazer a forma correta;
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
c = int(input("Digite o ultimo numero: "))

soma(a, b, c)


'''
3- Crie uma funçao que receba 2 numeros. o primeiro é um valor e o segundo um percentual(ex.10%)
Retorne o valor do primeiro numero somado do aumento do percentual do mesmo. 
'''

print()
print("#############")
print("QUESTAO 3")
print("#############")


def aumento(d, e):
    c = d * e
    return d + c


# mesma coisa aqui
v = float(input("Digite um numero: "))
n = float(input("Digite um percentual(ex: 0.1): "))

resposta = aumento(v, n)
print(resposta)

'''
4- Fizz Buzz - Se o paramentro da funçao for divisivel por 3, retorne fizz, se  parametro 
da função for divisivel por 5, retorne buzz. Se o parametro da funçao for por 5 e po 3, 
returne FizzBuzz, caso ao contrario, retorne o numero enviado.
'''

print()
print("#############")
print("QUESTAO 4")
print("#############")


def calculo(j):
    if int(j) % 3 == 0 and int(j) % 5 == 0:
        return "FizzBuzz"
    elif int(j) % 3 == 0:
        return "Buzz"
    elif int(j) % 5 == 0:
        return "Fizz"
    else:
        return j


r = input("Digite um numero: ")

retorna = calculo(r)
print(retorna)
