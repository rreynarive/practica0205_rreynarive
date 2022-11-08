# Escribir un programa que pida al usuario una palabra
# y muestre por pantalla el número de veces que contiene cada vocal.

palabra = input("Introduzca una palabra:\n")
list_vocal = ["a", "e", "i", "o", "u"]


for vocal in palabra:
    if vocal == list_vocal:
        print()

