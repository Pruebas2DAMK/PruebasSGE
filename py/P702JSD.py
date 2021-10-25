'''
Joel Sempere Durá - Ejercicio 2
-------------------------------
Pide dos numeros al usuario y devuelve su division
'''
preguntaNumeros= "Introduce dos numeros para realizar una division"
errorDivision= "Solo se aceptan valores numericos"

try:
    #Dos variables asignadas a un mismo input dividiendo los datos introducidos por un split
    numeroUno, numeroDos = input(preguntaNumeros+"\n").split()
    #compruebo si son numeros para realizar la division, y casteo que lo son , si no, no divide
    if numeroUno.isdigit() and numeroDos.isdigit():
        division = (int(numeroUno)/int(numeroDos))
        #Convertido en float por si divides un numero muy pequeño entre uno muy grande no suelte un chorro de numeros
        print(round(division, 2))
    else:
        print(errorDivision)
        exit(-1)
except Exception as e:
    #captura de error
    print(e)