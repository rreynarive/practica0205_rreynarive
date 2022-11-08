# Escribir un programa que pregunte al
# usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla
# ordenados de menor a mayor.

lista_loteria = []

loteria = int(input("Introduzca numero ganadores de la loteria:\n"))
while loteria != 0:
    lista_loteria.append(loteria)
    loteria = int(input("Introduzca numero ganadores de la loteria:\n"))

lista_loteria.sort()

print("lista de ganadores", end="\n")
for loteria in lista_loteria:
    print(loteria, end="\n")
