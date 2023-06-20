n = int(input("¿Cuántas temperaturas quieres introducir?: "))

temperaturas = []
suma_temperaturas = 0

for i in range(n):
    temperatura = float(input("Introduce la temperatura {}: ".format(i+1)))
    temperaturas.append(temperatura)
    suma_temperaturas += temperatura

promedio = suma_temperaturas / n
temp_max = max(temperaturas)
temp_min = min(temperaturas)

print("La temperatura más alta es:", temp_max)
print("La temperatura más baja es:", temp_min)
print("La temperatura promedio es:", promedio)