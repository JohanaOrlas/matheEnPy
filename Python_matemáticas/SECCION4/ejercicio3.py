""" Cree un programa que lea un número y muestre si éste es divisible entre cinco o no.
Autor: Valentina Orlas
Fecha: 2023
"""

# Declaración de variables a utilizar

numero = float(input("Ingrese el número: "))

# Condicional para saber si es par o no el número

if numero % 5 == 0:
    print("El número es divisible entre 5")
else:
    print("El número no es divisible entre 5")