
def arrozConTomate(ingrediente="tomate"):
    return "El arroz tiene + "+ingrediente

numeros=range(0,11)
for i in numeros:
    if( i == numeros[7]):
        print(i)
numero=0

while True:
    numero+=1
    
    print("*"*numero)
    if(numero > 101):
        break

print("como te llamas")
nombre=input()
print(f"Hola {nombre}")
print("Hola "+nombre)
print("Hola",nombre)

print("digame una cantidad en pesetas")
dineroPesetas=input()

dineroEuros=round(int(dineroPesetas)/600,2)

print("Lo que tu tienes son "+str(dineroEuros)+ "€")

print(arrozConTomate())