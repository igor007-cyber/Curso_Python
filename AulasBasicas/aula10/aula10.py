#!/usr/bin/python3

usuario = input("digite o nome do usuario: ")

# comando len mostra a quantidade de caractere que tem na palavra ou no texto
quat_caract = len(usuario)

print(usuario, "tem", quat_caract, "caracteres",
      "o seu tipo é", type(quat_caract))

if quat_caract > 6:
    print('digite novamente')
else:
    print('usuario correto')
