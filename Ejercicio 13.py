# Escribir un programa que pregunte por una
# muestra de números, separados por comas, los guarde en una lista
# y muestre por pantalla su media y desviación típica.
num = input("Introduzca numeros separados por comas:\n")
num = num.split(",")
n = len(num)
for i in range(n):
    num[i] = int(num[i])
num = tuple(num)
sum = 0
suma = 0
for i in num:
    sum +=1
    suma += i**2
media = sum/n
desviacion = (((suma-media)**2)/n)**(1/2)
print("La media es {0} y la desviacion tipica es {1}".format(media, desviacion))