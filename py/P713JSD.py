'''
Joel Sempere Durá - Ejercicio 13
--------------------------------
Simular una cesta de la compra con un diccionario. preguntar articulo y precio y añadirlo a la cesta
hasta que el usuario decida terminar. mostrar al final la lista de la compra y el coste total:

Lista de la compra
Artículo 1 Precio
Artículo 2 Precio
Artículo 3 Precio
... ...
Total Coste
'''
cestaCompra = {}
funLoop = True

#bucle que recorre el diccionario y lo imprime
def imprimeCestaCompra():
    salida="Lista de la compra\n"
    totalCoste=0
    for producto, precio in cestaCompra.items():
        salida += producto.upper() + "    " +str(precio)+" €\n"
        totalCoste += float(precio)
    salida+="\n-----------------------------\n" \
            "Total    "+str(round(totalCoste,2))+" €"
    print(salida)

while funLoop:
    seguirComprando=input("¿Quiere añadir algun producto a la cesta de la compra? (s/n)\n")
    if seguirComprando[0:1].lower() == "s":
        try:
            #guardo clave valor en estas dos variables
            nombreProducto=input("Nombre del producto:\n")
            valorPrecio=input("Valor del producto:\n")
            #actualizo el diccionario
            cestaCompra.update({nombreProducto: valorPrecio})
        except Exception as ex:
            print(ex)

    else:
        #muestro el contenido de la cesta
        imprimeCestaCompra()
        funLoop = False