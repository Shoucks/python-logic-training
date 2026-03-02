# E02
#2.	Pide números hasta que el usuario escriba 0 y suma todos.

num = int(input("Escribe un numero del 0 al 9 "))

if num == 0:
    print("Correcto y el total de todos los numeros es", num)
else:
    num2 = int(input("Escribe otro numero "))
    suma = num + num2
    if num2 == 0:
        print("Correcto y el total de todos los numeros es", suma)
    else:
        num3 = int(input("Escribe otro numero ultimo intento "))
        suma2 = num + num2 + num3
        if num3 == 0:
            print("Correcto y el total de todos los numeros es", suma2)
        else:
            print("Error numero no encontrado")