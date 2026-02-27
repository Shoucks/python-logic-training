# E04

Cliente = input("¿Eres cliente vip? (si/no) ")
Compra = int(input("¿Cual es el monto de su compra? "))

if Cliente == "si" or Compra >= 100:
    print("A conseguido un descuento")
else:
    print("No hay descuento aplicable")