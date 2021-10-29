'''
Joel Sempere Durá - Ejercicio 9
Muestra por pantalla solo las suspendidas.
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
            asignaturas[contador][1] = int(nuevoValor)

    #salida del recorrido con los nuevos datos
    contador = -1
    salidaFinal = ""
    for x in asignaturas:
        contador = contador + 1
        #print(contador)
        #si la nota es menor a 5 la muestra por pantalla
        if int(x[1]) < 5:
            salidaFinal+="Tienes que repetir:\n"+x[0]+" has sacado -> "+str(x[1])+"\n---------------------\n"
        #Si la nota es mayor o igual a cinco la retira de la lista
        else:
            '''
            He probado con del, con remove y con pop, no se que se me pasa
            que algunos valores los salta'''
            del asignaturas[contador]

    #resultado de la lista despues del pop
    print(salidaFinal)
    print("Resultado final de la lista -> "+str(asignaturas))
except Exception as ex:
    print(ex)
    exit(-1)

#resultado de la lista final
#print(asignaturas)