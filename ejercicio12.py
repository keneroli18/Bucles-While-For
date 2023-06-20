n = int(input("¿Cuántos estudiantes quieres evaluar?: "))
notas = []

for i in range(n):
    numNotas = int(input("¿Cuántas notas quieres introducir para el estudiante {}?: ".format(i+1)))
    while numNotas < 4:
        numNotas = int(input("Debes introducir al menos 4 notas. ¿Cuántas notas quieres introducir para el estudiante {}?: ".format(i+1)))
    notasEstudiante = []
    for j in range(numNotas):
        nota = float(input("Introduce la nota {}: ".format(j+1)))
        notasEstudiante.append(nota)
    notas.append(notasEstudiante)

promedios = []
for estudiante in notas:
    sumaNotas = sum(estudiante)
    promedioEstudiante = sumaNotas / len(estudiante)
    promedios.append(promedioEstudiante)

notasPlanas = [nota for estudiante in notas for nota in estudiante]
notaMaxima = max(notasPlanas)
notaMinima = min(notasPlanas)

print("La nota más alta es:", notaMaxima)
print("La nota más baja es:", notaMinima)
print("El promedio de las notas es:", sum(promedios) / len(promedios))