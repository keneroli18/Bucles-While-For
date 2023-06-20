n = int(input("Ingrese la cantidad de temperaturas a ingresar: "))
while n <= 0:
    n = int(input("La cantidad ingresada es inválida. Ingrese un número entero mayor que cero: "))

temperaturas = []
for i in range(n):
    temperatura = float(input("Ingrese una temperatura en grados C: "))
    temperaturas.append(temperatura)

maxima = max(temperaturas)
minima = min(temperaturas)
promedio = sum(temperaturas) / n

print("La temperatura más alta fue:", maxima, "grados C")
print("La temperatura más baja fue:", minima, "grados C")
print("La temperatura promedio fue:", promedio, "grados C")