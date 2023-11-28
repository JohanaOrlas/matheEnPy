""" Cree un programa que lea un número entre 1 y 15 y muestre si éste es primo o no
Autor: Valentina Orlas
Fecha: 2023
"""

# Declaración de variables a utilizar

numero = int(input("Ingrese un número entre 1 y 15: "))

# Condicional para saber si el número es primo o no 

if numero == 2 or numero == 3 or numero == 5 or numero == 7 or numero == 11 or numero == 13 :

    print("El número es primo")
else:
    print("El número no es primo")