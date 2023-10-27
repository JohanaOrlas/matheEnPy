"""Programa que calcula el área de un triángulo
Autor: Valentina Orlas
Fecha: 20/10/2023"""

# Definición de las variables que se utilizarán 

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

#Proceso para calcular el área

areaTriangulo = "{:.2f}".format( (base * altura) / 2 )
#Salida de datos

print("El área del triángulo es: "+str(areaTriangulo))