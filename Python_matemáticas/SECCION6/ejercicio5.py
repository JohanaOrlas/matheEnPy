"""Programa que pregunta al usuario si desea salir, si o no “S/N”, si el usuario teclea la letra S el
programa se detendrá, de lo contrario continuará ejecutándose
Autor: Valentina Orlas
Fecha: noviembre 2023"""

#Variables
salir = True

#Proceso
while salir:
    preg= input(" ¿ Desea salir del programa S/N ? : ")
    if( preg.lower()  == "s"):
        salir = False







