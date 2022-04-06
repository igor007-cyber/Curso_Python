#!/usr/bin/python3

x = 0
y = 10

while True:
    print(x, y)
    x += 1
    y -= 1
    if x == 9 and y == 1:
        break
print()

b = 10
for a in range(9):
    print(a, b)
    b -= 1
print()
# outro tipo:
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
