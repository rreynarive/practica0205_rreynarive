# Escribir un programa que almacene las matrices:
a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1, 1))
resultado =[[0, 0]
            [0, 0]]
for i in range(len(a)):
    for j in range(len(b[2])):
        for k in range(len(b)):
            