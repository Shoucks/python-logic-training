#Bloque 01
# E01
edad = int(input("Dime tu edad "))
if edad <= 17:
    print("Menor de edad")
elif edad <= 64:
    print("Adulto")
else:
    print("Adulto (65+)")

# E02
nota = int(input("Dime tu nota del examen "))

if nota <= 5:
    print("Suspenso")
elif nota == 6:
    print("Aprobado")
elif nota == 7:
    print("Notable")
elif nota == 8:
    print("Notable")
else:
    print("Sobresaliente")

# Puede mejorara
#
# E03
numero = int(input("Dime un numero "))
if numero <= -1:
    print("Negativo")
elif numero == 0:
    print("Cero")
else:
    print("Positivo")

# E04
numero = int(input("Dame un numero Positivo"))
if numero >= 10 >=50:
    print("Perfecto")
else:
    print("Fuera de parametros")