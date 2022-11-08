# Escribir un programa que almacene el abecedario
# en una lista, elimine de la lista las letras que
# ocupen posiciones múltiplos de 3, y muestre por
# pantalla la lista resultante.
list_abec = list("abcdefghijklmnñopqrstuvwxyz")
for i in range(len(list_abec), 0, -1):
    if i % 3 == 0:
        list_abec.pop(i-1)
print(list_abec)