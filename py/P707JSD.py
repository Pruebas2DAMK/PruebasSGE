'''
Joel Sempere Durá - Ejercicio 7
pregunta una frase y una letra y muestra por pantalla el numero
de veces que se repite la letra en la frase
'''
try:
    frase=input("Dime una frase:\n")
    letra=input("Dime una letra:\n")
    cuentaLetras=0
    for x in str(frase):
        if x == letra:
            cuentaLetras=cuentaLetras+1
    print("La letra selecionada se repite dentro de la frase "+str(cuentaLetras)+" veces")
except Exception:
    print("ERROR")