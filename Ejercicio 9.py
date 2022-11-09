# Escribir un programa que pida al usuario una palabra
# y muestre por pantalla el número de veces que contiene cada vocal.

palabra = input("Introduzca una palabra:\n")
list_vocal = ["a", "e", "i", "o", "u"]
for vocal in list_vocal:
    veces = 0
    for letra in palabra:
        if  letra == vocal:
            veces = veces + 1
    print("La {} aparece {} veces".format(vocal, str(veces)))

