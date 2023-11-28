"""Programa que calcula la suma de los primeros n números naturales
Autor: Valentina Orlas
Fecha: noviembre 2023"""

#Variable
n = int(input("Ingrese un número natural: "))

#Proceso
if( n < 0):
    print("El número ingresado no es natural")
else:
    i = 1
    suma = 0
    while( i <= n):
        suma += i
        i += 1
    print(f"La suma de los números naturales hasta {n} es: {suma} ")


