saldo = int(input("Ingrese su saldo: "))
monto = int(input("Ingrese el monto a transferir: "))

if monto <= saldo:
    saldo = saldo - monto
    print("Transferencia realizada")
else:
    print("Saldo insuficiente")