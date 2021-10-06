#Joel Sempere Durá

mensaje = "Dime cualquier cosa que se te pase por la cabeza: "
print(mensaje)
entradaUser = input()
separador="============"

if (len(entradaUser) > 1):
    print("Has escrito "+entradaUser)
    print("Tiene ",len(entradaUser),"caracteres")
    listaRango=list(range(len(entradaUser)))
    print("Te creo una lista con un metodo del tamaño de caracteres de tu texto",listaRango)
    print (separador)
    for i in entradaUser:
        print(i*2)
    print(separador)
    print("cinco caracteres de izquierda a derecha: [",entradaUser[0:5],"] y cinco de derecha a izquierda [",entradaUser[-6:-1],"]")
else:
    exit()


