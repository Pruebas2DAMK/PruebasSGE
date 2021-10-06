#Joel Sempere Durá
#"%s lo que sea" % "variable o otro texto"
#"%s lo que sea %i y con un numero" % ("texto",numero)
#list = []
#list.append(añadir cosas)
#print list
#len(list)
#boolean ex -> dato in list -> true o false
#pasar lista a otra lista con .extend
texto = "Tamaño de lista l: "
#Creo una lista
l = [1, 2, 3, 4, 5, 67, 2]
#creo una tupla
t = (45,68)
#Añado un nuevo valor
l.append(91)
print(l)
#añado la tupla como un valor mas dentro de la lista
l.append(t)
print(l)
#pido el tipo
print(type(l[-1]))
print(type(l))
print("Dime cosicas")
#Los recibo y con split los divido en datos independientes
l2 =(input().split(" "))
print(l2)
#tamaño de la lista l
print(texto,len(l))
#extiendo el tamaño de l con l2
l.extend(l2)
print(l)
#tamaño de la lista l con el extend
print(texto, len(l))



