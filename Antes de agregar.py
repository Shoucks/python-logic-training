# E02

edad = int(input("¿Cual es tu edad? "))
acompañante = input("¿Vienes acompañado? (Si o No) ")

if edad >= 18 or acompañante == "Si":
    print("Puedes pasar")
else:
    print("No puede pasar")