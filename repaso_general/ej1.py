import os
os.system("cls")

## Ejercicio 1 — La fotocopiadora
##Una fotocopiadora cobra $15 por hoja. Si la cantidad supera las 100 hojas, aplica un descuento del 20% sobre el total.

##Escribí un programa que pida la cantidad de hojas y muestre el precio final con 2 decimales. Si hubo descuento, mostralo por separado.


##Cantidad de hojas: 50
##Total: $750.00

##Cantidad de hojas: 150
##Subtotal: $2250.00
##Descuento (20%): $450.00
##Total: $1800.00

## PASOS
## 1 - Ingresar cantidad de hojas
## 2 - Ingresar precio
## 3 - Obtener total multiplicando cantidad por precio
## 4 - Si el total supera las 100 hojas aplica descuenta 20%
## 5 - Imprimir el descuento en $
## 6 - Restar el descuento al total

cant_hojas = int(input("Ingrese cantidad de hojas   "))
PRECIO_HOJA = 15
total = cant_hojas * PRECIO_HOJA
print(f"$Total:  {total:.2f}")   
if cant_hojas >= 100:
    descuento = total * 0.2
    print("Descuento (20%): $", descuento)
    print("Total: $", total - descuento)



