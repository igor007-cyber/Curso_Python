'''
Tuplas em python
'''

t1 = (1, 2, 3, "a", "igor")  # isso aqui é uma tupla

print(t1)
print(t1[0])
print(t1[2:])
for x in t1:
    print(x)

t2 = "befi", 'ian', 'gabi'  # criando uma tupla

t3 = t1 + t2
print(t3)

n1, n2, n3, *_, n9, n10 = t3  # aqui ele vai distribuir pra todas as variaveis

print(n9)

# OBS.: TUPLA NAO PODE SER MODIFICADA. SÓ DA PRA MODIFICAR SE PASSAR A TUPLA
#       PRA LIST

x = list(t3)
x[3] = 'felipe'
print(x)
