print("¡Bienvenido al conversor de longitud de Python!")
opcion = int(input("Qué deseas convertir?\n1.Metros\n2.Kilometros\n3.Centimetros\n"))
if opcion == 1:

 opcion = int(input("A que los desea convertir?\n1.kilometros\n2.Centimetros\n"))
 if opcion == 1:
          m = float(input("Ingrese los metros: "))
          km = m / 1000
          print(f"{m} metros a km son {km} Km")
 elif opcion == 2: 
        m = float(input("Ingrese los metros: "))
        cm = m * 100
        print(f"{m} metros a centimetros son {cm} centimetros")
elif opcion == 2:
      opcion = int(input("A que los desea convertir?\n1.Metros\n2.Centimetros\n"))
      if opcion == 1:
         km = float(input("Ingrese los Km: "))
         m = km * 1000
         print(f"{km} a metros son {m} metros")
      
      elif opcion == 2:
           km = float(input("Ingrese los Km: "))
           cm = km * 100000
           print(f"{km} kilometros a centimetros son {cm} centimetros")
elif opcion == 3:
      opcion = int(input("A que los desea convertir?\n1.Metros\n2.Kilometros\n"))
      if opcion == 1:
           cm = float(input("Ingrese los centimetros: "))
           m = cm / 100
           print(f"{cm} a metros son {m} metros")
      elif opcion == 2: 
           cm = float(input("Ingrese los centimetros"))
           km = cm / 100000
           print(f"{cm} a kilometros son {km} kilometros")
