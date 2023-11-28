"""Programa que calcula el promedio de tres notas para n estudiantes
Autor: Valentina Orlas
Fecha: noviembre 2023"""
#Variables
nEstudiantes = int(input("Ingrese la cantidad de estudiantes: "))


for i in range(1, nEstudiantes +1):
    n = 1
    sumaNotas = 0
    while(n <= 3): 
        nota= float(input("Ingrese la nota del estudiante " + str(i)))
        sumaNotas = sumaNotas + nota
        n = n + 1
        promedio = sumaNotas / 3
        formatP = "{:.2f}".format(promedio)
    print("El promedio del estudiante "+str(i)+" es: "+ str(formatP))

      
     
 

#Ciclo while se usa cuando no sabemos el número de iteraciones con certeza. Depende de una variable control del ciclo que cambia para hacer que el ciclo se detenga. Depende también de una condición

"""contador = 0

while(contador <= 99):
    contador = contador + 1
    print(str(contador))
"""
