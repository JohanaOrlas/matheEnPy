"""Programa para calcular la edad de un usuario en x años
Autor: Valentina Orlas
Fechas: 20/10/2023"""

#Se ingresa la edad y el núemero de años a calcular

edad= int(input("Ingrese la edad: "))
anios = int(input("Ingrese los años a calcular: "))

#Calcula la edad
aniosEdad = edad + anios

#Salida
print("En  "+str(anios)+" años va a tener "+str(aniosEdad)+" años")
