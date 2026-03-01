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