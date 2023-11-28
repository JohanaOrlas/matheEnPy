"""Programa que imprime los números naturales de 1 a n
Autor: Valentina Orlas
Fecha: noviembre 2023
"""
#Variable
num = int(input("Ingrese un número natural: "))

#Proceso
if(num < 0):
    print ("Error, el valor debe ser positivo")
else:
    i = 1
    print (f"Los números naturales hasta el {num} son: " )
    while(i <= num):
        print(f"{i}")
        i += 1