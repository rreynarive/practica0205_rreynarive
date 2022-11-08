# Escribir un programa que pida al usuario una palabra
# y muestre por pantalla el número de veces que contiene cada vocal.
palabra = input("Introduzca una palabra:\n")
list_vocal = list("aeiou")
for vocal in list_vocal:
    for i in palabra:
        if i == vocal:
            print(i)
