numero = int(input("Ingrese un número: "))

if numero > 10:
    resultado = 1
    for i in range(1, 11):
        resultado *= i
else:
    resultado = sum(range(1, numero+1))

print("El resultado es:", resultado)


    