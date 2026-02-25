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
numero = int(input("Dame un numero Positivo "))
if numero >= 10 >=50:
    print("Perfecto")
else:
    print("Fuera de parametros")

# E05
nick = "admin"
password = "1234"
usuario = input("Nombre de usuario ")

if nick == usuario:
    contraseña = input("Coloque contraseña ")
    if password == contraseña:
        print("Accede a base de datos con exito")
    else:
        print("Nombre de usuario no coindice con la contraseña")
else:
    print("Nombre de usuario incorrecto")

# E06
print("Comparativa de numeros para ver cual es el mayor")
Numero1 = int(input("Pon el primer numero "))
Numero2 = int(input("Pon el segundo numero "))

if Numero1 > Numero2:
    print(Numero1, "es mayor")
else:
    print(Numero2, "es mayor")

# E07
print("Identificador de años bisiestos")
año = int(input("Coloque el año "))

if año % 4 == 0:
    print("El año", año, "es bisiesto")
else:
    print("El año", año, "no bisiesto")

# E08

print("Detector de consonante o vocal")
letra = input("Pon la letra: ").lower()

if letra == "a":
    print("Es vocal")
elif letra == "e":
    print("Es vocal")
elif letra == "i":
    print("Es vocal")
elif letra == "o":
    print("Es vocal")
elif letra == "u":
    print("Es vocal")
else:
    print("Es consonante")

# E09

print("Para saber las sensacion relativa de temperatura")
temperatura = int(input("Coloca la temperatura en ºC: "))

if temperatura < 10:
    print("Frío")
elif temperatura > 25:
    print("Calor")
else:
    print("Templado")

# E10

print("Calculadora")

Numero1 = int(input())
Operador = input()
Numero2 = int(input())

if Operador == "+":
    print(Numero1+Numero2)
elif Operador == "-":
    print(Numero1-Numero2)
elif Operador == "/":
    print(Numero1/Numero2)
else:
    print(Numero1*Numero2)
    
