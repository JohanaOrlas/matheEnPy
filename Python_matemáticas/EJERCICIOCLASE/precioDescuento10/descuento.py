"""Cree un programa que tome el valor de un producto e imprima su precio final si éste
tiene siempre un descuento del 10%  
Autor: Valentina Orlas
Fecha: Octubre 2023""

"Declaración de variables"""

precioInicial = float(input("Ingrese el precio: "))

"""Proceso para calcular el descuento"""

descuento = precioInicial - (precioInicial * 0.10)

"""Salida de datos"""

print("El total a pagar con el descuento incluido es de: "+ str(descuento))