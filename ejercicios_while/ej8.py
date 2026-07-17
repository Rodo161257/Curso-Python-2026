## Ingresar notas hasta ingresar -1. Mostrar cantidad de notas ingresadas, el promedio,
## el mayor y el menor.
suma = 0
cantidad = 0
nota = int(input("Ingrese una nota:  "))
while nota != -1:
    suma += nota
    cantidad += 1
    promedio = suma / cantidad
    print ("cantidad de notas:  ", cantidad)
    print("promedio:  ", promedio)
    nota = int(input("Ingrese nota:   "))
if nota >=0:
    print("la nota mayor es:  ", nota)

