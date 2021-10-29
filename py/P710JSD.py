'''
Joel Sempere Durá -Ejercicio 10
Guardar un diccionario con los precios de las frutas de la tabla, preguntar al usuario por una fruta y un numero de kilos
y muestre por pantalla el precio de ese numero de kilos de la fruta.
Si no esta en el diccionario avisar al cliente
'''
dictFruta = {
    'platano': 1.35,
    'manzana': 0.80,
    'pera': 0.85,
    'naranja': 0.70
}
preguntaFruta = input("¿Que fruta quieres comprar?\n").lower()
#recibe la salida del usuario en minusculas
if preguntaFruta in dictFruta:
    #si existe la fruta entonces pregunta los kilos que desea
    cuantosKilos = input("¿Cuantos kilos quieres?\n")
    #se obtiene el valor numerico
    precio = float(dictFruta.get(preguntaFruta))
    #se convierte a numero la string que nos ha pasado el usuario
    kilos = int(cuantosKilos)
    #resultado final positivo
    print("El precio total es de " + str(round(precio*kilos, 2)) + " €")

else:
    print("Lo siento, no disponemos de la fruta que usted anda buscando")