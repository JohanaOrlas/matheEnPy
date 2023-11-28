"""Programa que calcula la suma de los cuadrados de los números entre 1 y n
Autor: Valentina Orlas
Fechas: noviembre 2023"""

#Variables
n = int(input("Ingrese la cantidad: "))
i = 1
suma = 0

#Proceso
while i <= n :
    suma += (i**2)
    i += 1

print(f"La suma de los cuadrados entre 1 y {n} es: {suma}")


