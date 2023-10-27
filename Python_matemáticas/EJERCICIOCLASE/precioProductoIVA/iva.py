"""Cree un programa que tome el precio de un producto e imprima su precio final al consumidor con un IVA
del 19% 
Autor: Valentina Orlas
Fecha: Octubre 2023
""

"Declaración de variables"""

precio = float(input("Ingrese el precio del producto: "))

precioFinal = (precio * 0.19) + precio

print("El total a pagar con el IVA incluido es de: " + str(precioFinal))
 




