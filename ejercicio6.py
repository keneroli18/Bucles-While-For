num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 < num2:
    for i in range(num1, num2+1):
        print(i)
else:
    print("El primer número debe ser menor que el segundo.")