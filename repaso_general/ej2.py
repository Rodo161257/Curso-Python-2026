import os
os.system("cls")
"""
Ejercicio 2 — El clasificador de entradas
Un boliche tiene estas categorías por edad:

Edad	Mensaje
Menor de 18	"No puede ingresar"
18 a 25	"Entrada joven: $2000"
26 a 59	"Entrada general: $3000"
60 o más	"Entrada libre"

Escribí una función clasificar_entrada(edad) que reciba la edad y devuelva el mensaje correspondiente.

clasificar_entrada(16)  # → "No puede ingresar"
clasificar_entrada(22)  # → "Entrada joven: $2000"
clasificar_entrada(45)  # → "Entrada general: $3000"
clasificar_entrada(65)  # → "Entrada libre"

💡 Pista
¿Cuántas ramas tiene este problema? ¿Cuántos elif necesitás?
¿En qué orden conviene escribir las condiciones para que no se pisen?
La función tiene que devolver el string, no imprimirlo — ¿qué instrucción usás?

"""

def clasificar_entrada(edad):
    if edad < 18: return "No puede ingresar"
    elif edad <= 25: return "Entrada joven: $2000"
    elif edad <=59: return "Entrada general: $3000"
    else: return "Entrada libre"
    
edad = int(input("Ingrese edad   "))
print(clasificar_entrada(edad))
