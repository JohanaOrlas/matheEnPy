"""Cree un programa que reciba dos números y muestre el mayor. En caso de que los números sean iguales
también se debe mostrar al usuario.
Autor: Valentina Orlas
Fecha: Octubre 2023
"""

# Declaración de variables a utilizar

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Condicionales para saber cuál es mayor o si son iguales

if numero1 > numero2:
    print("El número "+str(numero1)+" es mayor")
elif numero1 == numero2:
        print("Los números son iguales")
else: 
    print("El número "+str(numero2)+" es mayor")