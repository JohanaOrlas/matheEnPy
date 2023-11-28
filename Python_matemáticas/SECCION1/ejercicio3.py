"""Programa para calcular la cuota de un monto de un préstamo
Autor: Valentina Orlas
Fecha: 20/10/2023
"""
# Definición de las variables que se utilizarán 


montoPrestamo = float(input("Ingrese el monto del préstamo: "))
plazoMeses = int(input("Ingrese el plazo en meses: "))

#Porceso para calcular la cuota mensual 
cuotaMensual ="{:.2f}".format((montoPrestamo * 0.027) / ( 1 - ( 1 + 0.027 ) ** (-plazoMeses)))#"{:.nf}".format() --> así se muestra n cantidad de números después del punto decimal

print("La cuota mensual a pagar es de: "+ str(cuotaMensual))