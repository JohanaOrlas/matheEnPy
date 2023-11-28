"""Programa que muestra los números impares entre 1  y n 
Autor: Valentina Orlas
Fecha: noviembre 2023"""

#Variables
n = int(input("Ingrese un número: "))
i = 1


print(f"Los número impares entre 1 y {n} son: ")

#Ciclo while para mostrar los numeros impares de 1 a n
while i <= n:
    if i % 2 != 0:
        print(f"{i}")
    i += 1