"""Cree un programa que lea los tres ángulos internos de un triángulo y muestre si los ángulos corresponden
a un triángulo o no.
Autor: Valentina Orlas
Fecha: Octubre 2023
"""
# Declaración de variables a utilizar

angulo1 = float(input("Ingrese le primer ángulo: "))
angulo2 = float(input("Ingrese le segundo ángulo: "))
angulo3 = float(input("Ingrese le tercer ángulo: "))

# Proceso para la suma de sus ángulos

sumaAngulos = angulo1 + angulo2 + angulo3

# Condicional para saber si los ángulos corresponden a un triángulo

if sumaAngulos == 180:
    print ("Los ángulos ingresados forman un triángulo")
else:
    print ("Los ángulos ingresados NO forman un triángulo")