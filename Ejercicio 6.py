# Escribir un programa que almacene las asignaturas
# de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado
# en cada asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que
# el usuario tiene que repetir.
lst_materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobado = []
for materia in lst_materias:
    nota = float(input("¿Que nota has sacado en {}? ".format(materia)))
    if nota >= 5:
        aprobado.append(materia)
for materia in aprobado:
    lst_materias.remove(materia)
print("Tienes que repetir {}".format(str(lst_materias)))
