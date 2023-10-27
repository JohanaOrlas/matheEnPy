"""cree un programa que lea una cantidad e imprima un porcentaje a calcular requerido sobre esa cantidad
Autor: Valentina Orlas
Fecha: Octubre 2023"""

cantidad = float(input("Ingrese la cantidad: "))
porcentaje=float(input("Ingrese el porcentaje a calcular: "))

cantidadTotal = cantidad - (cantidad * porcentaje/100)

print("El total a pagar es de: "+str(cantidadTotal))