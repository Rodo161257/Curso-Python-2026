# Ejercicio 5

# Pedile números al usuario hasta que ingrese un 0. Al final, mostrá cuántos números ingresó (sin contar el 0) y la suma de todos ellos.

        
suma = 0
cantidad = 0
numero = int(input("Ingresá un número (0 para terminar): "))
while numero != 0:
    suma += numero
    cantidad += 1
    numero = int(input("Ingresá un número (0 para terminar): "))
print(f"Ingresaste {cantidad} números. Suma: {suma}")