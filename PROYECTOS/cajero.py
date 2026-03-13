saldo = 10000

while True:
    print("\n====CAJERO AUTOMATICO====")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Retirar dinero")
    print("4.Salir")
     
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        print("Tu saldo es: ",saldo)
    
    elif opcion =="2":
        monto = float(input("Ingrese monto a depositar: "))
        saldo += monto
        print ("Deposito realizado.")
    
    elif opcion == "3":
        monto = float(input("Ingrese el monto a retirar: "))
        if monto <= saldo:
            saldo -= monto
            print("Retiro realizado.")
        else:
            print("Monto no valido")
    elif opcion == "4":
        print("Ha salido del cajero.")
        break
    else:
        print("Opcion no valida.")
        
    