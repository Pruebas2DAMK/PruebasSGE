'''
Joel Sempere Durá - Ejercicio 8
Almacena las asignaturas del curso en una lista, preguntar las notas en cada una de ellas y imprimir
'''
try:
    asignaturas = [
        ["EIE", "0"],
        ["SGE", "0"],
        ["PSP", "0"],
        ["DIN", "0"],
        ["ADA", "0"],
        ["PMDM", "0"],
        ["ING", "0"]
    ]
    #para empezar desde 0
    contador=-1
    for i in asignaturas:
        #la asignatura en pantalla
        #print(i[0])
        #avanzando a la siguiente sublista
        contador=contador+1
        #la nota para modificarla
        for j in asignaturas[contador][1]:
            #asignamos nuevo valor
            nuevoValor=input("La nota de la asignatura "+i[0]+" es:\n")
            #si el valor no esta dentro del rango es un cero
            if int(nuevoValor) < 0 or int(nuevoValor) > 10:
                nuevoValor = 0
            asignaturas[contador][1]=int(nuevoValor)

    #salida del recorrido con los nuevos datos
    for x in asignaturas:
            print("En "+x[0]+" has sacado un "+str(x[1]))
except Exception:
    print("ERROR, no acepto cadenas de texto ni floats")
    exit(-1)

#resultado de la lista final
#print(asignaturas)

