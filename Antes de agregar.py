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
    
