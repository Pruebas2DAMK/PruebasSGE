'''
Joel Sempere Durá -Ejercicio 5
Muestra al usuario cuanto tiene que pagar segun su renta anual
'''
try:

    rentaAnual = input("¿Cuanto cobras a lo largo del año?\n")

    #Evitando introducion de caracteres alfabeticos
    if rentaAnual.isalpha():
        print("Solo se aceptan valores numericos")
        exit(-1)

    tipoImpositivo = 0.05
    rentaAnual = int(rentaAnual)
    mensaje = "Tiene que pagar "

    if rentaAnual < 10000:
        '''
        Como no existe el case lo he hecho asi,
        cada if comprueba que el numero se encuentra dentro de su rango
        si es asi se establece un nuevo tipoImpositivo y se calcula en el mismo print
        que castea un string del casteo de un int de la operacion a realizar
        '''
        print(mensaje + (str(int(rentaAnual * tipoImpositivo))) + "€")
    elif rentaAnual >= 10000 or rentaAnual < 20000:
        tipoImpositivo = 0.15
        print(mensaje + (str(int(rentaAnual * tipoImpositivo))) + "€")
    elif rentaAnual >= 20000 or rentaAnual < 35000:
        tipoImpositivo = 0.20
        print(mensaje + (str(int(rentaAnual * tipoImpositivo))) + "€")
    elif rentaAnual >= 35000 or rentaAnual < 60000:
        tipoImpositivo = 0.30
        print(mensaje + (str(int(rentaAnual * tipoImpositivo))) + "€")
    elif rentaAnual >= 60000:
        tipoImpositivo = 0.45
        print(mensaje + (str(int(rentaAnual * tipoImpositivo))) + "€")
    else:
        print("ERROR")

except Exception:
    print("No has introducido un valor numerico")
