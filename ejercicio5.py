n = int(input("Ingrese un número: "))
suma_impares = 0
contador_impares = 0

for i in range(1, n+1, 2):
    suma_impares += i
    contador_impares += 1

print("La suma de todos los números impares desde 1 hasta", n, "es:", suma_impares)
print("Hay", contador_impares, "números impares en total.")