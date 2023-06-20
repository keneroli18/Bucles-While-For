n = int(input("Ingrese la cantidad de estudiantes: "))
while n <= 0:
    n = int(input("La cantidad ingresada es inválida. Ingrese un número entero mayor que cero: "))

notas = []
for i in range(n):
    print("Ingrese las notas del estudiante", i+1)
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    notasEstudiante = [nota1, nota2, nota3]
    notas.append(notasEstudiante)

notasPlanas = [nota for sublist in notas for nota in sublist]
maxima = max(notasPlanas)
minima = min(notasPlanas)
promedio = sum(notasPlanas) / len(notasPlanas)

print("La nota más alta fue:", maxima)
print("La nota más baja fue:", minima)
print("El promedio de notas fue:", promedio)