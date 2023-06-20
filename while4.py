num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 >= num2:
    print("El primer número debe ser menor que el segundo.")
else:
    i = num1
    while i <= num2:
        print(i)
        i += 1