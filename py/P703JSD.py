'''
Joel Sempere Durá - Ejercicio 3
--------------------------------
Pide un numero entero al usuario y muestra por pantalla si es par o impar
'''
numero=input("Introduce un numero entero\n")
try:
    if numero.isdigit():
        #probando un ternario para comprobacion
       resultado = numero+" es par" if (int(numero) % 2 == 0) else numero+" es impar"
       print(resultado)
    else:
        print("Solo se acepta UN numero entero")
except Exception as e:
    print(e)
    exit(-1)