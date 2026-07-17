from random import choice

def verificar_ganador(carton, salientes):
    return carton.issubset(salientes)
        
def sacar_numero(bolillero, salientes):
    numero = choice(list(bolillero))
    bolillero.remove(numero)
    salientes.add(numero)
    print(f"Salió el {numero}.")
    return numero