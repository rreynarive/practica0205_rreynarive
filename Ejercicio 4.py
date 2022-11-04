# Escribir un programa que pregunte al
# usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla
# ordenados de menor a mayor.
loteria = list(input("Introduzca numero ganadores de la loteria:\n"))
for a in sorted(loteria):
    print(a)

