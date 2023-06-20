notas = []
n = int(input("¿Cuántas notas quieres ingresar?: "))

for i in range(n):
    nota = float(input("Ingresa la nota {}: ".format(i+1)))
    notas.append(nota)

promedio = sum(notas) / n
print("El promedio del estudiante es:", promedio)