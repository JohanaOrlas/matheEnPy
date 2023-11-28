"""Programa que dado un número n, calcule su factorial
Autor: valentina Orlas
Fecha: noviembre 2023
"""
#Variables
num = int(input("Ingrese el numero para calcular su factorial: "))
acumulador = 1

#proceso
if num < 0:
    print("El factorial no está definido para números negativos.")
elif num == 0 or num == 1:
    print(f"El factorial de {num} es 1")
else:
    for i in range(2, num + 1 ):
        acumulador = acumulador * i

print(f"El factorial de {num} es: "+ str(acumulador))




