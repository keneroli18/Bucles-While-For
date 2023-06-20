suma = 0
numero = int(input("Ingrese un número entero (0 para finalizar): "))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número entero (0 para finalizar): "))

print("La sumatoria de los números ingresados es:", suma)