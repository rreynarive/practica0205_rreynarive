# Escribir un programa que pida al usuario
# una palabra y muestre por pantalla si es un palíndromo
palabra = input("Introduzca una palabra:\n")
palindromo = palabra

palabra = list(palabra)
palindromo = list(palindromo)
palindromo.reverse()
if palabra == palindromo:
    print("La palabra es un palindromo")
else:
    print("No es un palindromo")