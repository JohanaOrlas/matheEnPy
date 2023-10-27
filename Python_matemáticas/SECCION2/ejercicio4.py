""" Programa que calcula el precio final con IVA incluído
Autor: Valentina Orlas
Fecha: Octubre 2023
"""

# Declaración de variables a utilizar

precio = float(input("Ingrese el precio del producto: "))

# Proceso para calcular el precio final con IVA del 19%

precioFinal = (precio * 0.19) + precio

# Salida de datos
print("El total a pagar con el IVA incluido es de: " + str(precioFinal))
 
