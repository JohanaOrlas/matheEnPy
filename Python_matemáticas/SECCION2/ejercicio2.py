"""Programa que calcula el área y el perímetro de un cículo
Autor: Valentina Orlas
Fecha: 21/10/2023
"""

#Importación de la librería math 

import math

# Definición de las variables que se utilizarán 

radio = float(input("Ingrese el radio: "))

#Proceso para calcular el área y perímetro de un cículo 


areaTriangulo = "{:.2f}".format(math.pi * (radio**2))
perimetroTriangulo ="{:.2f}".format( 2 * math.pi * radio)

#Salida de datos

print("El área del círculo es : " + str(areaTriangulo))
print("El perímetro del círculo  es: "+str(perimetroTriangulo))
