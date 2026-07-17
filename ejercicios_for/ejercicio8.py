import os
os.system("cls")

## Ejercicio 8 imprima un triángulo con n asteriscos
"""
n = int(input("ingrese un número:  "))
for i in range(1, n+1):
    print("*" * i)
"""

n = int(input("ingrese un número:  "))
for i in range(n):
    asterisco =  (i+1)*("*") 
    print(asterisco)
