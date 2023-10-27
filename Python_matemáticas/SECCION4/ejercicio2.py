""". Cree un programa que lea un número y muestre si éste es par o impar
Autor: Valentina Orlas
Fecha: 2023
"""

# Declaración de variables a utilizar

numero = float(input("Ingrese el número: "))

# Condicional para saber si es par o no el número

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")