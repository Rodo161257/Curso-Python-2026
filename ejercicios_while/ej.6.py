# Ejercicio 6
# Simulá un cajero automático simple: el usuario empieza con $1000 de saldo. En cada iteración le preguntás cuánto quiere retirar. El programa termina cuando el saldo llega a 0 o el usuario ingresa un monto mayor al saldo disponible.
saldo = 1000
retira = int(input("ingrese $ a retirar   "))
while saldo >= retira:
    saldo = saldo - retira
    print ("saldo", saldo)
    retira = int(input("ingrese $ a retirar   "))
print("Saldo insuficiente. Operación cancelada")
    