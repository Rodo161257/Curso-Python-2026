
import os

from carton import generar_carton, estado_del_carton
from sorteo import verificar_ganador, sacar_numero

os.system("cls")

def jugar_individual():

    print("Empieza el juego")

    print()
    carton = generar_carton()

    print(f"Tu cartòn: {sorted(carton)}")
    print() ## salto de lìnea

    input("Presione Enter para empezar...")

    bolillero = set(range(1, 91))

    salientes = set()

    cont = 0
    while not verificar_ganador(carton, salientes):
        num = sacar_numero(bolillero, salientes)
        cont += 1
        if num in carton:
            estado_del_carton(carton, salientes)
        input("Presione Enter para continuar...")

    print(f"BINGO! Ganaste en {cont} turnos")      
