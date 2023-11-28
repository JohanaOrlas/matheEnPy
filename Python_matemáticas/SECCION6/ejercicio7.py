"""Programa que muestra el promedio de n números, dejándose de solicitar si se ingresa el cero
Autor: Valentina Orlas
Fecha: noviembre 2023"""

#Variables
n = int(input("Introduca la cantidad de números que se van a usar: "))
i = 1
suma = 0

#Proceso
while( i <= n):
    numero = float(input("Ingrese el número:  "))
    if(numero == 0):
        print("\nIngresar números mayores a cero")
        break
    suma += numero
    i += 1
if(i > n):
    promedio = suma / n
    print(f"\nEl promedio de los números ingresados es: {promedio}")


