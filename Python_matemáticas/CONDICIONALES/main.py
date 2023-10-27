"""
Programa que muestra el manejo de condicionales en Python 3 
Autor: Valentina Orlas
Fecha: Octubre 20 de 2023"""

#pedimos nombre,  si nombre es María la saludamos 

nombre = input("Ingrese nombre: ")

if nombre == "Maria":
    print("Hola María")
else: 
    print("Usted no es María")

print("--------------------    elif    ---------------------------------------")
estrato = int(input("Ingrese el estrato: "))

if estrato == 1:
    print("Tiene derecho a subsidio completo")
elif estrato == 2:
    print("Tiene a medio subsidio ")
else:
    print("Usted no tiene derecho a subsidio")