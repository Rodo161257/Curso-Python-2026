## Elegir número secreto decir si es mayor o menor y contar intentos

intentos = 0
secreto = 7
numero = 0
while secreto != numero:
    numero = int(input("Ingrese número:   "))
    if numero == secreto:
        print("ACERTO!!!! El número secreto es el", secreto)
        intentos +=1
    elif numero < secreto:
        print("El número es menor al secreto")
        intentos +=1
    else:
        print("El número es mayor al secreto")
        intentos +=1
    print("Intentos:",  intentos)


##Ejercicio 7 Maxi
secreto = 42
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adiviná el número (1-100): "))
    intentos += 1
    if intento < secreto:
        print("El número secreto es mayor.")
    elif intento > secreto:
        print("El número secreto es menor.")
    else:
        adivinado = True

print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
