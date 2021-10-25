'''
Joel Sempere Durá
-----------------
Programa que recibe una cadena de caracteres y la guarda en una variable,
pregunta al usuario por la contraseña y la imprime si coincide con la guardada
sin tener en cuenta mayusculas y minusculas
'''
preguntaInicio = "¿Quieres introducir una contraseña? (s/n)"
preguntaContra = "Introduce tu contraseña: "
contrasenyaGuardada = "prueba"
esCorrectaContrasenya= False
def compruebaContrasenya(respuestaContra):
    if respuestaContra == contrasenyaGuardada:
        print("Coinciden\nTu contraseña es ->\n"
              + respuestaContra)
        esCorrectaContrasenya = True
    else:
        print("Contraseña incorrecta")



while True:
    print(preguntaInicio)
    respuestaInicio = input()
    if respuestaInicio[0:1].lower() == "s":
        print(preguntaContra)
        respuestaContra = input()
        #=====================================
        while True:
            if len(respuestaContra) == 0:
                print("No es posible guardar una contraseña de ese tamaño, vuelva a intentarlo por favor")
            else:
                compruebaContrasenya(respuestaContra)
                break
        # =====================================
        break
    elif respuestaInicio[0:1].lower() == "n":
        print("Hasta Luego\nSaliendo...")
        break
    else:
        print("Tienes que responder adecuadamente")


