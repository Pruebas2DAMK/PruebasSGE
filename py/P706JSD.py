'''
Joel Sempere Durá- Ejercicio 6
'''
contrasenya="contraseña"
while True:
    compruebaContrasenya=input("Introduce la contraseña:\n")
    if compruebaContrasenya == contrasenya:
        print("!Correcto!\nBienvenido de nuevo")
        exit(0)
    else:
        print("Contraseña incorrecta, intentelo de nuevo")