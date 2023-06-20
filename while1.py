num = int(input("Introduce un número: "))

if num > 10:
    resultado = 1
    i = 1
    while i <= 10:
        resultado *= i
        i += 1
else:
    resultado = 0
    i = 1
    while i <= 10:
        resultado += i
        i += 1

print("El resultado es:", resultado)