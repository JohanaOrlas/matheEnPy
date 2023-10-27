"""Programa que calcula el volumen de un cubo
Autor:Valentina Orlas
Fecha: 21/10/2023
"""

# Definición de las variables que se utilizarán 

ladoCubo = float(input("Ingrese un lado del cubo: "))

# Proceso para calcular el volumen del cubo
volumenCubo = "{:2}".format(ladoCubo**3)

# Salida de datos

print("El volumen del cubo es de: "+str(volumenCubo))