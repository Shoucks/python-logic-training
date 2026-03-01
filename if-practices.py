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
    
# Bloque 02
# E01
print("Introduce una contraseña, debe tener minimo 8 caracteres y al menos un número ")
contraseña = input()

longitud = len(contraseña)

if any(c.isdigit() for c in contraseña) and longitud >= 8:
    print("Contraseña aseptada")
else:
    print("Contraseña no tiene minimo 8 caracteres o no contiene un número")
# No quedo muy claro como funciona pero dejo aqui la explicacion
# ¿Qué está pasando ahí dentro?
# for c in contraseña: Python va letra por letra de la palabra.
# c.isdigit(): Pregunta: "¿Es esta letra un número?".
# any(...): Si encuentra aunque sea un solo True en todo ese recorrido, te da el visto bueno.

# E02

edad = int(input("¿Cual es tu edad? "))
acompañante = input("¿Vienes acompañado? (Si o No) ")

if edad >= 18 or acompañante == "Si":
    print("Puedes pasar")
else:
    print("No puede pasar")

# E03

numero= int(input("Pon un numero entre 1 y 100 que sea par "))

if numero <= 100 and numero >= 1 and numero % 2 == 0:
    print("El es valido")
else:
    print("Numero incorrecto")

# E04

Cliente = input("¿Eres cliente vip? (si/no) ")
Compra = int(input("¿Cual es el monto de su compra? "))

if Cliente == "si" or Compra >= 100:
    print("A conseguido un descuento")
else:
    print("No hay descuento aplicable")

# E05
# in se usa para verificar si en la variable contiene ciertos caracteres
email = input("Introduce tu email ")

if "@" in email and "." in email:
    print("Email con formato correcto")
else:
    print("Email con formato incorrecto")

# E06

numero = int(input("Introduce un numero para comprobar si es divisible por 3 y 5 "))

if numero % 3 == 0 and numero % 5 ==0:
    print("El numero es divisible por 3 y 5")
else:
    print("El numero no es divisible por 3 o 5")

# E07

numero = int(input("Si colocas un numero entre 1900 y 2100 sera correcto "))

if numero <= 2100 and numero >= 1900:
    print("Correcto")
else:
    print("Incorrecto")

# E08

nombre = input("Introduce tu nombre")

if nombre == "" or len(nombre) <= 3:
    print("Esta vacio o nombre menor a 3 caracteres")
else:
    print("El nombre es correcto")

# E09
# un poco incongruente el ejercicio porque fallar 2 veces seguida y mas de 3 intentos es logica imposible con estos metodos actuales.

contraseña = input("Coloque la contraseña ")
pasw = "1234"
if contraseña == pasw:
    print("Contraseña correcta")
else:
    contraseña2 = input("Contraseña incorrecta, introdusca denuevo ")
    if contraseña2 == pasw:
        print("Contraseña correcta")
    else:
        print("Cuenta bloqueada")

# E10
# se puede mejora con != para negar los dias y poner como resultados inversos y con .lower() para volver minusculas la letras 
dia = input("Verificador de dia laboral (colocar en minuscula)")

if dia == "sabado" or dia == "domingo":
    print("Dia no laboral")
else:
    print("Dia laboral")

# Bloque 03
# E01

print("Seleccionador del mayor de 5 numeros")
num1 = int(input("Introduce el primer numero "))
num2 = int(input("Introduce el segundo numero "))
num3 = int(input("Introduce el tercer numero "))
num4 = int(input("Introduce el cuarto numero "))
num5 = int(input("Introduce el quinto numero "))

if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
    print(num1, "es el mayor")
elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
    print(num2, "es el mayor")
elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
    print(num3, "es el mayor")
elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
    print(num4, "es el mayor")
else:
    print(num5, "es el mayor")