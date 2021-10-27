'''
Joel Sempere Durá- Ejercicio 4
-------------------------------
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo
y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a
la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por
pantalla el grupo que le corresponde.
'''
alfabeto = ["abcdefghijklm","nñopqrstuvwxyz"]
nombre=input("¿Como te llamas?\n")
sexo=input("¿Eres hombre o mujer?\n").lower()[0]
grupo="A"
#Si es una mujer y la primera letra esta en la cadena de caracteres cero o si es hombre y la primera letra esta en la cadena 1 entonces pertenece al grupo A, si no al B
if  (sexo == "m" and nombre.lower()[0] in alfabeto[0]) or (sexo == "h" and nombre.lower()[0] in alfabeto[1]):
    print(nombre+" estas en el grupo "+grupo)
else:
    grupo="B"
    print(nombre+" estas en el grupo "+grupo)


