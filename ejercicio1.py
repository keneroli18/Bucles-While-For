n = int(input("Ingrese el número de elementos a sumar: "))

suma = 0
for i in range(1, n+1):
    suma += i

print("La suma de los primeros", n, "números es:", suma)
