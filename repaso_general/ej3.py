import os
os.system("cls")

"""
Ejercicio 3 — La alcancía digital
Alguien quiere ahorrar $10.000. Cada semana deposita una cantidad variable. El programa pide montos hasta que:

Se llega o supera el objetivo, o
El usuario escribe 0 para parar antes.
Al terminar, mostrá cuánto ahorró y si llegó al objetivo.


Depósito (0 para parar): 2500
Depósito (0 para parar): 3000
Depósito (0 para parar): 1500
Depósito (0 para parar): 4000
¡Llegaste al objetivo! Ahorraste $11000 en 4 depósitos.

Depósito (0 para parar): 1000
Depósito (0 para parar): 500
Depósito (0 para parar): 0
No llegaste al objetivo. Ahorraste $1500 (te faltan $8500).
"""


OBJETIVO = 10000
total = 0
ahorro = 0

monto = float(input("Ingrese depòsito   "))
while total < OBJETIVO:
    monto = float(input("Ingrese depòsito   "))
    ahorro += monto
    if monto >=OBJETIVO:
        print("Llegaste al objetivo. Ahorraste $: ", monto)
    elif monto == 0: print("No llegaste al objetivo. Ahorraste $", monto)
    else: print("No llegaste al objetivo. Ahorraste $", monto)
    







OBJETIVO = 10000
total = 0
depositos = 0

monto = float(input("Depósito (0 para parar): "))
while total < OBJETIVO and monto != 0:
    total += monto
    depositos += 1
    monto = float(input("Depósito (0 para parar): "))

if total >= OBJETIVO:
    print(f"¡Llegaste al objetivo! Ahorraste ${total:.0f} en {depositos} depósitos.")
else:
    print(f"No llegaste al objetivo. Ahorraste ${total:.0f} (te faltan ${OBJETIVO - total:.0f}).")
        

