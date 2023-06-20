n = int(input("Ingrese la cantidad de notas a promediar: "))
notas = []
i = 0
while i < n:
    nota = float(input("Ingrese la nota {}: ".format(i+1)))
    notas.append(nota)
    i += 1

promedio = sum(notas) / n
print("El promedio de las notas ingresadas es:", promedio)