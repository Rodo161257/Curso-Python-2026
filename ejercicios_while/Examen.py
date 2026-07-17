"""
## Ejercicio 1: respuesta B, da un float

## Ejercicio 2: respuesta B, da 2, el % (módulo) redondea a entero, sin decimales
x = 17 % 5
print(x)

# Ejercicio 3: respuesta correcta 2, 4. 6 imprime los números pares. Si bien el 8 es par el rango se toma hasta el número 7, por lo tanto el par más próximo al final es el 6.
for i in range(1, 8):
    if i % 2 == 0:
        print(i)

## Ejercicio 4:  imprime naranja, -2 significa segunda posición desde el final
        
frutas = ["manzana", "banana", "naranja", "uva"]
print(frutas[-2])

## Ejercicio5: diferencias entre while y for

## Ambos proporcionan iteración. El while se utiiza cuando existe una CONDICION y mientras esta es falsa  sigue iterando. Si al inicio del bucle la condición es verdadera el while NO SE EJECUTA, mientras que un FOR SIEMPRE SE EJECUTA y recorre un rango o una lista.
Además voy a utilizar un WHILE cuando no sepa cuántas veces voy a iterar y un FOR cuando sé con exactitud cuántas veces voy a iterar.


## Ejercicio 6: Escribí un programa que le pida al usuario su edad y muestre la categoría correspondiente:

## Rango	Categoría
##  0 – 12	🧒 Niño/a
## 13 – 17	🎒 Adolescente
## 18 – 64	🧑 Adulto/a
## 65 o más	👴 Adulto mayor

edad = int(input("Ingrese edad    "))
print("La edad ingresada es:  ",   edad)
if edad >= 0 and edad <=12: print("Niño")
elif edad >=13 and edad <= 17: print ("Adolescente")
elif edad >= 18 and edad <= 64: print ("Adulto/a")
elif edad <= 0 or edad >= 120 :print("Edad inválida")
else:  print("Adulto mayor")
## Ejercicio 7: WHILE
## Escribí un programa que le pida números al usuario uno por uno y los vaya sumando. El programa ## termina cuando el usuario ingresa el número 0. Al final, mostrá la suma total y la cantidad de ## números que ingresó (sin contar el 0)

cantidad = 0
suma = 0
numero =  int(input("Ingrese numero   "))
while numero !=0: 
   suma+=numero
   numero = int(input("Ingrese numero  "))
   cantidad += 1
print("La suma de intentos es   ", suma)
print("Cantidad de intentos   ", cantidad)

"""

## Ejercicio 8 PROFESOR ESTE EJERCICIO NO LO HICE, ES EL QUE MÁS QUE COSTO
## JUNTO CON LOS EJERCICIOS 3.4, 3.5, 4.1 Y 4.2 DEL CUADERNILLO.
# 
# Escribí un programa que:

## Calcule el promedio de cada alumno.
## Imprima solo los alumnos que aprobaron (promedio ≥ 6), con su nombre y promedio redondeado a 1 decimal.
## Imprima el nombre del alumno con el mejor promedio


curso = [
    ["Lucía", 7, 8, 9],
    ["Tomás", 4, 3, 5],
    ["Valentina", 10, 9, 8],
    ["Mateo", 6, 5, 7],
    ["Sofía", 2, 4, 3],
]

 ## 1. Promedios
mayor = 0
for alumno in curso:
    promedio = sum(alumno[1:]) / len(alumno[1:])
    nombre = alumno[0]

    if promedio >= 6:
        print(nombre, promedio)
    
    if promedio > mayor: 
        mayor = promedio
        maxAlu = nombre

print(f"Mayor promedio: {maxAlu} con {mayor}")

