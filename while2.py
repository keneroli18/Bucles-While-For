num = int(input("Introduce un número: "))

suma = 0
i = 0
while i <= num:
    if i % 2 == 0:
        suma += i
    i += 1

print("La suma de los números pares desde 0 hasta", num, "es:", suma)