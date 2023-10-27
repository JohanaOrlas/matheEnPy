""" En un supermercado se tiene los siguientes productos: lentejas, crema, arroz y vino. Las lentejas y el
arroz no pagan IVA, el vino y la crema si. Cree un programa que reciba el nombre de alguno de los productos
mencionados y muestre si el producto paga IVA o no.
Autor: Valentina Orlas
Fecha: Octubre 2023 """

# Declaración del las variables a usar

producto = input("Ingrese el nombre del producto: ")
productoLower = producto.lower()

# Condicionales para saber si paga IVA o no

if productoLower == "lentejas" or productoLower == "crema" or productoLower == "arroz" or productoLower == "vino":

    if productoLower == "lentejas" or productoLower == "arroz":
        print("No paga el IVA")
    elif productoLower == "crema" or productoLower == "vino":
        print("Paga IVA")
else:
    print("El producto ingresado no es válido")   
