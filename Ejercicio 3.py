# Escribir un programa que almacene las asignaturas de un
# curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada
# asignatura, y después las muestre por pantalla con el mensaje
# En <asignatura> has sacado <nota> donde <asignatura> es cada una des
# las asignaturas de la lista y <nota> cada una de las correspondientes notas
# introducidas por el usuario.

lst_materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

mate = input("¿Que nota has sacado en Matematicas? ")
fisi = input("¿Que nota has sacado en Fisica? ")
quimi = input("¿Que nota has sacado en Quimica? ")
histo = input("¿Que nota has sacado en Historia? ")
leng = input("¿Que nota has sacado en Lengua? ")
lista_notas = [mate, fisi, quimi, histo, leng]

for m, n in zip(lst_materias, lista_notas):
    print(m, " En {0} has sacado un {1}".format(m, n))
