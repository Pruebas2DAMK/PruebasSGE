'''
Joel Sempere Durá - Ejercicio 12
Diccionario vacio que se rellene con informacion sobre una persona,
cada vez que se añada informacion debe imprimirse el diccionario
'''
dictInfPersonal = {}
funLoop = True

#bucle que recorre el diccionario y lo imprime
def imprimeDiccionario():
    for k, v in dictInfPersonal.items():
        print(k + " -> " + v)


#controlo el bucle principal con un booleano
while funLoop:
    #pregunto si quiere añadirme algo, solo tengo en cuenta el primer char
    infPersonal=input("¿Quieres añadir algo sobre ti? (s/n)\n")
    #lo paso a lower para no tener problemas
    if infPersonal[0:1].lower() == "s":
        try:
            #guardo clave valor en estas dos variables
            datoNuevo, valorNuevo=input("Dime cosicas [dato:valor]\n").split(":")
            #actualizo el diccionario
            dictInfPersonal.update({datoNuevo: valorNuevo})
            #saco por pantalla el contenido del diccionario
            imprimeDiccionario()
        except Exception as ex:
            print(ex)

    else:
        #muestro el contenido del diccionario
        imprimeDiccionario()
        #si no quiere seguir rompo el bucle
        funLoop = False