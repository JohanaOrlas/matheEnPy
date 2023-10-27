"""Cree un programa que reciba tres números y muestre el mayor. En caso de que los números sean iguales
también se debe mostrar al usuario.
Autor: Valentina Orlas
Fecha: Octubre 2023
"""

# Declaración de variables a utilizar

numero1 = float(input("Ingrese el primero número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Condicionales para saber cuál es mayor o si son iguales

if numero1 > numero2 and numero1 > numero3:
    print("El número "+str(numero1)+" es mayor")

elif numero1 == numero2 and numero2 == numero3:
    print("Los números son iguales")

elif numero2 >numero1  : 
    print("El número "+str(numero2)+" es mayor")
    
else:
    print("El número "+str(numero3)+" es mayor")