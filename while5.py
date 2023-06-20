total = 0
monto = float(input("Ingrese el monto de la factura (0 para finalizar): "))
while monto != 0:
    total += monto
    monto = float(input("Ingrese el monto de la siguiente factura (0 para finalizar): "))

if total > 1000:
    descuento = total * 0.1
    total -= descuento
    print("El total a pagar es:", total, "(incluyendo un descuento del 10% por superar los $1000)")
else:
    print("El total a pagar es:", total)