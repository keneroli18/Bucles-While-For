n = int(input("Introduce un número: "))

suma = 0
contador = 0
i = 1
while i <= n:
    if i % 2 == 1:
        suma += i
        contador += 1
    i += 1

print("La suma de los números impares desde 1 hasta", n, "es:", suma)
print("Hay", contador, "números impares en total.")