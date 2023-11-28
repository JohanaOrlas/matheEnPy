"""Programa que calcula el promedio de 10 números
Autor: Valentina Orlas
Fechas: noviembre 2023"""

#Variables 
promedio = 0
i = 1
suma = 0
#Proceso
while(i <= 10):
    num = float(input("Ingrese el numero: "))
    suma += num
    i += 1
promedio = suma / 10
print(f"El promedio es: {promedio}")

